# Literature Review: Quantitative evidence synthesis- a practical guide on meta-analysis, meta-regression, and publication bias tests for environmental sciences.

*Generated on: 2025-12-26 20:59:54*
*Progress: [28/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Quantitative_evidence_synthesis-_a_practical_guide_on_meta-a_20251226_205954.md*
---

# Quantitative Evidence Synthesis in Environmental Sciences: A Systematic Review of Methods, Challenges, and Best Practices

## Abstract

**Background:** Quantitative evidence synthesis, particularly meta-analysis, has become an indispensable tool in environmental sciences for aggregating disparate research findings into robust, generalizable conclusions. As the volume of ecological data expands, the need for rigorous statistical integration to inform policy and conservation has never been greater.
**Objectives:** This systematic literature review aims to synthesize the current state of meta-analytic practice in environmental sciences, focusing on the transition from traditional models to multilevel frameworks. It critically evaluates methodologies for meta-regression, heterogeneity quantification, and publication bias testing.
**Methods:** A comprehensive review of methodological guidelines, historical milestones, and contemporary applications was conducted. Key sources include seminal works on ecological meta-analysis and recent proposals for reporting standards such as PRISMA-EcoEvo.
**Results:** The review identifies a critical paradigm shift towards multilevel meta-analytic models that explicitly account for non-independence—a pervasive feature of ecological data (e.g., phylogenetic relatedness, multiple estimates per study). Despite this methodological maturation, current practices often lag; surveys indicate that fewer than half of environmental meta-analyses adequately report heterogeneity or assess publication bias.
**Conclusions:** To ensure the reliability of evidence synthesis in environmental policy, researchers must adopt advanced hierarchical models and adhere to rigorous reporting guidelines. Future research should prioritize open science practices and the development of bias detection methods suitable for highly heterogeneous datasets.

---

## 1. Introduction

The field of environmental science is characterized by an explosion of primary research data, often distributed across diverse taxa, ecosystems, and experimental designs. While this accumulation of knowledge is valuable, it presents a significant challenge: how to synthesize conflicting or variable results into coherent conclusions that can guide environmental management and policy [cite: 1, 2]. Traditional narrative reviews, while useful for hypothesis generation, are often susceptible to subjectivity and "vote-counting" bias, where the significance of results is tallied without regard for sample size or effect magnitude [cite: 3].

Quantitative evidence synthesis, primarily through systematic review and meta-analysis, offers a rigorous alternative. By statistically combining effect sizes from multiple independent studies, meta-analysis increases statistical power, improves the precision of effect estimates, and allows for the exploration of sources of variation (heterogeneity) [cite: 4, 5]. In environmental sciences, these tools are increasingly used to address pressing global issues, such as biodiversity loss, climate change impacts, and pollution risks [cite: 6, 7].

However, the application of meta-analysis in ecology and evolution faces unique challenges compared to its origins in medicine and social sciences. Ecological data are frequently non-independent, highly heterogeneous, and subject to complex interaction effects [cite: 8, 9]. Recent surveys of the literature reveal concerning gaps in methodological rigor; for instance, a 2023 survey found that only approximately 40% of environmental meta-analyses reported heterogeneity statistics, and fewer than half assessed publication bias [cite: 5, 10].

This paper provides a comprehensive review of quantitative evidence synthesis in environmental sciences. It serves as a practical guide to the theoretical underpinnings and application of meta-analysis, meta-regression, and publication bias tests, with a specific focus on the necessity of multilevel modeling to address the complex structure of environmental data.

---

## 2. Key Concepts and Definitions

To navigate the landscape of quantitative synthesis, it is essential to define the core components that distinguish it from other forms of literature review.

### 2.1 Systematic Review vs. Meta-Analysis
While often used interchangeably, these terms represent distinct processes. A **systematic review** is a formalized process of identifying, selecting, and appraising literature using explicit, reproducible methods to minimize bias [cite: 6, 11]. A **meta-analysis** is the statistical procedure used to integrate the quantitative results (effect sizes) of the studies identified in the systematic review [cite: 4, 6]. In environmental health and ecology, these are often combined (SRMA) to provide the highest level of evidence for decision-making [cite: 6].

### 2.2 Effect Size
The fundamental unit of a meta-analysis is the effect size—a standardized metric quantifying the magnitude and direction of a biological phenomenon. Common effect sizes in environmental sciences include:
*   **Standardized Mean Difference (SMD):** Used when studies measure outcomes on different scales (e.g., Hedges' *g*) [cite: 12].
*   **Log Response Ratio (lnRR):** Widely used in ecology to compare treatment means to control means; it is interpretable as a proportional change [cite: 12, 13].
*   **Correlation Coefficients (Zr):** Used for associating continuous variables, often Fisher-transformed to stabilize variance [cite: 12].

### 2.3 Heterogeneity
Heterogeneity refers to the variation in effect sizes across studies that cannot be attributed to sampling error alone [cite: 5, 14]. In ecology, high heterogeneity is the norm rather than the exception, driven by variations in species, study sites, and experimental conditions. It is quantified using statistics such as $Q$, $\tau^2$ (between-study variance), and $I^2$ (percentage of variation due to heterogeneity) [cite: 14, 15].

---

## 3. Historical Development and Milestones

### 3.1 Origins in Other Disciplines
The conceptual roots of combining research results trace back to astronomy in the 17th and 18th centuries, where mathematicians like Gauss and Laplace developed methods to combine observations [cite: 16]. The first medical application is often attributed to Karl Pearson in 1904, who aggregated typhoid inoculation data [cite: 4, 16]. The term "meta-analysis" was formally coined by Gene Glass in 1976 in the context of social sciences, defining it as the "analysis of analyses" [cite: 4, 16].

### 3.2 Introduction to Ecology
Meta-analysis was introduced to ecology and evolutionary biology in the early 1990s, significantly later than in medicine [cite: 1, 3]. Early proponents, such as Gurevitch and Hedges, argued for its utility in replacing narrative reviews [cite: 1, 2]. The establishment of the National Center for Ecological Analysis and Synthesis (NCEAS) in 1995 played a pivotal role in promoting these methods, providing a venue for synthesizing vast datasets to address macro-ecological questions [cite: 1].

### 3.3 Evolution of Methodological Complexity
Initially, ecologists adopted fixed-effect and simple random-effects models from medicine. However, it became increasingly apparent that ecological data violated the assumptions of these models due to complex dependencies (e.g., phylogenetic relatedness). This led to the development of mixed-effects models and, more recently, the advocacy for multilevel (hierarchical) meta-analytic models that can explicitly handle non-independence [cite: 5, 8].

---

## 4. Current State-of-the-Art Methods and Techniques

The current best practices in environmental meta-analysis have moved beyond simple weighting schemes to sophisticated modeling frameworks that reflect the biological reality of the data.

### 4.1 From Random-Effects to Multilevel Models
The standard random-effects model assumes that while true effects vary across studies, the effect sizes within a study are independent. This assumption is frequently violated in environmental sciences, where a single paper may report multiple effect sizes (e.g., multiple species, time points, or treatments) [cite: 5, 8].

**Multilevel meta-analysis** addresses this by introducing additional random effects. For example, a three-level model might include:
1.  **Level 1:** Sampling variance (within-estimate error).
2.  **Level 2:** Within-study variance (variation among effect sizes from the same study).
3.  **Level 3:** Between-study variance (variation across different studies) [cite: 17, 18].

Recent guidelines explicitly recommend environmental scientists abandon the standard random-effects model in favor of multilevel models to avoid Type I errors and spuriously precise confidence intervals [cite: 5, 10].

### 4.2 Meta-Regression
When heterogeneity is detected, the goal shifts from merely summarizing the mean effect to explaining the variation. **Meta-regression** extends the meta-analytic model by including moderator variables (covariates) that may influence the effect size [cite: 5, 19].
*   **Ecological Moderators:** Latitude, temperature, species traits, or experimental conditions.
*   **Methodological Moderators:** Study duration, sample size, or measurement technique.
Meta-regression allows researchers to quantify how much of the heterogeneity ($R^2$) is explained by these predictors [cite: 14].

### 4.3 Handling Non-Independence
Non-independence is a critical threat to validity. Two primary forms dominate environmental data:
1.  **Phylogenetic Non-independence:** Closely related species tend to respond similarly to environmental stressors due to shared evolutionary history. This is handled by incorporating a phylogenetic correlation matrix into the multilevel model [cite: 12, 20].
2.  **Hierarchical/Nested Data:** Multiple observations from the same research group or site.
Solutions include using Robust Variance Estimation (RVE) or constructing a variance-covariance matrix to model the dependencies explicitly [cite: 8, 21].

### 4.4 Publication Bias Tests
Publication bias, or the "file-drawer problem," occurs when studies with significant or positive results are more likely to be published. Traditional detection methods like the visual inspection of **funnel plots** or **Egger’s regression** are often ill-suited for ecological data because high heterogeneity can distort funnel plot asymmetry, mimicking bias where none exists [cite: 22, 23].

**State-of-the-art approaches include:**
*   **Multilevel Meta-Regression for Bias:** Extending Egger's regression to hierarchical models to test for bias while accounting for non-independence [cite: 22, 24].
*   **Time-lag Bias Tests:** Assessing whether effect sizes decrease over time (the "decline effect") [cite: 22].
*   **Selection Models:** More complex approaches that model the probability of publication based on p-values, though these are computationally demanding [cite: 22].

---

## 5. Applications and Case Studies

Quantitative synthesis has been applied to a wide array of environmental questions, influencing both basic science and policy.

### 5.1 Biodiversity and Climate Change
Meta-analyses have been instrumental in quantifying the global fingerprint of climate change. Landmark studies have synthesized data on phenological shifts (e.g., earlier flowering times) and range contractions [cite: 7, 25]. For instance, highly cited meta-analyses have aggregated local studies to reveal global patterns of species redistribution, providing the evidence base for IPCC reports [cite: 7].

### 5.2 Environmental Health and Toxicology
In environmental health, Systematic Review and Meta-Analysis (SRMA) are used to assess the risks of chemical exposures. A review of 48 environmental health SRMAs demonstrated their utility in linking chronic low-dose exposures to health outcomes, although it noted weaknesses in how exposure heterogeneity was handled [cite: 6, 26].

### 5.3 Conservation Interventions
Meta-analyses evaluate the efficacy of conservation strategies. For example, syntheses have examined the impact of protected areas on species abundance or the effectiveness of different restoration techniques. These studies often employ "forest plots" to visualize the effectiveness of interventions across different biomes or taxa [cite: 20].

### 5.4 Case Study: The Value of Statistical Life (VSL)
In environmental economics, meta-analyses of VSL estimates are crucial for cost-benefit analyses of environmental regulations. Recent studies have employed two-stage random-effects and multilevel models to synthesize VSL estimates, accounting for the non-independence of multiple estimates derived from the same survey populations [cite: 17].

---

## 6. Challenges and Open Problems

Despite methodological advances, the field faces significant hurdles.

### 6.1 The "Apples and Oranges" Critique
A persistent criticism is that meta-analysis combines studies that are too dissimilar ("mixing apples and oranges") [cite: 2]. In ecology, where no two field sites are identical, this is a valid concern. However, proponents argue that exploring this heterogeneity is the very purpose of meta-analysis—to determine if effects are generalizable across different contexts [cite: 2, 19].

### 6.2 Reporting Deficiencies
A major impediment is the quality of reporting in primary studies and meta-analyses themselves.
*   **Primary Studies:** Often fail to report sample sizes, variances, or necessary statistics to calculate effect sizes, leading to data exclusion [cite: 5].
*   **Meta-Analyses:** A 2023 survey revealed that less than 50% of environmental meta-analyses reported heterogeneity statistics or tested for publication bias [cite: 5, 10]. This lack of transparency undermines the reproducibility and credibility of the findings.

### 6.3 Complexity of Non-Independence
While multilevel models offer a solution, they require sophisticated statistical knowledge and software proficiency (e.g., R). Many practicing ecologists may lack the training to implement these models correctly, leading to the continued use of inappropriate fixed or simple random-effects models [cite: 3, 5].

### 6.4 Publication Bias in Heterogeneous Data
Detecting publication bias remains difficult when heterogeneity is high. Standard tests (e.g., Trim-and-Fill) perform poorly in the presence of high between-study variance, which is characteristic of ecological data. There is a lack of consensus on the best bias correction methods for complex, non-independent data structures [cite: 22, 23].

---

## 7. Future Research Directions

To advance the field of quantitative evidence synthesis in environmental sciences, several directions must be pursued.

### 7.1 Adoption of Reporting Standards (PRISMA-EcoEvo)
The medical field has benefited immensely from the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines. The recently developed **PRISMA-EcoEvo** extension addresses the specific needs of ecology and evolution [cite: 27, 28]. Widespread adoption of these guidelines by journals and authors is essential to improve the transparency and utility of meta-analyses [cite: 5, 29].

### 7.2 Open Science Practices
Future meta-analyses should embrace open science by archiving data and analysis code (e.g., R scripts) in public repositories. This allows for reproducibility, updates as new data become available, and the use of data for "second-order" meta-analyses [cite: 30, 31].

### 7.3 Advanced Methodological Training
There is a clear need for curriculum development to train the next generation of environmental scientists in advanced meta-analytic techniques. This includes training in:
*   **Network Meta-Analysis:** To compare multiple interventions simultaneously [cite: 4].
*   **Spatial Meta-Analysis:** To explicitly model spatial dependencies and autocorrelation in environmental data [cite: 32].
*   **Phylogenetic Comparative Methods:** Integration of evolutionary history into evidence synthesis [cite: 3].

### 7.4 Improving Bias Detection
Research is needed to develop and validate publication bias tests that are robust to high heterogeneity and non-independence. Simulation studies comparing the performance of selection models versus multilevel regression approaches in ecological scenarios are critical [cite: 22, 24].

---

## 8. Conclusion

Quantitative evidence synthesis has transformed environmental sciences from a descriptive discipline into one capable of generating rigorous, generalized inferences. The transition from simple statistical models to advanced multilevel frameworks represents a necessary maturation of the field, acknowledging the inherent complexity and non-independence of ecological data.

However, the potential of meta-analysis is currently limited by suboptimal reporting practices and the slow adoption of these advanced methods. As environmental challenges such as climate change and biodiversity loss accelerate, the scientific community must commit to higher standards of evidence synthesis. This involves not only the application of robust statistical models—specifically multilevel meta-regression—but also a cultural shift towards transparency, open data, and adherence to reporting guidelines like PRISMA-EcoEvo. By doing so, environmental scientists can ensure that policy and management decisions are based on the most reliable and comprehensive evidence available.

---

## 9. References

[cite: 3] National Center for Ecological Analysis and Synthesis. (n.d.). Meta-analysis in Ecology: Lessons, Challenges and Future. https://www.nceas.ucsb.edu/workinggroups/meta-analysis-ecology-lessons-challenges-and-future
[cite: 2] Stewart, G. B. (2010). Meta-analysis in applied ecology. *Biology Letters*, 6(1), 78–81.
[cite: 1] Koricheva, J., Gurevitch, J., & Mengersen, K. (2013). *Handbook of Meta-analysis in Ecology and Evolution*. Princeton University Press.
[cite: 4] Wikipedia. (n.d.). Meta-analysis. https://en.wikipedia.org/wiki/Meta-analysis
[cite: 16] James Lind Library. (n.d.). A historical perspective on meta-analysis. https://www.jameslindlibrary.org/articles/a-historical-perspective-on-meta-analysis-dealing-quantitatively-with-varying-study-results/
[cite: 5] Nakagawa, S., Yang, Y., Macartney, E. L., Spake, R., & Lagisz, M. (2023). Quantitative evidence synthesis: a practical guide on meta-analysis, meta-regression, and publication bias tests for environmental sciences. *Environmental Evidence*, 12(1), 8.
[cite: 10] Nakagawa, S., et al. (2023). Quantitative evidence synthesis: a practical guide... (Preprint). ResearchGate.
[cite: 33] Nakagawa, S., et al. (2023). Quantitative evidence synthesis... (Preprint). EcoEvoRxiv.
[cite: 30] Nakagawa, S. (n.d.). Meta-analysis tutorial. GitHub. https://github.com/itchyshin/Meta-analysis_tutorial
[cite: 11] Mengist, W., Soromessa, T., & Legese, G. (2020). Method for systematic literature review and meta-analysis studies on environmental science. *MethodsX*, 7, 100777.
[cite: 6] Whaley, P., et al. (2015). Systematic review and meta-analysis in environmental health... *Current Environmental Health Reports*, 2(3).
[cite: 26] Mandrioli, D., & Silbergeld, E. K. (2016). Use of Systematic Review and Meta-Analysis in Environmental Health Epidemiology... *Current Environmental Health Reports*.
[cite: 14] Pires, P., et al. (2025). Harnessing meta-analyses' insights in ecology and evolution. *Royal Society Open Science*.
[cite: 31] Page, M. J., et al. (2025). Transparency and reproducibility... *Sports Medicine*.
[cite: 34] YouTube. (2025). Landmark meta-analysis environmental science examples.
[cite: 35] U.S. EPA. (2025). CADDIS Case Studies.
[cite: 22] Nakagawa, S., & Sanchez-Tojar, A. (2021). Methods for testing publication bias in ecological and evolutionary meta-analyses. *Methods in Ecology and Evolution*.
[cite: 23] Nakagawa, S., & Sanchez-Tojar, A. (2021). Publication bias tests... (Preprint).
[cite: 24] Nakagawa, S., & Sanchez-Tojar, A. (2021). Methods for testing publication bias... (ResearchGate).
[cite: 36] Crystal-Ornelas, R. (n.d.). Meta-analysis of Ecological Data: Publication Bias.
[cite: 7] Bellard, C., et al. (2015). Highly cited papers in biodiversity and climate change research.
[cite: 25] Brook, B. W., & Fordham, D. A. (2015). Hot topics in biodiversity and climate change research.
[cite: 8] Song, C., et al. (2020). Handling nonindependence in ecological meta-analysis. *Ecology*.
[cite: 9] Noble, D. W., et al. (2017). Nonindependence and sensitivity analyses in ecological and evolutionary meta-analyses. *Molecular Ecology*.
[cite: 13] Noble, D. W., et al. (2017). Non-independence and sensitivity analyses... (ResearchGate).
[cite: 37] Gurevitch, J., et al. (2013). Statistical Models for the Meta-analysis of Nonindependent Data. *Handbook of Meta-analysis in Ecology and Evolution*.
[cite: 21] Nakagawa, S., et al. (2021). Comment on Song et al. *Ecology*.
[cite: 20] Cinar, O., et al. (2025). Examples of forest plots... (ResearchGate).
[cite: 12] Nakagawa, S., et al. (2017). Methodological issues and advances in biological meta-analysis. *Evolutionary Ecology*.
[cite: 17] U.S. EPA. (2024). Guidelines for Preparing Economic Analyses (VSL Meta-analysis).
[cite: 15] Horvatinec Isaković, J., et al. (2025). Methodological issues... (ResearchGate).
[cite: 18] Senior, A. M., et al. (2016). The nutritional ecology of obesity... *British Journal of Nutrition*.
[cite: 5] Nakagawa, S., et al. (2023). Quantitative evidence synthesis... (ResearchGate).
[cite: 19] Noble, D. W., et al. (2022). Nuisance heterogeneity... *Journal of Experimental Biology*.
[cite: 2] Stewart, G. B., et al. (2010). Meta-analysis in applied ecology. *Biology Letters*.
[cite: 1] Koricheva, J. (2013). Handbook of meta-analysis in ecology and evolution.
[cite: 32] Nakagawa, S., et al. (2023). Quantitative evidence synthesis... (PubMed).
[cite: 38] Nakagawa, S., et al. (2023). Quantitative evidence synthesis... (PDF).
[cite: 14] Pires, P., et al. (2025). Harnessing meta-analyses' insights... *Royal Society Open Science*.
[cite: 27] O'Dea, R. E., et al. (2021). Preferred reporting items for systematic reviews and meta-analyses in ecology and evolutionary biology: a PRISMA extension. *Biological Reviews*.
[cite: 28] O'Dea, R. E., et al. (2021). PRISMA-EcoEvo... (ResearchGate).
[cite: 39] Monash University. (n.d.). Preferred Reporting Items...
[cite: 29] PRISMA Statement. (n.d.). PRISMA for Ecology and Evolutionary Biology.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL-nXg6CM7GxlfcFpsvhw82JCytNVlJOd3LcmnlBlAzNyj--dEpXxrqdGQP3jxbTJQ6vKiPE8_c6-tP002MKvhFjhpzdGfwIqym5wAaljEpWgU92hj6Z1DjhoeqQ3wcdbOW7Tr3pUyPGl3mncnNIWsZiKQIxica1iFITPdanB2R6pV3w4ghbxQS2zLDCrW7hqXEkwDnrFWzp4O1XF3SG-3ict9Bi3MqNK6lL7pqh5HVxibFFWSgfvPW9T9AMdEVe6DngHdkaYjWbGVCJ91fvsFwcDK3HPUmByd2FCuHpEYGNSUmKqvYbr884w8yvxT_Chlt2FJga-8XEDEKfi3gGjkF21MpJJDrt4o9yGezUOHygEm3q3t7PfVpFG8pvU5exkOuetgOLkbemAKIFZANXk2Ek85WUjsgAnSutTkRwUFEmW_kpshgG5S-LHuXkJUWAHybN42b_E7pGI=)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxVRcmJAvaWiQeKt81MKPYgoztXRCyDwO0tGdcvzM8UIXOOGU4CfZNPKyBzWL7M27A5JU6W-JQtcoQbQCNedT6gTpmHB1AVsml20wvzq38Uk_hqpF0izyB6Lw5vSrhGxPPsAd28jhc)
3. [ucsb.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA95R-rJVmuVfEVKsfMt1RTX8ogM3UykiqMv1kBVqZvp0le-o4KPnfpWTvQK0onk704kCTwyA2lOZUVcyetMUS5Vmxi1FuzxMEtqaAIszMRvM6aqSSqAegE7Dvsrdl2_8GLaUls4P1mMBFgpHigovEFd9GdcXcv7dbr79AXxqnjd5zsuybTUjJBIZo-FqQ-Q8EcQ==)
4. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx3jOzvK7tlPFZ3z16faiA1E8xPi0bFXmU_vsWGcrwUGPzpkTyaUISzSdjVwZCXj6AE-hVpHxYgVzngsL69Hu3Yom5ox1mohj6FERDTIIB-6WdKDTDoEEIq45kuiATFuDu)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnnIpfpwK2Jma2KGFNq_c6ddhE1xEDm1i-naJRAi2xahis9H9k8wWYR-e1LrpHpSFcEIKBdJPPT-Xh8EpKWIkNBkHv19iH3Ft4kUnjynoZedo19lD1bhYSKAxi8SrNIIqL-Vjr5XYdhbOIcbuG_OJ381Y9nGFVP0OWM9o5ZPiyXtCZP-0Zmt6eIW-b17lCyNEofwMCbQ8ajng6btsi7dBqsNDZs2_-quenpeVzPOPx0osBmOf6fqLGsQK7m2QEf3ZA7rR_PhVq4zVdCGsSd_SNj6p-brUkjrHhACUgj00eNMgbsEfKw4vABrE7p-gGmBvkow==)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtZfl-3DP3DOTe1Js_9P1Bk2RRk9LLLrCGIUgP7qVq8rdgvC9gqGvoj_xomH6eCDs8GlMQPVfs3udrYCaupruNPIZjRltj5hfUPh9OJMssCQdZ-eMbvqHflcH6lO1qKsLiiZsjj7XC)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5c7UNVJdp-Ltin9D_yO59IOG-CADsltDxSz90vfE82zRa3PIbkWAbAmvbtGUelDtqqql-q3bcAtUzHL65an0lK54TWl-FHZy4NZWigvrUba1-AS9msdgZzHx7QKVRZejSdQBAjS7X)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0AG2rHZFbYvVqf7UIVsWnsxMXUvX70eACJw_m6fjG7EkLXcXxhuTyTpXCizJ1Jo7E5qpWXagjoGvMD04V3CtwVbF5LqCic4b7TyyeS6tcF3RQMG08yc8NbcvUQIqbcQ==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXoOnxKoTRr6ktgBYgdtmr_aJpcZazn2vuM0IP7769L59AxY7jOVB11ggVG5MiPmWfsZPGAsZY4flbn-WRqyUtNSHMKXOttWo0abMGZjzPo4M-MHd0_hifM5lPwNKMsw==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKxTMvqOVHUM-TgZ_Jui6RlQOxyYVZTL5SDN20E1vbpTmmqaFNnPhhcKxCh0DZPui5pCE40u9es67VtcJsjghTmgZu1zazFJqWPwT783Eg1ZmkPkswJCTv5v-_5ygYKNZqSNoxAK8gty-GyRiJ585zDbb-Odgcm8EDWjOPoitM8DtqTFTDahaJk9QVgJ64ZtLLD2PU3dLpI_lKY1KBkl22prBp_HZl0axFaEt16Z7sEmJ-9CYTXCoIRuZJBop2KHBDO_ss5hHsrdFtW7P8gBRI9IEcKIiSu8IGAqyx_8A_Qe2JKqE73MMRCFakn4WPAWkZiA==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5om7w3EBosgM_ZGIxP7rAxG4DGHdZNPas5AwCVtgIz1hj663wmk9ZtSxX92LF1aI76rDUnN_Owr4WbQHhUzRA3x3e72VRPETzzkCXkiOHRlczdEIrA8c6-OPej5GCGw==)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKauFD07ijEMFGZtIPR6TVAVaEUp1MpUkYiP5D-G1ULizreViL8Mrz_EE-M4Ao5MWr8ZCk4BUxsFdzIq7RriFJKWGwUiiE-7VgQlL0F_rzcktTd3te6f8OLYpiMANnrPvGIA0R4DRr)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIxIbTeTQDukqeyi9u8z4i8fkqQTDB9QcXLvtbziXD6blSYFr14uyxDYlr12KGoleEjYhLymsFtddT_IYPHBOSZVLUuYK-074UAKlaB7cnyoVLc9uak_fy1jwQzZH0Gnr4kwAZYmYNJXbf-n5V6qT8V1reX8v8i94_6LO2Lnxo3UXc0kRa9s1BsvBHsynyMZi09j7FIXuqy7sH4Ld66febYBdSf5NDJdw7XZjJwtrkmnW2tmf9MdbmCERU_jQhFds=)
14. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHOpKlbw5azJTTJ-a9-zU1DAS_2-uBspbDv_LTn1_Ua1AZCq4xP5Fu5hXL2t7Vj8S9FptyySCE6FDJS3yCyhMunadBF_8VVtUUzxfPZQxgI55yFDxjw79sRt8QL9ocZODgbwR9Esa4-cVCmP1rnpIPORD1sR1n56eaQBXu8zq9Z9bVkwbsLBhoUfQmoIjE8JxG15okxR3ySbwXyAGGrzvvLUs6RzPcbuivuQ==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8x2gouuxO_YrU--Bj1rRMrkpL9SD5wze40Qp__GmSKDVtkpgHyQcDY2tv_HQrNml_IcO4j95jM9ZRKq_TeWZn3IvfgospvVrbwtVpS06IxhZANXSyHpV42vxhloF0bTiw6wyNug2vJ-iOKd_OMA6dW1G7B4V5PNI7BmqRP3GvHIko5CNDzKWpiox3Mti2dbD3A4T6V_BCfd-P07yskJMF0TsShR5RYQ==)
16. [jameslindlibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_g5oEhoVLjoERwaCGkhvmNd95xByjKUln9H46PnZBbtqj1PRGEM3L4HJwZ3OoDttsKDnoAy0SN75_IDAMiU9ztjsgI7hsknjlGDBXBuGmrfZUh464P7s4H_bPOfHxd5dZZ9vx3njKQJf7174sII-9Y9Bn2OsJBKb1HBJpDAeq_zlmO7AfSavegV2ME-GrmBZbUfr_wACKwWBCCcA3d_84-_Lxfp7hsqeAgABBcUduVSLcd6Cm2-TjV8Y-HBo=)
17. [epa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvhNQWvBXfsVNZ-_ia9GwlQIa6oXVs2l4UX_iOfdKmVVyLFIP21u6jx7YGoSuBK9UBlS9ZweAwmBfK-MR7yLhMe3b5nzlmvA67J_SRwbweCPMalv5ngWv5VqhuFYakCkklg4uv6P76zPz5J82_CDxuq1vTL60adw==)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpykf9LGfcMPE-k1om1qXVkSZZBRQ7478WAlOaU655Cb90ZppxKzs6ip8PgB6f7QvKXiLOhJYUedkFU-CfOkX92djEEEoQTCqiOUYA48nqhr38DgfV4mququUoUz9sgHrnoGLBUOXA)
19. [publicationslist.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2fbQwASrBBQfGlK6FQbxQHXl8_GTDLqj3WHbAMGUnig2GOaEXFoyxbF5I_XvMk7hPZoouYO1THHpUYl1Boqpg82mDZW6ZMkzkg7J7AyTC49qCAjDONPhOS1_4ElkfF-kvlk0dz_ZTyD8grmGSIN6tqcXysSiEfIgK9-GWUtMYyrvd2p2ML2AaQ0ZEyqQuMk33zHoLPhvj5oc=)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJv_4r0vG6xCYrarA6Y0LeVzSbUW8oF6gB3B0V-YrioLX-eShj_KE_Cd2a6KM4kXtypztBHzt441ReM9qMomWtMrwMQTbhpRqMOyZScJwC4bFrFxbiyRH9NtS8_8I-PyIrmtMviB_EX4_aL3l5wY1_bK9sx2vKd02YS8urmWuALVNq8EnVIrQ3wCZSQT6-cwrUnMAVakzErUXxfmZRubc3HjndU_Pw3_eV2WPHzTIy2OEHxFybqvZgw1q6kD8kOiYY7Rc=)
21. [publicationslist.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmwamyT6cCayFoV0J4RdcYvmMJ6mfzzEO3s2RA_b1LKNQXmveD3mHF_r10dUXVRWpjvfbDYng2XC7dgzLwmCzbPWX2mYhWsNpyYMRdiWEFP_Ugr2dqZ_IaUnRltxnIwpIKr_QdNNHJ4MQULvUIYsCcm5o-51ZOs_Wz1fICCdbtoIcSL0Zf4TGVPt7fYc7Iekyn6QMUF0m_WoM0-YNdwVUXXNXso-XKTh0=)
22. [anu.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP1PLahLWgXPo2tAmVfSKmDnTVTQtjIgzhwfgUVjSq6zEgp-eMGHqlDqUyVEODpN1QEGytkV-z316rb6HVrB5o9_pQWvE9KJfaNu81r1u2R7axfRrz21b4kzD82AnhB_5bvXAO5v_7kM9vqEPZc4vum6-OIH2xEyuKnaIbhB6II8X97vR8nvgZs_-G)
23. [weebly.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVgOIA7kkU_HcB52qO6h4pGoXtFShLLwY4ltMp-Y4IDc870nEKBp-Z0-dWjz-XlAvIANIJEY8g-qXX-sKVNsuWXfuud07Xy6OrBzbztaVlSRwzoFWsrKZrPoroBxy9lilaws2OoEm940nUocvYHGvTUZ8a3CSwu3bZK2ZH)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhZrm9VeYf9L3Y4UlSY83u18YwGbo85cBTDScha-gPb2_QiLRw1CadOFc0qWNQbvYRbKEk8kZvWnt7j8UsLlWYrYi7Jd3FuNNGFvfreamEgYpl-vhrFooU7LHaxvLX1p0tYaFsKTd7BRe_Ysz4fp5oSGsDnEplO4jI-HUyOR6DAlep1Tf_WVdb13OjAGnMrMGX6FTLrRvG_iA6p-arS6uzUfhHzT4tvJ8P67lednibGPjX4gXu5AICz2wp)
25. [dulvy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAlyni3vopvsaj8SUHhkdjA3iVyD93briOGXUxKnZFDWeAIwYmg3Jv9KTgWwB6Q0oHdjXos1pbr1MQ0_ZLfiOliH3a4sTZb04v2kBE2Cdx2PZhrGuJpUrjKsHJYxBuaaY_RKQtTlzVNEYD8VuhGRsim_mHM10_CqAdAqVCez-aASvDqczGzL9o)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz0yzc4Jw5OqHVbzCnVlvqqTNI9M22P1DaIM92tPvzxMBGxX-pWjRH5cMV38SdlWW6wOrtZiSS6PmAEOXytoTSOzRnccuvOGTTVW8QfiqP0N455omekysTfp2s3x15Cc8dNHjnJncLCHapj-T5_ZGS8MZwzmqL1X1AcLHEJoMl90KV6rC1ySp4iTEQLp879i6smx61h124XlhZ91hIr7ciczzbvTF6zcJvz5hLacLtHUreJXz2Fbf4-4C0CMUMNcXnp2aBsKZyDO8JN3NgEmWMCGCboBim81S_kl5kxddIM8Zmh3EOkSuhg8EvGw==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHme2i608WZWDYFZjg8IfHmosTg0j5PsbDOEt_lhCP_BHEppvde4u4La6U4iaRn2Jx5P083WmErfqpiOmmAaSWu1lF09qkRrpTeyBz-F2GAU7HdaCRm5mlcM_glbYeug==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaZHXCAQ6U69S_7zSiEhELF-uWuLnan2Q0WR7GNeeSUlbbUhdTMDx8s5-IwQzMgI6rQZ220CUsbM_5DANy6s5ED2fhzlnDczU5aByF54BahCwmAZEDcuzPaIKG4FX5_yKG6DGJmgNJrKPMojtn5f9N7ni_ZRQsuXY5dMML8igfipPo-kRYP5uckZrLK6ika5tQ6NJY0wUrEOVutKl7g1CeQl90ZG33ie2bzfTlrucCSJ15g7gvJwUstTEHcMOKUw==)
29. [prisma-statement.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu8saxe7LvW5KS-BvGa7IhGF5ePgSE07Tlyj3OiBd27dNFku2VadYSHF0OZRdfxPi7WvP6dccYl7llttbP7OUWvNbV6U18vrZLA9AwECIWAu3wgMcVMAKKDRfWfqk=)
30. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Dp0ctsV7aWJ6AL3QMdYZtGvrrO_vMlBUOrA__wWRQKE1TmbKambZQSELip2tJxTcfdUwesJM1ZhSg9Lnpe5W3586IM_BDB2R7jnKnfwyS-q3nKlkBUUnzrVMDrO_HDc44j5hXRgo7Dc=)
31. [sportrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgXlGE3ekQOnpkLp0DsUJPeMcCUKnUNvJp_OAlTXg9HlB_qJSCnO1DHlx4JPPhN-wvyS8q88fuH8riQKo907es--VjF-PnhHWVthNKLRFh0qcO-5qi3WqgwWjmF2oFQgeScXIWUI890mweyChs9w==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8tj12A_8tOlGpRDRyW-WStS0oTST9t1ENh3GYZr_P1fYkWW_vNnVPsuDQpnKlSCgJnYlg2AJ0LZVUaY78SPMXRTTStzxpdY41JDiMZIhr5snS4LNzc99xPErxjPfQew==)
33. [ecoevorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9CcUUwVjpKWm_MRbWwb7widPgp2G6tdJRlfmljIDYu0qCT1rXg21KbRiutBSIbPjYIzYMXMZGf8D6SpG48_FRLCM5sY-iDPEuLWJJKV4yhIEbdJ168yeE9wKsSr_5PK4jlQ==)
34. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJmNrjjkx-vY8gaViHI-8brQpBe1ZRDgWawpimZ-vqZPZpZX-ei_B1hQQtAqltOrPZ1_LRPezWJVH9uLX4pVvReCSC5c54uaXu89Er9gzOCQ4J8C_EB7T4sJU2B_jx9zYx)
35. [epa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzohs95bvM9sR11mOuVNvyPx--5RuARRCbM2336QZZnP9WImRnFk3c6zNl82R7WL7sQS-3BkySNWr7JqB3MeYvr24Ua9gRvKHALAh7KblureFSvmPnaiLAgBj2pLI=)
36. [bookdown.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQYpI0tOd-4LXcIZk8HA72_uUpcsg7Zd6zpKibt2kJ079FqHcCnJyHSz6P0rAhL-59IlK1jpjTJfHoB4mVKYjUjTziHXi4XOu_0ZAcVRrpiwOEvyqK0xNS9HH6YpukH_Gx54PBqh4zrg1LxA_AGTGiwj8o57xAN72rbNMCMCCs1Dk-jYbPyWdeU8vE7SCbR30kbQk=)
37. [doi.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvXj6wFxPg4bo7IFt9DfovZoSXjb7DpMZYYGcSgnlkpWXyHK2c7B_JyVnHg9Fx9eoqMsUmfSOf_c33X-frg8ctK4Usue-x_8GYO_W6KxEuzvF5oVnncwqY5FL0PJOQzrS10GJWEWN8uYXxScVaK90=)
38. [reading.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8qXup5tZVgFpBoVIIUgk6adzDdhQngF4gfC7-hJADxhaDnRToJ4M7Hviw-BMC_hlw4dtmZQmofBe_PHCgn4bMh_1MBG2A2fD5NoAqMMzC1AgIy_HjEzfG-xYowuEkJWvA9AwTK2Q_eAyKSrQ3BH3JdqIH)
39. [monash.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt95sr7r1CWQnQ53C1kUeB4HssQPqVtnl7kXCLwe2plSlBmFOTQ77oBPm8dGuhsKY-Mpk0UXQLlnhwbrRWqKOs4kgTOadRByTxms5SV_PpESOH-lz7v73DtXHTAPqfWzmpQW4CxjLyxd36sBbezq0FFnZeKZDJyGnheJsqEdALfAdWgdxjWmnSfQrLxWY2CliJ5a9r6nKj_BRE9J7grQzM1l27Bg==)
