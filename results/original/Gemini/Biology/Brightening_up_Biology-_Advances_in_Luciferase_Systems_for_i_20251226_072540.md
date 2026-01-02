# Literature Review: Brightening up Biology- Advances in Luciferase Systems for in Vivo Imaging.

*Generated on: 2025-12-26 07:25:40*
*Progress: [25/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Brightening_up_Biology-_Advances_in_Luciferase_Systems_for_i_20251226_072540.md*
---

# Brightening up Biology: A Systematic Review of Advances in Luciferase Systems for In Vivo Imaging

**Key Points**
*   **Evolution of Bioluminescence:** The field has transitioned from native Firefly Luciferase (FLuc) systems to highly engineered enzyme-substrate pairs (e.g., AkaLuc/AkaLumine, NanoLuc) designed to overcome tissue attenuation and improve sensitivity.
*   **Deep Tissue Breakthroughs:** Recent innovations in 2024 and 2025, such as the synthetic luciferin **AkaSuke** and the **BLUsH** (Bioluminescence Using Hemodynamics) technique, have revolutionized the ability to image deep brain structures and metastases, bridging the gap between optical imaging and MRI.
*   **Computational Advances:** The integration of deep learning, specifically Self-supervised Hybrid Neural Networks (SHyNN), is solving the ill-posed inverse problem of Bioluminescence Tomography (BLT), enabling accurate 3D reconstruction of light sources.
*   **Multimodal and Functional Applications:** Beyond simple tracking, systems like **Bioluminescent Optogenetics (BL-OG)** allow for the non-invasive control of neuronal activity, while BRET-based sensors (e.g., Antares) allow for the monitoring of specific cellular events with high signal-to-noise ratios.

---

## 1. Introduction

Bioluminescence imaging (BLI) has established itself as a cornerstone of preclinical biomedical research, offering a non-invasive, highly sensitive modality for longitudinal monitoring of biological processes in living subjects. Unlike fluorescence imaging, which requires external excitation light and often suffers from high background autofluorescence, BLI relies on the enzymatic oxidation of a substrate (luciferin) by a luciferase enzyme to generate photons [cite: 1, 2]. This "glow-in-the-dark" mechanism provides an exceptional signal-to-background ratio, making it indispensable for tracking tumor burden, infectious disease progression, and gene expression patterns [cite: 3, 4].

However, the application of traditional BLI has historically been constrained by the optical properties of biological tissue. Hemoglobin, melanin, and water absorb visible light, while lipids and cellular structures scatter it, severely attenuating photons emitted from deep tissues [cite: 1, 5]. Consequently, the "holy grail" of BLI research has been to shift emission spectra into the near-infrared (NIR) window (650–900 nm) and the second near-infrared (NIR-II) window (1000–1700 nm), where tissue transparency is maximized [cite: 6, 7].

This review provides a comprehensive analysis of the recent "brightening" of biology through advanced luciferase systems. We examine the transition from native enzymes to engineered powerhouses like AkaLuc and NanoLuc, explore the 2024-2025 breakthroughs in synthetic substrates like AkaSuke, and discuss the integration of deep learning in tomographic reconstruction. Furthermore, we highlight novel functional applications such as Bioluminescent Optogenetics (BL-OG) and MRI-linked bioluminescence (BLUsH), which are redefining the boundaries of in vivo optical imaging.

## 2. Key Concepts and Definitions

### 2.1 The Luciferase-Luciferin Reaction
Bioluminescence is a chemiluminescent reaction occurring within a living organism. The core components are the **luciferase** (enzyme) and the **luciferin** (small molecule substrate).
*   **ATP-Dependent Systems:** The most common system, derived from the North American firefly (*Photinus pyralis*), requires ATP, Magnesium ($Mg^{2+}$), and Oxygen ($O_2$) to oxidize D-luciferin, producing oxyluciferin and light ($\lambda_{max} \approx 560$ nm) [cite: 8, 9]. This ATP dependence allows FLuc to serve as a sensor for metabolic activity but can limit signal in necrotic (low ATP) tumor cores [cite: 10].
*   **ATP-Independent Systems:** Luciferases from marine organisms, such as *Renilla reniformis* (RLuc) and *Oplophorus gracilirostris* (NanoLuc), utilize coelenterazine or its analogs (e.g., furimazine). These reactions require only oxygen and the substrate, making them distinct from metabolic state reporters [cite: 10, 11].

### 2.2 Bioluminescence Resonance Energy Transfer (BRET)
BRET is a biophysical phenomenon where a bioluminescent donor transfers energy non-radiatively to a proximal fluorescent acceptor molecule [cite: 12, 13]. This mechanism is exploited to red-shift emission spectra. By tethering a blue-emitting luciferase (like NanoLuc) to a red or orange fluorescent protein, researchers can generate light that penetrates tissue more effectively than the native enzyme's emission [cite: 14, 15].

### 2.3 Optical Windows
*   **Visible Spectrum (400–650 nm):** Subject to high absorption by hemoglobin and scattering.
*   **NIR-I (650–900 nm):** The "therapeutic window" where hemoglobin absorption drops, allowing deeper imaging [cite: 1].
*   **NIR-II (1000–1700 nm):** Characterized by minimal scattering and autofluorescence, offering the highest spatial resolution for deep-tissue imaging [cite: 6, 7].

## 3. Historical Development and Milestones

The scientific journey of luciferase systems began with the identification of the reaction components by Raphaël Dubois in the late 19th century, who coined the terms "luciferine" and "luciferase" [cite: 9, 16]. A major milestone occurred in 1985 with the cloning of the firefly luciferase (FLuc) gene, which democratized the use of bioluminescence as a genetic reporter [cite: 9].

**Table 1: Key Milestones in Luciferase System Development**

| Era | Milestone | Impact |
| :--- | :--- | :--- |
| **1887** | Dubois identifies Luciferin/Luciferase | Established biochemical basis of bioluminescence [cite: 16]. |
| **1985** | Cloning of *Photinus pyralis* Luciferase | Enabled genetic encoding of light production [cite: 9]. |
| **1990s** | *Renilla* Luciferase (RLuc) adoption | Introduced ATP-independent, blue-light systems [cite: 2]. |
| **2012** | Development of **NanoLuc** | Engineered from *Oplophorus*; 150x brighter than FLuc, highly stable [cite: 8, 11]. |
| **2018** | **AkaLuc / AkaLumine** System | Directed evolution created a pair matching NIR emission with high catalytic efficiency [cite: 17, 18]. |
| **2024** | **BLUsH** & **AkaSuke** | MRI-detectable bioluminescence and ultra-bright synthetic NIR substrates [cite: 19, 20]. |

## 4. Current State-of-the-Art Methods and Techniques

The current landscape of in vivo imaging is defined by the pursuit of red-shifted emission, higher quantum yields, and improved substrate biodistribution.

### 4.1 Engineered Luciferase-Luciferin Pairs
To overcome the poor tissue penetration of yellow-green light ($\sim$560 nm) produced by native FLuc, researchers have engineered enzyme-substrate pairs that emit in the NIR.

*   **AkaLuc and AkaLumine (TokeOni):**
    Developed through the directed evolution of FLuc, **AkaLuc** is optimized to catalyze **AkaLumine-HCl** (marketed as TokeOni). This pair produces emission centered around 677 nm (NIR-I). Crucially, AkaLumine possesses superior blood-brain barrier (BBB) permeability compared to D-luciferin. Studies have shown AkaLuc/AkaLumine to be 100- to 1000-fold brighter in vivo than the FLuc/D-luciferin system, enabling the detection of single cells in the lungs and deep brain structures [cite: 5, 17, 21, 22].

*   **AkaSuke (2025 Breakthrough):**
    In early 2025, Saito-Moriya et al. introduced **AkaSuke**, a synthetic firefly luciferin analog with a thiazole ring introduced into the AkaLumine scaffold. AkaSuke generates intense NIR bioluminescence ($\lambda_{max} = 680$ nm). When paired with a newly identified Japanese firefly luciferase variant, **DkumLuc1**, it achieves detection sensitivities comparable to or exceeding the AkaLumine/AkaLuc system. Notably, AkaSuke demonstrated a 7.7-fold higher signal from lung metastases compared to D-luciferin and allows for sensitive visualization of ectopic hematogenesis [cite: 19, 23].

*   **CouLuc and Multiplexing:**
    The **CouLuc** system (Coumarin-based luciferins) represents a shift toward orthogonal pairs for multiplexed imaging. CouLuc-1 and its evolved enzyme **Pecan** emit red light and are chemically distinct from D-luciferin. This orthogonality allows researchers to image two distinct biological events simultaneously in the same animal by sequentially injecting different substrates (e.g., D-luciferin followed by CouLuc-1) without cross-reactivity [cite: 24, 25, 26, 27].

*   **Infraluciferin (iLH2):**
    Another approach involves **infraluciferin (iLH2)**, a substrate that can produce emissions ranging from visible green to NIR depending on the specific luciferase mutant used. This single-substrate, multi-color capability simplifies dual-parameter imaging, allowing for the spectral unmixing of different cell populations [cite: 28, 29, 30].

### 4.2 BRET-Based Systems: NanoLuc and Antares
While FLuc variants dominate deep-tissue imaging due to red emission, **NanoLuc** (NLuc) offers superior intrinsic brightness and ATP independence. NLuc is a 19 kDa enzyme engineered from the deep-sea shrimp *Oplophorus gracilirostris*, utilizing the substrate **furimazine**. It is approximately 150-fold brighter than FLuc but emits blue light ($\sim$460 nm), which is heavily attenuated in tissue [cite: 10, 11].

To harness NLuc's brightness for in vivo imaging, it is often incorporated into BRET systems:
*   **Antares:** This construct fuses NLuc with two copies of **CyOFP1**, a cyan-excitable orange fluorescent protein. The BRET efficiency is high, effectively converting NLuc's blue energy into orange-red emission ($\sim$584 nm). Antares has demonstrated significantly higher signal-to-background ratios in deep tissues compared to FLuc, primarily because the substrate furimazine has lower background autoluminescence than D-luciferin [cite: 14, 15].

### 4.3 NIR-II Bioluminescence Imaging
Imaging in the NIR-II window (1000–1700 nm) significantly reduces photon scattering. Recent developments utilize BRET between luciferases and NIR-II emitting nanoparticles, such as **Ag2S quantum dots** (QDs). These systems allow for high-resolution imaging of vasculature and stem cells with micron-level spatial resolution, surpassing traditional NIR-I BLI [cite: 6, 7, 31].

### 4.4 Deep Learning in Bioluminescence Tomography (BLT)
Bioluminescence Tomography (BLT) aims to reconstruct the 3D distribution of light sources from 2D surface measurements. This is an "ill-posed" inverse problem, meaning multiple internal source configurations could theoretically produce the same surface image.

*   **SHyNN (Self-supervised Hybrid Neural Network):** Introduced in late 2024, SHyNN integrates conventional model-based reconstruction (diffusion approximation) with machine learning. Unlike purely data-driven models that require massive training datasets, SHyNN uses a self-supervised approach to adapt to specific in vivo scenarios, significantly improving tumor localization and volume estimation under high-noise conditions [cite: 32, 33].
*   **1DCNN:** Other approaches utilize one-dimensional convolutional neural networks to map surface photon flux density directly to internal source distribution, bypassing iterative inverse solvers [cite: 34].

## 5. Applications and Case Studies

### 5.1 Neuroscience: BL-OG and BLUsH
The application of luciferase systems in neuroscience has expanded from observation to control and novel detection modalities.

*   **Bioluminescent Optogenetics (BL-OG):**
    BL-OG utilizes **luminopsins** (LMOs), fusion proteins of a luciferase and a light-sensitive opsin (e.g., Channelrhodopsin). When the luciferin is administered, the luciferase emits light that activates the opsin, modulating neuronal activity. This allows for "chemogenetic" control using optogenetic mechanisms without implanted fiber optics. Recent 2024 studies have demonstrated non-invasive, dose-dependent activation of brain circuits using BL-OG, offering a safer alternative to deep brain stimulation [cite: 35, 36, 37, 38].

*   **BLUsH (Bioluminescence Using Hemodynamics):**
    A groundbreaking 2024 study by Ohlendorf et al. (MIT) introduced **BLUsH**. This technique solves the optical depth limit by converting the optical signal into a hemodynamic one detectable by **MRI**. Vascular cells are engineered to express a photoactivated adenylate cyclase (bPAC). When proximal bioluminescent cells emit light, bPAC triggers vasodilation. This local blood flow change is detected via T2*-weighted MRI, allowing for whole-brain, deep-tissue localization of bioluminescent sources with MRI resolution [cite: 20, 39, 40, 41].

### 5.2 Oncology and Metastasis Tracking
The enhanced sensitivity of systems like AkaLuc/AkaLumine and AkaSuke has redefined cancer research.
*   **Case Study:** In glioma models, AkaLuc allowed for the detection of as few as 5,000 cells in the brain, tracking tumor expansion from very early stages where FLuc signals were undetectable [cite: 17, 18].
*   **Metastasis:** The AkaSuke substrate has shown particular efficacy in visualizing lung metastases and ectopic hematogenesis, providing 7-8 times higher sensitivity than D-luciferin, which is critical for evaluating early-stage metastatic spread and therapeutic response [cite: 19].

### 5.3 Infectious Diseases
During the COVID-19 pandemic, BLI proved vital. The **AkaLuc** system was successfully accommodated into the SARS-CoV-2 genome. Because AkaLumine penetrates tissues effectively, researchers could visualize viral replication in the lungs of live mice with high sensitivity, facilitating the rapid testing of antiviral therapeutics [cite: 22].

## 6. Challenges and Open Problems

Despite these advances, significant hurdles remain:

1.  **The Inverse Problem in BLT:** While deep learning (e.g., SHyNN) has improved 3D reconstruction, BLT remains computationally expensive and sensitive to noise. Accurate reconstruction requires precise anatomical priors (CT/MRI), complicating the workflow [cite: 32, 42].
2.  **Substrate Delivery and Cost:** Synthetic substrates like AkaLumine and furimazine are significantly more expensive than D-luciferin. Furthermore, while AkaLumine crosses the BBB well, other substrates (like coelenterazine) have poor solubility and biodistribution, limiting their use in the brain [cite: 5, 22].
3.  **ATP Dependence vs. Independence:** FLuc's ATP dependence is a double-edged sword; it indicates cell viability but can lead to false negatives in hypoxic/necrotic tumor regions. Conversely, NanoLuc (ATP-independent) may remain active in metabolically compromised cells, potentially overestimating viable cell counts in therapeutic studies [cite: 10, 43].
4.  **Spectral Overlap:** In multiplexed imaging, separating signals from multiple luciferases (e.g., green FLuc vs. red FLuc) requires spectral unmixing algorithms that can be prone to artifacts if the emission peaks are not sufficiently distinct [cite: 28, 29].

## 7. Future Research Directions

*   **Orthogonal "Color" Palettes:** The development of more distinct luciferase-luciferin pairs (like the CouLuc series) will enable routine "hyperspectral" bioluminescence, allowing the simultaneous tracking of tumor cells, immune cells (e.g., CAR-T), and therapeutic agents in a single animal [cite: 25, 26].
*   **Integration with MRI (BLUsH 2.0):** The BLUsH technique opens a new frontier. Future work will likely focus on improving the kinetics of the hemodynamic response and expanding the toolbox to other photo-responsive vascular effectors to increase temporal resolution [cite: 20, 41].
*   **Clinical Translation of NIR-II:** While currently limited to preclinical models due to the toxicity of some QDs, developing biocompatible, biodegradable NIR-II bioluminescent probes could pave the way for intraoperative imaging in humans [cite: 7, 44].
*   **Standardization of AI in Imaging:** As AI models like SHyNN mature, creating standardized, open-source datasets for training BLT algorithms will be crucial for widespread adoption [cite: 32].

## 8. Conclusion

The field of luciferase systems for in vivo imaging is undergoing a renaissance. We have moved far beyond the dim, surface-limited signals of early firefly luciferase applications. The advent of **AkaLuc/AkaSuke** has conquered the depth barrier in small animals, while **BLUsH** has ingeniously bridged the gap to MRI, offering unlimited depth penetration. Simultaneously, **BL-OG** has transformed luciferase from a passive reporter into an active control mechanism for neural circuits.

These advances, coupled with the power of deep learning for 3D reconstruction, are "brightening up biology" in the truest sense. They allow researchers to visualize and quantify the intricate dance of cellular processes—metastasis, infection, and neural signaling—within the intact, living organism with unprecedented clarity and precision. As these technologies mature and converge, they promise to accelerate the pace of discovery in oncology, neuroscience, and drug development.

## 9. References

[cite: 35] Neuroscience News. (2024). Noninvasive Light Activation Method Could Revolutionize Brain Treatment. *Neuroscience News*. [cite: 35]
[cite: 36] University of Rochester Medical Center. (2024). Rochester researchers have refined the noninvasive method of bioluminescent optogenetics to activate parts of the brain. *ScienceDaily*. [cite: 36]
[cite: 37] Shipley, F. B., et al. (2024). Feasibility of a novel combined opto- and chemogenetic tool, BioLuminescent-OptoGenetics (BL-OG), for the ChP in vivo. *PMC*. [cite: 37]
[cite: 45] Gomez-Ramirez, M., et al. (2024). Strength of Activation and Temporal Dynamics of BioLuminescent-Optogenetics. *bioRxiv*. [cite: 45]
[cite: 32] Deng, B., et al. (2024). Self-supervised hybrid neural network (SHyNN) for bioluminescence tomography. *Biomedical Optics Express*. [cite: 32, 33]
[cite: 34] Zhang, Y., et al. (2021). Deep-learning optical reconstruction method based on one-dimensional convolutional neural networks. *PMC*. [cite: 34]
[cite: 39] Analytical Science. (2024). Illuminating Deep Brain Structures: MIT engineers devise innovative method to detect bioluminescent signals. [cite: 39]
[cite: 1] Tung, C. H., et al. (2021). Advances in Luciferase Systems for in Vivo Imaging. *ACS Chemical Biology*. [cite: 1, 5]
[cite: 2] Iwano, S., et al. (2020). Recent Advances in Bioluminescence Systems for In Vivo Imaging. *International Journal of Molecular Sciences*. [cite: 2]
[cite: 5] Prescher, J. A., et al. (2021). Brightening up Biology: Advances in Luciferase Systems for in Vivo Imaging. *ACS Chemical Biology*. [cite: 5, 46]
[cite: 6] Huang, P., et al. (2020). NIR-II fluorescence/dual bioluminescence multiplexed imaging. *ResearchGate*. [cite: 6]
[cite: 7] Li, C., et al. (2021). Recent Progress in Near-Infrared II Fluorescence Imaging. *Frontiers in Chemistry*. [cite: 7]
[cite: 24] Bagchi, D. (2021). A new class of bioluminescent substrate-enzyme pair for deep tissue multi-colour imaging. *RSC Blogs*. [cite: 24]
[cite: 21] Tocris Bioscience. (n.d.). TokeOni: Deep Tissue Bioluminescent Imaging. [cite: 21]
[cite: 19] Saito-Moriya, R., et al. (2025). A bright synthetic near-infrared luciferin, AkaSuke, enhances the capabilities of deep-tissue bioluminescence imaging. *bioRxiv*. [cite: 19, 23]
[cite: 25] Love, A. C., et al. (2023). Coumarin Luciferins and Mutant Luciferases for Robust Multi-Component Bioluminescence Imaging. *JACS*. [cite: 25, 26]
[cite: 27] Prescher, J. A., et al. (2021). Photon output of CouLuc-1-NMe2 with an engineered luciferase. *ResearchGate*. [cite: 27]
[cite: 19] Saito-Moriya, R., et al. (2025). Characterization of AkaSuke in living cells. *bioRxiv*. [cite: 19]
[cite: 42] CBO Algorithm. (2024). Consensus-based optimization for bioluminescence tomography. *arXiv*. [cite: 42]
[cite: 20] Ohlendorf, R., et al. (2024). Imaging bioluminescence by detecting localized haemodynamic contrast from photosensitized vasculature. *Nature Biomedical Engineering*. [cite: 20]
[cite: 40] Lab Manager. (2024). Engineers Use MRI to Detect Light Deep in the Brain. [cite: 40]
[cite: 38] Brown University. (n.d.). BioLuminescent OptoGenetics (BL-OG). [cite: 38]
[cite: 32] Deng, B. (2024). Self-supervised Hybrid Neural Network (SHyNN). *Optica*. [cite: 32]
[cite: 23] Saito-Moriya, R., et al. (2025). AkaSuke synthetic firefly luciferin. *bioRxiv*. [cite: 23]
[cite: 20] Ohlendorf, R. (2024). BLUsH: Bioluminescence Imaging Using Hemodynamics. *PubMed*. [cite: 20]
[cite: 41] Ohlendorf, R., et al. (2024). Abstract: Bioluminescent probes detected with MRI. *PubMed*. [cite: 41]
[cite: 22] Iwano, S., et al. (2024). AkaLuc/AkaLumine for SARS-CoV-2 imaging. *PMC*. [cite: 22]
[cite: 17] Kuchimaru, T., et al. (2020). Akaluc bioluminescence offers superior sensitivity to track in vivo glioma expansion. *PMC*. [cite: 17, 18]
[cite: 10] BenchChem. (2025). A Head-to-Head Battle: NanoLuc vs Firefly. [cite: 10]
[cite: 11] Promega. (n.d.). NanoLuc Luciferase Technology. [cite: 11]
[cite: 8] England, C. G., et al. (2016). NanoLuc: A Small Luciferase is Brightening Up the Field of Bioluminescence. *PMC*. [cite: 8]
[cite: 28] Jathoul, A. P., et al. (2019). Near-infrared dual bioluminescence imaging using infraluciferin. *eLife*. [cite: 28, 29]
[cite: 30] Stowe, C. L., et al. (2022). Infraluciferin (iLH2) for dual color imaging. *Frontiers in Bioengineering and Biotechnology*. [cite: 30]
[cite: 3] InnoSer. (2024). The Application of Bioluminescence Imaging in Preclinical Oncology Research. [cite: 3]
[cite: 4] Alsawaftah, N., et al. (2021). Bioluminescence Imaging Applications in Cancer: A Comprehensive Review. *IEEE Reviews in Biomedical Engineering*. [cite: 4]
[cite: 14] Chu, J., et al. (2016). A bright cyan-excitable orange fluorescent protein facilitates dual-emission microscopy and enhances bioluminescence imaging in vivo. *Nature Biotechnology*. [cite: 14]
[cite: 15] Berglund, K., et al. (2021). Antares BRET system mechanism. *PMC*. [cite: 15]
[cite: 12] Xu, Y., et al. (1999). A bioluminescence resonance energy transfer (BRET) system. *PNAS*. [cite: 12]
[cite: 13] Berthold Technologies. (n.d.). BRET Principle. [cite: 13]
[cite: 16] GoldBio. (n.d.). The History of Luciferin and Luciferase Discovery. [cite: 16]
[cite: 9] The Scientist. (2024). Luciferase: A Powerful Bioluminescent Research Tool. [cite: 9]
[cite: 47] iBiology. (2015). Hastings on the evolution of bioluminescence. [cite: 47]

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Shgrpg9KfLCl1fXoRxQ1OfeWAtpWIyaRM9aufqYbbQ-JGFcnyqkStWYyz9Rv8Dm_Fs2lAZ0xGHFeVuQz_pwxYj-O-Zm-Z5H3DNLb6zV7hFgVvtlcdO7RzLneCMS_M67CDCvvQK6l)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHyb8uPaL75v8_urHy8cuEHD6MSBa8-mhSmzmKB9dN9gyVISpfHwSwvRHKsXc5807Usgcl-C43RNlHBv62w40b1F3RlgtOt2DtdK8CH7UhFC2udeDBQnW8q0OdjeIGdw==)
3. [innoserlaboratories.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmow30JZwlegRi-GQWryC7Pcr-vvSK32pE7I1pcOdLC6El2hlFydcLmsr3e8uZAA-Mrog-HWtQy5_Zj9Q5yGEkKYlf3Nq-NCMObwCr5vnQq_I3XM-p13moB2x8v5CX-l1g0jrO7i9kVzvU9mw5klQ6SHR4acNKRPQvf3XSvnHWOy24T9HdGtvLF8cEZTS1pWJJd7tAg4SPgEiynYHoqe9HTQhsTrWtCwzL1HU=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE-AtVR191aft4XtUII4UdxPutBUW2IxXFJf102CPGL-3JkD_i2r9GiOr1zkDCH3jlTS4hXihkAmZ4ijNx9JV_lqtX5ktbzg6BRy4p3kFUxe4ZhxAO-XYOhTmxIWL8fiPHMmpl_0qh3GqnyeDGtCmtzqHNBMlCMC9fR2n_nurV9hOnURMK2X0wmwkTuMR-s7Yj-WqDauux10OhhZoV64r9VRk0tBUzDfa5u0XS_0c=)
5. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdt2o5uUrYP-lhYa1MGV5gTqgetSf2__Cleq2xo-4iUoDZPEgQWeklCOTVO_28Xh420h7ymDQ88xQb4RwNW3tdhTptEp0cP9LqOqdq5rMZUpIV6Cd0ZAK6AhlgRLvOWCF1nMyhmDvXmak=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNXt5JKfqRRLSkLyY54Ni4r-Ulshv6hpV3Tw-kjhm4N2KieX6zrxpBtl6iZeLOy2ZBBzzSK0Wsltccjxm8gpgMXMQjrNXvrhcJA0GKG4EjQRIkGC-0LZ0MSOALIUZ4NzSwCIpP8TJB4ZjPjhE0jTGeOJpTn-wBixWz4UkXmZZPDCB7Oybu9DbsGudNUarZ6hBPCs1t8lup0HvtW3NYW5Cm8lSZ2Thv1ouzyxetH-yFIkTeR3-cU2jC90Lu1zo=)
7. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFczvib4tgoRiERom30EP5NzYK2I9XE8EbU-y8XEKOiCFd0K8B0O09OhkYwjWRxjr59z3Ldh0x8F6B2jGCFYEmQT_0bwn-kiWGeiZGhDH6BfQYe3B7J1MpY7Dd1bsWQJ1d_i24HAyiuaKhoyNjVcqDqcJ8ResVRSAmrpbdIaRce17p8INlmwxKLbpzIEg==)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcgN9xCsmFcak-xp5CyuMCkBqzBS94GClMfRCcW5lkeveJVVU9Vifmglu7eYvH0C4A3BqYaU8qxhQaONhJ-GT5curz-ggVi7Tpb--3GwCjp7lwOfQj-j7lENZfYAmK-ApQlmjv3fQQ)
9. [the-scientist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjXAghb_bDuuQLJIoqrVlOoH7CmTB9DsDhF0M3OeiWfmRm9x5Qqcm4O3wbaN6nhvtfUdF-jm3FYtD0k97OiNnTrqKKkrr8wau6Tnc1H9PHq21ePzgENbPvnL1OwCnHBjfE9P3Gi8QF_TBCQUIGr7y4Lok1mCz74SuV4j3i6KoCCwtt1t4-fFhhaVnZIw==)
10. [benchchem.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKjd_-q5zEGors6JXwbxTvNoV3-Bh_rNj2H2fueZWr3U14cFs1Qw3D5oPtd17WkdRUKFDHtnH5HoJrz2VMvIluA3ag8zxT3F6c8wQuNwNETG0OvI8NlUALF3180YwbOE_QjPycSmjnhGdVCt79YJRvzDnJC6HglK5z-x_MBI8w2HCXjYek5k4d6VZt1tHU7I6ySxf671924ctSo77MMZWgRzH0hDq8HvhE9A==)
11. [promega.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjjtXppseTJ99CgP1iFtYMgSL7tXLdDCrFGCJQTP9amg6L9kMgPm9qC05LaDx_XHVpv03-wmxh8CpiOQ7mbEkGDbTdhG_rFK0Baks6hwe1lJvOR2j_-hk0TeHSnu3AEn95-oPmEfdPBbqJwAZJcCiYscxlN6VbLRFnZEkPxXlZd5YVXJvMA00B1TK7t0D8KA6EeP3ht7KTCJ4E9g4FQ3necD8vvkIyEZy6yNY_dJTF7qm61pmuKbhkJCrelZ3BXQYbYX71GIZm8PbPttbmJFA=)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvkzNgUgCrxyXrvI7-bCSfPOKc6PH-OFYFyiZToui29w9JqKxOk2YUF8K4QQzTn1LJzhe8wD5tF1M6vZAn9FO7WS91NpYxfHwSWnCXKpPgkOF2eWBh0jvfF16cmlcDMuZo0vt8Vw==)
13. [berthold.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkl2drtPrKzWrDEEk5cdy7ALQnTqaK90CEvdDNZuXbU5WkMRmvqfLWrtAGyt4w8jJRjXnTHOMpMsMyWSNhbIB56UBW0bHpZmLYQ0WUs3x41RPf2ysr4AOEitYTxhAjU-0_uwJmuCduiA8sxlSvrO0AN8Y-L7YzlHaB9jK1UtyF6UNmXp8xgpc9v7n10qpDr8K2-4b7VkSviQ8f3_u3JiIyCLKpeQ==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT0qfEgNm1aUKuPNT3S--Va4GDBumBQN689tIiBwZBpeby4YlCDv0c5rGOH58_AIKOPr96GDkUGYP9673FV6shux0Fd6EYr_oJf7_dL4kkAjXcpZO1dVxk2M9ce5sRfLBW5wCipr7l)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR03EuOJzaHtFyf9vgyg63L7TRWx1nNMmxNv7OJ1iBPQLvJCBImxrolUuy6Eucy1rNtH8jBqiJFWlQlHarj075M6t2KL0k1uwRkBCmk2eCwC3kHvSHDEX37haXQdJcKOwdS-cgiNML)
16. [goldbio.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPqMcQY_xDs55z1b8LKTuGB_2rpCWqFQqLrHb6s6MBIKkQ0FUJGyPpj5NrPPbgGbz7dDqq-ls6NdSQljkqBJKeo-J2P8zsJ_KetYKOsJOGUR-NZHc0xnGIKQZMHqWIjxbsCO1fyI996D9d0BBgRJ483uBjyNvzXQEkOT7FGdejR7Z5KZpWRgJtGtSDcnfLp3loKfBAzT04)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWJxEgSTqwnLfF67Hd0ZqSJis6SFU3UlxhAJTV4aNyIaPN7xRrnWLFJGq8JdG7qjFMo31ew90vKFr89NmfAZsvI51RjJEacLEq2IPI7Nb2g4eOEveGkL8ObKiH7T2AUhEgTSVr3JJo8atoC6EdguhgLevT84KZcmiW2WFLq9cduP2UBzjS8OVyUkG64linawOzlxrp_PZ8Nlqel8OXwHJ07QLTDT_z9U3d_CbNvPLKPY_XQy3tOrnD1lQECsh)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpu3iNZQC3qF1A946iiE1cADE20WHH4VISvQDZvBe6Pl8MRjKAbphZ62y8FGzJ8YEDhgB74evquRjNW4kJGhRa8B1B9cpKHciyyqUiCEm0hhV6WRlsk-pWBFsordibjx1YycftnUBf)
19. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkG2Q3W4LmxufcimebhOTOezX_P38rKslAQwzGPXDHHNoNc8JsHPfn0TOBAt-L9yuPEMB4T70hv90l2g3UYdroV1ggxT6oUz6XwS9glcQLG5n_2Ue7k7ndDsqReibSwt2JyZ_WCqvl_GJ2ShcpHrZ26-5AezxRFm7Lis8=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA-_yGbN39oT6r-CqqFB97CBOjX5XiqqXo347ZmnfTMnY1GATfLe3PplEbj4n_Wj2fvGkJPo55EE2YyY5vNBEeUA4BX9TniG0GP6_EAnZX6VD48b-U6XxDB07vGkUhQh7OPrdR31CV3Q==)
21. [tocris.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIqZAYrYp9v6hGJHAtXXbHaPq1Naz-M5H7QjhUlwGvDlBdCEuq3q3stHeSCZRdzga2FQWO6XRslgOgqTLK99FElY-irhm83ZUoF7D4kBUSxUeFpqVB3icyCbbYUeUOsTaHOoNUq7iEWzEETcyy2nAYDNBo)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJciX7mfpsbkoe5WhAJSgbZG-RF6KFujcTIoX20cREvEf_7CfCGcxEEUDM9A3XFR1H71-FWboK-R_DHuE3IT_arMIw8sIkefeC4voQYW2sWm1Jq0AtAtCqu_BRWPTBbQyBpXO7cROAxQ==)
23. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF4zD8rgI4VebmCmEfzwm-bn-q9nI_4q1M5t3b3dx1ktiPGqEpiF8yEMqthTdquJOJ-XelyFEu0Nu7wnloXqKSPA0qK_7EL_ZBlrS3-DRJ7uUgtwB2D0lOQmbZd8fbquotf_9OYFHGx4e1l4mJ-dkDVQ==)
24. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gptP8f0wnALCzdDYw2YjmkQl3G4G4hxPQ2Kl7_5Ax8yNnyaXjlvqujOJb5SUEbPodvYu6LbZVbi0sIkjEUcuailt_RxkIF672bJ50PnRD3bvh1_nVG24IOnGt087Es4hRhAxZCxBfal1k_hKCzehA8WSJCF2KqXmr2cN_m2T-1b15GdjGnkrSG7Js0dkhmbPqECRMVY2V_gOTjgV8ai2KJmPFcfQJHMhnhoXg3_vpPvb5g==)
25. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyJwDUQDWttN9ehq3VahHT5cL0RU7djUTWcCV0V9OJ3GPnZo3wAJSfov-5b-rTZ5R7QwghpQABBT-oPyizNcTnm5gzJ-0IKLvC8D0ipAyAIaP92ZC7f0Hrdb1lFHaWSK1l-FY=)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrYVdHSAI4cpeCcUNuHqQdLivW61rVvcJNRykv9PQWBhNc6aPG0swkQldEsX-YFBsxkklHuX8zzBgvz-x9Z55Vhf9mGWwiECGPt0X66AJVhNIxfIjBEaIxuTeW5w60sWsQ6rkK0gW5sQ==)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKnsqL6yRgNxpj0xPiaS9CgSthOH6fr5lYvqWPNpg9-c6kc3uxVUo4X9a24tL-zDIV3Zn3SDiHmscL72RgUFJN0FuL2WWvR_0qtOkf0pJv7XCbMCT3_cpM75dphYDOqXZTbzz-s4JaFoHDlJrzQhAIlgFIBIW91OMyqjIx0YLj5nRjT1mUBtTeP-sZPUJRL_eODdRZ13bwkO-jBXaR_zGVpVjK1A_Y-6XL8cfBas6gvyNAG_BRTSgR)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcXi3vn6z-mrTAIypt7OqNqzAufqu3p6brcQxyDmoylzkh0SgyFVCYLzWr_xlsrb0NQxF0G7rF4aQfssBl-xOxtFmkYWm8PD5Hnavsv5OH3gZOAqfgpP6UasuPXZAyEUAzA8Kvt1II)
29. [elifesciences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTqy1gfO63lqtDHJwP_VG7vZoS9eG_Ji84GvtKbNiWlYJ0N0dA1vfpB7MOwy8xs2hDdvRS5RR-CJ6Gry7pMddFyjuOV_Ol8iELRhZD8yyUljHwR3S_3Qx3tLf483KU)
30. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg6qzXhBulhxp53TbU3kJFKH8TYBVS49S37L38K1kHfM7-wWF_zeQ9-kRwC28AOAV1IHJMtq6pGBf6DF4E8uGTxgaBim_tyScaAyTnzBj2qAcIb0XikuSBsaAyJPnZ0hCuDsVRn7oqKW8pikp3ozh0U46iItVwvM6AzFqV5LVxu9M5NB5cZIVbhL9zMwV2CW6X-YTiB4lO44js3xEoeacXrvHW)
31. [uq.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjbxHsMn2NYdMws_o_7BtCi0pkRG-uiFHOFo3OcZQ3cVI7tIJUp-w73TsqprFaY-diRdsWBlMCZPNRNO05g6t5F2Aqp2aoaw4tduA1FSUfvqCbE0xBIFgq_qm8BQYP96AIBUq_WFI=)
32. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEq9rZLdjvss6zyAYLZavX3yWiGSjGcVs-BIfwXQA6TF5kmgCdWy7Z6MeV9EXH6LiDyQQC-l3LejkIkyDToSBQRIekGLI4ihNGzwMiajklVWyQZLdT9BRQbb-DSSfMveSQMyH-5DTRQCe6DurHAlt44)
33. [bham.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8o8MhQA7zAj22yN-ai7SP52dQyrxQNSFC6-2D-WpJ7bRF0b21VBAj3XWQxmkHuTqJe8o-iX3cMAdMPjIcBE0rnSS3y7UJDWEzQa5AjEXrSYhe02qjNZ0Dk7YRYoB2yq-Y_4gIMm931JEBhGFdSMAdyuyCGpJv6uhpT4opkTJmTOsdbnbrUiulBBwGmk-_)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFDEyxElU_EtmkYm6EKdibl5iexmIenKhKaNIdOG_W-PziO_cWYlmALlPJ6s5s9RiE9PZC9x4iMKYxH4uZ23dybg79O5YBsY5aQFgWwoF6m0r2kOQfCzWh-PlPpIIAEJHJxzxng7rw)
35. [neurosciencenews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy7DURupMD4v-EW4zAwh8ROCM4DvKfP4sH_IPc9Z-wMBUILEtHdWcTeMYBYMN3SeDKtfDcYEhp6_USKiqzCqA-ma8H8CwviGjwJbq2NWxxsDyvYsCRJAnb_WyQXPVdKJ9dByd6VkfjBeHy5wcbXK6HyckEq_uDCluSjMbwKZZAWkNF)
36. [sciencedaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGksz1gcjY4veZro-UPnnA98t5ZWQTFALoy4aZ4JWFAupL8wJ_e5EuZHWT-m7CxOBZ0WVW_Z44Ieffkrz__2y7hvfpP9ZnM04kqn4XP9AH-ABT-9cJI774XDKO_g7HMgxeZU1rwhg9pxkcpwALEgTvPHGx9dw==)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQAVXF5mC2QeNCV-0sMgt3M-XepfKdhllWDg6CxF-3S72Oppd_P1uHMZ1brpqdprssdSiLfIylj3PyANe9XJ728URKSfxYHQ53iMBsRdqeZ5l80oact0qe-PGIcf21CNpEpU3QRddkJQ==)
38. [brown.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSe5UTvqEUQNoffOK1nRxzk42mRoELNtMDLw97lmcV3J1snA76oiKZMQJDVUcYygjXf_-hhBYPKks21nHQOYkghrH_5crRPaFK7ARSwYhs3wYosuWltEtF-flsXibTPSE-GFWZprkZkOiiEIAa3w==)
39. [wiley.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFl_s80YlQURYhanUy6-fUa4HhntPK6QHt40dROAluYMR8A0fa3eN_FYJZFMuOZc5EzGMCaIj8aYpeVtXR4BuVI-WkttlUbTfW2c-zmSMXr9S8GGLzRflaExkF5ClUWs9BhGKlvIUQampkIppxJ3AkU2702fVj0lUUH5nSviJp4GqfKEd3ibHu713ulKw==)
40. [labmanager.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuwJRrNW8Bun7MXLA89rBQ7Jwi561bwnFKHM_VhwgnR3oUU8Gak8nQQfeO0CtE3n579RHScPwtDalI2vVQdLATJ6M1liSE4wW-lv-RMB4-VCyytZM8323a5mjkHkbTytfPXvcS5WgqUbvbw7OwXaOkA3j7VPd1GgmHk_Vr4EN6_muUJ8YHzTj_Ck=)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfnFTHKUagcNPaEx2ffBc2OpBmr9ftdPnuOc1ZSttiFdQC0DXLr2hCIdDCZqGcUs41KDM5YK_fj4ZRu3ekPg46mEVOy1yDWjmiKdlPz6quH93sYuonhOyQNvH54-onqg==)
42. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4QWBCI3UybD7N82bFN4X2bPGxevqt9K-u3rkkLiULJLMTn7zhTCvUn22FqjOXNKqVEWhYjqSiyOWTXdvM83j9S5_K261vUW8hqpRzUJI0qc6zCqvAdw==)
43. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkIzCej2VrB1X2zjyZgqO4ltkIkh8xPt6yv9oxOLVQHhAKbCn9o2dsSelO7t88XyaLlnrBtRrjtZj1DvrQDsGCB9mECdumdkOfXsTtLuYDWkzAVjjEDWzzWb_jaHOvpVDU0VlXuN83UEA3h9FK3OXvrtKybmfmtVWM7snsqgl72_Htr7kEr9HhVXnCQWJ5PWANjcfzbjAkNidUNygI7V_SC4mwCZfuBI6rU7udxHEU5vw-W1gHHOOOvscPalTtYtjSDdN9e68NDzhRtWJe5TNx45r8)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWh14rJbme95ksKb6O72yACWHUooTbRApAlsCJyWKf_r7Eat_X3SJbiMa1H5Y7ktJxh3glOrnctYqtne3Y1PundPDH3Xb_lWYMaM5UizL-aHwVZdk3I-L_mfg-Zaz2mQ==)
45. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPvL3F864PoCL2OhTPUETSkDvSMaKW7Vyeh78UEIEswEgoincS2WAolU0_xzJngWeYSLQxt27Eq-P5L00m5YvvRbzOSiQ3Tudsfy3ycAR_J2N3bcaiC_yXZ03bX744wWGVhyV5bO5cn_RgEoqW6XM8Pw==)
46. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0oDF0JQCkd-L_Sm0wTAwEAl1o5yIYl2C3bJHDIEtf4n40Od__FNWAW150FD0wkuJ-e1ah03DkOpn55rEm_3nY08cOnfWiienAumy9HvleenzyW7RM0J2cjKeMRDX4XaRT-6p3YS2FiGRAm-iRYuFIyn3BlKhYWAa2-kDbH2FiE23lD-9qLP7E1dRsrxTU-ijG9ePb2HW6486bHiYQFHhErr1vhlpgwZKAmjcfcGJCu0-8)
47. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-9HAYacq9HpWV09a-F9RKkn2I5ga31ToD-ZECq9jeYQGxbeVvYRz4tnbb9n2__iaKguYk9SH4HiWR6Iy2sjuE69lqwszdRpCkxgi8KXmKA-vwnWbjVzgQ1bB4tn3VZlqY)
