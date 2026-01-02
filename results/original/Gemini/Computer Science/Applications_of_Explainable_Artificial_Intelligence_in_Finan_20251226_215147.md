# Literature Review: Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature.

*Generated on: 2025-12-26 21:51:47*
*Progress: [34/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Applications_of_Explainable_Artificial_Intelligence_in_Finan_20251226_215147.md*
---

# Applications of Explainable Artificial Intelligence in Finance: A Systematic Review of Finance, Information Systems, and Computer Science Literature

**Key Points**
*   **Interdisciplinary Convergence:** The review synthesizes literature from Finance (domain application), Computer Science (algorithmic development), and Information Systems (user trust and adoption), highlighting that successful XAI implementation requires a tripartite approach.
*   **Dominance of Post-Hoc Methods:** The field is currently dominated by post-hoc explainability techniques, specifically SHAP (Shapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations), particularly in credit risk and fraud detection.
*   **Regulatory Pressure:** The European Union’s AI Act and GDPR’s "Right to Explanation" are the primary drivers accelerating XAI research, shifting focus from purely predictive accuracy to model auditability and fairness.
*   **The Fidelity-Interpretability Trade-off:** A persistent challenge remains the trade-off between model accuracy (fidelity) and the simplicity of the explanation (interpretability), with deep learning models in algorithmic trading presenting the most significant "black box" challenges.
*   **Emerging Frontiers:** Future research is pivoting toward Causal AI to move beyond correlation, and the integration of Generative AI (GenAI) to provide natural language explanations for complex financial decisions.

---

## Abstract

The rapid integration of Artificial Intelligence (AI) into the financial sector has unlocked unprecedented predictive capabilities but has simultaneously introduced significant risks regarding opacity, bias, and lack of accountability. This "black box" problem has necessitated the rise of Explainable Artificial Intelligence (XAI). This paper presents a comprehensive systematic literature review of XAI applications in finance, synthesizing findings from Finance, Information Systems (IS), and Computer Science (CS) disciplines. We analyze the historical evolution of the field, the current state-of-the-art methods (such as SHAP and LIME), and key application areas including credit scoring, fraud detection, and algorithmic trading. Furthermore, we critically examine the regulatory landscape, particularly the impact of the EU AI Act and GDPR, and the socio-technical challenges of user trust. The review identifies a critical gap in causal inference and the under-utilization of XAI in anti-money laundering (AML). We conclude by outlining a research agenda that bridges the gap between algorithmic transparency and human-centric decision-making.

## 1. Introduction

### 1.1 Research Motivation
The financial services industry is currently undergoing a paradigm shift driven by digitalization and the adoption of advanced machine learning (ML) and deep learning (DL) techniques [cite: 1, 2]. These technologies offer superior performance in tasks such as credit scoring, fraud detection, and market forecasting compared to traditional statistical methods. However, the complexity of these models—often referred to as "black boxes"—obscures the internal logic behind their predictions [cite: 3, 4].

In highly regulated domains like finance, the inability to explain a decision is a critical failure point. Stakeholders, including regulators, loan officers, and customers, require transparency to ensure fairness, accountability, and compliance [cite: 1, 5]. This tension between predictive performance and interpretability has given rise to the field of Explainable Artificial Intelligence (XAI). While Computer Science literature focuses on the development of explanation algorithms, and Finance literature focuses on domain-specific accuracy, Information Systems (IS) literature addresses the crucial aspect of user acceptance and trust [cite: 6, 7].

### 1.2 Objectives and Scope
This paper aims to aggregate scattered knowledge across these three disciplines to provide a holistic view of XAI in finance. Building upon prior systematic reviews, such as those by Weber et al. (2024) and Černevičienė & Kabašinskas (2024), this review addresses the following objectives:
1.  To define and categorize key XAI concepts relevant to financial applications.
2.  To map the historical development and milestones of AI in finance leading to the XAI necessity.
3.  To evaluate state-of-the-art XAI methods and their specific utility in financial tasks.
4.  To identify regulatory, technical, and adoption challenges, including the impact of the EU AI Act.
5.  To propose future research directions, including Causal AI and Generative AI integration.

## 2. Key Concepts and Definitions

To navigate the literature, it is essential to distinguish between related but distinct terms often used interchangeably in the field.

### 2.1 Interpretability vs. Explainability
While often conflated, **interpretability** refers to the degree to which a human can understand the cause of a decision *intrinsically*. Models like linear regression and decision trees are considered inherently interpretable (or "white-box") because their internal mechanics are transparent [cite: 3, 8].

**Explainability**, in contrast, typically refers to post-hoc methods applied to complex "black-box" models (like Deep Neural Networks or Random Forests) to approximate or visualize their decision-making process in human-understandable terms [cite: 8, 9]. XAI seeks to bridge the cognitive gap between the mathematical operations of the model and the reasoning required by human users [cite: 6].

### 2.2 Taxonomy of XAI Methods
The literature categorizes XAI methods based on their scope and applicability:
*   **Model-Agnostic vs. Model-Specific:** Model-agnostic methods (e.g., SHAP, LIME) can be applied to any machine learning algorithm, whereas model-specific methods are tailored to specific architectures (e.g., attention mechanisms in neural networks) [cite: 4, 10].
*   **Global vs. Local Explainability:** Global explainability aims to understand the model's behavior across the entire dataset (e.g., feature importance rankings), while local explainability focuses on justifying a specific prediction for a single instance (e.g., why *this* specific loan application was rejected) [cite: 11, 12].

## 3. Historical Development and Milestones

The evolution of AI in finance can be traced through distinct eras, each characterized by increasing complexity and a subsequent need for explainability.

### 3.1 Pre-2000s: Rule-Based and Expert Systems
In the 1970s and 80s, financial AI was dominated by expert systems and rule-based algorithms. These systems were inherently explainable as they relied on "if-then" logic programmed by humans [cite: 13, 14]. The birth of algorithmic trading in the 1970s and the rise of neural networks in the 1980s marked the beginning of automated decision-making, though early neural networks were limited by computational power [cite: 15].

### 3.2 2000s-2010s: The Rise of Machine Learning
The 2000s saw the proliferation of statistical learning and data science. High-frequency trading (HFT) took off, and credit scoring began shifting from simple scorecards to more complex ML algorithms [cite: 14, 15]. During this period, the focus was primarily on predictive accuracy, with less emphasis on transparency.

### 3.3 2016-Present: The "Black Box" Crisis and the Rise of XAI
The widespread adoption of Deep Learning (DL) and ensemble methods (e.g., XGBoost) in the mid-2010s created a "black box" crisis. Models became too complex for human comprehension, clashing with emerging regulations.
*   **2016:** The introduction of LIME (Local Interpretable Model-agnostic Explanations) provided a breakthrough in explaining individual predictions [cite: 11, 13].
*   **2017:** The introduction of SHAP (SHapley Additive exPlanations) unified game-theoretic approaches to feature attribution [cite: 10, 16].
*   **2018:** The implementation of GDPR in Europe introduced the concept of a "Right to Explanation," legally mandating transparency for automated decisions [cite: 17, 18].
*   **2023-2025:** The emergence of Generative AI (GenAI) and the EU AI Act has pushed XAI toward "agentic" workflows and natural language explanations [cite: 19, 20].

## 4. Current State-of-the-Art Methods and Techniques

The literature reveals a heavy reliance on a few dominant post-hoc methods, though intrinsic methods remain relevant for high-stakes compliance.

### 4.1 Feature Attribution Methods
*   **SHAP (Shapley Additive exPlanations):** SHAP is the most widely cited method in financial literature [cite: 10, 16, 21]. It assigns a value to each feature representing its contribution to the prediction, based on cooperative game theory. Its popularity stems from its solid theoretical foundation and ability to provide both local and global explanations.
*   **LIME (Local Interpretable Model-agnostic Explanations):** LIME approximates a complex model locally with a simple linear model to explain individual predictions. It is frequently used in fraud detection and credit scoring to explain specific rejections [cite: 22, 23].

### 4.2 Visual Explanations
Visualization techniques are critical for the Information Systems aspect of XAI, aiding user trust.
*   **Partial Dependence Plots (PDP):** Used to visualize the marginal effect of one or two features on the predicted outcome [cite: 24].
*   **Accumulated Local Effects (ALE):** An improvement over PDP that handles correlated features better, which is common in financial data [cite: 4].

### 4.3 Counterfactual Explanations
Counterfactuals are gaining traction in finance because they provide actionable feedback (e.g., "If your income were $5,000 higher, your loan would have been approved") [cite: 4, 25]. This aligns closely with GDPR requirements for providing meaningful information to data subjects [cite: 26].

### 4.4 Intrinsic and Hybrid Models
Despite the popularity of post-hoc methods, some researchers advocate for "inherently interpretable" models (e.g., Generalized Additive Models or GAMs) for high-stakes decisions to avoid the "fidelity-interpretability" trade-off [cite: 21, 27]. Hybrid frameworks that combine deep learning performance with rule-based logic are also emerging [cite: 28].

## 5. Applications and Case Studies

The application of XAI in finance is unevenly distributed, with credit risk and fraud detection being the most mature areas.

### 5.1 Credit Risk Management and Scoring
Credit scoring is the most researched application domain for XAI [cite: 1, 16]. Traditional logistic regression models are being replaced by XGBoost and Neural Networks to capture non-linear borrower behaviors.
*   **Application:** Lenders use SHAP values to explain why a specific applicant was assigned a high-risk score, satisfying regulatory requirements like the US Equal Credit Opportunity Act (ECOA) and GDPR [cite: 19, 29].
*   **Impact:** XAI allows for the inclusion of "alternative data" (e.g., utility payments) while maintaining the ability to audit for bias against protected groups [cite: 19].

### 5.2 Fraud Detection and Anti-Money Laundering (AML)
Fraud detection involves identifying anomalies in vast datasets.
*   **Challenge:** Standard ML models often produce false positives, blocking legitimate transactions.
*   **XAI Solution:** Methods like LIME help analysts understand *why* a transaction was flagged (e.g., unusual location combined with high value), allowing for faster manual review and improved trust in the system [cite: 23, 30].
*   **Gap:** While fraud is well-researched, AML remains understudied in the XAI context, despite high regulatory burdens [cite: 1, 31].

### 5.3 Algorithmic Trading and Investment
In investment, XAI is used to decode the signals generated by "quant" models.
*   **Stock Prediction:** Researchers use XAI to identify which macroeconomic indicators or sentiment signals (from NLP) are driving market predictions [cite: 3, 16].
*   **Portfolio Optimization:** XAI helps portfolio managers understand the risk factors allocated by AI, moving beyond simple correlation matrices to deeper causal understandings [cite: 1, 32].

### 5.4 Financial Distress and Bankruptcy Prediction
XAI is employed to predict corporate bankruptcy by analyzing financial statements. Unlike traditional Altman Z-scores, AI models can digest unstructured data (news, reports), and XAI tools visualize which specific financial ratios or news sentiments triggered a distress warning [cite: 33].

## 6. Challenges and Open Problems

Despite progress, the integration of XAI in finance faces significant socio-technical and regulatory hurdles.

### 6.1 The Fidelity-Interpretability Trade-off
A central tension exists between model accuracy (fidelity) and explainability. Complex models (e.g., Deep Neural Networks) generally offer higher accuracy but lower interpretability. Simplifying these models for explanation can result in a loss of fidelity, where the explanation no longer accurately represents the model's behavior [cite: 27, 28]. This is a critical risk in finance, where an incorrect explanation for a trading decision or loan denial can lead to liability.

### 6.2 Regulatory Compliance and the "Right to Explanation"
The regulatory landscape is becoming increasingly stringent.
*   **GDPR (General Data Protection Regulation):** Articles 13-15 and 22 create a "Right to Explanation" for automated decisions. However, legal ambiguity remains regarding whether this requires a technical explanation of the algorithm or a justification of the outcome [cite: 17, 20].
*   **EU AI Act:** Article 86 explicitly requires "clear and meaningful explanations" for high-risk AI systems (which include credit scoring and life insurance) [cite: 20, 34]. This moves compliance from a "nice-to-have" to a mandatory operational requirement.

### 6.3 User Trust and Human-Computer Interaction (HCI)
From an Information Systems perspective, the mere existence of an explanation does not guarantee trust. The "Trust Paradox" suggests that users may over-rely on explanations (automation bias) or distrust them if they are too technical [cite: 4, 35]. Research indicates that user characteristics (expertise, cognitive style) significantly influence how explanations are perceived, yet user-centric evaluation of XAI tools remains limited [cite: 7, 36].

### 6.4 Technical Limitations of Post-Hoc Methods
Post-hoc methods like SHAP and LIME have limitations. They can be computationally expensive and, crucially, can be unstable—meaning slight changes in input data can lead to vastly different explanations, undermining trust [cite: 27, 37].

## 7. Future Research Directions

The literature points toward several emerging frontiers that address current limitations.

### 7.1 Causal Artificial Intelligence
Current ML models in finance are largely correlation-based. Future research is pivoting toward **Causal AI**, which seeks to understand cause-and-effect relationships (e.g., "Did the interest rate hike *cause* the market drop, or was it a coincidence?") [cite: 38, 39]. Causal inference techniques, such as synthetic controls and structural equation modeling, are being integrated with AI to provide more robust investment strategies [cite: 40, 41].

### 7.2 Generative AI and Natural Language Explanations
The rise of Large Language Models (LLMs) offers a new avenue for XAI. Instead of static charts, **Generative AI** can provide natural language explanations for financial decisions (e.g., a chatbot explaining a mortgage denial and suggesting remediation steps) [cite: 19]. This "Agentic" approach aligns with the need for human-centric financial services [cite: 42].

### 7.3 Human-in-the-Loop (HITL) Orchestration
Future systems will likely move toward "AI Orchestration," where humans and AI work in tandem. Research is needed on designing interfaces that effectively keep humans in the loop, allowing loan officers or traders to override AI decisions based on XAI insights without succumbing to automation bias [cite: 43, 44].

### 7.4 Standardization of Evaluation Metrics
There is a lack of standardized metrics to evaluate the quality of explanations in finance. Future work must develop benchmarks to assess XAI tools not just on computational efficiency, but on user comprehension, trust, and regulatory compliance [cite: 4, 45].

## 8. Conclusion

This systematic review highlights that Explainable AI has transitioned from a theoretical niche to a critical operational requirement in the financial sector. The convergence of high-performance "black box" algorithms with stringent regulations like the EU AI Act has made XAI indispensable.

While methods like SHAP and LIME have become industry standards for credit risk and fraud detection, significant challenges remain regarding the fidelity-interpretability trade-off and the stability of explanations. The literature suggests a future trajectory moving away from purely correlational, post-hoc explanations toward **Causal AI** and **Generative AI** interfaces that offer intuitive, dialogue-based transparency.

For researchers in Computer Science, the challenge lies in developing more stable and causal explanation methods. For Finance scholars, the focus must be on applying these tools to understudied areas like AML and systemic risk. Finally, for Information Systems researchers, the priority is to design user-centric interfaces that foster genuine trust and facilitate effective Human-AI collaboration. As finance becomes increasingly algorithmic, XAI will serve as the essential bridge ensuring that these systems remain fair, accountable, and intelligible to the humans they serve.

## References

[cite: 1] Weber, P., Carl, K. V., & Hinz, O. (2024). Applications of Explainable Artificial Intelligence in Finance—a systematic review of Finance, Information Systems, and Computer Science literature. *Management Review Quarterly*, 74(2), 867–907. [cite: 1, 46]
[cite: 46] Černevičienė, J., & Kabašinskas, A. (2024). Explainable artificial intelligence (XAI) in finance: a systematic literature review. *Artificial Intelligence Review*, 57(8). [cite: 16, 47]
[cite: 16] Wilson, T. (2025). Explainable Artificial Intelligence (XAI) in Finance: A Systematic Literature Review. *Artificial Intelligence Review*. [cite: 11]
[cite: 11] Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why Should I Trust You?": Explaining the Predictions of Any Classifier. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. [cite: 1, 11]
[cite: 21] Kumar, S., et al. (2025). Systematic Literature Review On Explainable AI In Finance: Methods, Applications And Research Gaps. [cite: 21]
[cite: 48] Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*. [cite: 49]
[cite: 50] European Commission. (2024). Artificial Intelligence Act (Regulation (EU) 2024/1689). [cite: 20]
[cite: 51] Goodman, B., & Flaxman, S. (2017). European Union regulations on algorithmic decision-making and a "right to explanation". *AI Magazine*. [cite: 48]
[cite: 9] Arrieta, A. B., et al. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion*. [cite: 9, 48]
[cite: 2] Cao, L. (2022). AI in Finance: Challenges, Techniques, and Opportunities. *ACM Computing Surveys*. [cite: 1]
[cite: 8] Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*. [cite: 6]
[cite: 52] Gramegna, A., & Giudici, P. (2021). SHAP and LIME: an evaluation of discriminative power in credit risk. *Frontiers in Artificial Intelligence*. [cite: 32, 37]
[cite: 31] Bracke, P., et al. (2019). Machine learning explainability in finance: an application to default risk analysis. *Bank of England working papers*. [cite: 33]
[cite: 53] Bussmann, N., et al. (2020). Explainable AI in Fintech Risk Management. *International Journal of Production Economics*. [cite: 22]
[cite: 13] Gunning, D., & Aha, D. (2019). DARPA’s Explainable Artificial Intelligence (XAI) Program. *AI Magazine*. [cite: 9, 11]
[cite: 54] Wachter, S., Mittelstadt, B., & Russell, C. (2017). Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR. *Harvard Journal of Law & Technology*. [cite: 4]
[cite: 55] Pearl, J. (2009). *Causality*. Cambridge University Press. [cite: 39]
[cite: 15] Permutable AI. (2024). AI in financial markets: 7 key milestones. [cite: 15]
[cite: 56] Taktile. (2025). From credit scoring to GenAI: How modern credit decision-making has evolved. [cite: 19]
[cite: 57] Alphanome. (2023). Causal Inference in Finance and Investing: Moving Beyond Correlation. [cite: 38]
[cite: 58] Hoofnagle, C. J. (2013). The Federal Trade Commission's Inner Privacy. [cite: 1]
[cite: 3] Yeo, W. J., et al. (2023). A Comprehensive Review on Financial Explainable AI. *arXiv preprint arXiv:2309.11960*. [cite: 58]
[cite: 33] Misheva, B. H., et al. (2021). Explainable AI in Credit Risk Management. *arXiv preprint*. [cite: 33]
[cite: 38] Selbst, A. D., & Powles, J. (2017). Meaningful Information and the Right to Explanation. *International Data Privacy Law*. [cite: 17]
[cite: 43] Shin, D. (2021). The effects of explainability and causability on perception, trust, and adoption of explainable artificial intelligence. *International Journal of Human-Computer Studies*. [cite: 59]
[cite: 39] Kostopoulos, G., et al. (2024). Explainable Artificial Intelligence (XAI) transformation in Decision Support Systems. [cite: 60]
[cite: 61] DNV. (2024). A Systematic Literature Review of User Trust in AI-Enabled Systems: An HCI Perspective. [cite: 7]
[cite: 62] Fritz-Morgenthal, S., et al. (2022). Financial Risk Management and Explainable AI. [cite: 8]
[cite: 30] Mhlanga, D. (2020). Industry 4.0 in Finance: The Impact of Artificial Intelligence (AI) on Digital Financial Inclusion. [cite: 63]
[cite: 22] Demertzis, K., et al. (2023). Blockchained smart contracts in the supply chain. [cite: 23]

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ5yHqIm3MX6TynyU6LBhJJyjc6evSQXOgLCIJH2NPgjiKvaopqH-7YeKqeI4gTrU1gbCmVgxaucXvetKANS5T4X7DhNzfXf43x94syJTP9ecfds76o4K3BEtWa-CB4im6J6bfyDCit2ZuDUyMN6ULBWQzv3B70mkJOKpj9Y81cUN0NmlINDB4_L9kAnb3u0M2c0JlR3hb9Acd_l4zSrb6G7X8nBXl1SlVvXlJ_15cG8wL-TDaC6wnQngm7UTqCqXhbKymDnFK7kZxkM8G1McfXo_i0u1Ehm8e6pX_mrQASGQjqiND3LtbWfiiONpJ1Hw-OAJYYPZFOjPmWQ==)
2. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgkzJ3Rq0ARqymjSzdwIRfwOUqVvHWegZdNaJT4ljmZiPnk7h5RciXSpoCU21xvKulP_LDjwhtb7pRXcWEOFWmjSdRN5hJfJO7bGfggATA53BILNxQAQ24yqfu5z-JSa1vYIrPQDr2qGmCCr7csKfDA4GvaloPX-2yNWMo-L4HyQbE3RG1)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhU5aWUc8_lzyqLtXTjlLEDwAnlw_2QBFISYt1HQObjxLf2WLHtb59ogpYxf8RwO3UXb8VvbNSPt87GKj47UZP06WSK0kK8tlzAAOlyhk62cq654n5Zf659EL9ztPFtFMEKqnTGW5yFctdTu-_0BfKbIA99vqhOHGlPK1bB312460OJfmjBkWzfb2R1AK3ySAGmD1_HifKIeXLuPAn8w2Qw99SViGwjq_BYUKHDax8GwmvCoypBz2zDB_0tqqrIl0tCQ==)
4. [cfainstitute.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD5TjwFgTCaKWfn-yTNeWAGO9YMWD-vRq-Lt05b-BnJa9si8meD1P1bqVRWUjBfGI5ztH52EGuQVTZke61jU93nhDxLqW9mdFGJxVX246iyDCCYfaNSmf-l6rSCzAPJcC_qCXXTkfNgfIQHf2eN11tVnqF_Lrxx1P6yqZ1tREkqaFJ)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEpsmElHVNuDmLxG0EuALYFBS3Khv5IxeFokZCCirAE6-CUugENaoaGjCi6XXgS2tlcnI2U1V4WZoVQpk5-SvPesWx02Vq61q1i-cIGh4Sy2XMZ4hMqfj4buWmF-T6S2VR5wr7ClQF5jPSbCv00xSRRDmuF-r3BoaXktlDX7JPx0Oo19qJmQPK2aRLAn343H3QsFjFLGJj586cFLsZtgLzYTyHX5s_Www4mrH4BR5gLwl41ikDyb7yJ1_C)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE08fbFvUReILntc9IW-jsZvcEzc7N85xbyQvUAgh0cml4rCQLUs5tg4issH9C0OcDM1jFQ5D55mT9FqL8pJSpHpRPJZdOMwCWdHr0gv6qItyhcQzeQi5FQpP4DD_fM_miPbZZ10ABDLmUMoyhmZnFNUvuh2HMY77qhSW0uTkFtGuZYT7qQEw3_OrSnwxGeOloZWVzIoQzvgp1bNEZNW1XhevrK_dJ5HHSMJ7yb5O1EeSHj0dXk3ed581pT)
7. [dnv.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmorYDVgHPLG8nb9IoPgLXG1dRJMngJk19y38GyZYH8iqUyQLSlNNgAK30SyFKzTs8Ye7tmQ9DasR0-XpN_iXxlCmIoUXYPsdVoi3SpWJHvWfL-U1eoHTbYk12Mq8qxXinH5bKsynVnA2JHZogwmWilPxIBkNu8Ib1LNfty-9cQddZW0JWbdvy5_E4l7w575j14JqohhUFGaRdT_8ZiwOCvV3VUyHbfhefr6bKN1h7Hq0gWMc=)
8. [sentic.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLldqPJY_GbPWAhW-YaiGw7txSKEZIAa8gquFqknNPP6OEKeenOeLg8LSO9BTSzMXjWTRPjly9UwSkqbHKoHedksQZztW_xMfw4utNKYtwVQ6BTb2FdMTqFjYkhtcUnvud05yChoeZFsfgJJc1bQ==)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFutrD3mfHaV_aPt4gKCJd-APH1_jYQOMDEbj-CIjos6b97-PTMeDSEaDbI7OtP87KQ7zw1d_0dGtoAGdARehX9v-LLb7oWov4b1bytFm8C4HRgi6uVHQ==)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE19Kh-UWAJOCB_2VfuTjSs7zcd3iiJbUwtRWqVC1EH-ocb40YVlfIAFNzQJybBWbpxKPhECIGRetEYpC8IDxkVJTluOjou5BkRd4v7MY6riVN_8VelMrFFCaTYjeju)
11. [cfainstitute.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFStUSyWSbYqCwdhq5jVOozBYth61blN30l_6PNmymLgsAgduqXdMdvvInbbMuYU1rpMvS0hYu2ZLZciZyd2-Al0KcXvzoRDpnFAuCil-uhKU_AoVwpm_7_Ssidy-hiWnkh7oqVl2TrsfB0uBzs4kbBjLxiqX3k1FNpFaYunaN9rxW2snUVvO_-jIzASpkdsvXQZSbslqbOW2TpBZypPNfIoksda3o=)
12. [mab-online.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELX65qTrYbLi2Lg69ctzf_Cn6rhXpAxBgBmYrW8ajbqGvnf2XBAARpHro_skGaPSD7KmCfErRQqaHIL4RkVMooMNtDHPoQaxhuqDC2czaViBeFzlMB6XREipBp)
13. [digitaldefynd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO2gOZo0PjfRf42gGop8_2mWFw6Jrzq52ynKHv9sn5VBxQA_Taj7Z7jS3NC4xfiGBwu1ixLL5wH7NqWAz8TDmCj3YYYCz6wRDBj7uVemnA1dsyKyUHBIqxBdIDHN02w4xSommxCNawmhWXhgGgxeq9ZeSA)
14. [loanworks.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbaQRquM_MH3lu2LOm0iSSclbKn96tm9xewgFKbG-ZBLYztbUTAPl3vUZsc4QE8R0kWifzTXVJBsymPRdU7CdfbdQiLgXpZApzxR0rurUSBaP4LFav2xds8Dzx8nS8rfU9vcIdJmEL-L-nxT8xhOJ41G-XXprLNkA9ZeMAmll1ZrNs2sy9rZSFXEv29_0=)
15. [permutable.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxs1Q_OKFkV9UoCfUm88pqCasqpiZ3k4cWRuDlOxA88YPDqJf2HBcsPKJXC7nyBH3O5GtFihyT1wMmGdMlFAW6bpYX3bVQlo9sG97ds_SI6F_4YY3cfoGNDWvlJ0KtyTOpzoSM6ifvJBdTOQc_tg==)
16. [dntb.gov.ua](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9oryKv_1UOtDqDJ2qw46-8EJrIlN5O2inAebC7wqYgJDHVNOu5RKYn_No2mXUgF1k48lVZwnFr4GtMpCQ5MDtaL1T1Py8jlSFLEJm_NUSD83vea0MWvzqgoVGb7viEWbm)
17. [fpf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHKNfCAalZuE7FPXxOFxtIFOWDDFdo8bfOuUCo9IMkXj7LqwcVXqr_mNkQYsx9KEpO6xsqGGHAdviaNfmXC72-rZpy1WK-iRIUlpbIsyMMCix_ZxCgTOJYPstfEX8gxhaCXHbKPnNMbHJ4YVBBbSyY8AGBNLWjJuybJbmWvolnP_h0KGozbT2TZszKEjk-CYM0bIefDVOixRF5iH_d-g==)
18. [exabeam.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2D3gCJGrEL-HewcCIgxj2zkLJrZyB9itSa0ihwkn4CAW32Uo5a8wYTpp0bBjCWTrCyPjlLSaMtmwwCbrlRp7HcmoCK1EOR3iJSYZQ-8C1gKzMlrkeis4JtYWkiY_JFi3b6L348SM9KLA3k3I9NPPZRxKD0xSjn9P65jGeEbtCVOO_-lMUj4qWXXXDCQgzslWwkMYfa4KtcPJEsHV7jb0yv69abwTKvXe)
19. [taktile.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE20JIUYM9ouxrR5PvkuR9Wm1zIACi6DwH-w9Yf_Da2CtW8cHNCTeEMu-DWyo3mP7tFQqNVGII5rZLelTOYZnprU7wJls-0hx1qGEU7OHjdg9vgvdxCR3RuVr7iyeQt_Wq-jOmhOuC7X_VdVI7RG7Q=)
20. [clydeco.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDqTgP6bmaxCTMnYIbQGSHsny07CjCvnkbc4SIXjM_p0MY9r33nsqusYqDzA-raIMdGS8fanr5wfIkgU_aadCEq0Svzx6PzwUfJYoNHgnNvNxnoBsKwwSBtB1CODxRYlzk1s50YwbTIuA3ZU9GtMgU5WdMdoGz0cS16mosj0lXUKWCeAJIu0vSKFiW8f9qk5Tu6v4T)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGlNGprQ8_ierLaNIetH4pes_EpU_AJY6Vn9xEnonTe0qkEYjOe5Zi_SX7M3xxSfRZu8GdD-LxWVaOa1yOfI9Tgj7Hd6fnHLxStVPtOGr7x7-Gy-UKDPJ_9HYzW9q5kn_KLF7LnvhlUA-CNnvkDF2HWJ38anLFyI-0br1_cXNzr3s1y8tDiPTh72MbyW5HjeDYuAjvpx4KuLGzXVNcazBY2ugU3vswa5V-2e-c_ud_BQKJfNGksuJwKALq-4w_QbTUbrnuLjt8c3Z0)
22. [jisem-journal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrFo99a7iN-mEhkYq3DUxesEisaNn8ifKZb3TMIyyJfF7OLqTPgms5pE8LZcLjxf1pACdqBzhLSRT4IcD5V5jAqXyTplGwhBTkj7XTFzWTrt-dK0KWmOG3RadjrWd6mq-kZ42hanIfWsq4YO8kBlQ8_b__r7yB_sbxtMXos7x6eWE=)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm_Yo43QxJvua-zfuFGrL9WuiShjhazf_Z1zCIU444JaovDniMlgQpw5zUpVqN6SY2s6uJ4on_DDbvm_7s8X2Sy2x2LaPJO5CpAzxMxhTNmxahSgCuKlhHhDVjPp8=)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRpDq8hTHDXerA33zyuUxT_Gdd03GtAKCKaFocZEv9FavLnyasRsCBT1jsJqicv5cRts37mCKUgwgj9bINB2htdmd9_264uEDLUHZAf55Zsbpw4fF_OzYS9A==)
25. [ijaem.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERyJbiWgmf23a1dPIwrhmKPanQwD4XQi_LDQ3cJckMGQ4KfysitzmrOs4JJRRW2epD9nfN6VEXl9T-ylnI3QJVJrcgU3XaIfRHoy1GfoqwhDGcVGCKyfxBKvJpxisJunP04LP5_rp5z1DXh8JxfrwjTD9kIPQ8KY-4P9Sz2IZiN3ANf8joLWnPSr6CFiNM0ZOmzgZ1QqPma9q2eMZNQG6NZVcsDZVgaX-v22FbiITMOXgDaoCCVnpybsZGvPdbnuHT6onNc3op-jItKHgj5ZwPL8yELNU=)
26. [ergomania.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOc6caAPp9BkoBa-1_FzTatgzMyvMhtq3bKN7SCJwFKeGbx91yOWaywP-oCl0URv27DkqW-TRRhi1BK2ixp0G3Ptu8l3-GzzfBr4hZm3UlIBBmioMPGTQLsn9ujPWg55PpOtF5nV5dNkOOF_1ztTBK)
27. [humai.blog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkT4q1GxNvO0s722Rut3RH6OAsSmv8cxVyYJMY7eEoUhA7evlrsJr66zhYuhB0lc5c7vSyFZeByHTZU7otJ1lamgZ9WOz0Howx2kJS7H1_VlISZ-rXPEHCxdzW-AJrTI7S3UGy26gBS5y5EsLJEGEMT93IOL7JLKjBFghx28cAoN8kT4xr_KYrXw==)
28. [ijert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbvvn1YK-SURK6bKb7I4RQeuaJKTcDpHgZcCW7oy89Y9j0rpGcGenWiiXzmxgrLrPOktOv06PteLlNEGrzhx9LIpGSGJ5NW5fo_iQrJKrNfzn7J_cvxeVv8hvyF01WmqXE6VY0KA88ox8AlvyJkNE3RVVqd_QfefTfbzAy3ewaNQyYVs9ne-3y7E3Fu-KYjhmNT5MbTph4Mrteg2u8EJq0d3989I_SAXxnSdNMbaKttBQ=)
29. [ijsra.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1dm_l852cQk4PRVBvHlZbZpxygxiBflbR4PX_whBa2nsI-H1PYgQuTqDGnH1nN9LL_YIOvgI8ndV2u8gR-8l009FFs56D7Of4si1W4Y3BMLQvw1IYp0pI-zy4rzjIVCJyeFziN2W_UFT4M6gqMCI=)
30. [ijirmps.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIpznxzEBZvK60hu-_uEKobE-zWaKKz0-GKxmwS1HKtBcUYMioOwtUtmIJfBD2RL0-xNyHmyZnjHnv3UzDqenD7j486BQQ_BuYNzVSeMX7E8YMwLAYW9NgHXISK46pRf_BVACP_YM=)
31. [bohrium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0cAsFNcHTnTmjnhXHFtCwvIBq5wxE9UEKTsZO07hiflHcnyQx1iSrZpK0qdd5XZI8d5zHhEVAgy_ryORTkrdmesPSciar194yToRDIlOfHD11MMbP8MUxRcif_FHsujPS90_0ARqXE1vMjmxZCBTm-fTvu8K7ivJPjRX2D7du7jXanTI1O199-7B-AL8hcOGPg1UmkwUC6igt2gkMFlVHn1HmFMUNTac_mxIy1la2fwM_RaP0gTbUmf7TwHBwco1KU6EVx31OgH1CeGt925Ry1d8aDsG5GM_XtcOheScqpA8NOiWQItDQFn-XHAIEKdAtSaqnGh2DIJ9g7YKpDsPcPxEMEzBkdQ==)
32. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ-ZSMTzBrfswywLxJ9tFb_xlgtsUkKv5C-lCpJ5b1QVNxDwYv9FASkMYQSIXZbxewGi_iJ6pcTHQBxJDuH0T_5vH6R6LIg_WI-6ZJwI7_9nWCEDB5w7jJJIzLQMXXuejjtHpGFPNaC6Bj7AGTcbSWXe_ynSxvr6WtNG3UNEPOuIW1CRhNWU63Ou0qMmrzaqpj-5u5SQiDmBh3)
33. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv85ocW2RK_tspIrq_j3SYcLBjbDEsLOVcZcve9aRWWCLZpfUpByCFd-SYtD8nQoH-p3WKp8hUIIvGVcFEbko1694mKc6s8DgHGuEIG2_HeOuC9M7h8P85OWKUPzYOZBSwscw7sXVBeGEm)
34. [sozialministerium.gv.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQhYG5IVjJgHlRJtsyyMnTiHG3MnYe3C-3Vwts8jsoj6Su0naroVOkp7TCWnfzRHMIQJCD8MwqPh_BxSUxYrjmbJvklYh1U3JxODfroqUPC3N6MmyPDdGnVAar_FzgqucM1SF53doeJC2ICWrWMwk-38XLA6uaaQpMObzXGKLkuiH2dtV-geYHwn8yT27vs9uVD6S8EqsBAuz8d4MMkR6BnyCsKIeAYRdFHH6b9ExpLtzud2B4XGwiXJVrn99C5nXy)
35. [bankingexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfqhevp4RQ8XziTjIvRGD9exPI0xdS-wG4zCkqlj-c9HbjgC_IrXOzJ90POoz192h3MNe8Txt8knWnLSVtp_IPOEy_Vp24_kr9uXaYMZoy43y393B-UZiL2fB6aj9E6r1EMLuCrAG84a0W8bbuRySVuHDfJUEtx4HKX6mJ1OuWOVqoZnPs8dEKNz-wG08zQM6bJ2KTRkjQE2oTzBTKmD5-YVKHYckPHvrp2WGI4ByMMCweP9I=)
36. [nano-ntp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2cZTZ3GSfKOm4erc0TW3ZeBYjufoGr0jOadXissZT-2PBVyjJyIYpKlCiu-f9EyDEdQhgHbqvs_cuOS1jZ3CNm6px6N_qJ9vRuP23soRhvjHnNxEY-tkMnzVaEh-xeNbmPvKQfHKGvgmWtz2pEjcigBcWS9-uP4i)
37. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ1thoNOV3n99f0gdVNqpnTan3V63oOVX9ffS3myrVVEV7oORETCUCJpzeFpxYGSpsAXwHOw-Oy1Lcdj5hCwajZxFFHgMYL9mb8XZ8x-CwUWl7k-xfDcnXF0XG_4rYVw==)
38. [alphanome.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhuQ2ifUKxvWmzL9FxWvFOr8DEygK8bqBLr3EHHl8fDL0QIPuX45BQMRNz4_W66a3S2hhCHoyt0OB0aMNCnfIyk7pk_l2hh4Yh_3SWl7EtcKQF1ERqOLdGlnJofvRCcjq6YIY_ifPKDBA4O1Hd4IU57BdrcgnK_hAXGVVWQisMFUdzPRu_kv3zmonkV1oAx14-aoUcK9LZ)
39. [spglobal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaqBwk3dD6Hr0xQOAh6XJEQp3FriiUMZ0YPGh7JQmgZkf5bv_agK01FJZtt_XxWeIm4l2qCpXX1LGYGq6R3m3dsP3mdqR10I-PdL3CFygOZeLkXhjYBWtfbH-YZJhjka9gT5FKEZ7_plf8ASxJCafv5F3JLU8mtfsdgIZj1bxuOG40Pjo-wTrpXx89IJ6dmU6VK3px0UZiEwV-iMD-XGNPkeMh0kxg2V5XNUkrB9LhAoKFEGtieE0=)
40. [alphanome.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfPux9BgtLlBm9K23XfeFjX6jMxyX3Z4nSMZvob1LgZgGr6gYnoD4Q-1kldvtLWOKd0EkSsXwaJ6H5viC58Oxyj0Ai7wXWjtLuGLOZ-O5sXKm3GppYTtnK7XZ-FTPDftKWL2xT3Tf0mOh3tfoChNOR9y1HLi4TZXvQuvXlE1EIeknPxfT-4f9q)
41. [alphanome.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEq7kGWArQNYcsbVuEUcsFX8jHKimbdxNpYogkVcD-1VO4obKVnYnWLAlvFNzOUxyxfB2wLmzI3ME4TIJVnux2Gc1u2Y6RbNxu36Ivn9GcrhPMfwkcDUm1ed-7bm0hKRyMhKkmZgaDXHclb_NJwNpudSNw6qrYXT6cjAIdzIRJ7vK_Z4H4PjBSFk9VU57Y29RP6ugU=)
42. [aidatainsider.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEepOXU8Srse25euYSTV3Ed7X39mqag-z3BEuXdu37gKDkKnSyZv80TYHtL2WwfRffQ_zPzAT1v2kP-GV2qxBUk-zVUnDUSjcNO3DH2xE7QdwsaPZ7Js0D88DDYQ2lnoxRv-PKjyslbiRd2DWBHmPJviR5zR-4L_Lq--iNmjFzoW4hzQvMNVgdoWA==)
43. [financialexecutivesjournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXzTFx2BGzVW4500VXH4JMGI3tF2HZohw5BWTQzlPnvHhBS6QT1rqLczTuu94btJdMpFJlBL6tm4ia3DdXaLYgFOvRzNk-k-KN68Gno5xeKN22LLIAS5_gZh-TXA507WG_wFKkvuFQzqiWpE9GqXSG91Ei-9Bn1J2csmrfjIVKz-K7uaBGvxgxkii_tZADR5Md1TIgwNRAqiqYConN21pMXGJtP73dCbVwTibQaWgNeApdt7MoZfkk_sLcgw==)
44. [forbes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNe9Vk3ddJ6iL9jYzi9Q2rgSqeyejXngHcClppEbSxWW5zArT1iZQ1IqqkkU9LdcYBjOVu7GccaRLmvYO5oH4yPfhPNitcTLYcmStd-8qbUofrg_LF-kW3JcY2Y_leZWPtg5Cbws7JXG6Cxs1Wzle7GpsqFlxmAjOCibPQJvrRdgAmnz7xE5yGkI4zYZENtyRtVy6GGPqUR4facAVTzzidKzBvRHEklgLGm-EElenmvTjQHGa4)
45. [ecejournals.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxNsn2x8ZP2-SY_Go7PG8ZFrRRJdFK0ttpr92ZKmYFs44PjaYd-yqA56tquX_r2iAFCEEKiTwrmK_sJvB21MvmFYcKxPqfjuqt9UUPcyzDo4fC1U5pGMQQlAl7fsRkbMZy9Jw1eyTiIVpi94kKM6xi)
46. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlhgbhcFSvshLyHMA0q8DusEyFIPvBUQIAGBWrVeLCHNHyJJAJwV4vjQFUfcySnlnGsCY7i-yOMSHRDD7UWTvcU6JdR7pHWqAF6_FwIB_pDVgQibCtIaFLdJXlW___NrAbeKy5VeAw60zPHshLhoKOTRM0e_n4QDc61UN0fw==)
47. [colab.ws](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGih1FnbamAgvdzx6ofXEguH4TWaTk5FLx-iflRfFTvOEITWlE39cWlbhOVUD1uRMJjqrsUyxzJssHy4YEZ7QeIbjg-BUGJpnXKm0NTbeRUwR_nYj9aoL9H_cSvtNwS2aVXV_4NY17agqEo20c=)
48. [ijfmr.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ02QMGtLU7pQ_FujzuJJy3QbWT1nEXxwXbZ8REpBowMVCcZs0Onhk735P06TOkNac6kn2-d3165gIdR9QoF4WosCzyYn3IGkz81upkH_vCvsAIKpS-UcO91TgUSZguurYBjs=)
49. [scienceopen.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd4Lf30-UXOn5u0qyo5kO8crH0LUyPHrwEpN7xKj40hl-kD67QwnnUNn_KgCwvoHtSqKUojzBKVjbIpeE79mvbMVFSVMp9_CxT-DJcQXXqWalZF4jLpJKg-RG36BYAjUN_7IOR97uJ4g3Pd_SgnqH8HZoyLHdK6xanz8m-1uyTtg==)
50. [ktu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkX3G9RdvoiCbzknsjNxkeCT6UclfIIiT63k8OyuVdQh7YvciYxAKB2qILIREgVufcbzPrnZg3IJBjgGlOOnEo6Q51nMvoBMzqIVtCg5hpO0KxBcxVhdsRa_Or722iw5pmwfsfWAde7N2UnEct)
51. [qeios.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2W9Fy9IjG-8Y-98LRkgUT9550t971eTafGCGje-MGjEWyrgcyTfKG5ZUyYQqokx92Y2PQ7iuIbDXMf6bvK_o6bY4V67eacMUjGJZvBDFQn9QHL8NcuYg=)
52. [scilit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZggFOGj3svakKrTavNzxcXaz26Oo4-fY47oQhG16xqXSAn-BtVDdgCZD9EhsVCKelsQh1DCjLotXW_MnFMQax2NqVyofiUfcsvOYWjptIu2BTxdHqm94VXIT8HMCIyzOK8sU14Yng8fu68F4ZbvyAt100XnhbQV3fOw==)
53. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSoejlo2R2CQBmjYeLQ1GWZRIsNGRHMZX2H5LQhlOd6JwMKCbfqRnscGFk7r6_2QGzWqpOtBu-dGHOve9QykvNG5Hh1GQg91qBegSqcb1J15OF5LXhG6HgJu_cqNp_Va32)
54. [moomoo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr2NgJTWpG51mo3-gneYumEGQsKHz3HZ3kS-DtOPp-d4ckEvzp2Us2zq2mhNK6gg5RfrcT9flyd2ZxvILcY0UTSaaIWoCZQEgoiRG3vhCfE_285_1CK9MS1R5DmvFwyRLlYr9R4vf1xVnqzTaa_V-hf9xaPayZrmIFbmsM2PFtuU21C_PGFRbVQUFXU9YRiQQawbQ=)
55. [issarice.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXEJ1Il30DJAjSBNxiV96jvbVCgCczr40fUMdTvD9sU7pKceNpFNrXu2LO80PIF74VEyQ26bveEUWwBQnwprG_imxImym7Hy0YUoQ5EFZOMvtSqVrTyw-KFQVLhjcepf53jXgm_CVBXCM=)
56. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTzxD9Wtz13LR4mCAR6e2EoyQvSfym5uoZJpBQaMiReM2EFgqHAlA8Zn1kdxothkjXjZ6svSMl0g06bqn7o-c70KwU5i14YJWMUCxVS741HHST0_tSXYrfWA==)
57. [scirp.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEAWECiTDiwJSG3iUNOneTt9k7akytnpIBw_dK8hrC1Z-wtV8AWw1ipyfTOxmRHTB6xHKuXLcPUPIaBavGVCV4V-mW6ZfdlHeRE-UUBQ6acBN8tRvX8aZXAGTYcrJJ00sf_Lq3ak4O-f6BhqB7Qj3MPQryeQ4QvEJFyQ==)
58. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgvJ3TecKKLFJn0jvS_9Cp4P-jZ-7jYvK-7V4pJFaOW7gv4Bkl_CqIEWqq4a9SH-ayki1yKJK7JkEuoWgm0TXQhKmBlVfl5O-EiIypDzB3KkwJhrUJXg==)
59. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3lHqfPtPRGjrqSFeyB54TiStG_uh6T-x0ThGFEBVWte07B_dKWDy2jVhvtpu2lryfKcxFyPEUaFVgxYnpf82BAYum2_JzpReLk0JIG_KMcCFDkqaf55CTHYLjHZo9SPGeC0n51YTQpCQU2eFTCz-cMDwwS8XrQflYrowP1l1XIxtpZllTWSnqgP12Zmk2yJaWaw3sjdKxP7FyDFA7RGG3GoLAmZB8-nTmT4pm5uucaci6UXqbu5tAyHjjl3s7Tgpamg==)
60. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETmSGmwVcsA5MwHsIUE3R5OtP96Zwe_ykHhz2O41Vp-FcIkphRyxe3zI_anMszapSEfjLkJ2jOPfiAeSbE3dKLUqtjjglMID2aMuc0t_SRjj5g-nbodQeXLK6yjsK9yrhE8AGZC-borDDrfBBYthz6S125oqIsLg-qTyJriEa5UOj8IWh2VEt-j8wUh2Ib6Ea9Lbyxro3rTI6eOOp5JC12Fa_vTnajJizmqUdoAq_JF4Y57-Ny_QwjyL23XI-4IUN5VeLsAw==)
61. [scirp.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFPsRY3sp0oG7z3E8ULYZXmZ5pxDLRTdB5M_4h034H40Tc4MrYvSUPUdaL5BKH52_dlrQYlXHRyYVRm_8gvV2wDc0u076vBgMT_OR4zfDSTW2DBTyHhjEqqwpdUTGxW9lnJbUg1uGjhCC28t_VRcYdQkLU)
62. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOCttxofv7wkOK_6r0Wm4-TuIIlvxZQY1INGGYskw8J-sJZTsmxyWgEkkXozyVCRnbXiLgZnTLtCkxXpCiNDNkL_bcQKTw1UZU7XxbkDpScP8dNn_7ayNOoZAueB7dD-T7LxhGhTsgV75PiNqJEBpAH_Ga7Oo-Jh-lkQAgFcCBKC5zL5hprNY0)
63. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcwM9XJeI7YOGWraR7KWMXjqhzq-wifGEZnJPG0P4DXUeWTZXwx_wUNWKfkyZ6PKCBLBpMSTjpsoN5wS-M49SePStSNZlgyyeAhTfU7bQxpDmL3lCsCg9ppddDygagOQ==)
