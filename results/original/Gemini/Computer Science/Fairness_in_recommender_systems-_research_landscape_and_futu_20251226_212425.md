# Literature Review: Fairness in recommender systems- research landscape and future directions.

*Generated on: 2025-12-26 21:24:25*
*Progress: [31/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Fairness_in_recommender_systems-_research_landscape_and_futu_20251226_212425.md*
---

# Fairness in Recommender Systems: Research Landscape and Future Directions

**Key Points**
*   **Paradigm Shift:** The field of Recommender Systems (RS) is undergoing a fundamental shift from purely accuracy-driven metrics (e.g., RMSE, NDCG) to "trustworthy" AI, with fairness as a central pillar alongside diversity and robustness.
*   **Multi-Sided Nature:** Fairness in RS is complex because it involves multiple stakeholders. It must balance **Consumer Fairness** (users receiving unbiased recommendations) and **Provider Fairness** (items/creators receiving equitable exposure), which often conflict.
*   **Methodological Evolution:** Techniques have evolved from simple post-processing re-ranking to sophisticated in-processing methods, including **Adversarial Learning** (to unlearn sensitive attributes), **Causal Inference** (to de-confound popularity bias), and **Graph Neural Networks** (to correct structural bias).
*   **Emerging Frontiers:** The integration of **Large Language Models (LLMs)** introduces new challenges regarding semantic bias and intersectionality, while new legal frameworks like the **EU Digital Services Act (DSA)** and **AI Act** are moving fairness from a theoretical goal to a compliance requirement.

---

## 1. Introduction

Recommender systems (RS) have become the primary information filtering mechanism of the digital age, governing user experiences across e-commerce, social media, streaming platforms, and employment markets [cite: 1, 2]. Historically, the primary objective of these systems was to maximize utility—defined by metrics such as click-through rate (CTR), conversion, or rating prediction accuracy [cite: 2, 3]. However, a growing body of literature has demonstrated that a singular focus on utility often exacerbates systemic biases, leading to unfair outcomes for specific user demographics or item providers [cite: 4, 5].

The motivation for fairness research in RS stems from both ethical imperatives and practical sustainability. Unfair recommendations can perpetuate societal discrimination (e.g., gender bias in job recommendations) and degrade the long-term health of a platform by alienating minority user groups or niche content creators [cite: 2, 6]. Consequently, the research landscape has expanded to include "Trustworthy RS," where fairness is treated not as a constraint but as a core objective [cite: 7].

This paper provides a comprehensive systematic literature review of fairness in recommender systems. It synthesizes the historical development of the field, categorizes state-of-the-art methodologies (including adversarial and causal approaches), analyzes real-world applications in high-stakes domains like hiring and the gig economy, and identifies critical research gaps regarding intersectionality and Large Language Models (LLMs).

## 2. Key Concepts and Definitions

To navigate the literature, it is essential to distinguish between *bias* (a statistical property) and *fairness* (a normative value). While bias refers to the discrepancy between model predictions and ground truth (often caused by data artifacts), fairness reflects the social requirement that the system should treat individuals or groups equitably [cite: 2, 6].

### 2.1. Taxonomy of Fairness in RS
The literature generally classifies fairness in RS along three orthogonal dimensions: the stakeholder (subject), the granularity (level), and the optimization objective [cite: 8, 9].

#### 2.1.1. Stakeholder Perspectives
*   **User Fairness (C-Fairness):** Focuses on the consumers of the recommendations. It ensures that different user groups (e.g., grouped by gender or race) receive recommendations of comparable quality. For example, a medical RS should not provide less accurate health suggestions to minority groups [cite: 8, 10].
*   **Item/Provider Fairness (P-Fairness):** Focuses on the items or their creators. It ensures equitable exposure or attention for items. This is critical in two-sided marketplaces (e.g., Airbnb, Uber, Spotify), where the livelihood of providers depends on algorithmic visibility [cite: 8, 11].
*   **Multi-Sided Fairness:** Attempts to satisfy the fairness requirements of both users and providers simultaneously. This is computationally challenging as C-fairness and P-fairness are often zero-sum games; improving exposure for niche items (P-fairness) may temporarily reduce recommendation relevance for users (C-fairness) [cite: 9, 12].

#### 2.1.2. Granularity: Group vs. Individual
*   **Group Fairness:** Requires that the system treats defined groups (protected classes) equally. Common metrics include *Demographic Parity* (independence between recommendation and sensitive attribute) and *Equalized Odds* (equal error rates across groups) [cite: 13, 14].
*   **Individual Fairness:** Based on the principle that "similar individuals should be treated similarly." This requires a distance metric to define similarity between users or items, which is often difficult to operationalize in sparse data environments [cite: 8, 13].

### 2.2. Key Metrics
Research has adapted metrics from classification tasks to ranking tasks:
*   **Exposure-based Metrics:** Measure the visibility of items. For example, *equality of exposure* demands that the exposure of an item group is proportional to its relevance or size [cite: 4, 10].
*   **Utility-based Metrics:** Measure the satisfaction of users. Differences in NDCG or Recall across user groups indicate unfairness [cite: 10].
*   **Intersectionality:** Recent work argues that single-axis metrics (e.g., race *or* gender) are insufficient. *Intersectional fairness* considers subgroups formed by combining multiple sensitive attributes (e.g., Black women), which often face compounded discrimination [cite: 9, 15].

## 3. Historical Development and Milestones

The evolution of fairness in RS can be traced through distinct phases, moving from awareness of bias to sophisticated mitigation strategies.

### 3.1. The Era of Accuracy and Bias Discovery (Pre-2015)
Early RS research focused almost exclusively on accuracy (RMSE, MAE) and matrix factorization techniques [cite: 3, 16]. During this period, "bias" typically referred to statistical deviations like *popularity bias*—the tendency of algorithms to over-recommend popular items at the expense of the "long tail" [cite: 2, 17]. While not initially framed as a social justice issue, this laid the groundwork for understanding how algorithms distort information distribution.

### 3.2. The Rise of Fairness-Aware Machine Learning (2015–2019)
As machine learning began impacting high-stakes domains, researchers translated fairness concepts from classification to recommendation. Seminal works began to address specific biases, such as gender discrimination in career-related ads and the "filter bubble" effect [cite: 2, 18]. This era saw the introduction of post-processing methods (re-ranking) as the primary intervention strategy [cite: 19].

### 3.3. The Trustworthy RS Paradigm (2020–Present)
The field has shifted toward "Trustworthy RS," where fairness is integrated into the model architecture itself.
*   **Causal Revolution:** Researchers began applying causal inference to distinguish between correlation (user clicks) and causation (user preference), addressing biases like *position bias* and *conformity bias* [cite: 20, 21].
*   **Legal and Regulatory Pressure:** The introduction of frameworks like the EU AI Act and the Digital Services Act (DSA) has forced the industry to move beyond theoretical metrics to auditable transparency [cite: 22, 23].
*   **Generative AI:** The advent of LLMs in 2023–2024 has introduced "Generative Recommendation," necessitating new definitions of fairness related to semantic bias and stereotype propagation in generated text [cite: 24, 25].

## 4. Current State-of-the-Art Methods and Techniques

Contemporary approaches to fairness in RS are categorized by the stage of the pipeline they intervene in: Pre-processing, In-processing, and Post-processing.

### 4.1. Pre-processing Methods
These techniques modify the training data to remove bias before the model sees it.
*   **Data Balancing:** Techniques involve up-sampling minority groups or down-sampling majority groups to achieve statistical parity in the dataset [cite: 19].
*   **Counterfactual Data Augmentation:** Recent methods generate "fake" interaction data to simulate a balanced world. For instance, if a user interacted with a popular item, a counterfactual sample might simulate an interaction with a less popular but similar item to mitigate popularity bias [cite: 10].

### 4.2. In-processing Methods
These methods modify the learning algorithm to optimize for fairness alongside accuracy.
*   **Adversarial Learning:** This is a dominant approach where a "generator" (the recommender) tries to produce embeddings that are useful for prediction but from which a "discriminator" cannot predict the sensitive attribute (e.g., gender). If the discriminator fails, the embeddings are considered fair [cite: 18, 19, 26].
*   **Regularization:** Fairness constraints are added directly to the loss function. For example, a term penalizing the correlation between predicted scores and sensitive attributes allows the model to learn a trade-off between accuracy and fairness [cite: 19].
*   **Causal Inference:** Causal graphs are used to model the generation of interactions. Techniques like *Inverse Propensity Weighting (IPW)* and *Backdoor Adjustment* are used to de-confound the effect of item popularity or display position from true user preference [cite: 20, 27]. This is particularly effective for "long-tail" item fairness [cite: 17].
*   **Fair Graph Neural Networks (GNNs):** GNNs are prone to amplifying bias because they aggregate information from neighbors (homophily). State-of-the-art Fair GNNs use topology rewiring or fair message-passing mechanisms to prevent the propagation of sensitive attributes across the graph [cite: 17, 28].

### 4.3. Post-processing Methods
These techniques re-rank the output of a trained model.
*   **Fair Ranking:** Algorithms like *Detriment* or integer linear programming are used to permute the top-$k$ recommendations to satisfy constraints (e.g., "at least 30% of recommended candidates must be female") [cite: 29, 30]. While flexible and model-agnostic, these methods often incur a higher cost in accuracy compared to in-processing methods [cite: 19].

### 4.4. LLM-Based Fairness
With the rise of Large Language Models (LLMs) as recommenders, new methods are emerging.
*   **Fairness via Prompting:** Researchers are exploring "fair prompts" that explicitly instruct the LLM to consider diversity and equity when generating recommendations [cite: 31].
*   **LLMs as Auditors:** LLMs are used to evaluate the fairness of other models by analyzing the semantic content of recommendations for stereotypes, acting as a "fairness recognizer" [cite: 31, 32].

## 5. Applications and Case Studies

The theoretical advancements in fairness are increasingly being deployed in industrial settings, particularly in two-sided marketplaces.

### 5.1. Hiring and Recruitment: LinkedIn
LinkedIn provided a landmark case study in deploying fairness-aware ranking in talent search. Their system uses a re-ranking algorithm to ensuring that the gender distribution of top-ranked candidates matches the distribution of the qualified talent pool. This "representative ranking" approach improved fairness metrics (e.g., exposure for female candidates) without statistically significant degradation in business metrics (hiring efficiency), demonstrating that the accuracy-fairness trade-off is not always a zero-sum game [cite: 29, 30].

### 5.2. The Gig Economy: Uber
In ride-hailing platforms like Uber, fairness is often framed as **income equality** among drivers (provider fairness). Algorithms that purely optimize for rider wait times may systematically disadvantage drivers in remote areas or those who refuse unprofitable rides. Research has proposed "income-aware" matching algorithms and income redistribution schemes to reduce the Gini coefficient of driver earnings while maintaining platform efficiency [cite: 33, 34]. However, investigations have also highlighted "algorithmic gamblification," where dynamic pricing opacity makes pay unpredictable, raising concerns about the fairness of the algorithm's transparency [cite: 35, 36].

### 5.3. Accommodation and Hospitality: Airbnb
Airbnb's search ranking algorithm balances guest relevance (conversion probability) with host equity. A notable intervention was the "New Listing Boost," designed to solve the cold-start problem and give new hosts a fair chance against established "Superhosts" [cite: 37, 38]. However, recent analyses suggest that removing such boosts or heavily weighting past reviews can entrench a "rich-get-richer" dynamic, making it difficult for new or marginalized hosts to gain visibility [cite: 38].

### 5.4. Microfinance: Kiva
Kiva, a peer-to-peer lending platform, utilizes RS to match lenders with borrowers. Unlike commercial platforms, Kiva's objective includes social good. Research here has focused on **fairness-aware re-ranking** to ensure that loans from underrepresented regions or sectors receive adequate exposure, preventing funds from concentrating solely on "popular" types of borrowers. Studies show that fairness constraints can significantly improve loan distribution equality with minimal loss in total funding volume [cite: 39, 40].

## 6. Challenges and Open Problems

Despite significant progress, several critical challenges remain unresolved.

### 6.1. The Accuracy-Fairness Trade-off
A persistent debate in the literature is the nature of the trade-off between utility and fairness. While some studies (e.g., LinkedIn) show they can coexist, theoretical work suggests that in many cases, enforcing fairness constraints (like demographic parity) mathematically necessitates a drop in predictive accuracy (Pareto optimality) [cite: 14, 41]. Optimizing this frontier remains a key technical challenge.

### 6.2. Intersectionality
Most existing methods address single-axis fairness (e.g., gender *or* race). However, real-world discrimination is often intersectional. A system might be fair to "women" and "Black people" independently but grossly unfair to "Black women." Modeling intersectional fairness is difficult due to data sparsity—splitting users into fine-grained subgroups reduces the data available for learning, exacerbating the "cold-start" problem for the very groups that need protection [cite: 9, 15, 42].

### 6.3. Dynamic and Long-Term Fairness
Most fairness evaluations are static (one-time ranking). However, RS operate in a feedback loop. A small bias in exposure today leads to fewer interactions for the disadvantaged item, which leads to even lower exposure tomorrow (the "Matthew Effect"). Research into **long-term fairness** using simulation environments and reinforcement learning is nascent but critical to understanding how biases compound over time [cite: 43, 44].

### 6.4. Data Privacy vs. Fairness Verification
To measure fairness (e.g., demographic parity), the system needs to know the sensitive attributes of users (race, gender). However, privacy regulations (GDPR) and user reluctance often result in this data being missing or noisy. Developing "blind" fairness methods or robust proxies that do not violate privacy is a significant open problem [cite: 18].

## 7. Future Research Directions

The future of fairness in RS will likely be defined by the integration of generative AI and stricter regulatory compliance.

### 7.1. Fairness in Large Language Model (LLM)-Based RS
As RS evolve from "retrieval" to "generation" (e.g., ChatGPT recommending an itinerary), the definition of fairness must expand. Future research must address **semantic fairness**—ensuring that the *language* used to describe recommendations is free from stereotypes. Furthermore, "hallucination" in LLMs can invent non-existent items or attributes, posing a new type of reliability risk that disproportionately affects underrepresented entities [cite: 24, 25, 32].

### 7.2. Regulatory Compliance and Auditing
The **EU Digital Services Act (DSA)** and **AI Act** explicitly mandate that Very Large Online Platforms (VLOPs) assess and mitigate systemic risks, including algorithmic discrimination [cite: 22, 45]. Future research will likely focus on **auditing frameworks**—standardized, third-party tools to verify compliance without exposing proprietary code. This moves the field from "self-regulation" to legal accountability [cite: 23, 46].

### 7.3. User-Centric Fairness and Perception
There is a gap between mathematical fairness and user perception. Do users *perceive* a fair ranking as better? Research suggests that explaining fairness (e.g., "We showed you this diverse list because...") can improve user trust, but poorly implemented fairness can be seen as "forced" or irrelevant. Future work must bridge the gap between algorithmic metrics and Human-Computer Interaction (HCI) [cite: 47, 48].

### 7.4. Benchmarking and Reproducibility
The field suffers from a lack of standardized benchmarks. While repositories like **BARS** and **FairnessRecSys** are emerging, there is a need for widely accepted datasets that include verified sensitive attributes to allow for rigorous cross-model comparison [cite: 49, 50, 51].

## 8. Conclusion

Fairness in recommender systems has matured from a niche sub-topic to a fundamental requirement of algorithmic design. The research landscape has successfully identified the sources of bias and developed a robust taxonomy of fairness definitions (user vs. item, individual vs. group). Methodologically, the field has advanced from simple re-ranking heuristics to complex adversarial and causal learning frameworks that treat fairness as a core optimization objective.

However, the "solution" to unfairness is not merely technical. Case studies from LinkedIn, Uber, and Airbnb demonstrate that fairness is deeply contextual—what works for hiring may not work for ride-sharing. As the field moves forward, the integration of LLMs and the enforcement of regulations like the DSA will require a more interdisciplinary approach, combining computer science with law, sociology, and ethics. The ultimate goal is to transition from systems that merely "optimize engagement" to systems that sustain a fair and equitable digital ecosystem for all stakeholders.

## References

*   **[cite: 1]** Zhao, Y., et al. (2024). Fairness and Diversity in Recommender Systems: A Survey. *ACM Transactions on Intelligent Systems and Technology*. [cite: 1]
*   **[cite: 43]** Wang, Y., et al. (2023). A Survey on the Fairness of Recommender Systems. *ACM Transactions on Information Systems*. [cite: 2, 43, 52]
*   **[cite: 2]** Wang, Y., Ma, W., Zhang, M., Liu, Y., & Ma, S. (2023). A Survey on the Fairness of Recommender Systems. *ACM Trans. Inf. Syst.* [cite: 2, 6]
*   **[cite: 10]** Zhao, Y., et al. (2024). Fairness and Diversity in Recommender Systems: A Survey. *arXiv preprint*. [cite: 10, 53]
*   **[cite: 13]** Wang, Y., et al. (2023). The Taxonomy of Fairness Notions in Recommender Systems. [cite: 13]
*   **[cite: 8]** Wang, Y., et al. (2025). Fairness in Recommender Systems: Taxonomy and Dimensions. [cite: 8]
*   **[cite: 4]** Wu, et al. (2023). Fairness in Recommender Systems: Evaluation Approaches and Assurance Strategies. [cite: 4]
*   **[cite: 5]** Deldjoo, Y., et al. (2023). Fairness in Recommender Systems: Research Landscape and Future Directions. *User Modeling and User-Adapted Interaction*. [cite: 5]
*   **[cite: 54]** Wang, Y., et al. (2022). A Survey on the Fairness of Recommender Systems. *arXiv preprint*. [cite: 54]
*   **[cite: 6]** Wang, Y., et al. (2022). A Survey on the Fairness of Recommender Systems. *ACM TOIS*. [cite: 6]
*   **[cite: 11]** Ekstrand, M. D., et al. (2021). Fairness in Recommender Systems. [cite: 11]
*   **[cite: 14]** Rajkomar, A., et al. (2018). Fairness Metrics: Demographic Parity, Equal Accuracy, Equalized Odds. [cite: 14]
*   **[cite: 3]** Sun, et al. (2022). Benchmarks for Implicit-Feedback based Top-N Recommendation Algorithms. [cite: 3]
*   **[cite: 16]** Billsus, D., & Pazzani, M. (1998). Singular Value Decomposition in Recommender Systems. [cite: 16]
*   **[cite: 19]** Jin, D., et al. (2023). A Survey on Fairness-Aware Recommender Systems. *Information Fusion*. [cite: 19]
*   **[cite: 26]** Wu, et al. (2023). Feature Fairness and Adversarial Training in Recommender Systems. [cite: 26]
*   **[cite: 7]** Jin, D., et al. (2023). Trustworthy Recommender Systems. [cite: 7]
*   **[cite: 12]** Wang, Y., et al. (2022). Joint Fairness in Recommender Systems. *ACM TOIS*. [cite: 12]
*   **[cite: 18]** Beutel, A., et al. (2017). Data Decisions and Theoretical Implications when Adversarially Learning Fair Representations. [cite: 18]
*   **[cite: 24]** Jiang, M., et al. (2024). Item-side Fairness of Large Language Model-based Recommendation System. *The Web Conference*. [cite: 24, 25]
*   **[cite: 31]** Zhang, J., et al. (2025). Fairness in Recommendation Systems: LLMs as Fairness Recognizers. [cite: 31]
*   **[cite: 28]** Chen, A., et al. (2023). Fairness-Aware Graph Neural Networks: A Survey. [cite: 28]
*   **[cite: 17]** Chizari, N., et al. (2024). Graph-based Recommendation and Popularity Bias. [cite: 17]
*   **[cite: 4]** Wu, et al. (2023). Fairness in Recommender Systems: Evaluation Approaches and Assurance Strategies. [cite: 4]
*   **[cite: 20]** Gao, C., et al. (2023). Causal Inference in Recommender Systems: A Survey. *ACM Trans. Inf. Syst.* [cite: 20, 55]
*   **[cite: 56]** Airbnb Engineering. (2025). Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking. [cite: 56]
*   **[cite: 57]** Tan, C. H., et al. (2023). Journey Ranker: Multi-task Learning for Airbnb Search Ranking. *KDD '23*. [cite: 57]
*   **[cite: 39]** Liu, et al. (2019). Fairness-Aware Loan Recommendation for Microfinance Services. [cite: 39]
*   **[cite: 58]** Burke, R., et al. (2023). Adaptive Recommendation Framework at Kiva Microfunds. [cite: 58]
*   **[cite: 40]** Liu, et al. (2019). Personalized Fairness-aware Re-ranking for Microlending. *RecSys '19*. [cite: 40]
*   **[cite: 47]** Kecki, V., & Said, A. (2024). Understanding Fairness in Recommender Systems: A Healthcare Perspective. [cite: 47]
*   **[cite: 48]** Kecki, V., & Said, A. (2024). Understanding Fairness Metrics in Recommender Systems: A Healthcare Perspective. [cite: 48]
*   **[cite: 41]** Kecki, V., & Said, A. (2024). Public Understanding of Fairness in Healthcare Recommender Systems. [cite: 41]
*   **[cite: 44]** Feng, Q., et al. (2025). Long-term Fairness in Healthcare ML. [cite: 44]
*   **[cite: 29]** Geyik, S. C., et al. (2019). Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search. *KDD '19*. [cite: 29, 30]
*   **[cite: 59]** Wang, Y., et al. (2019). Uber Eats Recommender System and Multi-sided Fairness. [cite: 59]
*   **[cite: 33]** Raman, N., et al. (2021). Reducing Inequality in Ride-Pooling Platforms. *IJCAI-21*. [cite: 33]
*   **[cite: 49]** Medda, G., et al. (2022). Consumer Fairness in Recommender Systems: Contextualizing Definitions and Mitigations. [cite: 49]
*   **[cite: 50]** BARS Project. (2023). Towards Open Benchmarking for Recommender Systems. [cite: 50]
*   **[cite: 51]** Fair Fairness Benchmark (FFB). (2023). PyTorch-based Framework for Evaluating Fairness. [cite: 51]
*   **[cite: 22]** European Commission. (2025). Digital Services Act: Impact on Platforms. [cite: 22]
*   **[cite: 45]** Mozilla Foundation. (2023). How the Digital Services Act Addresses Platform Recommender Systems. [cite: 45]
*   **[cite: 23]** DLA Piper. (2025). Fairness and Unlawful Bias in the EU AI Act. [cite: 23]
*   **[cite: 46]** European Parliament. (2024). Regulating High-Reach AI and Recommender Systems. [cite: 46]
*   **[cite: 37]** Rental Scale-Up. (2022). Airbnb Search Ranking Algorithm and Host Equity. [cite: 37]
*   **[cite: 38]** Beyond Booking. (2025). Understanding the Impact of Airbnb's New Algorithm on Property Page Rankings. [cite: 38]
*   **[cite: 30]** Geyik, S. C., et al. (2019). Fairness-Aware Ranking in Search & Recommendation Systems. *KDD '19*. [cite: 30]
*   **[cite: 27]** Zhang, Y., et al. (2022). Causal Inference for Fairness in Recommender Systems. [cite: 27]
*   **[cite: 21]** Zhu, Y., et al. (2023). Causal Inference for Recommendation: Foundations, Methods and Applications. [cite: 21]
*   **[cite: 35]** Worker Info Exchange. (2025). New Research Exposes Deepening Exploitation of Uber Drivers by Algorithmic Pay. [cite: 35]
*   **[cite: 36]** PowerSwitch Action. (2025). Uber's Inequality Machine: Data on How AI-Driven Pay is Harming Workers. [cite: 36]
*   **[cite: 34]** Bokányi, E., & Hannák, A. (2019). Ride-share matching algorithms generate income inequality. [cite: 34]
*   **[cite: 9]** Wang, Y., et al. (2024). Intersectional Two-sided Fairness in Recommendation. *WWW '24*. [cite: 9]
*   **[cite: 15]** Wang, Y., et al. (2024). Intersectional Two-sided Fairness in Recommendation. *arXiv preprint*. [cite: 15]
*   **[cite: 42]** Gohar, U., & Cheng, L. (2023). A Survey on Intersectional Fairness in Machine Learning. [cite: 42]
*   **[cite: 25]** Jiang, M., et al. (2024). Item-side Fairness of Large Language Model-based Recommendation System. *The Web Conference*. [cite: 25]
*   **[cite: 32]** Jiang, M., et al. (2024). Item-side Fairness of Large Language Model-based Recommendation System. *ResearchGate*. [cite: 32]

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO0OFU7znQSCd40pwDLcAWy2n8KfeXMqynRwft41Uy1e8B1L-8ZVKB9O3ZR4GLXOZFHDNLH_iTROQObXvMq6It4PsSXHZ_GHR2KAFzFMr1iBDQt8Ixih_4aGyrxo3YrUTPh0b7K9nap_MRPjcbBzUUpDev624RONO1n-ua58TTQc2kLCiFAzOeL_QFmt90xWkIiKnwWgyl6_zKSUKJLKE=)
2. [thuir.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlj9S-o-lR-awH41dz5BuDAqRPrAKaTkxd6UbBHaXScDrR1CtCLfIhD5LClhLQMEp8a6AJAvuI2mg5J57APR25-Iif60Jbw9wjxooK3x72OGbfuSjDGul-9aoMDyUOmyaWTKQKlAZguSORNNCPdzojLvSVjA==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkIKbvRR8Bs82V155-DmyaBD2HgsJUKhot7XIjNRwBYQ0B6LfjdqfQvIpKeosSZqBqF80Bnf6QuhMvxLg0cIq00RIgcHJJulijHKvIyfQzYZhv2iZMhg==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5HDhuvIazrQb-oLrO2_-_aK8oOY6ec-PvcTPKx_ea-j-a07WoVJpbs-chPBqYm_qBahJ_VM6dVA9wf4erlhG0OavhKtFSnmhwFWNlmyuyGtyhrciMRWVqWO3QXOXBLA4MlyWfnQvSW0oVpLs4am8ELcxwDX-hQsaJi-ZXbLYXd0zjSheSyFsSPKkXMS-wrtdbV9dbFT1c_WAZU9FEMfltOeD9vJ4aMWTuHexVKmB5pCNcSf97Wijo)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUb4AzOhI6ijqEjD18aYCyfWclfvPfpfI0ZNRCwUlzmw2OiNp5ymaIZwOvWF4F8q3ZGGofzt4mhu4pdVvFPA25HsHMizdt84NgFF_XRuP1-ZaLv_O2vHDfmBpuzPubVa_d4OxtW_GIhrEr-Rrf6ix0v5Qz8Iy2sgSmhM2wTyRwmYDjNclu-FjpMY1dZ_a9340BdQTziOIAvwuR-NqYLyBvFIKw2PgKGEr_0c-ubb6d5vM=)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWwTjbvp8lE1977ihDdK7Bn9R4_G7SDuYBsN9qkZuP45YcfRBj_a6GJarSMSbCeddD2YRxVIWIKLbBqnBcqP6UZ1Uc8X1CPP1RRByDqKLh_Flh6-4gEg==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcMmfHDImU3G3_76Hg1MU988zX6tTekq_We_WRy8ak0YLic4ddGcKmEIpqPF0xCgxqdwtmNHDxxLaUKb8woHEryD3DL8jjFyqcGi05PRvvJnah5eSPKwnpLz41rGzITeTHInCQuT9fAI32d5W5X1SbzLq6qkIK834TyOVcrIjHrv0D2VDWdnLGZ-FxhqypfSfC4XNBdn8eC2BYdtRRXcl-0lf1wR0PL0xNTWWuCLVfy34hz2DwgtoKCdtXlonBSa6Zfw==)
8. [tudelft.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqviKa1wva73PEtN7s5M73YY74I8L9eZ1mupEOpOWVwA16CUAVnzRnys_RkswgwEgXc5C5AWBDqC9PiEbwR_C_8h7rlkkiCFNOacZNJ4-jUo5WIL2-7ZBS0J7EHOzXgYbJH7rV_VN6l0is4kwxtFxkhmqQN8AVO5LSQnaxET1cI5sR)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3omIYocpt-JmqIPdHYKbe49qbqKgL-3JkThUQo9BjbrxopFCyLs4kiqHoQ4U27L8BGegOiIM-kqDVtoFDGTI0eD4_yNw_2BXgGBOTwbryrtHShTPeoA==)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGwd30SeKfVzY0HmYVeesNmBXg0TVkZ5RuDsBqjMyKlAESex1t6UEhRsLcakiB_byW-YD4DbjSMrbRegB08BHIJOXlVgpeyc4spz1QDnydNzcpTZsUJNsGtA==)
11. [tuwien.ac.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqfya_jObcCTYihaTQiaaNBfda_w3cxJZwhcEiCo2hErH2zG9xrP9Vkx_VzlNEw4kkl87yakZDjqbUWZcNal9rg4WBvGgA82kGgQnLPlMyBqOaODyp5gKR7KlvgRW7CUUmwjJOutbS9dyCCjT3zsku4k0Het4ImRM=)
12. [thuir.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOhDFzLcc6hv9I9sHWtr2XaY6taXEjnNAEdc6Q-Naxkvk78M-XegstsjIvfzqInUyqN47S9mXKGm17VJ2tX5LwaW5WSltb2qqu7y5gN9SFtqXfxVWgfnFqDIKlgaUFOflvXAfrLUToVbY7cVEaM2GWWUqbiM1_dwsViP7c)
13. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlrEtjsT75nkFa5lXkqdb-TY95RfxkwJJjn8r9xAWrUyYWv5TPlfBFC-Q11Mc9LlAIGjWQiXFE_c33-7_2EhkwoZ_w9ZbDuNliQqUxSOnlUn0fWTQxYtV4t0rwwBLEuRo=)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESX-doEDAY7fpxKvcW5ucoj6jsL9F8WWtnb_SyA5uWed_W8i7I4bdo8hz4LpnwJA-AwzlhrLQ1emNcJaADZPbnuUWPR3fogk9Gh1GZXnjriSkH1UufIZOFPQ==)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz5K1cIuRw7kNdoSLuQgBsN2MyqIq57DmrbFvdimmtViT2t6AfnmrYFWDnb6wAHaTJpNUWObDWnpgpofHl8I0ms5zr50s8WCJTp4orqPfxntnH-0s2qQ==)
16. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwiJhQRqM68vsgvYwNc0kt-gSxJEUm4Z8e1DEhWh9gxR96b17SHPLfiWxDmF9g8MDfA2E6GsCljcvwFV6PNCD5TfBTiopO9fh8ys--N4BGbclsIyWZPVxvZ1P4fA9vKZQ3XzluC7bCcs0V6yjhtoGCNZwLOiPEZpjnT3gyZvtTJbVmSNYQaMmyse7-HSDYQGmf5vhzF3x-NX_cI0iJ-hb_GMU-cfjitSuOe977-HEHc21-O83Bur64KUrg)
17. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQc_FjyrozgzW8yEgxQqEsRkV7DVfTQqzX1yqfZQ3jrYTdPw8psHTlz1r60WaXSRzjVylUa5P-oOkXJPnFZLS8tgEB2s61Z7DCETmv98zYbGZeRSP1yDhA6A==)
18. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsSqLgnGiMpozwiS7uHxtgOoAFwnStgtBt3oCWHCKDmA8R3iYh6sAaxEJhPuHd4z0nBvm4oiBk8Aqg9ZSq1BphNnBEdmjKRg0bz_MG8G4Vtw2PDO1XklhXs2gH161T0IGq0axV)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2DXT_WdZ-7J37wRxcAFvYAdMHvFLnN9dfVg28gdCyvRYCAdZCWFqnU_13DHADLx-hG18bc9ONmQq3Qj6_pIJ727hLxP-Q22z3ikYGb3myEi2iV2MO8dUhLYmA5YDJbTzzdOec3xJXBXG9iC2aoZ6L3X3NoiJBAAViHKRmgP5IPCZBruJO1z9FDprG4XYbOpxnuFnyhFAb)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjKDvVAotwMjUNBGi0-2XweBbEyjoqM0NRZL8qtlyodKCZpprYHpeWJgVgjie-e9OJ7skvv-_3XtekB2TLx9rebefRMzf7p_acGryZGo_ZydJpduQ_RQ==)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuJvc_fcAV3mHJaOirFMbWet-otACRpykLmbHXr02yGzmx7-kHosAUBGOkGP3fHrT9UZCM9M717iKanEZCUviDJ5B850lKoQgXNb8QeNJWwX7fyID_Eg==)
22. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHEeXKXIg3ExEVaiz9Nvhp5xmuVLjKllIXiJMQNVqScMDWF_YBluAacIrITgRPfZcirTYDj_nCLHmoeg0u5GVKCOwTS-5lRkHyUpy9XzDcghY6MacN0xxRpk3IEYjkJYlGRhcy_sfWyXIJna1JZS9iNju2uCEVVwGbkJqA)
23. [dlapiper.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7Pv58X0L9mwDanTrP3wws9upV2qAYwjRWhovh93-4sAD43QMu7EXzwo4TAU1jWEvIdIiCjmpjEnBe7cJJS3pwFF7iKMcW37zIHY_8jpv2J5wGPKLatC1a4yP5RbC5WBa1cxYKy6L3xvC2jztCG_70_4UP52tC1hlGxip_ROLp-idK3-gAOwB4NYuPT4WvzHVp-mzY)
24. [ustc.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoXpLp_hZ1Dj7Q2Ka808sLzsV2_LCoAFk2W-JAsS-0y4WoRhn_ID9YNTFigc5kP4ub3lGPp5WykN7PEB-EwgrZe8VRgrdHAZUJD6bSCZ9WII6QuEaWHngH7lFtlJrK6o2vkDcgurFf0CpOvf3whNsg2A==)
25. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY6pt0dntNjgZPzwGaGyBdXbjopwqCrLB1tYSGdeT_mtjoFAWR_sjPgdxB1JsxKAvtrSUDLWHDqIXZfWrxf5ijMvr88n-0xRHEslNst-ollEUTWXdtpzqgFi3LXQjqJJb2e499nKyiCyzV7pCoBllgY2b6lz4R5SX1aB-1yL8PQ_eaZr4=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQK0CqyXVjWWbqx5NULDnm-YWS8U7G-vcVuJsJrx-W7pw3OeQ8Gnomg2pyTMT3f0V4dJh9V6bBvjhVn7rz2xNEQQbRHn7lYcaJwhHR6Z1MpRY7EUE6OA==)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRIivrrGH1qsSqxvJ85qKVdeW7maGNfIf0wEY4-1UzlBBSqdvwRQSqaNd322Ew9tzT2FmmgKKKL2XRUDN3_9r8G3rBxNqWE9uM5N3jClNy3ZJkT5WZBQ==)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmbSZa8LWvKcoOL7DMJFcLYYIsx175GQ0dypd0x2CDWAGZnUKiXLFEbjzQZfZio3JNsEQoTe9yg1gr-ktsy07yxTdhEpASFaDcUrrkECBYOOOehq5VKA==)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA_R63OQxTbH9_dVREd7LkRtp51OP9ckyt10aHgZUIF2-Amk_ABC40ljRhB9qwgWFd9zzx1IVz1l0Oe2M27QqD49-ezK3vzxsGqdmEsiySFmu1OAqt9Q==)
30. [kdd.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG24paMF2CvvQrY5fDeV_LcH1d6VCl8iCzYMMgTVq7D-La_8KP_tSA-3Wx7KTqiNg_nTlHn8pBbH5IGOBeLnLhTIzMd5oQhTRXRbB3gJCiQZZ23j1aey8SMW1MrhTI0W2OThfMAj0kvRWY442CJGf1yP-0b4m2qnutnWoDnPae0aymVlU-KMkLshpKunOxhQVD2OE9LInb5OzMi6qQ-HrLY_Rg_ty8xqxzySwxntdwbCkNa)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqFukVusSzNmDSi_TBabTDPtOPvQNZlIO6jUlgMHvvwjJU4FkWAIeoCViRbA0QtFP76PxSrJxGaswUUyZlRLSlwyOCnqzllTniQfEHOPbp7fK7jjKO3KuDpZ2CfpuqEg==)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mMwDzjpZAq_77aj0osdiD5AdSF-B1g3uAiE8YeEFu-JQPS7VXBnG6_tGZlAiT-aVJRNc6x5lSFkupbpcs0RY-oQIL562EsxNskYXFCOgPfXbNlQXYynOPNcAVStGTsJalhcUpq3mYBYirRQbbyeSu3iLTG5lm81kHdqe9Ugz1b-ykZYbt2SqmYuC56VnFDu0oOPOmqS9iJgCo21JIw-pSoK2xVXLaWZX3E5qW0_C)
33. [ijcai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSffznpfvMdRqkJ1Rf9_DbDCLSoyRZBdHEykrVzl2g0ToJWgDzf5v1GbyUMB4m2uBaCwRdZaa4u0rkPGdrhzrYAtAMwb1ZdJsJJfp-TUlSPRbWrBwsCrdp6poitdqj8B_LuvUdbw==)
34. [metadataetc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn407cPBneAYSpqa0JOiTE07lt2TkwOVrgeRvwf8S3spbjbKg1nLqQaHViSpC0msIFxY6cAyFVZFW5YTD1RxwHq0dOSL301MEmbERCSvx25bhNZOtHdxyA-7ZQSQYHvZACKfbFmhYKdf6e7zovDvWjT865VnNxZu0xfDbU4EADcFfcDvSHh4lq44JKbhC5qVfiRvhe3Hs2j2pVr_NX9k5wlcGzRNQnB5Jr3jLYvuGQDeHZjTlLs5cKIG2GaBkQuICDuBCi8NHAweGovQ7oqcM2u9Me)
35. [ier.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGExKHP5_RE5d44DlqABfdvK_oAQp-BAkOhMGJCQHsaXHNv3T4veQBzwWmKTZeUx_H4WO2Clb_K3VfqXinwWn6ERL8tgsas08a4rTpPg_RirjvKZnkWWq4JtbPaRwXZr_m2JuZqbv_ESrwsQWZXSAgub5LNitkqjfkrcJbqaUmZkIdA8uuS7S1hNjCx2YZj2UB9SfMjONTfoDd38shW3tvd0g==)
36. [powerswitchaction.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ02POW2u6FiAx0r37aS7NyKZJICYVmdD9TLY-x3JjZEExSCb4r3ppnap6ALjc2ZERRQAxBSgnLp2VhfMSK7QQ9RMjrrfsQtwyYv-6D66J5s4CSKEsH1HqS9O08GHIKIvbMAreHHOWLk_a9IuQtc6QoAWACIIs-PbmKlk=)
37. [rentalscaleup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3hgWH48Ogg54_TMiY0ZOCZdAe8hT5Wo55pMYBZ5ikLR5FIK0W2H51XmxnF-eOYChcEvYwGrPn3FCo81JAh8Arl0r7IdBno7vU853aanDLN6uJuLslmjUQmf-wrMUbQiLyMC9MSGl9zRmT7-744Ss97PPqoA==)
38. [beyondbooking.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1bE2oz1mvC2dk_k3tWp3G5NxKdj3P5WnaEeOXx0_njtX9CUmOvt3IIcZdV2SJplGmUNVmtZmu0d5p57VmRnURHsDslFxqW0EfRxBJE4rwRzjDItmolbavcLtziz1EmTaU6SiueKqu1DnevXYtKk1udHOz1SLoOK8drpsSMg_EdGX0pRI94YheMS-lX0C34pTV2_aphlDyWHrlya2RjLeqkGihyg==)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZoBno8rh66i6J8j-DQY-iNZOrVuaMnVlXJpaJGd9s7piZ6OyXta8PUx-4uBNzogdJsxlzwLaR1RxkfBEgv5Hk7vC0AutdQuLyAg_C2g7G6ieeIWFOqo0fo1KOHhXhp7FeSkcZSq4zOzxLkcxLDm3llb26tzVSfYgGqt0uyNUzGdHlw32Dt7LyGQIVIu4Vi4O2QrmVk8oRr-LX5wP9-pJq6neJdeA=)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRgUOjq6l2uZhsOJHu6sXsjO1uf9xV1-ImmV_ANE0kY4zCJQE97YhHhCQsQ2z_46ZOJQSibj6VdKM4uaiOhfCR-Up6N4V73FiumFlgN-tG_iKGbpJNSwV0Bd89NcjBi_I3Dg8XLg-Q-fmndZUjiiqu2xt-Y8oMv4cWD4Qx0ci2nvPcHGUL2KwA9wK4Xo3HkGLzH_lf00Hu6hH6Of9k-go_)
41. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgYBC8_S3Mf07qTo7Bf3gAW8uiRKwXXETvgA_FfAyithyFodo8aaL9FNO9ISerZWqiMUjf0AsllDrvW6My2eVxwE6AJ8thN8TVsba3NVJfGvMzNHRoPBKPxw==)
42. [montrealethics.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETll-s7DeSAlyiw_9i1QuRa-jUaWfg1DbJVmimTAcdMcfGZILnEBySsMV1r7czykWeIUCtOKh4WAa9P2sm88NXB6VdGJXj-Z1EonpGz0eyEEK8jnocHOFDfZbehCG-RX9rSH1QVhi4lw_Cbwy6WwTLJxaadW-WL7zJY_wwqP-idNg239TcZPbhRNWZcIkTZGypjn95LnxZSGeQLdiGoQB8ds-iC9vmDak9ng==)
43. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa4MyqhDWiAt3OI0g9BvvcrhhcWGH-k7jAYlqmuVucUwoMIOB4Kny1Q2obPID1wLfH0u-d3uEPlVDjnkQ1AoF2BU3dmDg7kdAJyapoXXVJlAhucm9Vv7Njbvu0rzFt7DeZuh3JEhpqkkSOiB7xzKhpt52vClYzg8ocx44KfJaz2xpCnzQzOSNK7QbC7Knbq9BmuNr404L1BV60xKpicZymUNyPQ-kdDuurRkQYxobYIGcDZZbdbBN_lcVF7gg=)
44. [computer.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeGV95PH5MNQJQdJjvd_r9PGYtY_cFYnV1bWDugFBtquJL5eGRsLAxH-ldgifEf-HhP_K1MznnmQY-XdyLxGQHyOb1aIZsGSjV5hQ82sTbSYB8-ezC-4cl-0QLIAGhcW3Xne-1R48QAmjLGOLNoolOvjQgEzjbmKsFvBk=)
45. [mozillafoundation.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSjtwdX0cRW35o3gnOR2dm8uzsg0EwlZCzc33zg-TemndWyDAkDZTII9dCJJcov3Jyi8c-a1hR7xW_EEPlVnYyjXKRq-WF5P6zZKxWvUgrUNBy2ncWIAKbzAtG_N3ZSuv0x0hRexOaRMCTsz7-_xJix7GqkhCgw59ZsRFYlZyaANLeaqMp2Yl76TbXFEIFcsKPiSuHwLSTuFtZIvm9YZ_CN7rxYaVh-mrgp2gU2vYHgZussmT67e5N)
46. [policyreview.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyE1ezMBaNdBU3UdVYHebwCJLMLk1ZNZ01rZWH1UvPNrl769GMPs_K-ZHpBsuB6qrQyoet_HH2ThyZS0toHQZWSW6-HXune8jgbGXLNj5zbovHseAC2xG3Ru_OOyv1W3tRdC7VYMBEgpvq6mIPwRTKuDtk_2F5u0L4WQ==)
47. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1egBSK3cpjrBQ7DL0pLuCZGj5v5YhHbntI89phEHc-gQAY0XRTnLxK90UDygCXoBdlJu8_XUNaSUmj3r8pt_xk6zOuj_v1Hfp4eUSs9lW93298s8ozUtxJhc=)
48. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9H9YyWdfoF5RJtR74SPuWYazfu5s65tH61bzKI6PDrZF0DjEddbeHGJPVAOD7dtiw9bNJhxFhIioDC0F3NlKQPjIh_yBTzm2p20vTrFplNuW3qyh9aQ97ngZtjorx_Omj57LWuyw-U1yzEbxC35VFWNwMsxxNHWlQoB4WCsIftNX5IalfU0nNusYMwQ74GsP1aYIvoqTdznSdfQXT_pFUCxk4otMGvi-B6Mn9CYDPbg4irvEv0iwI)
49. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL8CdDKaAROkuaLtKWiYspcHPMFcJQaviASP6KkJH_QUvx6Zvi37CihTWpzeX71ToQj0IrF2Gid1pA-Udzc6fVgeDZ2vwNldnYTiPEOEFJxO2uCMcPOfO33gkvBoTvKT72A2Ia)
50. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK16_Ik1UVv0PNDry12lbKbgNattFyQ2CGF7Cl2EkDiATCu9aU7QhHXXiN_3eeBLpiUmaoyj8v283_ADUjrKRMkimcGEVn_uBRn2iDFMJvWagDJbo=)
51. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLezAJa6adKiQRDqaqPGPIUhK8il9Qdj4hxJCZwZvHzJB27SxmZ411m0xPjUBCzAh30Fzs8Q-oK5cH_9H7bDqSEG71u1Ex8kixTrm_vuaT8nXv4kEpmeDq2-VhS5zqHwurAqxkfg==)
52. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH58z2CzsmEFvSdD_Kbxq0FTqr6ob2vv-hAQyT5uOuy58vYme7q_uN2Ez2dBFV9-OuNxGxOWMtTtHX9GfFoGvaGHILohI6PkBz59P7uBGV4N4YCzNUrFQ==)
53. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbFAs-KCWwS3-RW2cfdC0p5wgSq5MRU0C8h6HtpERXIMmQw85e6gOPgcdX9jDPkUPDVDR_eltYltRUGNshQZp6Kr88e-yyYkIpy5U2qIk3zs47mOspGw==)
54. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXro9eSjfLbDHg0wjZYW7afFkBHEDddfm-M6ARyXMg-aG-fu7RgPTxrszkI1q6UaRH-mb3ROTEY4qYTPlSO5NRzm97GhmNL1GtwBS-gOcsukn5CjnK5Q==)
55. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdJEE2wZ3dsc5xefmt1vm7G-97YctcbgEm3321VzT5XwdwW_d6odC4KGjFcUrHMQzCuFMqH07Y4BCDBlbp-UCA_nyLKaQ8gMjRUr8XZV4eHzHe9JT2lVPeLMMXsa3O88-VWLoihqcrL1HdSwp1HF0XBIqCfw==)
56. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfgaBdDam1JybTw5A1O2Vp9snzScry9-yYawzAbt-9DwhBdlZxWNopv8t1S7prPwE27rk3G_hYicWKozutdPpP70rg7lzhOOlECxVTTWFJo8P5TPGrag==)
57. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe-TC_UGM-AEn58RCaGorjncXkaH63HLr-RSPoPj0wpqO8w64NQ1kAx-S0b35wsW_Co67QSdnK8BsxHyqk_MmPHw5p6XcI8e-CYy49Am3Zhj9YastxwA==)
58. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHww3URjok5z5vr1kA4Grg-j93FMle4M_QcXBVWr_aPNRID7zLcfR4w9mr5D_hhF6zFlJZoX4WGGhVZE0h2-_0-1Floe50tmAWW239a8njcQv3N32l9Yp4EZXm00FQ75P90lZO2)
59. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy_PHbT-RIWeD-ApQijqiJAJpWBwXV6WrBvSPaC2amGUIeAzhUTHAaPJsyzFq0ZW4wdzHQ7FGGtbCRiaG_qfu3zcb_QZCGqcEo-ElTSBBzn27Yh9zc1ViKImSxXD2cIzaVYj0sckipRLtCkm0NXV9_wwNdmVaUst0_D0yeb4D9Bw6LVzsg8D4o5TP7ZQMBg55omuI=)
