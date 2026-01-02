# Literature Review: Pre-trained Language Models in Biomedical Domain- A Systematic Survey.

*Generated on: 2025-12-26 21:58:33*
*Progress: [35/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Pre-trained_Language_Models_in_Biomedical_Domain-_A_Systemat_20251226_215833.md*
---

# Pre-trained Language Models in the Biomedical Domain: A Systematic Survey

**Key Points**
*   **Evolution of Paradigms:** The field has transitioned from feature-engineering and static embeddings to Pre-trained Language Models (PLMs) like BERT, and recently to Large Language Models (LLMs) and Multimodal models (LMMs).
*   **Domain-Specific Pre-training:** Evidence suggests that models pre-trained from scratch on biomedical corpora (e.g., PubMedBERT) generally outperform general-domain models adapted via continuous pre-training (e.g., BioBERT) due to domain-specific vocabulary alignment.
*   **The Rise of Generative AI:** 2023–2025 marked a shift toward generative models (e.g., Med-PaLM 2, OpenBioLLM-70B) which demonstrate expert-level performance on benchmarks like USMLE, though challenges regarding hallucination and reasoning consistency remain.
*   **Multimodal Integration:** New frontiers involve integrating vision and text (e.g., LLaVA-Med, BioMedGPT) to handle radiology and pathology tasks, moving toward holistic "medical generalist" agents.
*   **Critical Bottlenecks:** Despite performance gains, deployment is hindered by "hallucinations" (factuality errors), data privacy concerns, and the lack of rigorous real-world evaluation frameworks beyond static benchmarks.

---

## Abstract

The proliferation of biomedical data, ranging from scientific literature to Electronic Health Records (EHRs), has necessitated advanced Natural Language Processing (NLP) techniques to extract actionable insights. Pre-trained Language Models (PLMs) have emerged as the *de facto* standard for these tasks, evolving from encoder-only architectures like BERT to massive generative decoders and multimodal systems. This systematic survey reviews the development, taxonomy, and application of PLMs in the biomedical domain. We critically analyze the historical progression from BioBERT and ClinicalBERT to state-of-the-art Large Language Models (LLMs) such as Med-PaLM 2 and OpenBioLLM. Furthermore, we examine the shift toward autonomous medical agents and multimodal foundation models. The review identifies significant challenges, particularly regarding model factuality (hallucination), interpretability, and the ethical implications of clinical deployment. We conclude by outlining future research directions, emphasizing the need for robust evaluation metrics that transcend traditional benchmarks to ensure patient safety in real-world settings.

---

## 1. Introduction

Biomedical text mining is a critical discipline at the intersection of bioinformatics, medicine, and computer science. The volume of biomedical literature is expanding exponentially; PubMed alone adds over a million citations annually, and EHRs generate petabytes of unstructured clinical notes [cite: 1, 2]. Traditional NLP methods, relying on rule-based systems or statistical machine learning, struggled to capture the complex semantic dependencies and specialized terminology inherent in biomedical text [cite: 3, 4].

The advent of the Transformer architecture and the pre-training/fine-tuning paradigm revolutionized this landscape. General-domain models like BERT (Bidirectional Encoder Representations from Transformers) demonstrated that models pre-trained on vast corpora could learn universal language representations. However, the direct application of general-domain PLMs to biomedicine often yields suboptimal results due to a phenomenon known as **distribution shift**—the significant difference in word distribution and semantic structure between general web text (e.g., Wikipedia) and biomedical corpora [cite: 1, 5].

This survey aims to provide a comprehensive overview of the efforts to bridge this gap. We explore the trajectory from domain-adaptive pre-training (DAPT) to the training of domain-specific LLMs from scratch. Unlike previous surveys that focus solely on specific architectures or tasks, this review integrates recent advancements in multimodal learning and autonomous agents (2024–2025), providing a holistic view of the current ecosystem [cite: 6, 7].

---

## 2. Key Concepts and Definitions

To contextualize the literature, we define the core taxonomies governing biomedical PLMs.

### 2.1 Pre-trained Language Models (PLMs) vs. Large Language Models (LLMs)
*   **PLMs (e.g., BERT, RoBERTa):** Typically encoder-based models ranging from 100M to 300M parameters. They utilize a "pre-train then fine-tune" paradigm where the model is adapted to specific downstream tasks (e.g., Named Entity Recognition) using labeled data [cite: 2, 8].
*   **LLMs (e.g., GPT-4, Llama-3):** Generative decoder-based models with billions of parameters. They rely on "in-context learning" (prompting) or instruction tuning and are capable of zero-shot or few-shot performance on unseen tasks [cite: 9, 10].

### 2.2 Training Strategies
*   **Continuous Pre-training (DAPT):** Initializing a model with weights from a general-domain model (e.g., BERT-base) and continuing training on biomedical text. This leverages general language knowledge but may suffer from vocabulary mismatch [cite: 5, 11].
*   **Training From Scratch:** Initializing the model with random weights and training exclusively on biomedical corpora using a domain-specific tokenizer. This approach typically yields better performance for specialized domains [cite: 5, 12].
*   **Instruction Tuning:** Fine-tuning LLMs on datasets formatted as instruction-response pairs (e.g., "Diagnose this patient based on the symptoms...") to align the model with user intent [cite: 9, 10].

### 2.3 Evaluation Metrics
*   **Standard NLP Metrics:** Precision, Recall, F1-score (for entity extraction), and Accuracy (for QA).
*   **Biomedical Benchmarks:**
    *   **BLURB:** The Biomedical Language Understanding and Reasoning Benchmark, a comprehensive collection of datasets for NER, Relation Extraction, and QA [cite: 13].
    *   **MedQA (USMLE):** Questions from the United States Medical Licensing Examination, used to test reasoning capabilities [cite: 14, 15].
    *   **Med-HALT/MedHallu:** Benchmarks specifically designed to test hallucination and factuality in medical LLMs [cite: 16, 17].

---

## 3. Historical Development and Milestones

The history of biomedical PLMs can be categorized into the "BERT Era" (2019–2022) and the "Generative Era" (2023–Present).

### 3.1 The BERT Era: Domain Adaptation
The release of **BioBERT** (2019/2020) by Lee et al. was a seminal moment. BioBERT initialized weights from the general BERT model and underwent continuous pre-training on PubMed abstracts and PubMed Central (PMC) full-text articles. It achieved state-of-the-art (SOTA) performance on biomedical Named Entity Recognition (NER), Relation Extraction (RE), and Question Answering (QA), significantly outperforming the original BERT [cite: 1, 5, 18].

Following BioBERT, **ClinicalBERT** (Huang et al., 2019) addressed the specific nuances of clinical notes (e.g., abbreviations, telegraphic sentence structures) by pre-training on the MIMIC-III dataset. ClinicalBERT demonstrated that models trained on scientific literature (like BioBERT) were insufficient for clinical EHR tasks, such as predicting hospital readmission, due to the distinct linguistic characteristics of clinical notes [cite: 19, 20, 21].

### 3.2 The Vocabulary Hypothesis: PubMedBERT
A critical turning point was the introduction of **PubMedBERT** (Gu et al., 2021). The authors challenged the assumption that starting from a general-domain model was beneficial. They demonstrated that the vocabulary of general BERT (based on Wikipedia) was ill-suited for biomedicine (e.g., splitting common medical terms into nonsensical sub-words). By pre-training from scratch on PubMed data with a custom domain-specific vocabulary, PubMedBERT outperformed BioBERT and ClinicalBERT across the BLURB benchmark, establishing "training from scratch" as the superior, albeit more resource-intensive, strategy [cite: 5, 11, 12, 13].

### 3.3 Other Notable Encoder Models
*   **SciBERT:** Trained on a mix of biomedical and computer science papers, offering a broader scientific vocabulary [cite: 12, 22].
*   **BlueBERT:** Combined PubMed and MIMIC-III data to bridge the gap between biomedical literature and clinical notes [cite: 19, 23].

---

## 4. Current State-of-the-Art Methods and Techniques

The field has recently shifted toward Generative AI, characterized by massive parameter counts and instruction-following capabilities.

### 4.1 Proprietary Medical LLMs
**Med-PaLM** and **Med-PaLM 2** (Google) represented the first models to achieve "expert" passing scores on the USMLE (MedQA). Med-PaLM 2 utilized an ensemble of prompting strategies and instruction tuning on medical datasets to achieve accuracy exceeding 85%, surpassing unspecialized models like GPT-3.5 [cite: 14, 24, 25]. Similarly, **GPT-4** has demonstrated strong zero-shot performance on medical reasoning tasks, often outperforming specialized models in reasoning capability, though it lacks public weight availability [cite: 9, 14, 24].

### 4.2 Open-Source Medical LLMs (2024–2025)
To democratize access, the research community has released powerful open-source models:
*   **OpenBioLLM-70B:** Developed by Saama AI Labs (2024), this model is fine-tuned on the Llama-3 architecture using Direct Preference Optimization (DPO) and a custom medical instruction dataset. It reportedly outperforms GPT-4 and Med-PaLM 2 on several benchmarks despite having fewer parameters than proprietary giants [cite: 26, 27, 28, 29].
*   **John Snow Labs Medical LLMs:** In late 2024 and early 2025, John Snow Labs released a suite of models (7B to 70B parameters) that claim SOTA performance on medical summarization and QA, emphasizing factuality and reduced hallucination rates compared to GPT-4 [cite: 30, 31, 32].
*   **BioMistral and MMed-Llama:** These models focus on multilingual medical capabilities and lightweight deployment (7B parameters), making them suitable for resource-constrained environments [cite: 31, 33].

### 4.3 Multimodal Foundation Models (LMMs)
Medicine is inherently multimodal, requiring the synthesis of text, imaging (radiology, pathology), and omics data.
*   **LLaVA-Med:** Li et al. (2023) introduced LLaVA-Med, a vision-language model trained in less than 15 hours. It utilizes a curriculum learning approach, first aligning biomedical vocabulary with image-caption pairs from PMC, then learning conversational semantics via GPT-4 generated instructions. It enables users to ask open-ended questions about biomedical images [cite: 34, 35, 36].
*   **BioMedGPT:** An open-source "generalist" model designed to handle text, images, and molecular data. It unifies various biomedical tasks (e.g., molecule QA, radiology report generation) under a single sequence-to-sequence framework [cite: 37, 38, 39].
*   **Llama3-Med:** A recent multimodal adaptation of Llama-3 that integrates visual encoders to achieve SOTA on visual question answering (VQA) benchmarks like VQA-RAD and SLAKE [cite: 40, 41].

### 4.4 Autonomous Medical Agents
The frontier of 2024–2025 is the development of **Agentic AI**.
*   **Agent Hospital:** A simulation environment where patient, nurse, and doctor agents (powered by LLMs) interact. The "MedAgent-Zero" strategy allows doctor agents to evolve and improve their diagnostic accuracy by treating thousands of virtual patients, achieving high accuracy on MedQA without human-labeled data [cite: 15, 42, 43].
*   **Biomedical Agent Frameworks:** These systems integrate planning, memory, and tool use (e.g., accessing external knowledge bases or calculators) to solve complex, multi-step clinical problems [cite: 7, 44].

---

## 5. Applications and Case Studies

### 5.1 Clinical Documentation and Summarization
One of the most immediate applications of LLMs is alleviating administrative burden. Studies show that models like GPT-4 and specialized variants are used to draft responses to patient portal messages, summarize complex patient histories, and generate discharge summaries. Real-world deployment at academic medical centers has shown that "writing for professional communication" is the most common use case among healthcare professionals [cite: 45, 46].

### 5.2 Information Extraction (NER and RE)
While LLMs excel at generation, traditional PLMs (BioBERT, PubMedBERT) remain highly efficient for extracting structured data (e.g., genes, drugs, diseases) from unstructured text. However, recent work indicates that LLMs can be augmented with Retrieval-Augmented Generation (RAG) to perform few-shot NER, though fine-tuned PLMs often still hold the edge in cost and latency for high-volume extraction tasks [cite: 47, 48, 49].

### 5.3 Clinical Decision Support (CDS)
Models are increasingly evaluated on their ability to act as diagnostic aids.
*   **Case Study:** In a comparison of GPT-4 against standard clinical decision support systems for drug-drug interaction (DDI) checks, GPT-4 showed lower sensitivity, missing clinically relevant interactions that traditional databases caught. This highlights the danger of relying solely on probabilistic models for safety-critical checks [cite: 50].
*   **Hospital Readmission:** ClinicalBERT and its successors continue to be refined for predicting 30-day readmission risk by analyzing discharge notes, often outperforming structured-data-only models [cite: 19, 51, 52].

### 5.4 Medical Education and Simulation
The "Agent Hospital" simulation demonstrates the potential for LLMs to serve as training grounds for medical students, allowing them to interact with "virtual patients" that exhibit realistic disease progression and symptomology [cite: 42, 53].

---

## 6. Challenges and Open Problems

Despite the hype, significant barriers prevent widespread clinical adoption.

### 6.1 Hallucination and Factuality
The tendency of LLMs to generate plausible but incorrect information ("hallucinations") is the primary safety concern.
*   **Benchmarks:** New benchmarks like **Med-HALT** and **MedHallu** have been developed to specifically stress-test models with fake questions or complex reasoning tasks. Results show that even SOTA models like GPT-4 struggle with "hard" hallucination detection, and general-purpose models often fail to distinguish between real and fabricated medical citations [cite: 16, 17, 54].
*   **False Confidence:** Models often express high confidence in incorrect diagnoses, which is dangerous in a clinical setting [cite: 17, 55].

### 6.2 Data Privacy and Security
Training models on patient data (EHRs) raises significant privacy issues. While de-identification is standard, LLMs have the capacity to memorize training data, potentially leaking sensitive information. Federated learning and on-premise deployment of open-source models (like Llama-3 derivatives) are being explored as solutions to avoid sending data to external APIs [cite: 6, 56, 57].

### 6.3 Domain Shift and Generalization
While models like PubMedBERT handle literature well, they may struggle with the "messiness" of real-world clinical notes (typos, jargon). Furthermore, models trained on data from one hospital system often fail to generalize to another due to differences in reporting standards and demographics [cite: 1, 5, 50].

### 6.4 Evaluation Gap
There is a discord between academic benchmarks (like MedQA) and real-world utility. High performance on multiple-choice questions does not necessarily translate to safe, effective clinical decision-making. Recent studies call for "Real World Evaluation" (RWE) frameworks that assess model outputs in actual clinical workflows rather than static datasets [cite: 45, 58].

---

## 7. Future Research Directions

### 7.1 Reliable and Explainable Agents
Future research must move beyond static QA to dynamic agents that can explain their reasoning. Techniques like Chain-of-Thought (CoT) prompting are a start, but rigorous verification mechanisms (e.g., citing specific guidelines or evidence) are required to build trust [cite: 7, 44].

### 7.2 Small Language Models (SLMs) for Healthcare
To address privacy and cost, there is a growing trend toward "Small Language Models" (e.g., 7B parameters or fewer) that are highly specialized. Training these models on high-quality, curated medical textbooks and guidelines (rather than noisy web data) could yield models that are both accurate and deployable on local hospital infrastructure [cite: 32, 59].

### 7.3 Multimodal Integration
The integration of "omics" data (genomics, proteomics) with text and imaging is the next frontier. Models like BioMedGPT aim to become true "biomedical generalists," capable of bridging the gap between molecular biology and clinical presentation [cite: 37, 39].

### 7.4 Mitigating Hallucination
Research into "refusal-aware" models (which know when to say "I don't know") and RAG systems that ground every generation in retrieved clinical evidence is critical. Benchmarks like MedHallu will play a vital role in measuring progress in this area [cite: 16, 60].

---

## 8. Conclusion

The application of Pre-trained Language Models in the biomedical domain has undergone a rapid transformation. From the vocabulary-aware encoders of PubMedBERT to the multimodal reasoning capabilities of LLaVA-Med and the agentic simulations of Agent Hospital, the field is moving toward systems that can perceive, reason, and act. However, the "black box" nature of these models, coupled with the persistent risk of hallucination, necessitates a cautious approach to clinical deployment. Future success lies not just in larger parameters, but in better data curation, rigorous real-world evaluation, and the development of systems that prioritize patient safety and data privacy above all else.

---

## References

[cite: 5] **BioBERT vs PubMedBERT Comparison.** (2024). *Medium*. [cite: 5]
[cite: 19] **Adapting BERT for Biomedical and Clinical NLP.** (2024). *Medium*. [cite: 19]
[cite: 1] Lee, J., et al. (2020). **BioBERT: a pre-trained biomedical language representation model for biomedical text mining.** *Bioinformatics*. [cite: 1, 18]
[cite: 3] **Comprehensive Investigation into Applying LLMs in Healthcare.** (2023). *arXiv*. [cite: 3]
[cite: 22] **Pretrained Language Models for Biomedical Tasks.** (2020). *ResearchGate*. [cite: 22]
[cite: 9] **Large Language Models in Biomedicine.** (2024). *PMC*. [cite: 9]
[cite: 26] **OpenBioLLM-70B.** (2024). *Hugging Face*. [cite: 26, 27, 28]
[cite: 30] **John Snow Labs Achieves State-of-the-Art Medical LLM Accuracy.** (2024). *OpenDataScience*. [cite: 30]
[cite: 40] **Llama3-Med: Multimodal Medical Model.** (2024). *arXiv*. [cite: 40]
[cite: 61] **Survey of LLMs in Healthcare.** (2024). *MDPI*. [cite: 61]
[cite: 62] Wang, B., et al. (2023). **Pre-trained Language Models in Biomedical Domain: A Systematic Survey.** *ACM Computing Surveys*. [cite: 2, 62, 63]
[cite: 2] **Taxonomy of Biomedical PLMs.** (2023). *ResearchGate*. [cite: 2]
[cite: 64] **Survey of PLMs in Medical NLP.** (2024). *PubMed*. [cite: 64]
[cite: 8] **Pre-trained Language Models in Biomedical Domain.** (2021). *arXiv*. [cite: 8]
[cite: 6] **Challenges of LLMs in Biomedicine.** (2024). *arXiv*. [cite: 6]
[cite: 44] **Biomedical LLM Agents Survey.** (2024). *MDPI*. [cite: 44]
[cite: 56] **Ethical Concerns of LLMs in Medicine.** (2024). *PMC*. [cite: 56]
[cite: 10] **Strategies to Adapt ChatGPT for Biomedicine.** (2024). *Briefings in Bioinformatics*. [cite: 10]
[cite: 47] **Benchmarking LLMs for BioNLP.** (2023). *arXiv*. [cite: 47]
[cite: 48] **LLMs in Biomedicine: NER Study.** (2024). *arXiv*. [cite: 48]
[cite: 49] **Benchmarking LLMs for BioNLP Applications.** (2024). *ResearchGate*. [cite: 49]
[cite: 4] **Biomedical NER Challenges.** (2023). *PMC*. [cite: 4]
[cite: 24] **Top 5 Medical AI Models Compared.** (2024). *Dr7.ai*. [cite: 24]
[cite: 57] **AI in Medicine: Opportunities and Challenges.** (2024). *Medify*. [cite: 57]
[cite: 50] **Barriers to LLM Implementation in Clinical Practice.** (2024). *MDPI*. [cite: 50]
[cite: 14] **Capabilities of GPT-4 on Medical Challenge Problems.** (2023). *Microsoft Research*. [cite: 14]
[cite: 7] **Biomedical LLM Agents Survey.** (2025). *arXiv*. [cite: 7]
[cite: 54] **Evaluation Metrics for Medical LLMs.** (2025). *PMC*. [cite: 54]
[cite: 65] **Medical Hallucination Detection.** (2025). *arXiv*. [cite: 65]
[cite: 45] Unell, A., et al. (2025). **Real-World Usage Patterns of Large Language Models in Healthcare.** *medRxiv*. [cite: 45, 46]
[cite: 18] **BioBERT Technical Details.** (2020). *Bioinformatics*. [cite: 18]
[cite: 16] **MedHallu: Benchmark for Hallucination Detection.** (2025). *MedHallu Project*. [cite: 16, 60, 66]
[cite: 42] **Agent Hospital: Virtual Hospital Simulation.** (2024). *Tsinghua University*. [cite: 42]
[cite: 15] **Agent Hospital: A Simulacrum of Hospital.** (2024). *arXiv*. [cite: 15, 43]
[cite: 11] Gu, Y., et al. (2021). **Domain-Specific Language Model Pretraining (PubMedBERT).** *ACM Transactions on Computing for Healthcare*. [cite: 11, 12]
[cite: 13] **BLURB Benchmark.** (2023). *PMC*. [cite: 13]
[cite: 20] Huang, K., et al. (2019). **ClinicalBERT: Modeling Clinical Notes.** *arXiv*. [cite: 20, 21, 67]
[cite: 25] **UltimateMedLLM vs Med-PaLM 2.** (2024). *Stanford CS224n*. [cite: 25]
[cite: 17] Pal, A., et al. (2023). **Med-HALT: Medical Domain Hallucination Test.** *CoNLL*. [cite: 17, 55, 68]
[cite: 37] **BiomedGPT: Open Source Multimodal Model.** (2024). *UGA News*. [cite: 37]
[cite: 34] Li, C., et al. (2023). **LLaVA-Med: Training a Large Language-and-Vision Assistant.** *Microsoft Research*. [cite: 34, 35, 36]
[cite: 32] **John Snow Labs Medical LLM 2025 Release.** (2025). *John Snow Labs*. [cite: 32]

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsDxYXUBV3ENhEBcBLXUh1XECM-UsySAuA_GB_N1YDfj2cgqWSxhpkstWjVPwELyDLHJLd_k3x2Svh9TX6wFfO1sLf-ckLW_VL_il3wB1oMGE3gqgwyNzb6OqnaO5yaw==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTv2PbrS-KYSHaCE5w8RbTj_IOaShX6ij0wCK0K6jLRSechY5hCPgwZlmPqyfPohgOFbL-eFGTq_Yr8yzRrWeW-PGSlmsdDVAjcc6woMWcifnZ7TKIGAuWhxNdNl9YEsB1L6tZtova1ybbgdo5nZOpZr_NgTPvKmARp94SmYv6lTShW0dZRlVcQ9l89MbceT8ElTAYe4cp_sZMOiIxVVJG4SZNSspuDcj_zWRtmw==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeWL5mArdtvMnaxuGLTF8XXB0C0puVLSd4oMWMI-Ow5smUnvdJRVwmdS1zC2xGRks6jwaWyd6aC3TOEH9WPn0r8ICp24KNWRCv81uUVQZoLta2ZV6Nwg==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBREtrs2TvAwnugkuzW6hkg78DYMj3jPlxsfqgyO0nVsPUIwZ5saUysBVvPcNYRefsy84eXqGpXTzN4D660t2JOO9qjsLgCjbtp9LkmsqmXqTiJhp6F-AX_93T-lpk16eZvFnfQQNt)
5. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpj_SQ5G2ugswTL_4jKDam-vdYpmPLd-YVaj_f1H-KrBpeJApyUEsF3RConsABHn1Tgin4uXoQoR3oVbInz7ksRmpfBjb6xt7SPsszstRR-TjcoxsBzPRwePNvajHickx_5iYKNI4FRhCli9Zs4buZGiJc6d9Mr7gyTIDBJune9G0fM7exo2GVX_bsNprEN6p2TM4s)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHqkUWLKavu6dUvDmTbIvd745J1NoWTUrKp7DXCHzAhbHA1IcLL72gzjukXxqvoL_mBcJtwJfGPLq5hM6RejKTiyAj8mRdovCRpX5CPTA7tcBXPn2-N2FCBw==)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr-Zth-ZDph2LLLDtbb23t2CEhKa093HtZDGWkq3l55RLA-cvyepDiyIBp_xG7sBDBFOpyCMn7UtUSM9yl3Ow1GFC04HxxtD6igS5JzdGXGi6jnfDCMpF3OA==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFS1aRFilv2-BRE7X7aAeiNd6oUJdum3YvftFRbcXItYuFGcPWK2PbtCu26h8jJjaVZVMtvTBT-X0v_b039E3ExVokEW5VpAWHC1R6Qr8LcaQPcRQtv8A==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd7ChN7h9h6rcbfuxSdagHqDCaraRb7hiPbbym8fGsFLMxjBXR6WtybPmUZLyEQHzCYg4YYq7tQtQFMIlY4NPhNJeJt8k6X3EF9yUPNRGQckeiS4_HKE9fteyEbxxb_GhS3C_Fscouog==)
10. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKrJCifnDCaA_LSWREetGYVqtjPtJaaGNaLhzIPGvob-NXVe3JJ27HPAW5V-TjyBO_UUChLy2B99OSrKdOTf47Rw_U6U_Nmgt3iOjRJDUwxMp62sercgYDyH_WTL-o_4McWqQVlMGCL01PnPyeEHg=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEasAEgXsC4g2RA16xxA_i4j_lMF_6HLw21MUPtp_J16Vr9y5htxMtmRBaOQbb6VvyWnL76SItnZMOst4vF8sr7UiJyd46kckgxhFY5cZGYP9v6gqtFd8gC3qrcRaqbaHRIsYAgugiAcCMpFb_bUEoAfw13KGYuxyt8gEbcMzK39E3qEBm4D00fs9nO7YbrrvhBPuJaU5XBT3n-9sFGisAlGuis1-mnGu_Bbq3u9xcYTdLr4dcF_ecz6Ozys_zaHw==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIh9AkGcqwRsh0IkShU1jYlYQPjyvlHwHHbJYpJnnfZedVR5vVv4lZ5ygEAhRYt3zNS764xQeZii2zPa1EE8bYJG1DZKmXqf1aLdUFrL2YMe8rfN7BP-UkvdfOCXGIUTbOR1zBl9VOYd6w4NpP0qUo4qM2iCK633HdFiP_mXyzawG6yW-N5608Fi2ZdS7Kj4EB1ob6_F9yy9vIza-DL0AfjnnWWuy3jNyEuTecJ_shCKPWgEfl68YitwaYTufIWw==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEbNkXa6ghQUIklUCJtKsOEyq5JRkSS_uep5pQMur-IDguUrOvmvNQXEWgYN8wZYag8RWHr-FYEC0Unh5JPpE3T7UxEZOls-giR9neDyO1k_bzNmc2uPCnlbba0fjYEy3xIGENeX4RfA==)
14. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH88ieIYg2Pf5orx7oHk-8_CoQGsf4MiOYBiA4oQZ9i5xvom4Ae-bqIlUQ68JdL8KJMGV0VtF--Axkk9RFtYM4NnzH-yMS9FpxFbAPUOfKlBmPCd4OlgW0HBy5Dc_8dwVc0JWegmJhvUhKJF3DLfjq0tsKqjPmMe2_mqHmoRVyUfB1Ftrv2KozpYbmCTr73daKMB27F14Oxo84tSURKDqI=)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUP5Ix3_V9l20CUF6s0zwflHihs2qWfjeio-Kik2VxwlQlJ1PjDPzPVdoL-Zy4uvsmAE_IFJcbwteUVLB8Pd99kuMLRWgXFBS0jzp-4E8HMwjFznrKYUu0w==)
16. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3uqKSy3UzE1cVtjxkGuGiHVhXbQCYO-L_NCA2v2EOIj0HURN_GxV84stdsm_Wkvn8Yje1eEmlOjhVAwWOIAue0xSJVOY44P6iiL3dIrApdUU=)
17. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFv8MCBRMDLmmpdeUZGGz9VUgQDA4JsvxnOGLDUcbOgq8wD3SbXn7bgnEY99ucv55mb1k9xAJeP3jkji2rlYP_9Mxulcdjaw1wKtOd38_QYQ==)
18. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8pwxhTOKHmjq8cOftFONLxOjOEE95iCI4NMwmyYfVMM6Ty-4twuVKoVqBdnubmLsTAuaWNRi3N7nQX8RwNMjqZ6F8CWF2NwHa8qFnQxDr6aSodlvU_tUWBwi4WBOUgPqtgbuf-jMBfcveysn_LxUkIz2GyPCsxg==)
19. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb5lspwwIlU9zWJorSL28pReKcwTngB2qYI2uxqJSxoBT7O6RBRDi2G3txfSn--P9Sfoow0XSjmBax7FcTRASKi3Tm3T4_6BUI14oTMKN_X3v6-MW5fMctHFvv7q1aWbogdAxuGdrulDMnAaa1X_4DgtRgt2KQc3kBzQia6xj-8FbqVu-ZeP0ujl387EieI_nxzZj2rSeAKwHMbEhvDy0my4NotA0JaPN3RidQydAd9hdUaTff)
20. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6B8cv24ELbmCyeX8nGhcepCQxyXpMpWnWiTJUSik-pnwsjf3um3-EbEuWSq37nDST9bBp6MT2OWnMxTIm79mxmnXw0SSxF_fGbz7NcmDPzetrhzfH_FwlEz-z-6HIHrZU5bDggr7xd8L9v8_H4GMTXfxj3adJctjEPGNE1Z7JbaA1QVrYOlTUKjeopoMxsCPbyxeUxeN8JxsTb3R8TQhVVcFQolg3uy7Di2NIQ5eJRm_aN86KXrjgk9C-fc4qaS7X04DcV5HKEm0=)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpQDmEcV_RuvKJv0JolN99FksHfZqcPhlY0q5lXktSdmb4mBKRzZ48Alg4LCiV0iBq--ULeBTTITZhcOoYf2_1gTQ6YJgxe1MV0vjkJcnTy7oD-cYNKA==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMtJ1VEs88qRPItX6sIKJtVzaAkL83UR6zV86LhZ-oIBuSrnZqGY7-yXlPwEVP_rJITo4Ss6nlEuG7b4AnBOYeroeDcFPzmdtmiRkoSvnT83k0BsFwHNsbCCZZsyvz-GsLjg4_NQ5AxnjgXKkmpS_cyfWljebX1_8v2xDPZz4u4RHxV3E4sbYSzrmtjKF0kjYKVwqpXYqhMDyQEWjzeyW0jQ8pUcnbZbU3GMnBPeEU93QTjngUing0sNAE0_siuGyzALSmMIihxbrhGtfxKiYHuKbGtea_Gg==)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-UDdNUUvTWC6zYs3Vb7d7iyd8B9Ztm9-mTbmLRv-wJNV-kjiTO326RTzDEwNT_6IFt1PngAHnzXvOkmFxMgGXgz5DSbhYyaNVWlsIjGvlYBGeBYdZp2EdUQGBXuJsZ__59UO4JF3oYQ==)
24. [dr7.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAKxSZd6nRkpCuOPjJN2ea5LkWvv-buiQaUBVZEVE_LK2-BuWYZo7aizAn10qeg6y3mgjnBv9QxR06hZ8IVwBzHGNzCtYlY5KjOhsGqZVgRCXn8PpmpY-RU0TUJSaJiBHAqkoih41_Suft6-ILjsAkYc-3I9QOK3mx6CEMvwxs8yculkTNha8s5EfNEXVJtIk=)
25. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvUqVA-TbzJNnQqOtdHMrJWMqojOHiyqT-TGOaVjLXpEPHwO2vgQCcEovySx2o6UZwSehUQV9faJGjfnPDGAA8RXb66KPJZY1TOPqMk3MKJsjITha3B0Yuz_liTRb3aFKnhaTDCKPEv3OwJmaFXOyclItFDxFBMw==)
26. [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUq7O1mHi2Nq5NKKoR0YsQODrzKOp5g15fhtnF2uf8n6zhwt3X0q37aTPuwNpptGIHwleexEwOxMZ2usmx_oTEvxnU6e_fjP0gBwKccucbNp09v8T7YLuwh0JxWzAQJS8MCAl)
27. [dataloop.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOcdmpJ75u2O78CYqk6e0NXEyduNTjrRYIr6Jd8V7W5FfiCme9uns0Y4u1-UBcOu3VGr-QDU6SbSmo6Kpv3qniBFdu6B2J7bxdjugwxUKz0wJCM56WlLGO2XU_raszP7IGsomfz1TBwRE7xsuc_gJKAHOtufH4)
28. [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjYRo0u5iDqQoql_8krHJGhvzHcRU_Idb0cvK_L3LXnBplVBKEprRYzmX6FNaIlHi45bTzSzlZE-AAXETPBEIaCFMG9fi2K_dYrg9G6uCDR_5KDH1C9cu1DqicB9IculTwZ9ap3-RfvFNq6VcjurZ4)
29. [saama.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyN4JHCMGMLowe_A6xG9n9-N3oQCK1uAMFnAYXn2-zyUItlAWLNh8_D_pFD3FlYFZvvZPdtEUC6FbWkHSF5bpmOYvwACkj-KYuiOp4aOS9ZGgknTqeRzitCCoyMHaaCViQ-1K2Ex5VMMIlxvShGLXCiQ==)
30. [opendatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvW6wDVPsx_ssknnJYjHNdR11HDPZMcM9KCuyB3QMWPuZlNknDA7ZuIPo2LjMN8GdKurPYvfbA1dizJaN0tYUJjT-0gZ8Oece2RdiSzDBnqtmE9YLdKZ-snZ_BRwTV9I8k1yF07RCeRAyl-n0MqzkzJgyGX_xvlD_7XNstoj8wn4_4Dh2m9gaKdWL60-Rx9uGJwdISQcKf3co=)
31. [amazon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsEpt65GS-rKo8mjsFVCYiAmQO2TcYo2YArUAzzKkwIJwsckeggjErEGkWGETe2YSZJkIgwdO-WfM--rN1MkqmGcR-b5f9tQjrAGHIy1EBy2G3P3LmPL1bOw4L3YEuG1-N295e_BYUycm3BhCEnvnlOtfRm9Dm5Ko4FdpEmqEi3W9_ZIdhoXa0pzqzQYA-iUEe60g9MHHi0jXSk8PaQFLPoRoA9k-mVKznSjADFAJ14A==)
32. [johnsnowlabs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzAQ01DL_eFANb3OYBZUtsAYZCnXMRJPkivECUgy9O2Iiqo1pdo4bOGrfx1F9GT-WZr1dtSteeBVqqXzyBy-VQTYW3SC3coZ_f037ZdwJLfuHNIl-Oec5CK5IOlfid1kHKuvSCjVV8O1Ho5ebM8PTHzEBWNaPAo2A0upbF0o16w67h6mH2gDTQ7n4TmwF5OMmsSanyjWDA8eT86GtckCRC4de9)
33. [dataloop.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAiHSgX2z5M_npjczlzCrK6nvwPqLbOhyYG7dLk-HnR_GuTR0_vkY1e9XesID3OYt9bJZVlyxovfB2Ee9CZWTlqrqZAtWEDl-48D_LoWD3-hTKORKgv46qCPYQ1yNJROK8iGseRjtGp8LYZPgVjLHVA6Q=)
34. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE75UtGZBmb3xoWsymSJ43xy3vzl90DN8hQ28WqqVdRBAlESD5ZRdBw6DwfDMX9-Wkdzwd2FBCLEG4yGrRYKw6pF6-_v8MHbs5xA_kwiATSBrW0zk6nwETpfCeyRMfUVQQ6viyhOL5C2hUP4ZU76z1-iMM1S6dITkmwQ7l9glwdKrOJH6ArNRnKd7NqLTjns5h7-D_VIdTr4fsMi4dQF0xOFKWhloGpglaa5YHpobT3scHdPqxRutnJhc05NHamgB0=)
35. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgZyheciQQPBtC036GsEPkH711egK-zXymli3mr08TvD_sKsTJwPOh96PjqsSOShcZ7ns5_kG1a6N-QkqnICD3k2DeEQDuYl28qrYy899BBhq8Xosyr6v5FlbEUqjkIaLIHfp9c65fCYLQPzkgQnh0SZUtH6d2fusjgTBXMEq006oDDSxssczlzYYDLMnrYjzGlT5-U3SH91j5RkpjnHHuuXJUPpCDzkFCFKb_gng=)
36. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOlAepfP1WXYLkj1AYkmaGBEAMHMQbjjIYSiz4z3uK8aFQN3o5K32U3Sg-jnY6rP92NujM3ASAb22oOBxYlZ0SsVxfL1b9Dom6Hy6fGQLjxIxLyJAYuw==)
37. [uga.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmqTaK2ASP4qH7D7WYnvJuuV81KvtZjn_wvM0z9ONUuqhSNsj41G2W8uwjqpjrdVIEceiJlCP_nJvh3o0kX-EFmKN8Mg2AdJcnOi--W1xnV-oJiNNfhgznebFz7vaNxV_Xlq4u-xKJhX3MPyc8--iZyQGHc4Cxirzx31oPFmpkgK_KaH4GtNnrtCrSgp_XHx021oQi06mm7HrXrJwmhdcgkhpzVJA-RpQ_7sse)
38. [marktechpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkA7PjsfTPI0GX-qP2ue2d0vAo91qywslzGaRw2jWvuZb8auQupz8cMEKbcniy78sd9MDpEHfmDWLU3_BPxGKtYNg16ZmihKKPAZht5nATtXlW38zq1cj6Bd4WAI28MlOHfAuDz85LY50yAVsx1tW5NrwigWLGvEZhy3sndDhuck7RHD9M-upmJCKF7iOMm9inq115WGc86x4wLlfZQw1N64Ol0qENMzQ8MbGo__ZJ_voyRxJGzIEnuCe4jpxKcOPbyN9t_ckVJdgwz37yohnR3hujGttB8GKcLag_xb98HA==)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl2Ep38fbUhKQECsOh92YekOvYhagEDdssa5XVfb-5YOjJ4FKoHMEH7CpNsAeMGZpAp1BMayxa6JUmRGRLo7h_uwOB-uj2vh7woIVjrIB7g0D6ySRbKjpRYwXSVT7MxQ==)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnFsbwk4dS4JrjVGgDcxYNsK9BPKOOakEn_AWZ9o_WWfe7Rbf5c2II2IS82rWIX0ptdOIY2dTqbvHK7PuWKuPoOj03pRwzyXOyOw5qrrAeGKKK6MTVUdlFBA==)
41. [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgvuV24jg1xDBPeHbgso9TWEGaTIgUle7iPtyIehAxofwPbTtK_PGj0nPpbMefCBHXA4QTi8KKDGL_42R4VjRfKgmd3iNk1SDArhJntScayGbOSudzpJbyUBP4dhRxvskAihkGks735jE-4Vz4dLgZphWO-8Ul95TmP6X58qXI)
42. [tsinghua.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOemNFGX5FeT5M_-wM1PfvotIFeQLgwAFcvbiDKPWBhyRnygREmIwYSNsbwE7ur41oa0Kw8OjLPLGw1fIYcNEl0U0BLInBvtgHxvATHgzb7WZtJmtaCDBtCEA5hpcONatLlX0S4oT9)
43. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB5Jaa-VZau5NEdag6fD1zQ93WTJg1hV5ffKfycsTYlzVeH1yAqViE2YG13vCwJO-DnXbDQh_cOP3jDkmTNs2kgiOYSiYC4k8j839pDwBKX9LzP_79_A==)
44. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw57n6FuvQKor7IIeUCSE0Rx8mG1a7uImgeHEXlhiP43ESRdL4qklN-fPeI2Vc6BtAZG_HG6EupsP7LACtbsxpP-HbSr3r_4dp_DFNryNrAR0XgGcHLPpAHo775h2L)
45. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ3A3473V1jQtQqRRMJURTO-uFpd8xO44G3a7NaqgfY3QAIU1eGnBhnUh8DG-iwqjq_Tz3lyF8fU2DbTW_YvQe9vpvsBU3n_o0LOj7Hh4RHhwWQxSMlBUsnWL4eUfkbJFrZMKBgbHkz2qKEb3T5E2dGMqH1YheowZeqtcM)
46. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtDRHGxUGvL_NqANy8g9WUNPSMKsPP5nHrEGE8fzY0sgaYC8In929LlEfx1jmMWxWHOqp2yyIwMt7ASOvfr-6nuBpgVU6lDgAFeuKU_mx5TU1CjChsXxn_535A-SYjRF1KXR932XIRfUgbuW2iRrj3cSTx)
47. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEshYShSJbeqdqAch6FsxoaxKgaRr6AvZERx0-TNQmmf9XbEYPiVgfUkaI_dSZvCXoEASYdRFzb9u2PTFIS6CYTrPrSLfRakyMXp3mD7VlqQdwARuioRw==)
48. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI3R-i5e0QR6SvA1CAdmWYhi4o9GZsGfpyOplwvIg3Y0RdBfLKeGtWOKTNX73wnlijTktZR3k9xqr0Xsip6Hnt1oBlW07layzSm9ed7J5pi4-_NbJ5Sg==)
49. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3bseYt3qj7QNxUpHVnOFNk-Q_XfEBIXjCmg8Jn3-1gcNivIh9C1OGVYuCITjdviocrd530z7dSWZmBjQPyYkV--bSPH8EXKNdIdQxPrPnt5nBv3yqeo1pbT0ZBdS7LQEraVz0abdpG6gpwkMv_rRQwnGeHMZz6qqmWUBvAdJGLC2JjaabCTKGZwGJYfTfu3pdQFGL6TrJlbgosiKuwzaR8yeZEVsVhpcjjUpZPW9ss35PaMicPmiUx2SkBYUE_QLsWjEF-R1u1s-FfgC0XZ83yS2eiC-Vo0k=)
50. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9wvxIe_VkMf-65EUIdI7pYKoiFCNhiALMxloEJTQL30hO0lSE0LQt_BRHRuukGzZojIFPyz4JB4m9RT_30bKZOoWY2hU_AL1d7lvyym5bOSEvB0tX7yTD70P0kcJkCQ==)
51. [ijisrt.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCoddyxWqXDPdOW6PDM2_9xIjidp32nQe1kn8LCYQOcvyZPOOTU9En8DCrYieF0WSFKj-5JR38Co9G5234SBrXU_c2XimP8DIIzv22QpK7aMbvDOUF1WY1F26jVuDbz44q7Z6YJTuMjBhBcci2CcYaQB6iOtcX8t-TvKJIh1F2kYBYMZbeCyglSddQLd5jIRJrYhq36HNIKoS3Th59prS0)
52. [westminster.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhXRorGp2I0CvoxfsawOMJuzxk-N850nncWti1vjpBuoFQpc-i21G7W-bsH9diFJnEhsxSK9DtwCl4e0Jdp4MuWuj-po6JdjQ9EUniONol0sVKAi-HlbMU1HccaynIn9LwdPYCcxoUj3WJzkGBClQWE_y9hdBGqpHbSsrXlnScZ29_JBxGgzXdzj3aH2bSubsctV6umruZDLwvIddNqLZ3nRAT83WAh3CP_sNy7Q_0p5eAAuZOq0MXvPhDi1loMKy2PXjLRdRQNbQq)
53. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEg8C-T8Yl7T6JVgHuPcW4h69cnL1IaoRgVWNrPSZH5qucjbIlncBBHQ_5GwPmQ-336If6C8gnol5SQe7f7OJl3FOBbeDvR_rUgJuprBiPr39qmPrzEYAdptfiogJh660am0-seVcrKY7hgFMn9Kp4oTLDKe30s094Lm73rzTjx_lQ-py0upQ==)
54. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoo-Exij6BrNKQD9rcZAPPHCpVlIKVMxUReRo3aIeawA3s_Ptcue01iIY9-0-LHTXQdBuRLDqr4-_xgx6VNubOweQAmv_x_Ri-VX0H0uB-4LuYTdBylp_vqRC9Hx8kFr_F22Dx7EayNg==)
55. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFjjnrGi8GqGnjjbUfj4fELwXX_-fpwoxxbgqHHNMZ2IhssIR2RH9lyyD8DAxR5v9cieocQ8iYMK7DcA3NTnmE-fEWsSWrEmCOLhsFA92qR2I1YZPn8m6X)
56. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3-g52t2fko1JMHCqSi5uVqF_jxcnZ0O2jhGUE67pdpi8ghmHThTrBSzZ2X0pW4EpogZ_LDutCWVpR5cm9ZmwWjLe_aM_AAb7SX4xZHpxmvVxxhC14AKwH8PoPdv7CGl1AwxtwpDFlYw==)
57. [medify.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEhLNpDDnQvbb3_vTFHRKvPcUeWCV9Rm_nkObGU6IxtaPHzpYLF91p4tPP39luRxiYWku24G88dqWL1zFaSufyyQHGNo00M9mMlkfU0usyfcXXZprHup5G6EMIUgSYAEZKEAoNiIhYAyywXahAc7TupQXbWpO7SJYqR8C5kFCA3Lq0DKXDWUokjWl78pkZW2akfL0qj0v-em0occu5kLIwidU4ukfJ5ZTciA==)
58. [munjalshah.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwz4c3kiOpDzuqlPG5g0zGDazkmccHBBTCU3TDlmSjJIQYFYxZnibqinZ-bO6x9Ass75N6tZqpcJzEvGPZqKPqtSOQGw--1PsrjjXY--bBX4mTKbWhHxvbauSbn0IEWpPEaFxabAA9OT3Iiut31KIF3o0DFLmfV8czF9-IfsjDPEPHAAI9ODAZsJfzno7-cbYyew==)
59. [johnsnowlabs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkSYWhgIWHNofyQiVIX1iwMZBb4F5GQkr3sEbjUoXyR7mkUwsy-aSkkzggw5oBFfCbVX0QDHsPrpX3nmW_Yu7tJP4ibutcQsFQk5QRnfZmirjrzo1Hv7zP5nIsgk5B-4VxSPCdbAmapWAJAznGrr7R4VfyIAGMwKFJMJbjuS-kE8JMrGPa5W4mdlBOnKJYWeMADzKD2miBQaRyUk5X88oRTjp7WlCqTa7-dQHlCB-oXvP8eh7_rDWACibUkKic5FyKOySucBrs9xbGfI2hugcxPdm5ePBTg2_BrMJutFY2PKDG-BViReVOPwWPGjrjCjg-fBM-sBQ=)
60. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkbIfhNy6ygNkLYUhzZgfILwlHAdnRkGOkuw9p-s7AazZTG70hQolBnLEwUGwIY6uWyirIx1bP2IRpNRrlDjexlWX5Raovxv8gyx0V5pFlcdVDIvCXaGInlyFwBIeXemp3Dh3q0XqvAaLnt0wTuDUdCzlyXW_z9lLISHQXLB3sOJ4e3KU1aXdS7VKT0QCeaX0AttK94RB4ztEZuthFh-YkYHrPv9dC66wLr6AmsxF_iEvbj2tixwiDSsuI2jBzCF3AlUkSUdYOvXGx)
61. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE61pnfYIEPFAFwrAaBe_CfUN5DiEBBwDbVC-3xl2PollUa5TtHTMjvV3yy3IYegp-q7tj0CAlbQLMo9NccZlnju6RN9KvrFi3pFmkKnCf7d1o-Yk09xsEg2RdVBg==)
62. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSf9llVc_ivnTRU0vnc0OylC3jeWdtIn-FDIo0LmG6GfW8TFBzicTeGtpBHfQG3FRozsJZhtUw_tTDtvCNcGkwzPjNsJNRELxl0TD8FRthOo_9cuidnF4PjIgc-_40hItxyaNdRGtqHIUXcMM3uKi3I6ywm2bZvHnmbXCBrXgbh56QyZp6WGL1gtXsRlMlhyiBztHlgnb6GqCfD9YGd8Rf0NwloQMbTLNf469eVHKD8EgJSX3sOfxTIUHP3jia96Q=)
63. [vu.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERYm8pjgG1GhJ6g39a764gVBZtE9RVDCLGOVe6SDScguQWsZLTMSbWWNXXzNDqE4_mMDe5WpdnbAiEggKsTf9PdXa1hXha8p829RwKVpktQJwr3tAYF-K26qZ686oAFXMVG1M2m92PMrnmGVmmiLPnHYtaRTEu7JKfWaWHcx58EiyD2LxOow6vbvCRiodBLYvdFclQE07SDkBTBVHCEyU=)
64. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNZCKW17Kqg9HuCGYg7HEWnN0IIa43cklBOhmocj-220V13DHUEohk00yE_y-iTxb8TxZmtEZJPyOy2r-h4JsWy0xJQdMdUTC1aFkY_PihAqifc9ZaPLRxpajvHyXBTg==)
65. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyiM8U3qXBNKo9ApIx8uRqQzjJd_SLbdK5vRo80Mqpfl5e-OAWxWSh9z2EAp2ps3HZme_ee9loL8y90IEwT8uAtkXudn0nuet-kHbvNHyl9IITJr8T7rwOww==)
66. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHE90Mvc2A9NW-aF5y_CRjimV0QvQt7xsIueWgzlNr_zxpWa9oV_PSAtIRqherd3QRvv94JMfDbYMV5cW8AznczIpn6SKBoobn7TyfLVx5AkUjR1dkT8bD6TdVRuKST1hvcoQ0=)
67. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM-tBCwv44carBVsR0cBghsU8pofgt1y8bgNtiGJD4ljvnInHpiS2ch597-Y5v8h0h6HwXruS49cv_ANL02THwC3aduXoYm9mVe3J_95_4MDm85EaRs_O0EWVwIeIUw6BGvPwDzzQBxv9Jv7ZRIMFfqaMdnVRfsXGmZgfdNWjmfFY9ih2EWAWScxuava68SC2TQOLHKUTYx3M_iUGeBE5QtFTKgk8aSoccZvKyVbO8mJk=)
68. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDo6056l0LOAF48oxWpvDzI0ge_jXGfDkzD_x2WRUXWU_WqV6jkNpEUgFblWst163Wp3-DkfMq69k74z0Q8inaZ55szv_kJ522CcLuKBJQPhWjGF5rlSneiVFTEYMURA==)
