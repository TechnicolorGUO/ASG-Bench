# Literature Review: Directions in abusive language training data, a systematic review- Garbage in, garbage out.

*Generated on: 2025-12-26 21:43:49*
*Progress: [33/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Directions_in_abusive_language_training_data_a_systematic_re_20251226_214349.md*
---

# Directions in Abusive Language Training Data: A Systematic Review of the "Garbage In, Garbage Out" Paradigm

**Abstract**
The rapid advancement of Natural Language Processing (NLP) has led to sophisticated models capable of detecting abusive language with increasing accuracy. However, the efficacy of these models is fundamentally constrained by the quality of the data upon which they are trained, adhering to the computer science axiom: "Garbage In, Garbage Out" (GIGO). This systematic literature review examines the landscape of abusive language training data, building upon foundational surveys to analyze the current state of dataset creation, annotation, and utilization. We critically evaluate the prevalence of sampling, annotator, and demographic biases that compromise model generalizability and fairness. Furthermore, we investigate the emerging paradigm shift toward synthetic data generation and the utilization of Large Language Models (LLMs) for annotation, assessing the risks of "model collapse" and the circular propagation of errors. This review synthesizes findings from 2016 to 2025, identifying critical research gaps and proposing a data-centric agenda for the future of online safety technologies.

---

## 1. Introduction

The proliferation of abusive content on social media platforms—ranging from hate speech and cyberbullying to toxicity and harassment—poses significant risks to individual well-being and social cohesion [cite: 1, 2]. To mitigate these harms, the computational linguistics community has increasingly turned to machine learning (ML) and deep learning solutions. While algorithmic architectures have evolved from Support Vector Machines (SVMs) to Transformer-based Large Language Models (LLMs), the performance of these systems remains inextricably linked to the quality of their training data [cite: 2, 3].

The principle of "Garbage In, Garbage Out" (GIGO) posits that flawed, biased, or poor-quality input data inevitably produces unreliable output, regardless of the sophistication of the processing algorithm [cite: 4, 5]. In the context of abusive language detection, "garbage" data manifests as ambiguous definitions, low inter-annotator agreement, sampling artifacts, and systematic biases against marginalized groups [cite: 2, 6].

### 1.1 Research Motivation and Objectives
Despite the critical importance of data quality, research has historically prioritized model architecture over dataset curation. A seminal review by Vidgen and Derczynski (2020) highlighted that creating high-quality datasets is "difficult, laborious and requires deep expertise," often leading researchers to rely on flawed public datasets [cite: 2, 7]. Since that review, the landscape has shifted dramatically with the advent of generative AI, which offers new methods for data augmentation but also introduces new risks of synthetic data contamination [cite: 8, 9].

The objective of this paper is to provide a comprehensive systematic review of abusive language training data, addressing the following questions:
1.  How has the definition and taxonomy of "abusive language" evolved in training datasets?
2.  What are the primary sources of bias ("garbage") in current datasets, and how do they affect model performance?
3.  How are LLMs and synthetic data reshaping the GIGO paradigm?
4.  What are the best practices for future dataset creation to ensure robust and fair detection systems?

---

## 2. Key Concepts and Definitions

To understand the GIGO problem, one must first define the input parameters. The field suffers from a lack of terminological consensus, leading to incompatible datasets and models that fail to generalize.

### 2.1 Defining the "Garbage": Data Quality in NLP
In machine learning, data quality is defined by accuracy, completeness, consistency, and representativeness. "Garbage" inputs in abusive language detection typically fall into three categories:
*   **Noise:** Mislabelled examples due to annotator error or ambiguity.
*   **Bias:** Systematic skew in data distribution (e.g., over-representing African American English as hateful) [cite: 6].
*   **Artifacts:** Features that correlate with labels in the training set but not in the real world (e.g., specific keywords like "sport" appearing only in non-abusive classes) [cite: 3, 10].

### 2.2 Taxonomies of Abuse
The terminology used to label training data varies widely, often conflating distinct social phenomena.
*   **Hate Speech:** Language that attacks or demeans a group based on attributes such as race, religion, or sexual orientation [cite: 11, 12]. It is often defined by legal frameworks or platform policies.
*   **Abusive Language:** An umbrella term encompassing hate speech, but also including insults, aggression, and profanity that may not target a protected group [cite: 11, 13].
*   **Toxicity:** A concept popularized by the Perspective API, defined as a comment that is "rude, disrespectful, or unreasonable" and likely to make someone leave a discussion [cite: 14].
*   **Cyberbullying:** Repeated, targeted aggression, often involving a power imbalance [cite: 1, 15].

The lack of standardized definitions means that a model trained on "toxicity" (e.g., the Jigsaw dataset) may perform poorly when tested on "hate speech" (e.g., the Waseem dataset), as the underlying constructs differ [cite: 3, 14]. This conceptual misalignment is a primary form of "garbage" input.

---

## 3. Historical Development and Milestones

The evolution of abusive language datasets can be categorized into three distinct eras, each characterized by specific data collection methodologies and associated quality challenges.

### 3.1 The Keyword Era (2016–2018)
Early datasets were primarily constructed using keyword filtering.
*   **Waseem and Hovy (2016):** One of the first public datasets from Twitter, collected using keywords like "skank" and "nigger." While pioneering, this method introduced severe sampling bias, as the dataset contained high concentrations of explicit slurs but lacked implicit abuse [cite: 6, 16].
*   **Davidson et al. (2017):** Differentiated between "hate speech" and "offensive language." This study revealed that keyword-based datasets often conflate profanity with hate, leading to high false positives for communities that use reappropriated slurs [cite: 17, 18].

### 3.2 The Crowdsourcing and Deep Learning Era (2018–2022)
As deep learning models (LSTMs, BERT) required larger datasets, researchers turned to crowdsourcing platforms like Amazon Mechanical Turk.
*   **Founta et al. (2018):** A large-scale dataset characterizing abusive behavior on Twitter using crowd workers.
*   **Vidgen and Derczynski (2020):** A landmark systematic review of 63 datasets. They concluded that most datasets were "locked away," small, and biased, formally establishing the GIGO concern in this domain [cite: 2, 7]. They introduced *hatespeechdata.com* to catalog resources [cite: 2].
*   **OLID/OffensEval (2019):** Introduced hierarchical taxonomies (e.g., Is it offensive? Is it targeted? Who is the target?), moving toward more granular data annotation [cite: 19].

### 3.3 The Generative Era (2023–Present)
The release of ChatGPT and other LLMs transformed dataset creation.
*   **Synthetic Data:** Researchers began using LLMs to rewrite or generate abusive content to overcome privacy restrictions and data scarcity [cite: 8, 20].
*   **LLMs as Annotators:** Studies investigated replacing human crowd workers with LLMs (e.g., GPT-4) to label data, raising new questions about machine bias and the circularity of training [cite: 21, 22].

---

## 4. The "Garbage": Critical Analysis of Data Quality

The "Garbage In, Garbage Out" paradigm is most evident when analyzing the systematic flaws embedded in training data. These flaws are not merely random errors but structural deficiencies that propagate harm.

### 4.1 Sampling and Topic Bias
Most datasets are created by querying APIs for specific keywords. This results in **topic bias**, where the model learns to associate specific topics (e.g., sports, politics) with abuse simply because those topics were oversampled in the abusive class [cite: 10, 23].
*   **Keyword Over-reliance:** Fortuna et al. (2021) found that keyword-based datasets fail to capture implicit abuse (abuse without slurs) and covert hate. Models trained on these data perform poorly on "in-the-wild" data where abuse is context-dependent [cite: 3, 10].
*   **Author Bias:** A small number of prolific users often contribute a disproportionate amount of abusive content in training sets. If a dataset splits comments from the same author between training and test sets, the model may learn to identify the *author's writing style* rather than the concept of abuse [cite: 3, 10, 24].

### 4.2 Annotator Bias and Subjectivity
The "Ground Truth" in abusive language is inherently subjective.
*   **Demographic Mismatch:** Annotators on crowdsourcing platforms often do not represent the demographics of the victims of hate speech. Research shows that annotator identity (race, gender, political alignment) significantly influences whether a post is flagged as abusive [cite: 25, 26].
*   **Low Agreement:** Inter-annotator agreement (IAA) is notoriously low for hate speech. Traditional metrics like Cohen’s Kappa treat disagreement as "noise" to be eliminated. However, recent "perspectivist" approaches argue that disagreement reflects legitimate social diversity and should be preserved rather than aggregated into a single majority vote [cite: 21, 27, 28].
*   **LLM Annotation Bias:** Recent experiments using LLMs (e.g., GPT-4) to annotate data show that while they are cost-effective, they exhibit distinct biases. Okpala and Cheng (2025) demonstrated that classifiers trained on LLM-annotated data flagged African American English (AAE) as abusive at higher rates than those trained on human labels [cite: 22].

### 4.3 Racial and Dialectal Bias
A pervasive form of "garbage" is the systematic misclassification of minority dialects.
*   **The AAE Problem:** Davidson et al. (2019) and Sap et al. (2019) demonstrated that datasets annotated without dialect awareness lead to models that penalize African American English. Tweets containing reappropriated terms (e.g., "nigga") used in a non-hateful context are frequently mislabeled as hate speech [cite: 6, 29].
*   **Propagation:** When these biased datasets are used to train models like BERT, the bias is amplified. Okpala et al. (2022) introduced AAEBERT to mitigate this, but the root cause remains the training data [cite: 29, 30].

### 4.4 Temporal Degradation
Data rot is a significant issue. Social media posts are frequently deleted or accounts are suspended.
*   **Reproducibility Crisis:** Researchers often release only Tweet IDs to comply with platform terms of service. Over time, the most abusive tweets (the core of the dataset) are deleted by the platform, rendering the dataset useless for future reproduction. This "data degradation" means that older datasets lose their most critical examples [cite: 17, 31].

---

## 5. Current State-of-the-Art Methods and Techniques

To address the GIGO challenge, the field is moving from simple data collection to sophisticated data engineering and synthesis.

### 5.1 Synthetic Data Generation and Rewriting
Privacy concerns and data scarcity have driven the adoption of synthetic data.
*   **"Don't Augment, Rewrite":** Casula et al. (2024) proposed a method of using generative models to *rewrite* existing abusive texts. This preserves the semantic meaning of the abuse while anonymizing the content and bypassing copyright/privacy issues. Their results showed that models trained on synthetic data could perform on par with or better than those trained on real data, offering a solution to data degradation [cite: 8, 20].
*   **Adversarial Generation:** Tools like Dynabench use "human-and-model-in-the-loop" approaches to generate "tricky" examples that fool current classifiers, specifically targeting the "long tail" of implicit abuse that keyword searches miss [cite: 32].

### 5.2 Cross-Lingual and Low-Resource Approaches
The field is heavily dominated by English data, creating a "linguistic GIGO" problem for other languages.
*   **Translation and Transfer:** Techniques involving back-translation and cross-lingual embeddings (e.g., XLM-RoBERTa) are used to leverage English datasets for languages like Indonesian, Arabic, and Spanish [cite: 1, 16, 33].
*   **Multilingual Meta-collections:** Projects like MetaHate and DETESTS aggregate datasets across languages to create more robust, diverse training corpora [cite: 21, 33].

### 5.3 Active Learning
To improve data efficiency, researchers are using active learning to select the most informative examples for human annotation. This reduces the volume of "garbage" (redundant or easy examples) and focuses annotation budget on ambiguous cases [cite: 34, 35].

---

## 6. Applications and Case Studies

### 6.1 Case Study: The "Waseem & Hovy" Legacy
The Waseem and Hovy (2016) dataset remains one of the most cited resources. However, its construction via keyword search resulted in a dataset where "sexism" was heavily correlated with specific sports commentators (due to a harassment campaign active at the time). Models trained on this data learned that discussing sports was a feature of sexism—a classic GIGO example of topic bias [cite: 6, 10].

### 6.2 Case Study: LLM-based Content Moderation
Platforms are increasingly deploying LLMs for moderation. However, Piot et al. (2025) found that while LLMs can rank the relative performance of detection models, they struggle with instance-level reliability in subjective tasks. They do not fully replicate human nuance, suggesting that replacing human datasets with LLM-generated labels may lower the ceiling of detection quality [cite: 21, 27].

---

## 7. Challenges and Open Problems

### 7.1 Model Collapse
A looming existential threat to abusive language detection is "model collapse." As the internet fills with AI-generated content, future models will be trained on data generated by previous models.
*   **The Feedback Loop:** If LLMs are used to generate training data (synthetic abuse) and also used to detect it, the variance of the data distribution shrinks. The models "forget" the tails of the distribution—the rare, nuanced, or evolving forms of human abuse [cite: 9, 36, 37].
*   **Poisoning:** Synthetic data, if not carefully curated, acts as "garbage" that reinforces the biases of the generator model, leading to a degradation of performance over generations [cite: 37, 38].

### 7.2 The Subjectivity Bottleneck
The field has not solved the problem of disagreement.
*   **Gold Standard Fallacy:** The assumption that there is a single "correct" label for a hateful tweet is flawed.
*   **Metric Limitations:** Standard metrics (F1-score, Accuracy) do not account for the severity of errors (e.g., censoring a marginalized group vs. missing a slur). New metrics like Cross-Rater Reliability (xRR) are being explored to capture the pluralism of human judgment [cite: 27, 28].

### 7.3 Privacy vs. Utility
Strict privacy laws (GDPR) and platform restrictions (Twitter/X API changes) make sharing raw text difficult. While synthetic rewriting [cite: 8] offers a path forward, it remains unproven whether synthetic data captures the full pragmatic nuance of human abuse (e.g., sarcasm, dog-whistles).

---

## 8. Future Research Directions

### 8.1 Data-Centric AI
Future research must pivot from architectural improvements to data engineering. This involves:
*   **Data Sheets and Cards:** Mandatory documentation of dataset creation, annotator demographics, and sampling strategies to make "garbage" visible [cite: 2, 38].
*   **Dynamic Benchmarking:** Moving away from static datasets (which rot) to dynamic benchmarks that evolve with language [cite: 32].

### 8.2 Perspectivist Learning
Instead of aggregating labels to eliminate disagreement, future models should learn from the distribution of annotator votes. Systems should be able to predict *who* would find a statement abusive, rather than making a binary determination [cite: 21, 39].

### 8.3 Safe Synthetic Data
Developing rigorous protocols for generating synthetic training data that avoids model collapse. This includes "watermarking" synthetic data and ensuring human-in-the-loop validation to maintain diversity and grounding in real-world phenomena [cite: 37, 40].

---

## 9. Conclusion

The domain of abusive language detection has reached a critical inflection point. While model architectures have achieved superhuman performance on some benchmarks, the utility of these systems in the real world is stalled by the "Garbage In, Garbage Out" reality. The systematic review of the literature reveals that the "garbage" is multifaceted: it is the bias in keyword sampling, the subjectivity of underpaid annotators, the erasure of minority dialects, and the degradation of historical data.

The widespread adoption of LLMs presents a double-edged sword: it offers tools to clean and augment data (e.g., via rewriting) but threatens to flood the ecosystem with synthetic noise that could induce model collapse. To advance, the field must embrace a data-centric ethos. We must move beyond maximizing F1-scores on flawed static datasets and toward creating living, diverse, and transparent data resources. Only by rigorously addressing the quality of the input can we ensure that the output serves the goal of a safer, more inclusive digital environment.

---

## References

[cite: 3] Fortuna, E., et al. (2023). Dataset annotation in abusive language detection. *SSOAR*. [cite: 3]
[cite: 1] Maity, K., et al. (2025). Survey of abusive language detection datasets and data quality. *arXiv*. [cite: 1]
[cite: 23] Aluru, S. S., et al. (2020). Deep Learning Models for Multilingual Hate Speech Detection. *PMC*. [cite: 23]
[cite: 10] Mishra, P., et al. (2019). Detection of Abusive Language: the Problem of Biased Datasets. *NAACL*. [cite: 10]
[cite: 34] Kirk, H., et al. (2022). Is More Data Better? Re-thinking the Importance of Efficiency in Abusive Language Detection. *ACL*. [cite: 34]
[cite: 2] Vidgen, B., & Derczynski, L. (2020). Directions in abusive language training data, a systematic review: Garbage in, garbage out. *PLOS ONE*. [cite: 2, 7, 41, 42]
[cite: 25] Arango Monnar, A., et al. (2024). Bias and reliability in hate speech datasets survey. *ACL Anthology*. [cite: 25]
[cite: 17] Osho, O., et al. (2020). Racial Bias in Hate Speech and Abusive Language Detection Datasets. *ACL Anthology*. [cite: 17]
[cite: 43] Wich, M., et al. (2021). Annotator bias and data quality in abusive language detection. *RANLP*. [cite: 43]
[cite: 24] Wich, M., et al. (2021). Investigating Annotator Bias in Abusive Language Datasets. *PMC*. [cite: 24]
[cite: 39] Dehghan, S., et al. (2025). Dealing with Annotator Disagreement in Hate Speech Classification. *ResearchGate*. [cite: 39]
[cite: 44] Chandra, A., & Choi, J. (2025). Abusive text transformation using LLMs. *ResearchGate*. [cite: 44]
[cite: 36] Arthur.ai. (2023). The Real-World Harms of LLMs Part 2: When LLMs Do Work as Expected. [cite: 36]
[cite: 21] Piot, P., et al. (2025). Can LLMs Evaluate What They Cannot Annotate? Revisiting LLM Reliability in Hate Speech Detection. *arXiv*. [cite: 21, 45]
[cite: 27] Piot, P., et al. (2025). LLM for hate speech data annotation reliability. *arXiv*. [cite: 27]
[cite: 22] Okpala, E., & Cheng, L. (2025). Large Language Model Annotation Bias in Hate Speech Detection. *ICWSM*. [cite: 22]
[cite: 8] Casula, C., et al. (2024). Don't Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data. *ACL Findings*. [cite: 8, 20]
[cite: 31] Casula, C., et al. (2024). Synthetic data for abusive language detection. *ChatPaper*. [cite: 31]
[cite: 7] Vidgen, B., & Derczynski, L. (2020). Directions in abusive language training data: Garbage in, garbage out. *PLOS ONE*. [cite: 7]
[cite: 4] Wikipedia. (n.d.). Garbage in, garbage out. [cite: 4]
[cite: 5] TechTarget. (2023). Definition: Garbage in, garbage out. [cite: 5]
[cite: 32] Vidgen, B., et al. (2021). Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection. *ACL*. [cite: 32]
[cite: 6] Davidson, T., et al. (2019). Racial Bias in Hate Speech and Abusive Language Detection Datasets. *ACL*. [cite: 6]
[cite: 13] Alrashidi, A., et al. (2025). Towards a comprehensive taxonomy of online abusive language informed by machine learning. *ResearchGate*. [cite: 13]
[cite: 11] Seemann, Y., et al. (2025). Definitions hate speech vs abusive language vs toxicity vs cyberbullying. *arXiv*. [cite: 11]
[cite: 14] Fortuna, P., et al. (2020). Toxic, Hateful, Offensive or Abusive? What Are We Really Classifying? *LREC*. [cite: 14]
[cite: 12] Council of Europe. (n.d.). Verbal violence and hate speech. [cite: 12]
[cite: 28] Emergent Mind. (2025). Cross-Rater Reliability (xRR). [cite: 28]
[cite: 16] JITECS. (2025). Hate speech detection in the Indonesian language. [cite: 16]
[cite: 33] Pereira-Kohatsu, J. C., et al. (2025). Systematic review abusive language datasets 2023 2024 2025. *arXiv*. [cite: 33]
[cite: 29] Okpala, E., et al. (2022). AAEBERT: Debiasing BERT-based Hate Speech Detection Models via Adversarial Learning. *IEEE*. [cite: 29]
[cite: 9] UK Government. (2025). Future risks of frontier AI annex A. [cite: 9]
[cite: 40] The Alan Turing Institute. (2023). Exploring responsible applications of Synthetic Data. [cite: 40]
[cite: 38] EPIC. (2024). Comment on NIST AI Executive Order Mandates. [cite: 38]
[cite: 37] Spasic, I., & Nenadic, G. (2025). Model collapse abusive language training data. *arXiv*. [cite: 37]
[cite: 35] Kottke, D., et al. (2024). Re-thinking the importance of efficiency in abusive language detection. *arXiv*. [cite: 35]

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESZI-ilwihsDVfFysfDsXpYb7NR7Nf9d77SppQ3lFHpTchgnIoPFk8D6X7sUPgcWgsY9A2_1ONNe_QzVKhiYpxhvLY9AstUkYFRaHQAdSZUG_xrHj2DepY)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDFLBvAqy8B4aSVnNr8B8c9-wqExhKI_tBMDnz7WlvVff9bsOLg7_TtPSgvDnQzfheQNiNehBLPlFeKebERAXK08Mn4W9LYHOPkGmDsjB1HR5ahTZH838FafGcumPB17G6DqCmcfw=)
3. [ssoar.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbFzUuB_mFbDHWrlkuAqrU8oJ2ZYnjZjzwaPbbsI0iN6xrpVBsWIp1N2nkiVxT6ZdfzRM_MKzu36KNm6k8_xOQLofsyvq8Hs9Ye0Jw-ylc9xWp669f6gu-XtF6qFVMN2JmLnPiHlwUc2K2Rt8vVlyqKcORVeNbcqtBi3wJCnZDZnA7O1mZ9SqzNGfUTNGH5zXh55v1X27Gk2LNjyHB5ySPjh9Tcjz-cNNMmdnurl6onxj6ZUWcYPKXSYdSuqTtdXxLMARwxJEA3GWrg4GYcdcULII-HdWuX_IW3QMwnY8AcZGElQSfah7wM4ociQ8KrrGumA2-XwbaqucGLwbysZlW7jTM-t_1xzDKkioy9Eu3uhCxmP-us_74EA==)
4. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4Fscpi96t4Ijhy3eUT9GrWWOBBHkAQzgQagM0Dhah_ozyWwXDZAa0GIOebAdyGAD7ji1pFYa480rVV-J2SHK1OCgTiB-ToYp1gjptT7wK5BCB4qo6b7-C-6zsBt_QgKPnCG5zLLhIvO4_)
5. [techtarget.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF8areBpVo4DB3i4YLrEYZ5D3_aTnXfsRc-VUBgJZjUMK9N9t342Y370DnCY4jEyg9-hl6_LyZiTLxvxZ3USkLzWPa3HPeRSxKT11EgcC384sORGiwDbdm32Pj4nd7b-GidY79yWqQD422_VMUW8nLZT8057JIv5zCrAukCyX5fAtWGc5N-LI=)
6. [ingmarweber.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3IzoKYk4KRmJ0lDGhCgG3pKEbcP-DRsfKGdR2YFt6IZGk44legCzmQRA4oIeaG-ZDV3Z3ui6QR5zDfNT2CjZiVQPvMSjTo3AaapUXkBgPvoFxviKFa-3d9a0K4pdXnT1uQ5_Y46DMOWsgu_3kbjVdtZJsCu-booavfN6Gq5i-Khvl6BAkGI9uWFWbfMucYuMSmXaJiyBgqZPBGkUAgJ0F-X4g8jvdSZtEO053sg==)
7. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6Op8rDdmhVNNyPs7Nlc7bnrwou3S-YfSU--H46gDyLi3uq_eFmVzaj50Ds-SmkepkQP54zi_6VUwCaf4Ed8TC-vRyido2DDolMQG0VIfkauyB7s5FSlR7_xYdqLVybFCLsf6qNN5zC1vD1romRca-m-VkswE-H5pfPQAwu8g=)
8. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET9ELPPCTxR1T2wvM5XiQJkFBcEpP6U06GVISwTYoK1nuQnBVL0qyGH4l3e6LlfRbkH-_-GPY4XvHWLontNC2wbkJTWVMPvepwsX4x0YoBoFcHKfp80BC0VnGzTEqc3SaaaoGy)
9. [www.gov.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY-uztT1hiih7od6BxUa9_uHVmxjp2k2N35txT7OsiS-74tG0JnBWvW5xxlZ35T9lh1rm3t2JiJop5P3i3ViU7Vd5Lj7Eifvj4chwMDJf8phWvbe77s0kNW18x5ep9OokhwmY4ZUJSo-PLrmlRg8Y1E9AMQnOf8bGGjopSNq03UuYH6-6fDlgpH4XppR9w9d8LijfFDgjy-XS4umGhMWIFpmCWP2DBnSymOyYf6lVdzFgnDODhhaD0)
10. [liner.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCJkhV04CcbRpwDNm5DiMQ280Q7jXwA1Vsc8QEeKIvybxtVNXGYiHhg8KvUpOrHYSMdrCYfMoByRqHfrDsd15PKm8zXL4zxV27gTu4vMuTuA11OcZpi0uywsxQMZj60RstgmzP5dlpztEmsGd22Q0uT2R6DiRwIXqR2t-NuP_Hlg==)
11. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd2Nse-Sa1rPYs9jsTBWJmWJ7IvtCnGt1HHweCFoBKZmDORwDwF_NdstS4VG3X2bPl78poH8c-QVklNursv4zm2Dh3w17Gtq1h_TpY7jWd4i_eVu92)
12. [coe.int](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz9zFxAOtPYX3VGkz-QIXsotCwQwZpkKCdBoSbBUCzPcCkRT4ErDuVlb0YnKmaTNGluwiXIKDe835v42lT2A5rzxFPAuBPOw82ZOYW6ydK0NUv7LIgz9BHj9bEX0b0s_L99R9hw0NOJlOzRPzKUuTaoDP_GdLQ_xpGqrQxLHM=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHPDM8imJhIT6fBVXI75p_gqFm8e3X58M8-fUGTvopyPrUBxCxcCQ-fBFF3kkNdYAbbeci0Zfl22m0lqyBIaALcs2B6fcnHx_rDotL1UfZAx28weKl3aKHpugt9hOeGapNvWMd9eXwJcOCHBRmnjjI7MOnkdiSbmp4zWIGpI2h9MRSvEmGZ4UELTw1DiFf1T6lsdqXk5GyZF7tTRW3yl0EvlucgPQK_bo1Qb3tey0lQgvsuAua_0uHgpqKgUmrCew=)
14. [lrec-conf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK_kth6e_v4qlI_362ZtmVWmYNVkzqkwQEvqTPF-ocFDF7NGiHa_eoVoVutZBxS0lo6MVB6VwSqTuBwzPhvY3F2K4y7prjjAN2VOkp_9P9Sjz_DDl7T5W9XC9Je3kH_mW_SBekAYxYda81eAG4MU7d_DuiBcSi)
15. [bu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjF18LMtu5TRMKTeywbWlnOsdF1waQNNSI4kgqdVmvgJN5arMXxoFuEsD9GVhHnrDP9vAFxUii9rfw3-NlpwH6GG2Z4VusPIKG0s5zzzRW9jGgGcakM2UMq2Z6YvHhSbMalNDCw99dR5Ju6SmkRCWJ1USPtoFJEepe0u8dWCgWgClShN4Pt6I=)
16. [ub.ac.id](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm6y3wAEE9eHmGkNjyhkvCEJJKulQ8_Q4-Y_DoQ9x-jqoLl8r6gztlJlPsDJ9ChUdWTSGjAWR95ZvSNUKhq43U3Dh1FCQ_dnW9y5vi0i5-kVEMAZ_DN8MiUzGWoYV8DrR0qlDk6-kKZvyvBkeHZA==)
17. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBAZnlCmw9BGrHJtXSWFf9FIWxFWliZucrS2zhG5pEEq5CW8s71AD6mnaRZNP-542I9kj2ibCcmQPijWf47KTREjRKzFHKATqiq0ugrNO2ze5OFBQiVOh001boihlcg==)
18. [kaggle.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDJnE6zGlw6oJTsw673g9x87Ti_meH2jFb3Ipq1KyGz353A-4jSgoPgKsZexPSwX0GgPFMWD4APoLfE7dSSOzba2kPiVU5_kIQ67HR5K-nw6Fmp2XLoZM-XJfZYmogQ5cAx9RZJ6iianmVuyqnfwIK0MTYYfxzmKh3OAmk3MO1Di0U30IKRUIhTLSw)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcBGKQGbsXVKiok9EfwEslkVbwrVINaXQLroJbQOb-fHqRnC4Itx9SeUme_RpuZnee5tQFlGue0Q2QpjuhfrETrF96Rp5_SjlP3pXIk3brQN3n3FAsF9ALGRlH8-3ShnOj9hXgKJivAapxZ8Z2syxv-mAmrnEQ9wIjCz4Ad2D7K32JfVkVMBpGCws-e3di3bPsICYe4-I2dkxzi0qoAGIYzInNMOWcueP4ag==)
20. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF-c7OC6jEPaDa7unB5kLIam8OTV7K_dzTQOBrqNvBUsSXXNtmiMcCrMuRqX-89ZHMbDkjr6YA-KmYWFysq0a1_PlFoQG0JY4XYhmg556aRdw_qyGw3pk2zw3IxiWoU847_UGSGUVU)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-U3WAjuF38b4DphI99lRqCFjtusX_CqYzyFZ8b4GYlmiNb6AHDLY9j2Fv6Ekqi63cY338kLhTDzbfaRxPYFR8dSEzWKjV9Mhe2w6x-eDmhjE0n8oqTWoRgA==)
22. [aaai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuqX3TOhEx6guR8p3qYeLEAK6QCitC6xpWpjGYZm5KcQPfuxaR0Qfnp1HfuH3oGGjC4qpMH4TQk-2izBSzIJPs1Si7PPQCcTpAVYberqnBU3MeMEaAfvfbtXDCys0EEkjnuN8IpmqVtJ0hA0Y=)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFTxoUPmR_7aaMWgJs18fXPTZKpGNCVUbsMp3xlavGSB88xBVtP-RdcIxGD4iFzbutch54191D4q-Wn3DyYEAb7bk8xfBvZrCLj0xv2jRz9BkD8_iqZB2GZu9lRorr7sFCQ7npz75I)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJSxc6l23F6wU92K61nDfj5LIj8vDi-Leg6BNM22NPRbVMyfGno1ajAs6HbWWZ9xBtFHyl8MsVs_Yd0tV1WpJ8QCWClWG6dxE9YUsROStKVGtHJqL006_SAOtN7FE3Y1fqIUlnUug=)
25. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYujDMiHPPwMHsDDsSK0Cw27bjFgXMX2hD_FtA9KxTvqzLaR3nWvnvxw50_APmRIv7r5f4n-Gs6BFWiLgVqOlTW612p3NXfjJq8PTpkb7pB9NFcvl5GpYnqbzeRLH3frU=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGVgHfX1nVfOAOkM8HJ3ZGoPUFhBnV0fgkj0_FJFtz8WKfxXRFU3ibEvfRZX4DqmyddMH_DbjbEpPNi4vmiMO8DzQu7cJG7eFGOc_25UgiN2upL0o9vJKS)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAizTMVHgx_vfg0VohjU00MadAuwP-OIptlIcXbrwZbLMLXIxEbKJ1WHhud-NjyGn6c1U5ie5HKI-g0L6cwEU7MdkBsXQLLjccMNQX3EIvKfM5ppuOTY4_)
28. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0eZUbN-f2Z39YOW3NG5MLOyvCfcJLPJIj3UEQ0xqzBxjlhJHJFPShwq9gbodeKJAvL6tDlVbOzgf5kaNm1Bc6LUTe2x095Nsl9-eWlP8UHnM7lExbPirU_iiq17K6D_yLtEd77mEMiEBH1hoOQe2Te6ddHg==)
29. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_1_8ATkIVFj8n_nPp3mNrRA97C8iL1qLvg6cJ9PiyoPXIo56I-Yq_cfwYz66NipG4T3JAxqa8LjB1PuRkoAs7fuJ1kb1PLRzFl519QY8djSdwN9loKYoFt_kqntuPsf3mQRWLwwF63lWT7uspoKwRNhBjuA==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5FbggS18QJUfiChU86Rm59P3kVual63uDLVo9Wjztp-QnnP6Ijl465n8PogV3AE1EPN2y-8RQIY83O1lvmIekJqYpzq-2retJpkEPO587Lknh5io4YVygd1C3kM8YsQmhy_8DvEU8mWOOTz_n-wOUdT6YOxUSHcr-TwDk-w9UuxMhC0CVExy8zBs282xgyH3befW-jY5p5rfB4opAqWejXzw2z7s476o95eDtlpMkkg_RJrh9Qp_JWdMz)
31. [chatpaper.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK9Mcnc1JqGZ48unzEHDrb2BtFicZEgvQdOdCS9bUP2938L0pZg03EB2gZIvtsAOhstUswUHyMdehqZ_Tfs1xOAOObogrYQuwq0fbkpOROOhA9bjofWw==)
32. [hatespeechdata.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc2ayZlbCazQ3aEmPXdemyzdoBgJqSUQlx4Oq3fxPw3IGLoQgIyFgDc1pWPNSRtC4wAMPCyNmknwrES35bK_Nc3sdh41nnj8K-c6TbW8zhpg==)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU-RAJX18f1GVHLADrwNpKICnJEsI6Zf1OV-Xw-7iuzdTXKhXUhiDzuOqzLr88sHUm6IB9c_3xQDNtF5aSCG2vb6TI4wVUikVZliLkduCtFr3R8Z3T357R)
34. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0g7oF_kUlOFNw-EZM5gQz76wl7Sd3q4LcojT-oj7ZBZR3rdXVeJMwAue9gJWAZPXXYNqGeBmPHoMragkYwtxlVe9u--KqVzvlxkGHnQibIrKiZfVWs6HFv-HJFA==)
35. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyo76mdaZDSZNpz5TlFsWCEx5fEe49YeFKVeddQ26HdZUXq0xvOXCtjWv7oRJztTop3TNTP0eEGfxo2Qr-wLWGvmkZawrkGZ66SXpACGSp4UpONvbJyIGx)
36. [arthur.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ty1LH8Vo3esvgv3Zm6i4v-3X291GB1BhnOQjyzCT-vSXIERXdkdlve9Xg0TpZe9vIyBIubfizuXW5nFyDnfA8QP-6qFFuS9Bhe8OZhM8CTHif0jv-wg_ftiXHT7K_5oxlwugS_nYyllC7tvBNG5AfVunDauBFFu26wIuKWPs0F1mB4jvDkeDcUDorkI6P5Ej)
37. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy8nF3AjJyX-e8nIv7qu7pdsY9EFmGBdNFoufJobBjb0rORwYdz9vMm177w_ZCFO6zvIHpYToa5Q9D6cR0XqeqPkDoa1ebHuLybYwuqyEPdZpAXzWGlq7u)
38. [epic.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU4qukiJ8tRptWbEkxrMnUuvCpGyvWSjZAYHrH90fgWRkTlu5Sp0nHpmBgPYh4KSKz6WrSGY_iS5bx3jXN4Bh9At_G4gNjkoBl1Gd7NUnGgnpOwUum3EjZKs0IX8pSCz1m-vjpn8SAUbY2PeATeceGcuM8P3dn4hpoEcKPw_91LJTwsOhve3Vw7tfcQETwoWEJAzs4WyGaWO56141ud5lCF9Y=)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLX7aLqhe_zJUUe7mPELS9DDWsUzStEfXP3hWWyv3a6itxdG9-_d_p6zC2V-FAllNzegywLRStzmlQpzfTuK4Dyrf_62WMAoK7uhttLyP-AfKUB0DFt76ROJS0UT-cKqkVBpcxcJxV9IF1stUXcwyNJW8mcy4nT9vBrpYeUoYYMmhRih1Q0Pemp7j0YbW43fanXPoNwhrLuA8v74yHr-aOPA==)
40. [turing.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG73m7FNI8VrVpPrOOFqBit-FbnSq6Zv4kbACtKE5Kg64nKfCqxvmUUNzkEIOsOlinE1BlL4lv_HNIGALydVkSqpZaNdHJuG8FS9JabXKviKAkenmvgD9d2Z-LikRRqrH21jHVYnWVsSTuxqJYLBQvqw81SBRcjqo7skxepWSpN5AZUENReOTOpVqFQ54sZqTZniiN1PrBFYasfQPJ1xpi5bBZRlLBB8tiYGb1AVciLmHKg_iU=)
41. [turing.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlu_rMaylHCAkMNH1PU6H96_UGg5xuU4xbAyYAwTwWzubwgrSfRRzwyOGfyROL2fL9rQqa-yDlfC8c97CeXJFYP6eYJcnOqHfSHxN8Cws771pKmdJi-WZu-odh3VEPQGDiKRx02andWgI1imN-RyvI6CDyOLRlwRV7yK6V6zYA5GZr2zdWMjQPgkcBvCoxo1F8x3y129tgy5hCSVDytxBVElvjOWX7oMhKGqff7Cc2)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv9BQT9AFg0RXeBR246O9T2ZdaSP1fLY9TcQ1Kb6yc5MQdf-7WrIPRX37aRu3BBaXqMabVmffl8ajXU74y-fMcFRSkxQc5MJXLjjKFVsCm1O2sS9mEZAN_w7iOJiWj)
43. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNvJWG4OAMZwnBxJeGqCUhxEyeh14j_hjnguz2g9rhqlSyrY--uzMlsHWu5FUMOzjNxCa7WceVUcjQuzYJaeEbHXmKSYE3AOYuYzC2GDPADvNideagmVto3bVv2H7tkDIlRg==)
44. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHLxAZgsOyrPQql_aBBntZDh2w4Jyx-WkWxVlbhrdYoPb2QeZURmoA3uUttJ5s6_klUraQmpybs5mzgnGLWP3HhZBHXDD-Mh3nff56FZARU7mjvpdXPPp-DyAHsTlMInVcDOn_qSjJ-OOso-zpjsOB5m1-gAwBDu5tio2P4t2S40hqSMuzoNBmuPsvoFoe)
45. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9l3pd_p_J7eGkehOFpglKGQcuj90HFcEVQ6-pK8qSzQZz62KvMnX0EZQeLtMA5Z-bw-uYL18YyrONxC-F-I28_wNh4D6XJO9xZ4Hb_72rOofAieULXleGNjVQ5GFdWoejY-faMhqtcKcgwEG82W-wAIUIHiBTqxx4a2gcR5Myi8lZxj_JHD5Nq8rWuZn5HfKtxPK-m29oMMzb9ymX0q9eCvTX4mIIngpj9T1efHtioAzb-4xtEtT9PZAgznC7L4I=)
