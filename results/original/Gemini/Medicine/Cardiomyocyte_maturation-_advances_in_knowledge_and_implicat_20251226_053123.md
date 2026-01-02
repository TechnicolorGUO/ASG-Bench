# Literature Review: Cardiomyocyte maturation- advances in knowledge and implications for regenerative medicine.

*Generated on: 2025-12-26 05:31:23*
*Progress: [12/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Cardiomyocyte_maturation-_advances_in_knowledge_and_implicat_20251226_053123.md*
---

# Cardiomyocyte Maturation: Advances in Knowledge and Implications for Regenerative Medicine

**Key Points**
*   **The Maturation Bottleneck:** While human induced pluripotent stem cells (hiPSCs) can be efficiently differentiated into cardiomyocytes (CMs), these cells typically remain in a fetal-like state, lacking the structural, metabolic, and electrophysiological characteristics of adult heart muscle. This immaturity limits their utility in drug screening and poses arrhythmia risks in regenerative therapies.
*   **Multidimensional Maturation:** True maturation requires synchronous development across multiple axes: a metabolic switch from glycolysis to fatty acid oxidation, structural organization (T-tubules, sarcomere alignment), and electrophysiological refinement (hyperpolarized resting potential).
*   **Recent Breakthroughs (2024-2025):** Significant strides have been made recently, including the development of vascularized cardiac organoids ("vaschamcardioids") that overcome size limitations, and combinatorial protocols integrating metabolic selection, nanopatterning, and electrical stimulation to induce adult-like phenotypes.
*   **Clinical Translation:** Clinical trials (e.g., Heartseed, HELP Therapeutics) are currently evaluating hiPSC-CM spheroids and patches for heart failure. However, engraftment arrhythmia remains a critical safety challenge, currently managed pharmacologically or through improved cell purity.

***

## 1. Introduction

Cardiovascular diseases (CVDs) remain the leading cause of morbidity and mortality globally, necessitating novel therapeutic strategies beyond standard pharmacotherapy and surgical interventions. The adult human heart possesses negligible regenerative capacity; consequently, the loss of cardiomyocytes (CMs) following myocardial infarction (MI) leads to permanent fibrotic scarring and progressive heart failure. The advent of human induced pluripotent stem cell (hiPSC) technology has revolutionized cardiovascular research, offering an unlimited source of patient-specific cardiomyocytes (hiPSC-CMs) for disease modeling, drug discovery, and regenerative medicine [cite: 1, 2].

However, a critical barrier impedes the full translational potential of hiPSC-CMs: their developmental immaturity. Standard differentiation protocols yield CMs that structurally, functionally, and metabolically resemble fetal rather than adult myocardium [cite: 3, 4]. These immature cells exhibit spontaneous automaticity, rely on glycolysis, and lack the force-generating capacity of adult tissue. In regenerative medicine, the transplantation of immature cells carries significant risks of fatal arrhythmias due to poor electromechanical integration [cite: 5, 6]. In drug screening, the fetal phenotype can lead to inaccurate predictions of drug toxicity and efficacy [cite: 7].

This systematic review critically examines the current state of cardiomyocyte maturation. We analyze the biological hallmarks of maturation, trace the historical evolution of differentiation protocols, and detail state-of-the-art bioengineering strategies—including recent 2024-2025 breakthroughs in vascularized organoids and combinatorial stimulation. Finally, we discuss the implications of these advances for clinical trials and identify persistent challenges in the field.

## 2. Key Concepts and Definitions

To evaluate advances in the field, it is essential to define the specific phenotypic distinctions between immature (fetal/hiPSC-derived) and mature (adult) cardiomyocytes. Maturation is not a singular event but a complex, multi-axis developmental process.

### 2.1 Structural Maturation
Adult CMs are large, rod-shaped, and anisotropic (aligned), facilitating directional force generation. They possess a highly organized sarcomeric structure with distinct Z-discs, M-bands, and a high density of mitochondria positioned between myofibrils. A defining feature of adult CMs is the presence of Transverse tubules (T-tubules), invaginations of the sarcolemma that bring L-type calcium channels into proximity with ryanodine receptors (RyRs) on the sarcoplasmic reticulum (SR), ensuring synchronous calcium release [cite: 8, 9]. In contrast, hiPSC-CMs are typically small, rounded, and lack T-tubules, resulting in asynchronous calcium propagation [cite: 1, 10].

### 2.2 Metabolic Maturation
The fetal heart operates in a hypoxic environment and relies primarily on glycolysis. Postnatally, the heart switches to oxidative phosphorylation (OXPHOS), utilizing fatty acids as the primary substrate (60-80% of energy) to sustain the high ATP demands of contraction [cite: 11, 12]. Immature hiPSC-CMs retain a glycolytic profile, possess immature mitochondria with sparse cristae, and exhibit plasticity that allows them to survive hypoxia but limits their contractile efficiency [cite: 13, 14].

### 2.3 Electrophysiological Maturation
Adult ventricular CMs are electrically quiescent (non-pacemaking) with a hyperpolarized resting membrane potential (RMP) of approximately -85 mV, maintained by the inward rectifier potassium current ($I_{K1}$). They exhibit a rapid action potential upstroke driven by voltage-gated sodium channels ($Na_v1.5$). Immature hiPSC-CMs, conversely, often beat spontaneously due to low $I_{K1}$ expression and high pacemaker current ($I_f$), and have a depolarized RMP (-50 to -60 mV), which predisposes them to automaticity and arrhythmias [cite: 15, 16].

**Table 1: Comparison of Immature vs. Mature Cardiomyocyte Phenotypes**

| Feature | Fetal / Immature hiPSC-CM | Adult / Mature CM |
| :--- | :--- | :--- |
| **Morphology** | Small, round/polygonal, isotropic | Large, rod-shaped, anisotropic |
| **Metabolism** | Glycolysis, Lactate | Fatty Acid Oxidation ( $\beta$-oxidation) |
| **Mitochondria** | Perinuclear, sparse cristae | Intermyofibrillar, dense cristae, high volume (30%) |
| **T-Tubules** | Absent | Abundant, organized |
| **Contraction** | Spontaneous, weak force | Quiescent, strong force, positive force-frequency |
| **Calcium Handling** | Trans-sarcolemmal influx | SR release (CICR), synchronized |
| **Resting Potential** | Depolarized (~-60 mV) | Hyperpolarized (~-85 mV) |
| **Proliferation** | Proliferative | Post-mitotic (polyploid) |

*Sources: [cite: 1, 2, 4, 9]*

## 3. Historical Development and Milestones

The trajectory of cardiomyocyte maturation research has evolved from simple differentiation to complex tissue engineering.

*   **2006-2010: The Era of Differentiation:** Following the discovery of iPSCs by Shinya Yamanaka, early protocols focused on efficiency. The "GiWi" protocol (GSK3 inhibition/Wnt inhibition) became the gold standard for producing high-purity CMs [cite: 17]. However, researchers quickly noted that these cells remained arrested at an embryonic stage [cite: 18].
*   **2011-2015: Biophysical and Biochemical Cues:** Research shifted to mimicking the in vivo environment. Studies demonstrated that long-term culture (up to 120 days) improved maturation but was inefficient [cite: 2, 18]. The introduction of triiodothyronine (T3) hormone and substrate stiffness modulation marked the beginning of active maturation strategies [cite: 8, 15].
*   **2016-2020: Metabolic Selection and 3D Engineering:** A pivotal milestone was the development of metabolic selection using lactate-supplemented, glucose-depleted media. This method exploited the metabolic flexibility of CMs to purify cultures while simultaneously driving oxidative metabolism [cite: 19, 20]. Concurrently, Engineered Heart Tissues (EHTs) utilizing pillars for auxotonic load demonstrated that 3D mechanical stress is essential for structural alignment [cite: 21, 22].
*   **2021-Present: Organoids and Combinatorial Protocols:** The field has moved toward "vaschamcardioids" and complex organoids that integrate vascularization and multi-lineage cells (fibroblasts, endothelial cells) to recapitulate the cardiac niche [cite: 23, 24].

## 4. Current State-of-the-Art Methods and Techniques

Current strategies have moved beyond single-factor interventions to combinatorial approaches that simultaneously target metabolism, structure, and electrophysiology.

### 4.1 Metabolic Engineering and Selection
Metabolism is now recognized as a driver, not just a bystander, of maturation.
*   **Fatty Acid Supplementation:** Culturing hiPSC-CMs in media enriched with fatty acids (e.g., palmitate, oleate) and low glucose forces a metabolic switch to $\beta$-oxidation. This "metabolic maturation medium" has been shown to enhance mitochondrial biogenesis, increase contractile force, and upregulate ion channels [cite: 12, 13, 25].
*   **Lactate Selection:** Recent refinements in 2024-2025 have optimized lactate-based purification. By depriving cells of glucose and providing lactate, non-CMs are eliminated, and the surviving CMs exhibit enhanced contractile force and drug responsiveness [cite: 19, 26].
*   **Mechanism:** The metabolic switch inhibits Hypoxia-Inducible Factor 1$\alpha$ (HIF1$\alpha$) and Lactate Dehydrogenase A (LDHA), unlocking the transcriptional programs required for structural maturation [cite: 13, 14].

### 4.2 Biophysical Stimulation
*   **Electrical Pacing:** Chronic electrical stimulation at physiological rates (1-2 Hz) forces hiPSC-CMs to adopt a positive force-frequency relationship, a hallmark of adult myocardium. Pacing promotes the expression of Connexin-43 (Cx43) and improves conduction velocity [cite: 16, 27].
*   **Nanopatterning and Topography:** Culturing cells on grooved substrates or conductive nanomaterials (e.g., carbon nanotubes, graphene) induces anisotropic alignment. A 2025 study by Li et al. demonstrated that combining nanopatterning with electrostimulation and metabolic medium creates a "triad" of stimuli that generates cells with advanced "notch-and-dome" action potentials and aligned sarcomeres [cite: 28, 29].
*   **Conductive Biomaterials:** The incorporation of conductive polymers (e.g., polypyrrole) or silicon nanowires into scaffolds bridges the electrical gap between cells, synchronizing contraction and reducing the threshold for excitation [cite: 1, 30].

### 4.3 Vascularized Cardiac Organoids
A major limitation of 3D spheroids has been the lack of vascularization, leading to necrotic cores in tissues larger than 400 $\mu$m.
*   **Vaschamcardioids (2024):** Yang et al. introduced "vaschamcardioids" (vascularized and chambered cardiac organoids). These are generated by combining hiPSC-derived vascular spheres with cardiomyocytes. They exhibit ~90% spontaneous beating, contain six distinct cell types (including cardiac precursors and fibroblasts), and successfully model cardiac fibrosis and drug toxicity [cite: 23, 24].
*   **Self-Assembling Vascular Networks (2025):** A landmark study published in *Science* by the Stanford group (Abilez, Wu, et al.) utilized a novel chemical recipe to induce co-differentiation of endothelial and smooth muscle cells within heart organoids. These vascularized organoids can grow larger and reach a more mature state than avascular counterparts, potentially enabling surgical implantation [cite: 31, 32].

### 4.4 In Vivo Maturation
Transplantation into a living heart remains the most potent maturation stimulus. Studies in neonatal and adult rat hearts show that engrafted hiPSC-CMs undergo hypertrophy, T-tubule formation, and isoform switching (e.g., TNNI1 to TNNI3) over a period of months [cite: 33, 34]. However, this process is slow and complicated by species mismatches (xenotransplantation) and immune rejection [cite: 35].

## 5. Applications and Case Studies

### 5.1 Regenerative Medicine and Clinical Trials
The ultimate goal of maturation research is heart repair. Several high-profile clinical trials are underway:
*   **Heartseed (Japan):** The "LAPiS" Phase I/II trial utilizes highly purified hiPSC-CM spheroids (HS-001) injected intramyocardially. The spheroid format is designed to improve retention and survival compared to single-cell suspensions. The trial targets severe heart failure and focuses on safety and LVEF improvement [cite: 36, 37, 38].
*   **HELP Therapeutics (China):** This group uses allogeneic hiPSC-CM sheets/patches. Early results suggest tolerability, though efficacy data is still emerging [cite: 36].
*   **BlueRock Therapeutics:** Developing BR-CM01, an allogeneic cell therapy for heart failure, currently in early clinical phases [cite: 36].

### 5.2 Disease Modeling and Drug Screening
Mature hiPSC-CMs are critical for modeling adult-onset diseases.
*   **Arrhythmia Modeling:** Immature cells often fail to model conditions like Long QT Syndrome (LQTS) accurately because they lack the appropriate balance of ion channels. Metabolically matured cells have been shown to better recapitulate the electrophysiological signature of LQT3 and the response to sodium channel blockers [cite: 12, 27].
*   **Cardiotoxicity (CiPA):** The Comprehensive in vitro Proarrhythmia Assay (CiPA) initiative relies on hiPSC-CMs to predict drug safety. Maturation protocols that enhance $I_{K1}$ expression are vital for preventing false positives in toxicity screening [cite: 7, 11].

## 6. Challenges and Open Problems

Despite progress, significant hurdles remain.

### 6.1 Engraftment Arrhythmia (EA)
The most critical safety concern in regenerative medicine is Engraftment Arrhythmia. When hiPSC-CMs are transplanted, they often beat spontaneously at a rate different from the host heart, acting as an ectopic pacemaker.
*   **Mechanism:** EA is linked to the automaticity of immature cells and poor electrical coupling.
*   **Management:** Studies in porcine models show that EA is transient (lasting weeks) and can be managed with a combination of Amiodarone and Ivabradine [cite: 5, 6, 39].
*   **Prevention:** Genetic editing to remove automaticity (e.g., knocking out HCN4) or advanced in vitro maturation prior to implantation are active areas of research [cite: 40].

### 6.2 Vascularization and Scale
While "vaschamcardioids" represent a breakthrough, creating a fully perfused, thick cardiac tissue suitable for human transplantation remains a bioengineering challenge. Current organoids rely on diffusion or primitive vascular networks that may not connect immediately to the host vasculature upon implantation [cite: 31, 41].

### 6.3 Heterogeneity and Standardization
Maturation protocols vary widely between laboratories. The definition of "mature" is often subjective. There is a lack of standardized metrics (e.g., a universal "maturation index") to compare cell lines and protocols [cite: 2, 9]. Furthermore, hiPSC lines exhibit donor-specific variability that affects their differentiation and maturation potential [cite: 12].

## 7. Future Research Directions

1.  **In Vivo-Mimetic Bioreactors:** Future systems must integrate all maturation cues—electrical pacing, mechanical load, and metabolic media—into scalable bioreactors that can produce billions of cells required for human therapy [cite: 42, 43].
2.  **Genetic and Epigenetic Engineering:** Direct manipulation of maturation drivers (e.g., overexpression of *PGC1$\alpha$*, *HOPX*, or *ERR$\gamma$*) or epigenetic modifiers could accelerate the process without long-term culture [cite: 35, 44].
3.  **Immune-Evasion:** To facilitate allogeneic therapy, maturation protocols must be compatible with hypoimmune (universal donor) lines, such as those with HLA knockouts or overexpression of immune-cloaking proteins (e.g., CD47) [cite: 36].
4.  **AI and Machine Learning:** As demonstrated by the Stanford group, AI can be used to optimize differentiation recipes and predict maturation outcomes based on morphological features, accelerating protocol development [cite: 45, 46].

## 8. Conclusion

The field of cardiomyocyte maturation has transitioned from a phase of discovery to one of engineering and translation. We now understand that the immature phenotype of hiPSC-CMs is not an insurmountable defect but a reflection of the absence of physiological cues in standard culture. By reconstructing the developmental niche—through metabolic switching, biophysical stimulation, and 3D vascularized architecture—researchers can now generate cardiac tissues that increasingly resemble the adult human heart.

The recent emergence of vascularized organoids in 2024 and 2025 marks a pivotal step toward creating transplantable tissues that can survive and function in the human body. While challenges regarding arrhythmia and standardization persist, the convergence of developmental biology, stem cell science, and bioengineering brings the promise of true cardiac regeneration closer to reality.

***

## References

[cite: 1] Hasan, A. et al. (2024). "Cardiomyocyte maturation: advances in knowledge and implications for regenerative medicine." *Advanced Healthcare Materials*. [cite: 1]
[cite: 47] Karbassi, E. et al. (2020). "Cardiomyocyte maturation: advances in knowledge and implications for regenerative medicine." *Nature Reviews Cardiology*. [cite: 3, 48]
[cite: 11] Persad, A. & Lopaschuk, G. (2022). "Metabolic maturation of hiPSC-CMs." *Pharmaceuticals*. [cite: 11]
[cite: 49] Sakamoto, T. & Kelly, D.P. (2024). "Transcriptional control of cardiac maturation." *Journal of Molecular and Cellular Cardiology*. [cite: 49]
[cite: 50] Clancy, C.E. & Santana, L.F. (2024). "Advances in induced pluripotent stem cell-derived cardiac myocytes." *The Journal of Physiology*. [cite: 50]
[cite: 2] Ahmed, R.E. et al. (2020). "Current approaches to promote hiPSC-CM maturation." *Frontiers in Cell and Developmental Biology*. [cite: 2, 51]
[cite: 52] Dai, X. et al. (2025). "Long-term culture and metabolic maturation." *Journal of Molecular and Cellular Cardiology*. [cite: 52]
[cite: 10] Jiang, Y. et al. (2020). "Maturation strategies and limitations." *Bioscience Reports*. [cite: 10]
[cite: 35] Guo, Y. & Pu, W.T. (2020). "Cardiomyocyte maturation: new phase in development." *Circulation Research*. [cite: 53, 54]
[cite: 17] Burridge, P.W. et al. (2014). "Chemically defined generation of human cardiomyocytes." *Nature Methods*. [cite: 17]
[cite: 3] Karbassi, E. et al. (2020). "Cardiomyocyte maturation: advances in knowledge and implications for regenerative medicine." *Nature Reviews Cardiology*. [cite: 3]
[cite: 40] Fan, Y. et al. (2021). "Mechanisms driving cardiomyocyte maturation." *Frontiers in Cell and Developmental Biology*. [cite: 40]
[cite: 41] Takeda, M. et al. (2024). "Challenges in cardiac regeneration." *Bioengineering*. [cite: 41]
[cite: 55] Zhao, M. et al. (2020). "Regulation of cardiac proliferation and maturation." *Frontiers in Cell and Developmental Biology*. [cite: 55]
[cite: 4] Yang, X. et al. (2020). "Maturation of human pluripotent stem cell-derived cardiomyocytes." *Nature Reviews Cardiology*. [cite: 4]
[cite: 51] Ahmed, R.E. et al. (2020). "A Brief Review of Current Maturation Methods." *Frontiers in Cell and Developmental Biology*. [cite: 51]
[cite: 56] Yoshida, S. et al. (2019). "Maturation of hiPSC-CMs: A review." *Stem Cells International*. [cite: 56]
[cite: 57] Wu, Q. et al. (2023). "Strategies to improve proliferation and maturation." *Stem Cell Research & Therapy*. [cite: 57]
[cite: 15] Poon, E. et al. (2014). "Structural, metabolic and electrophysiological maturation." *Stem Cell Reports*. [cite: 15]
[cite: 58] Schubert, M. et al. (2023). "Advanced structural, metabolic and electrophysiological maturation." *TU Dresden Research*. [cite: 58]
[cite: 28] Li, W. et al. (2025). "Comprehensive maturation of iPSC-CMs through metabolic, structural and electrical interventions." *Nature Communications*. [cite: 28, 29]
[cite: 59] Rossi, S. et al. (2024). "Practical culture conditions for iCM maturation." *International Journal of Molecular Sciences*. [cite: 59]
[cite: 16] Guo, Y. & Pu, W.T. (2020). "Cardiomyocyte Maturation: New Phase in Development." *Circulation Research*. [cite: 16]
[cite: 8] Parikh, S.S. et al. (2017). "Thyroid and Glucocorticoid Hormones Promote Functional T-Tubule Development." *Circulation Research*. [cite: 8]
[cite: 44] Miki, K. et al. (2021). "ERRgamma enhances cardiac maturation with T-tubule formation." *Nature Communications*. [cite: 44]
[cite: 60] Zhang, J. et al. (2024). "Mechanobiologically Mediated Differentiation." *Bioactive Materials*. [cite: 60]
[cite: 33] Kadota, S. et al. (2017). "In Vivo Maturation of Human Induced Pluripotent Stem Cell-Derived Cardiomyocytes." *Stem Cell Reports*. [cite: 33, 34]
[cite: 34] Kadota, S. et al. (2017). "In Vivo Maturation... in Neonatal and Adult Rat Hearts." *Stem Cell Reports*. [cite: 34]
[cite: 35] Bi, R. et al. (2021). "Maturation of Cardiomyocytes Derived from Human Pluripotent Stem Cells." *Frontiers in Cell and Developmental Biology*. [cite: 35]
[cite: 61] Karbassi, E. et al. (2020). "Cardiomyocyte maturation: advances in knowledge." *Nature Reviews Cardiology*. [cite: 61]
[cite: 57] Wu, Q. et al. (2023). "Strategies to improve proliferation and maturation." *Stem Cell Research & Therapy*. [cite: 57]
[cite: 19] Yoon, H. et al. (2025). "Enhancing Cardiomyocyte Purity through Lactate-Based Metabolic Selection." *ResearchGate*. [cite: 19, 26]
[cite: 59] Rossi, S. et al. (2024). "Metabolic Selection and Maturation." *International Journal of Molecular Sciences*. [cite: 59]
[cite: 26] Yoon, H. et al. (2025). "Lactate-based metabolic selection." *Tissue Engineering and Regenerative Medicine*. [cite: 26]
[cite: 62] Otero, J. et al. (2020). "Lactate enhances cardiac proliferation." *bioRxiv*. [cite: 62]
[cite: 20] Tohyama, S. et al. (2015). "Distinct metabolic flow enables large-scale purification." *Cell Stem Cell*. [cite: 20]
[cite: 63] Liu, Y. et al. (2025). "Vascularized cardiac organoids maturation advances." *Cells*. [cite: 63]
[cite: 23] Yang, J. et al. (2024). "Generation of human vascularized and chambered cardiac organoids (vaschamcardioids)." *Cell Proliferation*. [cite: 23, 24]
[cite: 64] Hoang, P. et al. (2025). "Geometric constraints on cardiac organoids." *Theranostics*. [cite: 64]
[cite: 31] Bai, N. (2025). "Stanford researchers create vascularized mini-organs." *Stanford Medicine News*. [cite: 31]
[cite: 32] Abilez, O.J. et al. (2025). "Vascularized heart and liver organoids." *Science*. [cite: 32, 65]
[cite: 53] Guo, Y. & Pu, W.T. (2020). "Cardiomyocyte maturation: new phase in development." *Circulation Research*. [cite: 53]
[cite: 4] Karbassi, E. et al. (2020). "Cardiomyocyte maturation: advances in knowledge." *Nature Reviews Cardiology*. [cite: 4]
[cite: 66] Martyniak, A. et al. (2024). "Cardiomyocytes Maturation: Cellular and Molecular Mechanisms." *International Journal of Molecular Sciences*. [cite: 66]
[cite: 9] Wheelwright, M. et al. (2021). "Cardiomyocyte Maturation: Derived from Pluripotent Stem Cells." *Frontiers in Cell and Developmental Biology*. [cite: 9]
[cite: 67] Lieu, D.K. et al. (2013). "Maturation phases of hPS-CM." *Stem Cells*. [cite: 67]
[cite: 18] Lundy, S.D. et al. (2013). "Structural and functional maturation of cardiomyocytes." *Stem Cells and Development*. [cite: 18]
[cite: 11] Persad, A. & Lopaschuk, G. (2022). "Metabolic maturation of hiPSC-CMs." *Pharmaceuticals*. [cite: 11]
[cite: 21] Mummery, C.L. et al. (2021). "Engineered Heart Tissues." *Circulation Research*. [cite: 21]
[cite: 22] Zimmermann, W.H. et al. (2025). "Engineered heart tissue history." *Annual Review of Biomedical Engineering*. [cite: 22]
[cite: 68] Cho, S. et al. (2022). "3D culture platforms for cardiac tissue." *International Journal of Molecular Sciences*. [cite: 68]
[cite: 69] Murry, C.E. et al. (2014). "Heart Regeneration with Engineered Myocardial Tissue." *Annual Review of Biomedical Engineering*. [cite: 69]
[cite: 42] Roberts, M. et al. (2023). "Upscaling Engineered Cardiac Tissues." *Bioengineering*. [cite: 42]
[cite: 70] Al-Gharaibeh, A. et al. (2025). "Preclinical Applications of PSC-CMs." *Metabolites*. [cite: 70]
[cite: 5] Nakamura, K. et al. (2021). "Pharmacologic therapy for engraftment arrhythmia." *Stem Cell Reports*. [cite: 5, 39]
[cite: 6] Nakamura, K. et al. (2021). "Engraftment arrhythmia prevention." *bioRxiv*. [cite: 6]
[cite: 39] Nakamura, K. et al. (2021). "Antiarrhythmic drugs prevent EA." *Stem Cell Reports*. [cite: 39]
[cite: 7] Lee, J. et al. (2025). "hiPSC-CMs for drug-induced cardiotoxicity." *International Journal of Molecular Sciences*. [cite: 7]
[cite: 31] Bai, N. (2025). "Heart organoid news." *Stanford Medicine*. [cite: 31]
[cite: 63] Liu, Y. et al. (2025). "Advances in Human Pluripotent Stem Cells." *Cells*. [cite: 63]
[cite: 65] Harris-Kim, M. (2025). "Advancements in stem cell research." *Stanford CVI*. [cite: 65]
[cite: 23] Yang, J. et al. (2024). "Vaschamcardioids." *Cell Proliferation*. [cite: 23]
[cite: 71] KU Leuven. (2024). "Vascularized cardiac organoids on-chip." *Research Portal*. [cite: 71]
[cite: 12] Feyen, D.A.M. et al. (2020). "Metabolic maturation medium." *Nature Communications*. [cite: 12]
[cite: 25] Zhang, J. et al. (2020). "Fatty acid oxidation in hiPSC-CMs." *Cell Reports*. [cite: 25]
[cite: 11] Persad, A. (2022). "Metabolic maturation review." *Pharmaceuticals*. [cite: 11]
[cite: 13] Gentillon, C. et al. (2018). "HIF1a-LDHA axis in metabolic maturation." *Circulation Research*. [cite: 13]
[cite: 14] Gentillon, C. et al. (2018). "Glucose deprivation promotes oxidative phosphorylation." *Circulation Research*. [cite: 14]
[cite: 54] Guo, Y. & Pu, W.T. (2020). "Cardiomyocyte maturation review." *Circulation Research*. [cite: 54]
[cite: 48] Karbassi, E. et al. (2020). "Cardiomyocyte maturation." *Nature Reviews Cardiology*. [cite: 48]
[cite: 3] Karbassi, E. et al. (2020). "Semantic Scholar Entry." [cite: 3]
[cite: 72] Karbassi, E. et al. (2020). "ResearchGate Entry." [cite: 72]
[cite: 73] Martyniak, A. et al. (2024). "Cardiomyocyte Maturation Methods." *International Journal of Molecular Sciences*. [cite: 73]
[cite: 74] Zhang, Y. et al. (2024). "Carbon dots for cardiomyocyte maturation." *Regenerative Medicine*. [cite: 74]
[cite: 43] Sugiura, T. et al. (2025). "Scalable production of iPSC-CMs." *Global Translational Medicine*. [cite: 43, 75]
[cite: 30] Tiron, C.E. et al. (2024). "Nanopatterning and conductive biomaterials." *International Journal of Molecular Sciences*. [cite: 30]
[cite: 27] Matsuo, T. et al. (2025). "Nanopatterning and electrostimulation." *Frontiers in Bioengineering and Biotechnology*. [cite: 27]
[cite: 76] Kim, J. et al. (2025). "Ultra-Tiny Scale Technology." *Small*. [cite: 76]
[cite: 11] Persad, A. (2022). "Metabolic maturation and CiPA." *Pharmaceuticals*. [cite: 11]
[cite: 29] Li, W. et al. (2025). "Comprehensive promotion of iPSC-CM maturation." *Nature Communications*. [cite: 29]
[cite: 24] Yang, J. et al. (2024). "Vaschamcardioids summary." *Cell Proliferation*. [cite: 24]
[cite: 23] Yang, J. et al. (2024). "Vaschamcardioids abstract." *PubMed*. [cite: 23]
[cite: 31] Bai, N. (2025). "Stanford Science paper details." *Stanford Medicine*. [cite: 31]
[cite: 45] Abilez, O.J. et al. (2022). "Micropatterned Organoids." *bioRxiv*. [cite: 45]
[cite: 46] Yang, H. (2025). "Lab News - Vascularized Organoids." *Adam Yang Lab*. [cite: 46]
[cite: 36] PatentVest. (2024). "Cardiac Cell Therapy Landscape." [cite: 36]
[cite: 37] Ye, L. et al. (2021). "First In-human Clinical Trials." *Frontiers in Cardiovascular Medicine*. [cite: 37]
[cite: 38] Sugiura, T. et al. (2024). "Heartseed and HELP trials." *International Journal of Molecular Sciences*. [cite: 38]

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1m7AsJ2l3y6zLPDR05IVy87F78HU8oAh5r7wkmpXwX-3RhIwkKuQ0yz7XGoS3pbZufWfymbeRAEfuyKf69w_BBsQ2fr70G5T7REZUxf0TFs7km3pxGhg_BcTyMXftgw==)
2. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETVU0YfBS3sC-ZuYq7MTZrNO8mVE6nuKPWCeNGY0mUn4Q2Zdiu3GAQnBXnPlsJ_QO3NJITlymcLr2Y9lCzJ1xa2rFQXI0YWjet3yg1faGlQUDgh0XZVykuwOwo_KncFnr_vzAPegkSj-c5RbpbmHMAV8ICH802ZnP8xXsLd2Vi4cIIDOODbR7z1rujxFkquTS3KX61Ksl7oC_FOvd9Ukdd)
3. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeW2OiQ9EXI0kcF4DSgbRc4Q20pXgDc0PmBzMdt66oWEXij-VpvFljIycg5PCJqvEsXmCt_k4MbHvY_DHJWYh9-NtfG43Iensy0K7Opwi-Tb5yAuY0RqLQtUCfskAKASICDTdn7-GS4sJhK9Tec3B5s5fHn_S8-PuKUqKNoiqXlYhMn__NBxBZFB8WGL4wCeK-EQh8XwPvhNBypkJUqFtIhvxeFkkZM9DNNi6uaobrSTgHqy2lUKQEcvterxebZHMoBAwT3wJ8pJIt)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJMXkarNsx0o1YoUfsttdhW6JKfQX_qGFNFC0YCJV2H5_0KON-qQszCpyVnPcCFHr3B5SuNv84nFibTW5nz87DJa3QjmG989fH0vMchmufi7I13FHg2x6MhDa1l0iJaRrR6MUFOrvh)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK7RqROzkQCQFQIy2LW4d_qO1EasO2Q6LNsVw7Q70ndw0oRWzR20vvQ3swKsgODgBZSaLnYnu6nd0UDaTQ9yqg88Zvy2VWlzwrLowqjjdpjWLCBF0jSqblpig35BokICS9tMK_byhar_MUbsd2Z3vlcMPY4ou1uATFeczvU3qYkrD_h2SVHAj0lzrrmmpzLoymthJHQp09ap9KKX_HDxaG5gf7a83HNIvIvOsjFR8IVmBoe1rWWWqoms832Zi0yzlIFMGrRHhb399dtQmD)
6. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtIVqE7VAxx_myIo7Xdhl7sBGxbd4165cFm4PIuijK4OjwTlOybWPdayhBB3QTak7Nyb-NDjO2k3Wi2Sll04uwJywJpE2ANPZBbTqqrQt9wSlGsmTpdZqbjCVqvCPwMiYfEmsQ6M61XEVhPc3dUOlIrA==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyQ1z8dd0Kjj1jv5QnaM_E_L2SjfjYpaCfg1z-Sl9vNRnXgnfH2yjWkfmFyoXIOzl-75InRQdfoDJuuMwMl_27z6zeqCsGhuPy5XD59G2tSiXDN8HF5ST4tk9iMevqvMKNMRCHQJ0u)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcVeJnJdGkcAyiEi1wTjtz78f3dO2B4QE7_PSD-qYfHynAdvQEf5cTEtIcdTy5gU3qe0Q70jB80OUEdgFeojgjE2AHGcTs1D8CNvHWrw4gCBIWQL_bGEKy5q4bq0mvzk3XoHxSc7T2)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUh9a7vInRS-56F1O0PAWSMCBYntr0zFXWvfvObkuoa8GI2Sqqlkd8ZoFfIa93bW__VDoO-u4VvHs3liF2wvikaS9vEkL0aP7-zKkGu6n3zI83oNYIVqe7gEb-TSxADO9v_gI9wV84)
10. [portlandpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKnasOIJRfNtw4vyIJgo57L8JNpHk9vxCq9EkZ7XJ9fkWVaWjRJgOimMDoKEchomLaeHYBKL4VgBvxelyuPBs0ozkvp-On9ivu9wIC8780SZVfNBB9FFZNN-U_BDjvvOLCYy5HRuVG6paEaKpL3I9nqd5ocSRkhNO9bcdznUuKguWOVAhpSEs1uzrsBjiWNVCPykWrytt-kALUKO62F9Lnr9ba_hLt05wzSQ==)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWA0sqaPxbqwMgaMjqkEABl-Cwe-cjvqcqRGzlHcFx-s8il-jVZwwiZu6Q3YiE3VKHxDFwAWYIL6qWddu-UG6-uYEpSCrpFPhqc6p5ipvUIAciIAVAh-8Rovy-URNI)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI30HHmoXt1UqNsROJuBBiyswkHHrQSoghnjlei1dJoafqQ2mv-NAWpqI3FBJKKibNUX1wGZDncu-IxfVbNEbwXHyG-JWeStoEzf06sRD_oT2qjPcGs6mNDGbuHKDRPU9oR8bYNggV4g==)
13. [ahajournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCUbhrl9p2u93KGP-EpwzxsnKjVoswL54c5EYbPGDpVU9p0YhoKM7m4vkYEp869TKNBd9aUhARsR41cJDLIN-XNR8NLxoHQyX2yCq3FrALkNq08dUWmHUf219608TyECcU-I9obqck-LyZFZF9AiH28Sjq)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqhkeCuTTk23fzXT0sfQT8XArl042KtxAnyDUWP0McDcD8TXYfy31cciKmFoEl9CAJ02k1PjDVQuLNwL2addgiDgx9XwWTM0DAopcdyaUF3YJDXAwpdt7EhHKeJ3-RjUlMzxXGk8Fg)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCfCgbWQn3SMP8_fC6cSV-hPgqjEEMjY9tHAXbBOme6uTWbO5EJ4hHP5ZO1Pi72uQiEmAOtlnnvQ3h55tq_AzocJeJWKpPo3Zx32p4kRChuGNEA5QMSjgKVGgAdqSRKkxG0CsdseGC)
16. [ahajournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy0BjdIxWXbzA6z-hHVI_fh72kfMVzasZ4CF7YlMzNFAjExFA6FGSxACwlyJVZ2rGmLreXdvirT-anipsMNSwKYkCcXr_KrVKaGZCmAvySR5HOhqF1mXKpCbf6mfb1Trr-hDyDi5szUf2fyi25qtBr6smv)
17. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG08C0Ro3BDaqp86AfMTiCem1nX5qm30oEcXsGh1r2EYNSThjTNGaj4AzRdgCtT_8H9wh0TdhIEqILGKkUZDmRw7AEncdEXBYVN-4aaigCviqg1ROahFLBkcEcuwNh_jYRQ2IFW0l0NRkAWSKJg)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3lEMADHFR5P53ChQCXoYP69s9F0jEWOHKP18PUy7vNZPGuRjFYFltDcejmpTAcBMiO0iL4_Ghxl17KmBukpgWgaDBIfZBf3eEcybfD1hYN_97eapuo0tTj39QBlElACquR3JE3eOJ)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEYBgN7ILgrlCKhqoUTVkTcJKEPmq0YfLctJvJ6ALkX5cpYyVv923Ww-yRpHCrZqplziTdZ0emyFiY98NFBa9mpr3DxSCMn7E6bhUrLbwC6evKPXibZzvPO3hWHglJXnKnPXjRlVRKkITiWRXW1KQS3vfL7XmF81Wl8u3Ba-Jm7q2VbaC1X4FO-L4OL0hqlHcT6KOS9S_8vzN1RwPw8DFCYuKueGaX0KzlRs0f3Ew7BQ8=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIDrHJle57dZxgiETjsObJNLZyTk5BLGMMoD5OSxZ9x5njVKV9MV1z0yqhmOTDIMS2JgwA_4SEGoLgKfsSi9UeE5IwZKg8NMUT_750QIg6e02QiqV0_n_qDQND9kB0K7JyAqzeh-Om)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz46mWKZMc0QHHoJeJ4cIwCYolAX1e1gUY0RL7KXLlJxgdtF5IDH38vwqnQCVZZv6TIjDeL2f_5OPTc2_0EGhqgGYUZrZR83IABI7rU8baWbjO9BZ5OtH8ZU-r2gWviUk1Iv9LWzZH)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhlIkxGJn1cuZhxcEm9S2KD5uiFbksGXaRtnRqlbpKtJPTkNdupMrTzB-XE5FA9vfPVtIGyBv-IdbO5pYL6LTu9miekAH9glMAEdYvwTX5zlFnKnnj3RhCnWZzYv5cszUs7RTgdqCC)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx4ymTYRx3YNZfsje4sTo74zOVO-Vqkplzaojlnvt5qw7WoBeiHbIKO06UnM3Z3p9drN2Q5VUMwXxjpmTjdpiZPjmjMed6q1Hkjp8eL7EoA9txtN6HOVQYz53D4vaHFw==)
24. [hep.com.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUGb8zVNj3UOvg1EVqdOdeg6z1I3uGlGtx5H5AwLiH2hTwEsASTpTKiQDcsoxMxFNDQMQtWVuvPO_xXg1oJzkVBE2E5ls-pJg0Zsjr7N9-IwDEttHpORMQ-T8ElvjIe1g=)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrsg-JdaWoH-3XunwWUgTg-5fQQ__PqUPXLoAZUGrf5NTBnVs1Ustn9WaKMXUQC5je47H3g6oVxR8S0F42CRUowna7Voy4T-n4VRhkpss9UG-6QPXlylmKPhVP4tHShe8J2MHKImk)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFO1ajr5sUhNHxOcMaE31GTPPYXuEIp4VaposZjzmwGhUmaOMQyC378XVoAxdMfYdPjCAjUzZICjHAOZAkfAVmuzFEArwC01dWN7uP2kXHpisgaDTTZwWTTE1VjMGsjdg==)
27. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9ehh-_HsS_Qhf96H4NUcjNsonR8r-usvTEfRacyqB3RbF3_zb8eqqmyx7kH2KOmBNeod6i9eDgU0yUwWjIXuo_uXqqMEg1spYJS3_GuSgF-3_mcnso0uUADMJJEJsa2WM_4jUAnuA0HrbUitpCw1GEWoSjVRj0bTXYf4uf6iZVBrjVHrQ1EF8Ze5pWKZ8LtcyQtT1Uu0eRMrcD2cieMwuPG_6ww==)
28. [nanion.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLryycOs1xZiTS5HSA1kX0rUEm3mlGvygWgcRT0Qj0syWZPmP8WrSAVZ3tcdJFRpGQ4mhU_1JPuKUgVXjUL58f57rjqeXYFuC9X2m-m_g4ozLnEHHTijf5GFAt_iQ2CSQpB0TjUyWtd_x8TNwDMPAxFUzwLq-priSaAbk2BVX2We12MZzSSEEJVDDb6U45yIFPYDZj23Udnt1LjIjscnnYDq_-fXDSKrAmuU3jst0iLA==)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFenQOFhiFMis5xAVWJFZb6An7gcHWSZT96I6x53XIAcKjwhHdN-rsTe_iax5cV8h4ls7HJMJtpw0cdHGLoB53QF0n2JjM5YQ25Y87e9JVPKHREVyn_yUC-evq2Q5WNlzzCFcybx1e62U23Q9THcSxz1qdp9djB_boyX-xRIrRAj9fZrG2k6MqmSsZgNWbtrLPy6RqAb9ICPhBzEEDHyvmvUVNgmLK9vZy406vo37J2ZSfmg-AMvCHhRa8ywdKCdKp9MS1U60eWW8rx2QdXiwLcT1HuvkUdb4bvjEd3_2Ok63J3)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRP0euNQTnqBVkl0hbDrl--dPdAfOkeSpvTuAGukOtV81GuYiryKTH6EDX7mEcdljtLIOQ1NEVjbpYfDDWMR3RZbExI5EAEcEuQaj2yu1TnUE6BG05uwxEoizv8K4-fRDmmjKltC-olg==)
31. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUYWt61Femaj00MHXv4trui7SipUcxSl1YcJWLbrlIM46Px7ixdZYvVua3Dt-FU5Eyb5yKEoXkjkn9HQX6CkotERWb51Hpq4QqL_eTl5Ll1MYpDnTdHtUMCEC8ShZMxZE7VyKvpZPUecVQR6KkkCQpWghHotF-WBU=)
32. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSTYeeCbTgKEHz25C1KF94M6Kx1Wd0a97qWV-eV5Q5zigazhEzT6nA-RTdast5vL1YrArtwgVqx6JC0C_ZSL2cqV08QpN13UQ41hpiV7bpV47vAc4GbMWvwdJwQQd0aHiIjpYDMc0l3qtc3Mfm5SPHDeslIuK6d_VAy-eQZEeN5hnO9RKSHo3HK_bjlRgFYHhUhpY=)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7F_NCLzhmzUr4PcpzzMYQUZgL6mNsXbgMwYVCyCNhBRySo2wFd-4bJXQc1M_j5Fs03abiu-99vtju3T9CtnV2F543bFGp9jJG73wIaa6GLAasmhM42QiJRHVIE38DZysTVxbhqp22GaZ-Cil2JZUbT_t0nuJMX-de4tqefnVTAoBYVXmAvuWrBKLrTuEfN_pkPUqrKrnurzDA_TG8FtQrFD4eVPJDPBlh7EaxBbhl37N3DG9x0MS61PhzurT1mTF0BFikZvzWrWx3qAxIskU_OVwtR-0Bj5GFY-E=)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEDIVCuJkwpSvPehQZVZdfQnUHuDDMf1Bp0HNkJB5HLYQF5UDJ0Ll2Ou5-h69tD0sa1mhZ1HgmU1_jXcShea9fICyxVQAgnm7mBU3qtrNtCI0vabD14W4YDEov3A0ylF7hUZUOhE3x)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdcWxwcW-oV3bTvLR8dl8CCFjf2nZYUbXdjUZBBLAAr36Q3jXXQodoaRLdoUF_jU4mKZydp5ILBUsH4XRzpi2UEbBnAoU1Zgim7YOLlQRDW2WmD7vCOmcrg088oms82BKInr-IWqh3)
36. [patentvest.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH48r8XvH9NnRiOXgrKQsuqDQ0ivTpRg_ccAklmBe6uV1dyDkhjvaojvCXCjhr00IKEDVhyDqyrqGgmpytvD7qC8WOLBQarZByI1Jj6uZc-rLRxkYXlTJxC1mBBTXXajsb1UvIpvE4RpmMisb3LztGumgtOu3jTfzMkL9mjOcG_5ZuMpLNJG459g-IzEU-K_ZzgCxh0Ek4BKzGWAULOQMbdt7pWnZQm5rpOLPykfUz0)
37. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn13wPpcVLaJvOBua5Sp1WARm52d7rwTCUuerWAkGOUSRQE-hmndAAVRaxvS0BKQPan5Fi2nt8wyhKFRvXh8aJHAC0YcHef5vsAtubW564wgRSv-_iPU-YjgyLPtFlIUjrFL8C7GLKRSx0TNrYn34nNj3rJXNjBOROlzCkeqegEej7x56NYpQEV8tFmZM5oHsoGvI8W1nplfE=)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGay_s6y4HzBtV3JzWs4YXL9Gy5y5stsvLmLaK6u0J12Uhs6890mq97_dgnZplI9KjQz5pSoYhfK3iRFRMN-cv3qJHQU3fAp05tzNHV1MwMsr6At_e52-G3oTiiWlyom5eNO-uAd-42aw==)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEozJ_76teODcFN6idV5H7F5PhSN1zYhli0lksgtHtmNxuE5ALFaosAw6uQbZIBV2ic-lPKkki6JK29JvdnH_3XTaqTLVK4pkvJNShio4mj9tB1QUETvNmgPfKFd_SJ0g==)
40. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8U0OpsYp4Njn6SA4JrqBl2Lm5v21QqCGhGACO_9ylpPoyn5i4t4hHFhh0Ij1iqpUEwwn2Ks9O64cFKGYTYXKXSZaT-4IXJ7W39Pdd7Scz30HSHtQXEuQv5UGaANEm42Qvk0nx7dRaHGUI-TEcHjDGnbFLnEt1Q-B7HYCHIbRFUC3t76Jey3a-wkMzKbpHwa4Jm5tUrg4QlgoNytjLWvfUYg==)
41. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbkozvGTKTIjdc8k55NBnAD5orF7DD2uec_FiiULY5SM4H09c4jHFPnXkg5qGbF0blDqEzVjqzh-1BrBtHiuYKSZ1kHlvxDCO1yLrvBPRZB4kS8nCO24HZaFW18j5K)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH54uOx6Y-OaM2pIReYUyvBhPvz3kbTovFH1esxGigaZJu-BMDTXxE7ly0zLEdRouMbvlZHJMZv8boJia8SwSP9Eh5sAzBArj-jyQ748EkTpzzeo8xAkSiw0_o3p1c=)
43. [accscience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFole1q2Gsky2_ajPOtmz5GaOL6V1GiJnWB69j_RMXql0D9cFmu-n0qYxEFKETxR5-IoP8BQGV3itIgkUtGnJqzR1ylWnbhQjhD_JEBPl6xGPjjk4D7dzVQa3m1JXPzSeWH11lzQEdz7EUL7aDkJUFHd8=)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEte4JDBcTPQIQlQnPdPMp36HfuuxEb2I10Lf2S1f9S0HKY-z-lfgqFIc2kP870YCQhbFO0fGfD8j-6IwWKSeNeMeLrBm0J6PI5rD087hfxjVmHjE2XYuXUCjEVWr3NXw==)
45. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsd1h251Wm7zUJ6ng41mTuhl2G6n3bYASF_DZAwtC1G1ptosv055UX3YbL5e0ce4j2pQniha5iBwJWEAcHhZF_KGsd6Rt1gNQ0kpY4etI9yveTw99xEPP0kV0yzdF6iEM1fUc0w86QJv70ixBy0tgzNOskJeLsd-KInXzZ8BcaWxCzifMD9Z8PaFdNAbXORgNyMtSbD0BSCrbXQnxFkIufS8amoXqw2y1NTe7ICUEj_NzaLnhfnAGBrXXx7FWA88DrzlVlmfYU_MH4)
46. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUsz3P2hT2YYoHEgZkZhFegbCl46iEHq6TFlCDVRWFERHx-xFL526nRB1IpXlVnelQXTgBjfgPBv_nSoICmNvgCo0COktZA_Y5b9pz0j-9NpU9Bf2-_ZyRRvtMWiYJnUvnp1MS)
47. [physiology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKqGvQZwSX0-5E0n0F6XRx72H6wJXaS1jfZsKwurK5WPZMX-rpum1ODpZjFwmWZAdeWniVjDkOsiWeXLsS0JvXgOkiuVycJqKhtTmMISZCJnJv27W_gPJdGM8ynOyE2nHIACDGjypEDNga2B8IFbwjNdj4mca_Loki)
48. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSs6u_iwQ-K8apUJXSiITRmlmQepWRQAAPfb5X6B-5hDPRykDJ0AV9IK9Waw1YIQX9Llf4hg62MixXjMIsKpIPbZIqIWydGHTCJW5R16rdSFquUSkA-AUDOwDu76OvCg==)
49. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCTs9tYLzJXEN9qbhEKVMHL95-kNKHrNKY2QjIKptGLS_08MsR-4-GeynDqaiRPVIs860eVAViMF78NBno2zWf1V2Bam0wVW8hFfLe1pxXPqdJgX0TIWUHhWWGsdI8EA==)
50. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSUSANnSzEXv6t17VB33wVhIac6oRt-1pgJWdXvc_TxX_wuXJzSaLZYIZMD1MsLEdGOgTjJz0SIOpbscpijPspCAVE1OjioLdadf1eHx9Temb-w0V2qEtneMDtPe_DdQ==)
51. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpFTMgwHYOHCWcP6ew-2TOai3-TEoRW1MyCLJmsWNJ4H8Gz_R19zaYQWr5fyxgHLY9kK4MvaqXlpn7O-EZw7wC-fwii8ZycJNwn8RdO2SXlyw11yEj9YdaFhY44jo7X5yvQA1S6pofKpVnGhPPDdV8c7E1uvWb4cyP-pOBaWzH4A31Umazakiu4v10VCYM-eHtYTdDIxrUGbV6o_YPsoZtdLlXBCkEK-cGgumnbtINdeuMYvNdsIxHDV2S2iy1hymVuZnzr-N4GD6K_OEzyJwRL_IZaNVL)
52. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz9N2y8OLbjfIn4P4s3SpIz8zgXP97EH23hULV7GMttJ7MhzuCeMAyxLP0m0nFOpaXDCQyrBxMnjhtS1RwbFcKNGexs_OBSjtjQEPIfYUuLnnMlGHavrH5bsyNFxACC816iND6wNZGpw==)
53. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIXLGpHBD0Hn-W9TqCZXQnh7l1dHXVEZd9lHMmjqdBXdfcsv3amKEKyl-Xib272EB0f0TQ-ljlmchzAN83ErGkCYtm1gHubEEP9Z6MvE01_K_Kzg-4Ss0TtqmbGZXau8SM-8DWeIsR)
54. [ahajournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF6o8GBZAe3d3plbZsd14XIyQYiW44jJP84csr03bAyYBitVqbGJYa_CJsV77wDmZeTxOUezNBP8FoXPljzf4uYt-OJoDvO2s1X8wNn32QkUtnXkxgOz6lz3kNQ-02-8MZJkIW0XTP-I40nKIfwSQmEh5yT2LqPYMk5czXNxkvpDKYrYM-TcVozllL3fP7u9efWuhH)
55. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrPtAXC6WQe9DrxmqwEeNIqKKEZ4sAdQ2eqUoNgfrMCwBQVGEqf4rCzl4LCGy8RrzXGEE6vogARnb3gqkwOBwdtAxYPV_Yyqf8ZnPznhWYJC5keNKO6Z-nY5ktS-T1-bgbbo7pQQLyHGDG67rNHq1y_xu_h7ErycKCf-Ol08Q_7MslUKxUJQ4jHq5vVDUCLm0iQdKTJ-Y6IUG_PLadp-7DNA==)
56. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL5UT21pOFmY3nw-xXg_kAkhrFURYo4Elo_obYvB6UexwP5_IHabOye4ZMshQbWX6hD-ccv840tdkHN2ku6F9Km9uSasFwLE3kTzp39bqgqLnp_JGCJiwyPzjlQNnSU6hwGi5fZK3-)
57. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEej6GGcwQrvNmg1_tArhZD57XZTMHxDxy1HX37ZU9YbqAVmdgswXlDm6WCY00EZrtAe7-SvzLzgM4wflz91vvsWI1hDOfKUGYxDZWD00AEswitI0zDK7mMmet_86QoENq7tRMLp3U20A==)
58. [tu-dresden.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEixtAZkaR9O-gEJTvyywLueEmHaJqk4iXqPeS3Dkeg3Kq28wlZvHbe0J_efNV81JtnMcqOASD3fUWA3dmylyfr_Xhf_sQSaQUphV_xCM55YqrsHaIML_pNCuWLlwnuSTIXpwlb_NCDHoAJ7SWww9fx000XMtJXFAJo8_mCXQAJN7alERHWF-WEko6YfM4lFvmM3QPkWCQvm1tGrC0p0ngWDVDJvRydUje7BnfNIwZ-VCbikbDcyqbfj3YVjguS7yBKhYLK13NuDgD3RQS-7lVurpNKlDjjAtgXB5WnxPyOT7UnGY2fx3EPosrT3roV06QEx0u0HxNFVRY4LcX_hjQz67Gzd_WkMlnbjjYPqo7c8u4=)
59. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQAVI6ZS043cngzCVMt0BmNiO9Jex1HWuolVTwZBU3QiUqP_U2ROwuT88OSdbAAyfFhmRmnnM5dI9YLEvLidE_CCpxwwh_reGAiXv0Nq6Yjko8dmHeSjtQYPBKDM6BNg==)
60. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWXqpaIG53d0k0x-fka5O3w6j8hmJ4N-kjvrWeHaefcSvU_xajyM_2RTXU42LnrPUgAHYDnp2S7a3F-DtYyAtOCfMZdHrxQTDuHgTUn_-m5i-0K1MhyMC0WNQm4oHeBQ3FEDPijyRysQ==)
61. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8hAba9uDiPT4py_f0RkZk6UIcgnvqglW4Uw1uWnGswdh1ZE121po25-ATzKOzSQqB3U6PkoejjIh9LKQFMEPJe1ELK1ACgGzDln20cpbRyleO1AcZxEKvccVJFN0o8RfCALO_Dkv_)
62. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYOv84YWCgA489nLVB7_nrif3-xg0enGXD_0Rblw0OKqnNPNvCC6oWtdfQZc06A-6DEg-fsftQH7agd6bbYAz6EzvgT98x2F_0Iu_Oa1mZM3S77p6tYUvkpK-pq1bH72E9VMeAKcVqSJFv2ekjkUri74YJpQ==)
63. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdpIG42mp4xFqcQDgjIhYdOMo_YXcFM62rOB0hMJoCjY53EtAT9uPSto7cQ8IRuOOg6-gaQzhUEM491NxVe_JfT5YXPhh82L6YeYwJoORPQNbEFg-FE7Ey3mf8)
64. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbwwdfTYdqdVutQoz6IW3949p7WvRNPlTIRFTEJ_a__ianTPlB7F4DlUDK29Z9ufoa8CF-NN7OQHRPBu8N86FeZhNLd8kxwd7G9opFWgFMEKf_M091BnAJ2r60cteAn4IRP_EsKMU4ZQ==)
65. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE36_JiL-ZGB2kfkH2utmDz66gW8u7B97c6XI53YkNuZk3qiUSmgacpmTc8qc3cFa4lTpUqdRMo6GspwaUuZW0Dhi72VGnv3R7zBiFWHw8MzjHf4BMNC5c82nKRDgBG86nnJ5Hzhe_zkYNwn1E5kIuj_3QFq5ah87NztcWbIQ2vp4g3u_RF4o5UCeizKfhiVni6fEeO0ycvgVTb7W40cKqkdkontgoXmm-1vgPJRU3v8Mv-y89fQcFZSVvssOT7qSIRjbgSVPoeWtIWNw==)
66. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeK4nVo6LsrUI2K_kFRR_YbmWOj1S_ZzOni5eA3fUIoOHpZkuzcGiuGqZJTnW-2QuUhct8utTbrENdLinH5JBG02APCQhwG4iSy6_P9jF4SuTIM-FlC8mxcgYxY1EuMeRar0SpRYvdnprGOJfGJgkiJiWeI6WEcFYM3mujrJT75PeP58ub2NUmpuVcn5gOg96IATyahGJ1INg48uOKrrkvvNnc06dJP-58riAuNF9G_Uv1l2eRH6MIofjaCSwHuFarpUwcOOlIvM9Ajw==)
67. [ucdavis.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRB1uf4WM8aO0LB3rmHGV7gLuyUjoNGNLgCyta5znHqM6bac2emOUkcXyC5ndS63mSNkC4MRo5xDJn2d92TgxOutbQR1eAn_dY0lg134cUw3ff0fCBquwkyE73JhBLri3UoNxbaZ97-8xtQ9GnQjWcRfAmdweQp_wBZJs=)
68. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrIus134u-p4bfjQqTcF9Gq83YCiu0rpu_4_iulOpnIvmeyUaUkAn-ZZ6qfJumztRkg7hNqDplRqYPRiP--q5Aw1fjxRO6cXyyI96bITA-nEgZgUc0WAxnaePL5zAWzlxqj1Qt405W)
69. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqjajjJJKiKaGfftqKhwjbvM2wjL9vU-PYM03zQqvjxaJKn4GSXrJ7aftgjBrmtYD76XIVjevb_4fixf2r0CIURCH0wlMDyoSSVvNz92ymqfHid25GT-Jx_cKV9ZkNXrx31uzLTUW57PPjQKvmfcTmTRKT5Appj4c855xgR5aAPXlGfh5Ape201BSvIeM97SKsUUn8ur_qbW40JJi4)
70. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC6OhtHfwx-uac83viLdPxnRefjbubgdCstTnmFYBnjLJqUSQQuDGpD8Fo_u-NahaGWNjRphm0C6D5zNLvmBJno9m9PO_l7t5s7FrfcdjPZj9JGHK2z2JszJFLtkxF)
71. [kuleuven.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJ4KkqhCicayERRPEC1xduf-C8FX8OsSxnFIGQ3cASQNG85DL7oXie0TTu8ECknU6HCoEU88fV30W9rFzN2YjQ7nRKh72Cd7lrSLtA1CrnU7S7qItxoU7TcpZjgQCwhMxthWMRIvVBooxFFtR)
72. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG76p5ZrlZBQLvN1fChS0LQJ4JO6Km99MGWDAOpsFkyGOwEum2Xqvd6mZX4fYWCAwYH9fQCtIInGwFWrgA6UVOAaTY3f2l94V13qX6FDUOntNERyt1Bhk1mZ0KLmrFZPvwgp4bq82kztaxaVi0IjZSA5M6OSi0Q7ruxwmCeBU3J_eWovX_pa9uM5fDlV4GCPWPoWIoriaDD7CIk0JyLwKhSq7G6C5IBArsk0w2J5-AX6mwpgXgKBpHb9Hg0pVV6pcB91i4=)
73. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEReJqaJmc4kzvdHjn_rRM_iVBEP7iG0qyNoIgDygRR8Jb30b02hfY-k2Ix8KgTIAll0p06Qa6xrr4o0c22XSBQIhImfhO3vxsii0UL8vDpmaiop51ZqJfunlPViK_bcuVexgqupxb3Rg==)
74. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXzdSA-kKZO0rRkAOuTqNB-VWdZaqGxC042LgoJl6DguMH3aNI4-GxCmVkejWAXhH9moSY1ckFzKsYaudddA-4YTniH4pdnObt9XEOx95vGN6CXz8AfIBIKCeopeO0rKFED3QZ0MCj_o5Wk9hq8pRDS6_dPqzDI5GDcBKPorSAjmlI8-2LjjlZAvI1YYv2c65rZGg=)
75. [hep.com.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKezaDMsPxx8SSJuC1ROk6AMpU79ANZk-ILnV0oj7rBi83EDgAEH0ayJG-zthxu9FY2U1BElvwIR__5eaag07Q2kyOqbt8wNU92mYTivhSsswqoh7AibuzjrWxi2a2blBTXVMDC--6sSY=)
76. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-lFB7u_zM2YgR4lJMJ3z8fsaZ2juRc1NOSmK8X-Z_po__VeSsKbDTkKmPZ7EJzYrhIeBwIB-Iff6wIYObc8PLRWW12NmPqRts1b5tFrPryG1CScUqiwpKhHZnY6DUNZc7GhglyV93CBBMVszghn17DdRvw9VkUhSeiEJzkC6AALfwzWwRHM-dGitJDAW9xgE8-Cz2VM-KWqTH44GnUIZUs8ttnRbqABuLjpv-VdE=)
