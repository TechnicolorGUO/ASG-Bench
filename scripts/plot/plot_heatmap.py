import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_result_heatmap(csv_path, systems=None, save_path=None, use_minmax_scale=True):
    df = pd.read_csv(csv_path)
    category_order = [
        "Biology",
        "Business",
        "Computer Science",
        "Education",
        "Engineering",
        "Environmental Science",
        "Medicine",
        "Physics",
        "Psychology",
        "Sociology"
    ]
    category_abbrev = {
        "Biology": "bio",
        "Business": "bus",
        "Computer Science": "cs",
        "Education": "edu",
        "Engineering": "eng",
        "Environmental Science": "env",
        "Medicine": "med",
        "Physics": "phy",
        "Psychology": "psy",
        "Sociology": "soc"
    }
    group_order = ["outline", "content", "reference"]

    def abbreviate_category(name):
        if name in category_abbrev:
            return category_abbrev[name]
        parts = [p for p in name.split(" ") if p]
        if len(parts) > 1:
            return "".join(p[0].lower() for p in parts)
        return name[:3].lower()

    if not {"aspect_group", "aspect_name", "aspect_average", "system", "category"}.issubset(df.columns):
        raise ValueError("CSV format does not match aspect_averages schema.")

    if not systems:
        systems = df["system"].drop_duplicates().tolist()

    categories = df["category"].drop_duplicates().tolist()
    ordered_categories = [c for c in category_order if c in categories]
    ordered_categories += [c for c in categories if c not in ordered_categories]

    hardcoded_aspects = [
        ("outline", "Formal Precision"),
        ("outline", "Structural Coherence"),
        ("outline", "Substantive Integrity"),
        ("content", "Critical Insight and Novelty"),
        ("content", "Scholarly Communication"),
        ("content", "Scope and Relevance"),
        ("content", "Structural Coherence"),
        ("content", "Synthesis and Integration"),
        ("reference", "Bibliometric Comprehensiveness"),
        ("reference", "Evidential Integrity"),
        ("reference", "Referential Pertinence and Compliance")
    ]
    hardcoded_df = pd.DataFrame(hardcoded_aspects, columns=["aspect_group", "aspect_name"])
    df = df.merge(hardcoded_df, on=["aspect_group", "aspect_name"], how="inner")
    index_order = hardcoded_aspects

    pivot = df.pivot_table(
        index=["aspect_group", "aspect_name"],
        columns=["system", "category"],
        values="aspect_average",
        aggfunc="mean"
    )

    desired_columns = [(system, category) for system in systems for category in ordered_categories]
    pivot = pivot.reindex(index=pd.MultiIndex.from_tuples(index_order, names=["aspect_group", "aspect_name"]),
                          columns=pd.MultiIndex.from_tuples(desired_columns, names=["system", "category"]))

    mask = pivot.isna()

    if use_minmax_scale:
        vmin = float(pivot.min(skipna=True).min())
        vmax = float(pivot.max(skipna=True).max())
    else:
        vmin, vmax = 0, 5

    fig, ax = plt.subplots(figsize=(18, 6))
    sns.heatmap(
        pivot,
        ax=ax,
        cmap="coolwarm",
        cbar=False,
        annot=False,
        linewidths=0.5,
        linecolor='gray',
        xticklabels=True,
        yticklabels=True,
        square=True,
        alpha=0.5,
        mask=mask,
        vmin=vmin,
        vmax=vmax
    )

    ax.patch.set(hatch="", facecolor="#d0d0d0")

    xtick_labels = [abbreviate_category(cat) for _, cat in pivot.columns]
    ax.set_xticklabels(xtick_labels, rotation=90, fontsize=8)

    ytick_labels = [name for _, name in pivot.index]
    ax.set_yticklabels(
        ytick_labels,
        rotation=-25,
        fontsize=8,
        ha="right",
        va="center",
        rotation_mode="anchor"
    )
    ax.tick_params(axis="y", pad=2)

    outline_count = sum(1 for group, _ in pivot.index if group == "outline")
    content_count = sum(1 for group, _ in pivot.index if group == "content")
    if outline_count > 0:
        ax.axhline(y=outline_count, color="black", linestyle="--", linewidth=1)
    if content_count > 0:
        ax.axhline(y=outline_count + content_count, color="black", linestyle="--", linewidth=1)

    categories_per_system = len(ordered_categories)
    if categories_per_system:
        for i in range(1, len(systems)):
            ax.axvline(x=i * categories_per_system, color="black", linestyle="--", linewidth=1)

    ax.set_xlabel("")
    ax.set_ylabel("")

    if categories_per_system:
        system_centers = [
            i * categories_per_system + categories_per_system / 2
            for i in range(len(systems))
        ]
        ax2 = ax.secondary_xaxis("bottom")
        ax2.set_xticks(system_centers)
        ax2.set_xticklabels(systems, fontsize=9)
        ax2.tick_params(axis="x", length=0, pad=8)
        ax2.spines["bottom"].set_position(("outward", 35))
        ax2.spines["top"].set_visible(False)
        ax2.spines["left"].set_visible(False)
        ax2.spines["right"].set_visible(False)

    plt.subplots_adjust(bottom=0.28)
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()


if __name__ == "__main__":
    csv_path = "results/analysis/analysis_qualitative_20260117_093907/aspect_averages.csv"
    systems = ['Autosurvey','AutoSurvey2','Gemini', 'InteractiveSurvey', 'LLMxMapReduce_V2','Qwen', 'SciSage', 'SurveyForge','SurveyX']
    save_path = "results/plots/aspect_averages_heatmap.pdf"
    use_minmax_scale = True
    plot_result_heatmap(csv_path, systems, save_path, use_minmax_scale)