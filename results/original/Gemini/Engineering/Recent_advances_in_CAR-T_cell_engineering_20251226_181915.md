# Literature Review: Recent advances in CAR-T cell engineering.

*Generated on: 2025-12-26 18:19:15*
*Progress: [11/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Recent_advances_in_CAR-T_cell_engineering_20251226_181915.md*
---

# Engineering the Next Frontier: A Systematic Review of Recent Advances in CAR-T Cell Engineering

### Key Points
*   **Evolution beyond Blood Cancers:** While CAR-T therapy has revolutionized hematological malignancies, recent breakthroughs in 2024-2025 demonstrate significant progress in solid tumors, particularly targeting Claudin 18.2 in gastric cancer and GPC3 in hepatocellular carcinoma [cite: 1, 2].
*   **Engineering for "Smart" Sensing:** Novel logic-gated mechanisms (e.g., Tmod™) now allow T cells to distinguish tumor cells from healthy tissue based on Loss of Heterozygosity (LOH), addressing the critical challenge of on-target/off-tumor toxicity [cite: 3, 4].
*   **Expansion into Autoimmunity and Aging:** The application of CAR-T therapy has expanded beyond oncology, showing durable drug-free remission in Systemic Lupus Erythematosus (SLE) and potential for reversing age-related fibrosis by targeting senescent cells (senolytics) [cite: 5, 6].
*   **Manufacturing and Delivery Revolution:** The field is shifting toward rapid 24-hour manufacturing protocols and *in vivo* engineering using lipid nanoparticles (LNPs), aiming to democratize access and reduce "vein-to-vein" time [cite: 7, 8].
*   **Safety Vigilance:** Despite these advances, the FDA has mandated boxed warnings regarding secondary T-cell malignancies, necessitating long-term surveillance and rigorous risk-benefit analysis [cite: 9, 10].

---

## 1. Introduction and Background

Adoptive cellular therapy (ACT) has emerged as a pillar of modern oncology, with Chimeric Antigen Receptor (CAR) T-cell therapy representing its most transformative modality. First conceptualized in the late 1980s and achieving FDA approval in 2017, CAR-T therapy involves the genetic modification of a patient’s T lymphocytes to express a synthetic receptor that redirects specificity toward a tumor-associated antigen (TAA) independent of Major Histocompatibility Complex (MHC) presentation [cite: 11, 12].

While the initial success of anti-CD19 CAR-T therapies in B-cell malignancies—such as acute lymphoblastic leukemia (ALL) and diffuse large B-cell lymphoma (DLBCL)—was unprecedented, the translation of this efficacy to solid tumors has historically been hindered by physical barriers, antigen heterogeneity, and the immunosuppressive tumor microenvironment (TME) [cite: 13, 14]. Furthermore, the logistical complexity and high cost of autologous manufacturing have limited patient access [cite: 15].

This systematic review synthesizes literature from 2024 and 2025 to analyze the "next generation" of CAR-T engineering. It moves beyond the established paradigms of hematological efficacy to explore novel structural designs, gene-editing enhancements (CRISPR/Cas9), logic-gated safety switches, and emerging applications in autoimmune diseases and senolysis.

## 2. Key Concepts and Definitions

To understand recent advances, it is essential to define the structural evolution of the Chimeric Antigen Receptor:

*   **The CAR Construct:** A synthetic fusion protein consisting of an extracellular antigen-binding domain (typically a single-chain variable fragment, scFv), a hinge region, a transmembrane domain, and an intracellular signaling domain [cite: 16].
*   **Generations of CARs:**
    *   **First-Generation:** Contained only the CD3$\zeta$ signaling domain. These exhibited poor persistence and minimal clinical efficacy [cite: 17].
    *   **Second-Generation:** Incorporated a co-stimulatory domain (e.g., CD28 or 4-1BB) alongside CD3$\zeta$. This is the standard for currently approved therapies like axicabtagene ciloleucel and tisagenlecleucel, providing necessary signals for proliferation and survival [cite: 11, 18].
    *   **Third-Generation:** Utilize two distinct co-stimulatory domains (e.g., CD28 and 4-1BB) to combine rapid effector function with long-term persistence [cite: 16].
    *   **Fourth-Generation (TRUCKs):** "T cells Redirected for Universal Cytokine-mediated Killing." These are engineered to secrete transgenic cytokines (e.g., IL-12) upon antigen binding to remodel the TME and recruit innate immune cells [cite: 17, 19].
    *   **Fifth-Generation:** Incorporate intracellular domains of cytokine receptors (e.g., IL-2R$\beta$) to trigger JAK/STAT signaling pathways, mimicking physiological T-cell activation more closely than previous iterations [cite: 18, 20].

## 3. Historical Development and Milestones

The trajectory of CAR-T therapy has been marked by distinct eras of innovation:
*   **1989-1993:** First generation CARs were developed, establishing the feasibility of redirecting T-cell specificity via antibody-derived domains [cite: 12].
*   **2010-2012:** Clinical breakthroughs in CLL and ALL using second-generation CARs demonstrated massive expansion and persistence in patients, leading to complete remissions [cite: 11].
*   **2017:** FDA approval of tisagenlecleucel (Kymriah) and axicabtagene ciloleucel (Yescarta) marked the commercial era of gene-modified cell therapy [cite: 11, 21].
*   **2024-2025:** The current era is defined by the approval of therapies for earlier lines of treatment, the first randomized positive data in solid tumors (gastric cancer), and the expansion into non-oncological indications like Lupus [cite: 1, 5].

## 4. Current State-of-the-Art Methods and Techniques

Recent literature highlights a shift from simple structural modifications to complex synthetic biology and genomic engineering.

### 4.1 CRISPR-Cas9 and Gene Editing
The integration of CRISPR-Cas9 has allowed for precise "knockouts" (KO) of genes that limit T-cell function. A pivotal 2024 study demonstrated that **CD5**, a surface glycoprotein, acts as a checkpoint inhibitor on T cells. Knocking out CD5 using CRISPR enhanced CAR-T cytotoxicity and persistence in both hematological and solid tumor models, surpassing the efficacy of PD-1 knockout strategies [cite: 22, 23]. This suggests that relieving intrinsic inhibitory brakes is as critical as providing activation signals.

### 4.2 Logic-Gated Engineering (AND/NOT Gates)
To address on-target/off-tumor toxicity in solid tumors, researchers have developed "logic-gated" CARs. A leading example is the **Tmod™ system** (e.g., A2B530). This system uses a "NOT" gate logic:
*   **Activator:** A CAR targeting CEA (Carcinoembryonic Antigen), expressed on both tumor and normal gut tissue.
*   **Blocker:** A receptor targeting HLA-A*02.
*   **Mechanism:** Tumors often undergo Loss of Heterozygosity (LOH) and lose HLA-A*02. Normal cells retain it. The Tmod cell kills only if CEA is present *AND* HLA-A*02 is absent. This exploits a genetic difference between tumor and host rather than just antigen expression [cite: 3, 4, 24].

### 4.3 Armored CARs
"Armored" CARs are designed to resist the hostile TME. For Hepatocellular Carcinoma (HCC), GPC3-targeted CAR-T cells have been engineered to co-express **IL-7 and CCL19** (7 x 19 CAR-T). IL-7 supports T-cell proliferation, while CCL19 acts as a chemokine to recruit other immune cells (dendritic cells and T cells) into the solid tumor mass. Clinical trials (NCT05911217) indicate this strategy significantly improves infiltration and tumor control compared to conventional CARs [cite: 2, 25, 26].

### 4.4 In Vivo Engineering via Lipid Nanoparticles (LNPs)
To bypass complex *ex vivo* manufacturing, researchers are developing *in vivo* CAR generation. CD5-targeted lipid nanoparticles (LNPs) carrying mRNA encoding a CAR can reprogram T cells directly within the bloodstream. Recent preclinical data (2025) showed that this method could generate functional CAR-T cells that reduced liver fibrosis by targeting activated fibroblasts, offering a scalable "off-the-shelf" solution without the need for viral vectors [cite: 8, 27, 28].

## 5. Applications and Case Studies

### 5.1 Solid Tumors: Breaking the Barrier
Solid tumors have been the "holy grail" and the stumbling block for CAR-T therapy. 2024-2025 has seen breakthrough results:

*   **Gastric/Gastroesophageal Cancer (Claudin 18.2):**
    The phase II trial of **satricabtagene autoleucel (satri-cel)** in Claudin 18.2-positive gastric cancer reported a statistically significant improvement in progression-free survival (PFS) compared to physician's choice of treatment. This represents the first randomized positive trial for CAR-T in solid tumors, with an objective response rate (ORR) of 42.9% in high-dose cohorts [cite: 1, 29, 30].

*   **Glioblastoma (GBM):**
    Intracerebroventricular (ICV) delivery of bivalent CAR-T cells targeting **EGFR and IL13R$\alpha$2** has shown feasibility and safety. By delivering cells directly into the cerebrospinal fluid, researchers overcame the blood-brain barrier. Early phase 1 results indicated rapid expansion of CAR-T cells in the CSF and tumor regression in a subset of recurrent GBM patients [cite: 31, 32, 33].

*   **Hepatocellular Carcinoma (HCC):**
    The **C-CAR031** trial, utilizing a GPC3-specific CAR armored with a dominant-negative TGF-$\beta$ receptor (to block suppression), reported a 50% objective response rate and a 90.9% disease control rate in advanced HCC patients. This highlights the necessity of "armoring" cells against TME suppressors like TGF-$\beta$ [cite: 34].

### 5.2 Autoimmune Diseases: Systemic Lupus Erythematosus (SLE)
In a paradigm shift, CD19 CAR-T therapy is proving curative for autoimmune disorders. A landmark *New England Journal of Medicine* study (2024) and subsequent follow-ups showed that a single infusion of CD19 CAR-T cells led to deep B-cell depletion and durable drug-free remission in patients with refractory SLE, idiopathic inflammatory myositis, and systemic sclerosis [cite: 5, 35, 36]. The therapy appears to "reset" the immune system; when B cells eventually return, they are naïve and non-autoreactive. *In vivo* LNP delivery of CD19 CARs is also being explored for SLE to reduce costs [cite: 37].

### 5.3 Senolysis and Aging
Targeting senescent cells (which accumulate with age and drive inflammation) is a novel frontier. **uPAR-targeted CAR-T cells** have been shown to function as senolytics. In murine models, these cells eliminated senescent cells in the liver and pancreas, reversing liver fibrosis and improving metabolic function in aged mice. Remarkably, a single dose provided long-term prophylactic benefits against metabolic decline [cite: 6, 38, 39].

## 6. Challenges and Open Problems

### 6.1 Safety: Secondary Malignancies
In 2024, the FDA issued a class-wide **boxed warning** for all approved BCMA- and CD19-directed CAR-T therapies regarding the risk of secondary T-cell malignancies (T-cell lymphoma). While the absolute risk remains low and the benefits for cancer patients generally outweigh the risks, this has necessitated lifelong monitoring protocols and rigorous investigation into insertional mutagenesis caused by viral vectors [cite: 9, 10, 40].

### 6.2 The Solid Tumor Microenvironment (TME)
The TME remains a fortress. Physical barriers (stroma), metabolic starvation (hypoxia, glucose deprivation), and immunosuppressive cytokines (TGF-$\beta$, IL-10) exhaust CAR-T cells rapidly. While armored CARs (Section 4.3) address this, "exhaustion" remains a primary failure mode. The discovery of CD5 as a checkpoint [cite: 23] and the use of PD-1 dominant-negative receptors are attempts to mitigate this, but consistent deep responses in solid tumors are not yet universal.

### 6.3 Manufacturing and Cost
Traditional autologous manufacturing takes 2-4 weeks, during which patients may progress. The "vein-to-vein" time is a critical bottleneck. Furthermore, the high cost (often exceeding $400,000) limits accessibility [cite: 7, 41].

## 7. Future Research Directions

### 7.1 Rapid and Automated Manufacturing
The industry is moving toward **24-hour manufacturing** processes. Platforms like **MARS Atlas** utilize automated isolation, activation, and transduction without the need for extensive *ex vivo* expansion. This preserves the "stemness" (Tscm phenotype) of the T cells, which correlates with better *in vivo* persistence and potency, while drastically cutting costs and time [cite: 7, 41, 42].

### 7.2 Allogeneic "Off-the-Shelf" Therapies
To eliminate patient-specific manufacturing entirely, allogeneic CAR-T cells derived from healthy donors are under intense development. Gene editing (TALEN or CRISPR) is used to remove the endogenous T-cell receptor (TCR) to prevent Graft-versus-Host Disease (GvHD) and CD52 to allow for lymphodepletion. Trials like ALPHA3 (targeting CD19) are positioning allogeneic products for earlier lines of therapy [cite: 15, 43].

### 7.3 Convergence of Modalities
Future research will likely converge *in vivo* delivery with logic gating. Imagine an LNP injected intravenously that transfects T cells *in situ* to express a logic-gated CAR that targets a solid tumor while sparing healthy tissue. This "drug-like" application of cell therapy represents the ultimate goal of the field [cite: 8, 44].

## 8. Conclusion

The field of CAR-T cell engineering has transitioned from a proof-of-concept in leukemia to a diverse, sophisticated discipline capable of addressing solid tumors, autoimmune diseases, and even aging. The years 2024 and 2025 have been pivotal, marked by the first randomized success in gastric cancer (satri-cel), the clinical validation of logic-gated safety switches (Tmod), and the "immunological reset" observed in Lupus patients.

While challenges regarding safety (secondary malignancies) and the immunosuppressive TME persist, the trajectory is clear: the next generation of CAR-T therapies will be smarter (logic-gated), faster (24-hour manufacturing), and more accessible (*in vivo* delivery). These advances promise to transform CAR-T cells from a "last-line" rescue therapy into a foundational pillar of medicine for a broad spectrum of human diseases.

## References

[cite: 11] Frontiers in Immunology. (2024). Recent advances in CAR-T cell engineering review 2024 2025. [cite: 11]
[cite: 13] PMC. (2020). Recent advances in CAR-T cell engineering. [cite: 13]
[cite: 12] Frontiers in Immunology. (2024). Recent advances in CAR-T cell engineering review 2024 2025. [cite: 12]
[cite: 14] Frontiers in Oncology. (2025). Next generation CAR-T cell engineering strategies. [cite: 14]
[cite: 22] CRISPR Medicine News. (2024). CRISPR enhances CAR-T cell cancer therapies. [cite: 22]
[cite: 15] Frontiers in Oncology. (2024). Allogeneic CAR-T cell therapy current status and future 2024. [cite: 15]
[cite: 43] Allogene Therapeutics. (2024). Allogeneic CAR-T cell therapy current status and future 2024. [cite: 43]
[cite: 21] ResearchAndMarkets. (2025). CAR-T Cell Therapy Market Research 2024-2025. [cite: 21]
[cite: 6] MSKCC. (2024). CAR-T cells show promise against age-related diseases in mice. [cite: 6]
[cite: 38] BioWorld. (2024). CAR T cells could slow aging by eliminating senescent cells. [cite: 38]
[cite: 19] Cancers. (2023). 4th and 5th generation CAR-T structure and examples. [cite: 19]
[cite: 17] ResearchGate. (2020). Five generations of CAR T-cell structure. [cite: 17]
[cite: 20] ResearchGate. (2024). Generations of CAR-T cell therapy. [cite: 20]
[cite: 18] ISSCA. (2025). Evolution of CAR-T cells from first to fifth generation. [cite: 18]
[cite: 16] ProteoGenix. (2021). CAR-T generations. [cite: 16]
[cite: 41] Blood. (2024). Automated Rapid CAR-T Cell Manufacturing Process. [cite: 41]
[cite: 7] bioRxiv. (2024). Automated CAR-T cell manufacturing advances 2024. [cite: 7]
[cite: 45] CGTLive. (2025). CAR-T cell therapy for autoimmune diseases SLE lupus 2024 2025. [cite: 45]
[cite: 35] UC Davis Health. (2024). A breakthrough for lupus treatment study explores CAR-T cell therapy. [cite: 35]
[cite: 46] PMC. (2025). CAR-T targeting Claudin 18.2 GPC3 solid tumors clinical trials 2024. [cite: 46]
[cite: 9] FDA. (2024). FDA requires boxed warning T-cell malignancies following treatment BCMA-directed or CD19-directed. [cite: 9]
[cite: 10] CancerNetwork. (2024). FDA mandates new CAR-T cell therapy boxed warnings in hematologic cancers. [cite: 10]
[cite: 40] Pharmaceutical Executive. (2024). FDA warns drugmakers of additional cancer risks associated with CAR-T cell therapy. [cite: 40]
[cite: 3] OncLive. (2023). A2B530 harnesses unique mechanism of action to integrate CAR-T in solid tumors. [cite: 3]
[cite: 4] ResearchGate. (2022). A2B530, an autologous CEA-directed Tmod T-cell therapy. [cite: 4]
[cite: 6] MSKCC. (2024). CAR-T cells show promise against age-related diseases in mice. [cite: 6]
[cite: 39] PMC. (2023). uPAR CAR-T senolytic aging fibrosis recent advances. [cite: 39]
[cite: 1] CARsgen Therapeutics. (2024). Satricabtagene autoleucel Claudin 18.2 gastric cancer results 2024 2025. [cite: 1]
[cite: 29] ASCO. (2024). Satricabtagene autoleucel Claudin 18.2 gastric cancer results 2024 2025. [cite: 29]
[cite: 30] Medscape. (2025). CAR T-Cell Therapy Boosts PFS in Advanced Gastric Cancer. [cite: 30]
[cite: 24] JITC. (2022). A2B530 Tmod system CEA HLA-A*02 logic gate. [cite: 24]
[cite: 36] BioPharma Dive. (2024). NEJM paper fills in details on remarkable CAR-T result in autoimmune disease. [cite: 36]
[cite: 37] NEJM. (2025). In Vivo CD19 CAR T-Cell Therapy for Refractory Systemic Lupus Erythematosus. [cite: 37]
[cite: 5] NEJM. (2024). CD19 CAR T-Cell Therapy in Autoimmune Disease - A Case Series with Follow-up. [cite: 5]
[cite: 8] Curapath. (2025). Reimagining CAR-T Therapy: In Vivo Engineering with Lipid Nanoparticles. [cite: 8]
[cite: 44] MDPI. (2025). In vivo CAR-T LNP recent advances 2024 2025. [cite: 44]
[cite: 27] EurekAlert. (2025). New method enables in vivo generation of CAR T cells to treat cancer and autoimmune disease. [cite: 27]
[cite: 28] PubMed. (2025). In vivo CAR-T LNP recent advances 2024 2025. [cite: 28]
[cite: 42] Applied Cells. (2024). MARS Atlas CAR-T manufacturing 24 hour Blood 2024. [cite: 42]
[cite: 47] News-Medical. (2022). Researchers streamline way to manufacture CAR-T cells in just 24 hours. [cite: 47]
[cite: 31] VJOncology. (2025). Phase I trial of ICV-delivered bivalent CAR T-cells in glioblastoma. [cite: 31]
[cite: 32] Nature Medicine. (2025). Intracerebroventricular bivalent CAR T cells targeting EGFR and IL-13Rα2 in recurrent glioblastoma. [cite: 32]
[cite: 33] Nature Medicine. (2024). IL13Ra2 CAR-T glioblastoma intracerebroventricular 2024 2025. [cite: 33]
[cite: 2] ASCO Pubs. (2024). GPC3 CAR-T IL-7 CCL19 hepatocellular carcinoma 2024 2025. [cite: 2]
[cite: 25] PubMed. (2023). GPC3 CAR-T IL-7 CCL19 hepatocellular carcinoma 2024 2025. [cite: 25]
[cite: 26] ResearchGate. (2025). GPC3-IL7-CCL19-CAR-T primes immune microenvironment reconstitution. [cite: 26]
[cite: 34] GI Oncology Now. (2024). New CAR T-Cell Therapy Shows Promise for Treating Advanced Hepatocellular Carcinoma. [cite: 34]
[cite: 23] Science Immunology. (2024). CD5 deletion enhances the antitumor activity of adoptive T cell therapies. [cite: 23]
[cite: 48] Penn Bioengineering Blog. (2024). Knockout of CD5 on CAR T Cells Boosts Anti-Tumor Efficacy. [cite: 48]

**Sources:**
1. [carsgen.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEehFQLzETb5zOy078-uN0Ut6cQV8BOBUlLXbehuD5VTa-2w17ARnXm4QbBxHQ2o6AuRtW20wWE-a_seBTy6LEKRCYl9m0WhPvbTLh5Y6XSRvYX_jz_yq2OKh6MJcR94g==)
2. [ascopubs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmupWiuM0QV-gg77yg9dDbuHQOFgxilZYFTlGwA9CrSk0LSVg73LR2VLpaYZGGoRmdKL3TYzuw3sPxFobSXOr02J_CHIMT-QbXzd2RBdGLzZ6z8io_U3xz-eJa3phWW0ay1Ph1IoJ23U40UW_x5sHO)
3. [onclive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZBhI7_LlwLo4JQBDlscwGjnh1zfyZNmxaRzMHKqRxhCuqjFRUZltNtjo7VRoLyYdRMLC1vClato1MDNxO_ob3576e-Ev6SIdIaneC_vr2jeC7NGhx-IFakNGKLAX8KUebuhfsdJax7Q0KiWBTARym1PGygXmP6AA8Q-PXD9o2MLb2b_BA-KceT7N55EQP8lURiMs2o90650MMvM_3AGPWiQ==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE446nCZu9Y7-sy95q9UaGm-CSSlRNGXma0ofRxH2A6Kk3i7IuUs0FMO0inZw1nkviV6ykXtHLw3krpiokM4T0t7yMqIRhO6rjOmX1ZMLp_oCxW9pE_mHlXrsLhocef5Yyn-GOixyLi5jBnQPJU_hgXL5LU_kUhKfS3sp-FOwSGqlVFjg2Ks6r5GLeJAO3Cw2UndJHeq3uLAFAhyTcYl6q76OpkfP9YBSzCHTwIgMSHlRw0Xf0w_Js3nCs2bo4EXkDBp4oWAcIld9nFFfFF7vQA8pioQmE_n9hG_rxjQ40fYXYImdQjN1q0PwquWUjY2r3wnA2yGUQOUNQTTKtv40fc)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEw0RG939Ncw_wlFwqXNXTf5Ukw_VyWrg6dqkTPRfhoCBzIQnS92IVrdq5isJAkNJi68Mc0NILJqEJhXhR3BUdf7TdUp4nRDpdCcwPkfrUEJPu8waSpM0m0eVomb9Ab7g==)
6. [mskcc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOJ-b3OU_5xFTDEFMij6UYWtSMsOISdOtwxceJLe3MPOH8PqbzvtU7-MZ8SLg_TVx_dg2hm1zCLV_MA3AIHnPrpb0u3Iao36rdPu0j1T6KpC14FEKxVoCy6_yQ3V7oYx743DUh7k2i5x4cbV1XrrX6ScqpdFbVniOYRjp8jpUSQ5c_xPruta61Va13OQ==)
7. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCtmuT7de0p6g-NRWyJ7Ks_3JjRub7ECwhGTsxQSJ6wss4eFd4amE_o6lSFHPEvs1MLAk3S_G79MY1OhyKPcB8dvCczdaua63cp6m2q_DuNVoPzXW5Xyws7ijeEUh8f8OCssTc_6qCrguAe49vrnXmpRx8hacg)
8. [curapath.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe77RwcENhjg12eXHrZYb7e6KUiJsTcbnZDB9yfmflMs8yb3Jchj72a7VK6A7phoMGp2y3w-ratQ4VudzwvRZBlGiYF_7GWirXlJwlGUu9NBExUC8C8bbBq3K9VhXXEEYOoiZCiPCT5CEc4gFH-TKnq8umAQ38bYNi44oGj2H9EusbtcZ7f3sOX6hbJ61KY95TeZHGY00=)
9. [fda.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu14q9qdCFnOX4GRDZMokiviiKdiFSBnrMdJnq1jZidvxCh4r4C-3dUUdgnfDb7y_L15zxnp-fAwk3qpulHwKV18FmsqLFF2DCs7pFSmJZ04NQV0FrHSbUtrwMvZcHHO4aOcDjQEyEpiszyr76vz1o7tG9dt2HMgVMLUgZmjPNUwoQdyrbu7f6FEhoY29wihID6jT3Eks8WKw8PKGyJOBVAyyKX7fKso68GrVa9gWbF9Nn_PtABtzEswkK0wtg1CTkKSe4asswDQX2p0XyOlZCLVKOubGJVKPlbVP8eVfumQ8L1Q==)
10. [cancernetwork.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFl8mYhLlK54mLgT23LT5mT3GZQ6X-jG3BHa5wp28OnaX6Ku52LA789KujiqqKWh3DDaKdIeR-ExrXoeotKk96fFMe1Ndh718SB9jHxaLNlZeu8fLvHstI-fM0kNU5dVFBmyBMRKEimvqpuxV68fTTu_M4xYNT3ylgpa8f0YZpJCplV_6iTmcPLYGpU6YiSRcWAh29djAHC8me8HiPuVbcL8Y=)
11. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGofXlR3yBomXxybzBHBNhOecqw29PZR4NCpvz0GjEnT6yqtDlpZJn4FAee39v-Ezt31jHKbeYY4ga0rJt_7XUrNnNmeykuHjlkw6m2tSI7Qkv8e3perCjecvnywBUq0XyWyxC_6_Qm5DGnItc6uPvOJOgZDr6V8kBuBkVpw-tyKPRnnDp4Z8VVdnEaIbaJ)
12. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrwmGMuG0Zb_pRqEuCgVrnQ_Hs7vD6--3501W3opu_J6M6y6NCIpE4nzGcwC9EhEtfIsrGUPTesCLuwO_eLttjrIMBm0UeFOH1ao7PGEY8wRFJPqAiax4Nfhx3xHVdxPqxi22wKTMZutcrBaumVi0Mo44OBrLQrX24-wB6v7GEFEVCkaeTg_InzkudHlMJ)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOOTPk3QUnZHv-sQwcEhW0XXeUArFYxLqaMh_fGcDgW0LYwNKg11Q83FEWaprnuGOlyXrmkITMaj10oQ9okr0-_y2YAxGGVw7ulbKJmnFQglj_A0qJsYxARAIR--SWli_2K4hQ9VQM)
14. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCkj4LDoLzJi3MuFuNLtJKWTOmsj0wC3z0wiEUWoyJf6yX_giJ9vMfwcteMsMTOmP_4JL3TuxPsZ3QlwkLukvVpBeRveBmbEI0OvQPRYoP-pnxlrx_J68b3eBXreyKxfa58GnJHldg1hwOHDz2oXOgNXeNQaJvnEmPwsz3sTq_w6BXc3JSu_xNxATrJrh-Jg==)
15. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAiFKFw6jdcD3NqFxYRN7Mc22GMaMnJrRp4bbNi9F0SYImuJ09LEITfyCrH1qxLrkBZB0Y-EvM9b0vryzuXys9anhKjrCiBH_usftmYv6KAwYkYq4uHQ-fHJgKVELzqMF4-ZjhVaHdDwOYpJ1gMJ0ccfaLvd73rvPbxdAv-O6zEptBWnqzGl_ZLlWS)
16. [proteogenix.science](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeM5fA_-wdXYKKeR2uONB-vfkOJf3xIzBu6IEGWjG5NLS0wv5booMR4OrKDsn70yMWttSbC7zs8GGrl22pLoMSPcVFdM6CVzfXXcq0OkyZ6lObae4RaAz6AAm2KD1g0ngLA9vZm1ez2FQELXrYLYW_bn8-Lt7wsr6zmUXSbje03A==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr8MQ-zu6yDU7mypQP4NhvseRymtKHkDQC2jAT4Ak5Nc3Lo4Evu2-ATCMKBmfDjT7fI_CzyhbdUKULqNOQoGG-uTVkjJfcMpDl8Dc_Ze7UuzfEmBtIsPryMPTKuXXfq4kYbMBoS8fYFnn5IlbZRuYyfTD74roN3mKMvCRt6yzxU688x8H28cV3UAP_1gAAYsvZZqMI6S5dY30ZVQTMc7f3flloCjtaAxwOx5HCVKA4WaZrGL80pCpQ6ZNdYZZVVrcQ)
18. [issca.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGowAy1csWti0HiwXMtbRyY_lkPexWGXFsOTEabVifeeJ0c1aUY6pQMOc5s0DhhG2wP7A4nJBF-EC_SMCqghbkawhLFdGn2jdqUxF848b7qSdOEDj2yeY-DnGvAMQIdvfHJ3Q6RXhANgGJbniYoizsV7SOvOviALkjMv_-8e5ZqGPQYHiE=)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7SxnnSMR0UvhIV7gIlbREZ0pOadmJ_fjP-KJKM5soi3g6uMzIxhK-91Pla_nlqLGWgs6ISAIzWGiWQTejCLWvo662R_dH_jEwG2wfHFFyhGhvrckcjA971hzX9Z0t2Q==)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwtz73WLpBlf4vsk9crr_GjDC4GYQHBlIv6ZSHEwuKutMaSrjZtBa5qoYjvbGdOxUjVtgRA7DCMmiK96_fY_hod8V2nUEvO9YWsRhRLZA1hWCHylm9lqpPTLIzmsIL--UT4o_epu2XhkM05NbfBHRPtqvJXAKQa1UAX_clnToStmfbObV9MMsto-tIhO1qdeVt8RSP_2cV13rYd8Sue4c1nrhXkAGPbSuoT0dlWdYCj3J-cOE_ffJUt6_9ww==)
21. [crisprmedicinenews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVNKfY4Gqqa6cqB7gBsyRR4CsXUqWrk9_X_0LkH8fREmyhX5L0270wdccyxxS9GjbG3idyIMp_3YmsMCfMwLJPzFV1gmZVlQodBNQx6IbCxHppYycLEp6zBb_a4_fUhVSezUVI6b0BTiPmtuQT4mBiiRAPiIdH1y8sEKLhadTqq0RWozb6vjiZdmJs4GBqI6fd0R0n0qtgXRobcyVfZEr0hYmdnmLlssDMIr3RDxTPiqBoCkbbQDLtj3-Sp7UFCQHH1jto5QLad8uKNF4-luMs)
22. [crisprmedicinenews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH25zo3RM0gQxC3twuis17tLZgMAKmYv0H5VE3hANfXUYqaJEHdgM1ZPLHbc5BaBOu2iqPJGXtTnTBUoi4jplxKV0OhmcisBSbxil3BRvPu3WjdCU_TJp1RaS6s3YIQRoUQ6Gp92rICS_fXzHh1x6AIbpmJxPFsctdvHxIy0M5A_4I4vjDUkg==)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcMXK-_ZGCHxCLnVZ9lrKithR-5OwPDZzQsFMzLPkxW1Hricug1Y10RpiaMDOSxx9LXkHR4IlDfHtZDBWoEdIAtm8A81WC7jAp87MT9MW4DUGqpBxzvF3R2SIvQvWuqw==)
24. [bmj.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr6fpjqVfUn4RI6Be-U8ph4TPsgiijOweoyETehn7PfnBon06ONUY-nSxjTCKrLU6ePawHZowOeD09yt1C_txhMf38KxrbTfje0Q7fKxshdrZyNvI7H4CehF3WIu9LIWJe1g==)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHptiu2-TrM-KsH3BIvQBciNTmgIiw-FlaciUUYlFWpdj68ls4ElRZp0KiumtgdCli-o7KGh34Of7iXwj6_yUOl4PuABy-cE8qxUivmgGg9csWQMUTS9HjUcZkc4jQUAg==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc7ZCT_DLvv4XAqQpbTe_mkyFJ9ndVEIFW7-pFsPFdWsUZc2hwIi9lH6LL1FX0YxIl0j7WJzeOWcC_eG77XzbbyHKzgZNyOTjOAP_SIk9VzijHt-UzvYkkFBFLIFJ7me3NxBE2coaJTPO-AYqu8ZH6DOyIzy231P97DeYty0FNkH0sZGEVYfBY71ZALoCn4MWnWKEaVswOns8Hny1AgHTku-pnlmBYt4dGBq-sOnXmD0ZglnLeRk3pK2XYXgLzeV8lHkj7ae1xzputzw77sxUX7w==)
27. [eurekalert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsqtiJxgfRFLcv1JY7jITO3p6Jn1SyMiWM9q0TSgFET07PheEWaxThM9O4uuMr6UqJq_PbJmC8Aru_eUnCgM9--j97qfqPoOlxauQaqr4BqejahLQKkVElQVqB3qquPtsODl7lL7M=)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY5w_U_h0ljVkwxJ86Wm_Kg6nwTt9DG_UDlIUYucPnEnXbRQyQrYw3FduS3XM1Hhy-f9Hh76YcFg7F_8kas6CnC1mGG5FB24hkR1_XsbxSTxwkBA6F0PYqeyY-NA5IAQ==)
29. [asco.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7VobxTk__d1PYXUanebL29uNYrNXxWKvj3yFcVgvwW5zMZKK70bPgHQ3vHLef8bO19NHarBkjID9GoU64xgWIAmKtUFqRHA0_Ct8fSl37tpq-mtZJRxmRcNItxI5h2zt4tJmwn4pUpAc=)
30. [medscape.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExnoLR88OJpjEcJGHchQ77aDb4pG9PTAQ5Utz9h8uIH7ftzDS-bTQkPKfvMpBTj1q-oLoWSWBf-jjIPN5xoRiHFlN4Cem866eVSVmy0Wb5JFUlrcU29xhSdZaFoW5K2SUdGOAPAe8QSRDbHJuPKLiZLc4J1lWMSeBig-AscxKsdFS7sCppjhRL8G7qqn-Q9JGFiQ5yu_NYP5dHqxgr)
31. [vjoncology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElAVJps2ayJzrLobQvXh2pK2cu2z522mB7PSJnBpn9Iu5z7vMUDldON5guhgVhvbE536kOIUXMlxq2_5cazeKCOf6VlWbYIuKkSe7CtNoAUQzz396-cIOtmQ5u_DkyocMbhAlvZVhp1ezM-pJCdEpQfJZ4r0n7F5AtjivyS5HaymtcIRP7rKSi3jRiATbQyGiqvFjObQf_Q9Fq0lrQ9sm1CrCgMBxV-w==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeTbIcPoefDyRO2eAzgiiiq1cqG5hfDpPYGxcSSxuSlBsieN2R_9sNH6edrFW5TsM2tfF2APuW2rTbbvJElfrvj5XSSG1xqakQtOKlpI5s_clJUEBe6ieZqRD98mtrGA==)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyalVvhQAWy_1p8TyedX-2ga9hkvg6-8UsILdPIu48Bi80rFvMHbMFK_PO9TTW3YWju00nTv5rG5abjrwcQHhiH6mCXOP8EQqB4Zt4V1au7jd1XkG64f9FnCdoHxn2KQ==)
34. [gioncologynow.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpzIuASn4DuZOfm3g22TSxi2r7qHWPywOp27dwzE6xl8cFRhZavtyI7_MksAord2nBBkw5FrAbHPO_gs3eh-MtPeMIGCz9XiIV6Ivcod5lAK4XS8HkfJxcjoJalWF824baN-uwpVwtWCkrHv3Go9ZpBArZ8hvakenax-NWnGD3MdYm61I_ECMs_u9k9siWM-qYXqUahW0M8rGs0ZtlnVOGpKz87zVAR8Xv1vNF)
35. [ucdavis.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFodE-i2xhB3fxNnUrLn9pJ4D7XWiw_8vLouHFkyKkgw76umirKzpaiotPRR43Gq1cU4FSWM-kkWx97ktTlksiQ_2-TjM89-0j54GKPbOHIkku_8phvFgSyKUgg8RYVWwQ8sgbFRYuoavoFPjJs5foJzxmj9NZXEmxyhnngnBYK4BKRAEyi9iMtTlbvgJXQqx_sEmnxlBUvwRzjvoT0hETi_6DOqz0lfxkZ0ZhBx3wTrZ-htriboSMo2ne4Zh2urTTZFWUX)
36. [biopharmadive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0Ks0xexMHDqzv7IX_R4evZqAkf6tctUejTD-e0Q-GJKc0awfiNdZi7iLl2i2LiLjSLLH_brFg1o4QfVwDDI7mkO4rUB-6UbOkrHYLxrfW2IPcVmyS7x2P0PmMfvy7CA7pMlLQLGKqJaxKKvidpTs9JoS3ZL1itkSCe9lWFc7Ln-18SQQ024elXSA=)
37. [ovid.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHN8qxOF_IcRPBwUJfkfGiBsejZAKzGfKcww9b19VuIHScY1jWLz_M7GGlQcVc3bJDFaebl10BkTL1wbAteG4KYl_IHIvwNJcvL8hRQJ_mQSIeUldBkr27XchbbbOehmbAImx3byRafMEBZ2oViJZjS4H0lQZ8KdlWaSVYWC7Kblf3yQOtCDXDG-sDsLA2XdBGZPctRPSEgus50xpn0yFCERpsM_wKGVB0bq7rO99E=)
38. [bioworld.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeXqia1PejbpiUjPAawApnMwNo7CMVxY8XMj2majUgY6CWpT8Faqrrjytq6KDgikdxobEaMQrLfnz-JWcvSXaedMVsRb9U7Dsrh2ykQomacY82XLmVAd-qKwbBLdu5pAQFoQFQ1abMT0lPF8qayQ2cJwVbT1h11YuRFaV467fmWBONhnHpzar0dLA-B-XMVma9yqegYwG_t4zl)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdBGM7ahMLzLxeDIgwWjvm6Krl5vz8wVOWSitJFubGFASapCVQTWNhFKp_li4U-v5Pykm8hycPSgC5liho9cu-lkJTVEpB4KDrMmNRNdXsdg6BC7AVr5qcTtOLuCkvxqkA_pCvyqbiWg==)
40. [pharmexec.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZJS5S4uw0nJl5uEyUt8CVq8ZagGbAnbQeY9eRtOaGHZb46ykyJEJkBCC6jxbZNGCGZAYW5NObflWH-F2oe6_zG4TPHwmInHy8qw6sEYECi4nQl12A6BdsBHTpiFLKa4wGvYtmKMCYUaZleDTfZ55s_vSFSZfdhqwXmvtBJmJwSG3aF_EnCP3zhIokKFKWqrIkQpiWhjPA01Ovlwnr0Mpe4GqS7LGxoQ==)
41. [ashpublications.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-koX6ZKSuzA_0ATy9E5oBDjmct_iowgmymtmZFbOtExBOioyrtc6lyjVM88EYzjHsJm1o-pC9yuMetqjo178PHFHZdEAeTgyVlQ7F9kFvXM_4tEl3XTJ7MdmT24NOubP1aJ3Tv_DmlwGfYyGJSD1k8W37J3oc7DewC7YlwtkQV25VztAaDb50gs22W8bnxBuJ4EGdOzZhi7yK6Wqpp7WjzDPZY6mYtsjFo57nUHRt)
42. [appliedcells.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrb1-2mHDuuhjJSwRAyTNx4eXlFlFKkfGjDq744k9wCxZVQcxrFabAClWJ_K4GOZw_Y-uNxWgPbdmIQLlkM9d4tiY_puzYUT_c99-M-er7Gy01SLnXWbkdIR9rcQBYBzBK10h8MSfc8PKmcg==)
43. [allogene.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfL435MLtEZBHp2caUh-GMCdEi4U22lRIvhMCba4uk87zUQ_eYUHEeOPtTQY6QNYiYAgH9-vfIrGCnc4YOtC2lsot8av9jpTQXxW2AFbRhmFyr4rTfTr1Chk4qBrN4yQKOxCUGe97yyoXNcihTORy9LB0btlgygS7_JHU6mvcjZVTHyr3S1wMSZoigBC6yS2QDY1-AxUk-2XI8eL145iCJsNZ0lmKrGrwR51XpeHA=)
44. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHrTci0MhlgpJa0zyb0FaImeOIsj5-eNFkpdtw31Tp4GgIPg2AYh7Xbrz1rbG6fWKlYnsYS6PLNhcigdLQSJB_EobcDvGsmtEAXl3janVmyidYGqscnxpOYX4sEKSl)
45. [cgtlive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFl5cqnWk65A6QnDtn7c1RevzCDqzFLl7aZXiZet0EZ_n65gkOI5c0yu89bDaqxJ29SxKz83l5qFJ0lBjUHnipcPaLw3Ghi4vHf662kmD-SuI4muKcFue4lTYmjwMcYQbf6vLE-D0Rf7bFcbwDg438MetwbdGfrLUZWGovRbLaWdPc4K-sjD2nlWM-q21E=)
46. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIixzPOe1a573roPep2M5S6TIasRM6i0eUivn9-c0Vg4k7Ixet_8gd8_XyH-VVdgZnP6uwCa4INBpNjYAj7q9dZMaJdhfaYbRHOsn82fwk9UNOjPvBH6XFs425rrfOBwxWCO5KINweEg==)
47. [news-medical.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn3CNpaASKM42fKzqMXPaJ1i04GIGAvfo7EV6eWFBofvMXVNsN6zZJnZERhyyMkTX7rCjtoa7TQZ12lWOid402Sr0e04UGDDAyvpZ858hE0SfTyJD219n15jOcJH7VBnco0N5Z10zpDXQASb6CsCyOAKWi0YbRAxnyokEUTuQzODvjZHCVtsogz6Av73zl7sdAsUSm11a-_Q9xToqZ3GCvO3hW44q_CqPPKMaY)
48. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZZEDWa5v15cQq3pbPV-SBqcT0lbJY-aSfFNWcqdoWX0PsZsmuNGScwSMB1-ZHYomF8WmMAE7wUr5D1uvm9xcQbjn_nXAWA9D85rI7xf2bUwiVRnYlmby-qDaN1_XTl0vf9FpcF7vPuiseB12_SKd2ffdOvqoOkvsxaWgPkQ5ltRSmbiB2n1si0an3hfzx)
