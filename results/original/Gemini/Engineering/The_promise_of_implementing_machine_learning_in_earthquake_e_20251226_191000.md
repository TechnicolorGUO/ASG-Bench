# Literature Review: The promise of implementing machine learning in earthquake engineering- A state-of-the-art review.

*Generated on: 2025-12-26 19:10:00*
*Progress: [17/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/The_promise_of_implementing_machine_learning_in_earthquake_e_20251226_191000.md*
---

# The Promise of Implementing Machine Learning in Earthquake Engineering: A State-of-the-Art Review

**Abstract**

The integration of Machine Learning (ML) and Deep Learning (DL) into earthquake engineering represents a paradigm shift from traditional, purely physics-based empirical modeling to data-driven and hybrid intelligence. This paper provides a comprehensive systematic literature review, revisiting the foundational promise of ML in seismic applications and evaluating its current realization. While early adoption focused on basic regression and classification for hazard analysis, the state-of-the-art has rapidly evolved toward Physics-Informed Neural Networks (PINNs), Generative AI (diffusion models), and Foundation Models (e.g., SeisLM). This review critically analyzes applications across seismic hazard assessment, ground motion synthesis, structural health monitoring, and post-disaster response. It identifies a critical transition from "black-box" predictions to interpretable, physics-consistent simulations. Despite significant milestones, challenges regarding data scarcity, generalization, and trust remain. The paper concludes that while the promise of ML is being fulfilled, the future lies in synergistic frameworks that fuse domain knowledge with the scalability of foundation models.

---

## 1. Introduction and Background

### 1.1 Research Motivation
Earthquake engineering has traditionally relied on mechanics-based simulations and empirical correlations derived from historical data. While these methods have successfully underpinned modern building codes and safety standards, they face inherent limitations. Physics-based models, such as Nonlinear Time History Analysis (NLTHA), are computationally expensive and often rely on idealized assumptions about material behavior and boundary conditions [cite: 1, 2]. Conversely, empirical models, such as Ground Motion Prediction Equations (GMPEs), often struggle to capture the complex, high-dimensional non-linearities of seismic wave propagation and site-specific structural responses [cite: 3, 4].

The motivation for implementing Machine Learning (ML) in this domain stems from its ability to handle vast datasets, identify latent non-linear patterns, and serve as rapid surrogate models for complex simulations. As articulated in the seminal review by Xie et al. (2020), ML offers the "promise" of enhancing computational efficiency, treating uncertainties more robustly, and facilitating near-real-time decision-making [cite: 5, 6]. Since that publication, the field has witnessed an explosion of interest, driven by the proliferation of seismic data and advancements in algorithmic architecture, particularly in Deep Learning (DL) and Generative AI [cite: 7, 8].

### 1.2 Objectives and Scope
This paper aims to provide a comprehensive, state-of-the-art review of ML in earthquake engineering, updating the landscape established by previous surveys. The specific objectives are:
1.  To trace the historical evolution of ML applications from simple neural networks to modern foundation models.
2.  To critically evaluate the performance of emerging techniques, including Physics-Informed Neural Networks (PINNs), Diffusion Models, and Transformers.
3.  To categorize applications across the seismic risk chain: from hazard analysis and ground motion synthesis to structural response prediction and post-event recovery.
4.  To identify persistent challenges, such as the "black box" nature of AI and data scarcity, and propose future research directions.

This review synthesizes literature ranging from foundational studies to the most recent preprints of 2024 and 2025, covering the rapid ascent of generative and physics-guided approaches.

---

## 2. Key Concepts and Definitions

### 2.1 Machine Learning vs. Deep Learning in Seismic Contexts
In the context of earthquake engineering, **Machine Learning (ML)** refers to algorithms that parse data, learn from it, and then make a determination or prediction about some aspect of the world. This includes traditional methods like Support Vector Machines (SVM), Random Forests (RF), and probabilistic methods [cite: 6, 9].

**Deep Learning (DL)**, a subset of ML, utilizes multi-layered artificial neural networks (ANNs) to learn representations of data with multiple levels of abstraction. DL has become the dominant force in recent research due to its superior performance in handling unstructured data, such as seismic waveforms (time-series) and damage imagery (computer vision) [cite: 8, 10].

### 2.2 Physics-Informed Machine Learning (PIML)
A critical concept in modern computational engineering is PIML. Unlike purely data-driven models that may violate physical laws (e.g., conservation of energy), PIML integrates domain knowledge directly into the learning process. This is most commonly realized through **Physics-Informed Neural Networks (PINNs)**, where the loss function is augmented with residuals from governing Partial Differential Equations (PDEs), such as the equation of motion [cite: 2, 11, 12].

### 2.3 Generative AI and Foundation Models
**Generative AI** refers to models capable of generating new data instances that resemble the training data. In earthquake engineering, this includes Generative Adversarial Networks (GANs) and, more recently, **Diffusion Models**, which are used to synthesize realistic ground motion accelerograms [cite: 13, 14, 15].

**Foundation Models** represent the frontier of AI. These are large-scale models (like GPT in language) pre-trained on vast amounts of unlabeled data and then fine-tuned for specific tasks. In seismology, models like **SeisLM** are emerging, trained on millions of seismic waveforms to perform tasks ranging from phase picking to event detection [cite: 16, 17, 18].

---

## 3. Historical Development and Milestones

### 3.1 Early Adoption (1990s–2015)
The application of AI in seismic engineering is not entirely new. As early as 1998, researchers explored fuzzy expert systems and basic neural networks for seismic risk assessment [cite: 19]. However, these early efforts were constrained by limited computational power and small datasets. Through the 2000s and early 2010s, the field relied heavily on "shallow" learning algorithms. SVMs and Random Forests were popular for classification tasks, such as liquefaction potential or building damage states, due to their interpretability relative to neural networks [cite: 6, 9].

### 3.2 The Deep Learning Boom (2016–2020)
The period between 2016 and 2020 marked a significant acceleration, characterized by the adoption of Deep Learning. Convolutional Neural Networks (CNNs) revolutionized vision-based damage detection, allowing for automated crack detection from images [cite: 20]. Simultaneously, Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks were applied to time-series data, enabling dynamic response prediction [cite: 8].

The seminal review by Xie et al. (2020), "The promise of implementing machine learning in earthquake engineering," crystallized this era. It categorized the field into four topic areas: seismic hazard analysis, system identification, fragility assessment, and structural control [cite: 5, 6]. This paper highlighted the potential of ML to replace computationally expensive simulations, setting the stage for the next phase of innovation.

### 3.3 The Era of Physics-Informed and Generative AI (2021–Present)
From 2021 onwards, the focus shifted toward addressing the limitations of data-driven models—specifically, their lack of physical consistency and data hunger. This era has seen the rise of PINNs to solve forward and inverse problems in structural dynamics [cite: 11, 21]. Furthermore, 2023 and 2024 have introduced Generative AI (Diffusion Models) for high-fidelity ground motion synthesis [cite: 22, 23] and the first seismic foundation models, marking a transition from task-specific models to general-purpose seismic intelligence [cite: 16, 17].

---

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Deep Neural Architectures
**Convolutional Neural Networks (CNNs):** CNNs remain the gold standard for grid-like data. In earthquake engineering, they are extensively used for processing ground motion spectrograms (time-frequency representations) and post-earthquake satellite imagery for damage assessment [cite: 8, 20].

**Recurrent Neural Networks (RNNs) and LSTMs:** For sequential data, LSTMs are favored for their ability to capture long-term dependencies in seismic records. They are widely used to predict non-linear structural responses (e.g., inter-story drift) under seismic excitation, often serving as surrogates for Finite Element Analysis (FEA) [cite: 1, 21].

**Transformers and Attention Mechanisms:** Originating in NLP, Transformers are replacing RNNs due to their parallelization capabilities and ability to handle long-range dependencies via self-attention. The **Earthquake Transformer** and **Seismogram Transformer** are notable examples used for signal detection and phase picking [cite: 16, 17].

### 4.2 Physics-Informed Neural Networks (PINNs)
PINNs represent a major leap forward. By embedding the equations of motion (mass, damping, stiffness) directly into the loss function, PINNs ensure that predictions adhere to physical laws.
*   **Mechanism:** The loss function $L$ is defined as $L = L_{data} + \lambda L_{physics}$, where $L_{physics}$ penalizes violations of the governing PDEs.
*   **Applications:** PINNs are used for structural identification (inverse problems) and solving structural dynamics (forward problems) with limited data [cite: 2, 11].
*   **Hybrid Models:** Recent advancements include **LSTM-PINN** hybrids, which combine the temporal learning capability of LSTMs with the physical constraints of PINNs to improve convergence and accuracy in non-linear systems [cite: 21, 24].

### 4.3 Generative Models: From GANs to Diffusion
**Generative Adversarial Networks (GANs):** GANs have been used to generate synthetic ground motions to augment scarce datasets. However, they often suffer from "mode collapse" and training instability [cite: 13, 14].

**Diffusion Models:** The state-of-the-art in 2024/2025 has shifted to Denoising Diffusion Probabilistic Models (DDPMs). These models learn to reverse a noise-adding process to generate high-fidelity data.
*   **HEGGS (High-fidelity Earthquake Groundmotion Generation System):** A novel system utilizing conditional latent diffusion models to generate 3D seismic waveforms using minimal inputs (location, magnitude). HEGGS outperforms GANs in preserving seismological characteristics like P/S phase arrival and spectral content [cite: 23, 25].
*   **Latent Diffusion:** Other studies have applied latent diffusion to spectrograms, enabling the synthesis of broadband ground motions that satisfy GMPEs and physical constraints better than previous methods [cite: 14, 15, 22].

### 4.4 Foundation Models (SeisLM)
The introduction of **SeisLM** (Seismic Language Model) marks the entry of foundation models into seismology. Pre-trained on millions of unlabeled waveforms using self-supervised contrastive learning, SeisLM learns general features of seismic signals. It can be fine-tuned for downstream tasks (detection, phase picking) with minimal labeled data, demonstrating superior generalization compared to models trained from scratch [cite: 16, 18, 26].

---

## 5. Applications and Case Studies

### 5.1 Seismic Hazard Analysis and Ground Motion Synthesis
Machine learning has transformed how ground motions are predicted and synthesized.
*   **Ground Motion Prediction:** Advanced ML models (XGBoost, Deep Learning) are replacing traditional regression-based GMPEs, offering higher accuracy in predicting Peak Ground Acceleration (PGA) by capturing complex source-path-site effects [cite: 3, 4].
*   **Waveform Synthesis:** The **HEGGS** system demonstrates the capability to generate realistic waveforms for hypothetical earthquakes, aiding in the design of structures in regions with sparse historical data. This allows engineers to move beyond scaling historical records to generating site-specific synthetic records [cite: 23, 27].

### 5.2 Structural Response Prediction and Surrogate Modeling
Predicting the non-linear response of structures during earthquakes is critical for performance-based design.
*   **Surrogate Modeling:** DL models (LSTMs, TCNs) serve as surrogates for NLTHA. For example, a Temporal Convolutional Network (TCN) can predict the time-history response of a building in seconds, whereas a traditional FEM analysis might take hours. This speed enables probabilistic risk assessments involving thousands of simulations [cite: 1, 28].
*   **Case Study:** Research has demonstrated that hybrid LSTM-PINN models can predict the displacement and velocity of Multi-Degree-of-Freedom (MDOF) systems under El Centro earthquake excitation with high fidelity, even when trained on limited data [cite: 21, 24].

### 5.3 Structural Health Monitoring (SHM) and Damage Assessment
*   **Vision-Based Assessment:** Post-disaster, rapid assessment is vital. Models trained on satellite and drone imagery can classify building damage grades (e.g., EMS-98 scale). However, recent studies note that while Generative AI models can analyze images, their zero-shot classification accuracy for specific damage grades still requires improvement (ranging from 28% to 75% accuracy) [cite: 19].
*   **Vibration-Based SHM:** ML algorithms analyze accelerometer data from instrumented buildings to detect changes in modal properties (stiffness degradation) indicating damage. Unsupervised learning (Autoencoders) is particularly useful here for anomaly detection without labeled damage data [cite: 8, 20].

### 5.4 Geotechnical Earthquake Engineering
*   **Liquefaction and Lateral Spreading:** Explainable AI (XAI) techniques like SHAP (SHapley Additive exPlanations) have been applied to XGBoost models predicting lateral spreading. These studies reveal that ML models can accurately identify critical soil parameters (e.g., from CPT tests) that lead to failure, aligning well with domain knowledge while providing higher predictive accuracy than empirical formulas [cite: 29].

### 5.5 Regional Seismic Risk and Resilience
ML facilitates regional-scale assessments by integrating diverse datasets.
*   **Urban Resilience:** Graph Neural Networks (GNNs) are increasingly used to model the interdependencies of infrastructure networks (water, power, transport) to predict cascading failures and optimize recovery strategies [cite: 20].
*   **Early Warning:** Foundation models like SeisLM and SeisCLIP allow for faster and more accurate earthquake detection and phase picking, which is crucial for Earthquake Early Warning (EEW) systems [cite: 4, 17].

---

## 6. Challenges and Open Problems

### 6.1 Data Scarcity and Quality
Despite the "Big Data" era, large-magnitude damaging earthquakes are rare events (the "tail" of the distribution). Most ML models are trained on abundant low-magnitude data, leading to poor generalization for large, destructive events. While synthetic data generation (HEGGS, GANs) helps, validating these synthetic records for engineering applications remains a challenge [cite: 22, 23].

### 6.2 Interpretability and Trust (The "Black Box" Problem)
A significant barrier to industry adoption is the opacity of DL models. Engineers and regulators are hesitant to rely on "black box" algorithms for safety-critical decisions. While XAI methods (SHAP, LRP) are emerging [cite: 29, 30, 31], there is still a gap between mathematical explainability and engineering interpretability.

### 6.3 Physics Consistency
Purely data-driven models can predict physically impossible phenomena (e.g., negative stiffness, energy creation). While PINNs address this, they face challenges in training stability, particularly for highly non-linear, chaotic systems typical of collapsing structures. Balancing the data loss and physics loss in PINNs is often non-trivial [cite: 11, 21].

### 6.4 Computational Cost of Training
While ML models are fast at inference (prediction), training foundation models or complex PINNs requires massive computational resources (GPUs) and energy. This contrasts with the goal of democratizing these tools for widespread engineering use [cite: 2].

---

## 7. Future Research Directions

### 7.1 Advancing Physics-Informed Architectures
Future research must move beyond standard PINNs to **Neural Operators** (e.g., Fourier Neural Operators) that learn mappings between function spaces. This would allow models to generalize across different loading conditions and structural configurations without retraining, effectively creating a "neural solver" for structural dynamics [cite: 1].

### 7.2 Foundation Models for Engineering
The success of SeisLM suggests a future where "SeismicGPT" models exist—multimodal foundation models trained on waveforms, geological logs, and structural drawings. These models could perform zero-shot tasks, such as predicting the response of a specific building type to a specific ground motion without explicit training [cite: 16, 32, 33].

### 7.3 Generative Design and Optimization
Beyond analysis, ML will play a role in design. Generative AI could propose novel structural systems or dissipative devices that are optimized for seismic resilience, exploring design spaces that human engineers might overlook [cite: 34, 35].

### 7.4 Real-Time Digital Twins
Integrating ML surrogates into Digital Twins will enable real-time structural health monitoring and immediate post-event damage prognosis. This requires edge computing capabilities to run lightweight ML models directly on sensors [cite: 4, 36].

---

## 8. Conclusion

The promise of implementing machine learning in earthquake engineering, as envisioned a few years ago, is rapidly transitioning into reality. The field has matured from simple exploratory applications to sophisticated, physics-aware, and generative systems. The development of **HEGGS** for realistic ground motion synthesis and **SeisLM** as a foundation model for seismology represents the cutting edge of this evolution.

However, the transition from academic research to engineering practice requires overcoming the "trust gap." This necessitates a continued focus on **Physics-Informed Machine Learning** to ensure safety and consistency, alongside **Explainable AI** to provide transparency. As computational power grows and algorithms evolve, ML is poised to become not just a tool, but a foundational pillar of next-generation earthquake engineering, enabling more resilient infrastructure and safer communities in the face of seismic hazards.

---

## References

[cite: 7] Hu, Y., et al. (2024). Applying Machine Learning to Earthquake Engineering: A Scientometric Analysis of World Research. *Buildings*. [cite: 7]
[cite: 3] Amer, S., et al. (2023). Earthquake prediction using hybrid machine learning techniques. *Soil Dynamics and Earthquake Engineering*. [cite: 3]
[cite: 13] Marano, G.C., et al. (2024). Generative adversarial networks review in earthquake-related engineering fields. *Bulletin of Earthquake Engineering*. [cite: 13]
[cite: 34] Eucentre. (2024). Artificial intelligence and earthquake engineering: a new frontier for safety. [cite: 34]
[cite: 19] Estêvão, J.M.C. (2024). Generative AI for Rapid Post-Earthquake Damage Assessment. *Buildings*. [cite: 19]
[cite: 35] Luo, H., & Paal, S.G. (2022). Artificial intelligence-enhanced seismic response prediction of reinforced concrete frames. *Advances in Engineering Software*. [cite: 35]
[cite: 8] Xie, Y. (2024). Deep Learning in Earthquake Engineering: A Comprehensive Review. *arXiv preprint*. [cite: 8, 10, 37]
[cite: 30] Liu, T., et al. (2024). Deep learning applications in earthquake engineering review. *International Journal of Scientific Research*. [cite: 30]
[cite: 20] Xie, Y. (2024). Deep Learning Applications in Earthquake Engineering. *ASCE Journal*. [cite: 20]
[cite: 5] Xie, Y., et al. (2020). The promise of implementing machine learning in earthquake engineering: A state-of-the-art review. *Earthquake Spectra*. [cite: 5, 6, 38]
[cite: 36] Tapeh, A., & Naser, M. (2023). Artificial Intelligence in Structural Engineering: A Review. *Millenium*. [cite: 36]
[cite: 6] Sun, H., et al. (2020). Machine Learning applications for disaster management. *Journal of Management in Engineering*. [cite: 6, 39]
[cite: 11] Karniadakis, G.E., et al. (2021). Physics-informed machine learning. *Nature Reviews Physics*. [cite: 11]
[cite: 40] Borate, P., et al. (2024). Using a physics-informed neural network and fault zone acoustic monitoring to predict lab earthquakes. *Nature Communications*. [cite: 40]
[cite: 14] Jung, J., et al. (2024). Broadband Ground Motion Synthesis by Diffusion Model with Minimal Condition. *PowerDrill AI*. [cite: 14, 22]
[cite: 15] Ren, P., et al. (2024). Learning physics for unveiling hidden earthquake ground motions via conditional generative modeling. *arXiv preprint*. [cite: 15, 41, 42]
[cite: 23] Lee, J., et al. (2025). HEGGS: High-fidelity Earthquake Groundmotion Generation System. *ICML 2025*. [cite: 23, 43]
[cite: 12] Rucker, C., et al. (2024). Integrating Physics-Informed Neural Networks for Earthquake Modeling. *Seismology Technology*. [cite: 12]
[cite: 1] Zhang, R., et al. (2025). Deep Learning for Structural Response Prediction. *PEER Report*. [cite: 1]
[cite: 2] Zhang, R., et al. (2020). Physics-guided convolutional neural network (PhyCNN) for data-driven seismic response modeling. *Engineering Structures*. [cite: 2]
[cite: 21] Zhou, Y., et al. (2025). Hybrid LSTM-PINN for Seismic Response Prediction. *Applied Sciences*. [cite: 21, 24]
[cite: 16] Liu, T., et al. (2024). SeisLM: a Foundation Model for Seismic Waveforms. *arXiv preprint*. [cite: 16, 18, 26]
[cite: 17] Li, Z., et al. (2024). Seismogram Transformer: A foundation model for earthquake monitoring. *Geophysics*. [cite: 17]
[cite: 30] Sun, H., et al. (2024). Explainable AI in Earthquake Engineering. *International Journal of Scientific Research*. [cite: 30]
[cite: 31] IEEE. (2024). Explainable AI for Transparent Seismic Signal Classification. *IEEE Xplore*. [cite: 31]
[cite: 4] Dai, K., et al. (2024). Explainable AI for Ground Motion Prediction. *Geophysical Journal International*. [cite: 4]
[cite: 29] Durante, F., & Rathje, E. (2024). Explainable AI for Lateral Spreading Prediction. *arXiv preprint*. [cite: 29]
[cite: 32] Multi Foundation Quake. (2024). Foundation models for earthquake nowcasting. *MDPI*. [cite: 32]
[cite: 33] Park, Y., & Shelly, D.R. (2025). Adapting Large Language Models for Seismology. *AGU*. [cite: 33]
[cite: 23] Jung, J., et al. (2025). High-fidelity Earthquake Groundmotion Generation System (HEGGS). *OpenReview*. [cite: 23, 25]
[cite: 28] Sun, H., et al. (2025). Machine learning applications for building structural design and performance assessment: State-of-the-art review. *Preprints*. [cite: 28, 44]
[cite: 9] Roeslin, S., et al. (2020). A machine learning damage prediction model for the 2017 Puebla-Morelos earthquake. *Earthquake Spectra*. [cite: 9]

**Sources:**
1. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYuyu2zNAKyO6VL8XWfBvLxgvXx7v4zSFAhflKI8fLJvKVdz7Qk_kRQqU8fvX3Y2bKW8TzQBa1y1KUv_ucY5FVCo4JFv2QKv__zDEmmDTWfWuMbR969fta81KEdf-Fbd779axumx8ZqMJfRtzWRQqEAiMYzpJ0CL5bBRazXBrqR7o=)
2. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE_mBz20x44FGd2BcSui84t2XVGUgPwXYKeanhB43zs76OjiutCvd958HIIW4Yaloo-Yyw29XNTfUbjjCjqHvsfICvce_Ge0PwRYslkRtd52ICchljWW21x-B323pSmyA5Mnwwz3XDQz8=)
3. [americaspg.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHN4X04wMRd_a5lVXNe53OrQpG1ADetMoGjwLpYkj7zbo8I9hK9bqXverfb3IiOowMobwYfVsOQOXNTFQrhv91otI6iihRcH6GIJ93pJeLEsJGqnXxSn7Fb9zHUl4Z1zzjWVjk57GTLT0=)
4. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG2jTncMKtCyUDmDM5_0s6zjneNpy3GgwAjtWx_dyCnHOlSVuPtBzJJsUEX2dIIM3y_oQknrQrmPn9cN94zX--Ez9r_h7QKt6IV9opYt-J0NDcylYGqqgbuxeWC-F0SfJ6ZiYzAXyh0MiX33vMg_bh)
5. [geoscienceworld.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJB-OZgTh1wswAREc61_tj7NqBvHAqjfsLEa6-qgAK62hNgH7B04DAkGCsVJ-Bz1OD5m0QaaxqRwY1Se8wJuecKmpGZeqx0jtL5XGElKkL0jYCzn_-etf9-NtVodB_47AhUM4Q-82EE-nMaptjZeZwNo2BamOpj-mCo2wrynKDj9w6cwnrJUytskQezypZ0RJ_HERo4gPUy8jXLVsx3vaxjeekeeXmnRngOfGC)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfe9nOL4t5b6BL6u7nerWreFVvPUG2O2PqeuhrhuBI7wDN8dEftdQcPr_ViPIwf_6Imzo9MfIyeIaGFTxw1ZrH2lvtqOSVHnexxC48EzXzR83aQIEH0TdSPUmnS9Cf1p-HtmGCtUxxezGyLtvuHhBViGmaVo3v0TEASFWaeJK_G361VZEN-QXZhlPxwjBLFIJOWwtD12q1LqL2BO2DBm8B37haTVV_KgknqBP0fCwA-5ZS32fpB15VFvtfSKT-uaWOiUVYLVw3SVm6)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIjLkOguVcgt42qlzYtaIcRUTvWBjNJAiV0WBqGpsj7bqNf0mjla9I7x9uD6u0Zv4h4lR7jknPkSkvzFUnPcp0LunAPeJHrdbxjyEB7Oc8RnFJLWpeOlGRGm_QSQwoYTs6oBLVAqWJdXeA4Nm1M6LB7sBM9t9K26Q7C8kHVoNfkAUfeSEr8K96kumTjFJQe9zM0uz_Zn7Y_ZRj-wwUEMqHEk2XsZuY5fRMB1guCpkG1HJFvagfaZFKiggDAjceAPZIcRIspeZJAQ==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7clHvogGm3E7c9lW-P_743c1BA1zeaufn4qcQKkSvyALq--4DSq0eLVsrZ6exE2DASFE140xcyZj7bZL_1PqOBJqsbnaNzH3Qfn_IO6u56bPlen68dEQ=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGAt4sHWkC6Lah97wkUYwxfrP7lWlj1gqw8346VoDOJUsQjGbFR615OHy2oXiQNisUhKoDSUCdjY1US_j3gqpVSsA5aD68FzgWjPdHFSrtcg9gUS9zuqSi-dhA-EHWEKghuI83K9ZDj9UOU4eE85PUVtqNHoiSNbOghY05HRPaMe0ctPxd4uRtFaJ1nVvOHnW7TzVfqXYC0pwCUlyg2z1hYQAIRrSx3HZa2YXj1BNDTKoMKCnZEhaBgz9EBVz_MbAp7g==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrTCdKKxBqwkXib3GBTd5wQ3f6SIYBvSrfE5drPFHJv1Eq--PKchnbFuzyhzwZL5xsIWuzuwXlfl_pXzMmyQC04E2_rLWtQEBQD7JnFIaQWGFZaardRIcH67F0XO-EGuoFJaUwRoCZLNZ0SZmOh3ia-_yaUx1l2-pvtyszzJNnI2Klk8b14wbjSKwbY8T3bb68spmHVN-DRjQ0x4hQ2BSeHrYv_GG6uw==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyjuZ40Mh82hf44y9O8UzWqrOqJdWaeiPFRowiqXBhqZ5QqF8rDaUa_Aw-rzIeaWJgxgvhOLpnpU4p3fOJ0z0Mo_9MeASK0YB6aqBhr-upDqPYIYC3-rDHW9mGhKXDWpMa-A30ABZUimvumrgWzPO81Yxs02tOAliJ4Pd98QM_RJrH0UDsJTpOPuKpw-fhzIdlB7xZ5g==)
12. [hackernoon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzdr7wcUnkuMCNF2XRpE2wL8LFV6V5you6CkXYduaxB1SrKAAMUKbAbxEN3sHgVvXHDtbq_73xgdqYsUYt1JO9ZNb3al3ukzGihdQhOmozsxOcYDx5PLsBeO9JSY9zHVOHevLg48ZAH69IeDMeyDHenwuGs-RWZ1bed_TpIVejoyzcXFqhsdsCTTUgTv_f2iczk-9Z6dWjj26sLUZ-HFxLtqHyvhZehBnwAczIEQ==)
13. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMCbkgxnj4vviYBoVFZ_M6lKpYlwEvr3JYQeJzSbsQViU-HXmZvZA3V1G-_whe3DbY2pA-kqsj6dO5AE-Jwbh4qCB4kkRyxUqCS0V6gSuAbRrh89A8Ief20jywXIYE7-fXdL57X1SKAHF-yEOywETVVIE3TeWs4lk_sERt_-utsSuwYzmu1h0nPcDpJbQKvlyfBHOYpfuCXA==)
14. [powerdrill.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCQzib8k6zZ5gfuMXRpmVEhEQ32GF1MSS5Tu7OzDa6T3-XBz3Dy5mRCqaBoHx3H2n4JATG8MtuA7MNzbx6mu1xgO7e-2DLPZe7CoQW2iUtesndtWsz6Cbs5AVcEZ1MK_lr7Zmm9VMFDpEkyoMwNShGxLVQGWiSHDFJ5Oy4IGE-pAQez5GgclHurIlCAFEl5w==)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwqwrOS6Ri1IlOqV_EAX-kt_bM4-QN0mgDKhGgnOe3uGB9S5aOGAu8e8hZoGe-HZsmY5sVirVu0jxT-qGEqmhnCMKI3f_JGSQ_BjNeMPAzE5GoYCC3uotbNA==)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6YvI6W0bpUrFvgNwP2GnhkGMxNifmt3Pa-nZPzd-T7wwUWXC7MGdGTOOF89oNaRs25gTf-qIfwSnSRd8gbiHZHDTAzOPiLudbFM3f97T16a_UmBZNPSnUyw==)
17. [seg.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5vEWlpHMZUdvarlutUCBEjAzNPY_pPGN73svqp7bA1OSkAE2n9DYOgMHaSyQj9DPsVdf1HpMrivBTuHcnwV3xUgzgMtVVOKpsvBR4E4m54gIGlmHfovxfH54V33A7f0tkOYETcIvifg==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1TLjSqIqbfHg8hZub08evTSRfAHvfSLPa9QtMJECd2vrOpRZUsJx4ZTxY_P2PW0Cyu3ytsweabZOto-UzvMY6FmS-GL1lpCnUL8fh8ZsXV-1s9TibLg==)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4VEbzQPc9Jioxe098ASP9ST07euQptF4sR1NLZKPOy4_pHDLiiMYGH-rM36OZP2PB9Pwcj9nw0xqBolb5RfZI0E4pkTk9z8hu0H4v3OigQW_FULP6eeDVyJ7dn2co_w==)
20. [ascelibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEGx6915KKVNO0Jz2AQtMIIfDxJnVy8nfu6jejThHEtbMcDbnwW_LQpXRs-JU_VteYhraQ42PxcIq9Aoy26kIBN9rdPsmACUa_SEqoWKm-tQTC1p93d64qAP1x0JaTNLUseAgIQLICFHPopw==)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZRbQCbG_myMyfesb7lSgwVlHI-Od15Ca0LK-tW9jP1xcyerZYW3LwMIhXlXNIfzmP_-fLTI5tMLfLQO1DUf_GkKTdA1ygEcOl8VsD_RpmwcCjjQwOtST_7bLVCOQ=)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbYH_16BGfEnzU8-Szd_8nE_E_7YcQ5YcZ-yzU5nBS6a7ky4IclT3oGepJHjXztFlJBBqRn0dNOqN1XujV4mVnOljZf_JwusZPM8ziYawZpUqJ2nk-BaQ6-sOF3KQMPByCeIVKLYYpcXwyt9En8Ww5AJ7gI8SMOVU8ShDalJQqHBSbceYuucgexknSoUpGThUFD9I2VuXFuKc2APM40MlfRGP5JFZdqeBIeKAxXQLcOvZ2Aqw=)
23. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxV-He2ybHc4Bcvy5peWX2RBGUGqKz02kexayJyVxtfjiMAgZwupSRRDIXxalNR-Q7-iNvBa8vnRbMBefa5NYWou6aiFRJ72ahHDxxJVoCJs0oURESgnjPwwOUWlNRiTE=)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgK802QZ3F37QlrLoLxCReeKROUbEmTJCgfFrV3Q6Bl8MIvbNwYxGxIKN2lNECcJXuZ3OmT0JyD5ro2Lr7JvlXnVhs4P8rJZLk-RSUha8rjpdyn9EtZ5nvpKEGmzvKCA==)
25. [donghunlee.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgKTelK_7XRtbRgPflmwR0xSZ8WCZI4ew1Rb9MQNkCXetysEIU9OjwLTTIxMnIZ1IB41wCrX9q7ZvaQBe_F92ruGVxO3PdhzLzUTrdleWRzNM2k3aMUWLQenjcnnjiU4wXhfTx)
26. [themoonlight.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeRLlO2Z_7-ExbxujzoEbzV2ZPKol3Hbs2UfHWY3NhqPykPGLVCe7cHCQ1sns75-9r7THLuo24-nYrnQR5b6FLCacaJoFVtmqzOoeUbY1jN5R9qi6P2-ECUi56cVnAqD5kzJjhY8PBo6WM7yvC67iCvt7PZSSLovkbQumYFpq1gwhytO82tDUe-tAp)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwb9IkK5QKhA-Kv-1ZKnBOpfhc1a7YMtCGg-xKZb63PGBfvi49fd_93FNGt3RTgpnmmduMQvAgo3R9jBvwq5VmbgEbhjmALO2nf96OendcqRAchZyAVA==)
28. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkmLwCib8JBdiqvXsaMcR7WxyGF-GFASwFf-DxB6MraPnPnumWka1GvzHWmZXq2zovoNrjCR97BdRUh28UBmLXwXLOslijCxp-WW5x82JVhm46o1ieepK3PsjhR3xoYCsYIFy3D0usvgQ=)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-wIU9EvZsna3cn_2twUOdIvQ-mo8ioNsaatHiQudGJTVwN-IftF4QDUxlVGSfzLeYfAwd245iBUZSuuqsNJsKbwQTC7gwxROg7PWx1R_4_4goAWC0_AmGHg==)
30. [journalijsra.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW507lvtXN-YiAlwdL9IZpsDC688OPlimBk3IIWrK-DwzT1Qp4p1vLLUXF9SOWqns_ry3biix4ruAKFtfR9DX1ED0gQ4-ZzOyEBLc3GhhxF2S93cuswwIGu1hKlf2KN-2wB50Ax3RuTxBk_SJpXgYw45dRyUcOUV_cNRlFgbc0PJMnQA==)
31. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1r8cNw2jI4pXN7KGUN0blKJChaDokkWaOkooxOUG5e7kBotiz7jEikMAL_Y38BQbUuGVx7Fhx3vw0BFh_MkWxcrUqq1aoh1qaOl4u5s0ncapZMEyFNrfj162I1lsOCIah-VB-)
32. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYdjHaEOWK6hXRxYHQRHjKITdGDdbPaXT3OzssTp3F2iQZ8qanFQe9dt1w2L7JGIIDP6SLq1yBIJ6LjKbN2-EH6UWEwPgmUqCYI4cgyr-feW-APp0NVVDxGodn)
33. [confex.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUhWrW3cDat6E_7UPKiFoEVHXnAVME3STY-aBv79zOcrhvrSZWPgFmAqK3fBIpFs005uq-YlDsoV8ESitZ76j4h_43wlXP6IO0ubEuYsRpbbALmPwKEv6R9KZ8M7YuRhNALlK9PD9qw-zpaM41eiKrkOoW)
34. [eucentre.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZrOG-_XFe-1kLB2Ont1n0sBQoQHrS6L874KwCQEgRGJSWMBR3A5JyMf1aKbZ1j0eNhLsb58pTBbES-ozZTgH7KrqIQbYiH6xxl8jkJwPQ483tA4bY7uTVsKO14X8FR7KWJG7XubXQecXmMEqNZBclctKAPhJ1lc2BxaVS6FH1rPxeGaiwKmwrGhZCPk3I8GS_1vgwhgxzB8WNL-i86g==)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnqP7okdMSM3R9QH1rJGR4PSjT5bx-8BsGRC3PEjBXT5PQWpQW6QkzE_LBWm0swZKB8_RmY-m_T_LIs-gWpEVzqFJFq1ynggXaTuEEFHkPmApG-HfQfppC34mLFns=)
36. [rcaap.pt](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsgpCeS5d7cqJ8wM2IMZTOx1l5C5WExIGlvCTRdUrZKP2M9IlEKKkQUdFpSXt51JAIamWdJfxqLdz7Dq6pponBqhEvPd9w_OI_JDDu5oowVtBeOFPhvH2aifgpRvNtQR4fIFoaL36KcPJ1qz4=)
37. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECk1-wXjmpwVt14yqVNgnV5Nz1-XJot3MO5xoAgFbmvDdFQL-lTRZwrrQyUCrr_y3GLVwGWnquM4-OLEo3UhcFrtxxtbwg8Wu4_MD-tR0o-MIuxSnFzQ==)
38. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh279zuwo-scWtRTyCzJw_FgHywyMJJjhpZvHSUWKG_FukCJGhDoqIJ-wVZoY-BNgv8N_tGcFdAKBn4mS0KJj8c7RyNLkCOk-fYsyW6SZmaasJTXmFBra478MIOUBzy8-XmaOLxRZRCdDTivdxooD5mIu0qqqpXwQxi3Xb6qh0vHmkMEwbG4rYkEUYI-Z4cLUaOKhN2UPo4h092UHrbOQN1Lu3xCRO1DNInxAuphS66GoJmLeV-Unh0y9uDHBow7bnddk=)
39. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2tN6lDDtI2im_r_A3dWGlBoLD8J-hR8Qo2rvQMhMcfOCLgZc8gB5AogBbbh5nHdW-IzUH3ozqbz-OHtwqsT2CgPGP3EPfAEK0XVLa4_vbjcDEOVPDYJlFwmJTJ0Kte-EmHOAtY01UEI8kt5Q6NAPyubXhUCjQoXc=)
40. [psu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6vHXgqAl9ApeotNk2b22tPfMAL2aezOCajUSEDfZprE3NlO77k22rI16rtyxWovWwEuP0g6ej8LGwCMsxAa783cByNU3ojQiJxsiHDmm92zV1_rW3w0RlVqo9pQB-v5zQCn-65ebJ_61fYCedINNoXpZ-Q0K4KyQkE25yASbFbvrCyASICbkM4iO3pmqsrnRAbQ1dZRpsZQ7yGXRT)
41. [nips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqp0iWaew9SpFks3ON6JeZdjnGjQL4GrQyBpyfBO6jLvdexhnYg3nm1tULqQY8v-MqEzdpW4g3DXNR3W1CKPPiB3Ox_MUZCMNrdMg-ITckDEsFdqlMv9tcgHLgqC_egBk7EEbo-LNud5eSZk8CMXZCtCkTMoLqw2WEJq565Uc-r6GVqqxMh1JAKFxPYaIyaaChSWlYd4rgcnmZ7bOKLQ==)
42. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLZ4eu1iMTtSUV462lrVLPza8tlXC0wGhVh1WGOAG5OThXoBiQkXcIp1vqpy7XBYPkDcCNnVc8L21rQf6UjjOO62uEMP6jrZcrxhCvzBixTQOXgCMgM9UJ0cpPLstn49jZYTRmHllzcYsGMfYTRUgbqnoPTvLoi1hQ8ms1fXkQTJgiiRUTVHokbnWar6-y)
43. [icml.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGajAm8Qcvz_NebX9W5vBzkCgBzWntYfg08OTqqqZalPGHAX7A2mTyfEpcsUc9_Pg7XM-ApQmConWuWqYxseXzd-kRHGWf40jn4sFMQp9acy2sJS0mj3Ocu)
44. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMSF0WwiT_EtooLsa8amlSxe1WdnfS0mXTBQAAZolEXkSL_X5ls7Sl5dSks6PMhWKDtRjLSD9oUQY4ZqoISIU8EGa1FU_mvi98Cv60QW3HpBBUBS4CWam4SQcUyr44bqo3p1XonJtHE9LFOp9v0Ha80GKc3ikc48CVYtsco7obe21OL1SqoENstwgy2-cw6cukF5jhvMSTRYT)
