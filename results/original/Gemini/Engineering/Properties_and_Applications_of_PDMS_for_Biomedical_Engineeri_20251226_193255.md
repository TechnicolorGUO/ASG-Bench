# Literature Review: Properties and Applications of PDMS for Biomedical Engineering- A Review.

*Generated on: 2025-12-26 19:32:55*
*Progress: [19/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Properties_and_Applications_of_PDMS_for_Biomedical_Engineeri_20251226_193255.md*
---

# Properties and Applications of PDMS for Biomedical Engineering: A Comprehensive Review

**Key Points**
*   **Material Dominance:** Polydimethylsiloxane (PDMS) is the dominant elastomeric material in academic microfluidics and biomedical prototyping due to its optical transparency, gas permeability, and ease of fabrication via soft lithography.
*   **Versatile Applications:** Its applications range from Organ-on-a-Chip (OoC) platforms for drug screening and disease modeling (including COVID-19) to hemodynamic flow phantoms and implantable medical devices.
*   **Critical Limitations:** Despite its popularity, PDMS faces significant challenges in clinical and pharmaceutical translation, specifically the non-specific absorption of small hydrophobic drugs and the rapid hydrophobic recovery of its surface after plasma treatment.
*   **Future Trajectory:** Research is increasingly focusing on surface modification strategies to stabilize wettability, the integration of PDMS with 3D printing technologies, and the development of biodegradable alternatives for tissue engineering.

---

## Abstract

Polydimethylsiloxane (PDMS) has established itself as a cornerstone material in biomedical engineering, particularly within the domains of microfluidics, soft robotics, and organ-on-a-chip technologies. This review provides a systematic analysis of the physicochemical properties that render PDMS suitable for biomedical applications, including its hyperelasticity, biocompatibility, and gas permeability. We trace the historical trajectory of PDMS from its industrial origins to its revolutionizing role in soft lithography. The review critically examines state-of-the-art fabrication techniques, moving beyond traditional replica molding to explore 3D printing and advanced surface modifications. We present comprehensive case studies on applications ranging from hemodynamic biomodels to COVID-19 drug screening platforms. Furthermore, this paper offers a rigorous critique of the material's limitations—specifically the absorption of small molecules and hydrophobic recovery—and discusses the regulatory and translational hurdles impeding commercialization. We conclude by identifying research gaps and proposing future directions, including the development of biodegradable alternatives and hybrid manufacturing processes.

## 1. Introduction

The intersection of materials science and biomedical engineering has long sought substrates that mimic the mechanical compliance of biological tissues while maintaining the robustness required for engineering analysis. Polydimethylsiloxane (PDMS), a silicon-based organic polymer, has emerged as the *de facto* standard for microfluidic prototyping and soft tissue modeling [cite: 1, 2]. Its rise to prominence, particularly following the advent of soft lithography in the late 1990s, fundamentally altered the landscape of Bio-MEMS (Biomedical Micro-Electro-Mechanical Systems), shifting the focus from rigid silicon and glass substrates to elastomeric polymers [cite: 3, 4].

The motivation for the widespread adoption of PDMS lies in its unique constellation of properties: it is optically transparent, allowing for real-time microscopy; it is permeable to gases, essential for cell culture respiration; and it is mechanically tunable, capable of mimicking the stiffness of various soft tissues [cite: 5]. However, the translation of PDMS-based devices from academic laboratories to clinical and pharmaceutical settings has been slower than anticipated. This retardation is largely due to material-specific drawbacks, such as the absorption of hydrophobic drugs and surface instability, which complicate quantitative bioassays and long-term implantation [cite: 6, 7].

This review aims to provide a comprehensive, critical analysis of PDMS in biomedical engineering. Unlike previous reviews that may focus solely on microfluidics or implants, this paper synthesizes the material's properties with its diverse applications, while rigorously addressing the translational bottlenecks that currently challenge the field.

## 2. Key Concepts and Definitions

### 2.1 Chemical Structure and Crosslinking
PDMS is a mineral-organic polymer (silicone) belonging to the siloxane family. Its backbone consists of alternating silicon and oxygen atoms, with two methyl groups ($-CH_3$) attached to each silicon atom. The material is typically supplied as a two-part system: a base (vinyl-terminated siloxane) and a curing agent (crosslinker containing silicon hydride bonds) [cite: 8, 9].

The curing process, typically a hydrosilylation reaction catalyzed by platinum, transforms the liquid pre-polymer into a solid elastomer. The mechanical properties of the resulting bulk material can be tuned by altering the base-to-curing agent ratio. The standard ratio is 10:1, but variations (e.g., 5:1 to 20:1) allow researchers to adjust the Young's modulus to match specific tissue types [cite: 10, 11].

### 2.2 Physicochemical Properties
*   **Optical Transparency:** PDMS is transparent from 240 nm to 1100 nm, making it compatible with UV-vis absorbance detection and fluorescence microscopy, which are critical for biological observation [cite: 4].
*   **Mechanical Properties:** It is a hyperelastic material with a Young's modulus typically ranging between 1 and 3 MPa, significantly lower than glass (~50 GPa) or silicon. This low modulus allows PDMS to conform to non-planar surfaces and mimic soft tissues [cite: 5].
*   **Gas Permeability:** The porous structure of the siloxane network allows for the diffusion of oxygen and carbon dioxide, a vital feature for maintaining cell viability in closed microfluidic channels [cite: 12, 13].
*   **Hydrophobicity:** Native PDMS is hydrophobic, with a water contact angle (WCA) of approximately $108^\circ \pm 7^\circ$. This property drives non-specific protein adsorption and complicates the filling of microchannels with aqueous solutions [cite: 4, 5].

## 3. Historical Development and Milestones

### 3.1 Early Industrial and Medical Use
Silicone polymers were synthesized in the mid-20th century, initially finding use in industrial applications due to their thermal stability and electrical insulation properties. In the medical field, early applications focused on encapsulation of electronic components (pacemakers) and use in catheters and shunts due to the material's physiological indifference and resistance to biodegradation [cite: 1, 14].

### 3.2 The Soft Lithography Revolution
The pivotal moment for PDMS in biomedical engineering occurred in the 1990s with the introduction of soft lithography by the Whitesides group at Harvard University. This set of techniques, including replica molding (REM) and microcontact printing ($\mu$CP), utilized PDMS stamps to pattern materials on the micro- and nanoscale [cite: 3, 15].

Prior to this, microfluidic devices were primarily fabricated using silicon etching techniques derived from the semiconductor industry. These methods were expensive, required cleanroom facilities, and produced opaque, rigid devices unsuitable for cell culture. Soft lithography democratized microfabrication, allowing laboratories to rapidly prototype devices using PDMS molds cast against a master (usually SU-8 photoresist on silicon) [cite: 2, 8].

### 3.3 The Era of Organ-on-a-Chip
Following the establishment of soft lithography, the 2000s and 2010s saw the rise of "Organ-on-a-Chip" (OoC) technology. Researchers leveraged the gas permeability and optical clarity of PDMS to create microphysiological systems that recapitulate the functions of human organs, such as the lung, gut, and blood-brain barrier. This era marked the transition of PDMS from a passive structural material to an active component in functional tissue engineering [cite: 12, 16].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Advanced Soft Lithography
While standard replica molding remains ubiquitous, recent advancements have refined the technique to produce higher aspect ratios and more complex 3D geometries. Techniques such as membrane sandwiching allow for the creation of multi-layer devices essential for barrier tissue modeling (e.g., separating epithelial and endothelial layers) [cite: 17, 18].

### 4.2 Surface Modification Strategies
To overcome the inherent hydrophobicity of PDMS, various surface treatments have been developed:
*   **Plasma Oxidation:** Exposure to oxygen plasma introduces silanol groups ($-SiOH$) to the surface, rendering it hydrophilic (WCA < $10^\circ$). This also enables irreversible bonding to glass or other PDMS layers. However, this effect is temporary due to "hydrophobic recovery" [cite: 1, 19].
*   **Chemical Functionalization:** Techniques such as silanization, layer-by-layer (LbL) deposition, and the use of amphiphilic block copolymers (e.g., Pluronic F127) are employed to create stable hydrophilic coatings that resist protein fouling [cite: 4, 20].
*   **UV/Ozone Treatment:** A slower but gentler alternative to plasma, UV/ozone treatment oxidizes the surface and can be used to modulate wettability with high precision [cite: 21].

### 4.3 3D Printing and PDMS
Historically, PDMS was difficult to 3D print due to its low viscosity and long curing time. However, recent innovations have bridged this gap:
*   **Embedded 3D Printing (e-3DP):** This involves printing a sacrificial ink into a PDMS bath or printing a PDMS-based ink into a support bath. Recent studies have utilized fumed silica-PDMS suspensions to improve rheological properties for extrusion printing [cite: 22].
*   **3D Printed Molds:** Instead of expensive photolithography, researchers are increasingly using high-resolution stereolithography (SLA) or digital light processing (DLP) 3D printers to create the master molds for PDMS casting. This significantly reduces the cost and time for prototyping [cite: 6, 23].

## 5. Applications and Case Studies

### 5.1 Organ-on-a-Chip and Disease Modeling
The most prominent application of PDMS in modern biomedical engineering is in Organ-on-a-Chip (OoC) systems. These devices mimic the physicochemical microenvironment of tissues.

*   **Case Study: COVID-19 Models:** During the SARS-CoV-2 pandemic, PDMS-based lung-on-chip models were pivotal. A human lung airway chip, consisting of differentiated bronchial epithelium and pulmonary endothelium separated by a porous PDMS membrane, was used to model viral infection and screen therapeutics like amodiaquine. These models successfully recapitulated host-immune responses and alveolar barrier damage, offering a humane alternative to animal testing [cite: 24, 25, 26].
*   **Gut-on-a-Chip:** PDMS devices have been used to co-culture intestinal epithelial cells with mucin-secreting cells under shear stress, simulating the peristaltic motion of the gut. These models are crucial for studying drug absorption and intestinal diseases [cite: 24, 27].

### 5.2 Hemodynamic Biomodels
PDMS is extensively used to fabricate "flow phantoms" that replicate the geometry of human arteries for hemodynamic studies.
*   **Aneurysm and Stenosis Studies:** The optical transparency of PDMS allows for the use of Particle Image Velocimetry (PIV) to visualize flow patterns within replicas of aneurysms or stenotic vessels. The material's elasticity is particularly advantageous here, as it can mimic the compliance of arterial walls, allowing researchers to study fluid-structure interactions that rigid glass models cannot capture [cite: 1, 13, 28].
*   **Blood Analogues:** PDMS microchannels are used to test particulate blood analogues, studying phenomena like the cell-free layer and plasma skimming in microcirculation [cite: 1].

### 5.3 Medical Implants and Wearables
*   **Neural Interfaces:** PDMS is used as a substrate for flexible electrode arrays (e.g., retinal and cochlear implants) due to its biocompatibility and insulation properties. It minimizes mechanical mismatch with neural tissue, reducing the foreign body response compared to rigid probes [cite: 1, 13].
*   **Wearable Sensors:** The flexibility of PDMS makes it an ideal encapsulation material for wearable electronics and biosensors that must conform to the skin. It is used in patches that monitor physiological signals or deliver drugs via microneedles [cite: 5, 28].

## 6. Challenges and Open Problems

Despite its widespread use, PDMS possesses critical flaws that hinder its acceptance in pharmaceutical drug development and clinical use.

### 6.1 Small Molecule Absorption
A major limitation of PDMS is its tendency to absorb small, hydrophobic molecules. This phenomenon acts as a "chemical sink," significantly reducing the effective concentration of drugs in microfluidic channels and skewing dose-response curves.
*   **Mechanism:** The porous, hydrophobic network of PDMS allows small molecules to diffuse into the bulk polymer. The extent of absorption correlates with the molecule's octanol-water partition coefficient (Log P) [cite: 6, 29].
*   **Impact:** In drug screening applications (e.g., testing antimalarial drugs like amodiaquine), this absorption can lead to underestimation of drug potency or toxicity. Computational models and experimental corrections are often required to account for this loss, adding complexity to bioassays [cite: 7, 30].

### 6.2 Hydrophobic Recovery
While oxygen plasma treatment can render PDMS hydrophilic, this state is unstable. Low molecular weight (LMW) siloxane oligomers from the bulk polymer diffuse to the surface, causing the material to revert to its hydrophobic state within minutes to hours. This "hydrophobic recovery" complicates the long-term culture of adherent cells and the stability of microfluidic flows [cite: 4, 31, 32].

### 6.3 Mechanical Mismatch and Biocompatibility
Although PDMS is softer than glass, its modulus (~1-3 MPa) is still orders of magnitude stiffer than many soft biological tissues (e.g., brain tissue ~1 kPa). This mechanical mismatch can trigger inflammatory responses or alter cell phenotype in sensitive cultures. Furthermore, while generally considered biocompatible, uncured oligomers can leach from the polymer, potentially causing cytotoxicity in sensitive applications [cite: 11, 33, 34].

### 6.4 Regulatory and Manufacturing Hurdles
The transition from academic prototype to commercial medical device is fraught with challenges. The FDA regulatory pathways for novel devices are complex, and the "batch-to-batch" variability of PDMS mixing in academic labs poses quality control issues. Additionally, soft lithography is difficult to scale to mass production compared to injection molding of thermoplastics (like PMMA or polycarbonate), which are preferred by industry [cite: 6, 35, 36].

## 7. Future Research Directions

### 7.1 Biodegradable Alternatives
To address the non-degradability of PDMS in tissue engineering implants, research is shifting toward biodegradable elastomers such as poly(glycerol sebacate) (PGS) and poly(ester amide)s (APS). These materials offer similar mechanical compliance to PDMS but can be resorbed by the body, eliminating the need for surgical removal [cite: 37, 38, 39].

### 7.2 Advanced Surface Coatings
Future work must focus on permanent surface modifications. "Grafting-from" techniques, where hydrophilic polymers are covalently grown from the PDMS surface, and the incorporation of amphiphilic surfactants directly into the bulk polymer before curing, show promise for creating long-lasting hydrophilic interfaces [cite: 4, 20].

### 7.3 Hybrid Manufacturing
The integration of PDMS with other materials and fabrication methods is a key growth area. This includes hybrid devices that combine the gas permeability of PDMS with the chemical inertness of thermoplastics to mitigate drug absorption. Furthermore, the refinement of 3D printing techniques for silicones will likely reduce reliance on soft lithography, enabling more complex, monolithic device architectures [cite: 28, 40].

## 8. Conclusion

Polydimethylsiloxane (PDMS) occupies a paradoxical position in biomedical engineering: it is simultaneously the most ubiquitous material in academic research and a material with significant limitations that impede clinical translation. Its optical clarity, gas permeability, and ease of fabrication have fueled the explosion of microfluidics and Organ-on-a-Chip technologies, enabling breakthroughs in disease modeling and fundamental biology. However, the "sponge-like" absorption of small molecules and surface instability present formidable challenges for pharmaceutical applications.

The future of PDMS lies in its evolution. Through advanced surface engineering, hybrid material integration, and novel fabrication methods like 3D printing, engineers are finding ways to mitigate its flaws while leveraging its strengths. While biodegradable alternatives may eventually replace PDMS in implantable applications, it is likely to remain the workhorse of *in vitro* biomedical engineering for the foreseeable future.

## References

[cite: 1] Yazdi, S.G., et al. (2018). A Review of Arterial Phantom Fabrication Methods for Flow Measurement Using PIV Techniques. *Annals of Biomedical Engineering*. [cite: 1]
[cite: 3] Wikipedia. Polydimethylsiloxane. [cite: 3]
[cite: 41] J. Funct. Biomater. (2021). Properties and Applications of PDMS for Biomedical Engineering: A Review. [cite: 41]
[cite: 12] Ufluidix. (2019). PDMS and its role in the realm of microfluidics. [cite: 12]
[cite: 6] MDPI. (2024). Recent Progress in PDMS-Based Microfluidics Toward Integrated Organ-on-a-Chip Biosensors. [cite: 6]
[cite: 16] PMC. (2024). Organ-on-a-chip: A Review. [cite: 16]
[cite: 42] MDPI. (2024). Organ-on-a-Chip in Dentistry: A Comprehensive Review. [cite: 42]
[cite: 30] Lab on a Chip. (2021). Simulating drug concentrations in PDMS microfluidic organ chips. [cite: 30]
[cite: 17] PMC. (2022). Rapid Prototyping of PDMS Microfluidic Chips. [cite: 17]
[cite: 2] ResearchGate. (2021). Properties and Applications of PDMS for Biomedical Engineering: A Review. [cite: 2]
[cite: 43] PubMed. (2021). Properties and Applications of PDMS for Biomedical Engineering: A Review. [cite: 43]
[cite: 5] MDPI. (2022). Properties and Applications of PDMS for Biomedical Engineering: A Review. [cite: 5]
[cite: 44] UMinho. (2021). Properties and applications of PDMS for biomedical engineering. [cite: 44]
[cite: 45] AGRIS. (2021). Properties and Applications of PDMS for Biomedical Engineering. [cite: 45]
[cite: 13] PMC. (2021). Properties and Applications of PDMS for Biomedical Engineering: A Review. [cite: 13]
[cite: 14] SciSpace. (2019). Study of PDMS characterization and its applications in biomedicine. [cite: 14]
[cite: 46] AIMS Materials Science. (2021). PDMS applications. [cite: 46]
[cite: 4] PMC. (2017). Surface Modification of Poly(dimethylsiloxane) Microfluidic Devices. [cite: 4]
[cite: 19] ResearchGate. (2024). A Review of Methods to Modify the PDMS Surface Wettability. [cite: 19]
[cite: 47] MDPI. (2024). Modification of PDMS Surface Wettability. [cite: 47]
[cite: 48] ResearchGate. (2019). Improvement of PDMS Surface Biocompatibility. [cite: 48]
[cite: 49] ResearchGate. (2012). Degradation of biomedical polydimethylsiloxanes. [cite: 49]
[cite: 50] Frontiers. (2021). Surface Topography of Silicone Implants. [cite: 50]
[cite: 51] ResearchGate. (2025). Effective Methods to Improve the Biocompatibility of PDMS. [cite: 51]
[cite: 24] PMC. (2023). Organ-on-a-chip and stem cell models for COVID-19. [cite: 24]
[cite: 25] PMC. (2023). Organ-on-a-chip models of viral infection. [cite: 25]
[cite: 52] PMC. (2022). Stem Cell Organoids and Organs-on-Chips for COVID-19. [cite: 52]
[cite: 26] PMC. (2022). Lung-on-a-chip: A new platform for the study of viral infection. [cite: 26]
[cite: 18] MDPI. (2022). Rapid Prototyping of PDMS Microfluidic Chips. [cite: 18]
[cite: 28] MDPI. (2024). Recent Advances of PDMS In Vitro Biomodels. [cite: 28]
[cite: 23] IEEE. (2022). PDMS Based Microfluidics Fabrication Using 3D-Printed Molds. [cite: 23]
[cite: 53] PMC. (2018). 3D printing in medicine: A review. [cite: 53]
[cite: 54] ACS Biomaterials. (2017). 3D Printing of PDMS Improves Its Mechanical Properties. [cite: 54]
[cite: 22] ASME. (2022). Embedded 3D Printing of PDMS-Based Microfluidic Chips. [cite: 22]
[cite: 37] PMC. (2011). A biodegradable elastomer for tissue engineering. [cite: 37]
[cite: 13] PMC. (2021). Properties and Applications of PDMS for Biomedical Engineering. [cite: 13]
[cite: 38] PMC. (2023). Biodegradable Polymers in Biomedical Applications. [cite: 38]
[cite: 39] UPenn. (2020). Biodegradable Polymeric Biomaterials. [cite: 39]
[cite: 40] ResearchGate. (2020). Beyond Polydimethylsiloxane: Alternative Materials. [cite: 40]
[cite: 35] PMC. (2012). Barriers to clinical translation of medical devices. [cite: 35]
[cite: 55] NectarPD. (2023). The Hidden Challenges in FDA's AI Guidance. [cite: 55]
[cite: 56] ProRelix. (2025). Challenges and Solutions in Meeting Regulations. [cite: 56]
[cite: 1] MDPI. (2025). The Impact of Polydimethylsiloxane (PDMS) in Engineering. [cite: 1]
[cite: 57] Pharmacy Times. (2024). Regulatory Hurdles and Ethical Concerns in FDA Oversight. [cite: 57]
[cite: 33] PMC. (2011). Young's modulus of soft biological tissues. [cite: 33]
[cite: 34] RSC. (2024). Comparing measurements of soft biological materials. [cite: 34]
[cite: 10] ResearchGate. (2015). Comparison of macroscale and microscale tests for PDMS. [cite: 10]
[cite: 11] PMC. (2019). Characterization modality specific material properties. [cite: 11]
[cite: 31] MDPI. (2022). Hydrophobic Recovery of PDMS. [cite: 31]
[cite: 20] MDPI. (2024). Fabrication and Analysis of PDMS Microchannels. [cite: 20]
[cite: 21] PMC. (2024). Modification of PDMS Surface Wettability. [cite: 21]
[cite: 32] PubMed. (2022). Hydrophobic recovery of PDMS. [cite: 32]
[cite: 4] PMC. (2017). Surface Modification of Poly(dimethylsiloxane). [cite: 4]
[cite: 29] Eden Microfluidics. (2024). PDMS Drug Absorption. [cite: 29]
[cite: 7] PMC. (2021). Simulating drug concentrations in PDMS organ chips. [cite: 7]
[cite: 58] UTwente. (2021). Small molecule absorption by PDMS. [cite: 58]
[cite: 30] RSC. (2021). Microfluidic organ-on-a-chip drug absorption. [cite: 30]
[cite: 27] ResearchGate. (2017). Design considerations to minimize drug absorption. [cite: 27]
[cite: 5] MDPI. (2021). Properties and Applications of PDMS for Biomedical Engineering. [cite: 5]
[cite: 36] PMC. (2018). Clinical translation of nanomedicines: challenges. [cite: 36]
[cite: 59] PMC. (2023). FDA regulatory oversight for medical devices. [cite: 59]
[cite: 8] Elsevier. (2024). Soft Lithography and PDMS. [cite: 8]
[cite: 15] Harvard. (1998). Soft Lithography. [cite: 15]
[cite: 9] Annual Reviews. (1998). Soft Lithography. [cite: 9]
[cite: 5] MDPI. (2021). Properties and Applications of PDMS for Biomedical Engineering. [cite: 5]

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwwH401aPW8qhwhjyl_rApFQDXUsZC1JCm5zlrKpU2ZObbgGTy2x2-VEeL_N2tl-4Pg39AmIkoRHPI-GmNCS2Lx5Z8GgCu0JZpK-AbDqF9uN1MLjtkgDcPsjW8Ag==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcvo1l5j6StsN_xo76uYV8evEHoSTX69T4UgEJtNq9dcf6koq7iyGewl0OFngFK4k-VPrmEzBNJxw50DXLFHDOk344yN2DOVikTLeKq2WctCDSOwl7mcSGVSHfLfi9XphDhGPBuKmcJ0O_iExIYvlIYDSDpLb28qAVuZIIUZuhHkCV8dh_y2eTqLLgtglFryoOFUhqthRNkXeQtC3eZG5rMJsqGIBgSjAZ2QmNKqAKVA==)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJiMb_4dMoROp8eBY0DSg3zrFGoQiRKfA3eC355YdG_GRFO2lmBvx4xoD92m-DJuq7m0Ani8MbbwkQ-UY-WIGEdg5O7C5q3Js5UmbKd7KiQG9VRl5oi3NYFREHnPz_DEV5GxfyTtv32Q==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI7_fiCsr0DypKnzNweye2GfxqoLVVSmMxUIfNsE3Ak6CLquSt0zIg26l4I4hGKXlvj_lXF3fDtf8-Wne4hdFxUGculx17IR8Z-ePDVQ_gEJ6pbS8skTwRyig_dqskRTqpnzp669mN)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXjztrX3J4LWMEoEney_Z9lw_RmLKcnFR2deZe7mqqcYXzrd4atdWSy9HhhXEWWzjCdotWyh5RsmO0BqEAGNYmWo9Lpz42ShQyo2BkG9TuE5VKPX_mq8aD4suU)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnYwfAhrhEL0RRExDDcyplmWIdX9sJFWDcJkTuuDuWt9VEqmDnJW9iZAKj9unXn-9-9a6edrqr14_H2OyYz77mo4j-LXUoD2y-1bIx9CldGz1kLZ7EKptap84Apg==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvKA7C6YHcEwBHeVFdZyk-1qSBtX5yP2Sg8bhmlR0pPRn41XFcpN1kB_UzVGCxqvqBMqMonzfyU-2E1mbyKQmXKOv8dUx0wub7VSnuav394is8tweXsuhKhYCuHubyIZ0kyBROY875)
8. [doi.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMKWHRoY0d-P2FSfqR3bSbrheHFKAcVbe9Sya27tOPFRrlMzVE77sNoBjeelOgIbgv4Pr8DcKZXzMGOlLNJ1YGliPxry4-LaNZcZX33xx6rBqAlQicpT5889qlLHgnPZtM_MPc5Jfe8Q==)
9. [purdue.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvwrVj8Wda2H8LzRA_-UUqlty8HnUL0pMMGnvk3ArbweMlxJ1UAI2kuhHy_bmlNNS_GYNdLdNh6FAOLNVf9KbQG1Pn731Wu7NviBTVrtfPwYbcNoRNBWDgbUeQceXMHXbs7xbCybwP_PKHMHdpKYvteFrmN7ol6NIFBg68sZRHUSJRVyGPWqO4n2KUPQyPTPq_)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDP0U27EdnrbmGUZoWeq8v598xnEGBQUznax4qDmFeJifFJvHKcnEDvcxiZIsOwN7_jip8VKZy0zRJNrofa0E3HEzN6x3df_Oez7Au_ijZLB53Mc2nBPgb0LnU08xE5iho55SLexp41Z_YYsKMAo218ddhoG2_zPq9FpQ9n3I-I_OfvNG-PGLJzT5OdaqKFtCkvJV3pMrd1Zp2yYJMmquI7Ii4zPQC1-FDmlnZxMgAH9S2sYJnvVCvwiiHnr33eILFGVfFbkmlqWy3uOhwYG6m7WwWrA==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFBvx6yCKNuPV9Y4f5pWAWKvPWfY3JYsjmxs7BGAMkwEjcyhu5PlJueTl29WfpLeRqdzp2HBU2Af34y9cj21iOt5Iyv2BHZ_pfinNeq5Z_Uw71AC2727HcSPMIPSjvKZIwKSp1LxmD)
12. [ufluidix.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBvrXsB7tC5Vo_QGGZe5nGBFpaMeJWzbyiAZnFFiYlaYZOJxMBFeN8M_21tc67zyOS9HLAUqb-jLfpYC3W3h9xJauH0dgwrcyha5w0Enwiwn0FANuQmtwqvNM4YplAxQWHHV632m8P2hJ7SK9R5scBJPscbDUKdnXHGLO4E5tOaR0PN2Tgw==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJLrqiM_1V2FFL2To2KoBu8KVoHXUjbLcO6EUmV0-zZPocpGKJJY1vh14oSCETShStYZyiYwsVd4ob4QciNb6EGTsmq3SSbh6K6pwc5smscwK7ZcarFQ8PDr0V-bToKrkXTq5PwhgY)
14. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdbLZKqK5OYV4IHuQ2YYSt63jWbipPeseGpzc8XLFaDHW2q2L2_XIL_Hb9LcmGC4jW0I70gjKfErTMCj8GDQ1P3GvlpHAHaJE3Nzz-2W0FKw-rHJxHe-CHz16FVSTak3SoKgv-DRLeEXUo-q2XuLUjt1Wao8cfa-Fl7KHeoARtx8nhRnatox-e4CEI9ieFRZSmt7qD)
15. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo85Xy9lVPGXOAZBZf1ZUAIUgpDReH2PC8SBCRkmyeMxkxwawxotZPYJ17ClbfxNqMbo2CJENI-epSpCOwj5Mb8jZCIEkzR0nnqVrzhxtoHoHb4tVAcaI3gLyiiVoZf66FJt-bt5AXZMeQ9rD98IAvGFbVtfSr)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKWzjxf0n6jtxwSTe0jK0jtTUXzstx-IqvAsuWaQcUFQ_o5wFW0MXGsE184346yX_YS8lHP-nfKmjrH2L8Oce4bFqXgWct42iluiLqUzstcspwH7enmg0Z7ExyYanCvXtA8OIVeQVo5g==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_wOKhc-r7_z8FADNxrd-PgPu-picwpAQnDeoOrW__JsmPxMMq8b3C_Zm1QB9cfZdzm2kdAe7OwI7_9XUt66LhqF8nQFqnck81ULmOLvpuYX0sE1dJFJGcfuellhIuKzlNid5qGK9A)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRPiGsnM6yo1Mv_zlbVgc-LGjh46e4p6RzOWlmY3DZyoznCAirG-8XtoArWX5_DEr8YhR9WTcRrZHZdQO9bjlvyeV9Dvjz-mrR9JOfA8frI09zQLsgN99HiPLzf9WCPw==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlgGRPM1g4dZTSJ_WTx7ZsyIhZMkPkmEpSpuNHDNbIjIIFWwVglsCNK7uWDmELsbAsmXm96eOU60JBa9H1mjoNkXY-_Nnkmykf97JSB_whhBrp-93Opey2R4JE2AZ30rskyj3xO-emzBaw8VC8_xftmQlVi1UWbv3sPtDi2_kMgtbiZvbKeEE6zG0Wz6zi7ggaEyMSBMOTgAl7az-CA8cG7QOoGnVUqw6NxtBZ9ldYA8Ehi07m9yl8aiyF)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElqp6cnkzI6b-nmIj-lhYYkB_8f3GCbZXa5TzHNekuwA9xBuiriP5N-GiKm1a3orh7iJa9dP0I3a4RL2T2bLZjEhtCZy7m7P0DQCy_QHmkIacSSaz6DhULcvJc6fCjzA==)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNhFmziy3CDhjn5Y0gQNiOgJRyYUePE_EoWxehxxGlzmWTQTwqSLi-ZVqXk6JQtCi5-GhEOrEl7earfgIDW58oLr4DHp4O-SUYHVl1MNZgOVOcDa20wLS7JrCUN_bFIwz6kV1ZWiSzoQ==)
22. [asme.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjmkHYlsDAaBirG83vDT5olNqpib49jLWPoEovb6RulFhbU09KXLA0zJ1CKTVFzXum8Vm5AtJ7_Dgi2ENxAFvoYDLbwNBx9TJB6ehAUxc8-_3Gl7EvD2-nCC5JkKYI8Rb9Ih2RD7rE5gj7qMPAfwiGWOZ99n2DMqpQ5ntgvNg0MfxgetdN4biJdr5TAeGEpfRIFXXsW_rSjcRtVyGaGBsReL2Zc9MVQkX42sWPSr2yjWZznyePUyhtoBWDAKIgAg==)
23. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQsegvb2B_Sew9QjbCemnLHiFNntiyNUsYltKimUliCWuty9ga3cGHh6Ue1-BfBqZeBw2X2jagkrf4GSqTiFxVAKO5w-bHcJyL7ah02eBWOjL4zSAJ5fop2iOUNauE4IUsvrw=)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4c9Lfrj0dAuOUw2UuwuLQ9yoqFKpGT1u9PQCd-X3_t0WKtfotO6PP1CRGoQbkhDoUH_gfVds48DTu5HpgSRLDOUi02ZzgxBkm8bkMT_FADFaSM8rEWFpIcoyzmJY_eTaxjD85aPwhA==)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGU8Mw_Snt73aoZX8wqgTM6OcgrD1GOP8RBLs2oaUJO8rt00Tr3YtB6vM1EAt78fmEpVAbxqkcK20Ma2M2h6zrk5hdeImonEIV4m2-b-cfPBYEI2DTvhRimC4EUPjjrJJQIgo3Bnd8)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAi4xFfLqQZN29vk0gQJpWkwKgrYYVsR6KYoZ29efxa0fe0ft8gjAB_L5HCG0jL5wEjB9tm-P-mLb8wA_kg--v51BQ-o-Sd8MNbRLb1sXj59NOz-3vsRNMuIhs0OBH_v-LhrmkwBZm)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIDMTpxh19gnTKXgfKemiDkrqgx8eh-CjnFj_ssfyPPBkWxYLMoMtg5Optetf4unoV0MMgaqgDV6dYDz33y8rtXNEth8rQZXJpXGxP3qZeORIMbfum-W-jtWjqMa2ZuYWjF7yhkmI9C6QgegZE_Kcf2wVyE2gQwg4t3LhuThcLgtNYfHwPd7ADdp0doa73xmzOFxj5FMYHBD_c3EMvaL-xbQOtW0BY67BppDtC5ftzl7ImqXMQyXVca1v7ssDbbjWbUFnbkfxP9uJop1FjOm2c2aBJ8g==)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqLvyK6KOlvuKq141NnQsuzjJm-FwYCjJ5ahTYFNPpZ_M5550uDQO7wThRQeNGUiUtbN0YCw6eCDO9TvuvCExfJU2uNu7dllYM7s7W8j4pQefeWLgtw0JrlQJImQzKqA==)
29. [eden-microfluidics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSuDyeunnDBkR0ky8BarJb3DVlpt6APGknYpQIjCK5L8bfVE8vcDHLDhEz7SLlA4KJakxc9PdU_Ksb2rs0ZMDaZ2l4wzgM3C6akp5CoO_pof00aL91pqT6e3khGSIM7jeuqjOh1hnmsvcjzBuy3e2y9ibuIfEhL4_OXSPJqQv6WozhpYC_A0sHs2Eety8=)
30. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4MCyMdO_zbOQjYjI8R9pI4TeGKq67CbXwzXnZpqm8xD1vSg8x__DEXcVSNjpfPg_E2lAFf_7YumBZgx4DnKWmRa2yABy9Pfvi9ILhYUKccRofVz8U3RF5QK3RlioukClr_-6N1pnKX_kEddv6mW9p0qK3rancUw==)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEf2ltffgX3Z7TmjPHesXC_qXMwpD2vcGrTpw1RwCKwx76BRJu_Fd46W0ecz2E7Xd6ehcPIv46PxdGfdyCph4NAhhVOJvrSStEjEXcXwJwHY9R5LtE38rZ1rWv4N_-)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOlMk43fnwkLc56furgXh8RhxdbdCkboj_kJqRB971AaGGM-qMX-rdrlzGd-mzPq-s3OfK0l2Jr3ILCbwdhZFsitsABWq9D7Ra2-noPjxfr2Fp-YoyYTm3HbQEgHGJKw==)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7YNP1EL6Zzs7mxXAqjwlyPD9lXme42jpiQxOd1gxOF1u1GWcTYnV9y6NhJYFQWtQhb1XytoEF1ufrGGEiTUx4bnbphzlAocYP7OGyk-tExr729anMD9tHJ7tV015qEdLITZo7p4dL)
34. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBLVkBQSgG07plEoA5nLggnNJShdCQhIzgRFMQpujT201jLSD13OBR--sSAmEqJVy9YNxarzuUOdRubJM8bpcuoqO16h15oRYxMxwY49IKniJbEku_eRVQdXoBvvtPwSnwb4G_8O2ZC5RLqgowwvez_FNYTQ==)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQtPAMb_sKur6FFZYQKEKvSGhEZyBkjtJFkSExMTmVqPJAoxSwFhP7irqUIKPiCSBCiWkyVmJSOhrw6OiBqVQ2Gf-EBCyYsD2UBceh-i6IywOBHWlHzz9hk4kSli7cZrohbGLkdv_e)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTATOvL_fdSOqQVfsy3gO9Z6rG2YfK4qTCjFGHDeQKMferFWxvOgCCvf1xLbsT7XzZKgAxNP4HpN_0oMFtfCpMc6SARF1iW5PlqyHiheY3h-Ua1vkK-35bo_MQ1TYESzfdixCR1TNU)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmuEK4EOhhH3IYF6xK0RV30EUs8zqG-ozhDqcBaqKOA520-X7IsdCBeSJLvWJg_bvS5fAROhFHjn5hr69GmOn7pB7bQ3C7xc5pgi3n2fcKJj4S4rldkR1J3UMQ4fbBm6WVuIO9CpWh)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPabRUGicqGgntWZbhw737JJqW7RyGkrXk7Iw_rbJUjhBfQRxlfJBJpqUGCdxkcleDZjGWFunIxecJRi5aC9xK-plUFaKjpTgqfge3jJAugZDTLRHI1Cm8s67Y352o5lEYH1uWYNnBAg==)
39. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMpKeYgTzxtXwbXXw4n63oVZbnxeE8FsBUeEuTaqMOJPpxYm1SzMddhq2bxTm1j7Xqqv1FzeDA9Y_RkuvBRQqWKU9mACg32rt0fP72AXP4LbUv4oYVK4W1qJt1hvIb5s1XIhpUiNNKXUszgd_Iozgc8M9r_krdI6pHFunNz51idggfq9H5ffw5xXWR)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDygAVYj6v-eMpxN44NOxeTXFQRATbiud-H2TGYVIOIqB_y4fT1-aSbsYfzKkJ7UjCyBiWn4F76nU644V06bkEjgzvMr-X9oR_On_xbatgNYc__BgxSUonnpCyke18x9v0E_GObuqnbZEQ_OOJYDjnUQWA5mNm5Vu64np1aIOb_BlLjAW6B9rtUtDww1oyvmNHREePk9r591J3BYUWeptoILwoBajUm5VyB-yyM8oA28qPjh4UjSdyACGanpBAk37XlTJEaBdVxdnt8qjgT_Q6uOQBoQknPeikJIoXUnXSUewlpJb4)
41. [dntb.gov.ua](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6Khq7_redl7x65a86KHktAV4xLffFPbmJMng6QXp1PIi8AoUWJwnqtuUM6pg32M1qvbCSDQaHDJLvMhLs54oacXg5SunwYbM9YMWtf36msa6rbyhBjRINWVgVXGhZs4Cd)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIZhL1jQ9FjXMArWNRtDNiDxKcgaKuB5rno3c7Ctsaswo-_Yr_quQLenpPmfP9_MXXDTrmsbiwhOL7yDltQSSSqzMywwYCuzDPjnP1rd2s8nsMcfRjn4i7DH7WQtI=)
43. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLK_W_t9fNQjwUBW9Ur36xPO2R3g7aL6wAY3p1JpX9JQCyrq0nizA09pq3IPWsUrT_up_qcPRuei---wYGcJQYszJsf2OH65Xr60r47-nZqBlNemKT7ThDXA0F-dRhvg==)
44. [uminho.pt](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmtfwerRpVZ_mdzfGGWvXmPS3gyy6pbzgGFA1QDHOsuxWn9Fb9iE7y6sPGsNNT66YwwQ09D0XlA-5YK8sky5dcyXl7xdQBvWYo5lUZA_7qdd8xBa-W85ELcViHcUC9bZUkxEqJe3Ojr494RdQhC2ovlxGGdyquCJhbs2W3KDW2QNBRYPS5w2b96Jy0Fuo7)
45. [fao.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEN20l3F6G4sWdj9T7lHQhZMo0Qj8ercQXTE4PJngx3030I2aocZH8S-m9C78Ba3hpHGqouP471S9N0L3Et05cONIyR18a-M5voqig5eRfpo3Qx5tIXmYmTCRdQVjpShIkwB2bgFY94WQnH_W0u3yKC5uF-kUXBiWe9vrtQoqx_BHv0Qn6IdgA=)
46. [aimspress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJOE0L6Fcj4Nm6kXlmiXUOHgjKePXZW3KtWnLfi-ClDNku9jdf4ZOcfMko0B3nqp4gtmWyZcKk3Lufny4sjjCqiNHwWdiZiFsSuHE828CrGB_jxlbw-9tVU7WMdPL_JPCAJWWHwMJSGWNsb6y7y6ZnPq9ZytvjzFjuLGoY--Jlajd8)
47. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_SRsDfxPZEtEkbczbuiwIQiQfd9K4ErGgpkgySx_g7Nc4N7_-6vX58gSnWDW29qcf4XO_JhhYAP4VUorx7XlK4f4oOrtXolLpK7OzhAQuD_2dZ4_4wr_fYPBydJM=)
48. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-JR9MhmB4iJvtgAGyv6SDi-zJm5D_p726u5F0wj261p7FJbLgORzOnxZm0MuecE-zUBoX36xJYNPSd5CKYSFcXZ9n3EYQ8-rl-fiMOPqi_lVuCEiAvFQFw0m00TBuXfrd05yyOGY8ihHBVx6C58FDwzoxJlnZrjY5ogf9fBRho0On9Jpz0PqyVmPPSo6eTzYDI_I6zNFYD5F43M8-2vVw3Ka2Gs-KdzmOk5x6JitIOyI3RGKwUVLSrHNL2UWMAi0wtMAmIK_Y44RTbz0=)
49. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMRVWihbtCmyii4NRCvq3TR_T1cY1pHV7U3crQnFD57eixnTqibs4flH7lCQx4QJBj8K67hA2QEHjYARjgRsvlzY0gvNw0RidhYFWYWsiPqo-UzuxtOfYcW8eeywl-A5rhXpnJUPznQTxSB1Mdu_DpOHImc1qLn2s1R-3DPuNizEDeOjbZ4AKHko0XlIMh7DfftPsKGT4-gg-pEQd4qwwVz0mpGYIiutLUGuaAs7t4xLZ27G31untddG6yPUHfaBLN4QZbJGU81ljuvfQ0RwsNKYBhsOxa-eDBR4l_qVHw_6v0VEzkk_NKyUMFA8PPrnAo983h-VE=)
50. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYv0ASnro52qm8CFMv4C07l-SuI0omilvc__JHmfqpQti_hEeGm_q4cMMilRb7Br8OUGcI8XvL6nQbvtynE5JZpNIg0HAt62s7TvWpCjr6zqO6jVcXSxMRvtxQ0o8XK9SV940VVXSHJa6rN2tv4ttGnoMIfT95JBr_kZPKCgZwsIlQKqtzSbnqZY6uh0AB0una-R36HPhGXIgxbr_xD9sNnwba)
51. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh9oxH7miacx7Q1AC2G3lQqHf8LDVCpjmj2pvDcArhCMUbaY7Xa5d1GFS1mnNHO_DxDuclYGqhssPA7l38CYDUXEujcyWKXzXSUG9JNxw6Ud384jiYRwk3Cc6IMYLsR0QM-tihpdtB6OAXanQ4Nx4TIdmmMKkZP2rJaZonjAf9B35zk7H6QFxlmpo2k4OYFttbTGBTRz7q0S-bjUWie2yJp2uIL9GTcx42-gkPl_0qevlNOQ==)
52. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi0OCdsnRicpzCuH1ae4svTP83SvcCNmyxTeVbD8EUUp_znt3922pOTTjf0TYwHLclrx1JAlYlCo6qTCGvc54IR9PWAP_o3Hw4VHd2SMW-Fh1926KSq1XKSLNJP19T8D2B4bxnBZyj)
53. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqzkYxavV3S37A1nSr3ZyfkiGUSDFC0WfsMCNvKh22EZ2AMGZpRFh3519u6zn1um1o_XmhZmYFxm7KoQQFqrhV5KMxY0JfREyW3pwMml07j2wgyCkixkWBwofb0oeowhw202wOZiHR)
54. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_-5zvug-mtHmuXqTrdXc_BRMTKRJs9UyJo_07Mhic0Jz5F-yf_YTqJ5os1pUFFswxzolqkBAdTWWZrPjXeM2q1gTMb3wzNKditRfFkJPWMALJevGsuuFH0AgqOQ3T0CBD_ctI0Po7lWo2mtuiuBMmM80=)
55. [nectarpd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFKFAv3EYDnDljg4gvMwUVLBpCtzdeHNqhkpPyVPb6Rg4Zu_oU1jqUGye7fOsY1XkwL6uXk9mDYND2IRl-4GiAsECuTz5y5uPTDsXJVDmyOiU43VTiZVulX4eoYShjEPmWOKMq79QyDvirBupJdcX4SCvmxUzrdi_T6z4Kdh8jkvuWGjlax4tySw==)
56. [prorelixresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaZzvX6cc30Xa7sTEVpsNq8CPVxhQEJ9zD4pxD5BdCYzUlm7KF9cPP6G4mQCsWwjMfiNvtil9LQgyOB9ApzLmHcmHV4sxjbnisNFL7S2e5Jtb-6MleFBxNT23ByRNdVPyM_mAge5hO-uuvFt7PyRWJsGmPay7JG0Jt2FZL8gHykBMlpOt0BQseY0N5aGw6Vu5Ck_K7m1iVBD4Yh3sHPtUwRtyIyHuJCzdb6f8J1EQqor4=)
57. [pharmacytimes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFe2C5-9BQQxKsZP55YxMm9mkSABygfBwJELzs-7W2S3Nua0V1rRZvTXq0VnbvlYPcyLeiRz9WwiHNfCcdef5rI0eY_bWcJVKfeVJJ22DWJpv3zVKcDNctmNvJ-7YRLkZMVL0dXA_uB-e8qO1GJRGJiZWXMLmjDY5OtsmKilY6SfOjOq37OP_9wf9FyHEflZ0m67e358OpbKqkXccvavYAYqqd6bUr1jUl3FA==)
58. [utwente.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuycZzrkd-GAIZ9qApwgLz-aNhZlZIck1tEQQnFAyXNJbJB9IUteZzCv6bZsbCWjKiwu6GPQf0swY9zcdko8IMEFTOmAp3h5kzzOwkqzs9LZU7ZMY6963CKuRpwphPG9ThW-N6fUg_7J1Q0Yqc7NjK5oWtt87HaYWljnxNlaB9rAYUPMjQDL4aN1ZloixFlMO32bXK6CnxxwQMVItZqmx2RQMeYw==)
59. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEirOmo8zP3f6--p9owJjDrrwRGBcXepstKqRjX3rC0LxN17NfY0uLnObuq2MRBxwwlA9Mbpqn8QZHjWPcCO-N1Z-vJT3huxpTHOVB42h8l-3PD0Zo4w8BQewZTFF31rf2X6iEoPtlzAw==)
