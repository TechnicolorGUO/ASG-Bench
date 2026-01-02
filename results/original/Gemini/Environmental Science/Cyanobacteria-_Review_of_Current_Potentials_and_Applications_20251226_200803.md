# Literature Review: Cyanobacteria- Review of Current Potentials and Applications.

*Generated on: 2025-12-26 20:08:03*
*Progress: [23/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Cyanobacteria-_Review_of_Current_Potentials_and_Applications_20251226_200803.md*
---

# Cyanobacteria: A Comprehensive Review of Current Potentials, Biotechnological Applications, and Future Horizons

**Key Points**
*   **Evolutionary Significance:** Cyanobacteria are among Earth's oldest organisms, responsible for the Great Oxidation Event (~2.4 billion years ago) that enabled complex life.
*   **Biotechnological Powerhouses:** They are increasingly utilized as "microbial cell factories" for producing biofuels (ethylene, hydrogen), bioplastics (PHB), and pharmaceuticals due to their ability to fix atmospheric carbon and nitrogen.
*   **Recent Breakthroughs:** The 2024 discovery of the fast-sinking strain UTEX 3222 ("Chonkus") and the application of CRISPR-Cas9 to increase succinate production by 11-fold represent significant leaps in carbon capture and metabolic engineering.
*   **Economic Challenges:** Despite biological potential, techno-economic analyses (TEA) reveal that biofuel production remains expensive (e.g., $15.07 per gallon gasoline equivalent for ethylene-based fuel), necessitating improvements in downstream processing and strain productivity.
*   **Bioremediation Efficiency:** Strains like *Oscillatoria* sp. have demonstrated superior pollutant removal capabilities, degrading 95% of pyrene in 30 days, outperforming many eukaryotic microalgae.

---

## 1. Introduction

Cyanobacteria, historically misclassified as "blue-green algae," represent a phylum of photosynthetic bacteria that have fundamentally shaped the Earth's geochemical and biological history. As the only known prokaryotes capable of oxygenic photosynthesis, they occupy a unique evolutionary niche, bridging the gap between simple bacterial life and the complex photosynthetic machinery found in eukaryotic plants [cite: 1, 2]. In recent decades, the scientific focus on cyanobacteria has shifted from purely ecological and evolutionary studies to applied biotechnology. This shift is driven by the urgent global need for sustainable, carbon-neutral solutions to energy crises, environmental pollution, and food security [cite: 3, 4].

The motivation for this review stems from the rapid expansion of cyanobacterial research, particularly in the fields of metabolic engineering and synthetic biology. Unlike heterotrophic bacteria (e.g., *E. coli*) that require organic carbon feedstocks, cyanobacteria utilize solar energy and carbon dioxide ($CO_2$) to synthesize biomass and valuable metabolites [cite: 5, 6]. This photoautotrophic capability positions them as ideal candidates for "third-generation" and "fourth-generation" biofuel production, which avoids the food-vs-fuel competition associated with crop-based biofuels [cite: 7].

However, the transition from laboratory promise to industrial reality is fraught with challenges. Techno-economic analyses (TEA) consistently highlight the high costs of cultivation and downstream processing as major barriers to commercialization [cite: 8, 9]. This review aims to provide a comprehensive, systematic analysis of the current state of cyanobacterial research. It covers historical milestones, key biological concepts, state-of-the-art genetic tools (such as CRISPR-Cas9), diverse applications ranging from bioremediation to nutraceuticals, and a critical assessment of the economic and technical hurdles that must be overcome to unlock their full potential.

## 2. Key Concepts and Definitions

To understand the biotechnological potential of cyanobacteria, it is essential to define the core biological mechanisms and terminologies used throughout this review.

### 2.1 Oxygenic Photosynthesis and Carbon Fixation
Cyanobacteria are Gram-negative prokaryotes that perform plant-like oxygenic photosynthesis. They possess thylakoid membranes housing photosystems I and II, where light energy is harvested to split water, releasing oxygen as a byproduct [cite: 1, 10]. The energy generated (ATP and NADPH) drives the Calvin-Benson-Bassham cycle, fixing atmospheric $CO_2$ into organic carbon. This process is facilitated by the enzyme RuBisCO, which is sequestered in specialized protein micro-compartments called carboxysomes to enhance efficiency [cite: 1].

### 2.2 Nitrogen Fixation and Heterocysts
Many cyanobacterial species (e.g., *Anabaena*, *Nostoc*) are diazotrophs, capable of converting atmospheric nitrogen ($N_2$) into ammonia ($NH_3$). Because the nitrogenase enzyme responsible for this process is oxygen-sensitive, these species have evolved specialized cells called **heterocysts**. Heterocysts provide an anaerobic environment for nitrogen fixation, allowing these organisms to thrive in nutrient-poor environments and serve as natural biofertilizers [cite: 11, 12].

### 2.3 Secondary Metabolites
Cyanobacteria are prolific producers of secondary metabolites—organic compounds not directly involved in growth or reproduction but essential for defense and adaptation. These include toxins (cyanotoxins), but also high-value bioactive compounds with antibacterial, antifungal, antiviral, and anticancer properties [cite: 3, 13].

### 2.4 Biorefinery and Circular Economy
The concept of a cyanobacterial **biorefinery** involves the integrated production of energy, chemicals, and biomass from a single system, analogous to a petroleum refinery. This aligns with the **circular economy** model, where waste products (such as wastewater or flue gas) serve as inputs for cyanobacterial growth, closing the loop on resource utilization [cite: 14, 15].

## 3. Historical Development and Milestones

The history of cyanobacteria is intertwined with the history of the planet itself, while the history of their study marks the evolution of microbiology and biotechnology.

### 3.1 Geological History: The Great Oxidation Event
Cyanobacteria are among the oldest lineages of life on Earth. Fossil evidence, including stromatolites, dates their presence to at least 2.7 to 3.5 billion years ago (Ga) [cite: 2, 16]. Their most significant contribution to Earth's history is the **Great Oxidation Event (GOE)**, which occurred approximately 2.4 to 2.1 Ga. During this period, cyanobacterial oxygen production overwhelmed the planet's natural sinks, leading to the accumulation of free oxygen in the atmosphere. This event caused a mass extinction of anaerobic microbes but paved the way for the evolution of aerobic metabolism and complex multicellular life [cite: 2, 17, 18]. Recent phylogenetic analyses suggest that multicellularity in cyanobacteria may have evolved as early as 2.3 Ga, coincident with the rise in oxygen [cite: 19].

### 3.2 Scientific Milestones and Genome Sequencing
The modern era of cyanobacterial research began with the recognition of their prokaryotic nature by Roger Stanier and colleagues, who proposed the name "cyanobacteria" to replace "blue-green algae" [cite: 1]. A pivotal milestone was reached in 1996 with the complete genome sequencing of **_Synechocystis_ sp. PCC 6803** by the Kazusa DNA Research Institute. This was the first photosynthetic organism to have its genome fully sequenced, providing the genetic blueprint necessary for modern metabolic engineering and systems biology [cite: 1, 20, 21].

Following this, the sequencing of *Synechococcus elongatus* PCC 7942 and other model strains facilitated the development of genetic tools. In recent years (2024-2025), the discovery of novel strains such as UTEX 3222 (nicknamed "Chonkus") from volcanic seeps has marked a new milestone. This strain exhibits rapid sinking and high-density growth, traits that were previously elusive but are critical for industrial carbon sequestration [cite: 22, 23, 24].

## 4. Current State-of-the-Art Methods and Techniques

The advancement of cyanobacterial biotechnology relies on sophisticated cultivation methods and precise genetic engineering tools.

### 4.1 Cultivation Systems: Photobioreactors vs. Open Ponds
Cultivation is the backbone of cyanobacterial biotechnology.
*   **Open Pond Systems:** These are cost-effective and scalable but susceptible to contamination and water evaporation. They are typically used for robust species like *Spirulina* (Arthrospira) [cite: 25].
*   **Closed Photobioreactors (PBRs):** PBRs offer controlled environments (light, pH, $CO_2$) and minimize contamination, making them suitable for producing high-value pharmaceuticals or genetically modified strains. However, they are capital-intensive. Recent innovations include using industrial flue gas as a carbon source in 100-500 L PBRs to produce compounds like squalene [cite: 7].
*   **Wastewater Integration:** The "ReNuAl" process exemplifies state-of-the-art integration, where cyanobacteria are cultivated on dairy manure wastewater. This method recovers nutrients (N and P) while generating biomass, effectively coupling waste treatment with production [cite: 14, 26].

### 4.2 Genetic and Metabolic Engineering
The application of synthetic biology tools has revolutionized the field.
*   **CRISPR-Cas9 and CRISPRi:** The use of CRISPR-Cas9 for genome editing in cyanobacteria was initially challenging due to the organism's oligoploidy (multiple genome copies). However, recent protocols have successfully utilized CRISPR-Cas9 to trigger double-strand breaks and enforce selective pressure, allowing for precise gene integration. A landmark study demonstrated the use of CRISPR-Cas9 to knock out the glycogen synthesis gene (*glgc*) and knock in metabolic genes (*gltA/ppc*) in *S. elongatus* PCC 7942, resulting in an **11-fold increase in succinate production** (reaching ~435 µg/L) [cite: 27]. CRISPR interference (CRISPRi) is also used to repress specific genes without permanent deletion, allowing for dynamic metabolic flux control [cite: 28].
*   **Metabolic Flux Analysis:** Advanced computational models and isotopic non-stationary metabolic flux analysis (INST-MFA) are now used to map carbon flow in engineered strains, identifying bottlenecks in pathways for biofuels like ethylene [cite: 29].

### 4.3 Discovery of Novel Strains
Current research emphasizes bioprospecting for "fast-growing" strains. Strains such as *Synechococcus* sp. PCC 11801 and *S. elongatus* UTEX 2973 have doubling times significantly shorter than traditional model strains, making them more competitive for industrial applications [cite: 29, 30]. The recently isolated UTEX 3222 ("Chonkus") from shallow volcanic vents in Italy is particularly notable for its high density and rapid sedimentation, which naturally addresses the costly harvesting bottleneck [cite: 22, 23].

## 5. Applications and Case Studies

Cyanobacteria are being developed for a wide array of applications, categorized here by sector.

### 5.1 Bioenergy and Biofuels
Cyanobacteria can be engineered to secrete fuel molecules directly or accumulate biomass for conversion.
*   **Ethylene:** Ethylene is a critical feedstock for plastics and fuels. Recombinant cyanobacteria expressing the ethylene-forming enzyme (EFE) can convert atmospheric $CO_2$ directly into ethylene. This pathway is a major focus of techno-economic analysis due to the volatility of the product, which simplifies harvesting [cite: 8, 31].
*   **Biohydrogen:** Cyanobacteria naturally produce hydrogen as a byproduct of nitrogen fixation or through hydrogenases. While promising, oxygen sensitivity remains a challenge for continuous production [cite: 9, 13].
*   **Case Study: Techno-Economics of Ethylene:** A detailed TEA by NREL analyzed a conceptual process for upgrading cyanobacterial ethylene to liquid fuel. The study projected a "midterm" minimum fuel selling price (MFSP) of **$15.07 per gallon gasoline equivalent (GGE)**, with a long-term target of $5.36/GGE. This highlights that while technically feasible, the technology is not yet cost-competitive with fossil fuels [cite: 8, 31, 32].

### 5.2 Bioremediation and Environmental Management
Cyanobacteria are excellent agents for **phycoremediation**—the use of algae to remove pollutants.
*   **Organic Pollutants (PAHs):** Polycyclic aromatic hydrocarbons (PAHs) like pyrene are persistent environmental toxins. A comparative study found that the cyanobacterium **_Oscillatoria_ sp.** degraded **95% of pyrene** within 30 days, significantly outperforming the green microalga *Chlorella* sp. (78.7%) and other bacterial consortia. This efficiency is attributed to the secretion of enzymes like polyphenol oxidase and laccase [cite: 33, 34].
*   **Wastewater Treatment:** The ReNuAl process utilizes cyanobacteria to treat dairy manure effluent. The system captures carbon from anaerobic digestion biogas and recovers nitrogen and phosphorus from the manure, producing a nutrient-rich biomass that can be reused as fertilizer. This approach mitigates eutrophication risks while generating value [cite: 14, 26].
*   **Heavy Metals:** Species like *Anabaena* and *Synechocystis* produce extracellular polymeric substances (EPS) that effectively sequester heavy metals (Cu, Cd, Pb, Hg) from industrial effluents [cite: 35].

### 5.3 Pharmaceuticals and Bioactive Compounds
Cyanobacteria are a rich source of secondary metabolites with potent biological activities.
*   **Therapeutic Agents:** Compounds isolated from marine cyanobacteria include dolastatin (anticancer), cryptophycin (cytotoxic), and cyanovirin-N (antiviral/anti-HIV). These metabolites are being investigated for their potential to treat diseases ranging from cancer to COVID-19 [cite: 13, 36, 37].
*   **Nutraceuticals:** *Spirulina* (Arthrospira) is commercially established as a "superfood" due to its high protein content, vitamins, and antioxidants (phycocyanin). It is widely used as a dietary supplement and natural colorant [cite: 3, 38].

### 5.4 Carbon Capture and Sequestration
With the escalating climate crisis, cyanobacteria are viewed as biological carbon sinks.
*   **"Chonkus" (UTEX 3222):** This newly discovered strain offers a novel mechanism for carbon sequestration. Its large cell size and high density allow it to sink rapidly in water. In an industrial setting, this trait could facilitate the low-energy separation of biomass from water, allowing the captured carbon to be dried and sequestered or utilized more efficiently than buoyant strains [cite: 22, 23, 39].

## 6. Challenges and Open Problems

Despite the immense potential, several critical bottlenecks hinder the widespread commercialization of cyanobacterial technologies.

### 6.1 Techno-Economic Viability
The most significant challenge is economic.
*   **High Production Costs:** For low-value commodities like biofuels, the cost of production far exceeds market prices. For example, producing the bioplastic polyhydroxybutyrate (PHB) using cyanobacteria has an estimated break-even selling price of €7.7–449/kg depending on the scenario, whereas the market price is around €4/kg [cite: 15].
*   **Capital Expenditure:** Closed photobioreactors, while efficient, require massive capital investment compared to open ponds or traditional agriculture [cite: 9].

### 6.2 Downstream Processing
Harvesting and dewatering microscopic cells from dilute cultures is energy-intensive, often accounting for 20-30% of total production costs.
*   **Dewatering:** Traditional methods like centrifugation and filtration are too expensive for bulk commodities. Flocculation and natural sedimentation (as seen in strain UTEX 3222) are potential solutions but require optimization [cite: 15, 40, 41].

### 6.3 Scale-Up and Contamination
Processes that work in the laboratory often fail at scale.
*   **Contamination:** In open systems, fast-growing heterotrophs or grazers (zooplankton) can decimate cyanobacterial cultures.
*   **Light Limitation:** As cultures become dense, self-shading reduces photosynthetic efficiency, limiting biomass productivity in large-scale reactors [cite: 25, 42].

## 7. Future Research Directions

To overcome current limitations, future research must focus on the following areas:

1.  **Advanced Strain Engineering:** Continued bioprospecting for extremophiles and fast-growing strains (like *S. elongatus* PCC 11801) is crucial. Genetic engineering should focus on improving photosynthetic efficiency and carbon flux toward target products using CRISPR-based tools [cite: 29, 30].
2.  **Synthetic Biology and Standardization:** Developing standardized genetic parts ("CyanoGates") and robust expression systems will accelerate the design-build-test-learn cycle for metabolic engineering [cite: 29].
3.  **Integrated Biorefineries:** Research should move away from single-product models. Future facilities must co-produce high-value compounds (pigments, proteins) alongside low-value biofuels to ensure economic viability. The integration of waste streams (wastewater, flue gas) is essential for reducing operational costs [cite: 14, 15].
4.  **Field-Scale Trials:** There is a gap between lab-scale data and industrial reality. More pilot-scale studies are needed to validate TEA models and test the robustness of engineered strains under fluctuating outdoor conditions [cite: 42].

## 8. Conclusion

Cyanobacteria have evolved from the architects of Earth's oxygenated atmosphere to promising agents of a sustainable bio-economy. Their ability to utilize sunlight and $CO_2$ to produce a vast array of compounds—from fuels and plastics to medicines and fertilizers—offers a pathway to decouple economic growth from fossil fuel consumption.

This review highlights that while the biological potential of cyanobacteria is immense, the technological and economic barriers are substantial. The field has achieved remarkable milestones, such as the sequencing of *Synechocystis* sp. PCC 6803 and the recent engineering of *S. elongatus* for high-yield succinate production. However, techno-economic analyses indicate that for commodity chemicals and fuels, current technologies are not yet cost-competitive.

The future of cyanobacterial biotechnology lies in the convergence of synthetic biology, process engineering, and circular economy principles. The discovery of novel strains like "Chonkus" and the refinement of CRISPR tools provide optimism that the biological limitations can be overcome. If downstream processing costs can be reduced and productivity scaled, cyanobacteria may once again play a pivotal role in reshaping the Earth's environment—this time by mitigating the impacts of anthropogenic climate change and pollution.

## 9. References

[cite: 33] [cite: 33] PMC8839941. (2022). Cyanobacteria bioenergy and bioremediation review.
[cite: 43] [cite: 43] ResearchGate. (2025). A Review of Microalgae- and Cyanobacteria-Based Biodegradation of Organic Pollutants.
[cite: 11] [cite: 11] ResearchGate. (2016). Bioremediation and cyanobacteria an overview.
[cite: 35] [cite: 35] ResearchGate. (2025). Cyanobacteria-based bioremediation of environmental contaminants: advances and computational insights.
[cite: 1] [cite: 1] Ohkawa, H. (2020). Scientific history of cyanobacteria research: Achievement of Roger Stanier.
[cite: 44] [cite: 44] Bristol University. (2022). Evolution of cyanobacteria through geological time.
[cite: 17] [cite: 17] Watersheds Canada. (2025). History of cyanobacteria.
[cite: 16] [cite: 16] Caister Academic Press. (2008). Cyanobacteria and Earth History.
[cite: 2] [cite: 2] Wikipedia. Cyanobacteria.
[cite: 3] [cite: 3] MDPI. (2020). Cyanobacteria biotechnology current potentials and applications review.
[cite: 12] [cite: 12] Open Access Pub. (2022). Cyanobacteria biotechnology current potentials and applications review.
[cite: 13] [cite: 13] MDPI. (2021). Cyanobacteria biotechnology current potentials and applications review.
[cite: 4] [cite: 4] PMC9785398. (2022). Cyanobacteria biotechnology current potentials and applications review.
[cite: 10] [cite: 10] PMC10301180. (2023). Cyanobacteria bioactive compounds applications review.
[cite: 36] [cite: 36] Biomed Grid. (2022). Cyanobacteria bioactive compounds applications review.
[cite: 37] [cite: 37] PMC8146687. (2021). Systematic review cyanobacteria applications.
[cite: 40] [cite: 40] PubMed. (2019). Challenges in downstream processing of cyanobacteria.
[cite: 41] [cite: 41] ResearchGate. (2025). Cultivation and downstream processing of microalgae and cyanobacteria.
[cite: 42] [cite: 42] Taylor & Francis. (2019). Challenges in downstream processing of cyanobacteria.
[cite: 45] [cite: 45] JEBAS. (2024). CRISPR-Cas9 cyanobacteria metabolic engineering recent advances.
[cite: 5] [cite: 5] Elsevier. (2018). CRISPR-based technologies for metabolic engineering in cyanobacteria.
[cite: 27] [cite: 27] PubMed. (2016). CRISPR-Cas9 cyanobacteria metabolic engineering recent advances.
[cite: 30] [cite: 30] Frontiers. (2024). CRISPR-Cas9 cyanobacteria metabolic engineering recent advances.
[cite: 6] [cite: 6] ResearchGate. (2025). CRISPR driven Cyanobacterial Metabolic Engineering.
[cite: 8] [cite: 8] NREL. Techno-economic analysis of a conceptual biofuel production process.
[cite: 31] [cite: 31] OSTI. (2016). Techno-economic analysis of a conceptual biofuel production process.
[cite: 32] [cite: 32] RSC. (2016). Techno-economic analysis cyanobacteria biofuel production.
[cite: 14] [cite: 14] ChemRxiv. (2024). Techno-economic analysis of an integrated process for cyanobacteria-based nutrient recovery.
[cite: 9] [cite: 9] ResearchGate. (2021). The economics of cyanobacteria-based biofuel production.
[cite: 7] [cite: 7] ResearchGate. (2024). Scalable Cultivation of Engineered Cyanobacteria for Squalene Production.
[cite: 25] [cite: 25] MDPI. (2024). State of the art cultivation photobioreactors cyanobacteria.
[cite: 46] [cite: 46] Biodiesel Magazine. (2015). State of the art algae photobioreactors.
[cite: 38] [cite: 38] MDPI. (2022). Commercial cyanobacteria companies products.
[cite: 22] [cite: 22] ScienceDaily. (2024). Commercial cyanobacteria companies products.
[cite: 27] [cite: 27] PubMed. (2016). Synechococcus elongatus PCC 7942 CRISPR succinate production.
[cite: 28] [cite: 28] PMC5111286. (2016). Synechococcus elongatus PCC 7942 CRISPR succinate production.
[cite: 47] [cite: 47] PubMed. (2016). Synechococcus elongatus PCC 7942 CRISPR succinate production.
[cite: 29] [cite: 29] PMC7345232. Synechococcus elongatus PCC 7942 CRISPR succinate production.
[cite: 23] [cite: 23] Tech Explorist. (2024). New cyanobacteria naturally captures carbon dioxide.
[cite: 39] [cite: 39] EcoWatch. (2024). Bacteria Chonkus carbon dioxide emissions.
[cite: 24] [cite: 24] Science News. (2024). Chonkus climate change cyanobacteria.
[cite: 48] [cite: 48] Lions Talk Science. (2025). Chonkus the cyanobacteria that could save the planet.
[cite: 8] [cite: 8] NREL. Techno-economic analysis cyanobacteria ethylene production cost.
[cite: 49] [cite: 49] ResearchGate. Techno-Economic Analysis of a Perspective Bioethylene Production Process.
[cite: 15] [cite: 15] ResearchGate. (2025). Techno-Economic Analysis of Cyanobacterial PHB Bioplastic Production.
[cite: 50] [cite: 50] ResearchGate. (2025). Techno-Economic Analysis of Cyanobacterial PHB Bioplastic Production.
[cite: 34] [cite: 34] GNEST. Oscillatoria pyrene biodegradation efficiency.
[cite: 33] [cite: 33] PMC8839941. (2022). Oscillatoria pyrene biodegradation efficiency.
[cite: 51] [cite: 51] PMC4755140. Cyanobacteria Great Oxygenation Event timeline.
[cite: 18] [cite: 18] ASM. (2022). The Great Oxidation Event: How Cyanobacteria Changed Life.
[cite: 19] [cite: 19] ScienceDaily. (2013). Cyanobacteria Great Oxygenation Event timeline.
[cite: 20] [cite: 20] PubMed. (2001). Synechocystis sp. PCC 6803 genome sequencing.
[cite: 52] [cite: 52] KEGG. Synechocystis sp. PCC 6803 genome sequencing.
[cite: 21] [cite: 21] PubMed. (1997). Synechocystis sp. PCC 6803 genome sequencing.
[cite: 26] [cite: 26] ChemRxiv. ReNuAl process cyanobacteria dairy manure nutrient recovery.

**Sources:**
1. [kitakyu-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaoOOtvd8wcFhJWkHMceepa8xjn0ovnGZEgbwjQv8JCuucq8ii8jWUh7ygObZwxwJ5Kse2WRBPCnwEwTz-YgA8JiCoIFzjO9fjh7v275nLduM6C5jhZO153SMRynHdGmcpVWd_C4Bbgln5HBzf7u2lR5FtMRC9qlJTXRfEOA==)
2. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk2eWsx6WyAihD8E9ZPbY5wQZq9vq0WHPXzMji7FBxdO2Hd24fCwnpkDCKE4QpR1K7pCNVtmKqx4Ps0MhTZ3XLt-6CmITcQV2sSh5W4ktHPCqbXpYhXKS_ydPtf7DT63Y=)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo95yKC4rDJ5doxapTqz6ZQ_H8CHS5l17FtrLjXHs8YEbnBf5hfbo-kIEe6a-ZTNw-tKHbEY3IE_72V31U8-DzJUsCwBFaaCyPL_SdiWxy5HMkU2RcppTXlLs=)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxHnNuHm2omN8NDRrBbzcxAE_ceOhZUBOPsaCK-XN9QEfCuARqyyHl4vQgRU_Uu8SVwbNEj6TnAd7EIqaLk40pstmzaEKIFYm8FldpIXQWRRH8CLi-oZohTg7H_7bO3ya41j8qvLA=)
5. [elsevierpure.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDsFRJtum1zdMYwe-AVkD639h95I3E7iR_JALB0tQzgD27R878wzXwFBDw4ZjVnKkGw5hmJ25g3EnzKT7u3SYJ6F3vdCd8fPJqKiSKP0quxmCV84Ncz9jbqlN7sjX_t_8VjDW4vfzqDUA1nh8qHcTkpJadKbd8UadMh8-fCkxDmZX_thyfs4r7RzU0RagjNQOK4w23oyilVd7CFBYB37Hu1JSKnzU=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ5SnIRGMdVNDe_LRSB4E_Qav7rx7WE7wquXfWb74Umpoe5ANCZJsksGV2jJhdtghhkOFZP2TXILFKBmiaHuJmPNWovRg1nWvoYYE_a-RT11fZHcCNWFPT_5DV2KoIHpnjto2T9xX9DK-B1rZ3eaWY7XAO8YFU_DLZpq_tBR6MZuPf5zSqd2OKUhEaj-4XzuhOEOt3SkRBpi0R3ueQwONJUeFEZlsXl2QDneUSG8HQFXv8_BroCcBbWNekt8R2ymu_)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnJImkBj-x7RfeSxgHpjyu61UbUW5QrGHUEsM3TaO8jAri4rlzmDYuB2hm90LAQmwrVzGSKt3uOOzvTRTGfVJ2E9j9jvUG_9nGt7cfitSB4k_quqUWr7ohjI871idFjG7UiozCj4vE6esKPNDBFz337_pjGk0f4A6ADs6VKCT5gWddDp7rZXmsyl2nL_Ul9KBnXejiPd6N406SPdZCWjuXLhOV4AhtE3zlb_m8vCmFue9T3y_gT_rfXyQr4y-QjmaCkGHGKQhQBD5xgWllHvi_WEZce-BnzFKbKrPgDWzpLArWikQ00g==)
8. [nrel.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-sTxv-WLKmfi3TmtXeCHpVGmS_N1YVfux95xi3q812X9B1r4smkvfntap_LeN11rLuqfEELVW-XokBm63fDSF8gs08Cu00G-DBCVehfs17XSJPGMFrBlL6RPaVr03fJpxh1ttMaoDNa7e_zK21_bDTmKAa4TByiuokMXMVJ2ZhvxvSdYE_BoJMQ2bFDNXekGKheKPbDFsglzu46l0_Fjw7nO0a0hgdQ==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk0UoVom4thP1GhA15V85vzADVWsyY6PpqdDjaQcuw6GnLfRrn9mcaLKYA1z2oEatpusoX96Rx9O8tHMgSViSluearqUnn8M-9G0BWkps182EgF77SCoEo_E1Vqlj7fct7JwTuf27pBtpqpact1YArEH75Vu_U-ylCiaKBbJ-gU_Zfp_urNhZpj9E901NIFkZ11KVLboRi5CgkPDxk5uXO7oLlCDh44cQF2oQdgnFUBWkfcLc3LJyyhzclb9w=)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYeiHjhHhwKupk4U79RTiKTvu2nUVQs2YXshfFDn8BCSzwQfms6jpWK_sLB-Glq6F8_MAVOQ6t69K4WU-_gK1vbZLv4jT5e8lCIz6Po1a9R2EBYVR-pkOuPsC1FffC54fM6f3Xwr16)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZCAJf5_DfvPzU67skiWn7GpHITs2KZ6cxFpr033BwxlheCM5781fhrvGAxrx2HtXyI6hVo6zHbypOL8hN1fQQLCuLylv9vli6DKfTx0uk4kgFeqBI4eZXfrgiN1VOzmJd9o7s9M3MDC0V9Q4DIKtczzWH3yVpW7HTGTMo4Wj66ViCR0kCMzUjnwZKUIYDtwdVgdy2)
12. [openaccesspub.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGico71B6cmiWCrB04Bnc175zTRr-bZwm6VKgqMwnJGlGrPl73jTkEvNgxoGMuAcQjXPm3vUj9tVlMHfsDvAxhi5yS1LY-SeNqL4ufgoaIvZMjrkjnAoMotfAzhewxXp_azCG2g6s3F10vh9QgcFgf-jm_eWMWam2X7gwUs7FLSRWKYaaU5l2oz4bEpGza1JJoWb36vocNuIx8=)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqEIcoUsh2k6MTYurpHearwW5HDbwtLujT3vafJ9g7eP37t9iOpdeK84lT4mQG_GxMFD2BiAriGQthfayAMXscUGsnIvcZDBl5hmKHhsKD2oKDlOx3x_DZQtcROg==)
14. [chemrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCVuMYFNjPNkz8USxkvZjwCdNtGRtRta0WSQZyEyQlPtA7vapB0RcbdkAAHI5uFIsIWS3za2MEQj8X662zY01KgATv78nvsJ9Huy0cKXM8M8cBkjrcvPLcq8xFKbQkbHKYaJA7_S2j-PVZBwaTv9rLm_D2MKVVG0mBxUOHpFSrSwkd)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIJ0_B8ePOK5yBh9RAhSawMMN5sPQpf0nBYJ4WYl9LNK8u-__nC949xnWW_A7ztL94EZLrvlmq357OGOx3xp4UB1rCdlwsVeUiK16MZZdQEtwbyWmcwWG-AyNghO2_qj1a6i4kqcjDDFOGqSg2wylNyuMBqDIB6PbyBzIJ56i-ifEj20A9MtiAROuHgtyPQCF-RyleU1nrP7EyJqg5kXUsghzNe2ninEmRj3Ft)
16. [caister.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwNu4rABZHeoNEkZaxKEXTnlVdg5RcoCb8c_kdtAWQ-hyIQxNEUGbNHwqvaUPo4JDFJuYc713qP1Xnmo0hVTsNb3yDR51KxExg1pgfm6Xssl_LTJJW6Iu7ZZZO0kaUKCDZONeB_K8p)
17. [watersheds.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhnvdCCrkCscVwOsUI6BIv5-W_fP5gV60RMLY9Xhziftn2Fssj6ZgG1IZwhNUe4jPq7dXtQlEukC7SVK-pUhOpOCMpjWjGdEhJrIg_cX2Ht_qFfbsyAoa6KhnJmy5OTia_94R4)
18. [asm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5mPXDVd5UytW6Ee1RMBKnqxwBTErz5C0R179KZKFjpcIlIBs9XECBUwuIIr4BP4dNKar0MPUJX7A26Bf-xFelahOwBGTY2oh3mOKLj2-BcsMkVcBKRbr-0DP3BjYvxWs0VoAdkrTyFuVc_130xHIgnoukJNKHyODffVhuPmskGai-orR1P0fs4yynOQgs)
19. [sciencedaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbBSkjphyTe6DdN-bM4kyMBZ8hXpzc0pbyxZHqtcgJVoulvUrUJJLk-jnXhN0ttKLwDmvtPK8f0R8fu8vlDHpMQFaAbIbxrpiTR2k6fs3Jjnahc-laT4fObaZ4sKyYwuEH-Ffl3vbaLHwltmWRSnIn3Wcc)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSM4yy33W5HMN6c3hkq2tyc4rN69Ge0q8DUy2VMvPEF66blTAzY-nQJcRgeSaFs2ppSDYhAFgRwfwjtm4eBkG4vspBqv3bL40u3yyLxok7_4ytNNrpd2k2GEriSdNw)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF8q9jgTEHI3aLQZptfjCFxGdzKFv90lZ_XqKeySKI8attwzTITTgKG-gAUxmGcinyBulQXnzPn5p2d5YZ3JzNRCbeiZbDB-CewaE7d1ZjSUe_ODQZxSmQeekl9Po=)
22. [sciencedaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1V99nwhfqgzIJAtQr4ZLUansXQQvd4dPjA5h9ub5bgIcEwh2PuA2nDCp6BgdW84I1gjdg4wdgT9AsLst94VIkCNIq_caAc8L6gDMFIKQNPqZBSoUiu6avjRRvj3ShcP6nvhFcwvsjzkkCdt_J8JBZmG1N)
23. [techexplorist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVB5SAosUNFZOndHhx7hOahM-jRXhTza1KZ9QsZxBGs2FMJHydIvsI4LCvW3a8CvVzWXUsVOG8wE_RZprt4nl4pnuBJDe4Gxhc240aGffcf3ZqiaEzi-OMNrG0l2EfCc0DBJZE2ri4tXrNq09Gq5zyBlNKwROMKENE1SNqYNfMXxxnpV39TPMp6tDy0m4=)
24. [sciencenews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcpzlHazLrrh_NUFrDopmLUdq7E-fzIwLbjm4wRus7FvlUtnepjBnO5HggbJvBrWFb4TrP2YUoA1JZS0bS1mWQg4e7GKRVipSH6mJtPmlVyLQ6jueibrC20d9MFtanlVhNv8oFyFfpDXqQOAGUdnsM78UzJzT4xB7TjZI4Rg==)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmC4DFusXJzMbmmW3NmacITozxNPLpJtnH8_3-NrN7U_RMbIGt74xtcSqFqqMdCD_nlNxVUcDNA52zblYzEfrn6CYAm_vXtSJ3gZz4KjdXvQb5sG9ug8bqXLZxkCk=)
26. [chemrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeBUV9qR_GeHMZ69F0pr-yCmAwNhyKEpjfIQkZ26oDzKDUAekZQLO_oSTsiSQZG2hcTFmc36iSUUNAPJ6pYFLSuHjZIM1LE6bxvwaIXe1VaTHlNK9FSA6uC-8Jj1yz4DohvRsZmmVmHBxCMqVbjly0QK6XhZzI0T_Hik73JHkQ55_yt7io4qyQA4cislbiRC43KWOwZ8sHiIrofHmkzptD_31TEL_TeVDXlA7_AAkFMgjB4Y_JBUcpYswp1Hwj)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhmwOHoAs0gUsJbH5hjv27RB7r5UT-nMVEc2HW25sh3EEC4J0oYzmpBgKQi70xtzMgXjm_hA32jNL-T9iHrCKE6-eOgW5fNM77OI_spnp0Bh7DxOXRQh0cVxEtUDwk)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi6JYvMRQZQd1fKgJdqrS1okX1OJsNYUUJB86Ec9snFKpRy3f8YVa70LUn2NapHjR4BVsCOnlkeRCjxs7fsQlDcsDVcjxSs2q9HFQj9AO1URoTFL2-Dlu8fJAkKSzlv6aeYDLhrFA=)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjaqmO76-x4xmlSelJ17sObqAGSQe__hWVi4sS9N6a-EbhmM_V-_F4PlScaEP-Nm50AGE5FolYaY5cySXQJTw0Dp638MKWnNUSB3iXhZLl8t9tHqaXtrapUMsNw-TQfZazG9gQlcY=)
30. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrBhQgyaPB4cJtKjE9nhvJm4WjUnAXxR4HVi_BG8ZjirFS_qSkQdKgBzyWUUcgu4aqo6i0Jg3jsryDDu6d1LkXj8hEItPfDvFP0RcJGgxzDv-sJLThq3d2YU8_urUJ9vnf2tLWOT_Rpz2JnFSPfdlCEY5O5PKi92fEMliAIV6tzlZV_cBquD2G1YU=)
31. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwMgLUyd5CQBCjwoEFt26-dCPtMTzr3zwnRD6YtopKeGkXldtf-PBIsVQR4hVATC32eIW3BywofUOI6cfIGjmvVXEpdTQMSzLC3zBWj8UwJFIszQIEmrmuk5n194cC)
32. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL-GHHD1aoL6nyKNcpeUlKIUFOlq2lSorzRthwegI6zV7o5cRhiajjdf9LzHU886AvRGiLhINuBxFmQBsc7UMYe_B6oBehRn_r97ahAC079p35ZqadTvrywcxnZNvNsv5c_K179j4d-G9fok-PXypbUCtOfxqO)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHKRm1mliWV2lTdIiSt-oQ4VZYDkjK5Rj8C_RTx3ym8_8MKmYh6Z1fj62vJm_DrIkUJsqOCy-QTjQgCEsRfVDfEMt0hn1JoOD6exYV8RcUShFpz4RNz_nJc4L-lxu-mBMoGHR9R6A=)
34. [gnest.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaNH69LBh8GIY2aj7yT6YPYMB_AnHJPax7L1B6XsdcjPD_vI-Fu1l7sHGy8WiHf7X_t_OqcVT0ukwYhci_Hy1UC4-qU_TlznsfkSvdnFoGkpzQ4BEigY7rV79apManXmiQ96tacL4ML-5RY_oBvELJNr-Vz59dZa2DpktjFsVUg_pLn6F4ujFGU0bLtzFi-ArQkZs3)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmASqzYxz_K-Aa6LQWUv9zPldZG2dhZcP9n5wM-CaxN1UsGQkIhMgtsAxqX8r5XfKpTNEpOWlve4QQ5TC0kZT9Yh_iq4A81Tcxhs7FOkvz9RGHq7ktnF_-cCuoUNy-8RnjqvwhwiKXHclAPi73aum337x9YUF71-uwCSQwY2luinvvqSr5Jkv2P-aUb8tQIraqTd77I7k3AksRVNyC0Ga-GqmOyrJv_aCJ1rfzZ0m0atGAptpCLt2amF0IhwbQfJTKFTQYb1_c7VNtQ4V5)
36. [biomedgrid.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmcVqtfYZjfcgpP6tK4rHM9G_F_FzpvvBNZwMUZKgfJEJrOliM8MyXMSvYbdMHvDMeMoU2oRPDbWbAYJ2ffHhsa5upvyDuloC9KbDlLoFbDC1X7YrISUXf2sLLhAaoczwpS4qz17SOrK1OCdfYPuKaanAGnwxMTgWSqgMlM6nASzYVc2MSF027OC38bvFjjxCh8dbpTBRGlezyQ9yGEegRWPV2TeAq83KBPUmFIEM_yYy3JoCYmhNRnYfYkKkF6w==)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5DmrIrXmSFBkgpWvaDG-yT9-2w779noGthuE0-_-tg4cFCtqRUg1B2RT5b_Cmi174L2q5G4y8u6IZC5q84gNg4I5NAgpfcyEu5W7KlHM26nBMeZquDSNLE2WiprFFg8KP9wBHalc=)
38. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVgCsmiWvB_qjyxgZZuh48x29nVZUjy_nM8dtNZ1Tj_0e47iu-TJHNx8FpS3t1zqtfPe9jKC8Hy1NPdvKjEkTXAGkvB55gxvKUxKgbo52H6HbYnvoAn12FObAReV8=)
39. [ecowatch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHslngx579RVd4z_AbGSkcIsYFFRYj7YLIGJ0XYC2bilgaHy-w99f08c4ucGeDYAmYfjzNCYWPKSracZZyc1vIaGEQ_iHm0agM1jsk8pl7xcvTPqEQP9WMou5k6wyj-6QaSih9OIARxV1ExVaXVFhQH6m1_EF__c2O_q-f2)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEphk0_sgtuH4QlC9PWbjL7M17mgV-jp-zzi3RMb79CPrgoUnrxu-IaLKyvBH7QSr5Slj4D4uF-xnDOHCsy8yyn6Qtujaq5Y1WRAbhELvSRICr-y9lnWNKDpWr6Mz-A)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4WpY28mHca__twE2Ctw9Q1y1pF2u7NWygS6bNhnJ4WF09zf-VnEdg1V45H5pbMnED-0XsChG-vHq1RruyPkYC8Vc-cq6y7-egtN63Vw76XgIUyyw3c9_vYdIzoXT_LudoNRPj_ei27uxdODXU3_MvSHZN0q1JMA_mYlTYgoKicS29Yx-qIzh4IfSovPFkCCc4A8qSu1qjnap7_Y5f1E7L8rhLJvNOCuvXRu8d-D4hIp3MQqMCDvS1m8892o-o4l9IOYixcCdh10hUqTM0CPFDA_gAxHaV6uQmVoz604lO1X4xgtK4iZcHD2Y=)
42. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIrq_dJ-gI_d0Mhha40Rm0-FgOPeNqDSQFx_5t5YyOguH9wN47E_zf9GoM8IBI_PMmQT17LFUhIq1AjnlDmUr5tTQ_09lt7bXcRV5l8HOGNznpEigdwM1QtRrAmu_PMUIUckYg-rTqNIFtXxFex32MpSq_vbpilg==)
43. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECJBrrF_XWS5ulVYWgd7LI6TXdMO8Heag_RcOUR9vFk9a2lXb8m50q3DzCz3B1o3NTSUPC0zsiB9rXuSooow8KKVH5bOdtg9835m-H6DaHBbVJiFFty58TvcDH7vc7gQUjCdzFm_-th0nHOMvUkpR9hEs8zXeBMvRemq25NrpVvcvcKbJ0sfIAAZLOOOPs5vcs4IWsVTZkaBOT8z3YCBaYzLsQwwxG7eObZJVX60rXz2ICSVgSBijx0ed_1Q8=)
44. [bris.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKrW0ESQRmBSeilMDvsg0PBlVL7-JXIDd3MXesO7YdKU81dGnZe6wqqChVdIaei-R76Z3fCxotLnlNHR1KPq1HSxcHqjOT14D8DmCtvzaNZoiFKlVy9Z0PxCuqFOV3P5n1ycaalWwR2XsUv7-8Fevoi9xP6e5d8B2G8Dippo7N6XyoAq5FJaU3X8wpzk3jh-KXfjG95YGjpxo1OaoOMGfrYg==)
45. [jebas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG662l_TJUvl3twZABxz4amRqS9MwETmlW6h3W5cZrW7DynqxpGjpPPOrvFgV3EidFiGq5R2teIj2xxhbJ24HSCkGvlFjz8ya0lwvATVdxwEpSojmWrAaft0xtHmgh3j_DkNot8nbWQ-eBkj2g=)
46. [biodieselmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTljmUu8gLJ1Yb8TgNk9ldBomONfLRLbaAvz9XfV2zAbMbe1y2-UGaQYoRgGgUEo56_7dT7i7QqZmlRbcGasWm9NXAdzZWlJECcNbsgZJ8yU53O7p86wQUtPw5tBEY8NuKU7SIrzb2wgOGUL5uz81eTWv7iq0XHxv4gQv_X7RFr3urnPgFyf8UDfU=)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkRU8MiZjfE4joA_oE2AeK82Q3Jc8s_rrxS7Np9tNBKYH1wJJnOn18nmoW58OuhVN3Ad0dByAxcb4aqZ5oNEMGS_TGCFI60rih073s_pkNqa3MDrxEqbdmG_FdkfBf)
48. [lions-talk-science.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwTPPLooGDjL9Be0UiKFoaX56WPpnYIQ0cPcRCvgTMxxCLsKiEtBMynQXeCqQWw-Yor5Zpbsh4-b4fnMyOO8vgRgliCZSMdGxlHpC1JWZTvlIsbuWctuAYLe3wYIoirwS0TDKbbMy9c6gy5dFKPvxQ1bnCZtJVtNPc3ksyOH5KjQ5OTbAjTamlbHVYL1T2123VLM5w)
49. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbmJBKnZ0ghS1ua6x4GO_wAcZ4WzNpFUeDr4M9EejrFHhUiHZT8RNCQHgdZI0R4zhRu6AGg7GtyEEaWn53fGN-yjTRedFBtfiiqNWrM_Ij-D4Y05Aw1gJmsQCeN_xVJoR9n9LCZKcDLRS0eD-GB_PLMCtIYDq_NJ07EhB8qs4WrRs2kigxkugK0ERVr6_-N_TCcymK5GW0FaeJbQbPJdCUVzd4kYJPFRRuui9VMxjDUHsO7OPtshN8JKK9YVY6q32EVeEEkY6Sm-9dXQV2cZ5l31cNhkhqTIxX_wnb3vpZMrIZKMNhk1k-UrA4Tf14MPHSwDyFu6Ch)
50. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcqVC38Lk-q9y551MCKpaxJeKJBJmuhS2QzE5mMprucqan6fbyoYL5l1BvKOkfHZOiWOTSFxpcZUT8YhGLlFLuilYnEX8CMogCY8KXj4cFKdRgZ50k3Y16sBye9eTxFeWPTR05sSuyJtv--E42BXdpA7MpRe1dP1rvEZfW0OQvee_kDuypkHQ0p2DWHLoYTur9MaXBJTPhCKys8YlYjoporjc35YipQsGDviF7)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVN-0qAh2YBx4RaTJukAdydgk63Lh54d-z6RhjoxNXvwmKDRsaCA2E1HqzHrMOUeRwAnlSkwWV40VqOtd0U5xtgVv_B4I2XZPL9WjRNwHtt5tLppwbCwl_H4fEbnLs5Cf1naoJhbY=)
52. [kegg.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwaxREKCAMhnvh1qgdqTrgf5IrL5RnrjlczYtHAXs4k5XEGz8oSkyX7jm-lPQBu7SZFM3wqSYOiu2OH9JU22PCdxGPyJ656zzYe8mNTzRZd6jWaq8E)
