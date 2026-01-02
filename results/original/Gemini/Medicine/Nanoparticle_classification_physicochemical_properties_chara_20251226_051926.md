# Literature Review: Nanoparticle classification, physicochemical properties, characterization, and applications- a comprehensive review for biologists.

*Generated on: 2025-12-26 05:19:26*
*Progress: [11/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Nanoparticle_classification_physicochemical_properties_chara_20251226_051926.md*
---

# Nanoparticle Classification, Physicochemical Properties, Characterization, and Applications: A Comprehensive Review for Biologists

**Abstract**
The convergence of nanotechnology and biology has catalyzed a paradigm shift in medical diagnostics, therapeutics, and biotechnology. Nanoparticles (NPs), defined as particulate dispersions or solid particles with at least one dimension in the size range of 1–100 nm, exhibit unique physicochemical properties that differ significantly from their bulk counterparts. For biologists, understanding these properties—specifically size, shape, surface charge, and surface chemistry—is critical, as they dictate the "biological identity" of the nanoparticle in physiological environments. This systematic review provides a comprehensive overview of nanoparticle classification (organic, inorganic, carbon-based, and biogenic), historical milestones from Faraday’s colloids to mRNA-LNP vaccines, and the state-of-the-art characterization techniques required to validate their synthesis and biological interaction. We critically analyze the formation of the protein corona, a dynamic interface that governs cellular uptake and toxicity, and review key clinical case studies including Doxil®, Abraxane®, and Onpattro®. Finally, we discuss the translational challenges, including the "valley of death" in clinical development, regulatory hurdles, and future directions in personalized nanomedicine.

---

## 1. Introduction

Nanotechnology has emerged as a transdisciplinary field with profound implications for biology and medicine. The ability to manipulate matter at the atomic and molecular scale has enabled the development of materials that can interact with biological systems with unprecedented specificity [cite: 1, 2]. For biologists, nanoparticles (NPs) offer tools for probing cellular machinery, delivering genetic material, and visualizing molecular processes in real-time. However, the successful application of these tools requires a deep understanding of the material science underlying their design and the biological barriers they must negotiate [cite: 3, 4].

The motivation for this review stems from the observation that while the synthesis of nanomaterials is often well-described in chemical literature, the translation of these materials into biological applications is frequently hampered by a lack of rigorous characterization in physiological contexts [cite: 5, 6]. Biologists must navigate a complex landscape of material classifications, characterization methods (e.g., DLS, TEM, XPS), and interaction mechanisms (e.g., protein corona formation, endocytosis). This paper aims to bridge the gap between material science and biology, providing a rigorous yet accessible framework for understanding how physicochemical properties influence biological outcomes.

---

## 2. Historical Development and Milestones

The history of nanotechnology in medicine is not merely a chronicle of modern invention but a continuum of discovery dating back centuries.

### 2.1 Early Foundations
While the term "nanotechnology" was coined by Norio Taniguchi in 1974 [cite: 7, 8], the use of nanomaterials predates modern science. The Lycurgus Cup (4th century AD) and stained glass windows of medieval cathedrals utilized gold and silver nanoparticles to achieve dichroic optical effects, a phenomenon explained much later by Gustav Mie in 1908 [cite: 8, 9].

A pivotal scientific milestone occurred in 1857 when Michael Faraday synthesized the first pure sample of colloidal gold [cite: 7, 10]. Faraday observed that the optical properties of the "ruby fluid" differed from bulk gold, marking the birth of modern colloid chemistry [cite: 11, 12]. He recognized that the color was due to the minute size of the particles, a foundational concept for what is now known as localized surface plasmon resonance (LSPR) [cite: 13].

### 2.2 The Modern Era and Clinical Translation
The conceptual framework for manipulating matter at the atomic scale was famously laid out by Richard Feynman in his 1959 lecture, "There's Plenty of Room at the Bottom" [cite: 7, 8]. However, the realization of nanomedicine began in earnest in the late 20th century:
*   **1965**: Alec Bangham discovered liposomes, spherical lipid vesicles that would become the foundation of drug delivery systems [cite: 7, 14].
*   **1985**: Discovery of fullerenes (C60) by Kroto, Curl, and Smalley, opening the field of carbon nanomaterials [cite: 7, 15].
*   **1995**: **Doxil®** (PEGylated liposomal doxorubicin) became the first FDA-approved nanodrug, revolutionizing cancer chemotherapy by reducing cardiotoxicity [cite: 14, 16, 17].
*   **2005**: **Abraxane®** (albumin-bound paclitaxel) was approved, introducing protein-based nanoparticle platforms that eliminate the need for toxic solvents like Cremophor EL [cite: 18, 19, 20].
*   **2018**: **Onpattro®** (patisiran) became the first FDA-approved siRNA therapeutic, utilizing lipid nanoparticles (LNPs) to silence specific genes in the liver [cite: 21, 22].
*   **2020**: The rapid development and authorization of **COVID-19 mRNA vaccines** (Pfizer-BioNTech and Moderna) demonstrated the global scalability and efficacy of LNP technology, marking a definitive maturity of the field [cite: 23, 24].

---

## 3. Nanoparticle Classification

Nanoparticles are broadly classified based on their chemical composition into inorganic, organic, carbon-based, and biogenic categories. Each class possesses distinct properties suitable for specific biological applications [cite: 1, 25].

### 3.1 Inorganic Nanoparticles
Inorganic NPs include metal and metal oxide particles, known for their robustness and unique optical or magnetic properties.
*   **Metal Nanoparticles**: Gold (AuNPs) and silver (AgNPs) are prominent examples. AuNPs are chemically inert and easily functionalized, making them ideal for imaging and drug delivery [cite: 1, 26]. AgNPs are renowned for their broad-spectrum antimicrobial activity, disrupting bacterial cell walls and generating reactive oxygen species (ROS) [cite: 27, 28].
*   **Metal Oxides**: Zinc oxide (ZnO) and titanium dioxide (TiO2) are widely used in cosmetics and antimicrobials but can induce toxicity via oxidative stress [cite: 25, 29]. Superparamagnetic Iron Oxide Nanoparticles (SPIONs) are crucial for magnetic resonance imaging (MRI) contrast and magnetic hyperthermia therapy [cite: 30, 31].
*   **Quantum Dots (QDs)**: Semiconductor nanocrystals (e.g., CdSe) that exhibit size-tunable fluorescence. While excellent for imaging, their heavy metal core poses toxicity concerns, driving research into carbon-based alternatives [cite: 32, 33].

### 3.2 Organic Nanoparticles
Organic NPs are typically biocompatible and biodegradable, making them the preferred choice for drug delivery.
*   **Liposomes**: Bilayered lipid vesicles capable of encapsulating both hydrophilic (in the core) and hydrophobic (in the bilayer) drugs. They are the most clinically established nanocarriers [cite: 1, 26].
*   **Polymeric Nanoparticles**: Constructed from biodegradable polymers like PLGA or chitosan. They offer controlled release profiles and high stability [cite: 7, 34].
*   **Dendrimers**: Highly branched, tree-like polymers with defined molecular weights. Their surface multivalency allows for the attachment of numerous therapeutic or targeting ligands [cite: 1, 3].
*   **Lipid Nanoparticles (LNPs)**: Distinct from liposomes, LNPs often possess a solid lipid core or complex internal structure. They are the vehicle of choice for nucleic acid delivery (mRNA, siRNA) due to their ability to protect genetic cargo from degradation [cite: 23, 35].

### 3.3 Carbon-Based Nanoparticles
This class includes fullerenes, carbon nanotubes (CNTs), and graphene. They exhibit exceptional mechanical strength and electrical conductivity. CNTs have been explored for crossing biological membranes (acting as "nanoneedles"), though their non-biodegradability and potential for asbestos-like toxicity remain significant hurdles [cite: 1, 36].

### 3.4 Biogenic (Green) Nanoparticles
A growing trend is the "green synthesis" of NPs using biological organisms (bacteria, fungi, plants) as nanofactories. This approach avoids toxic reducing agents used in chemical synthesis. For example, plant extracts containing phenols and terpenoids can reduce metal ions (e.g., Ag+ to Ag0) and simultaneously cap the particles to prevent aggregation [cite: 37, 38, 39].

---

## 4. Physicochemical Properties and Biological Interactions

For a biologist, the physicochemical properties of an NP are not merely static descriptors but dynamic predictors of biological fate.

### 4.1 Size and Surface Area
Size is the primary determinant of biodistribution.
*   **Renal Clearance**: Particles <10 nm are typically cleared rapidly by the kidneys [cite: 36, 40].
*   **RES Uptake**: Particles >100 nm are prone to opsonization and clearance by the reticuloendothelial system (RES) (liver and spleen) [cite: 4].
*   **Optimal Range**: The 10–100 nm range is often cited as optimal for prolonged circulation and tumor accumulation via the Enhanced Permeability and Retention (EPR) effect [cite: 18, 41].
*   **Surface Area**: The high surface-to-volume ratio of NPs increases their reactivity and capacity for drug loading but also enhances the adsorption of biological proteins [cite: 29, 42].

### 4.2 Surface Charge (Zeta Potential)
Surface charge dictates colloidal stability and cellular interaction.
*   **Cationic NPs**: Positively charged particles interact strongly with negatively charged cell membranes, facilitating uptake. However, they can cause membrane disruption and toxicity [cite: 26, 30].
*   **Anionic/Neutral NPs**: Generally exhibit lower toxicity and longer circulation times but may have reduced cellular uptake efficiency [cite: 29, 30].

### 4.3 Hydrophobicity and Hydrophilicity
Hydrophobic particles tend to aggregate in aqueous biological fluids and are rapidly opsonized. Surface modification with hydrophilic polymers, such as Polyethylene Glycol (PEG), creates a hydration layer that repels protein adsorption ("stealth" effect), significantly extending circulation half-life [cite: 40, 43].

### 4.4 The Protein Corona: The Biological Identity
Upon entering a biological fluid (e.g., blood), NPs are instantly coated by a layer of proteins, forming the "protein corona" (PC).
*   **Hard vs. Soft Corona**: The "hard" corona consists of high-affinity proteins (e.g., ApoA-I, fibrinogen) that bind irreversibly, while the "soft" corona comprises loosely bound, rapidly exchanging proteins (e.g., albumin) [cite: 44, 45, 46].
*   **Biological Identity**: Cells "see" the protein corona, not the pristine nanoparticle surface. For instance, the adsorption of Apolipoprotein E (ApoE) on LNPs is crucial for their uptake by hepatocytes via the LDL receptor—a mechanism exploited by Onpattro® [cite: 21, 47].
*   **Vroman Effect**: The composition of the corona evolves over time, with high-abundance proteins initially binding and being replaced by high-affinity proteins [cite: 44, 48].

---

## 5. Characterization Techniques

Rigorous characterization is essential to correlate physicochemical properties with biological effects. A multi-technique approach is recommended [cite: 49, 50].

### 5.1 Visualization and Morphology
*   **Transmission Electron Microscopy (TEM)**: Provides direct visualization of core size and shape at sub-nanometer resolution. Cryo-TEM is essential for preserving the native structure of soft nanomaterials like liposomes and LNPs [cite: 34, 51].
*   **Scanning Electron Microscopy (SEM)**: Offers surface topology information but generally has lower resolution than TEM [cite: 52, 53].
*   **Atomic Force Microscopy (AFM)**: Measures 3D topography and mechanical properties (stiffness) of NPs in fluid environments, avoiding drying artifacts [cite: 50, 51].

### 5.2 Size and Charge Analysis
*   **Dynamic Light Scattering (DLS)**: Measures the hydrodynamic diameter (including the solvation shell/corona) and polydispersity index (PDI). It is rapid but assumes spherical shape and is sensitive to large aggregates [cite: 6, 49].
*   **Nanoparticle Tracking Analysis (NTA)**: Visualizes and tracks individual particles to determine size distribution and concentration, offering better resolution for polydisperse samples than DLS [cite: 6].
*   **Zeta Potential**: Measures the effective surface charge, predicting colloidal stability. Values >±30 mV typically indicate stable suspensions [cite: 49, 53].

### 5.3 Composition and Structure
*   **X-ray Diffraction (XRD)**: Determines crystallinity and phase composition (e.g., confirming Ag0 vs. Ag+ in biogenic synthesis) [cite: 42, 50].
*   **Fourier Transform Infrared Spectroscopy (FTIR)**: Identifies surface functional groups and confirms ligand attachment [cite: 42, 54].
*   **X-ray Photoelectron Spectroscopy (XPS)**: Analyzes elemental composition and oxidation states of the outermost surface layers (~10 nm) [cite: 52, 54].

### 5.4 Protein Corona Analysis
*   **LC-MS/MS**: Liquid chromatography-tandem mass spectrometry is the gold standard for identifying and quantifying the complex mixture of proteins in the hard corona [cite: 31, 47].

---

## 6. Applications and Case Studies

### 6.1 Drug Delivery and Therapeutics
The primary application of NPs in biology is the targeted delivery of therapeutics to overcome biological barriers [cite: 3, 4].

#### Case Study 1: Doxil® (1995)
Doxil represents the first generation of nanomedicines. By encapsulating doxorubicin in a PEGylated liposome (~80-90 nm), the drug's circulation time was extended, and its accumulation in the heart was reduced, mitigating fatal cardiotoxicity. It relies on "passive targeting" via the EPR effect to accumulate in tumors [cite: 16, 17, 55].

#### Case Study 2: Abraxane® (2005)
Abraxane utilizes the body's natural transport pathways. It consists of paclitaxel bound to human albumin nanoparticles (~130 nm). This formulation exploits the gp60 receptor-mediated transport of albumin across endothelial cells (transcytosis) and the binding of albumin to SPARC (Secreted Protein Acidic and Rich in Cysteine) in the tumor matrix, enhancing drug accumulation without toxic solvents [cite: 18, 19, 20].

#### Case Study 3: Onpattro® (2018)
Onpattro (patisiran) treats hereditary transthyretin-mediated amyloidosis. It uses LNPs to deliver siRNA to the liver. The LNP design is sophisticated: ionizable lipids (which are neutral at physiological pH but charged in the acidic endosome) facilitate endosomal escape, while PEG-lipids control particle size and stability. The recruitment of ApoE by the LNP surface in situ directs the particles to hepatocytes [cite: 21, 56].

### 6.2 Vaccines: The COVID-19 Breakthrough
The Pfizer-BioNTech (BNT162b2) and Moderna (mRNA-1273) vaccines utilize LNPs to deliver mRNA encoding the SARS-CoV-2 spike protein.
*   **Structure**: These LNPs contain four key lipids: (1) Ionizable cationic lipid (complexes mRNA), (2) PEGylated lipid (stability), (3) Cholesterol (structural integrity), and (4) Helper phospholipid (DSPC) (bilayer structure) [cite: 23, 24].
*   **Mechanism**: The ionizable lipid is critical; it allows high encapsulation efficiency and promotes fusion with the endosomal membrane to release mRNA into the cytoplasm for translation [cite: 35].

### 6.3 Diagnostics and Imaging
NPs serve as potent contrast agents. SPIONs are used for T2-weighted MRI imaging. Gold nanoparticles are used in lateral flow assays (e.g., home pregnancy tests) and are being developed for photoacoustic imaging due to their plasmonic properties [cite: 26, 30].

---

## 7. Challenges and Open Problems

Despite successes, the field faces significant hurdles, often described as the "valley of death" between benchtop research and clinical approval [cite: 57, 58].

### 7.1 The EPR Effect Controversy
The Enhanced Permeability and Retention (EPR) effect is robust in rodent tumor models but highly heterogeneous in humans. This discrepancy explains why many nanomedicines that succeed in preclinical trials fail in Phase III clinical trials [cite: 16, 43]. Relying solely on passive targeting is increasingly seen as insufficient.

### 7.2 Biological Barriers
NPs must negotiate multiple barriers:
1.  **Opsonization/RES Clearance**: Rapid removal by the liver/spleen [cite: 4].
2.  **Extravasation**: Crossing the endothelial lining [cite: 59].
3.  **Tumor Penetration**: High interstitial fluid pressure in tumors opposes NP diffusion [cite: 59].
4.  **Endosomal Escape**: Many NPs get trapped in lysosomes and degraded before delivering their cargo [cite: 35, 60].

### 7.3 Toxicity and Safety
The same properties that facilitate cellular uptake can induce toxicity.
*   **Oxidative Stress**: Many metal oxide NPs (e.g., TiO2, ZnO) generate ROS, leading to DNA damage and apoptosis [cite: 29, 61].
*   **Lysosomal Dysfunction**: Non-degradable NPs (e.g., CNTs, gold) can accumulate in lysosomes, causing swelling, membrane rupture, and cell death [cite: 60, 62].
*   **Immunotoxicity**: Some NPs can trigger complement activation-related pseudoallergy (CARPA) [cite: 44].

### 7.4 Regulatory and Manufacturing Hurdles
Scale-up of complex nanostructures (like LNPs) is difficult. Ensuring batch-to-batch consistency in size, polydispersity, and drug loading is a major CMC (Chemistry, Manufacturing, and Controls) challenge. Regulatory agencies require rigorous characterization of the "nano" specific properties, which often lack standardized protocols [cite: 63, 64].

---

## 8. Future Research Directions

### 8.1 Active Targeting and Personalized Medicine
Moving beyond passive EPR, future nanomedicines will likely employ active targeting ligands (antibodies, aptamers) tailored to a patient's specific tumor biomarkers (e.g., HER2, folate receptors) [cite: 30, 41].

### 8.2 Biomimetic and Bio-inspired Strategies
"Camouflaging" NPs with cell membranes (e.g., red blood cell or platelet membranes) is a promising strategy to evade the immune system and enhance circulation time naturally [cite: 65, 66].

### 8.3 Theranostics
The integration of diagnostic and therapeutic functions into a single platform (theranostics) allows for real-time monitoring of drug delivery and efficacy. For example, using SPIONs to deliver drugs while monitoring tumor shrinkage via MRI [cite: 25, 30].

### 8.4 Green Nanotechnology
The shift towards biogenic synthesis using plant extracts or bacteria offers a sustainable, non-toxic route for NP production, potentially reducing the environmental footprint of nanomanufacturing [cite: 67, 68].

---

## 9. Conclusion

Nanoparticles have transitioned from theoretical curiosities to indispensable tools in modern biology and medicine. For the biologist, the key to harnessing their potential lies in recognizing that an NP is defined not just by its core material, but by its physicochemical identity in a biological context—its size, charge, and the protein corona it acquires. The clinical success of LNP-based COVID-19 vaccines has validated the safety and efficacy of nanomedicine on a global scale, paving the way for the next generation of targeted therapies. However, overcoming the biological barriers to delivery and ensuring rigorous, standardized characterization remains the central challenge for the field. Future breakthroughs will require continued transdisciplinary collaboration between material scientists, biologists, and clinicians.

---

## 10. References

[cite: 26] Joudeh, N., & Linke, D. (2022). Nanoparticle classification, physicochemical properties, characterization, and applications: a comprehensive review for biologists. *Journal of Nanobiotechnology*, 20(1), 262. [cite: 1, 2]
[cite: 40] Mitchell, M. J., et al. (2021). Engineering precision nanoparticles for drug delivery. *Nature Reviews Drug Discovery*. [cite: 30]
[cite: 30] Baetke, S. C., et al. (2015). Applications of nanoparticles for diagnosis and therapy of cancer. *British Journal of Radiology*. [cite: 30]
[cite: 5] Murdock, R. C., et al. (2008). Characterization of nanomaterial dispersion in biological media. *Toxicological Sciences*. [cite: 5]
[cite: 36] Khanna, P., et al. (2015). Nanotoxicity: An interplay of oxidative stress, inflammation and cell death. *Nanomaterials*. [cite: 36]
[cite: 1] Ealias, A. M., & Saravanakumar, M. P. (2017). A review on the classification, characterisation, synthesis of nanoparticles and their application. *IOP Conference Series*. [cite: 25]
[cite: 2] Faraday, M. (1857). The Bakerian Lecture: Experimental Relations of Gold (and Other Metals) to Light. *Philosophical Transactions of the Royal Society*. [cite: 10, 11]
[cite: 69] Feynman, R. P. (1960). There's plenty of room at the bottom. *Engineering and Science*. [cite: 7, 8]
[cite: 70] Barenholz, Y. (2012). Doxil®—the first FDA-approved nano-drug: lessons learned. *Journal of Controlled Release*. [cite: 16, 17]
[cite: 71] Gradishar, W. J., et al. (2005). Phase III trial of nanoparticle albumin-bound paclitaxel compared with polyethylated castor oil-based paclitaxel in women with metastatic breast cancer. *Journal of Clinical Oncology*. [cite: 18, 20]
[cite: 72] Akinc, A., et al. (2019). The Onpattro story and the clinical translation of nanomedicines containing nucleic acid-based drugs. *Nature Nanotechnology*. [cite: 21, 73]
[cite: 42] Schoenmaker, L., et al. (2021). mRNA-lipid nanoparticle COVID-19 vaccines: Structure and stability. *International Journal of Pharmaceutics*. [cite: 23, 24]
[cite: 6] Cedervall, T., et al. (2007). Understanding the nanoparticle–protein corona using methods to quantify exchange rates and affinities. *PNAS*. [cite: 44]
[cite: 34] Walkey, C. D., et al. (2012). Protein corona fingerprinting predicts the cellular interaction of gold and silver nanoparticles. *ACS Nano*. [cite: 74]
[cite: 49] Vroman, L. (1962). Effect of adsorbed proteins on the wettability of hydrophilic and hydrophobic solids. *Nature*. [cite: 44, 48]
[cite: 25] Nel, A. E., et al. (2009). Understanding biophysicochemical interactions at the nano–bio interface. *Nature Materials*. [cite: 40]
[cite: 75] Stern, S. T., & McNeil, S. E. (2008). Nanotechnology safety concerns revisited. *Toxicological Sciences*. [cite: 60]
[cite: 27] Singh, P., et al. (2016). Biological synthesis of nanoparticles from plants and microorganisms. *Trends in Biotechnology*. [cite: 37, 67]
[cite: 76] Blanco, E., et al. (2015). Principles of nanoparticle design for overcoming biological barriers to drug delivery. *Nature Biotechnology*. [cite: 59, 66]
[cite: 14] Hua, S., et al. (2018). Current trends and challenges in the clinical translation of nanoparticulate nanomedicines. *Frontiers in Pharmacology*. [cite: 77]
[cite: 7] Moghimi, S. M., et al. (2001). Long-circulating and target-specific nanoparticles: theory to practice. *Pharmacological Reviews*. [cite: 4]
[cite: 8] Anselmo, A. C., & Mitragotri, S. (2016). Nanoparticles in the clinic. *Bioengineering & Translational Medicine*. [cite: 58]
[cite: 65] Pinals, R. L., et al. (2020). Protein Corona Composition and Dynamics on Carbon Nanotubes. *Angewandte Chemie*. [cite: 45, 78]
[cite: 79] Lin, P. C., et al. (2014). Techniques for physicochemical characterization of nanomaterials. *Biotechnology Advances*. [cite: 42, 52]
[cite: 57] FDA. (2018). FDA approves first-of-its-kind targeted RNA-based therapy to treat a rare disease. *Press Release*. [cite: 22]

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGes6MkEbZEVAOu9Sh_O2DkIx0dss-6M6O6RKCq-4QLq0G846STuzEOCzyjupFF7gegaOeHPvTjhVZKe9X47-4wYo_02DhsBBUc_VOHUAI7s-jCzecvFQ400RKslW-V6masTfB-YlasjJj6g2TG-45S960lSvib9bh4Lm3ssqn8c-V57u3b-9CDJlZ3CK83AHgvIZwNgWObzboqxkA5xQ8-euG9kf0XfLXylO2UmOTzXszqNYE7rVYf3rmRBp_p1GKO9t-gN7_LXxjrYj-PoYDCqwIxZriUvF0-Z78bcRMOrZOK0op_YWNj)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU5c4E8edwamM3eMK_20cs0wJMvcOvvH0ah0_hGtb4Z6zWh_B99XugBfjjDJxCnhXJCpSRCF1QUKUumt9vyoOEKuU7NSNJq1KlGR1rHCtqdpH_PRFb4IFpw8NPGTpLykPzMSCre74T)
3. [ijsret.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0CQ6xtdBQuXjADgKpS3EZI-PMvn19P4xx65JvK-1Wx40mPZWZ_cafhhr6BiZfnK9rB005963evFHsDOGOkaFg1ZIG8cCLaI1PxYW2X34NmzRYWu2jE0aYaUIwJ-4OtjlnRqohSc1bLgd5EDKbQDeKY-B9m08=)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF23tlu1XMWVirojOCqEbJH35LvsZ78EpHqCSD-zYRiFOGXbEh1gLBJkVnaMPLFofs5BhdFBtEwPlikwbldKlBdJSofoKPxph6RkdbKJFhWQmvWpuT6RcgHWp0eBgYIXZ2ruaoP0QOe)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQz6bczauG-dqNNTFhw2T1FhlZy8jng58MkvGjltVtM9OeEgg-3_N7yuu30eIafDJdfjVGryra4wiZeKY3gdbREch9JpkvqmLQDw76l88qjJg149fnH_doIrOMtaaBZNJyN4ZI8FwK4cfFmUUn1lerWMgMEerddytnlRgRfg2-HG9FBQXbeMcQ-eG9oRAD96vv4bMh-G-w8mNKyZE7y0rUTSh0Ue5rERg7beJVIsJENU6qAByJmOYEsDDok4f-ucn5OARA-d4Gvv5LcH8=)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJxM9tIW8xJeN0vS15cD8zUqDw49gfFFsAcIVRjaJolOu3srcgM01JNBbnf2Du4VuQy21ViJvjHZkaMCG_ZPO-qkmgz7PBaoptypp-WAdzmjrWrQI1PzBumhGOw_ExJHYjcOv-bbWr)
7. [nanomedicine.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuvUZZtMaZZig6BeWiWG6k9AcSf_f7Dh2r-1jhu2BPxPilaQMCoGOWswHWhunoPU-ws2Y1KUukTAkbNT9UOfbRKiTVNpI3vM-LY_s-A3leCyq2sirpbFPRR-ZmBKa9SXZREiuHS62Pi3pEzTwF)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPmMk6-kkSwsYlFOMqYi5thAtTY90_00v9XtHZTNExmmWf2ggx7VafcYN5CXbHcvLxi4zh8k8Rex4jlOfoE7fWhP35svSAMzBAqOSAIrs5Y3t42oJRJvL4Meq6BLkZ5YUHaAiuhziE)
9. [fiveable.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcFIeOU0HSVsloD5_r3iEu9h20KwLTmJiw8iHEw1HLt1woQGcN5rWWTrXuD6PXQAxC88uzb6_CcB07NvrOchnmbusOvZ9NBq1bTmKA1KAy4ZzkdrrJ4kCHEd8qGObwxaKuX_wQZcbqLAnQf7v9FYqJb5RfNkBbzAJhqNcpuigdsVyxLz89DAt_rYxq41WPMpDP14WoodBQZrlJm4G_hhZOH4sXUysDVoawGf6dXG6cbWgnwahjgb23Wy1g)
10. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaKNfwbbW_oyOpCNWSpY3QnHJSNw_H5bbI75ptTmjphAe4Svrd7orZYoOq1rXbiFVgFP05Sj-4nDesnNC4VjfjG55_sBsu3ea_HfBc1wfLHlpg83UJ_fOIoed4q7NJTgPcU2RhJqkX4WndtZPgSlhWc0aqQrtxL1O0p6wBpXrIVqDm7AEyXjIYa4rxdjwf6cMnpSSK72Zzb1MkerWekcolJ8WKoM2kiORulDr8GWMDYLD-4oCByys-GZa2f6awX0Yy7xEyoQ==)
11. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFjycQg9LlzACOPIqXOaFJRpNVaDq4PpGy4TJLZzIROv_d3fpH2UyrQmmwIPFuZNzCQZ-bUns8RPBFLaGZZkmdBnrX3ratl1lDe3DjO2PDpIt6V57fIAwivPRq-h1OjOWwoQ==)
12. [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2VHJgKUzXwb5ZbIeXA7TFIfIPuLA2bq2fBBXY9X3M_XOSmm1trhFvlBh1faMsKHXEboG7JQE0GUcznWFDZOcAyCi4AJTOGDaQAgUvjDF6Mdt252ywZCnd364sK7Xomv251-9rThyNxfPgYfs988Y1UOSLEb7fxM88PS89Olu6XjodXNpSgQw=)
13. [rigb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIdU1YpeeO75VeyZqf_w4Q0uTY7VAcxbqhRtMLkAmVMQpEMiwIR6DMUBNvTzHevLfiUPE5hwezeNU9LdG9dh56gdISut7AtKZzll3DKaghjpYX4qoF2NaXiFUBpOV4d2dw7kqNblYzecaBGdcWVpt9VoA9f9arrDR7ZQ_j982VugUWxNsQ04oyupe6Qw==)
14. [medicaldevice-network.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGZFdX0Kb6cU3JI-VzJmLCBFVVKhgvQxQR8yLbMCftrAzF-Bq2XB6Hw7GJIBgvxrZKCY_QM7HoSBi2StBf5a28M1ahXJ9mPVIrfPrS3X3ACnTLplaX2eOkec4Ml34ddMPQBTKj3fUfeyKWmguJ-O2gwfUU3WMWQb-rJuoyaWzR7A1CK7--rtWZrg==)
15. [accessengineeringlibrary.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQsZTY9rDQqvg7BfDVeVtUU5hUQxiVareZthqoDCN07nQkgE3tSEPUdUM-MVqWbGxyXvD9cw7DQS-b3rfAMevtuuV6MGVQNGoxIATSNH-M9yx_LoTKmvwFH6Ct_N6mW-AnU4-ylAOiVkIfY2pASjdGeKFnYkoANHGM4k225AAcrAmg7uY_6WYZbUzkzyaVag==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbGPBEphftt9lFdDOMjgTO6b2MAItWIebotmp3MPFUM5hKQtKcVgoMRqZWiVauv6KIBIQ8NIFBzQRhty__-mYAAKj85yKhTyYVJ-eXCqlqcLrxlgKBM9zhGHcl_C3vBIJCMIxwwa0YxXylj8t1LT4TX7KOTEciLd4jcBPaUuyUl1P17MMjwlLM4ziFKv8AUGtBtoEZaozoatE6ZGZ9qi_1T516rAUcGtgcCh2E)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8t8LnYdVj5cI7dv-_regEqyC6efkj0Gy06H-HvBDtYtLxST7Tf_6voOnRU0FcpbblvMUFIrxIhCToaj7B_VWfl9J025ctvfe9V9102NfPIzErgHm5zdQztobvmFRR9A==)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgWuFqvrnAxMDcJRS4nsTq_27IuTBTpy-I2CS6XT8tHN-SVgN-fGKenBt3lqGlb-2ql78Rrt6WpHjq0YWnP6ABM2CiVpCF23S9vRxNr720FkUpj4sY37_4cTT2z1nhkHNcgCLnMaD-)
19. [drugs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkX38YWXIf9kdeWYe2r-tEx6nxM0566Cq940Tydt79HB-SR98Eb_zurblcyZS-2GPHK60JwWCGb_vclgZ7JpVs7KuoUOjeeU0__3EPsqYQmmAQ3o0_NoRxn_SLYvuqrHTa)
20. [sec.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSW0HyUwHuN0emSaONpIVH-uEuP2jNEeyvzC9PBJHP2uf6XBAqgwQgOTI6JEkcnml_JiD28RzZC9tdvexMkarDEtZmeUivdojM7PszqTIvzHpxitxAM3jo5bRZ6ykvnHi-37J5Dncuj9FeCoCLVK8QEk6JTXwRijhA2s7psfE6NVwl7Q==)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7dhBtAsLbsLaky9JcpmEweVq-qTEqnKp5kGRZwdp7foTqoeud18fDFVL74yxgXWytQ-Ybfc2-xb5Jd1AlvawjqOeXSIHt_C59W7m1O7uvQt3k81t2IUmwYIfbRhwHZzx_LPYlFEoh)
22. [prnewswire.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvvTbUeR4VZK6agfDqahMx1ncf3ZUarc2sbIR_2XmiVNzbOzmDAmGryEWyh4jhISglnA8sUAUcAs_YePKXIgbJYstZa2vhqgf0k-OIg0Ff5m16IBUR9W1kNh7EKY_jEcdlHD82qPkHuV1teePr5MlfwXKCnlmx5gml0av67tQWThYhOMJ0cvHMulDZr18F0zMr4NEWJ8B0c4tegEI6bOzyIxDc27Pn-BvkiZ799GNV6qFNok-wR4gijHN5IFzdWpA=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4bTMWzv_lmDFNdxebvAL63NVDM0qD-GH7xt9tXSnKWmTc74GTRD_yj6nRazY41AzkV_Re9z8VBCRqIDN9KYRcLsIzNtASF7v5YZ6vWvjHLeNBl78i1d6hedNUUOImNa8jW4IpPOnNgVVEjm5dC96GWCavJi3_lIXSKfshecJRvoghjl8iN1IJP_TrtTTyvuSAFRtNL8o1px296PlH6R8nnH0rJiiSAVVsy9rsNt6qjtKHSRrU0R86z2M=)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlMg8aKRBlmK02pAdi-KJbOMBjTJNUBvWWLFAw10bTIJZq5oRFKD3_VfMNd-cyZ1mCJQfB5-LKtu79hLv24-kpol8afys7Dwk-OEzcKZ_4RECBBFq2_rHEu7l-RFc6ocrQZIrUg0OX)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAkSrYGjA22qSDWjfeFIGppn3y6uRTvaq4ApOGDPhhHRAeopIgopahstRqMT7cBynG8l2LSxWSdGE3OAGlIdsVQ9NtwuZpBSIW7O9_Llxo0kscAMGLJ5kyLV3lxDy_ZA==)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYDYNWvJ6HcOIODXRl_KT6YJ3EUSM7hE0KvtxKT8AtdmUTa5565BK-hx37sKxrOaMQSVmyGZpEZ45_vookLF179_P2fYxdMX0wKtuFPbvH4L0p3krIjsnZgx59Jv7)
27. [gsconlinepress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxQDyxmuJIdquDsGO7mhnYheRz7lLAx7wERwawNDPZyfj8nAhTtFNZ1xbS5zpQwOaArFbaFlNIbtbgziSeZ5_ucg6obyBHnZS6yVhiSbE7b3fiaAg-cNOF_DTKujsXwDpySoii-JNQ9-rDlrxblw30djbh85XBZwrHMISaqYZx7_0HdzkfZfQZ9Q==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgTKT1OxwOYwJ-9rVaFcrELmU11GeFm0d4zvvlDI_Fx4pFbR5t4khdamrECa1YpCx4UPfisjB5KQdc5kKW_7U5xBZbCA83R6gE4VxqFe9PgczZqtRwch3lzbb1iP6ksTLu9Dsrsry0NweyJBkkkWrUQhWMGfJKDaYZs8h2I74SMM3Xf5ivK9wcR4XZh-aV5BeTebm7z5FSJWoHlOstSH65-91FfWFTmbkwD1XtPnNxbW0lmnx-_WVhO4UUMQ==)
29. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEILiFfJy7BpOsUiYlgC9lP2dBNisFM3cmitLiQ5zDhRMxVv9BESpZJtq1LGbTiLLeMTvma4fLDL2uNpaU5u3yCM7zEOdJRMmyikNcLJ37OcJG31vw0SdB6KT72reu-sQ==)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0nieQ6R_1w8mvZNdyhr_9vw3dJADT-Lcyket5-hLaQ4vw7FUio8U6QSoBI2aziyLhwt_hF5gD3JVGGE4wWxvNe-82j095Z7DDTb4zhpqQ3Aw8FJwz02Oe7pkW2RpDSVJg-VHftpS7)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKTQw5TqNk3-qs1P2MwqFiI50i0ddxAMZ867vpDiKfnJIFpAXS6eOkxN1GUCZ6aCcXrgK5qdn4hfEUcla0vAFE93kZBd5Db1PiBqs80l2vKgEG4Ew76GIBTzOPUSRlQlt2SpETucHM)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2hZTBgkqjlvU2kRO92MWte_4jLvMSakDjzCzu6Bk7oiFK19QvbUFL0SJALznrXECIjuX_FsPmPLwCLrBWc-FopUUfEAPuNUVpcAGQUau4H0E0rbsfPjnhSCtAD4OEwwGaT-wKCg5O)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXg8qJYbs-X-apEL4WCAFb4_XUKTHKH8SoafKEknzm952pUs-GiWCQjm5_nXhI3Tzlxe60WcLwVAKmzJzhqC3DjxfN3t_mI4Uj7MPUXeSNaiawnt0_LI9pK-fEZSR5aBtbWZp6psocUkih8FrmhLxzb70ow6vFMKTISNDW7htGHNmGQ4IQIt1ghWMAvul1YnqLSc-akUJ2VMiO4rW5M_fESnkvzzm6IbgWUaceh3ePfuE7r7t-bX8dZK-c2xo=)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7JiQZ1-5iVYqQB4H9KZ_kQybf3zyqzaF5rACPloFR9_ACsEu7ZHBtUPZUZihpdkR150ilYDK_ouxOUWDNdPRABCszNEKtiIA-jfNR0ibeU-DfpYYGl0IwgsSFj--lbdSib-TElb0spK9qXbA_QWqRPZf8Gz2_-ZKCRROvaavKAz4ApE_0tJ-5EzlB_azHad6caTUW7EcG5OyvsZ2gJw==)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIEFCJ_h21PFyGRM-GHGPHBchoooYGFi1L4NlCVyEbZCXlnozvZf8S2fYZBP0tIOhZaWnBh5PNn6sK7Vj1MTux948WNePecDGak9b09C34QJXaUDnwkqBYPH-3fy3DbA==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2tK9D0Btpa9R8N-bJQTf_Z4JZk5DEHucEsQBJwyCF6gIQWLv4VvFbX2RSuE0qTyePxQswtPm2tqPw5UgDpQAHI3ALASHapQOSQCa5rjJCY6OOd5lLyDiJMfSe9H5fqPV1xGbP0z8p)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_h4uat9sRJtzFo_2Xl4h2MqqPUVQKITIQJkBn_pHI8jYw_INF6JfuRjvw0rX_COhkMP_BHsdOHY5Vyd_cLvWKc8P5J85tmRJ1YGXoN95-B62ZNOnNpEe2860xDP5NnxD1K0buLRJj)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWSHXFKPumVo2rflBC0ABULngPXVcp7V9o3P-hQVbxVc0BWTzKVpYo_OVkQGHl7tv1niOi-fbXM-ziNTbKNCIVqAetEAlmBFi66TqCEpy9swliR6p-ZgI6DZLcqTgLhoFufdeUn6_1ptolOZZKTZ8I301_FstEQHkZtTgAGbjUVytftVO8aaBjlqN1w_q8mpgL0BMliebVSKXOz2ktoVWn1it9jTgNIV3Trc0eskNwY40aa0elzbCijeEiel_u_zwlKHIoayj3-ILjiRk=)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGfdY9F1kaGoNQt3uZKKyqu5Ub49jVcEtHi0Sfb3AKjsYssw7LoGCMiHdBjrB4V2E19VmG3l8bqihAnL_k8oCEu-8R2Ayx6nv68Ypu6JnOH-OzGh8RYuJAUnjkXiiuDZ4J9XU2G9Bx)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmp2YwlqxA857U_54KC5_R74s_qmLShqeX3g3YEaev9HrPhazB_a5rzK8fY_hTwncQBq7KI4U5VR5Ou7hHOIgXkzCuKiKrdVox-3P-pe2piW9SqTNS7IcV9_PNkyLsxI0aVFjNOxWc)
41. [symbiosisonlinepublishing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwRmVE7NshtnFc6lkj4AZB6_QZDahZAchZVkQtHW8mMzp1fWEif5xBrDGPGxQnHsNdyhdDbm1CLdb2sUris2vdCIfeRnlEfLRX35Pwhf8en_PZ9OlBGr2ZvVvsubyQT2z4evnbOh9ZXtBb5OWnTTUrcF63Kzxx_tQUjjlFGR-qvosZ4LZQD4LwpD47uzaMnl2FjpZXl-E3W-WtQx4SxDDmmQ==)
42. [ijrrjournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSV2tz-OjEM0Av3OcHBXvU6DiBn4fmcHaia2w-F5FrxrSE6UFkYDZxkKqXJKrFPspi42v9REVojNBHYz3V_uc53DwshZov4psxvoPSzQGMiv3WAF-6s58EloKu5Gjtgflro12w1b9s7w-K7oc75FzakQ5z4Yt8b1c=)
43. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyqMR0xXvYSCllHaM_cKT_kqaNOwWq69a4-vfJuatt5go-ZfRWK3Vu57AGT-Jv2yoGLm1gpJoxQ9xahUZJeYtffCphaLQaiJWyeO7vEqwMDxNNR9pZfiM4HBRlhDlT2YwUbpEUsWtiRhtfmMcNGCQb6iwAp-yjJdrEvKPcM4mS7wU06JSeiNhCiDMh)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfzn22x5s9GhQ3kEp13v08x7b74AtefhoYTgjzpFoMT8gpWsVt8SZTKwDOAJOLk--LXRT55olyAwv30GXSGlZoXKta2hF8W5dtJ2GNicYR_L_rUHHWH3t-GUsYRgYo-DUsFGPm3vWK)
45. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlyPyYBDggFOmT2pyR9KcMzniXelqVOs7yNp4O0GDFWXkM0LyGae5Jauw4_YrHwiLVRyhWc49tQAeIOJg7mm1BB5MXX_ayRbKiKLMsvHcHcsxrVgXT_ZiEVo9Dw85JCcRF1eY4WwoOzQSDa2Hplo6GiQ==)
46. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQZbNz8cB-2JZcZMD-tHpUvSMsn_ZzIHBZda7jS_K4NrAkx68aW9rjYxgUm_ZpC3X_00-WFMJvSzk2NNA8LHkNm18QiMfdxuDdppFkg-IHuOPfWC7yOghhSyr4vxnOBDUFwF4FrJmWQrCmxVyLUz-50OA9Fwv6rw==)
47. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tFAQKXkmx1ewzC00M6_r9jGi1e6Vk9_2GLGuJRyEcE06TBqibXyJrN6EQW2fPKMvRAtIRxWwNXDF0KUizD5F2KsSqNB5N1vQZMFB1SpvFagkHQj_5hFx3O1QzV909A==)
48. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJfN8bMfFlGv-rejZfApZyKaJcOOnPP25t5jKhEUAWQg6yINoHeo62a3QsUDmj3EJpPy9PRzaExw3PlfB_9WPVeaWzvhhoYYKUFdk6oEWclnS0d8ahc-CAHqHNjUsN-InN1qIx3xq7kObaILIhbQ21bzRFdGtLj2UzevIm2ZzLiohbNKjGKzQkVttaxQKTHUUE3DvOx5x5MTh6mUX1rHetwko=)
49. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDkHjo0StsZ7nQAwqGJPYKLZ5RHVrMxbXhBwxSgdwUOODd1O4f8TNXZVgjZAah5Zw7NjWKYwVnhdzhFgq9Nz6qX1zKz-6NiojPTonAiz1Kes2my1YtZqCWVzGSaBBiWJ8gfmjttmjWp1-IyA==)
50. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXxZrGlueuoI4oja0LJoSBU_rbdNoYwxm092aGXw9kp1ZQax28QBTcE4XeYVBFzr99U3jiqXoVapCHSxXc8qlT0mE-8GO46-hjReQ3s0d_uhWrNmdjeIvXkXhn3vRD5Bho6cm1LB0IsK341t3pogzPm1f7hQ==)
51. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2MkQEwDj1I0XvtqLWnhvMFioMkidFJS5wYGdUfzGAH0tH2onIwShN5-tM3fD_epMFC5gu0AnqmSfia0l5fwYmRx-mZoKu1sdUqH9EA1Dix0nN5wx_s-EcRTEZ14mIklt79apH5-M=)
52. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2XszJ_tdwCwFAE60OQqF59jjD81ravdSJhqi6aepLfXHQDX5yyPJqTJUOGEKSo5vG9rYWurHd_7m6nDlwMLGW__cTjK7RH_vEGxEhdvjbYwdct_RFJtmz9JBhY7b8px6t5Zh9S3kgme-fffH9oiLhPv2L6gufyY-oHBhLdq8n9PTgyZKLNz4c1malfWoKnouqllHpv7plfv4pydFuzuq55bXe-SnTUBQDZY_bNA==)
53. [delongamerica.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1SNgMsOe2QPZ11SkV0cZywgUHZmWKKqPPrj3Mxzbu8olxlQmkHhl_kw20qbsYGHdcccS1ja3VBeEkroybwDYFQ_8QXrz1dTNO3uyjOaGO8J46B6bRH1v0etCvw_AiJOuAg7SMaKnKV-EDyPKlgsyTqXXB0K1yXK_WSyLSfdFKE630dJtDEsT2pwQQg8M=)
54. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwOTl2oqCzxtFrT2nNknSNCVYdWcGswU0XI7eh-lhs_-pNooSk7VvSyaeDydXWMHd_6uXHskUdPEiFkw1HG3qxTUTTgYwfCKASjBdyHR0sh9kMo0S3dsH-nZANC6Xz2ImCtRmyaT7h)
55. [huji.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH7UfTpsbATkMitR7SwDInGn9O6hSFvSLEUOGVB6gdp6deCB60kGqoco4ENAeX7iy9LWrToPAZ6mLXYZIQzqTcnV0ZVPjyeBT1UE2Ej0PPa7NPO1JrZCJLU_bnl098Fa0H5nATO_IDVhgknRXXSdD1FRVKaiKEkw_axXtqY8DHKDBbFZ9Frs1TM4R14GMKmOON0n2ulQ==)
56. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKRPxZK-DAmBj1YDF9K0byY9nGZR_cRRymbfaRYkImLI4Dd2lc0sBN4vvV6HvsHGmRrJM_8NmwrIZ8xHLRAnX17W41x-9XKdk0iw8859GdQQC2g4ablsh36SFOG-Xwh5OyeHiy0a9_)
57. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwcz0GZVb1icuWQTx_g7hNkF3SW7f-Me7Nf3T6UUvvyS3q2eVLeJ0u56WFgINKCVhopb8hDD8jp8b7RYgvfJDpZ4Cd5RDMwzbggH6ctrI4yuhGz4Vq35TJb70UU4wDjQ==)
58. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHip6dUdcbi5JMcGZt8plPTqHwPOHC7NTdeExhKfpJ6ifVK13ZHKGAPiKz-77DPEnYmov-wtQa1fdXlh2rTy0RIxTvHf2Rm9LlGaMQQTmrsT1cYYRJK5RMrkqwPCIeH7A==)
59. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvv4wj4en53dr5Rb7G2_cQYnxM6cne5VHF5WScIqgxfmjm75q5licHzYQRtehFZeIqjlosUfPFVMfQKLBqUTkl0b4Nk4KV0__GCoNtHTUcuV_QFq1n2Oml7l7cgKKFkVrBfsdR6xRM)
60. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgs04LlTnoLEIjtzMbqeA0pcFqYERVJ6mn6pNO6ePDO1UDt_5YO9UOKby5XV2AeSNMc5QGxb62gnEFiczl5b2Le9ACPO9OMoLZp_gARQGSqux5rlTMnOFGoIienouma3XKRcS63zDP)
61. [cdc.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5yR_T1YV4l4LJhgoVciO70QDnt0QJGIyaQflQQzqtU6qyCF4kaEx8CWX94dT9aiNBDis5pIkqu6-Pk0pByiTrKeI3I8iIH0mnFRuqSBH4RQ_ktAKvyshiM0fLWYSSa6dyqqw6R8iDR19vAYCR)
62. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPkQISvxgBmiXA_Rj5d3IzDDP09WLwWr7KQN9EW_OYsZ-MjZ01Gu38FPBTD6ebB2MYmxt1kW4bzBKWPHjr9HPcbwAQaf9gA1p6F_z4-5-sJccGqpKKjzT5SlYOhVHxgZueYxOrjFT-7x8r-DtVUCrdn8dVksSl4AI6FvzTT2CbynqTp5w1taIRXc7SfJJM2VJjqDJXznd6S9_c-vicNT19pi7Mzghp0CU9krzp6FDJmbfyCGUXA3jNmDU-KU2K9dcDmYBD7XbatKfpeiTOT3993v6e8FSQpQ==)
63. [diversatechnologies.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqm8Po-gHIOrtCyjTDH89wZEGEjYpah_3oiwHD4zGkTV37pWBQjkvL3X-up07FhCJ-MFCsz6WHIhatHoo4_PaIwVurel2uBMJA5J-1jlnSsi2SwLcc2wWCplFSGCCEnZYE7X0BYDlZtNTrV5Wt09bH12jq5Ij1DxWMwWjcwOktBGrKwFNULGO_oeD2E65CWHKk_XWNRNQJDXustSvAa427)
64. [bio-integration.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDIp9M-RggC8e91UzkbrABcvQv8u5ebI4ODTnzbYFjg1Zxd_1XvQKZ2PzkBJdLSIdSmtwP3JQcqrQ4Fu4_PKJrq49eQMSjVQHnBLAddJr8CVRohWkPKhdJTmvhAS_hP-qjzDJ9wKvEVuBNA6asgUldMkVPjFE2SEy91AMsGg==)
65. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpYr5Es0gqq4ff5MWMCgWH5p7QQKPQZjiB2nZ1LTRUMfyH01-U062cMoyNC3c4pVTbKt-OhcSnL50LUkWmlrCyZggqA8kdVFeISyVMkhduOqoUTUroMVZK3bRifjP7_QPiG4Dvt9bDlymgHfzBWNlnEr1N5LXUnhmVTrtxGIjrETTZNgOqCHAsneZ_Bg0twWfH828_qsWaUUR3IZ-Q37y6tyzkPevgYxOBt_wSvQaLxLm0iSMwuRkTDrLf2xLi3RM=)
66. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHuRcGbZTyJFmatbhLFpPigXc7ktVwgM_0OUPySGLtlLgdek2uh4pCGKDS3w9fFS0KV90zQeFpkj1GJnogsDBg2qimSQcbvNXhiw5UbPbaW0hURSLMYDC0MEHh9VHWAA1AGfGvHwmQOv8mzPj1DtdqQ-ws7WuvSn1OwLnh3n9vIXTvmjLVTDASSmNE14BmqD-adxUfMcaP-9FZGOOzYlZrxcQ=)
67. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5__TrFXJXfhBNh6VLre_nXn9l1q3_fYGs6J8lfZsby38mlNyzf8kQb4IZD2xuSOhTB4dcbQmyTSoASOap7YUJ04FqRWThEWca0X4lBVzTXdyv_4i6WVa6bdkBtKEPQWW35nBlavwt)
68. [dntb.gov.ua](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqFZ-UarZ_rEtCugO3CREYsMgTqUQC2G6nQ-xDbOwjADfI3lxaNpoEJQ2g-JjxSEF6fO-2B1OOMlwedjQwmLK1EeZzdyo124R_eAH9brmXGp5xEQ1k3Ai_7nxtdj2VCUbQ)
69. [ijnrd.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHia02kUa7BwARwq85LH6Ynmq0pEW4Oa-J_0ptxE8DuYzBiywKkkEA28GX_AVlHrdC6iNzAjkqmeYp79cQ3XCUn8om_c9JqEO58ryo15Fxhq1Dra13Dy1Tb0Z9liIj12E3DZQSKFW6hc86mf7_bw==)
70. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErt9wf_Nz7wE2hM7_X2b2OUXwq4JrM6NPfysQaw34t6RAjOGJRoOHqaj-hlutxbZelzBRbhzrqxnhTB1s7GQ4xRXzPoyoCF0PiypQf6ab7D3pK5hoQUtZYFwC0RsMQsw==)
71. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPIGDiDrfXuzic9gwWY0poXEbMzOxFtPQIocA3GFANoMkxAELqE2KTUBrYWCCV82T4JoqojmHSe0dc6nHEmf8tWUyy1ua4I0uFKHzaWOK8tGQ7IhhQAqe5RY2Z66Gdmj2Rwf9yyAtboh_RynsojhHtoaVzM2uAIkoP4-zZtKi1efc8qw4ZFcxJ2lxaF9MhCApG)
72. [espublisher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_LsmHRMT0v5JOAsn4SigT6k9qfxsSwe54TFUwkPdhXdHoGDwIWGmwD5n5ZWXNRlw_mTKaIlGFye8wK1rYmZWwvOitNivZbLvhi9Kz-GYPt1v4EZkpL4qoNsm_CC5hsa-gZm2oLe2JEwlf8VsG0jiB502KnWh9pYx1jxS_DVQNp8-vellGWfGKVYzYYJFN)
73. [bocsci.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsiVoDA1DBtCUhSOSXc8psCo3n7ogiwNxVp_53du9cKvJTbvpP-dmDF6wTuGVK7pRXVRuSa-3SiSm_ie0MZIRwOXrrmoiVTfqUKjEkXJuOGxyIDwQ5TCU-ZWP2AboUu2zd17wyepSp6KYVZQYlngCEgVHK2kLtOAr7sIZXyOPl_4gSJQ==)
74. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjviK87JcSUImxQsc6qz-bG1eQyIVUTgDvPidRfvnPQwBro7tNzFprMsJqNQh3Sz8RKnnQGgc19dtOTJKLAKomY6M1I57_QMafamXXsOIvqnHkL9LwRuTCHAJPVwHqc7dR0-WemBYzR4MHRbgRioQLwHPZ1oFMt7CSxaG4shISUgUoYumTcOg4KrjxjOJ8RYc4_IJCn6U7LI1XQUFEeW208g==)
75. [scientificarchives.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLY_YSNThQka64WjA9kh5RYMd3aDPmtGcxd6rH6aSML6x2oGCa5DROWgBraPVDMCe64CIw2_ijWLGPqhz9-S3kUMRi7qn7WAW2MX64q2s5jSCH7ZQSaB0I_eGBFqqNqJu61eh24B7tusfe7duQAnUM64OqARzK6AFdg-b09W1pEo42cLbrpFB0KVoX7Ma7JJfCkkJ0rybWxcyFijjrtdP5QmBf-xSsPsIOQJfwoQg6C1oKXSxTHvRIL7PKY82Rdx7YdZBydkfKmjkzTP0Fcmp8iHrZ-g==)
76. [rsdjournal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6Ki2yec_h5FBY9nAMPN7YmK4V3onsa1bWQ40HP94hVKwKlVNYbl5tmAyBiMiu-c94InA3maBCcXt_Zo2lawtbHnZ8kC1RTmFi7tbpyYTUqFgUtuKmg59wF2zX6zjTEmJRlKA=)
77. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUe2WjlLGIKV5Hv_w9Fpn5_tIg8M0Z6LFRZvwKN2XZP_78dhioCkzRBjXJ9Pc9kS7vzo-5LsY7qnAKMb2xDgBGz2aZiTkc6fsJBEVDge2wCjcvC3TNXoWZyJJ3OtIh86ynnswzCt03jKeVBw4DDP-MUn_hFFDKM61_sCTbQeNqosU0iRJIQqAD8GpWmZYi)
78. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyz6_7OqjsjAVgoLSn_F_Wn5zlPRFV9u64vLaea_eykWBsXpNWSkYGYyDipdiUVnXiGN4TFtTbihHce9zqUoLxqdcW0ZpnX6qXUGB6gEwut6ECMT-pbBq0mJXmx8hlX-tOHKR67HsYUV8I32SW5vwK)
79. [meegle.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHar6GTbUamy_OMvgD_-jSlz8-Om9oNb3rz015LvEO_Amqhk1qax1JLqu0RHliPebE7aMvySi-VYiadFPMekHrnWMrgUUK45J39Suwd0NggH7SeEE3Fz9UdQqZYS2CioHCtZwNtxK_9R2CzWcbo3qO43s2xmT_Kzr0xRo_qo_zHsg==)
