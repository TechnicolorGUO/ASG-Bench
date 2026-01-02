# Literature Review: Organoids as host models for infection biology – a review of methods.

*Generated on: 2025-12-26 06:12:12*
*Progress: [17/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Organoids_as_host_models_for_infection_biology_a_review_of_m_20251226_061212.md*
---

# Organoids as Host Models for Infection Biology: A Comprehensive Review of Methods

**Abstract**
Infectious diseases remain a primary challenge to global public health, exacerbated by the emergence of novel pathogens and the rise of antimicrobial resistance. Traditional models, such as immortalized cell lines and animal models, often fail to accurately recapitulate human-specific host-pathogen interactions due to a lack of cellular complexity or species-specific differences. The advent of organoid technology—three-dimensional (3D), self-organizing in vitro tissue models derived from stem cells—has revolutionized infection biology. This review provides a comprehensive analysis of the methods utilized to employ organoids as host models. We examine the evolution of infection protocols, ranging from microinjection of 3D cysts to the development of "apical-out" polarity reversal and air-liquid interface (ALI) cultures. We critically evaluate the application of these methods in studying viral (SARS-CoV-2, Zika, Rotavirus), bacterial (*Helicobacter pylori*, *Salmonella*), and parasitic (*Cryptosporidium*, *Toxoplasma*) infections. Finally, we discuss the technological hurdles, including the lack of vascularization and immune components, and outline future directions for complex co-culture systems and organ-on-chip integration.

---

## 1. Introduction

The study of infectious diseases has historically relied on two primary pillars: *in vitro* cell culture using immortalized cell lines (e.g., HeLa, Vero cells) and *in vivo* animal models. While these systems have provided foundational knowledge, they possess inherent limitations. Immortalized cell lines often lack the cellular heterogeneity, polarization, and functional maturity of native tissue, while animal models may not support the replication of human-restricted pathogens or may exhibit divergent immune responses [cite: 1, 2].

Organoids represent a paradigm shift in biomedical research. Defined as 3D structures derived from pluripotent stem cells (PSCs) or adult stem cells (ASCs) that self-organize into organ-specific tissues, organoids recapitulate the histology, genetic signature, and function of their *in vivo* counterparts [cite: 3, 4]. In the context of infection biology, organoids offer a unique platform to study host-pathogen interactions (HPI) in a human-relevant, physiologically active context. They allow for the investigation of tissue tropism, pathogen entry mechanisms, and innate immune responses in primary tissues that were previously inaccessible [cite: 5, 6].

This review aims to systematically categorize and critically analyze the methodological approaches for using organoids in infection biology. We focus specifically on the engineering solutions developed to overcome the topological challenges of infecting 3D structures and the application of these models across diverse pathogen classes.

## 2. Key Concepts and Definitions

To understand the utility of organoids in infection research, several key concepts must be defined:

*   **Organoid:** A 3D construct derived from stem cells (ESCs, iPSCs, or ASCs) that self-organizes to mimic the architecture and function of a specific organ. They contain multiple cell lineages (e.g., enterocytes, goblet cells, Paneth cells in the intestine) [cite: 3].
*   **Cellular Polarity:** Epithelial tissues are polarized, possessing an **apical** surface (facing the lumen/external environment) and a **basolateral** surface (facing the blood supply/stroma). Most pathogens infect via the apical surface. In standard organoid culture (embedded in extracellular matrix), the apical surface faces the closed internal lumen, making infection difficult [cite: 7, 8].
*   **Adult Stem Cells (ASCs) vs. Pluripotent Stem Cells (PSCs):** ASC-derived organoids (e.g., intestinal organoids from crypts) typically represent the epithelium only. PSC-derived organoids (e.g., brain or kidney organoids) often contain mesodermal and ectodermal components, offering higher complexity but greater variability [cite: 4, 9].
*   **Tropism:** The specificity of a pathogen for a particular host tissue or cell type. Organoids are uniquely suited to study tropism due to their cellular heterogeneity [cite: 2].

## 3. Historical Development and Milestones

The field of organoid infection biology has evolved rapidly over the last 15 years.

*   **2009:** Hans Clevers’ laboratory established the first long-term culture of murine intestinal organoids from single Lgr5+ stem cells, demonstrating self-organization into crypt-villus structures [cite: 10, 11].
*   **2011:** Spence et al. generated human intestinal organoids (HIOs) from pluripotent stem cells, introducing a mesenchymal component [cite: 12].
*   **2012:** The first application of organoids for infection biology was reported by Finkbeiner et al., who successfully modeled **Rotavirus** infection in human intestinal organoids. This study demonstrated that organoids could support the replication of clinical viral isolates that were difficult to culture in traditional cell lines [cite: 12, 13].
*   **2013:** Lancaster et al. developed human cerebral organoids, paving the way for neurodevelopmental modeling [cite: 11].
*   **2015-2016:** The **Zika Virus (ZIKV)** outbreak accelerated organoid adoption. Researchers utilized brain organoids to causally link ZIKV infection to microcephaly, a phenotype impossible to model in standard cell lines [cite: 1, 14, 15].
*   **2018:** Heo et al. achieved a major milestone by culturing **Cryptosporidium parvum** in intestinal and lung organoids, completing the parasite's life cycle *in vitro* for the first time [cite: 16].
*   **2020-2022:** The **COVID-19** pandemic solidified organoids as essential tools. Lung, intestine, and kidney organoids were used to determine SARS-CoV-2 tropism, screen drugs, and study the "cytokine storm" [cite: 17, 18, 19].

## 4. Current State-of-the-Art Methods and Techniques

A major challenge in organoid infection is accessing the target cell surface. In standard extracellular matrix (ECM) domes (e.g., Matrigel), epithelial organoids orient with the **basolateral surface facing outward** and the **apical surface facing the enclosed lumen**. Since most pathogens (viruses, bacteria, parasites) attack the apical surface, researchers have developed distinct methods to overcome this topological barrier.

### 4.1 Microinjection
Microinjection was the earliest method used to introduce pathogens into the organoid lumen.
*   **Methodology:** Pathogens are injected directly into the central lumen of the organoid using a microcapillary needle under microscopic guidance [cite: 1, 20].
*   **Advantages:** Maintains the 3D architecture, luminal microenvironment (e.g., hypoxia, concentration of antimicrobial peptides), and cell-cell junctions. It is the most physiologically relevant model for luminal pathogens [cite: 8].
*   **Limitations:** It is labor-intensive, requires specialized equipment, and has low throughput (a skilled researcher can inject ~100 organoids per hour). There is variability in the volume injected [cite: 8, 20].
*   **Key Uses:** *Helicobacter pylori* in gastric organoids [cite: 6]; *Clostridioides difficile* toxin studies [cite: 1].

### 4.2 Organoid Fragmentation and Co-culture
To bypass microinjection, organoids can be mechanically or enzymatically disrupted.
*   **Methodology:** Organoids are sheared to expose the apical surface or dissociated into single cells, mixed with the pathogen, and then re-embedded in ECM to reform. Alternatively, pathogens are added to the media of intact organoids if they target the basolateral surface [cite: 1, 21].
*   **Advantages:** Simple and scalable.
*   **Limitations:** Disruption triggers wound-healing responses that may confound infection data. Re-formation takes time, during which the pathogen may be cleared or overgrow [cite: 20].

### 4.3 Organoid-Derived Monolayers (ODMs)
This method converts 3D organoids into 2D formats.
*   **Methodology:** Organoids are dissociated into single cells and seeded onto Transwell inserts or culture plates coated with ECM. This creates a polarized monolayer with the apical surface facing the supernatant [cite: 2, 21].
*   **Advantages:** Allows easy apical access for pathogens and therapeutics; compatible with high-throughput screening and transepithelial electrical resistance (TEER) measurements to assess barrier function [cite: 22].
*   **Limitations:** Loss of 3D architecture, gradients, and complex tissue geometry (e.g., crypt/villus curvature) [cite: 22].

### 4.4 Apical-Out Organoids (Polarity Reversal)
A breakthrough technique involves reversing the polarity of the organoid so the apical surface faces the culture media.
*   **Methodology:** Organoids are removed from the ECM (Matrigel) and cultured in suspension. In the absence of ECM integrin signaling, the cells spontaneously evert, exposing the apical brush border to the outside [cite: 7, 23].
*   **Advantages:** Combines the accessibility of monolayers with the 3D complexity of organoids. Enables "bath infection" (simply adding pathogen to the media) [cite: 24, 25].
*   **Key Uses:** *Salmonella* invasion studies (Co et al.) [cite: 23]; Respiratory virus screening (Influenza, SARS-CoV-2) [cite: 24, 26].

### 4.5 Air-Liquid Interface (ALI)
Critical for respiratory models.
*   **Methodology:** Stem cells or organoid-derived cells are seeded on a porous membrane. The apical medium is removed, exposing cells to air while the basal side is fed. This drives differentiation into ciliated and mucosecretory cells [cite: 27, 28].
*   **Advantages:** Mimics the lung/nasal environment; essential for airborne pathogens and mucociliary clearance studies [cite: 18].

### 4.6 Organ-on-Chip (OoC)
Integration of organoids with microfluidics.
*   **Methodology:** Organoid-derived cells are cultured in microfluidic channels that apply shear stress and mechanical strain (mimicking peristalsis or breathing) [cite: 29, 30].
*   **Advantages:** Introduces physical forces that influence pathogen adherence and host response; allows perfusion of immune cells [cite: 31].

## 5. Applications and Case Studies

### 5.1 Viral Infections
*   **Zika Virus (ZIKV) and Brain Organoids:**
    During the 2015 ZIKV epidemic, brain organoids were pivotal. Studies by Qian et al. and others demonstrated that ZIKV preferentially infects neural progenitor cells (NPCs), leading to cell death and reduced organoid size, effectively modeling **microcephaly** *in vitro*. This link could not be established in mice, which are generally resistant to ZIKV [cite: 14, 15, 32].
*   **SARS-CoV-2 and Multi-Organ Tropism:**
    Organoids confirmed that SARS-CoV-2 infects not just the lungs (via ALI models showing infection of ciliated cells) but also the intestine, kidney, and liver. Intestinal organoids revealed that enterocytes are a site of active viral replication, explaining gastrointestinal symptoms in COVID-19 patients [cite: 17, 19, 28].
*   **Rotavirus and Norovirus:**
    Before organoids, Human Norovirus (HuNoV) could not be cultured in the lab. Ettayebi et al. (2016) and Finkbeiner et al. (2012) used intestinal organoids to successfully culture these pathogens, identifying specific histo-blood group antigens (HBGAs) required for infection [cite: 12, 33].

### 5.2 Bacterial Infections
*   **Helicobacter pylori and Gastric Organoids:**
    Bartfeld et al. and others utilized gastric organoids to study *H. pylori* pathogenesis. They discovered that the bacterial virulence factor **CagA** interacts with the host receptor **c-Met**, triggering epithelial proliferation and potential carcinogenesis. This interaction relies on the 3D architecture and specific gastric lineages found in organoids [cite: 6, 34, 35].
*   **Salmonella and Polarity:**
    Using apical-out organoids, Co et al. demonstrated that *Salmonella* Typhimurium preferentially invades the apical surface, inducing cytoskeletal rearrangements. This model allowed for the visualization of bacterial entry in real-time without the artifacts of microinjection [cite: 8, 23].

### 5.3 Parasitic Infections
*   **Cryptosporidium:**
    Heo et al. (2018) established a landmark model where *C. parvum* completed its entire life cycle in human intestinal and lung organoids. This was a significant advance over cancer cell lines, which only supported asexual stages, allowing for the study of sexual differentiation and oocyst production [cite: 16].
*   **Toxoplasma gondii:**
    Brain organoids have been used to model *T. gondii* infection, showing preferential infection of neurons and glia, cyst formation, and distinct transcriptomic changes (e.g., type I interferon response) that mimic human toxoplasmosis [cite: 36, 37].

## 6. Challenges and Open Problems

Despite their success, organoid models face significant limitations:

1.  **Lack of Immune System:** Most organoids consist solely of epithelial cells. They lack resident immune cells (macrophages, T cells) crucial for mounting a complete response to infection. While co-culture methods are emerging (e.g., adding macrophages to lung organoids), they are not yet standard [cite: 38, 39].
2.  **Absence of Vasculature:** Organoids rely on diffusion for nutrients, limiting their size and preventing the study of hematogenous dissemination of pathogens. Necrotic cores often form in the center of large organoids [cite: 40, 41].
3.  **Variability and Standardization:** There is significant batch-to-batch variability in organoid generation, especially with iPSC-derived models. This makes high-throughput screening and reproducibility difficult [cite: 42, 43].
4.  **Complexity of Infection Protocols:** Techniques like microinjection are technically demanding and difficult to scale for pharmaceutical screening [cite: 20].
5.  **Incomplete Maturation:** Some organoids (especially fetal-derived or iPSC-derived) resemble fetal tissue rather than adult tissue, which may alter susceptibility to pathogens [cite: 6].

## 7. Future Research Directions

The next generation of organoid models aims to address these complexity gaps:

*   **Co-culture Systems (Assembloids):** Researchers are developing "assembloids" by combining epithelial organoids with immune cells, fibroblasts, and neural cells to create a complex tumor/infection microenvironment [cite: 38, 44]. For example, incorporating microglia into brain organoids to study neuroinflammation in viral infections.
*   **Vascularization:** Strategies include co-culturing with endothelial cells, 3D bioprinting vascular channels, or *in vivo* transplantation into mice to recruit host vessels [cite: 41, 45].
*   **Organ-on-Chip Integration:** Combining organoids with microfluidics (e.g., Emulate chips) allows for the introduction of flow, shear stress, and circulating immune cells, creating a "body-on-a-chip" simulation [cite: 29, 30].
*   **Standardization and Biobanking:** Efforts are underway to create standardized protocols and large biobanks of patient-derived organoids (PDOs) to capture genetic diversity in host susceptibility [cite: 46, 47].
*   **High-Throughput Screening:** Adapting apical-out and monolayer formats for robotic handling to screen antiviral and antimicrobial drugs [cite: 24, 48].

## 8. Conclusion

Organoids have firmly established themselves as indispensable tools in infection biology, bridging the gap between reductionist cell lines and complex animal models. By recapitulating the cellular heterogeneity, architecture, and physiology of human tissues, they have enabled breakthroughs in understanding pathogens ranging from Zika virus to *Cryptosporidium*.

While challenges regarding immune integration, vascularization, and standardization remain, rapid methodological advancements—such as polarity reversal and organ-on-chip technologies—are steadily overcoming these barriers. As these models increase in complexity, they promise to accelerate the discovery of host-directed therapies and personalized treatments for infectious diseases.

## 9. References

[cite: 1] Bartfeld, S. (2021). Organoids as host models for infection biology – a review of methods. *Experimental & Molecular Medicine*, 53(10), 1471-1482. [cite: 1, 5]
[cite: 2] Pauzuolis, M., et al. (2024). Organoids in infection research: current state and future perspectives. *Frontiers in Cellular and Infection Microbiology*. [cite: 2]
[cite: 20] Aguilar, C., et al. (2021). Organoids as host models for infection biology - a review of methods. *Exp Mol Med*. [cite: 20]
[cite: 5] Bartfeld, S., et al. (2021). Organoids as host models for infection biology. *Exp Mol Med*. [cite: 5]
[cite: 6] Blutt, S. E., & Estes, M. K. (2022). Organoid Models for Infectious Disease. *Annual Review of Medicine*, 73, 167-182. [cite: 6, 49]
[cite: 17] Snyder, E. (2020). The Future of Organoids in Infectious Diseases. *Corning Life Sciences*. [cite: 17]
[cite: 9] Hill, D. R., et al. (2024). Stem cell-derived human intestinal organoids as an infection model. *American Journal of Physiology*. [cite: 9]
[cite: 10] Sato, T., et al. (2009). Single Lgr5 stem cells build crypt-villus structures in vitro without a mesenchymal niche. *Nature*. [cite: 10]
[cite: 11] Clevers, H. (2016). Modeling Development and Disease with Organoids. *Cell*. [cite: 11]
[cite: 3] Wikipedia. (2024). Organoid. [cite: 3]
[cite: 4] Sino Biological. (2024). History of Organoids. [cite: 4]
[cite: 7] Co, J. Y., et al. (2021). Controlling the polarity of human gastrointestinal organoids to investigate epithelial biology and infectious diseases. *Nature Protocols*. [cite: 7, 23]
[cite: 26] StemCell Technologies. (2024). Apical-Out Airway Organoids. [cite: 26]
[cite: 24] Stroulios, G., et al. (2022). Apical-out airway organoids as a platform for studying viral infections. *Scientific Reports*. [cite: 24]
[cite: 50] Kramer, P., et al. (2023). Apical-out airway organoids and airway immune co-cultures. *ATS Journals*. [cite: 50]
[cite: 27] Jackson Laboratory. (2023). Protocol for primary human lung organoid-derived air-liquid interface. [cite: 27]
[cite: 48] Han, Y., et al. (2022). Organoid models for SARS-CoV-2 infection. *PMC*. [cite: 48]
[cite: 28] Toptan, T., et al. (2023). Organoid Models of SARS-CoV-2. *MDPI*. [cite: 28]
[cite: 18] Gamage, A. M., et al. (2022). Infection of human nasal epithelial cells with SARS-CoV-2. *PMC*. [cite: 18]
[cite: 14] Qian, X., et al. (2017). Modelling Zika virus infection of the developing human brain. *JoVE*. [cite: 14]
[cite: 38] Bar-Ephraim, Y. E., et al. (2024). Modelling disease with organoid and immune cell co-cultures. *PMC*. [cite: 38]
[cite: 39] Jovic, D., et al. (2022). Co-culture of murine small intestine epithelial organoids with innate lymphoid cells. *JoVE*. [cite: 39]
[cite: 8] Wilson, S. S., et al. (2021). Using organoids to study bacterial pathogenesis. *PMC*. [cite: 8]
[cite: 22] Wang, Y., et al. (2018). Enteroids and intestinal organoids for studying Salmonella infection. *PMC*. [cite: 22]
[cite: 29] Emulate Bio. (2024). Infectious Disease Application: Organ-on-a-Chip. [cite: 29]
[cite: 31] Dynamic42. (2024). Exploring infectious diseases with organ-on-chip. [cite: 31]
[cite: 30] Bein, A., et al. (2018). Microfluidic Organ-on-a-Chip Models of Human Intestine. *PMC*. [cite: 30]
[cite: 19] Zhang, M., et al. (2021). Human Organoids and Organs-on-Chips for Addressing COVID-19 Challenges. *ResearchGate*. [cite: 19]
[cite: 36] Seo, H. H., et al. (2020). Modelling Toxoplasma gondii infection in human cerebral organoids. *Emerging Microbes & Infections*. [cite: 36]
[cite: 37] Lee, J., et al. (2020). Toxoplasma gondii infection in human brain organoids. *PMC*. [cite: 37]
[cite: 16] Heo, I., et al. (2018). Modelling Cryptosporidium infection in human small intestinal and lung organoids. *Nature Microbiology*. [cite: 16]
[cite: 42] Blutt, S. E., & Estes, M. K. (2022). Standardization of organoid protocols. *Annual Review of Medicine*. [cite: 42]
[cite: 43] Kim, J., et al. (2024). Standardization of organoid production and quality evaluation. *PMC*. [cite: 43]
[cite: 40] Naderi-Meshkin, H., et al. (2023). Vascular organoids: advantages, applications, and challenges. *ResearchGate*. [cite: 40]
[cite: 44] Zhao, X., et al. (2023). Vascularization and immunization of organoids. *PMC*. [cite: 44]
[cite: 41] Qkine. (2024). The role of vascularization in organoid advancements. [cite: 41]
[cite: 5] Bartfeld, S. (2021). Organoids as host models for infection biology. *PubMed*. [cite: 5]
[cite: 47] Dutta, D., & Clevers, H. (2017). Organoid culture systems to study host–pathogen interactions. *Current Opinion in Immunology*. [cite: 47, 51]
[cite: 16] Heo, I., et al. (2018). Modelling Cryptosporidium infection. *Nature Microbiology*. [cite: 16]
[cite: 25] Sigma-Aldrich. (2024). Protocol Guide: Generation of Apical-Out Gastrointestinal Organoids. [cite: 25]
[cite: 21] Bartfeld, S. (2021). Methods using organoids to study infections. *PMC*. [cite: 21]
[cite: 34] Tegtmeyer, N., et al. (2017). Helicobacter pylori CagA and c-Met interaction. *Springer*. [cite: 34]
[cite: 35] Bertaux-Skeirik, N., et al. (2015). CD44 plays a functional role in H. pylori-induced epithelial cell proliferation. *PLoS Pathogens*. [cite: 35]
[cite: 15] Qian, X., et al. (2016). Brain-Region-Specific Organoids Using Mini-bioreactors for Modeling ZIKV Exposure. *Cell*. [cite: 15]
[cite: 12] Finkbeiner, S. R., et al. (2012). Stem Cell-Derived Human Intestinal Organoids as an Infection Model for Rotaviruses. *mBio*. [cite: 12, 13]
[cite: 23] Co, J. Y., et al. (2019). Controlling the polarity of human gastrointestinal organoids. *Nature Protocols*. [cite: 23]

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFPOwPOnWTg1Ms0wpb1sHuVvWRfYATUfmkvSQeRPRo5DqwKMCbrh0aGBCH8r4sFdXJmI0SR06VjRK9u-E5mbj3kHm4aLczVec7D0IUJMBI16N7iBoDYfKbQC9CIijCf5ZW-gKSzas=)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbCc_Zkxdvrh5f6LvhfF8wlwyiLwXXdDH8u7kRR-MdhogdKVtfb0Q8EUkxmN6efeZeJoCtFP3WQgQlIPAcvJr904cJqiM9L0TD1pG8Ljylw8Jy912Pu2sGdZHtTa0rzLj-YqKzC4hl)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqGjUlppG5HnkdR8K35gTVLO-h0lkaNKDecLJgZP29T5oTFm_pO7PcT3L8dgY-h3VxFdvD2X9Pu9hNgJ38fHpaPFlaLGIkWG3nhrQ0FFvH2tqdmvehw0H9GPGR)
4. [sinobiological.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH87PUnYdGvlanQHAbQdw42h5QK0MuIf3Ur9cEnfKcZkPyZTQQfKuYX7yHZd9Apc6dkuIzlXJvcJzOJYWuuqZmgdgwUpT2dFCchb8Sn91EaddVi444FsUucZm-QElv64K-x1wF5UeI88mpQhG8=)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhDV0aaiSUrJJRGi_XwWej36Gp1ilNvxOzlKpR4LtmcLqKCRQn97nklueRkxY5jynjR6K1aDCuniwyWOFANT5FZEqo6Wi5S_2TMa4DnwE4w7mlh5O-qW8tA7E30Pcf)
6. [annualreviews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAGdEjNv04ceYtLA6p98ZYaNk7_Ih_JYMqU5-ig8UnGkOUeWshKlnxVbKGilnVrAquqSFPzmnrR2etjpaXefuSAPnBXbtqeykwmLspBXfbzevK0gGzHpMKPS-v11jm6qHiw5-4pNjKaigrYqSNXsiqNwB5xY1N2SfYd9xq)
7. [sigmaaldrich.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7mHhFSNQCb1LSgoKqtdQd8AOVD1PQAZVEU8lhhRlVzyAyzHfxukLYcs3D1vIqwrX-y4C78s4hlg5LSSDYg3_ig0ns4nSMDv8pdnyBiRc0QMncCyTs_-tWR3Hq41zJsnApf4-C_Qs9ra_a85QiFOBJd8LjMhao9eNLu85zbrJSb8rXhW6lqGMAG2JhHqYTyKM2AnB9ma36LrfzUlHLYEcJRQcKGQtVeWtCfuuyCinPccS1hpmRTch2hpEo1JHXtyrW)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIbHTH0x4ezkEXRmRRzaazRerOycN7JNWV_vBd4lM2W1EfrYyn_D1DGIqD1KRtnX8weq961kq6wCIswhi2J6cs_MkNWIdBPEg3stetyM6CGUGKK6XfdvBrbl5Z6Kn_63XOmlBLfjo=)
9. [physiology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKPFAXHHqFdNyo8f1qdQdWSGx8MZ_z5N8LW552FVHA4gla_nu8uOBgBJFhNL-h8d5-d4Jth-hSVFO5fc4c-7srnEYpMSFIUImXQ3K24C-ixAj5Nn_clVcwZ6Dyw0dulSYAN-NrgijWun03Lv94skgnvr-qKqws)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhVI4VPy2o2tfIlnm-2PMfbV27pXDrC8AaNJIKjfZ6GqpxDKNR6A2eRanlZ9k0CClUnbnOZRZ6IQMF2kYnVecJ-PRm8xsJPE0MBcQANrSkbfPKrolvUpMU4MQFE0Xg4sBUVpsLP4k=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpbID4ZT-2ZXjmR-YWD4ivzIrTb_mLH7C3ig1oySszLjW_-NWJpzz_8U-FytmWwFPrgkvJDJ6CcFkX18ESBrrvYmDo26OorDFbh6fZFdDhIJmV1wXD_IIfiKoYRBUgEhoXf0GBiUCclSkADa2wBLkH9Vd5H7LskQPfBtGfmrlRFZ50HhWNsjmhVUdsrLxRmU8gK0XJPRLemZMIzPEstxTElVJ6AU-YPB8ECZv8_GxUlI8EPNgI5Qj2rQJOtlF_)
12. [asm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAA9dggXW12TE6i3TGeSWLTAKbS90JHgBdfoyBLTbSSd5c8S9g5wNhWRo53NIia51uJBcSvUHLpeIt2gURzTVmor9-mSZWE86GNVwWXDyx0JlHBC4E5cTlu5_iV-HE4Q8-W6kPQHqA)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVSfxxlguG4Twm-cIEoQ9LA0eD2POa9YDLXeQ3oLz0owKMO43SO36bfljpqRCKI7gQuWG7YBUefmPjU_RkbL0alHmqMZPO22Wex1iYXZxOu0JaYnvrHTiKhPwdJJ0q)
14. [jove.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtQ-3YrBQwn1FEgzMbflRJgw2T7eNV1f_kLIOUwp-ZQ-EQtHpHO-wKnFMkqSb7nYGMZnXI7LZ8Dpc6kx2tE1m3s0xaKOnBERQYrn3o7FmBqbwZXunVM_JCspVFw6TifFUlL8zDgDXc1XWCnQw8tX9wdoo1ym5LyLyS5f0TXykMswQgqBUQQ8hhfMKlWnya1nPpqtw=)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGCMTFyDouwkf2jj7dpK55RjLPthGGqp2HrlmiShmUYi92BCzqlKa20K2pGwluPgoAJTYi_XpkziyT0-BEVPEL8GAxZZf0U63UKKWOVzdrBgFhfGgkVIEhqOX28Mvs)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzzF6VuRdeKylH2wFh1oJOfcHFcIdDhMSSw2WNp70JJTMHbU9va7w1rjDNOo_kmMK_s-j-Eueg6Ars40Mj55KCty_sMSGRco0OPZLu7Iu9o-1CraWiKhVRFzB7yFxYMWH0TMu-kwM=)
17. [corning.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZvKGuZyhtQlg5Fl-d7V7nFyrTDsk64IXf1RJy_WCAT5xZl2yQM8uJ6AVG0uLvRUjczvAXX8Ax4dZ3jEc7sWL0Sj-Xw0gbxQe-tHOzQhtKjaqYaUQVtMesW6jtxPuYzqaz2Vx1glWi6rBNKCsSX1hBRUwi9CkLDft0g1IUXXwRoyNpg8DB3H9zwbW727DuZB6f90q8ba_74HsxxFtQQAxzzEzxxm4gFEoT3o09HnOqO6YSQ8gc7J8GcWk2s1Se3hnrlBdeNwdpkReCikF8)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGs3apELvvfYGnkTI6GkC5flxxXXYXIj-_zkLD3Pwr5RPKa1xV0y43zXetsGsIRvKTcgqNPOfVzwkjA3gedWDWCfg4Eucnwe1nfYWaKhDTUPqrEO_E6NTr9LGApGL0GOBgkvwLdEo=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP07cORDgcZmMRrCYZszxCpkek4Omk9md9NS2H2tYeHkROf94MHy3BG2O_ROzrJC9TX0xYKU9aDoVC6n_s7XHGBt917fPb__jjT9UCApsMREf0CN7nSakHv7SAYqv5lGpWs5z-kbB--Pb-ifCboPeWx7NPaG1yqSHQDgCULjgqQ5iLGBjjC9fs1rSrJu2Kjup8fj-NFlJrOQq64ZlYQk4JQo5eLdvV6zlZHq1UzlF338MhSyRgDH9pEU5GoLSoR4w=)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM2EBK513HSpvQlS8AZSetTPgkSOjG8j9aUY2h1ED-M9dCkrJLUjGz8n16SuduaTuKudEbiu_gd0im9wLlDK7OqDyI4TaAU2w11Yy5dL6dqXk-pWZvJDi2lzKpvGAGAYmZ0Ok3z09hmZ0EvR7oRyN2AmZbOmM7BkAApvOukOnrLlKWYMUsk-l3ACXjOisxwWKdz_23Tt0tkRt-3TYqI8Ld0DMZQYBRiqj4OpvM)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdj1qOhNClMAs4UkjNc7P3c3q0SUnMkzEUI16TT1ylpMiHFD2D1jQtgflzy4fLfwcSAm-qHGT_xeKwn_ahXMjWV_ONrDSYdNxMvP4wEYDLQAR5bGVXmxJKqULMADLayHOVRB30zuY=)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGETyF4MvQq-V_4yEwtPoePTObXgrKkltiywtIZbNmWHqXzX_12DXeQWO_zVU0v9sRXQxMeFDSTDhwIOWvyuXmrLgC4q4S4Msdz7pWJHjsM8D4pMLwGC8Bm91EsBvekf9KsVj0Liws=)
23. [asm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbCcb9-ozMtY9E5gpSTuD6qMc6X1-RxJoNk0eQ7iAJEIbHMTEWpW2Q8nzZY_ESHhGAEOiqCnd5CeHarnCi3ZDSS0DsQ5UEXpTH5PQkYSRxf5ci0ooX0PjoU7E7sbbbxlS8_CL5dk0=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmf5gRnXxiRg-2X3L0o4AnE-Y-F1oXjl0a3Zppccz8jaFC8gpGdmD46yVoRquDHG6cPmV-FPzOMCpICkIS_4xQC3CGRPNR4Y1LvpebJMlqk0qMf-ldc9i1aZwskPVro_QlmmIHtcgaLDBK3xh-FzMuvr-Bc0Bd_xwJUBn7v6Rydbr2kxSAcWlqLLoK5K19lb_AB_szuxatMjGl6qpO0IiYGrRFxNI_hFEraHqaqIfsctXxbFm0M7Qp6EHj6Z8LR8NgbLBGz2FGxklyuWYXCjy9zkk=)
25. [sigmaaldrich.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYTPim3eH4KwWSksaQRchBEA5ZTqvVWtZqjfSGMNcgWjn-7IIRXa48v01shF_fntdkRMZrKKtvMJ0itscooURuZUi3YoKawAJsExKw2AGV3se1SYgENT_FbqrTAzbWRr97xVD4lMFaVilwi_2KukRfv3PUrny8G1_gfWjOwrR7yGnGCKAM-lK9BEHilD7dKJ04SE3FT1yFfTMXW5N0v8v9xDqtKZUIAG6FaRXZgQXUQLNItjyWCELlUb2GjgcH8wi3)
26. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtgLmqj8ZWRplJzZi_H7e2CKmRSGhsW0A9W_KsvSMe4agfGWhxsGlW2ysCykHt7eWo62H8SLi7XDRICLacKTFG9CT3Vhu057wU4-N0vUDGzauiFhVhuDnYI-Wma62hdfiGy5azVvehwjGcZpgwPluDiqxMfHcmPDU63w==)
27. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl4VOwxq7-b3j8up7bN51dJboar3lRlNFL95s7_D0J6v3vOtPdSFgLZVAht64GqthVZRfhKoOnfzwuiGh_bJRz4ifK1g0rNOeNgkk5koxFku-MxD_QeV31I8iC5qYs-ku6qDy5bobOVp3KI4mZHbupP3nk_y5O6BiWvg==)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-rMgEDiUvQnFYOdIv3wG_4noBSlL6WDsfh401kca15yXoEyJt5SmTEjqZ6SdsRlhp2zvoX2fRXaJKJCQTFXVIJJtc1v9wQCEySLNwvtdD6VNyHAwj30zm2Q==)
29. [emulatebio.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzIhSQMchc-6vVFHXl_OhCSNAsefxxFb6VKYNPyR-L_RLhMyt6d4t1j7HyLSdtpJJ8Gs3Pv5HNn2qtuhjQTCMU4PTbBEG-5ePRUV5pJso8bDYDdLf_-NjPXYFQlGppqroGIZqHwKj_EXPEpw==)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcEG0hsQuB5hS6bhOsDKVQ47dL27zbYJ9vwAxrINdbmDN6yiNaG4cUSGX1Qsm5YebsQc79Nj53HypMlqMmr2zImfJvKusUPxI_BjQ4m0_HXcI7GV8E48IWTFAcx7NHK-nE6dpMg5Q=)
31. [dynamic42.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa_5WfYg9YVlrSPPKoynJi1qpOOth9iiBjtYmutjBgb6T9l6Tr8_84SEHrVlD2rN_s0ClMQovv9rflV59U8H5excuttMxx3WTN-q_e4VuQbFaiJaHO9umDqIxuXHhyAWRkJ2OCAkZRDB3m9MVOFziwTbUa3lPLyPpxBf8G)
32. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBejtnZ6NktTatVOCmtFLoynbjDNAYKtOpR0JtSXRwvFnLG97lhrdnjscWo4EuyrUswx0clxOk-l5ZHOyvUAI4dMlIqy-XdYbqExldXdLkMEHQhcBAYQbkULEF9o80MwSMQekC-M6gffNu8cofRwtq1pNe3FXRMtucofMROjNGwXfH5QHjemzlW8YEvsrIN-08VfoB8TQ=)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOB-8yFBfAwy3ic91MSTYAG8cI4Qct2mYKuVMdfIKzvCk6fcmeojgVNnbIALRO5R5zVdpenlmU6eOBenZEVVYEDgslWD7Lx4KQMOqGjHatQTW_5J76RqBV-3HNT8bHyoaxfSLSR8Q=)
34. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5mKJYoe8J36k5MSVj4-I8FpPA39KQ9Nyd3o3n4b1aTWCXNBJ3FtNNALEat_cq_1LdA2w8xbXlbi1cXESLStqRuT3UUXgQBB6mo0_K2PAJTPRxpNc=)
35. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEwmBGFnwBqoLIlFZL937VDs3azTYbV0I2blomklAv0gvPChFOq9M99sPtcrZd0H8Ta9xAoPM6RJOgLTOZmtDih_aTj9FsT1-edbh6GGTR0UYPKreT289G6V2LnQncb0nMx7Y4wuTf5iDoYf_-nfJMPlhmZztJvx5kc35OqYzXHmbG4jo=)
36. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiEAY4kBl6adSb1s2-bMxZYjPCfAVKtH3_5W2qNdgikiBh0sWuDL_pZMXMjDUKeiEzNu7UDmANrInUi6IGbSLG2GuFd2Q10-yX3ah8nFG6IMK3EjpxnpUay_NjDOjoSlGLRMIFGHy81kzXNpaVFh8gO2RS2Rl9)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt3JRmphSGmVdczdgnGgmg0VwmRkv_dntBuNMZ8DL30GOLLr8QekyjC1t76weGGckIe89d8eR92WYAhkA8rJnaId1RbcVTIf1eB5zGYoADZE3ctknPMsW15uC8zHr9RE0_DupZhxY=)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSJqTyruyY_pGQS9tf_I1FrNspe8wz92PZ_0WlcxyC6SeMnEWspSphLmCz2nm5oOrkLs6mY3JPzq5WK9_jmp73T63axi4pZwgkAkMgMQn1shNwsckmFC7p1h7cfHKq-ZmqgF0S_bF3)
39. [jove.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3X17Bl42YPcfHMRtH9lnK-0T9a_68SWR6Aw1yhcDx8VHOSv23MHlg06q39Posl8nKWevYRcQfUblfn1xrhahph_fHlEsdYa3IR8lBuefCR0O4FMJ1dLnjHffv7IlbHZYWdfqqXCYlwBv02u85B32blhzP58Rx2OmLCPF3IlEWlpOhVGrZij_J7gIrc1atPb1lXZ5q)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGyIfcBliY3EqnDwNRmfk-BwSdlgEwI7BcHetabXPwCGJ-vliVDcqBNa04BNFiBW_SyYTN9MwWTOgfvLqWygIC3RIdp18zMFBGBXLYvQfzN6bp_Ti7UlI2DsxqOCudNHi5DbhkPA2YShliwyVTnsfFGfauOUyFGue37Q7N_fTuuJCXXpERps0m9xxrO3JQTClklXtSbWN9NCm_ujNnL5zp0shl-Gk3JF4fMeXcu7eCFmmNSA9yylE69ICbGI92-v4Y9T14NaW1SDk=)
41. [qkine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Xw2KK09OGKLBaGphE14Hs0cBxClPwG4CYBlQPkIs1yecP8q3q5pEwPDCWd_9ioQelJVDJtM5gzYz4d-jfH1_VtLXgPrMb3VT1nV2tm0RHvCafdAl94EX0trLFBZJQwKXWCR0EVFx_1YVEw7Q0GNa-cLadZi76yHlrkwUWei6YbT6J_v7hhQDDOXVjnAJEKRWzWpvUvz6WXRBgqQ=)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIo-Zg9xS6uFhjDNM-R3E3BZH5Kz9t83w0vO7V4fj38vM-w4mUd_VV96LF55zcbq_IgdMaNZVkQH8TFpQLinlumgPtF24dm6Z2ZP772kO4QNUZ9SYOZ83cfMS11TvMU5hNWhsPNNk=)
43. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNEce2PLPYgzWftfgrGl9eDi9bZnk24QTmLZIURTCmq981Z-6itYGLLTxZU6EumfZcrvV4jVyplGASZa0XuEP1wZZOPZjP5pEfvJKyj-4wKF94AwfpeGWrUaJZDYiGtU94MLgmTQFN)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQo7LC2Z7WY73xjBE5OK53RNt-3UB22Li5EgrmKyhuEVJgRYXiXPXpM-Uwvm2XJtFYs4jkLqa6EBhblaSNe8x4cjMtlqJundy5r77S9GRIqZrpkfkEA6A6MtxkLbMap0UKhcTGfGQW)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhjVCiku9Flo6pWCMEcZaBFVcqabhPK5MpmK7U45RTJlxIwCc4Kpcfvw-0GDN4ZPoy16rhwIR2eH4lWGx_a2Jr9R6bLDU4WJ4pGTF0oRgqirHBCM6cSyRFaDA_rvemwMV1A7dwII=)
46. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmM8pzvUW_YSLfm4rFC6v39KuTl0vxyooJJU95OJNpSXjnapc2w9CVPIgeAGpjlsMcBw3NfrKPdGSNfUzsFjclgmMeo1Ip1LXci8izNR6PM17EqrE8fuxvdzSQ6SoaxTb7T5VnmELc)
47. [hilarispublisher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-1GTT5AkPW6mFAT0tu5QiYxku9wz_0XwrhlTsniqmPHIwmGEI9s1-t3xgFq-JE6WJv6S5nsnKXaMT_GouipsiZAvTQ69GMXKPlR0SQH9z0i1eoZ-FQRCotFFgLPgwZmBje3cU5Q2m9MaB3t2H2S6kuZn-Sw-k4OgfRpz6uA0sTiY6KSXOzbGgM34PFgy93GKWylJIYxRmKExAtsvcxcbz7yF8-mgYGEFsZRpxMgE1dhlrEjGpzVAp4Q==)
48. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtbOUWsCqh_ncpenh4OhTryncNN0h_K_zue-kiJU4Gfb8HvarUpiq4001DQjQikydMAJw-4B1hBQm2p-QvnA6gMTaL_MYdwhlktUxvLUQaUT2PTgjRMbC8NesN_h5bobl1NwqY2xs=)
49. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeze6xuA_VjWmwAMFWbwou6cm2C0_IZk_LFn-JkVbg8I1gZcZGkrSDVblu9Azd1E_nMTuAeNzhYTE4I6qQtUdsFXYDC2zoSxUIgw9QsRGi8QGMIh74IeYeJMR3AUNw)
50. [atsjournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKy8aCfGtjmL8HfMk3pdzKqyHcjxggh6aeXWVMhNk9MelsjhrQLLksI2jzaAJI-aHcnOPRHQW57CI9zsib71tl0XFyXBl9KrknibHJNxEp1ws3_XIdX_57jjF1J4K5sZemHPOG0qK-V6LEUOMJfM-oipFrIu910WrUG7eUrfgKXTGB6DgQ-_zOwK6CTB_E_KHj2wE6Uqc_rDd175SQVxF2eDU=)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx4qU64KpBQ_1MENL-xTCuubxcderRMm3QlcUJoSa6msICQYGqXgUbGS656xYbonkWy73-HpE3ifOMcqqjJazrDztH6_TKfEsLj8s2TaqWGnLbk8tfBk8rLKWUigx5)
