import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
from sklearn.decomposition import PCA

def radar_factory(num_vars, frame='circle'):
    """
    Create a radar chart with `num_vars` Axes.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding Axes.
    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):
        def transform_path_non_affine(self, path):
            # 如果插值步骤大于 1 ，则执行插值（为了避免 PolarTransform 自动转为圆弧）
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):
        name = 'radar'
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # 将第一个轴旋转到顶部
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """默认闭合折线"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """默认绘制闭合折线"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # 根据 frame 的类型返回不同的 patch
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=0.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                spine.set_transform(Affine2D().scale(0.5).translate(0.5, 0.5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta
def draw_radar_plot(column_names, values, title, save_path):
    """
    绘制单个雷达图

    参数:
      column_names: list，雷达图各轴的名称
      values: list，雷达图各轴对应的数值（顺序与 column_names 一致）
      title: str，图标题
      save_path: str，保存图像的路径（支持 png/pdf 等格式）
    """
    N = len(column_names)
    theta = radar_factory(N, frame='polygon')

    # 创建图和坐标系（注意 projection 使用我们注册的"radar"）
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))
    
    # 可根据数据范围设置合适的 rgrid（此处简单取 5 个刻度）
    ax.set_rgrids(np.linspace(min(values) * 0.9, max(values) * 1.1, 5))
    
    ax.set_varlabels(column_names)
    ax.plot(theta, values, color='b')
    ax.fill(theta, values, facecolor='b', alpha=0.25)
    
    ax.set_title(title, weight='bold', size='medium',
                 position=(0.5, 1.1),
                 horizontalalignment='center',
                 verticalalignment='center')

    fig.tight_layout()
    fig.savefig(save_path, dpi=600)  # Increased DPI to 600
    plt.close(fig)
    print(f"已保存雷达图： {save_path}")
def radar_plot_from_csv_file1(csv_path, system_val, model_val, save_path):
    # 若CSV文件分隔符不是逗号，请修改 sep 参数，例如 sep='\t'
    df = pd.read_csv(csv_path)
    
    # 按 system, model 过滤（这里假设 CSV 中字段名区分大小写）
    df_filtered = df[(df["system"] == system_val) & (df["model"] == model_val)]
    if df_filtered.empty:
        raise ValueError(f"CSV1中没有找到 system={system_val} 且 model={model_val} 的数据。")
    
    # 聚合所有不同的 category（即对所有满足条件的记录求平均）
    agg_data = df_filtered.mean(numeric_only=True)
    
    # 指定需要的列（注意字段名需与 CSV 中一致）
    columns_to_plot = [
        "Outline_domain", "Coverage_domain", "Structure_domain",
        "Relevance_domain", "Language_domain", "Criticalness_domain",
        "Reference_domain"
    ]
    
    # 计算平均值（如果聚合后的数据中不存在某列，会报 KeyError）
    values = [agg_data[col] for col in columns_to_plot]
    
    title = f"{system_val} - {model_val} (CSV1)"
    draw_radar_plot(columns_to_plot, values, title, save_path)
def radar_plot_from_csv_file2(csv_path, system_val, model_val, save_path):
    df = pd.read_csv(csv_path)
    
    df_filtered = df[(df["system"] == system_val) & (df["model"] == model_val)]
    if df_filtered.empty:
        raise ValueError(f"CSV2中没有找到 system={system_val} 且 model={model_val} 的数据。")
    
    agg_data = df_filtered.mean(numeric_only=True)
    
    columns_to_plot = [
        "Outline", "Coverage", "Structure",
        "Relevance", "Language", "Criticalness",
        "Reference"
    ]
    
    values = [agg_data[col] for col in columns_to_plot]
    
    title = f"{system_val} - {model_val} (CSV2)"
    draw_radar_plot(columns_to_plot, values, title, save_path)


def plot_survey_features(data, save_path=None):
    """
    Plot 7 radar charts, each showing 8 categories for one feature.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the survey features
    save_path : str, optional
        Path to save the figure. If None, the figure will be displayed.
    """
    # Set the style for academic publication
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_context("paper", font_scale=1.2)
    
    # Create figure with 7 subplots
    fig, axes = plt.subplots(3, 3, figsize=(15, 15), subplot_kw=dict(projection='polar'))
    fig.suptitle('Feature Distribution Across Categories', fontsize=16, y=0.95)
    
    # Add category labels
    categories = ['CS', 'Econ', 'EESS', 'Math', 'Physics', 'Q-Bio', 'Q-Fin', 'Stat']
    data['Category'] = categories
    
    # Define features
    features = ['Images_density', 'Equations_density', 'Tables_density', 'Citations_density',
                'Outline_no', 'Reference_no', 'Sentence_no']
    
    # Define pastel colors
    pastel_colors = ['#FFB3BA', '#BAFFC9', '#BAE1FF', '#FFFFBA', '#FFE4BA', '#E4BAFF', '#FFBAE4', '#BAFFE4']
    
    # Create angles for radar plot
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))  # complete the circle
    
    # Plot each feature
    for idx, feature in enumerate(features):
        row = idx // 3
        col = idx % 3
        ax = axes[row, col]
        
        # Get values for this feature
        values = data[feature].values
        values = np.concatenate((values, [values[0]]))  # complete the circle
        
        # Plot the radar
        ax.plot(angles, values, 'o-', linewidth=2, color='gray')
        ax.fill(angles, values, alpha=0.25, color='gray')
        
        # Set the labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=8)
        ax.set_title(feature, pad=20, size=12)
        
        # Add value labels
        for i, value in enumerate(values[:-1]):
            ax.text(angles[i], value, f'{value:.1f}', 
                   horizontalalignment='center', size=8)
    
    # Remove the unused subplot
    axes[2, 2].remove()
    
    # Adjust layout
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight',format='pdf')
    else:
        plt.show()

def plot_survey_small_multiples(data, save_path=None):
    """
    Plot small multiples horizontal bar plots showing categories for each metric.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the survey features
    save_path : str, optional
        Path to save the figure. If None, the figure will be displayed.
    """
    # Set the style for academic publication
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_context("paper", font_scale=1.2)
    
    # Define features and categories
    density_features = ['Images_density', 'Equations_density', 'Tables_density', 'Citations_density']
    count_features = ['Outline_no', 'Reference_no', 'Sentence_no']
    categories = ['CS', 'Econ', 'EESS', 'Math', 'Physics', 'Q-Bio', 'Q-Fin', 'Stat']
    
    # Create figure with subplots in two rows
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(15, 8))
    axes = axes.flatten()
    
    # Base cool color (blue)
    base_color = '#4B8BBE'
    
    # Plot density features
    for i, feature in enumerate(density_features):
        # Get values for this feature
        values = data[feature].values
        
        # Normalize values to 0-1 range for color intensity
        min_val = values.min()
        max_val = values.max()
        normalized_values = (values - min_val) / (max_val - min_val)
        
        # Create colors based on normalized values
        colors = [plt.cm.Blues(0.3 + 0.5 * val) for val in normalized_values]
        
        # Create horizontal bar plot with thinner bars
        bars = axes[i].barh(categories, values, color=colors, height=0.7)
        
        # Customize the plot
        axes[i].set_title(f'{feature}', pad=10, fontsize=16)
        # axes[i].set_xlabel('Value', fontsize=8)
        
        # Add value labels at the end of bars
        for bar in bars:
            width = bar.get_width()
            axes[i].text(width, bar.get_y() + bar.get_height()/2.,
                       f'{width:.1f}',
                       ha='left', va='center', fontsize=12)
        
        # Remove top and right spines
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)
        
        # Add grid lines
        axes[i].xaxis.grid(True, linestyle='--', alpha=0.3)
        axes[i].yaxis.grid(True, linestyle='--', alpha=0.3)
        axes[i].set_axisbelow(True)
        
        # Invert y-axis to have categories in the same order
        axes[i].invert_yaxis()
        
        # Adjust y-axis ticks to reduce spacing
        axes[i].set_yticks(np.arange(len(categories)))
        axes[i].set_yticklabels(categories, fontsize=12)
        
        # Adjust x-axis tick labels
        axes[i].tick_params(axis='x', labelsize=12)
        
        # Remove y-axis margin
        axes[i].margins(y=0.1)
    
    # Plot count features
    for i, feature in enumerate(count_features):
        # Get values for this feature
        values = data[feature].values
        
        # Normalize values to 0-1 range for color intensity
        min_val = values.min()
        max_val = values.max()
        normalized_values = (values - min_val) / (max_val - min_val)
        
        # Create colors based on normalized values
        colors = [plt.cm.Blues(0.3 + 0.5 * val) for val in normalized_values]
        
        # Create horizontal bar plot with thinner bars
        bars = axes[i+4].barh(categories, values, color=colors, height=0.7)
        
        # Customize the plot
        axes[i+4].set_title(f'{feature}', pad=10, fontsize=16)
        # axes[i+4].set_xlabel('Value', fontsize=8)
        
        # Add value labels at the end of bars
        for bar in bars:
            width = bar.get_width()
            axes[i+4].text(width, bar.get_y() + bar.get_height()/2.,
                       f'{width:.1f}',
                       ha='left', va='center', fontsize=12)
        
        # Remove top and right spines
        axes[i+4].spines['top'].set_visible(False)
        axes[i+4].spines['right'].set_visible(False)
        
        # Add grid lines
        axes[i+4].xaxis.grid(True, linestyle='--', alpha=0.3)
        axes[i+4].yaxis.grid(True, linestyle='--', alpha=0.3)
        axes[i+4].set_axisbelow(True)
        
        # Invert y-axis to have categories in the same order
        axes[i+4].invert_yaxis()
        
        # Adjust y-axis ticks to reduce spacing
        axes[i+4].set_yticks(np.arange(len(categories)))
        axes[i+4].set_yticklabels(categories, fontsize=12)
        
        # Adjust x-axis tick labels
        axes[i+4].tick_params(axis='x', labelsize=12)
        
        # Remove y-axis margin
        axes[i+4].margins(y=0.1)
    
    # Hide the last subplot
    axes[-1].set_visible(False)
    
    # Adjust layout
    plt.tight_layout()
    plt.suptitle('', fontsize=14, y=1.05)
    
    if save_path:
        plt.savefig(save_path, dpi=600, bbox_inches='tight',format='pdf')
    else:
        plt.show()

def plot_result_heatmap(csv_path, systems, save_path=None):
    df = pd.read_csv(csv_path)
    col_names = [
        "Outline", "Outline_coverage", "Outline_structure",
        "Coverage", "Structure", "Relevance", "Language",
        "Criticalness", "Faithfulness", "Reference", "Reference_quality"
    ]
    
    # 创建列名到显示名的映射
    display_name_map = {
        "Outline": "Outline Quality",
        "Outline_coverage": "Outline Coverage",
        "Outline_structure": "Outline Structure",
        "Coverage": "Coverage",
        "Structure": "Structure",
        "Relevance": "Relevance",
        "Language": "Language",
        "Criticalness": "Criticalness",
        "Faithfulness": "Faithfulness",
        "Reference": "Reference Quality",
        "Reference_quality": "Reference Supportiveness"
    }
    
    # 判断哪些列带_domain
    domain_cols = [c+"_domain" for c in ["Outline", "Coverage", "Structure", "Relevance", "Language", "Criticalness", "Reference"]]
    col_map = {}
    for c in col_names:
        if c in ["Outline", "Coverage", "Structure", "Relevance", "Language", "Criticalness", "Reference"]:
            if c+"_domain" in df.columns:
                col_map[c] = c+"_domain"
            else:
                col_map[c] = c
        else:
            col_map[c] = c
    plot_cols = [col_map[c] for c in col_names if col_map[c] in df.columns]

    # 找出所有 domain/category
    if "category" in df.columns:
        domains = df["category"].unique()
        domain_label = "category"
    elif "domain" in df.columns:
        domains = df["domain"].unique()
        domain_label = "domain"
    else:
        raise ValueError("No category/domain column found in csv.")

    n_domains = len(domains)

    # 画图
    fig, axes = plt.subplots(1, n_domains, figsize=(2.2*n_domains, 6), sharey=False)
    if n_domains == 1:
        axes = [axes]
    for i, domain in enumerate(domains):
        ax = axes[i]
        subdf = df[df[domain_label] == domain]
        subdf = subdf.set_index("system")
        # 关键：reindex 保证所有 system 都有一行，没数据自动 NaN
        data = subdf.reindex(systems)[plot_cols]

        # 每列独立归一化
        normed = data.copy()
        for col in normed.columns:
            if col.endswith("_domain"):
                normed[col] = (normed[col] - 1) / 4  # 1-5归一化到0-1
            else:
                normed[col] = normed[col] / 100      # 0-100归一化到0-1

        # Create a mask for zero values and NaN
        zero_mask = (normed == 0) | normed.isnull()

        if i == 0:
            yticklabels = True
        else:
            yticklabels = False
        sns.heatmap(
            normed,
            ax=ax,
            cmap="coolwarm",
            cbar=False,
            annot=False,
            linewidths=0.5,
            linecolor='gray',
            xticklabels=True,
            yticklabels=yticklabels,
            square=True,
            alpha=0.5,
            mask=zero_mask,  # Mask zero values and NaN
            vmin=0,
            vmax=1
        )
        
        # Fill masked areas with darker gray
        ax.patch.set(hatch='', facecolor='#d0d0d0')
        
        # 使用display_name_map来设置显示名称
        display_labels = [display_name_map[col.replace('_domain', '')] for col in plot_cols]
        ax.set_xticklabels(display_labels, rotation=90, fontsize=10)
        # 在 Outline 和 Content 之间、Content 和 Reference 之间添加分隔线
        outline_end = 3  # Outline 相关列数
        content_end = 9  # Content 相关列数
        ax.axvline(x=outline_end, color='black', linestyle='--', linewidth=1)
        ax.axvline(x=content_end, color='black', linestyle='--', linewidth=1)
        ax.set_xlabel(domain, fontsize=12, labelpad=20)
        ax.set_ylabel("")

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()

def plot_category_density_heatmap(csv_path, systems, save_path=None):
    """
    Plot a normalized heatmap of density metrics and similarity scores for each category.
    
    Parameters:
    -----------
    csv_path : str
        Path to the CSV file containing the data
    systems : list
        List of systems to include in the heatmap
    save_path : str, optional
        Path to save the figure. If None, the figure will be displayed.
    """
    df = pd.read_csv(csv_path)
    
    # Get density columns
    density_cols = [col for col in df.columns if col.endswith('_density')]
    
    # Calculate similarity scores
    pdfs_rows = df[df['system'] == 'pdfs'].set_index('model')
    
    def compute_l2(row):
        if row['system'] == 'pdfs':
            return 1.0
        model = row['model']
        if model not in pdfs_rows.index:
            return np.nan
        pdfs_density = pdfs_rows.loc[model, density_cols].astype(float)
        rel = row[density_cols].astype(float)
        l2 = np.sqrt(np.sum((rel - 1) ** 2))
        score = 1 / (1 + l2)
        return score
    
    df['Similarity_score'] = df.apply(compute_l2, axis=1)
    
    # Get unique categories
    categories = df['category'].unique()
    
    # Create figure with subplots for each category
    fig, axes = plt.subplots(1, len(categories), figsize=(2.2*len(categories), 6), sharey=True)
    if len(categories) == 1:
        axes = [axes]
    
    # Plot heatmap for each category
    for i, category in enumerate(categories):
        ax = axes[i]
        subdf = df[df['category'] == category]
        subdf = subdf.set_index('system')
        
        # Filter out pdfs and reindex to ensure all systems are included
        plot_systems = [sys for sys in systems if sys != 'pdfs']
        data = subdf.reindex(plot_systems)[density_cols + ['Similarity_score']]
        
        # Keep original values but clip similarity score to 0-1 range
        normed = data.copy()
        normed['Similarity_score'] = normed['Similarity_score'].clip(0, 1)
        
        # Create a mask for zero values and NaN
        zero_mask = (normed == 0) | normed.isnull()
        
        # Create heatmap with vmin=0 and vmax=2
        sns.heatmap(
            normed,
            ax=ax,
            cmap="coolwarm",
            cbar=False,
            annot=False,
            linewidths=0.5,
            linecolor='gray',
            xticklabels=True,
            yticklabels=False,
            square=True,
            alpha=0.5,
            mask=zero_mask,  # Mask zero values and NaN
            vmin=0,
            vmax=2
        )
        
        # Fill masked areas with darker gray
        ax.patch.set(hatch='', facecolor='#d0d0d0')
        
        # Set labels
        display_labels = [col.replace('_density', '') for col in density_cols] + ['Similarity']
        ax.set_xticklabels(display_labels, rotation=90, fontsize=10)
        
        # Add vertical separator before similarity score
        ax.axvline(x=len(density_cols), color='black', linestyle='-', linewidth=1)
        
        ax.set_xlabel(category, fontsize=12, labelpad=20)
        ax.set_ylabel("")
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()

def plot_category_density_heatmap_horizontal(csv_path, systems, save_path=None):
    """
    Plot a combined heatmap where:
      - The rows are the metric names (density metrics and similarity score).
      - The columns are system names. The columns from each category (domain) are placed 
        as separate blocks arranged horizontally.
      - Vertical dashed lines separate the category blocks and annotate the block with
        its category name.
      - Horizontal dashed line separates similarity score from density metrics.
      - Different color scales for similarity (0-0.5) and other metrics (0-2).
      
    The plotting settings (color, font sizes, linewidths, alpha, masked area color, etc.)
    strictly follow the original code.
    
    Parameters:
    -----------
    csv_path : str
        Path to the CSV file containing the data.
    systems : list
        List of system names to include as columns (e.g., including "pdfs" as reference if present).
        Note: The data for the "pdfs" system is used only as a reference for 
        computing Similarity_score.
    save_path : str, optional
        Path to save the figure. If None, the figure will be displayed.
    """
    # -------------------------------------------------------------------------
    # 1. Load CSV and compute similarity scores (same as original code)
    # -------------------------------------------------------------------------
    df = pd.read_csv(csv_path)
    
    # Identify density columns: those ending with "_density"
    density_cols = [col for col in df.columns if col.endswith('_density')]
    
    # Use rows from system "pdfs" as reference for computing similarity.
    pdfs_rows = df[df['system'] == 'pdfs'].set_index('model')
    
    def compute_l2(row):
        if row['system'] == 'pdfs':
            return 1.0
        model = row['model']
        if model not in pdfs_rows.index:
            return np.nan
        pdfs_density = pdfs_rows.loc[model, density_cols].astype(float)
        rel = row[density_cols].astype(float)
        l2 = np.sqrt(np.sum((rel - 1) ** 2))
        score = 1 / (1 + l2)
        return score
    
    df['Similarity_score'] = df.apply(compute_l2, axis=1)
    
    # -------------------------------------------------------------------------
    # 2. Prepare blocks for each category (domain)
    # -------------------------------------------------------------------------
    # Exclude "pdfs" from plotting (its row is only used as a reference).
    plot_systems = [s for s in systems if s != 'pdfs']
    
    categories = df['category'].unique()  # preserve original order
    blocks = []
    category_system_counts = {}  # Track number of systems per category
    
    # For each category, filter & reindex the data, then transpose 
    # so that rows become metric names and columns are systems.
    for cat in categories:
        if cat == 'cs':
            # Original logic for cs category
            subdf = df[df['category'] == cat].set_index('system')
            data = subdf.reindex(plot_systems)[density_cols + ['Similarity_score']]
            category_system_counts[cat] = len(plot_systems)
        else:
            # Modified logic for other categories - exclude AutoSurvey and SurveyForge
            filtered_systems = [s for s in plot_systems if s not in ['AutoSurvey', 'SurveyForge']]
            subdf = df[df['category'] == cat].set_index('system')
            data = subdf.reindex(filtered_systems)[density_cols + ['Similarity_score']]
            category_system_counts[cat] = len(filtered_systems)
        
        # Transpose: now rows are metrics and columns are system names.
        block = data.T.copy()
        # Rename row labels (e.g., "outline_density" becomes "outline", "Similarity_score" becomes "Similarity")
        metric_names = [col.replace('_density', '') for col in density_cols] + ['Similarity']
        block.index = metric_names
        blocks.append(block)
    
    # Horizontally concatenate the blocks. By using keys=categories the resulting columns
    # will be a MultiIndex where level 0 indicates the category.
    combined_df = pd.concat(blocks, axis=1, keys=categories)
    # For plotting purposes (and to mimic your original x tick labels),
    # flatten the MultiIndex and keep only the system names.
    combined_df.columns = combined_df.columns.get_level_values(1)
    
    # -------------------------------------------------------------------------
    # 3. Create a mask for zero values and NaNs (to be displayed in darker gray)
    # -------------------------------------------------------------------------
    mask = (combined_df == 0) | (combined_df.isna())
    
    # Create colormap following original code: "coolwarm" with masked values shown in #d0d0d0
    cmap = sns.color_palette("coolwarm", as_cmap=True)
    cmap.set_bad(color="#d0d0d0")
    
    # -------------------------------------------------------------------------
    # 4. Plot the combined heatmap
    # -------------------------------------------------------------------------
    # Figure size is set to 2.2 inches per category (as in your original subplot width)
    fig_width = 2.2 * len(categories)  
    fig, ax = plt.subplots(figsize=(fig_width, 6))
    
    # Create a copy of the data for plotting
    plot_data = combined_df.copy()
    
    # Normalize similarity scores to 0-2 range for consistent coloring
    similarity_mask = plot_data.index == 'Similarity'
    plot_data.loc[similarity_mask] = plot_data.loc[similarity_mask] * 4  # Scale 0-0.5 to 0-2
    
    sns.heatmap(
        plot_data,
        ax=ax,
        cmap=cmap,
        cbar=False,
        annot=combined_df,  # Use original values for annotation
        fmt='.2f',  # Format annotations to 2 decimal places
        linewidths=0.5,
        linecolor='gray',
        xticklabels=True,
        yticklabels=True,
        square=True,
        alpha=0.5,
        mask=mask,
        vmin=0,
        vmax=2
    )
    
    # Add horizontal dashline to separate similarity score
    ax.axhline(y=len(density_cols), color='black', linestyle='--', linewidth=1)
    
    # Adjust x tick labels: system names rotated 90 degrees with fontsize=10.
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=10)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=10)
    
    # -------------------------------------------------------------------------
    # 5. Draw vertical dashed lines to separate category blocks and annotate each block
    # -------------------------------------------------------------------------
    # Calculate cumulative positions for category boundaries
    current_pos = 0
    for i, cat in enumerate(categories):
        if i > 0:  # Skip first category (no line needed at start)
            # Draw vertical dashed line at the boundary
            ax.axvline(x=current_pos, color='black', linestyle='--', linewidth=1)
        
        # Calculate midpoint for category label
        x_mid = current_pos + category_system_counts[cat] / 2.0
        
        # Add category label with adjusted position
        ax.text(
            x_mid,
            -0.5,  # Increased offset to move labels lower
            cat,
            ha='center',
            va='bottom',
            fontsize=12,
            transform=ax.get_xaxis_transform()
        )
        
        # Update position for next category
        current_pos += category_system_counts[cat]
    
    # Remove x and y labels
    ax.set_xlabel("")
    ax.set_ylabel("")
    
    # Fill masked areas with a darker gray (per original code)
    ax.patch.set(hatch='', facecolor='#d0d0d0')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()
    
def combined_radar_plots(csv_path1, csv_path2, save_path, system_name_map=None):
    """
    根据两个 CSV 文件的数据绘制聚合雷达图，
    左边显示 CSV1 中所有系统的数据，右边显示 CSV2 中所有系统的数据。
    每个系统用不同颜色表示，雷达图维度固定为 0-5。

    参数:
        csv_path1: str, 第一个CSV文件的路径
        csv_path2: str, 第二个CSV文件的路径
        save_path: str, 保存图像的路径
        system_name_map: dict, 系统名称映射字典，key是原始系统名，value是显示的系统名
    """
    # ------------------
    # 读取 CSV1 并计算聚合数据
    # ------------------
    df1 = pd.read_csv(csv_path1)
    cols1 = [
        "Outline_domain", "Coverage_domain", "Structure_domain",
        "Relevance_domain", "Language_domain", "Criticalness_domain",
        "Reference_domain"
    ]
    
    # ------------------
    # 读取 CSV2 并计算聚合数据
    # ------------------
    df2 = pd.read_csv(csv_path2)
    cols2 = [
        "Outline", "Coverage", "Structure",
        "Relevance", "Language", "Criticalness",
        "Reference"
    ]
    
    # ------------------
    # 构造组合图：一行两列的子图，每个子图采用雷达坐标系
    # ------------------
    N = 7  # 两个图中需要展示的轴数
    theta = radar_factory(N, frame='polygon')
    
    fig, axs = plt.subplots(1, 2, figsize=(15, 7),
                            subplot_kw=dict(projection='radar'))
    
    # 获取需要显示的系统名称
    if system_name_map is None:
        systems1 = df1['system'].unique()
        systems2 = df2['system'].unique()
    else:
        systems1 = [sys for sys in system_name_map.keys() if sys in df1['system'].unique()]
        systems2 = [sys for sys in system_name_map.keys() if sys in df2['system'].unique()]
    
    # 为所有系统生成统一的颜色映射
    all_systems = np.unique(np.concatenate([systems1, systems2]))
    colors = plt.cm.Set2(np.linspace(0, 1, len(all_systems)))
    color_dict = dict(zip(all_systems, colors))
    
    # 左图：CSV1 数据
    ax1 = axs[0]
    # 调整数值范围以放大差异
    ax1.set_rgrids([1,2,3,4,5])
    ax1.set_ylim(1.0, 5.0)
    
    for system in systems1:
        df_filtered = df1[df1["system"] == system]
        agg_data = df_filtered.mean(numeric_only=True)
        values = [agg_data[col] for col in cols1]
        # 使用统一的颜色映射
        display_name = system_name_map[system] if system_name_map else system
        ax1.plot(theta, values, color=color_dict[system], label=display_name)
        ax1.fill(theta, values, facecolor=color_dict[system], alpha=0.3)
    
    ax1.set_varlabels(cols1)
    ax1.set_title("Area-aware ASG-Bench", weight='bold', size='medium')
    
    # 右图：CSV2 数据
    ax2 = axs[1]
    # 调整数值范围以放大差异
    ax2.set_rgrids([1,2,3,4,5])
    ax2.set_ylim(1.0, 5.0)
    
    for system in systems2:
        df_filtered = df2[df2["system"] == system]
        agg_data = df_filtered.mean(numeric_only=True)
        values = [agg_data[col] for col in cols2]
        # 使用统一的颜色映射
        display_name = system_name_map[system] if system_name_map else system
        ax2.plot(theta, values, color=color_dict[system], label=display_name)
        ax2.fill(theta, values, facecolor=color_dict[system], alpha=0.3)
    
    ax2.set_varlabels(cols2)
    ax2.set_title("ASG-Bench", weight='bold', size='medium')
    
    # 在图形右侧添加一个统一的图例
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0.98, 0.5))
    
    fig.suptitle("",
                 weight='bold', size='large', y=0.98)
    fig.tight_layout(rect=[0, 0, 0.9, 0.95])  # 为右侧图例留出空间
    
    # 保存为 PDF 文件，增加 DPI
    fig.savefig(save_path, format="pdf", dpi=600, bbox_inches='tight')
    plt.close(fig)
    print(f"组合图已保存为： {save_path}")

def domain_radar_plots(domain, model_name, system_name_map, save_path):
    """
    Draw radar plots for a specific domain, showing domain-specific metrics on the left
    and general metrics on the right.

    Parameters:
    -----------
    domain : str
        The domain name (e.g., 'cs')
    model_name : str
        The model name to filter data for
    system_name_map : dict
        Dictionary mapping system names to display names
    save_path : str
        Path to save the output figure
    """
    # Read the domain-specific CSV file
    csv_path = f"surveys/{domain}/{domain}_average.csv"
    df = pd.read_csv(csv_path)
    
    # Filter data for the specified model
    df = df[df["model"] == model_name]
    
    # Define columns for domain-specific and general metrics
    domain_cols = [
        "Outline_domain", "Coverage_domain", "Structure_domain",
        "Relevance_domain", "Language_domain", "Criticalness_domain",
        "Reference_domain"
    ]
    
    general_cols = [
        "Outline", "Coverage", "Structure",
        "Relevance", "Language", "Criticalness",
        "Reference"
    ]
    
    # Create the figure with two subplots
    N = 7  # Number of axes in each radar plot
    theta = radar_factory(N, frame='polygon')
    
    fig, axs = plt.subplots(1, 2, figsize=(15, 7),
                            subplot_kw=dict(projection='radar'))
    
    # Get systems to display
    systems = [sys for sys in system_name_map.keys() if sys in df['system'].unique()]
    
    # Generate colors for systems
    colors = plt.cm.Set2(np.linspace(0, 1, len(systems)))
    color_dict = dict(zip(systems, colors))
    
    # Left plot: Domain-specific metrics
    ax1 = axs[0]
    ax1.set_rgrids([1,2,3,4,5])
    ax1.set_ylim(1.0, 5.0)
    
    for system in systems:
        df_filtered = df[df["system"] == system]
        agg_data = df_filtered.mean(numeric_only=True)
        values = [agg_data[col] for col in domain_cols]
        display_name = system_name_map[system]
        ax1.plot(theta, values, color=color_dict[system], label=display_name)
        ax1.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    ax1.set_varlabels([col.replace('_domain', '') for col in domain_cols])
    ax1.set_title(f"{domain.upper()} Domain Metrics", weight='bold', size='medium')
    
    # Right plot: General metrics
    ax2 = axs[1]
    ax2.set_rgrids([1,2,3,4,5])
    ax2.set_ylim(1.0, 5.0)
    
    for system in systems:
        df_filtered = df[df["system"] == system]
        agg_data = df_filtered.mean(numeric_only=True)
        values = [agg_data[col] for col in general_cols]
        display_name = system_name_map[system]
        ax2.plot(theta, values, color=color_dict[system], label=display_name)
        ax2.fill(theta, values, facecolor=color_dict[system], alpha=0.3)
    
    ax2.set_varlabels(general_cols)
    ax2.set_title("General Metrics", weight='bold', size='medium')
    
    # Add legend
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0.98, 0.5))
    
    # Add title
    fig.suptitle(f"{domain.upper()} Domain Analysis - {model_name}",
                 weight='bold', size='large', y=0.98)
    
    # Adjust layout
    fig.tight_layout(rect=[0, 0, 0.9, 0.95])
    
    # Save figure
    fig.savefig(save_path, format="pdf", dpi=600, bbox_inches='tight')
    plt.close(fig)
    print(f"Domain radar plots saved to: {save_path}")

def metrics_radar_plots(csv_path, model_name, system_name_map, save_path, metrics=None):
    """
    Draw radar plots for specific metrics from a CSV file.

    Parameters:
    -----------
    csv_path : str
        Path to the CSV file containing the data
    model_name : str
        The model name to filter data for
    system_name_map : dict
        Dictionary mapping system names to display names
    save_path : str
        Path to save the output figure
    metrics : list, optional
        List of metrics to plot. If None, uses default metrics:
        ["Outline_coverage", "Outline_structure", "Faithfulness", "Reference_quality"]
    """
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Filter data for the specified model
    df = df[df["model"] == model_name]
    
    # Define default metrics if none provided
    if metrics is None:
        metrics = [
            "Outline_coverage", 
            "Outline_structure", 
            "Faithfulness", 
            "Reference_quality"
        ]
    
    # Create the figure with radar projection
    N = len(metrics)  # Number of axes in radar plot
    theta = radar_factory(N, frame='polygon')
    
    fig, ax = plt.subplots(figsize=(10, 10),
                          subplot_kw=dict(projection='radar'))
    
    # Get systems to display
    systems = [sys for sys in system_name_map.keys() if sys in df['system'].unique()]
    
    # Generate colors for systems
    colors = plt.cm.Set2(np.linspace(0, 1, len(systems)))
    color_dict = dict(zip(systems, colors))
    
    # Plot data for each system
    for system in systems:
        df_filtered = df[df["system"] == system]
        agg_data = df_filtered.mean(numeric_only=True)
        values = [agg_data[metric] for metric in metrics]
        # 处理小于最小值的数值
        values = [max(50, v) for v in values]  # 将小于50的值设为50
        display_name = system_name_map[system]
        ax.plot(theta, values, color=color_dict[system], label=display_name)
        ax.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    # Set labels and title
    ax.set_varlabels(metrics)
    ax.set_title("Metrics Comparison", weight='bold', size='medium')
    
    # Set grid and limits
    ax.set_rgrids([60, 70, 80, 90, 100])
    ax.set_ylim(50, 100)
    
    # Add legend
    ax.legend(loc='upper right', bbox_to_anchor=(0.3, 0.3))
    
    # Add title
    fig.suptitle(f"Metrics Analysis - {model_name}",
                 weight='bold', size='large', y=0.98)
    
    # Adjust layout
    fig.tight_layout()
    
    # Save figure
    fig.savefig(save_path, format="pdf", dpi=600, bbox_inches='tight')
    plt.close(fig)
    print(f"Metrics radar plot saved to: {save_path}")

def combined_all_radar_plots(domain, model_name, system_name_map_row1, system_name_map_row2, save_path):
    """
    Combine radar plots in a 1x3 layout with consistent color mapping across all systems.

    Parameters:
    -----------
    domain : str
        The domain name (e.g., 'cs')
    model_name : str
        The model name to filter data for
    system_name_map_row1 : dict
        Dictionary mapping system names to display names for the first row
    system_name_map_row2 : dict
        Dictionary mapping system names to display names for the second row
    save_path : str
        Path to save the output figure
    """
    # Read all necessary CSV files
    df1 = pd.read_csv("surveys/all_categories_results_reorganized.csv")
    df2 = pd.read_csv("surveys/global_average_reorganized.csv")
    df3 = pd.read_csv(f"surveys/{domain}/{domain}_average.csv")
    
    # Filter data for the specified model
    df1 = df1[df1["model"] == model_name]
    df2 = df2[df2["model"] == model_name]
    df3 = df3[df3["model"] == model_name]
    
    # Define columns for different plots
    domain_cols = [
        "Outline_domain", "Coverage_domain", "Structure_domain",
        "Relevance_domain", "Language_domain", "Criticalness_domain",
        "Reference_domain"
    ]
    
    general_cols = [
        "Outline", "Coverage", "Structure",
        "Relevance", "Language", "Criticalness",
        "Reference"
    ]
    
    # Calculate the new dimension
    density_cols = ["Images_density", "Equations_density", "Tables_density", "Citations_density", "Claim_density"]
    df1['Informativeness'] = df1[density_cols].mean(axis=1).apply(lambda x: 5 if x > 1 else x * 5)
    df2['Informativeness'] = df2[density_cols].mean(axis=1).apply(lambda x: 5 if x > 1 else x * 5)
    df3['Informativeness'] = df3[density_cols].mean(axis=1).apply(lambda x: 5 if x > 1 else x * 5)
    
    # Add the new dimension to the columns
    domain_cols.append("Informativeness")
    general_cols.append("Informativeness")
    
    # Create the figure with three subplots
    N = 8  # Number of axes in each radar plot
    theta = radar_factory(N, frame='polygon')
    
    fig, axs = plt.subplots(1, 3, figsize=(20, 7),
                           subplot_kw=dict(projection='radar'))
    
    # Get all unique systems from both maps
    all_systems = list(set(list(system_name_map_row1.keys()) + list(system_name_map_row2.keys())))
    
    # Generate colors for all systems
    colors = plt.cm.Set2(np.linspace(0, 1, len(all_systems)))
    color_dict = dict(zip(all_systems, colors))
    
    # Left: Domain-specific metrics (moved from right)
    ax1 = axs[0]
    ax1.set_rgrids([1,2,3,4,5])
    ax1.set_ylim(1.0, 5.0)
    ax1.tick_params(axis='both', which='major', labelsize=14)
    
    for system in system_name_map_row2.keys():
        if system in df3['system'].unique():
            df_filtered = df3[df3["system"] == system]
            agg_data = df_filtered.mean(numeric_only=True)
            values = [agg_data[col] for col in domain_cols]
            display_name = system_name_map_row2[system]
            linewidth = 3 if system == "pdfs" else 0.5
            ax1.plot(theta, values, color=color_dict[system], label=display_name, linewidth=linewidth)
            ax1.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    ax1.set_varlabels([col.replace('_domain', '') for col in domain_cols])
    
    # Middle: Area-aware ASG-Bench
    ax2 = axs[1]
    ax2.set_rgrids([1,2,3,4,5])
    ax2.set_ylim(1.0, 5.0)
    ax2.tick_params(axis='both', which='major', labelsize=14)
    
    for system in system_name_map_row1.keys():
        if system in df1['system'].unique():
            df_filtered = df1[df1["system"] == system]
            agg_data = df_filtered.mean(numeric_only=True)
            values = [agg_data[col] for col in domain_cols]
            display_name = system_name_map_row1[system]
            linewidth = 3 if system == "pdfs" else 0.5
            ax2.plot(theta, values, color=color_dict[system], label=display_name, linewidth=linewidth)
            ax2.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    ax2.set_varlabels([col.replace('_domain', '') for col in domain_cols])
    
    # Right: ASG-Bench
    ax3 = axs[2]
    ax3.set_rgrids([1,2,3,4,5])
    ax3.set_ylim(1.0, 5.0)
    ax3.tick_params(axis='both', which='major', labelsize=14)
    
    for system in system_name_map_row1.keys():
        if system in df2['system'].unique():
            df_filtered = df2[df2["system"] == system]
            agg_data = df_filtered.mean(numeric_only=True)
            values = [agg_data[col] for col in general_cols]
            display_name = system_name_map_row1[system]
            linewidth = 3 if system == "pdfs" else 0.5
            ax3.plot(theta, values, color=color_dict[system], label=display_name, linewidth=linewidth)
            ax3.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    ax3.set_varlabels(general_cols)
    
    # Add a single legend for all systems
    handles, labels = [], []
    for system in all_systems:
        if system in system_name_map_row1:
            display_name = system_name_map_row1[system]
        else:
            display_name = system_name_map_row2[system]
        handles.append(plt.Line2D([0], [0], color=color_dict[system], label=display_name))
        labels.append(display_name)
    
    fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0.9, -0.05), fontsize=12)
    
    # Adjust layout
    fig.tight_layout(rect=[0, 0, 0.9, 0.95])
    
    # Save figure
    fig.savefig(save_path, format="pdf", dpi=600, bbox_inches='tight')
    plt.close(fig)
    print(f"Combined radar plots saved to: {save_path}")

def combined_domain_radar_plots(domain, model_name, system_name_map_row1, system_name_map_row2, save_path):
    # Read all necessary CSV files
    df1 = pd.read_csv("surveys/all_categories_results_reorganized.csv")
    df2 = pd.read_csv("surveys/global_average_reorganized.csv")
    df3 = pd.read_csv(f"surveys/{domain}/{domain}_average.csv")
    
    # Filter data for the specified model
    df1 = df1[df1["model"] == model_name]
    df2 = df2[df2["model"] == model_name]
    df3 = df3[df3["model"] == model_name]
    
    # Define columns for different plots
    domain_cols = [
        "Outline_domain", "Coverage_domain", "Structure_domain",
        "Relevance_domain", "Language_domain", "Criticalness_domain",
        "Reference_domain"
    ]
    
    general_cols = [
        "Outline", "Coverage", "Structure",
        "Relevance", "Language", "Criticalness",
        "Reference"
    ]
    
    # Calculate the new dimension
    density_cols = ["Images_density", "Equations_density", "Tables_density", "Citations_density", "Claim_density"]
    df1['Informativeness'] = df1[density_cols].mean(axis=1).apply(lambda x: 5 if x > 1 else x * 5)
    df2['Informativeness'] = df2[density_cols].mean(axis=1).apply(lambda x: 5 if x > 1 else x * 5)
    df3['Informativeness'] = df3[density_cols].mean(axis=1).apply(lambda x: 5 if x > 1 else x * 5)
    
    # Add the new dimension to the columns
    domain_cols.append("Informativeness")
    general_cols.append("Informativeness")
    
    # Create the figure with two subplots
    N = 8  # Number of axes in each radar plot
    theta = radar_factory(N, frame='polygon')
    
    fig, axs = plt.subplots(1, 2, figsize=(15, 7),
                           subplot_kw=dict(projection='radar'))
    
    # Get all unique systems from both maps
    all_systems = list(set(list(system_name_map_row1.keys()) + list(system_name_map_row2.keys())))
    
    # Generate colors for all systems
    colors = plt.cm.Set2(np.linspace(0, 1, len(all_systems)))
    color_dict = dict(zip(all_systems, colors))
    
    # First plot: Middle chart from combined_all_radar_plots
    ax1 = axs[0]
    ax1.set_rgrids([1,2,3,4,5])
    ax1.set_ylim(1.0, 5.0)
    
    for system in system_name_map_row1.keys():
        if system in df1['system'].unique():
            df_filtered = df1[df1["system"] == system]
            agg_data = df_filtered.mean(numeric_only=True)
            values = [agg_data[col] for col in domain_cols]
            display_name = system_name_map_row1[system]
            linewidth = 3 if system == "pdfs" else 0.5
            ax1.plot(theta, values, color=color_dict[system], label=display_name, linewidth=linewidth)
            ax1.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    ax1.set_varlabels([col.replace('_domain', '') for col in domain_cols])
    ax1.tick_params(axis='both', which='major', labelsize=20)
    # for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    #     label.set_fontweight('bold')  # 设置字体加粗
    
    # Second plot: 8 domains with calculated values
    ax2 = axs[1]
    ax2.set_rgrids([1,2,3,4,5])
    ax2.set_ylim(1.0, 5.0)
    
    domains = df1["category"].unique()
    for system in system_name_map_row1.keys():
        if system in df1['system'].unique():
            df_filtered = df1[df1["system"] == system]
            values = []
            for d in domains:
                domain_data = df_filtered[df_filtered["category"] == d]
                domain_avg = domain_data[domain_cols].mean().mean()
                additional_avg = domain_data[["Outline_coverage", "Outline_structure", "Faithfulness", "Reference_quality"]].mean().mean()
                values.append((domain_avg + additional_avg) / 20)
            display_name = system_name_map_row1[system]
            linewidth = 3 if system == "pdfs" else 0.5
            ax2.plot(theta, values, color=color_dict[system], label=display_name, linewidth=linewidth)
            ax2.fill(theta, values, facecolor=color_dict[system], alpha=0.15)
    
    ax2.set_varlabels(domains)
    ax2.tick_params(axis='both', which='major', labelsize=20)
    # for label in ax2.get_xticklabels() + ax2.get_yticklabels():
    #     label.set_fontweight('bold')  # 设置字体加粗

    
    # Add a single legend for all systems
    handles, labels = [], []
    for system in all_systems:
        if system in system_name_map_row1:
            display_name = system_name_map_row1[system]
        else:
            display_name = system_name_map_row2[system]
        handles.append(plt.Line2D([0], [0], color=color_dict[system], label=display_name))
        labels.append(display_name)
    
    fig.legend(handles, labels, loc='lower right', bbox_to_anchor=(0.9, -0.3), fontsize=20)
    
    # Adjust layout
    fig.tight_layout(rect=[0, 0, 0.9, 0.95])
    
    # Save figure
    fig.savefig(save_path, format="pdf", dpi=600, bbox_inches='tight')
    plt.close(fig)
    print(f"Combined domain radar plots saved to: {save_path}")
def calc_similarity_score(csv_path, output_path):
    df = pd.read_csv(csv_path)
    density_cols = [col for col in df.columns if col.endswith('_density')]

    # 先构建一个 (model) -> pdfs行 的映射
    pdfs_rows = df[df['system'] == 'pdfs'].set_index('model')

    def compute_l2(row):
        if row['system'] == 'pdfs':
            return 1.0
        model = row['model']
        if model not in pdfs_rows.index:
            return np.nan  # 没有对应pdfs行
        pdfs_density = pdfs_rows.loc[model, density_cols].astype(float)
        rel = row[density_cols].astype(float)  # 已经是比值
        l2 = np.sqrt(np.sum((rel - 1) ** 2))
        score = 1 / (1 + l2)
        return score

    # 创建PCA可视化
    # 只使用非pdfs系统的数据
    non_pdfs_data = df[df['system'] != 'pdfss'].copy()
    if not non_pdfs_data.empty:
        # 准备PCA数据 - 使用原始的密度比值，将NaN替换为0
        pca_data = non_pdfs_data[density_cols].astype(float).fillna(0)
        
        # 执行PCA
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(pca_data)
        
        # 创建散点图 - 使用更小的图形尺寸
        plt.figure(figsize=(6, 4))
        
        # 为每个系统类型使用不同的颜色
        systems = non_pdfs_data['system'].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(systems)))
        
        for system, color in zip(systems, colors):
            mask = non_pdfs_data['system'] == system
            plt.scatter(pca_result[mask, 0], pca_result[mask, 1], 
                       label=system, color=color, alpha=0.6, s=30)  # 减小点的大小
        
        # 添加图例 - 调整图例位置和大小
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
        
        # 添加标题和标签 - 减小字体大小
        # plt.title('PCA of Density Ratios by System', fontsize=10)
        # plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)', fontsize=8)
        # plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)', fontsize=8)
        
        # 调整布局以适应图例
        plt.tight_layout()
        
        # 确保figures目录存在
        os.makedirs('figures', exist_ok=True)
        
        # 保存图像
        plt.savefig('figures/density_ratios_pca.pdf', bbox_inches='tight', dpi=300)
        plt.close()

    df['Similarity_score'] = df.apply(compute_l2, axis=1)
    df.to_csv(output_path, index=False)
# Example usage:
if __name__ == "__main__":
    # # Create sample data
    # data = pd.DataFrame({
    #     'Outline_no': [36.9, 42.6, 39.2, 33.7, 30.9, 33.9, 31.8, 30.0],
    #     'Reference_no': [212.1, 94.8, 207.0, 243.9, 259.5, 125.5, 138.5, 184.4],
    #     'Images_density': [0.9885, 0.6623, 0.8608, 0.8487, 1.5783, 0.9528, 0.8806, 0.5198],
    #     'Equations_density': [23.8144, 32.0484, 12.2378, 31.1363, 30.264, 13.2842, 13.1526, 61.1877],
    #     'Tables_density': [0.6292, 1.3685, 0.4867, 0.4604, 0.7152, 0.9671, 1.3672, 0.5404],
    #     'Citations_density': [27.2345, 26.0971, 39.0948, 242.9042, 88.7632, 24.8116, 21.1596, 157.469],
    #     'Sentence_no': [1003.2, 1320.5, 1480.1, 1315.2, 884.1, 819.2, 822.5, 835.0]
    # })
    
    # # Plot the radar charts
    # plot_survey_features(data, save_path='figures/survey_features_radar.pdf')
    
    
    # # Plot the small multiples
    # plot_survey_small_multiples(data, save_path='figures/survey_features_small_multiples.pdf')
    # 示例1：直接调用 draw_radar_plot
    # col_names = ["Factor A", "Factor B", "Factor C", "Factor D", "Factor E"]
    # values = [0.8, 0.6, 0.9, 0.75, 0.5]
    # draw_radar_plot(col_names, values, "示例雷达图", "example_radar.png")

    # 示例2：针对 CSV1 文件绘制雷达图
    # 假设 csv_file1.csv 存在且字段与上述描述相符
    # radar_plot_from_csv_file1("E:/AutoSurvey/all_categories_results_reorganized.csv", "InteractiveSurvey", "Qwen2.5-72B-Instruct", "figures/radar_csv1.png")

    # 示例3：针对 CSV2 文件绘制雷达图
    # radar_plot_from_csv_file2("E:/AutoSurvey/global_average_reorganized.csv", "InteractiveSurvey", "Qwen2.5-72B-Instruct", "figures/radar_csv2.png")

    # 示例4：合并两个 CSV 的聚合图并输出为 PDF
    system_name_map = {
        "AutoSurvey": "AutoSurvey",
        "InteractiveSurvey": "InteractiveSurvey",
        "SurveyForge": "SurveyForge",
        "SurveyX": "SurveyX",
        "LLMxMapReduce": "LLMxMapReduce",
        "pdfs": "Human"
    }
    # combined_radar_plots("surveys/all_categories_results_reorganized.csv", 
    #                     "surveys/global_average_reorganized.csv", 
    #                     "figures/combined_radar.pdf",
    #                     system_name_map=system_name_map)

    # 示例5：绘制结果热图
    # plot_result_heatmap("surveys/all_categories_results_reorganized.csv", ["SurveyForge", "AutoSurvey", "SurveyX", "LLMxMapReduce","InteractiveSurvey"], "figures/result_heatmap.pdf")

    # # 示例6：绘制特定领域的雷达图
    # domain_radar_plots("cs", "qwen-plus-latest", system_name_map, "figures/cs_domain_radar.pdf")

    # # 示例7：绘制特定指标的雷达图
    # metrics_radar_plots("surveys/global_average_reorganized.csv", 
    #                    "qwen-plus-latest", 
    #                    system_name_map, 
    #                    "figures/metrics_radar.pdf")

    # # 示例8：绘制组合雷达图
    # system_name_map_row1 = {
    #     # "AutoSurvey": "AutoSurvey",
    #     "InteractiveSurvey": "InteractiveSurvey",
    #     # "SurveyForge": "SurveyForge",
    #     "SurveyX": "SurveyX",
    #     "LLMxMapReduce": "LLMxMapReduce-V2",
    #     "pdfs": "Human"
    # }
    
    # system_name_map_row2 = {
    #     "AutoSurvey": "AutoSurvey",
    #     "InteractiveSurvey": "InteractiveSurvey",
    #     "SurveyForge": "SurveyForge",
    #     "SurveyX": "SurveyX",
    #     "LLMxMapReduce": "LLMxMapReduce-V2",
    #     "pdfs": "Human"
    # }
    
    # combined_all_radar_plots("cs", "qwen-plus-latest", 
    #                        system_name_map_row1, 
    #                        system_name_map_row2, 
    #                        "figures/combined_all_radar.pdf")

    # 示例9：绘制组合领域雷达图
    # combined_domain_radar_plots("cs", "qwen-plus-latest", 
    #                            system_name_map_row1, 
    #                            system_name_map_row2, 
    #                            "figures/combined_domain_radar.pdf")

    # plot_category_density_heatmap(
    #     "surveys/all_categories_results_reorganized.csv",
    #     ["SurveyForge", "AutoSurvey", "SurveyX", "LLMxMapReduce","InteractiveSurvey"],
    #     "figures/category_density_heatmap.pdf"
    # )

    # Add example for the new function
    plot_category_density_heatmap_horizontal(
        "surveys/all_categories_results_reorganized.csv",
        ["SurveyForge", "AutoSurvey", "SurveyX", "LLMxMapReduce", "InteractiveSurvey"],
        "figures/category_density_heatmap_horizontal.pdf"
    )

    calc_similarity_score("surveys/global_average_reorganized.csv", "figures/global_similarity_score.csv")
