# Literature Review: Mycobiome in the Gut- A Multiperspective Review.

*Generated on: 2025-12-26 06:20:34*
*Progress: [18/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Mycobiome_in_the_Gut-_A_Multiperspective_Review_20251226_062034.md*
---

# Mycobiome in the Gut: A Multiperspective Review

**Abstract**
The human gut microbiome is a complex ecosystem traditionally viewed through a bacteriocentric lens. However, recent advances in next-generation sequencing (NGS) have illuminated the critical role of the mycobiome—the fungal component of the microbiota—in maintaining host homeostasis and driving pathophysiology. Although fungi constitute a small fraction of the total gut biomass (approximately 0.1%), their large cell size and potent metabolic capacity exert a disproportionate influence on the host immune system and co-resident bacterial communities. This systematic literature review provides a comprehensive analysis of the gut mycobiome, tracing its historical emergence from obscurity to its current status as a pivotal frontier in biomedical research. We critically evaluate state-of-the-art methodological approaches, specifically comparing ribosomal DNA markers (ITS1, ITS2, 18S) and multi-marker strategies. Furthermore, we explore the "multiperspective" nature of the mycobiome by examining tripartite interactions between fungi, bacteria, and bacteriophages, as well as the host immune signaling pathways (Dectin-1/CARD9). Clinical applications are discussed, with a focus on Inflammatory Bowel Disease (IBD), metabolic disorders, and oncology, alongside the therapeutic mechanisms of fungal probiotics like *Saccharomyces boulardii*. Finally, we identify persistent challenges, such as the differentiation between transient and resident taxa, and propose future research directions to bridge the gap between descriptive profiling and mechanistic understanding.

---

## 1. Introduction

The human gastrointestinal (GI) tract harbors a dense and diverse community of microorganisms, collectively known as the microbiota. For decades, the term "microbiome" was effectively synonymous with "bacteriome," as the vast majority of research focused on the bacterial inhabitants that dominate the gut in terms of abundance [cite: 1, 2]. However, the advent of culture-independent high-throughput sequencing has revealed that the gut ecosystem is a multi-kingdom environment containing not only bacteria but also archaea, viruses (virome), and fungi (mycobiome) [cite: 1, 3].

The fungal component, or mycobiome, represents a relatively small proportion of the gut microbiota, estimated at less than 1% of the total genetic material and 1–2% of the biomass [cite: 4, 5]. Despite this low abundance, fungi are increasingly recognized as "keystone species" capable of exerting significant ecological pressure on the microbial community and the host [cite: 5, 6]. Fungi possess distinct metabolic capabilities, produce bioactive secondary metabolites, and engage in complex physical interactions (e.g., biofilm formation) that bacteria cannot replicate alone [cite: 7, 8].

The motivation for this review stems from the rapid expansion of mycobiome research and the need to synthesize disparate findings regarding detection methods, cross-kingdom interactions, and clinical implications. While early studies were largely descriptive, the field is now moving toward mechanistic inquiries involving host immunity and multi-omics integration. This paper aims to provide a rigorous, multiperspective examination of the gut mycobiome, moving beyond simple taxonomic lists to understand the dynamic interplay between fungi, bacteria, bacteriophages, and the human host in health and disease.

## 2. Key Concepts and Definitions

To navigate the literature effectively, several foundational concepts must be defined:

*   **The Mycobiome:** This term refers to the collective community of fungi (yeasts and molds) and their genomes within a specific environment. In the context of the human gut, it encompasses both resident commensals and transient species derived from the environment or diet [cite: 1, 9].
*   **Autochthonous vs. Allochthonous:** A central debate in mycobiome research is distinguishing between *autochthonous* fungi (true residents that colonize and replicate in the gut) and *allochthonous* fungi (transient passengers introduced via food or oral/respiratory routes) [cite: 1, 4]. For example, many plant-associated fungi detected in stool may simply be dietary artifacts rather than active colonizers.
*   **Dysbiosis:** While typically applied to bacteria, fungal dysbiosis refers to an alteration in the composition, diversity, or function of the mycobiome associated with a pathological state. This often involves a decrease in diversity and an expansion of opportunistic pathogens like *Candida* species [cite: 6, 10].
*   **The "Rare Biosphere":** Fungi in the gut are often described as part of the rare biosphere. Their low abundance poses significant technical challenges for sequencing, as fungal DNA is often swamped by host and bacterial DNA, requiring specialized extraction and amplification techniques [cite: 11, 12].

## 3. Historical Development and Milestones

The recognition of the gut mycobiome has evolved through distinct scientific eras, shifting from pathogen-centric views to an appreciation of commensalism.

### 3.1 Early Observations and the "Germ Theory"
The concept of a human microbiota dates back to 1853, with Joseph Leidy’s publication "A Flora and Fauna within Living Animals," which posited that flora exists within healthy hosts [cite: 2]. However, for much of the 19th and 20th centuries, following the establishment of Koch’s postulates, fungi in the human body were viewed almost exclusively as pathogens (e.g., agents of thrush or systemic mycosis) rather than commensals [cite: 1, 13].

### 3.2 The Culture-Dependent Era
Throughout the mid-20th century, the identification of gut fungi relied on culture-based methods. While these studies identified ubiquitous yeasts like *Candida albicans* and *Saccharomyces cerevisiae*, they severely underestimated fungal diversity because many gut fungi are difficult to culture or require specific anaerobic conditions that were not standard in clinical mycology [cite: 9, 11].

### 3.3 The Metagenomic Revolution and the HMP
The launch of the Human Microbiome Project (HMP) in 2007 marked a turning point, although its initial phase focused heavily on bacteria [cite: 14, 15]. A pivotal milestone occurred in 2017 with the publication by Nash et al., which characterized the gut mycobiome of the HMP healthy cohort using ITS2 sequencing. This study was the first to describe the fecal mycobiome in a large, healthy cohort (n=317), establishing that the healthy gut is dominated by *Saccharomyces*, *Malassezia*, and *Candida*, and that fungal diversity is significantly lower and more variable than bacterial diversity [cite: 12, 16, 17].

### 3.4 The Multi-Kingdom Era (Present)
Current research views the mycobiome as part of a "holobiont," integrating data on fungi, bacteria, viruses, and the host. Recent milestones include the characterization of the Dectin-1/CARD9 signaling axis, which elucidated how the host immune system senses and regulates fungal communities, linking genetic polymorphisms in these pathways to Inflammatory Bowel Disease (IBD) [cite: 18, 19].

## 4. Current State-of-the-Art Methods and Techniques

Profiling the gut mycobiome presents unique challenges compared to bacteriome analysis due to low fungal biomass and tough cell walls. The choice of methodology profoundly influences the results.

### 4.1 DNA Extraction and Lysis
Effective lysis is critical. Fungal cell walls contain chitin, mannans, and $\beta$-glucans, making them resistant to standard enzymatic lysis used for bacteria. Bead-beating is generally required to ensure DNA recovery from diverse fungal taxa, though it risks shearing DNA [cite: 11].

### 4.2 Amplicon Sequencing: The Marker Gene Debate
Unlike the 16S rRNA gene used for bacteria, there is no single "perfect" marker for fungi. The nuclear ribosomal RNA cistron includes the 18S, 5.8S, and 28S rRNA genes, separated by Internal Transcribed Spacer regions (ITS1 and ITS2) [cite: 20].

*   **18S rRNA:** This gene is highly conserved, making it useful for higher-level phylogeny (Phylum/Class) but often lacking resolution at the species level. It can also cross-react with host or dietary eukaryotic DNA [cite: 11, 20].
*   **ITS Regions (ITS1 and ITS2):** The ITS regions are the accepted "barcodes" for fungi due to high hypervariability.
    *   *ITS1 vs. ITS2:* Research by Nash et al. (2017) and others suggests ITS2 is generally superior for gut samples, providing better resolution and fewer biases than ITS1 or 18S [cite: 12, 20, 21]. However, ITS1 may be better for specific taxa like *Malassezia* in certain contexts [cite: 21].
*   **Multi-Marker Approaches:** A 2025 study by Orsud et al. demonstrated that single primers are insufficient for comprehensive profiling. They found that combining ITS1, ITS2, and 18S primers (the "triple-combined" dataset) detected significantly more Operational Taxonomic Units (OTUs) (n=397) compared to single primers (18S: n=58; ITS1: n=158; ITS2: n=183). This multi-marker approach is becoming the new gold standard for maximizing taxonomic richness and resolution [cite: 11, 22, 23].

### 4.3 Shotgun Metagenomics
Whole-genome shotgun (WGS) sequencing avoids PCR bias and allows for the analysis of functional genes and multi-kingdom interactions simultaneously [cite: 24]. However, because fungi constitute <0.1% of the metagenome, WGS often fails to detect low-abundance fungi unless sequenced at extreme depth, which is costly. Nash et al. noted that ITS2 sequencing provided greater resolution of low-abundance constituents compared to moderately deep WGS [cite: 12].

### 4.4 Bioinformatics and Databases
Accurate classification relies on databases like UNITE (for ITS) and SILVA (for 18S). A major limitation is the "dark matter" of the mycobiome—a significant portion of fungal reads cannot be classified beyond the kingdom or phylum level due to gaps in reference databases [cite: 9, 12].

## 5. The Healthy Gut Mycobiome: Composition and Diversity

### 5.1 Core Composition
The healthy human gut mycobiome is characterized by low diversity and high inter-individual variability. The dominant phyla are **Ascomycota** and **Basidiomycota** [cite: 25, 26]. At the genus level, *Candida*, *Saccharomyces*, and *Malassezia* are the most consistently detected taxa [cite: 12, 16].
*   **Saccharomyces:** Often the most abundant, though its status as a true colonizer is debated; much of it may be transiently derived from diet (bread, beer, fermented foods) [cite: 6, 9].
*   **Candida:** Species such as *C. albicans* are common commensals but have high pathogenic potential. They are immunologically active and capable of true colonization [cite: 1, 12].
*   **Malassezia:** Traditionally considered a skin commensal, *Malassezia* (e.g., *M. restricta*) is frequently found in the gut, potentially introduced via oral-skin contact, but is associated with IBD exacerbation [cite: 4, 27].

### 5.2 Diversity and Stability
Unlike the bacterial microbiome, which tends to be relatively stable in healthy adults, the mycobiome is more transient and unstable over time [cite: 6, 12]. This instability supports the hypothesis that a significant portion of the gut mycobiome is allochthonous, driven by environmental exposure and diet [cite: 4, 9].

## 6. Multiperspective Interactions

The significance of the mycobiome lies not just in its presence, but in its complex interactions with other biotic and abiotic factors.

### 6.1 Fungal-Bacterial Interactions
Bacteria and fungi coexist in close physical proximity, engaging in both synergistic and antagonistic interactions.
*   **Physical Interactions:** *Candida albicans* can form mixed biofilms with bacteria like *Staphylococcus aureus* or *Enterococcus faecalis*, enhancing resistance to antimicrobials [cite: 28].
*   **Metabolic Exchange:** Fungi produce metabolites (e.g., farnesol, fusel alcohols) that can influence bacterial growth and virulence (quorum sensing) [cite: 7, 29]. Conversely, bacterial fermentation products like Short-Chain Fatty Acids (SCFAs) can inhibit fungal hyphal formation, maintaining *Candida* in its commensal yeast state [cite: 30, 31].
*   **Antagonism:** Antibiotic treatment often leads to fungal overgrowth (e.g., *Candida* bloom) by removing bacterial competitors that normally suppress fungal proliferation, demonstrating the bacteriome's role in "colonization resistance" against fungi [cite: 30, 32].

### 6.2 The Tripartite Model: Phage-Bacteria-Fungi
A burgeoning area of research is the "tripartite" interaction involving bacteriophages. Phages are the most abundant viruses in the gut and regulate bacterial populations via lysis [cite: 33, 34].
*   **Mechanism:** Phages modulate the bacterial community structure, which in turn alters the bacterial-fungal equilibrium. For example, lytic phages can deplete specific bacterial species that compete with fungi, potentially allowing fungal expansion [cite: 35, 36].
*   **Direct Interaction:** Emerging evidence suggests phages may physically interact with eukaryotic cells and potentially fungal cells, or adhere to mucus to create antimicrobial barriers that indirectly shape the mycobiome [cite: 37, 38]. A 2025 study showed that probiotic administration (*L. plantarum*) altered both fungal and phage populations, with specific correlations between phage abundance and fungal reduction in the small intestine [cite: 35].

### 6.3 Host-Immune Interactions: The Dectin-1/CARD9 Axis
The host immune system plays a definitive role in shaping the mycobiome.
*   **Sensing:** C-type lectin receptors (CLRs), particularly **Dectin-1**, recognize $\beta$-glucans in fungal cell walls.
*   **Signaling:** Dectin-1 activation triggers the **Syk-CARD9** signaling pathway, leading to NF-$\kappa$B activation and the production of pro-inflammatory cytokines (IL-6, IL-23) that drive Th17 immune responses [cite: 39, 40, 41].
*   **Genetic Susceptibility:** Polymorphisms in *CLEC7A* (encoding Dectin-1) and *CARD9* are strongly associated with severe IBD. Deficiency in CARD9 leads to an inability to control fungal populations, resulting in fungal dysbiosis and increased susceptibility to colitis [cite: 18, 19, 42].
*   **Antibody Coating:** The host produces secretory IgA (sIgA) that coats commensal fungi. This coating helps contain fungi within the lumen and prevents translocation. Loss of CARD9 signaling impairs this anti-fungal IgA response [cite: 5, 18].

## 7. Applications and Case Studies

### 7.1 Inflammatory Bowel Disease (IBD)
IBD represents the most well-studied link between the mycobiome and disease.
*   **Dysbiosis Signature:** IBD patients typically exhibit an increased Basidiomycota/Ascomycota ratio, with an elevated abundance of *Candida* (specifically *C. albicans* and *C. tropicalis*) and *Malassezia*, and a decrease in *Saccharomyces cerevisiae* [cite: 43, 44].
*   **ASCA:** The presence of Anti-Saccharomyces Cerevisiae Antibodies (ASCA) is a classic serological biomarker for Crohn's Disease, indicating a loss of tolerance to fungal antigens [cite: 19, 43].
*   **Mechanisms:** Fungal dysbiosis in IBD is not merely a bystander effect. *Candida* expansion can exacerbate inflammation by inducing Th17 responses and enhancing bacterial translocation [cite: 1, 41].

### 7.2 Metabolic Disorders and Obesity
The mycobiome is implicated in metabolic health.
*   **Obesity:** Studies indicate that obese individuals have distinct fungal profiles, often characterized by reduced diversity and altered *Candida*/*Saccharomyces* ratios [cite: 6, 45]. A 2024 study on Chinese cohorts found that *Schizosaccharomyces pombe* was depleted in obese subjects, and its supplementation in mice reduced weight gain and improved lipid metabolism [cite: 46].
*   **Diabetes:** In Type 1 Diabetes, specific fungal genera are correlated with serum lipid levels, suggesting a role in host metabolism [cite: 26, 47].

### 7.3 Oncology: Colorectal Cancer (CRC)
Fungi contribute to carcinogenesis via chronic inflammation and toxin production.
*   **Signatures:** CRC patients show enrichment of *Malassezia* and depletion of *Saccharomyces* and *Pneumocystis* [cite: 48, 49].
*   **Interactions:** *Candida* may promote tumor progression through inflammatory cascades, while interactions between fungi and oncomicrobes like *Fusobacterium nucleatum* are being investigated for their synergistic role in biofilm-associated tumorigenesis [cite: 32, 49].

### 7.4 Therapeutic Applications: *Saccharomyces boulardii*
*Saccharomyces boulardii* CNCM I-745 is a probiotic yeast with proven efficacy against antibiotic-associated diarrhea and *Clostridioides difficile* infection (CDI).
*   **Mechanisms of Action:**
    1.  **Toxin Degradation:** It produces a 54-kDa serine protease that directly cleaves *C. difficile* Toxin A and its receptor [cite: 50, 51].
    2.  **Immune Stimulation:** It stimulates the secretion of sIgA in the gut mucosa, enhancing the host's immune exclusion of pathogens [cite: 52, 53, 54].
    3.  **Trophic Effects:** It releases polyamines that support enterocyte maturation and barrier integrity [cite: 55, 56].

## 8. Challenges and Open Problems

Despite progress, the field faces significant hurdles:
1.  **Low Biomass and Bias:** The low abundance of fungi relative to bacteria makes deep sequencing expensive and prone to amplification biases. The lack of a standardized primer set (ITS1 vs. ITS2) hinders cross-study comparability [cite: 11, 20].
2.  **Database Limitations:** A substantial proportion of fungal sequences remain unidentified ("dark matter") or are misclassified due to incomplete reference databases [cite: 9, 12].
3.  **Transient vs. Resident:** Distinguishing between food-borne fungi (e.g., *Penicillium* on cheese, *Saccharomyces* in bread) and true gut colonizers remains difficult without longitudinal sampling or viability assays (e.g., RNA-based sequencing) [cite: 4, 57].
4.  **Kingdom-Agnostic Analysis:** Most studies analyze bacteria and fungi separately. True multi-kingdom network analyses that integrate bacteria, fungi, phages, and metabolites are computationally demanding and still rare [cite: 24, 58].

## 9. Future Research Directions

To advance the field, future research must prioritize:
*   **Standardization:** Adoption of multi-marker sequencing (ITS1+ITS2+18S) as a standard protocol to maximize coverage [cite: 11, 23].
*   **Functional Mycobiomics:** Moving beyond taxonomy to function using metatranscriptomics and metabolomics to identify what fungi are *doing* (e.g., producing quorum-sensing molecules or secondary metabolites) rather than just who is there [cite: 7, 57].
*   **Longitudinal Studies:** Large-scale longitudinal cohorts are needed to definitively separate transient dietary fungi from stable colonizers and to understand the temporal dynamics of the mycobiome in early life and disease progression [cite: 9, 24].
*   **Phage-Fungal Interactions:** Elucidating the mechanisms of the phage-bacteria-fungi tripartite relationship could unlock new therapeutic avenues, such as using phages to modulate bacterial populations to indirectly control fungal dysbiosis [cite: 35, 38].

## 10. Conclusion

The human gut mycobiome is a small but potent component of the intestinal ecosystem. While historically overshadowed by bacteria, fungi are now understood to be integral players in immune development, metabolic homeostasis, and the pathogenesis of complex diseases like IBD and cancer. The field has matured from simple culture-based observations to sophisticated multi-omics analyses, revealing that the mycobiome operates not in isolation but through intricate multiperspective interactions with bacteria, bacteriophages, and the host immune system (specifically the Dectin-1/CARD9 axis).

The transition from descriptive studies to mechanistic causality is the next frontier. By overcoming methodological limitations and embracing a holistic view of the microbiome that includes the "rare biosphere," researchers can harness the mycobiome for novel diagnostic biomarkers and therapeutic interventions, such as fungal probiotics and targeted antifungal strategies. The gut is not merely a bacterial vessel; it is a multi-kingdom theater where fungi play a leading role.

---

## References

[cite: 11] Orsud, H., et al. (2025). Multi-marker comparative analysis of 18S, ITS1, and ITS2 primers for human gut mycobiome profiling. *Frontiers in Bioinformatics*. [cite: 11, 22, 23]
[cite: 24] Stewart, C. J., et al. (2018). Methods for gut mycobiome analysis. *Frontiers in Microbiology*. [cite: 24]
[cite: 22] Orsud, H., et al. (2025). Multi-marker comparative analysis... *PMC*. [cite: 22]
[cite: 21] Hoggard, M., et al. (2018). ITS1 vs ITS2 vs 18S for gut mycobiome sequencing. *Frontiers in Microbiology*. [cite: 20, 21]
[cite: 23] Orsud, H., et al. (2025). ResearchGate Publication. [cite: 23]
[cite: 1] Underhill, D. M., & Iliev, I. D. (2014). The mycobiota: interactions between commensal fungi and the host immune system. *Nature Reviews Immunology*. [cite: 1, 19]
[cite: 30] Zwolinska, K. (2023). Fungal-bacterial interactions in the gut. *PMC*. [cite: 30]
[cite: 4] Tso, G. H., et al. (2023). Fungal-bacterial interactions in the gut. *MDPI*. [cite: 4]
[cite: 31] Li, X., et al. (2023). Fungal-bacterial interactions in the gut. *PMC*. [cite: 31]
[cite: 25] Pareek, S., et al. (2023). Fungal-Bacterial Interactions in the Human Gut of Healthy Individuals. *ResearchGate*. [cite: 25]
[cite: 6] Sun, S., et al. (2024). Gut mycobiome comprehensive review. *MDPI*. [cite: 6]
[cite: 9] Wang, Y., et al. (2024). Gut mycobiome comprehensive review. *PMC*. [cite: 9]
[cite: 10] Singh, R., et al. (2024). Gut mycobiome comprehensive review. *PubMed*. [cite: 10]
[cite: 59] GMFH Editors. (2025). Key advances in the gut microbiome during 2024. *Gut Microbiota for Health*. [cite: 59]
[cite: 48] Zhang, F., et al. (2024). Gut mycobiome comprehensive review. *MDPI*. [cite: 48]
[cite: 60] Shah, S., et al. (2024). History of gut mycobiome research milestones. *PMC*. [cite: 60]
[cite: 2] Fasano, A., & Flaherty, S. (2021). The Invisible Organ: Shaping Our Lives. *MIT Press*. [cite: 2]
[cite: 61] Gasbarrini, A., et al. (2020). The gut microbiota: its history... *Microbiota Journal*. [cite: 61]
[cite: 13] Podolsky, S. H. (2025). History of gut mycobiome research milestones. *MDPI*. [cite: 13]
[cite: 3] Zhang, F., et al. (2022). The role of gut mycobiome in health and diseases. *The Lancet Microbe*. [cite: 3]
[cite: 32] Sokol, H., et al. (2022). Clinical applications of gut mycobiome research IBD cancer. *MDPI*. [cite: 32]
[cite: 49] Coker, O. O., et al. (2024). Clinical applications of gut mycobiome research IBD cancer. *Taylor & Francis*. [cite: 49]
[cite: 28] Li, X., et al. (2022). Clinical applications of gut mycobiome research IBD cancer. *PMC*. [cite: 28]
[cite: 62] Zhang, F., et al. (2025). The gut mycobiome in health, disease... *ResearchGate*. [cite: 62]
[cite: 7] Pierce, E. C., et al. (2021). Bacterial–Fungal Interactions... *PMC*. [cite: 7]
[cite: 8] Sanchez, L. M., et al. (2023). Molecular mechanisms of fungal-bacterial interactions. *RSC*. [cite: 8]
[cite: 29] Deveau, A., et al. (2022). Bacterial-fungal metabolic interactions. *Taylor & Francis*. [cite: 29]
[cite: 63] Bakhshandeh, B., et al. (2025). Quorum sensing molecules... *PubMed*. [cite: 63]
[cite: 58] Frey-Klett, P., et al. (2018). Bacterial-fungal interactions. *FEMS*. [cite: 58]
[cite: 39] Tang, J., et al. (2025). Dectin-1 Card9 signaling pathway. *Taylor & Francis*. [cite: 39]
[cite: 18] Doron, I., et al. (2021). Dectin-1 Card9 signaling pathway. *PMC*. [cite: 18]
[cite: 40] Li, J., et al. (2025). Dectin-1 Card9 signaling pathway. *PMC*. [cite: 40]
[cite: 42] Malik, A., et al. (2019). Dectin-1 Card9 signaling pathway. *PMC*. [cite: 42]
[cite: 27] Lamas, B., et al. (2022). Dectin-1 Card9 signaling pathway. *PMC*. [cite: 27]
[cite: 64] Kelesidis, T., & Pothoulakis, C. (2012). Saccharomyces boulardii mechanisms. *ResearchGate*. [cite: 64]
[cite: 65] Consensus. (2024). Does Saccharomyces boulardii increase beneficial bacteria? [cite: 65]
[cite: 52] Biocodex. (2024). Saccharomyces boulardii mechanisms. *Saccharomycesboulardii.com*. [cite: 52]
[cite: 66] Biocodex. (2024). Mode of action. *Saccharomycesboulardii.com*. [cite: 66]
[cite: 55] Czerucka, D., et al. (2019). Saccharomyces boulardii mechanisms. *PMC*. [cite: 55]
[cite: 5] Ost, K., & Schooley, R. (2025). Extra-bacterial gut ecosystem. *MDedge*. [cite: 5]
[cite: 35] BMC Microbiology. (2025). Probiotics may impact gut fungi and bacteriophages. *NutraIngredients*. [cite: 35]
[cite: 67] PubMed. (2025). Fungal-bacteriophage interactions. *PubMed*. [cite: 67]
[cite: 33] Gut Microbes. (2025). Fungal-bacteriophage interactions. *PMC*. [cite: 33]
[cite: 68] Federic, et al. (2023). Fungal-bacteriophage interactions. *PMC*. [cite: 68]
[cite: 12] Nash, A. K., et al. (2017). The gut mycobiome of the Human Microbiome Project healthy cohort. *Microbiome*. [cite: 12, 16, 17]
[cite: 57] Knight, R., et al. (2021). First next generation sequencing study... *MDPI*. [cite: 57]
[cite: 26] Salamon, D., et al. (2021). Analysis of the Gut Mycobiome in Adult Patients with Type 1 and Type 2 Diabetes. *ResearchGate*. [cite: 26, 47]
[cite: 47] Salamon, D., et al. (2021). Analysis of the Gut Mycobiome... *MDPI*. [cite: 47]
[cite: 69] Fava, F., et al. (2017). Impact of diet on human gut mycobiome. *PMC*. [cite: 69]
[cite: 70] Nutrients. (2024). Impact of diet on human gut mycobiome. *PMC*. [cite: 70]
[cite: 71] Lin, J. (2023). Effect of Different Diets on Human Gut Microbiome Health. *ResearchGate*. [cite: 71]
[cite: 72] Journal of Nutrition. (2020). Impact of diet on human gut mycobiome. *Academic OUP*. [cite: 72]
[cite: 73] Frontiers in Nutrition. (2021). Impact of diet on human gut mycobiome. *Frontiers*. [cite: 73]
[cite: 41] Sovran, B., et al. (2024). Dectin-1 CARD9 signaling fungal dysbiosis IBD. *PMC*. [cite: 41]
[cite: 43] Sokol, H., et al. (2016). Fungal microbiota dysbiosis in IBD. *Gut*. [cite: 43]
[cite: 19] Iliev, I. D., et al. (2012). Interactions between commensal fungi and the C-type lectin receptor Dectin-1 influence colitis. *Science*. [cite: 19]
[cite: 44] Li, X., et al. (2023). Dectin-1 CARD9 signaling fungal dysbiosis IBD. *PMC*. [cite: 44]
[cite: 11] Orsud, H., et al. (2025). ITS1 vs ITS2 vs 18S. *Frontiers*. [cite: 11]
[cite: 20] Hoggard, M., et al. (2018). ITS1 vs ITS2 vs 18S. *Frontiers*. [cite: 20]
[cite: 23] Orsud, H., et al. (2025). Multi-marker comparative analysis. *ResearchGate*. [cite: 23]
[cite: 16] Nash, A. K., et al. (2017). The gut mycobiome of the HMP. *PubMed*. [cite: 16]
[cite: 14] NIH. (2017). The gut mycobiome of the HMP. *CommonFund*. [cite: 14]
[cite: 15] Turnbaugh, P. J., et al. (2007). The human microbiome project. *Nature*. [cite: 15]
[cite: 74] Andes, D. (2017). Fungal species gut could be linked obesity. *UWMadison*. [cite: 74]
[cite: 75] Microbiota Journal. (2023). Gut mycobiome Type 1 Diabetes. *MicrobiotaJournal*. [cite: 75]
[cite: 76] Diabetes.co.uk. (2017). Research finds link between gut fungi... [cite: 76]
[cite: 45] Sun, S., et al. (2024). The composition of gut mycobiome in metabolic diseases. *PMC*. [cite: 45]
[cite: 46] Zuo, T., et al. (2024). The gut mycobiome of obese subjects... *PubMed*. [cite: 46]
[cite: 53] Buts, J. P., et al. (1999). Saccharomyces boulardii mechanism. *PMC*. [cite: 53]
[cite: 54] Qamar, A., et al. (2001). Saccharomyces boulardii stimulates intestinal IgA. *PubMed*. [cite: 54]
[cite: 56] Point Institute. (2012). Saccharomyces boulardii mechanism. [cite: 56]
[cite: 50] Castagliuolo, I., et al. (1999). Saccharomyces boulardii protease. *PMC*. [cite: 50]
[cite: 51] Pothoulakis, C., et al. (1993). Saccharomyces boulardii inhibits Clostridium difficile toxin A. *PubMed*. [cite: 51]
[cite: 5] Schooley, R. (2025). Extra-bacterial gut ecosystem. *MDedge*. [cite: 5]
[cite: 35] NutraIngredients. (2025). Probiotics may impact gut fungi and bacteriophages. [cite: 35]
[cite: 34] Gut Microbes. (2025). Bacteriophage fungal interactions. *Taylor & Francis*. [cite: 34]
[cite: 36] Gut Microbes. (2022). Phage-fungi tripartite interaction. *PMC*. [cite: 36]
[cite: 37] Frontiers. (2024). Phage-fungi tripartite interaction. *PMC*. [cite: 37]
[cite: 38] Barr, J. J. (2019). Tripartite symbioses. *PMC*. [cite: 38]

**Sources:**
1. [asm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW_BW5LEQdZilLgVKHFr-WxV_B4Y_UbYGHI6ch_Uk41bTcejit3PsiXrdoj1ca8aVSc2LF0Wc58r7RcXzE8wcCUHJpi9PolAVSbnsBnVsJupAuH_u2vjDQgDuhuQdJ5QWpv1t76OI=)
2. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHloVXHZOyfYm5TARielvg9ayAzpcmR1mQDm-ZTRwH5cexkYFxq0Goz8zyXFqz-J6GHbJHVRMdBmMkBd7dZOs6O5Jnv9kwpBqHAhZBZK54FiGQstKZU58MI_TCUynjoJqLye4MXSRSWSG_sBsSqT2yRH4bxHnJFMh9TRoDEwT6fTXsp-ozw4_UZFw==)
3. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBCYBDwIQd69GUumBPGsT2AXKqVnKbAJJXh0BMJIqWmVi-_boJl1NIvDOAvT8Hi7BhL-QdeqQJDeibN5lJTbvcga6BuveMgIkcK-7jKWRmGvnMCN3QmrEa3fehA92-HHMMXktyGOV1hcNBe57uqoFgayJ-yKkJFJBcpho7zzC-NSgzxfhfIgP8ybUTshpDQwWXFdfz8OPz-eZNpaLk6rqAk2RxfRJgQK2WXmK2h-3_XF5buxzEVRnqJuTNYIinCi0=)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsc0XJ3e2STZ-zhG2cB0MqpT_6sUEOMVsg0Lg8RaoCLPhu1_VtJ63OpSrNyT1yHqNBnA44hlDKC78JCymfF_aQX8h6OP41ZUi2RST-89YhGcGCBv8HPFZn9NYO)
5. [mdedge.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHESgS67jp3jmA27Xf1tkkdXUR4AsAwaEv3jB2wuNz_1UMGrgHJh-dSI8BDu5EZWGV5oU9Nt0yuwbOSMSVdENpjv8zk0ubhCR-XmTwso63qAbGib1cFhEglewftq-hhQ48Asmht6AicTTpo0IGpJGlct711pO2aMTjaEvi2-NkaNENXxkb2NZ3RS1PxsLkE3b74ZlFrRgZoYZQO2daI392TJvorp--02NPK3BBFAryCefdVyXIR477y5uGx55uEZmAwOA==)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPwExKIhmiWRY6isH5N3I9gzM83AiHIse0w7h4YPCNJN3zJv-mpitAZjseSac88tgxbtV7a6KA5ulYBsTDNEnTs04bdYhP2Xp4I2mbc1gpQ_evFkwel0Ek9q-KBA==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHDfld3nQMjJSTumGf9_PSxl2hk3b9SeY2gt_w-heZ_NuJ46FJR0By47EW7Y9NLqhErFV0AUZ6Jxyz5yn_98xRI5_FjoD2S-SBivbjwSFMaNJCm7Zulg0tN4djHsxlTybpcfPfmUsG)
8. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYBad3G6QsN_MHxg2PSfNAmBxrfdosDB44YQE6ndimy6ZooaiJnfwsYY_k1Zl0sk8JvaT-l9uWG3xo7lqhTeqcLJY_Q03wpTdg-6_0W2RvOpLAnesxZiSCCcilj9BaVd62EFIBA5IAAYVQ4i40_H-69eo_a_vX)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyz9YYufX9B60qMQWqEIfz7NtI5tIY3Fi4iYO9r9WDKmIycJIa77qbCMTHMIClxs9y20HVCsDZ7mVQoLodIbTWBKIDQN9bgoFVclvfoKrw06AIUkWATzjyMrDAmst3M_6LR1gxg8De)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU9Cp7i1wQsmHP7tFHTciAKUKbWN23oMxfab-BImJyv0t8HdDYi9cGf36m1G5oocDBsh1zSjccLYZVKfsf1WQfJCIBybc9egpsMdPdGh6c_QbnCqCtO4w8Z4-yTO5t)
11. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDoG6s0ubLOo7mkG1OE4YZnXBbqpl97RCWhW4nwuFWJ0wviITP7KbyP0oBFYxj0A5U3qsGRYSfBStHObQsyR-eGDf6OTOSmCK7mpqt__3LI3ccKHrrjcQ87eO75PpnF_rNCFU9LN6JZR24KBollmBznSVEZWVp4zZYySDkp-E6xBhDEqSwduse7VElSPgUmsQX)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLrSXFn9RHZFauY2xAT7KpAve3XiWjpyeiiSgVrtVN3iFJngkp1blPTZ3NiJMD9iANmm-e0tcSfqllT3nu7nP7o1cAOtRcCy6Al0QbOjfC8sUJiewKqEQJGwTVh0waFn7EUBDdRQs=)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTb6NYlKE0ZKgyNa-P5VOFRToG8fAuacYm3-rNZAC_HAFowDfRPDhgTVcP_jBQfkXl8a7JqI8zAE2RV6yZU5qw_yifOOplPkg1DnPoxk-lCnTk2dyH6EbTjQavmLMxWg==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFi2g3RIF3ejVyqWxBdFhYYLbOj_eqryxwhk1owN9gFvytnUhgub7ps8fCi0vNpNRBxY09tCTC_3nE9YFuwsMhS1agPk3RJe25A4-_TWbO_ht5noQ==)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbKGIMV0PbEoOHP__WgB1cdfiaRGuFrVD6gHMAbg4aZuJVm34J4KdP7lkM2vCV6jui0oaNHQGKx03yLbptl4fv-LEqZ6IE2mA7voCF94m_M1ZE_q4FS_eiQW-tbUPbc8g3tCAzcSU=)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOO-iYXmQuY4EdmsMGZdobforZxouDhs_VSQ63CFeikZZPFyWQ9Jnrv4N-bJc-BhMYLl6HMQHS1fxN38R6aERVhrlQKDTSD5l7QSxXTF4dPnV9N43ra9ZHl7xReSMA)
17. [researcher.life](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFREFkkjLmgVJTaagTB13ypWLwT8-B9Y2R8W_oc3pEvcAGt_9ttPiAJlRo1ywoE9rC0s7Fq8GXggM7XnnSFGIAbZgqy5KmdEyF_-Txexc37SRTP9CmHK-nX4WMIvmLGIJPNamB8cH715mtE4a5NjC1szsA3o1kJcfALu46MAK3qxpPyWZukl7lbnHRdITmPeNRqoORD1dDD-Sg1NAiKLE8e_xrEGJkbxG4norZf-0Y5PI3qWs2klxGxTPlpdGnFI60k)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC2sXyWtFd8NOM9jvKrUXGppu0M0c_wMH-3mLvCwpICNTnbbJmvGFREOrDMmkEXD3upxkQf3AQ6MeOEwisQKh4qkHTzCDaCJ4w2oMS8HhmofrwfTyURNZAMqEKc-m8dvflUlPOt-8=)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbNW-6flfFz44msmH9jz_CVJ1S7MlG6E3Oc31baHkNwJ15sq1nWbu5wrCbd8TPrI8SMRLGco7vn74ytNxL9X6ZgoRdZKsYXm85pvcVLUC7yrOpnwMDzd8itKn-AJsdiqftUH_x308=)
20. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMD_1ZmYWSIdX249yE7_kibVYV4JuG4rye9D0PcvvJlALCcRiyp24HW3Rmqs52R2AfTUsXyQobYhoPue4YU4I8HJGuVM_2hcZ2ehsWIsEMJSMHHOh8Uwcek7ivm5ToalR0BJhCbuz1aXLlvUyqsIZFgfvC54l3MGsWP0gYXbbQYb7V4DbkUbkjhqnh67s=)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5cudmqCJrQtyNJ6XSmeqM3sAEcXbvIknQ8aeQMRatgidwW9lVtZw6Y-FbMLuRtQmBMIwAlrI4Vzws7pu7QnICy78sVCTY4xJVN7rU7Nli3zh0jxOHtJVyVIIZ9efZHi4sDW9lXXQ=)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE79KbsNCkxOdA87v333vaZugJxZGX1gWCn-NRxIRjvwqOxuUVRJw9aifJTNc5Na6f1trE1PSEYi5EWg2metI8ucCWzcr50qgXN65EMm-ErbwHVaVQ0tzC0Fo-axj5_ctcsEJZnYbVu)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwIBDfHW6sVL_OpkeoYKeATdI2y4oaxtuyXhDTQ_yy7Wczy9y28B9feXR38r_e3L--boiNik60lLQdomHVdQsLneCuTCngCEzSeurOkXlwT8M33DeKZ7eq7EE6r9d8z-E1yQg4llqXc4FhRiY5Ijt87ekHlCHVSHFFJlSc4G3dK4ocQ0TJ0g5TWKHvHQTK74jIG_TH_5WjJA-vmUVP8FLSo6GM91HWDCoLa6jSodoCK3JPtti7ELAITGmmWRp7MrovbxKPxpD5WRo=)
24. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVMrj4yP3QkUXt69RJRwNS-H0C2xRwIGaYhcX93vMl4JGlM4phD3ye63hOSZnDZS756H7bmGEC1zXq5CnW37RYPWT3B-xlfvW_FnsAONuAM32J9Pe8DbGXrFCVjx06mZ-kSRt7gPBu92_G2ysTILuahNstMmMwaJcI0X7pCi2J5raJBr4bu1H8ELcTfc-j1A==)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbX-EXnLTRpMK_BD-DBTWM37XGiKbwvvuePouXr5IxxO-T1Z49BHVJYfzIwqZ2HbpycnX07qFl-la7DWXQvet7HaqJYpEKJf4HW_i-kJqYQLV9hZ9IQKMfSuWRqX12xj3sq-Yeip32KjcaabnVJK4xlOPS8QFaEMat0D8SSQoCIGe6biTufIQS_X5xhhR1LhQzk9e9RSVrn90X5w-gk27W4voX7E1nUIPRK79yPw==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7rshWLxdiUIxyyzjouVRcfeIuSoBVSTwczT-6i-oVbn45t3G_cO2kV1l9aQLhyT9cr6wdh_M29YZV1Aell0vsZZXd6sgpVcwX3kPlq_qkX0GEytDq9lIAJzXMBZSO3DNcu0DdY8TGEoM3FX3JAN4SqanSvAmkwQL0TWg44N_gILrXhsbg4g7xUK1mQBcwUE-abf_mPLRHq-zN3o1eVNFIqlA4X7-IBV4fvo8GmTqzCkLhKTPFKrSoR7FLd2O8sANpa2Vk-g6-pYTUQpbCIhGxKYuwZiGwWXzwiUs5l8OFCtOcWpMb-UIKHPLyhCeTrPG7lY9MH9iEP3Xbs8aZfiI32gF9EQ==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEHyxo2T4r2VR2ChOsVtt2ue1TEZmVYXgr1Tu3warg5Wn4zLK-yU9PLKY9U-7SQSut2kuh9zCeUpURyIuyTALX-nthpiJQFWYMknI2rLvYsMtCNTTnejf2CpPKAIlkdCJlFy4o0NM=)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-Kc-bTZ01XZsEjb5kDXkKBOq2ZUQUd_p7PruPGaLXcJcDSddHvq_bybWGosdQq0OjEeSjR56b4bk1El0g6us3eKI6DpHCM-6UNPhBFNmSuXFx5wKQv4jdxggbuqQCn9GdP73caQ4=)
29. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVSmSMjzerLECwQDe-PMHWSdMMgxkm0DqAKSB2E3a-uUdgZ_8sJcvUDH2ca2ntLjMTi1PLDrxcd81roEx2dgum-3cZX7-eZt-NsmvWGtk_wA4ouuK9hvFAMidOOVIpKjn_odQda5RGnWlrPHx2mJbwoIA_xzj5)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9EOZ0KbYkuHKgoav_yBla4Y5_4Ef4DiA_khFs_5Bs-u14pnnFMRdls45lMXYkPYAq0PhlcFSFwZzZZRiYsiFlAD9wEhHJn21LckKBd9F73vlTCy00T8KR0PtCUBwR_f5KpLnjm3A=)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGCHc0oLJA4qItC9XDeLro1nugvmw2fBIOPTUORKXxTOxp9DiK0RQWRyFufOaNxm3_sfcw1bAhBgOHzHHZU2-AQ9Ko48gnX5zU59v5ZAvrwI7MIA_l4Ozs83OW0Kpnh6HN-bpBy-y_)
32. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJhgQ4NQN8Ts9gGchfsQ5v85XGFfZNU6qCT-rd_3QOKgucyDymBcTntsbLHRDYeivOK0uGU4mZ0Ycco2o2US1ZlAEeSxCqnpOu5uwum6rnHVVgjz4Rupu7svdbAw8=)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFoJXr8SCYgddcLJnIFqb74o6-5-Ha0U7hUPeJpLQNodIH0Ech6RqA59gSoGnOAAG0ewO_Y0EsfoQroCaOIiBPjxQ6q_ZssbA8Y6oJ1DdWlVswBzX7_TRY-Qjqt4BeJ-50OwYyqZsy)
34. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeyXPApVX4ISPhstjsqKo0XGoJXjv1ulsOq7AmEXioofu6Y1ftborP7IF5UO7abEIRzQscPAvcN3YYVmHJkav0l_FOhbiTZgalYsRvTdmAWFbYEwauCbk9JBO3bRrlyuXhV6qxtBkQgVHJaNqgmJpGcuHzzJC-FA==)
35. [nutraingredients.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJ2JzD8NVm0bBb3e4lsRQXpsOCocBpC8Z3WF8AmieZd94OCSBqE6FkHLZkxxGLqtmwIYXuZ5qjkcMdBd4AmOklUfJDiFZ8TmxSukvSsz4dHk2-rQB2Ij3FzStzuiqrBCnRWsBrkcfIiGGab1gAxxjPFI_3xcknmtPVawwnKLxtauF-2oBGRuCYIhkOvzrQX5g8VJbz7bdnrbm1BuI=)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh6ovPRvc0_yTLVofMqlm9xVOBxPrqQeGg8m0lKCL27gkhoUSxkDXd3uusYwxl0J3iYTWEUFzhY-nkpjX_fiSRBn4-_tVEXk2XfrwkhaSjK8eLLuZaOwbVBXw7FUGvowqKMeNY7_o=)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbaM3Y6_jHddJ3km_0n2ZJBstB8XxqGqMRdoK5Yazb-gX5C-s9wky46ihfLMCmW7QRiSY8Eb-GDlWS6bWlhBlQF3oHRc4ozvGGJvJ1LBR6BsJA_ZawpPiQ7VKyx0kJq_4Kchs1xwZI)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsuBnk7g1ElGWG-xXN1ji1RN3XDUASLYlLWXxHgz7rNwa6Ce3QNClQIOWL_oDATPL4ZDZZR2d4coS3Q0iBpYF_PKB7eWGmgJKIl8GY8pdMgYzwi4AG9sAJDPULgCjMkabC09ncU3k=)
39. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1vX8EzSG_OGv74CE9_L9iVrHAuz1UrwicSqE6dnmfraX0WV3VWTqj20qv7jpVqdfEFwggXv3mLZAsOpYkJEEARn6CibN7_H4prRr7t_6yRxhMX4PJfZsd18TLQ2u8hfvi8TyupSyiTsTbIuaaFCxSW-ni2EhWBw==)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTV15Tga8TxDL7rkUgLfZEmyNMXn7eWEwJdZFMDZhsfpdjPXb2LPSd3WGpABazlBIybvjZ2_g6Q_C0mxAz3Dc9z8bQuwYeRkizyFXaYHCgIqYGHEGWXPpxLBIC76SK7Jegtj4abOrV)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoZydPQCQ3HmUa1Sb0dNNI__4ZkWLwhfBBzueEOBf8Y3p_XNBdl30BzLKgTdEgjVF1QVe563hoCPdP3pWFcG64Ns8Yqx_dEuCMgW9oRx7VR7x1UNISogEv01UieeHcgfx6ExjU2spt)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0uVc0vU-jyNd0YqU9xyPxn9g-WbImbDWK-9xoSKZS4QbFY85guM2qzSNXNdfLOWsZW9j5NU4bxopoQjWc5gJSXgJ1H60gTyG0Q67OyXac2bPYy8bJcdPsYxCNr-8-AZBrc8DrDdA=)
43. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUXns4Ib5nXXmIDDqDJsDJsEFAaDU6wi-BAr7_whL8ryh0Va3tPem04uXs9e_Hg6e9pmtf5fN2WixcVT_KDKCw5EB8EmhyZ4Q7tqxOwgdE1N0f2wHf6aFf4qm_lxjQRrxe81Vl0lI=)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGHcHCHP0cj8gigFJRzwzQFCi-mBUQuvdyFhPSQLuWanZbZYDZ029esHR2mnxKGoarV7ZsZvXszNbO67r8D4e41ZQbGQPyEOIyk2MdbA__ACyPoWUTCKARxYvshdAY824cRSCVt_H-)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeFulFq0g0mGUTTVOjrMeXwlvpu9yfwHdMrDJ_dbc8F7gEIJgURqp5keyXQRPtI3L-f593EUkUGEbynMXi38QSZQHUSKYVH_61zUhIE-obW4F9OZ5hQkbEtOB8_X_IViy2gtGGLAJL)
46. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFYjvwPrWp6861GErQdVA0EE884lBif_Ur4mJdzh8AhHaJ6Zxh1J2ELu_nTmEEfwyO5MLY-G5FUUrJKSjnMIKY8tHIc0bLXBcJyDL4lt-H-sjSUVHTfFkkxFCO47tG)
47. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvsc2Df2AwY8wmI71VN3J57QBn1y-aklrevpCS5INFXkecKqJkHmwsmygBNYITumipcgQvzz-LfT_wpWRtflMz1kxw4gklE9DzUEzlF0NqCyaT_Ou9B0-J7PspTdY=)
48. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqQKiP6RN3m2SAwvT_VngAQ96k1C1tWn7uPY_FZhNDhFQDmd83yLsnQEjVRr3-hzXMUcTUo1uxqf9x1yY0ber5QC75AAeSdidWRAqZ2U4RGDqxQIl8dbUPTXROKQ==)
49. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXGIGx4wvr1FljQZOhu_3Kzeny0lIGztAmQAixquhKPe4HKJWpCEVOI-Kw77bE6SB-0TeMQWvzl_44dQK7nX3uiz1846-HSDN_JBSgxyD9orVEbyOQeezAT5r0voo8eJstYjNqKz6LBUTqJ7ZTdQGmfS1fO7merQ==)
50. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8ZTCnyD4hYMqVwIQL2nRiyOVjnpLe6LktkV7GUbPThMON1Bjz4fQZ2eIXZor781lPN595QEzRVmuN9DCAypar4iK2Sg_RwZzTT78I7DNokkFubetEg0fR-umSOuDWlgyyL_Du)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYYeNrMESwoj5pzx6bE5Cy46Wlk6tuC5Z3IboOS8SmXZ36zN1MoCOw-Y0VMdA_Ja7-8VX2vnC430WKW8upzFlPMEY1T25UQycptfOxKOaPuZUNhuzhscARcxbImiU=)
52. [saccharomycesboulardii.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1MGST63l57_CoLDS2KttQ1A92Fa0DisRQ-nmwBvVmZX1B2M7quvgYO2fJ9OhAgMJ8OhB-La9UmXS9vGCF1upGOI-9T6scBWwXez6vwz1SOckDnEdy4JHZjKXlQzVqjHmB_8VC_Lwnu7UcbnBD678DrOXVqDD2yZZcF-yEIWK6kb51DNhCraeG)
53. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbUWyjmVAhhWnbuLCuJ-_ZaQu_7ixQetE_sPLq0Azl2N15dv2pB5jM6Ea0tbI4oV_cv24vZ62KasSINIspMNcc56RpoW4j9SHQ6-GxR9KHYY-6yg0SXHSZvFrU-6V6MN1x3FxY)
54. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuxwl6-hMsEjkQ89FZSD5GtjuqDp-T6esOwrawKqZKQ28AX7GNiBCDJpXvNJr5XEiT43yHLs1F4Zs7LRXItzu2j3WazSYw9RFn08732xCBxztZUCH7GT5N0p3dg0Yh)
55. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE377zDW-oczmpM3BQc8QYVfRsrKSaULlz9Wh4fiwIjDMmpgc4vrX-lJHPyqAA6w6LLFbztqqDvwAti1GtDMY-dZrGTcHfzymmi1kOWwNP_kCiVCcqwgGjivIbusZXwI6JX6KvCAx0=)
56. [pointinstitute.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFy17bfQybAQi1jxdLg0yXYiQH2U5Y6gjmO7T8VNmkC9HbPjhDIcWo9AesLFP2pZvE8hWNAvHQhgpueFPO_TxiPB4nDPAjiB35kDZ3wTQKfT-QQyVlbwCBeN7PZNj_zD8xvrTL9tkUDkWqyj5oNiJtD6fCZQnXfZKoHhglj4T9YszEUw2689r1Ow==)
57. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXk6f1S-KirdVmVP7ezj5NZJ4zy6kWzPYcKB6IOKp4g-KLkKw95YP4F3BxEae4JFpX6CcBATC7k9BD9ZlorbE3d6jsmPGz9Xmh2QfyAS-BkIqAExRVaYuU2dUY6g==)
58. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExronfOp-ibI8UyksE44QWIb8m7YEbJYIw7Vx5Urli2ZOB2EMXtfT6Xjwy4zf-KO8otoFM3mQd26pfq-RQw-C12VMWu6FT6XPYFLtnQ7kwOnnubp-DSRUq-r-PCR-lPU8fbjLjkOxDwRZ7U-Ex)
59. [gutmicrobiotaforhealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvWAK8G4L2MzSeXQhGC6a3OErQZOP-3AtkGOPKXOfw9MAqcmih6VxueYalZYHuTqsCzAagNk4Feqsy-NJwbSpD4DyXU4DVCC23qTj0udabw0Vr4wGg7MN-Id7D1ZZjarN5Yc4t013SwfTiarcDTPnmDSJFjWesuP5UHYDeA0-eNNV8N87Stk2MT2CU)
60. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4b1YQctU12qWlfDvCRfKEMnAz6apBPQ9FePqSn6uoe9ADnLzrPt_XwVKcy0dfEtV-n0a0Vj8prCwkf3d0D4AlAdl0FzUPVMZBl6GRRZ4biy7k8VxIVWQnpHmfrHYgztJU1-o84Qp1)
61. [microbiotajournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF13Fxb22qZra52okOzpVjDiBjFkrHungpbhL0qoWYK_P8801jLBDj1iVtxNp75AuskuQxJACHY6sZBtLQ2CgtqwD4MQLu4qfmfwwgx__HgTmTzTGANGQ8cbE6p9ktXdbsKtOmrD_6v6nhRJ4JwSPl4SykWuxLt8cU5jsvFuvI82lYhAzm4iLWZzqpIkjEo_iLgd9DdlunD0b26PWpvSWkM1JJ93WSagpEWCJN8HR6AYtMUmZ_KmHORwKNYo6Bfh_RCtV55yyHdTPCEIIkaC_hFK1T2edrXm55QdG88Y-jzmhll09fx9pAZGNdEVqNbx4CBzeVrxe04lL13Mrx2aLyQpqyxPljuQFcxkHJln7_bNXB9IzkCaVzJ719c2Gv3sWKJZq5zPw27vNq5HOJdKDo=)
62. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGJmJQU9m0hrwtypT-WiV56UuYp33AJRJPoOv7qcdSqJJc0mXtJ6Gd1BmEnUR1X--6_vJFtN7tKPIzB5yJosER53O2dpMkzGwfZyl8A0AsSaFtWXUfeTNmugi41bRKW2lwKKa9d3bCfC6HRU0caw5p0JwaAmX29lGdD_wgsJMckNlnbLjf0hu6UVO3Q9GQqDvdrggRa7-j4JzVYemzVRwsl7JQmbfYjzocE0VtbPYn59NkZV-_E0qSW0NteImNLPHd3lUC2d_tV3yr6cdnA4ia9MR38BuaNKvhsnqR9ExRsQ==)
63. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXXBeMydlacRuBqkFQEa-BRrcIcqMR2UEAhCniZl8gPEABq49KPdomlKnESHNZ5irSXEfSmHcZDN2lBwTSw7XygJ4FhQYfkVAq0rLYiPzXavFlP0iXx-B3u62bC4Ly)
64. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlFFhiR2BRgPpB4pNUiB12sqzGi5pAq09snkd3dwK2oyW5Ac9-PMCtoXmqdkpU-G2LBzOFsDx8-6V2FUPRURLhcGmtUJxfVha2R3q165Kfv9PvGRTQs2yMY71mcrtHg4DFIwlWVuotz-AvoW3l14vzumSEdHeB23hysC_YWt2jhxGVqgKwkqaTIbKmYxDQrCC9bajB7GGM)
65. [consensus.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG214CCQhcnX_2b8OebyPx9PFPCCT7CZxU7qKQmjgUsRJFrcToGatpxIXd98YS_zjjhNbwfDwAVyna1dxa_p6oGqDU96N7w5_Z5MuZkxg04firWhy3e1OmBkXP3xMl1T5oJnsCnSEsYeL8eUPEJru1uIMqr7ONIpRo6v32cjEMd1vVJ2j3tmEqdKwIj9MDosDGg-HhBsIW1Qi6wgLk=)
66. [saccharomycesboulardii.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0bKAaXiRgDuXqK49axoB3ZKeptstzzOcCrIuN6uxTbwPP83CxDjQIBSHmmvHj19sYzmwR5xfV0CguX7eqblJAF8PNGU_a7Bc0rOU1WHiPpDrjZHNWoYnlyECBKmCLikaOu-t0hJKCScxbmniY7N6XB5so2stK7n8Lk3JRxMizyhioO5WrKxKrDYZZ4-IofDt9519W)
67. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDkTA-InVurgKQEh8cvGArr7WMhRqTW1haiXX_RGiGHOF-Z4-tlj662AuofOZGuIZD3LvUwk5i7gXlBkY21HiIdGqqYmcorOrVh1IZiA3292Ok3n2tSxOwceE6VWt0)
68. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFshCL7wSmTzAeaWHK1Pa7ar8rEqvpfpgb0trdjWmX5RlBbc5XbjVtVkmKF39ktkx0-WDenNOBxpehjQ1-oaPFObTrqIc4hY-tU4jCBK35iRwY2Ofa4S0PKhlju09p_US8eUdpzhr0h)
69. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVHxJIhtRCHK9tfQXr2IQ3Im4cfYqyuWir8b7CA-3IKRBzf7N_bRBh3Z98NvQ3kbfwk_N6Dvlp_h_iqvO9fdtw4V0WRgYhFifD8h95XCWonDr4lqEG7ZI3nWcurbFJ2Ci4EqCcYU8=)
70. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNwxgX3QRCty1HwNs-g2QEgyqVpGO4HRhMMbFEH51QyZPaIpVBEYNn-eoHng0uKV3iPl-vvhVw5LbeBoPrr7367sxTno6JcbXJjB-09nyETn89fUaeQ1ViKfyTFuKI0tHSxtFMxJQO)
71. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8v_djG4c_LrWJ5oSAeOhjLEuSjiu26Kt5YvytE9Zkc5Uze1pPsoeVNINmULaSAUgDaDdKNU-9pKrjedOJ8EsQ4CZEA_onXVxsZvHCbLv_HawhFqDVMTGn35iiM0sBUp7wrxUU3ocHtu98yyw4E5H_eil3Ojj0l5g1os5X9OrHHrGiOq4LLb2IVvnM4cgiXxHLBktrS2zGcRjXnQ6WbfDBaXqskz6Kbjl0)
72. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlHjKOAWsWNI2nwkcSUQ-iQUHWu5wfZfFaOGsDsZyL_phGfoYIsiLiMkNmd11QK85_wYgUnMNqHwtZsqkmSemzI5buP6juZisloAeHpnDPMQu3JoZejo6bU9mQKnEKoYhAg-aVJi-uQSp0-g==)
73. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Rk39ycSONbd3vx4dZGbnV_cNuo3sCxnXVuiiVUOJEDuvyh5ZELxDxaYpgvuRjg2RyBGhc1IQIPhhNpD4qG5qYGoSc2Iul2CpaWqPrq9jZlv7nAqLEI5-mEOPBTtDhqSDoJAc091LXsaatXvvYsv1u7S58LzOhTjLeD2y7Hn4FbcpqySaUMtQ58Q=)
74. [wisc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFel09ASt25SlvWQUe5hqnHumv3KBEBKywNuP280cCebJFyVChuF89Vz7HhkIqCIAyRTScGIVyrVOdzPp2_pkENV9xD2mJnAgCHcAiWcHxE8YKfCjiVt-ntFIMyYAv__WzKxrjGFqZ12FbhOSrR2OUUaLKsTxnP4VWPophiLCLq_dSvEVdAzBGmtGdFdfRM9XlXYXecJ7Q=)
75. [microbiotajournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFOKqBarCyf75gIXeb1DFYqbx53Y9-lX3VtO4Ek6f2m4ycDS-QJW4Zy1C9G1ntepPGdZ5Yu6B_HgTlWKn2fI1nf1k3o6InapHjbGqKmDzFuRVOvvFtEXiXQlal8paVy4wdLJ99DYACPP4gOOAaX6vPwKbvgWbvfESuzSQFVRoot0oV)
76. [diabetes.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8-0S9nAHvRSb1brhVMAhYfTBYwFTqVDmotbCd5Tiq-rb-MN-grONS4sMzLvVyLuYkaQov0vdPMnQipyw0yU9-lu71XRd6i69vBm5p8wCyzta3YWHSZ0LQjV5sfSRDcZr5fQvbrrESb9XQ9qPkLwvPi6xz0uUAcGoRmc3d9tcuOa1Ljf1jxkikZyyvjfeFN4uvMq1L81Ayefsb_6cHd9AXhQbaBtaq4g==)
