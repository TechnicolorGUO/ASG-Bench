# Literature Review: A Review of Feature Selection Methods for Machine Learning-Based Disease Risk Prediction.

*Generated on: 2025-12-26 05:53:33*
*Progress: [15/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/A_Review_of_Feature_Selection_Methods_for_Machine_Learning-B_20251226_055333.md*
---

# A Review of Feature Selection Methods for Machine Learning-Based Disease Risk Prediction

**Key Points**
*   **The Curse of Dimensionality:** High-dimensional healthcare data (genomics, EHRs) necessitates robust feature selection (FS) to prevent overfitting and improve model generalizability.
*   **Evolution of Methods:** The field has progressed from traditional filter/wrapper methods to embedded deep learning layers, causal inference integration, and Large Language Model (LLM)-driven selection.
*   **State-of-the-Art:** Current frontiers include **Causal Feature Selection** (e.g., CausalDRIFT) to identify true disease drivers rather than spurious correlations, and **Federated Feature Selection** to handle privacy-sensitive, non-IID data across institutions.
*   **Interpretability & Stability:** There is a critical shift towards "stable" feature selection (measured by Nogueira’s index) and "explainable" AI (SHAP/LIME) to ensure clinical trust.
*   **Future Directions:** Research is moving toward zero-shot feature selection using LLMs and hybrid swarm intelligence optimization for real-time clinical decision support.

---

## 1. Introduction

The advent of high-throughput sequencing, wearable technology, and digitized Electronic Health Records (EHRs) has ushered in an era of big data in healthcare. Machine learning (ML) has emerged as a pivotal tool for leveraging this data to predict disease risk, enabling the transition from reactive healthcare to precision medicine [cite: 1, 2]. However, the efficacy of ML models in clinical settings is frequently hampered by the "curse of dimensionality," a phenomenon where the number of features (e.g., gene expression levels, clinical variables) vastly exceeds the number of samples [cite: 1].

In disease risk prediction, irrelevant or redundant features not only increase computational cost but also introduce noise that degrades predictive accuracy and obscures biological interpretability. Feature Selection (FS)—the process of identifying a subset of relevant features—is therefore not merely a preprocessing step but a fundamental requirement for building robust, generalizable, and clinically interpretable models [cite: 2, 3].

This review provides a comprehensive analysis of the landscape of feature selection methods for disease prediction. Unlike previous surveys that focus primarily on traditional statistical approaches, this paper critically examines state-of-the-art advancements emerging in 2024 and 2025, including **Causal Feature Selection**, **Federated Feature Selection**, and **LLM-driven selection**. We evaluate these methods based on their ability to handle high-dimensional data, ensure stability, and provide causal explanations, thereby bridging the gap between computational innovation and clinical utility.

## 2. Key Concepts and Definitions

To establish a rigorous framework, it is essential to define the core taxonomies and metrics governing feature selection in medical informatics.

### 2.1 Taxonomy of Feature Selection
Feature selection methods are traditionally categorized into three primary classes, though recent hybrid approaches have blurred these lines:

1.  **Filter Methods:** These techniques evaluate features based on intrinsic statistical properties (e.g., correlation, mutual information, Chi-square) independent of any learning algorithm. They are computationally efficient but often ignore feature dependencies [cite: 2, 4].
2.  **Wrapper Methods:** These methods treat feature selection as a search problem, evaluating subsets by training a specific predictive model (e.g., Recursive Feature Elimination or RFE). While they often yield higher accuracy, they are computationally expensive and prone to overfitting [cite: 4, 5].
3.  **Embedded Methods:** Feature selection is integrated directly into the model training process. Examples include LASSO (L1 regularization) and tree-based importance (Random Forest, XGBoost). These offer a balance between computational efficiency and interaction modeling [cite: 2, 6].

### 2.2 Stability vs. Accuracy
In clinical domains, **stability**—the robustness of the selected feature subset to perturbations in the training data—is as critical as predictive accuracy. A biomarker signature that changes entirely with the addition of a few patients is clinically useless. Stability is quantified using metrics such as the **Kuncheva Index** and **Nogueira’s Measure**, which assess the overlap between feature subsets selected across different data folds [cite: 7, 8].

### 2.3 Causal vs. Associative Selection
Traditional FS identifies features correlated with the outcome. However, correlation does not imply causation. **Causal Feature Selection** aims to identify the Markov Blanket (MB) of the target variable—the minimal set of features that renders the target independent of all other variables. This distinguishes true risk factors from confounders and spurious correlates [cite: 9, 10, 11].

## 3. Historical Development and Milestones

The evolution of feature selection for disease prediction can be traced through three distinct eras:

*   **The Statistical Era (Pre-2000s):** Early approaches relied heavily on univariate statistical tests (t-tests, ANOVA) to filter variables. While interpretable, these methods failed to capture complex, non-linear interactions between risk factors [cite: 1].
*   **The Machine Learning Era (2000s–2015):** The introduction of Support Vector Machines (SVM) and Random Forests popularized multivariate selection. Techniques like SVM-RFE (Recursive Feature Elimination) became gold standards for gene expression analysis [cite: 12, 13]. The concept of "stability" in FS was formalized during this period by Kuncheva (2007), addressing the reproducibility crisis in biomarker discovery [cite: 14].
*   **The Deep Learning and Causal Era (2016–Present):** The rise of Deep Neural Networks (DNNs) led to "black-box" models, necessitating explainable AI (XAI) methods like SHAP and LIME for feature attribution [cite: 15, 16]. Concurrently, the integration of causal inference (e.g., CausalDRIFT) and privacy-preserving Federated Learning has redefined the field, addressing modern challenges of data silos and spurious correlations [cite: 11, 17].

## 4. Current State-of-the-Art Methods and Techniques

This section details the advanced methodologies dominating the research landscape in 2024 and 2025.

### 4.1 Causal Feature Selection
One of the most significant recent shifts is the move from correlation-based to causality-based selection. High-dimensional medical datasets often contain "spurious correlations"—variables that correlate with the disease due to confounding rather than mechanism.

*   **CausalDRIFT:** Introduced in 2025, CausalDRIFT leverages the Frisch-Waugh-Lovell theorem and Double Machine Learning to estimate the Average Treatment Effect (ATE) of features. It excels in high-dimensional, low-sample-size (HDLSS) settings (e.g., breast cancer datasets), achieving competitive accuracy while prioritizing features with causal influence rather than mere association [cite: 11].
*   **Markov Blanket Discovery (SF-DRMB):** The Simultaneous-Fusion-of-Double-Rules Markov Blanket (SF-DRMB) algorithm addresses errors in conditional independence tests. By refining the identification of parents, children, and spouses of the target node, it improves the robustness of risk factor mining, outperforming traditional Bayesian network methods [cite: 10].

### 4.2 Large Language Models (LLMs) for Feature Selection
The emergence of LLMs has introduced a paradigm shift known as **Zero-Shot Feature Selection**.

*   **LLM-Select:** Recent studies (2024-2025) demonstrate that LLMs (e.g., GPT-4) can select predictive features given only feature names and a task description, without accessing the training data. This method, termed *LLM-Select*, has shown performance rivaling data-driven methods like LASSO, particularly in domains where semantic knowledge is valuable. It is especially useful for determining which features to collect *before* data acquisition begins [cite: 18, 19, 20].
*   **Clinical Prediction with LLMs (CPLLM):** This approach fine-tunes pre-trained LLMs on historical medical records to predict disease diagnosis and readmission. It outperforms state-of-the-art structured data models (like Med-BERT) by leveraging the semantic richness of clinical narratives alongside structured features [cite: 21].

### 4.3 Federated Feature Selection (FFS)
With the increasing enforcement of data privacy regulations (GDPR, HIPAA), centralized data pooling is often infeasible. Federated Learning (FL) allows model training across decentralized edge devices.

*   **Synthetic Data and Zero Trust:** A 2025 breakthrough in FFS involves using synthetic data to initialize model parameters and a zero-trust security model. This method allows healthcare institutions to collaboratively identify globally relevant features without sharing raw patient data. It utilizes backward elimination and threshold variation to improve communication efficiency by 4 to 14 times compared to standard FL [cite: 17, 22].
*   **Handling Non-IID Data:** Heterogeneity in medical data (Non-IID) across hospitals poses a major challenge. Recent FFS algorithms employ multi-objective optimization and mutual information to select features that are robust across diverse client distributions, mitigating the performance degradation typically seen in horizontal FL [cite: 23, 24].

### 4.4 Swarm Intelligence and Evolutionary Algorithms
Meta-heuristic algorithms continue to evolve for optimizing feature subsets in complex search spaces.

*   **Hybrid Swarm Methods:** Recent work combines Particle Swarm Optimization (PSO) and Ant Colony Optimization (ACO) with classifiers like SVM. For instance, the **Leader-Follower PSO with Levy Flight (LFPSOLF)** algorithm prevents premature convergence to local optima, achieving up to 8% accuracy improvement in disease detection tasks while reducing feature count by over 40% [cite: 25, 26].
*   **Genetic Algorithms with Ensemble Learning:** Integrating Genetic Algorithms (GA) with ensemble deep learning (optimized via Tunicate Swarm Algorithm) has shown superior performance in heart disease prediction, effectively navigating the trade-off between dimensionality reduction and information loss [cite: 27].

### 4.5 Attention-Based and Deep Feature Selection
Deep learning models are increasingly incorporating intrinsic feature selection mechanisms.

*   **Attention Mechanisms:** In multi-omics and image analysis, attention layers (e.g., Graph Attention Networks, BiFormer) dynamically weight features. For example, **DyGAF** (Dynamic Gene Attention Feature selection) identifies critical genetic biomarkers for COVID-19 by prioritizing genes with persistent importance across disease progression [cite: 28, 29].
*   **Feature Selection Layers:** New architectures embed specific "FS layers" trained jointly with the network. This addresses the accuracy/interpretability trade-off by forcing the network to learn sparse weights for input features, making the deep model's decisions traceable to specific inputs [cite: 4].

## 5. Applications and Case Studies

### 5.1 Multi-Omics and Cancer Subtyping
Multi-omics data (genomics, transcriptomics, proteomics) presents extreme dimensionality.
*   **Case Study (TCGA):** A benchmark of 15 cancer datasets from The Cancer Genome Atlas (TCGA) evaluated stability across omics layers. It found that miRNA features consistently exhibited higher stability than mRNA or mutation data. Regularized classifiers (SVM with L1) provided the best balance of stability and accuracy for TP53 mutation prediction [cite: 8, 30].
*   **Biomarker Discovery:** In adrenocortical carcinoma, factor analysis and network models were used to select features that are biologically coherent, contrasting with supervised methods that often select highly correlated but biologically distinct markers [cite: 31].

### 5.2 Neurological Disorders
*   **Autonomic Dysreflexia (AD):** A study on spinal cord injury patients demonstrated that rigorous feature selection could reduce 36 physiological features down to just 5 relevant ones (related to skin nerve activity and blood pressure). A 5-layer neural network trained on this reduced set achieved **93.4% accuracy**, significantly outperforming models using the full feature set [cite: 3, 32].
*   **Alzheimer’s and Parkinson’s:** Federated feature selection has been successfully applied to detect Parkinson’s disease using distributed medical databases, ensuring privacy while aggregating diagnostic patterns from neuroimaging data [cite: 33].

### 5.3 Cardiovascular and Metabolic Diseases
*   **Heart Disease:** Ensemble techniques combining Random Forest and Gradient Boosting with Boruta feature selection have achieved near-perfect accuracy (approx. 98%) in specific datasets by isolating key risk factors like chest pain type and thallium stress test results [cite: 34, 35].
*   **Diabetes:** Causal feature selection methods (like CausalDRIFT) have been applied to diabetes datasets. Interestingly, results suggest that in correlation-dominated datasets (like standard diabetes tables), traditional methods may still outperform causal ones, highlighting that causal FS is most beneficial when hidden confounders are present [cite: 11].

## 6. Challenges and Open Problems

Despite significant progress, several critical challenges remain:

### 6.1 The Stability-Accuracy Trade-off
While accuracy is the primary metric for ML competitions, **stability** is paramount for clinical adoption. A feature selection method that yields different biomarkers for the same disease across two similar patient cohorts is untrustworthy. Research indicates that many popular methods (e.g., standard RFE) have low stability. The **Nogueira measure** has been identified as a superior metric for quantifying this, yet it is not universally adopted in reporting [cite: 7, 8].

### 6.2 Interpretability in Deep Learning
Deep learning models with embedded feature selection often suffer from a lack of transparency. While tools like **SHAP** (Shapley Additive exPlanations) and **LIME** (Local Interpretable Model-agnostic Explanations) provide post-hoc explanations, they can be computationally expensive and occasionally unstable themselves. There is a tension between the non-linear power of DL and the linear simplifications required for explanation [cite: 15, 36].

### 6.3 Heterogeneity in Federated Learning
In Federated Learning, data is rarely Independent and Identically Distributed (IID). Feature selection algorithms that assume IID data often fail in federated settings. "Client drift"—where local models diverge due to different feature distributions—remains a significant hurdle for Federated Feature Selection [cite: 23, 24].

### 6.4 Small Sample Size (HDLSS)
The "High-Dimension, Low-Sample-Size" problem persists, particularly in rare disease research. While CausalDRIFT shows promise here, most deep learning and LLM-based methods require substantial data or pre-training that may not be available for niche conditions [cite: 11].

## 7. Future Research Directions

1.  **Integration of Causal Inference and Deep Learning:** Future frameworks should natively integrate causal discovery (e.g., structural equation modeling) into deep learning architectures to ensure that selected features represent actionable intervention targets rather than passive predictors [cite: 11, 37].
2.  **LLM-Driven Data Collection:** Moving beyond prediction, LLMs could be used to design clinical trials by identifying which features are *worth* collecting, potentially reducing the cost and burden of data acquisition [cite: 18, 20].
3.  **Robust Federated Protocols:** Developing FFS algorithms that are invariant to non-IID data distributions is critical. Techniques involving synthetic data generation at the edge (to normalize distributions without sharing real data) represent a promising avenue [cite: 17, 22].
4.  **Dynamic/Real-Time Feature Selection:** For conditions like sepsis or Autonomic Dysreflexia, risk factors change dynamically. "Online" feature selection methods that can adapt to streaming physiological data in real-time are needed [cite: 3].
5.  **Standardization of Stability Metrics:** The academic community must standardize the reporting of feature stability (using Nogueira’s measure) alongside accuracy to facilitate valid comparisons between novel algorithms [cite: 7, 8].

## 8. Conclusion

Feature selection has evolved from a statistical necessity to a sophisticated domain intersecting causal inference, deep learning, and privacy-preserving computing. The current state-of-the-art in disease risk prediction is defined by a shift towards methods that are not only accurate but also **causal**, **stable**, and **privacy-compliant**.

While deep learning and LLMs offer unprecedented power in extracting patterns from unstructured data, the integration of **Causal Feature Selection** (e.g., CausalDRIFT) and **Federated Feature Selection** represents the frontier of robust medical AI. These methods address the fundamental ethical and practical requirements of healthcare: understanding *why* a prediction is made and ensuring patient data remains secure. As the field matures, the focus must remain on validating these computational advances through rigorous clinical trials, ensuring that the "informative" features selected in silico translate to tangible patient benefits in vivo.

## 9. References

[cite: 1] Pudjihartono, N., Fadason, T., Kempa-Liehr, A. W., & O'Sullivan, J. M. (2022). A Review of Feature Selection Methods for Machine Learning-Based Disease Risk Prediction. *Frontiers in Bioinformatics*, 2, 927312. [cite: 1, 2, 6, 38, 39]
[cite: 4] Deep Learning-based Feature Selection. *PMC*, 8433983. [cite: 4]
[cite: 34] Ensemble Learning for Disease Prediction. *MDPI*, 2023. [cite: 34]
[cite: 40] Review of Feature Selection Techniques for Predicting Diseases. *IEEE Conference Publication*, 2020. [cite: 40]
[cite: 17] Madathil, N. T., Alrabaee, S., & Belkacem, A. N. (2025). Enhancing Federated Feature Selection Through Synthetic Data and Zero Trust Integration. *IEEE Journal on Selected Areas in Communications*. [cite: 17, 22, 33, 41, 42]
[cite: 43] Federated Learning in Healthcare. *PMC*, 12213103. [cite: 43]
[cite: 44] Federated Learning in Healthcare: Balancing Privacy and Accuracy. *ResearchGate*, 2025. [cite: 44]
[cite: 45] Teo, D. S. W., et al. (2024). Federated Learning in Health: A Systematic Review. *PMC*, 10897620. [cite: 45]
[cite: 46] Federated Learning for Medical Data Analysis. *MDPI*, 2024. [cite: 46]
[cite: 9] Causal Feature Selection Overview. *Fiveable*, 2024. [cite: 9]
[cite: 37] Feature Selection and Causal Graphs. *PMC*, 11554952. [cite: 37]
[cite: 12] Causal Feature Selection for Health State Identification. *Nonlinear Dynamics*, 2025. [cite: 12]
[cite: 10] SF-DRMB: Simultaneous-Fusion-of-Double-Rules MB Learning. *IEEE Xplore*, 2023. [cite: 10, 47, 48]
[cite: 11] CausalDRIFT: Causal Feature Selection Algorithm. *MedRxiv*, 2025. [cite: 11, 49, 50, 51, 52]
[cite: 2] Pudjihartono, N., et al. (2022). Feature Selection for Disease Risk Prediction. *Frontiers in Bioinformatics*. [cite: 2]
[cite: 3] Feature Selection for Autonomic Dysreflexia Detection. *PMC*, 9416695. [cite: 3, 32, 35, 53, 54, 55]
[cite: 56] Common Feature Selection Techniques in ML. *ResearchGate*, 2024. [cite: 56]
[cite: 57] Kuncheva Index Implementation. *GitHub*, 2024. [cite: 57]
[cite: 14] Kuncheva, L. I. (2007). A Stability Index for Feature Selection. *AIAP*. [cite: 14]
[cite: 7] Nogueira's Measure and Stability Analysis. *MDPI*, 2019. [cite: 7, 13, 58, 59]
[cite: 15] Interpretable Feature Selection with SHAP and LIME. *PMC*, 10074303. [cite: 15]
[cite: 16] SHAP and LIME for Chronic Kidney Disease. *IJARST*, 2024. [cite: 16]
[cite: 36] Comparing MDA, LIME, and SHAP Stability. *SciSpace*, 2020. [cite: 36]
[cite: 60] SHAP and LIME for Osteoarthritis Classification. *MDPI*, 2024. [cite: 60]
[cite: 8] Stability of Feature Selection in Multi-Omics. *MDPI*, 2024. [cite: 8, 30]
[cite: 18] LLM-Select: Feature Selection with Large Language Models. *arXiv*, 2024. [cite: 18, 19, 20, 61, 62, 63]
[cite: 21] Clinical Prediction with Large Language Models (CPLLM). *PMC*, 11623460. [cite: 21]
[cite: 30] Multi-Omics Feature Selection Stability. *ResearchGate*, 2024. [cite: 30]
[cite: 5] Benchmark of Feature Selection for Multi-Omics. *ResearchGate*, 2022. [cite: 5]
[cite: 31] Feature Selection for Multi-Omics Data. *Leiden University*, 2024. [cite: 31]
[cite: 17] Federated Feature Selection with Synthetic Data. *IEEE Xplore*, 2025. [cite: 17]
[cite: 22] Enhancing Federated Feature Selection. *ResearchGate*, 2025. [cite: 22]
[cite: 33] Federated Learning for Parkinson's Disease. *Semantic Scholar*, 2022. [cite: 33]
[cite: 6] Review of Feature Selection for Cancer Diagnosis. *MDPI*, 2025. [cite: 6]
[cite: 11] CausalDRIFT Performance. *MedRxiv*, 2025. [cite: 11]
[cite: 10] SF-DRMB Algorithm. *IEEE Xplore*, 2023. [cite: 10]
[cite: 19] LLM-Select Overview. *The Moonlight*, 2024. [cite: 19]
[cite: 20] LLM-Select Paper. *arXiv*, 2024. [cite: 20]
[cite: 23] Federated Feature Selection and Heterogeneity. *arXiv*, 2024. [cite: 23]
[cite: 24] Federated Feature Selection Thesis. *DIVA*, 2024. [cite: 24]
[cite: 32] Autonomic Dysreflexia Detection. *Frontiers in Neuroinformatics*, 2022. [cite: 32]
[cite: 25] Swarm Intelligence in Feature Selection. *ResearchGate*, 2025. [cite: 25]
[cite: 26] Leader-Follower PSO for Disease Detection. *IEEE Xplore*, 2024. [cite: 26]
[cite: 27] Tunicate Swarm Algorithm for Heart Disease. *TechScience*, 2025. [cite: 27]
[cite: 64] Hybrid PSO-ACO for Feature Selection. *Cureus*, 2025. [cite: 64]
[cite: 28] Attention-Based Feature Selection (DyGAF). *PMC*, 2025. [cite: 28]
[cite: 29] Attention-Based Feature Selection Thesis. *City University of London*, 2025. [cite: 29]
[cite: 7] Analysis of Stability Measures. *MDPI*, 2019. [cite: 7]

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMeObOefJ_NOSVNrkqUTmABFQ4tSa4qGeq2TTGYKD-kNOLqOy3AaWbE41FXhedki3uh8YZ1FtaQlg58bM_VTJ_NS9CykyeFhS2EA4bwJYrQhqsc6MX73nR6ecibIenu76EfhVPhko=)
2. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqJJ980CCOwbXI7AkLBzVVJ9MgGUSv8ISi5YUlbznhW8Un8wZcri2LdNbltc8N3JttDoHpxfOJ_UABqlOHAfCVWaM3SEHgZBBSce_74ypLN1SA5DMCuDCPRD0bG1yGOvv1VloAn9-X3ZKbtgweMGBbKu5FoQBP9HRy_DzKgqyd5woGVKUiDDarTus_HYmEkXI=)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpFEcd-AxvBQx81KN24PKNVcCXF80e8wvOYO0OMzSpuEMtptfcUJbYiFiwxJMBr_FNNDFt5F3ZmKa2ksKFSTcqoLV_ki-KwEcJEHvvTi7T0sGbEc8tgNZNunjQahlmJgKRTI1S0PA=)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcWP2Q2H7_tr2mSFzumjadRrTvhh3x2Eu1mGFgrG4kHhzhxJC3xhMYDd4CGehJNKmexpOxMzXYQmXf08x98FkHEKB9Vt6hFJ1UPSJf9ykWmHvtygY7B5HLAQVuLQhrsqSm_o1EFSI=)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn52gTyeqyS2Lb5cmVBzYnj7L4wYnoV-xbGsbwliY3Zttey963Jhn0P5hyqrjIPvrrvCMR3XTPPZvX5_vzXARWMiA0_5gckVZKeWOUIOrOo59wyFv6w0rjgWpSoH_VSyuPoBijo5pGL9Y_OobWGmSJQnKUKslc15ekEC9IRb3UUpRVtPgGhnB-WdXfd9MI0OfBAGAHRxDfJWL3E782ZO39Y5JmBS-YRQb6dGjM)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfpfbmYYNnIxyXEQQaNxRllFIwL8tlUWJMINCHjQRSegColZSPUe5i4qCeMo09HgqRnxi8WDVldaIyFrny43N7QCompSq8tl6J6xDsG9jwbOagZC84M_GzQQBv)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjUZ60-inIibybpu3R30VmPWOMYZUKqF6mjrLQCnp8UQOp7_O2S06Qw83pE4UTy62WHmP4mPXFvm1lw8Lth28nFjM5nR_eld4pNBHXY8PzJkl59mjwyZlBG6U=)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tG_qubhREVIVbpMecaZPqrkUMMb6TEtBbIDP4c-bTuT63R8sSFoJQIUL5Vijk1lVzMzOIsULm7qBPZE2bfQeqva4auJ4lUQi5CEka_otcremgJ8E_fah1k0OI10DBQ==)
9. [fiveable.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNwH5x04dQDEOmrpsjW3RCZ2wVF46SIlJKGWzLMd72Ru3XvFw8NC9iJ3YC4bFYWzN77Y_HZQzyBGwuJGC9Hgwp-EYjPDi2aJpkA8gNRKwMSgVfNadQRgLCOu9UCkwSCe7xwLhY9t347V2h0cnGKAYEwNPZe0fr-enhAs0G_E1CTycCPuT_m9YFzRA2bAk5JoLM4yplgw7v)
10. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7lkEdoTWAk33FdnLFBzLfc-1ETFsA_EAaHrb3u_VVgf-X_mFrYHRtfOszrlhFtF5xEw586VuqoSHe9o5IlDaxHSJ9d131CZXpGFl3Uk9B2F8AsJbRWZeCUQFZUIhhaJJJfXM=)
11. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiP-06LQxOAl60hmxq-8XpM9Yib4xOnN9qD6trNmvHeg_x8LUcePjql-5NUVID4V4CM5ygNjdMlGEvItHhijeSDkltzoJjJEyMX6VUzGKyk_li8vC0r_jjy4p_vdphW6LjpHJ0NY493rqBeR93ZBrFFw7sH821j6rS5Z4t)
12. [elsevierpure.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9wt97eBUHcb1XQgf-Z5BX9EbtydobTNEhoDe-iaGqdb870UMGfIWb3SBL8rbGEGrGfS_k_4Nb1xlAXok9qxDCSD1ZLlpqfDgTH3-_xl1ke6WSvHoCe_eQJl4W68qmogEmUBfEPBvAvAm3i3amIhp8RsxBOss8wVNlGcEErWaOcx2_crSsb4jEUt4ibvj5VAbeXOYhDflkT7BWcW6emvLw_EzeQvM=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOAVg3QauA0zyi8YJfZkBrA8--xPN2HH1M9JLcIYov5C4RQj7nAY87GsEr3NWK3rRytNbKYHQ1_enQUeRsa66NBFWvAGtchiqtDX-8b8XnNm0gGOp8_fb3VgJI5qcArLLPmhePj0OghfLsWl8P-T7exLfEyt4mHHugeRpYDA8dDg9e4lci1Y_Fnr65lZ6XGVNfd3z5)
14. [lucykuncheva.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDdwpQPRNTxTJZSUyk8pXNA8p47l003T_H1FRbUTC8dqcdCT14AQz1Nw4v_OkXiz7CDr4-nGh9voWFoUczYJh2B7d5rHpe0Rje5I-WJfBppcqbgJ1P8XLxY7zD1z6MocLNqA==)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExDmnqlCSLF-jtKnJUAMoz7qjy77uxW81pzjIH1SoMUdXbE_JAcLbaD8C4fpGMVVYlNQXsG8MK-dWPQuC9v8lUAFtwvnoqI3NULsYHe6Xzx6lwR6i9DNRauLMvJx3IEb74TDXXip5Z)
16. [ijarst.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOc0Ar_XQSbCsZ4CxMCNJOctncA3Wk8paGsxMG7s1A1xz8bxLwSLkefVuFNKgfTcDF1fQVpYC01v17FLUhB-CPd_u00KXjZjXuRMVosMfezj6DItmyCQGznWfrYP7K4cPJwErzk_eTmdhatCMPSPk1hgTJyAtINpuTHDsJ4Hi4CG48V_Cjdg2Z4IYlOg41Bpve5_IfqfHRX9S1s4BksgkeUCXyWnr0gdf48Jz96sP-NzsO3W7ezJ9hvEt_7LdHKz5LH_z5wlem9xPyJiXSda6G7pn0VZQwTe7o8Swz5Q==)
17. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGarGFdXPRTeKZlznn4WXiXUIjscDXr1sBNBRdV0aYTrE-g5DEoMd-BaaaAQ1UJxqxBFgJodlxtxCubbg_newoUYDGb_Sf5sHkjoLVCe580C6XW4dqUj6mOJutAY8B0E9UN6w==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZsJn9bSpEs-4sVNUvo-Batc36SmCo9jFfiiAooXBifHd2KzgY2R-7s7GLBoBzCJo4GhhpQHlvALQAmfaI1mj3kUb7KNvDxsrsH6r_pTGnjiu15SSD7BCN)
19. [themoonlight.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHcABx8zih02TCz1951lRnc-xiCOqZuW3SnE_qlrrKe9-5w31yzcRWx5DXx8tagrTVoV79L6L1e8Ss62ZaHSsQP28AF-TjIzkR_R69x11MXlFPpyyjYyIDaaXGFWErBTN5wvbUedli5g7LGyxBH6NQY_SMvibJnqUnKgpb2BcgWxohQ_a9iQYO1dGM9Hw4EmsCnA==)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMujUTln_qMLr8cZTuIS7QjaxkvfPlxOhRZgvxPVvHPbkXU9eO5UutnkjCaJpRszDwf_qWwBSRjplLaygoocAO8k_F2nKrcnY04oRRPQ2-RoXTbk59)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVZihUXx2ZJEuz3PSWuSG_9-FQvIdHGG-pFdc-ki4PfZtyUN1JrccD1Xi0KFK75zcSR5_-cyY76OjSWwqxA8g0CU0ol1DoJDKV0ojF4vpGlJakBCfPStg-f_dDppA-qXdip-fUDby4)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAagZOyFA1MserSLAg0-npfEZ3ZHK4_9cOmogcDd_v7qY6nGl-2UJZEoc3t-4r7afhk8_t_H7TTYFGjsDPILeg0XRMZLhtD6JHrXyR7EWDrNI77AOe0-R-Spmu2pc9WMrpOzEemZ73pKTC1WE4SSKSH4aZhmucmVSvTPa07LXub_91uB9sI3xBz_yLDkuSwT2Vq7vfLC5vKrwpSCDHepZDajPIki8uGFUsBRhPcz0QljRqNW2QmJTWMr5YD5mqf7I=)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECJNEdaTDXnlN6K9izfhyfGKOIj77M8_0LJDvpBH6NlSIWzuCTqDH5arDARUe1Q1VwvJnR-hVZjgEoFIv34Ic9-Qh9Vq3Dd0Tq4SYAeF6nl5sLqJNvmTnV)
24. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjupBuEjigBFAGwPNA-E7NTMdD0RYTG6s3FaZbNPywisIUToxHWkpKIGihHkv01B1UN_kjQ1AU0C06lk8EnN-c3KQ2kzOBXEkBqHI3-e2krKe1Yo-M0pmaeD6n08jpF8K4wbouybY986Kv9yIEbzvOORfKw6xN3A==)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2SWW8rmYdJZLyiekDDsb106CHpvc1Hu5FahtD3kaS2o8VvCCcae2le5tKSo_l-WA-O35C6YLxLlAU-1jOZfMPkAFMK8h5CDWloV-oqek7WG-6c-vTUcitvTLffknkJBh9fbPIoKS-LIAULY1HuSjlCdt-amPVsn-b_ZrphV6Chhi2O19PLeBrqJJ-g3fN_F5ugd4ml0BfZThQxJ8Y97VAL3qK7_dDull1weZX-nJUHwc=)
26. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4pb-Sep2ocI0C6QXhgHV9-w5jdasUWdbwDU3_DnKyBVzaZFRFgk2S5UKytZZXK5tfuKbhiK_0l1L_eCsjnI5ip3DSRSBWfrw1nf2oqDNabajAvzG26Sw39huzaWBl8LJRkB8=)
27. [techscience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK7UXOzWKYPxONr2duHO9FVfL3OxLjIEjFAVevNYpWw2SyW9TCuPt09SMAqdPqNTWQRAGOHMyS9F_ny1-mhxsjutDblwhmO0M5mtBqZOfpYOhO7paQR3QPAz01-FLS_P2MsJ924xLE)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHUg9i6fOvJqk9JwUeMwypbbJ21UZY5T4oLFUYdVG750K-TSYgo1p5lnjlDmfuSssS4inUD7z3CjMELdavjYFekqApxrMRXfLR5Pak9qTsnjZ0aYPsuDD-SPFBc1cVC94r3KorfOs-)
29. [city.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFk3pvhoM490Iuh6MB-w3e9QvXT4mClHIcecgYmsmWqDdtcpn-LNbxVxDPB7239CT8mrm-HcGYxoOPbpEL8nwbI6CVoyroH4nfRLwU-GzGXA3uyD8ihzGT5QqICft7qztp0PitOzdT0RvzXL3-6xHrQ0RuQ7NFG0RlndiPFrzNWXT-PA==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6p-5NgIPc7e0V73k9tl46KyXpsa67ztlCwaoDJlqmaBAdTT24Xkt1LcFR4_Qj2nAzcU-S5iLny7BqhUFeiir5e0vKuRvmyfoGUGcjnnSY0iSUWBnLUoJhnUZcptrs15FfgWXy58hxRpR2AEu3C0R7rPmcrv-UAVJsDqvNdeXLs6GbCvbD_p-mhaKwN3QcmMTmekY04UINjUAisEacfleevIYk)
31. [universiteitleiden.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGppk1ORMa2wkY93GPQMw1LCzP-GBAB_D6vQjLmIuG2GtSYIeBatenB85Gxbl9QvsudlpGFqny1niMSq6DpjvSiF7KM0m62nYM7I71Nmix9mxwptildsMbmcA_e-kF8usnKjZK-VKv_y2owloDqGzAAtM6MXQ==)
32. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PNgM8LULoSZN9mp5S7FQFoEgEHK_taUCm3uY6TCZpYR3dn936N9dJU9v0q9uAXrJ9KXFRh5zaAyHojn2GQfazsjxxbCmC3soNV1sb56SOT56nr_0S-TiCJYc8OY0fo3bEuUGe08-9Ybtw5aHuoNad6OEgzvk8XLGzuyN8TU-kmtTBlEI1WW5iR4Q-2Yu-8cF7w==)
33. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8DOnFiuqvkMXab81-yA-rp6_axKeM5LTbDYsUymRzxvEM_TTuN3Wf-5eyAqW5EU-TeZ4mPdNdfXr8PQjCu1GgwFDc8iDRBrz00Ey3zS31mp83-kIgWWDjYhfoQC43fw0mzbT6X7eE0SgLG8inAT-UZeSBm1vImILHd-793Xa4i0zsCX4sl5ziMpuTZQQY4D8KD18nq8j2Kt7M_S0vlXfhy3kMy609xrzy0QXX2XFKxV68BnOWFk4JU5UeOBOcuoSaHw==)
34. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH56J83sRNJcpzfzRwzxQZRIHPsCCwI1lXSIc9stGpXQvgov8eExIyaAixy5XqDvb_9bv0TcrM_6i-f_yp91DXuy-HRdIsGKGtaGBeXEHFn4PK_ndwmMdGBVq520A-9)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKoizzil0KdeTL_QKq0LaMen7UHJDM1UAZ-j2EikCrjBzZJsVgc5JGnkRswrMKwxBo_exfnLSqMwy49iPi25_jUqy_p2uQQRtJRn3KsA6LUCEyaj69bSX_nFwvVa8UpEAmmFRYzCo1ZRzijETpNbf65ibPkf3WfzMXQ4pjTQYlyUNCP5CV7BHH4aL9LnXQXHFjm0fMrD0N2VanU5Hk2a4m7REzghqln41duqNuH6S7X0HhRfes6WMC3fOnUqh11cI7jjaDdFwiEZ1-vINJPN0k6jtRYQvdXr5WkbEAMmwFhtCagQqZ8sMD8SG9DGGScJqKmmi-Ui_PvRXQpoTLnZP2wZHKECt8Sss3mYN5t5e6HOOPbyJ09czlcJm5fTvRpD3sBFuIqh4Ivv1jvDOcbX6cdYNGXQ==)
36. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_0qdVSQYp3bvb-43MKQgq-5TQqVq8SJv5FZjNkhnKb94NPuBlwAWLsMoLZIx0kgZCaGu0Et0DF1R6I47qrlkjc_aqcPsfLMrJ11JtOxzLkaPiEofmAAvTO7jTGwkIX6Calj8bclOt14KIHeWmAv2iAjFLdsA9VFkMsiqZcXBUeWK5EcEY-QhVXr2spMTzfrbVnC5V5Imr)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-OqjTQOHCW2z3rbz9JYrEF-DiRo05UNFmosQvRsfWdHAoftgRuRGmm49PCABixTMFq_GR6_7qqn1FX21ve5nFhYr2xkN4925lhNVXx5efNkrWHzZteOqN3B84aL05HlBdBvt3D4xx)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV23ZORECLBMJotbwRxvlbSvkMkqSqfxTENk5t63k4JYpyYDBozsNDi-aq-vRuro8uCPyGZ8HiW0uUYyJ6di2_j3dsAWuwibPRA4lPg0poZBDv16fX4fD6R7rdeQUZ)
39. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG4Y11QrhL1wHfxusnaoVkrGm5vhWkZk_gkrLUucItpPbr36oJXcQOWfpaiUekahTdfa5cCJ24J-TBVaxwpuN30UlvvZg-c9RgTHpyXUXJnJ-r64x7-4DXdcBz0ieaqHJMkkVObl3ObodDGB0oD5ZtO1eyLrEkhnbe97FObJSezzN4VQ==)
40. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU7w821DTZnChaa80SZKUyJezg58hLmeq8zaADKa1juWNKdA8YJWsRDjvPOYzPWXEVcVBbg9Dd-Dua5bJM8kPN7Hkm3tkjnQGB7BiMmj_mhibrwWA8DrzSJZIFfOetDlrf8g==)
41. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCPsVI2Qdatv_OyzIoF3ICObP3-zAXWNCdjYrCRlXo_N2sq1vQsZW5DHSpTfnRAu9_7l5otxB6FA1cp0vRpFW6NQeYmbqtfuzmLZqUF_hiGfFZbALb3WLwpi8OhoJVJnSUYJzQn2HPjr7WtWNaIQ==)
42. [uaeu.ac.ae](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-T94uPMxuDmcD02HYJ3cpdjIhUHFbs9fswoa6SZlM2TnB3yuyX7aUPhgZ8Y_LtFp6H6mS15Z_mnTqDcE5l1EYuZzhO2olgj0nc6mcRqdCjU4L3jrrvSVp4j7wuXkvmLVsH2CRfxNr_RR-iLApSlEs8bQ4eyqyJ9kU)
43. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0h-AU1ndylgrdz7Yb_ig5LYmi7-rvP_cr3Tym4eUmv2m_P884WMfMf6FWMnjVc-5fp_jquZRr5_Dgpci6WH8XVqISueT69pRArTVvrBJFf0lin02Lv4TiCrYtJB0NsvYfzwbo8b6M)
44. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0VdYRXRYWpaWJ51GdszpMzy0Lzpux9tb1CofJ61R3LZtb328fPgAl4KPBC_QLJPqJq5HXc18gYxGCffSCOH4PaZeEbxenW47VbBj8ikkp-ZARuxVTsfUMCe612XcL2xQRE2Dl5BiV_7nwF97AvHLYYiGSJYeBObHIsBu4OFDea1cq7WlAHN2-2B11_tL3TJdIoMXume6zBV9tWTh468iG2MbpGBslagbHHTkLRsJ-fyiJidIhA49fZMIe4jnJdASAs_7Lqn1JJ5OgTRRHJPbXjLTcFsiuECQ=)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcnKvLZVB-568lTM5DuJpHJmqJuK2F8IwenN-6inZl7qpruPumZ0J11CmSANLMvH433MRnal2TWaIyMAK8XcMOiLCw3HoC_cKbyqrDZf2QcIMyZ7c2rrsm2R2O8mthvHsNtVCslvTU)
46. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO7ebZTLYPhMybh2h6aJ4gGSGXfs1n5nFwA1ch7FY7LqtgjtV4c44ZvU_k65tg4LYBK0GzrD2TSqGwz-AFc5eZS27-DdWFT4WipqnUMi_exJ-1ejk_LKmGN3buDQ==)
47. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqcYYxl5YHiAhzrGHgE1ivpNG5FsfMg9kI71RyLuoeYtHdD44zfPdcaExE1hPC1uw2LZkJh0Y5DcnIaIkDGlXYWMTmHZ2p6xbpiUYLWJdHEZ66_aDZ6wxUKkKBm5xAPlb-N0j8Q7flrcTTBRuBriZFXkA7A_5uOQ==)
48. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA6cPRYfUrm06E7Plr2vVxpxBZmBF-mxCoEintIs1yt89A3iKR-_8cY-LvCOgtFCs3tC9P654ZNK40ZtyFv1RXpKaFzLmy8coJ377ES5abK-D-nJAi3ff61nq0NNB7p40EvoawOjkyLYx7czpqPIcLMPPNr6IamdYNdPPLNHnTSwc1-TOkYIbYFzDODJp8iptxfjcpYul_tP0s-0RhnDaBhNMgJKXkWd6lLhZX)
49. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUVB409J0zk2GvDctv06FaptQfO0wX_qGCDxjmJjZ5jFBe13SA-bZv8XmdvuXItR8KuQbKZtVLgG-YXsnN_3g9VgV0meJZvKVYJSzZ1Grkp4jfoty4IkSdWJnXzcACc-rqndKHEQEjq58Ht3xREP4FQf7ej0bZ5zsD62EHzhKfEcyl7hawukkyWSinl4fzc8BzWYkF16Ib)
50. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiJTIiiseIhxwWNK_BGkN4GYWioIqb1uobSiAJTzcK-GYhcw-TDkWY8UIJ_ED8dQP4jj7eUddV8nZjXUtAQX_fjzR1qb6gx0xxENA06uCQeOftvplO-eTdjaxDGZiyM9uDuJC5FFg-vnBmZA6yZwZXVfx8-7H54jDaxPY=)
51. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_nrXZaCNXIfYN_bLsCTr_2yZwcEDh96bSMyxijtJS7Nea4XweZ-K464EnT2JB5qjQynDagqzFSTpMYeVHWkTCaxI3F5EonbjxQd1wjsEFsPGVaSCBKTY7WPv0OHpNHExPPBKZOOlh5bpHVtg0tWIgM0Q=)
52. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSDF1dI9mknrLZTV5BoYeKHU_W8RihqJb25F0ZCvxrIlQXNMdaLYe3WuvAS-Dk92XecmvkiZCpwqvJMCx4ETGnJmHWS0rVoJ-HfaXTJ4W2zQzhhsUcCTXnnaGrL3rqCiBnizXgElRaof4z2P0gBfPZl9Ope2S1hpqV7idkAaSt3DxfjAj6SR5S3tQm_fpkniXtK2qEBRtVSD0SPKt-TRa6lDgN0KC43KfM5R7yONSfzaVRNhz-B5lSCZ-AlvadzS5SHoCofw==)
53. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLaOd95L1GxxAC-Y-C-HJ9c1AWOq7N8X5qComqnfhMhCmFpCBe75MqCu94ckOL5ZqlxF5Z8X0e_UHovXNn0coQvF7s7_CnjGkxPHcHSLKJ60y1-e74srVO)
54. [iupui.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTRVDsadHZfbQjHB2LG0uOFoqPacdrcLwMlCQ_MsaY4vf9A8D_mlzdxvvrbOAz3xqU4ldbrJIteBakBwCVrydp0OLNGDk6lCSTcAxQW-mKBmH2gHaYzhTm3j1xx2TMigB2uIbSjCtbacpDTLnfpPYPm2r4IdVRO7fo_aW0gOL4Z8kw6M2GV8s9JD3o9Q==)
55. [purdue.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs7CZWtmMnlNfKlmzcAYTRJzaZV7-lgHGtDRdd1IH3VsUDcPmt05sAKAK-zSwKWFpZBdWYch2Z-F_V_JTS1zQ0B3YwO6aD5oSh0MpSIbNhwAsYp3X8FxBBKwYgTqQZwWwEjU0Dj40fXQw=)
56. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc6v6nj5fPrMJXqN01AAf_F1LJJBd4HbiMsKgzTBaQTFhwWZGkpA1Sa5rcaV3YhkNUoBN5DXI78NL3c-19QD7rTMwXwgapmliH1RJUsEsSwHC4H6NN0n3jo4he9Bf3ayRZR0XKG8ACjOPg6nZhH4dv1Ehbb9VIfAtt0jtbGC_c9qgMLtqUfllO2mVe1jzfz74j9pmNR4pdto4S2m8dCGc=)
57. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF99-Hgpy60UntyLEb2LQ4jIMksykQfYIPiILtmnVxf18UQiDY9g1DHdaPWjwrEL_A7NOh1LNXLqlqm87iZxtfgHNpdZFq7vWJ2FyT3vTpRwsigcOiSe17mK5uTkjDqJgrQ)
58. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi4VKpxieedSPoKDm6WXLKLUiV9RyEMqsRsZEQaTgt5zQY8qgojY8WZvU-bLbAS0DS3BPRAWeUQdzkA2TsW0aDcftoF6oeF3eb9Cvy64PhyBdt8BYhkTN5uUijDDb9ig-ixHiuv_d7NdOA2BCrp6ixejadcDhATac-mMCBS9YXJbysza3OzJ6QzwVataTdYyHdpr27DGTSWRk_GDrk9mecI4WNXXwLb7-HddqoU2OUDhzhGe7Lc5YldpQfl8z-vSHCP2WVamQA-Ge9LkHAR9I=)
59. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaxAQ4cpq5inTo0izX-uNmX7kQHaRo2fTVu7U_hx9-wk1A5-QTG6_oALaM5SnCP0o9aXQWZJ5LI42TRiWTEl4xCKRHQEQmOesxQ2d2dtc5y1feZQARjWKy_dpcv3zXNm_2jwUBBEtKKuHgkQY-t8bYbesRaizV8S_cGG-aYMVCRo9qXUR-6EFGRFG59ZBpghd-o1Tg7uakpLX0mltU7_48KjFM_jBGF1K-UzLFAA==)
60. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZyPgEB3GSB7rQ5PCvxRkfWr5gvnDvOqENq1EnO66koi1JRQqnBADzCmNoTI3iTbjv-8W72swmvOnT9P7yl_Uo6YqkaPEX7oqKN3oT1KqPk3yxBBXj96g5VKHx)
61. [powerdrill.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX-WBxWZlNzqJMz5uoxnXQI07W8JQDJKE0zvDQxjdt6fjXV6keUAkvY7EcagJy5_pMQYifHkiwFmY62dVvBDU3w0gd6Fk6nqTAUoj_mjvDrJr9YFrAgOgy3seVYBm6CPfA6e1QN6RbiATF6neAUMClb3A09FQ3hTHjTpGvsFq5es0v3tQOMA64DLHzVVIW7OxSti4=)
62. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwue2s8UGWSw85xoi4LsxXcJSJq0_MsW6S66PxpF3ADCojDheU6W-PVSLOFpqX_suEMdiLaczNDQh72UMFjlCDflHY9jC8-lnSqd8BQXvDQcLeez_HGLeRHX-wjVrEE0ZY68c57rFtRT_oQwljqc_sa8QRlc5z-j1KH7DKyfx47nOzxhCtfymvWU6MoFIfpmvzNcNh2-qxq103AA54Xvs=)
63. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdM5UcU8F7PPFsrCJCmMTwB99F-s3R7s82IMhu7vqcCUWAezt9LyxMFNJqfFaxSes72klRaEMB7S-2nwqtggILLYESVQK68ebQA0CbbxoTySZu2HNiGFxPmN72sYiS6e0SWyozXDpilH0SrQ==)
64. [cureusjournals.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwAnQIqIwi5WspvwanIt2EOMZY7WBVYtva5-qaqe3RjkO_UmsO_NqV0WiIwtES0LAzajp89ZVRb8PoendELSGUp8y8CSC-U94ct3_HPTY3n3e6Y5WKJ9oJbnVQ2WNetjMpnpGrAxrffNTEjTDJmxbXoYDrY8OFr_o-Ns38yU_bzDTlA654ET7IE_wh9VJdy80t59hfW2dh4qaGzg==)
