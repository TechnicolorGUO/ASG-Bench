# Literature Review: A review of recent advances in tribology.

*Generated on: 2025-12-26 19:00:01*
*Progress: [16/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/A_review_of_recent_advances_in_tribology_20251226_190001.md*
---

# Tribology in the Era of Sustainability and Digitalization: A Comprehensive Review of Recent Advances (2024-2025)

### Key Points
*   **Paradigm Shift:** The field is currently undergoing a "Tribology Revolution" driven by the dual forces of **sustainability** (Green Tribology) and **digitalization** (Tribo-informatics/AI).
*   **Electric Vehicle (EV) Dominance:** A major industrial focus is the development of specialized **E-fluids** that manage thermal conductivity and dielectric properties while preventing copper corrosion, a critical failure mode in electrified powertrains.
*   **Macroscale Superlubricity:** Once a laboratory curiosity restricted to the nanoscale, superlubricity (friction coefficient < 0.01) is now being achieved on macroscale engineering surfaces (steel-steel) using novel carbon coatings and hydration lubrication mechanisms.
*   **Bio-Based Additives:** Lignin and nanocellulose are emerging as high-performance, renewable lubricant additives, demonstrating wear reductions of over 70% in recent studies.
*   **AI Integration:** Machine Learning (ML) and Physics-Informed Neural Networks (PINNs) are replacing trial-and-error experimentation, enabling the prediction of wear and friction with unprecedented speed.

---

## Abstract

Tribology, the science of interacting surfaces in relative motion, has historically been anchored in mechanical engineering and chemistry. However, the period of 2024–2025 marks a significant inflection point where the discipline is being reshaped by global sustainability mandates and the fourth industrial revolution. This systematic literature review synthesizes recent breakthroughs across four primary domains: **Green Tribology**, **Tribo-informatics**, **Electric Vehicle (EV) Lubrication**, and **Macroscale Superlubricity**. We analyze the transition from petroleum-based lubricants to bio-derived alternatives, specifically highlighting the upcycling of biomass (lignin and nanocellulose) into high-performance additives. We critically examine the rapid maturation of "E-fluids" designed for the unique electrical and thermal environments of EV powertrains. Furthermore, we explore the integration of Artificial Intelligence (AI) and Machine Learning (ML) in predicting tribological behavior, a development that is accelerating material discovery. Finally, we address persistent challenges such as White Etching Cracks (WEC) in wind turbines and the scalability of superlubricity. This review aims to provide a rigorous state-of-the-art assessment for researchers and practitioners navigating this dynamic landscape.

---

## 1. Introduction

Tribology—encompassing friction, wear, and lubrication—is a cornerstone of energy efficiency. It is estimated that approximately 23% of the world’s total energy consumption originates from tribological contacts, with 20% used to overcome friction and 3% to remediate wear-related failures [cite: 1]. Consequently, recent advances in this field are not merely technical refinements but are critical to global decarbonization efforts.

In 2024 and 2025, the research landscape has shifted dramatically. The traditional focus on extending component life has expanded to include "Green Tribology," which emphasizes ecological balance, biodegradability, and energy conservation [cite: 2, 3]. Simultaneously, the integration of Artificial Intelligence (AI) has given rise to "Tribo-informatics," allowing for the handling of massive datasets to predict complex non-linear tribological phenomena [cite: 4, 5].

This review is motivated by the need to consolidate these rapid developments. While classical tribology focused on hydrodynamic lubrication and metallic wear, the current state-of-the-art involves dielectric fluids for electrified powertrains, hydrogels for soft robotics, and atomic-scale manipulation to achieve superlubricity on macroscale steel surfaces.

---

## 2. Key Concepts and Definitions

To contextualize recent advances, several evolving concepts must be defined:

*   **Green Tribology:** A sub-field focused on maintaining ecological balance. It involves the use of biodegradable lubricants, biomimetic surfaces, and systems designed to minimize energy loss and emissions [cite: 2, 6].
*   **Superlubricity:** A state in which the coefficient of friction (COF) drops below 0.01 (and often below 0.001). While traditionally achieved at the nanoscale (structural superlubricity), recent work focuses on **Macroscale Superlubricity**, achieving these regimes on engineering scales under ambient conditions [cite: 7, 8].
*   **Tribo-informatics:** The application of data science, machine learning, and neural networks to tribological data. This includes **Physics-Informed Neural Networks (PINNs)**, which combine data-driven models with physical laws (e.g., Navier-Stokes equations) to improve prediction accuracy in lubrication problems [cite: 5, 9].
*   **Tribotronics:** An emerging field that couples triboelectricity with semiconductor electronics. It utilizes the electrostatic potential created by friction (tribo-potential) to gate and control charge carrier transport in transistors, enabling self-powered active mechanosensation [cite: 10, 11].
*   **E-Fluids:** Specialized lubricants for Electric Vehicles (EVs) that must possess specific dielectric (insulating) properties, high thermal conductivity for cooling, and compatibility with copper components and polymers, in addition to traditional lubrication functions [cite: 12, 13].

---

## 3. Historical Development and Milestones

Tribology has evolved from the empirical observations of Da Vinci and Amontons (classical laws of friction) to the hydrodynamic theories of Reynolds in the late 19th century. The 20th century saw the development of elastohydrodynamic lubrication (EHL) and the synthesis of additives (ZDDP) that defined the automotive era.

The early 21st century introduced **Nanotribology**, enabled by the Atomic Force Microscope (AFM), allowing researchers to understand single-asperity contacts. However, the milestone of the 2020s, and specifically the 2024-2025 period, is the **integration of the digital and physical realms**. The field has moved from *observing* friction to *actively tuning* it via smart materials and predicting it via AI [cite: 4, 14]. Another significant recent milestone is the shift in focus from Internal Combustion Engine (ICE) tribology to EV tribology, necessitating a complete reformulation of lubricant chemistry standards established over the last century [cite: 15].

---

## 4. Current State-of-the-Art Methods and Techniques

The methods employed in modern tribology have diversified significantly, moving beyond standard pin-on-disk testing to include advanced computational and characterization techniques.

### 4.1. Artificial Intelligence and Machine Learning (Tribo-informatics)
The application of AI in tribology has matured significantly in 2024. Machine Learning (ML) algorithms are now routinely used to predict friction coefficients, wear rates, and remaining useful life (RUL) of components.
*   **Predictive Modeling:** Researchers are using Artificial Neural Networks (ANNs) and Random Forest algorithms to forecast tribological properties of coatings and composites, achieving high accuracy without extensive experimental iterations [cite: 5, 16].
*   **Generative Design:** Generative Adversarial Networks (GANs) are being employed to synthesize new operational scenarios and model surface topographies, aiding in the design of textured surfaces for specific lubrication regimes [cite: 5, 17].
*   **Physics-Informed Neural Networks (PINNs):** A major breakthrough is the use of PINNs, which embed physical conservation laws into the learning process. This addresses the "black box" nature of traditional AI, ensuring that predictions respect physical realities, which is crucial for modeling complex EHL problems [cite: 9].

### 4.2. Advanced Surface Engineering
*   **Biowaste Carbon Coatings:** Novel techniques involve treating biowaste at high temperatures to create graphene-like nanocrystals on metallic substrates. These coatings can deform and coalesce in wear tracks to form graphitic films, enabling robust protection [cite: 18].
*   **Laser Surface Texturing (LST):** LST is increasingly combined with solid lubricants (like MoS2) to create reservoirs that supply lubricant to the contact zone, a technique now being optimized via AI [cite: 17, 19].

### 4.3. In-Situ Characterization
New test methodologies have been developed to address specific modern challenges. Notably, the **Wire Corrosion Test** has been standardized to evaluate the corrosion of copper in the presence of electrified lubricants, a critical method for the EV industry [cite: 20, 21].

---

## 5. Applications and Case Studies

### 5.1. Electric Vehicle (EV) Tribology
The transition to EVs has created a distinct branch of tribology. Unlike ICEs, EV powertrains operate at much higher speeds (up to 20,000+ rpm) and involve significant electrical currents.
*   **Dielectric Fluids (E-Fluids):** Recent research emphasizes the development of fluids that can directly cool electric motors (immersion cooling) without causing short circuits. Studies in 2024 have highlighted the importance of balancing thermal conductivity with dielectric strength [cite: 12, 22].
*   **Copper Corrosion:** A critical issue in EVs is the corrosion of copper windings and interconnects by sulfur-based additives in lubricants. Recent case studies utilizing the Copper Wire Resistance Corrosion Test (CWRCT) have shown that vapor-phase corrosion can be significant for certain polyalphaolefin (PAO) and diester fluids, necessitating novel inhibitor formulations [cite: 22, 23].
*   **Thermal Management:** Integrated e-axle fluids are now designed to manage heat from both the motor and the transmission, requiring ultra-low viscosity fluids to reduce churning losses while maintaining film strength [cite: 13, 24].

### 5.2. Green Tribology and Biolubricants
Sustainability is driving the replacement of mineral oils with bio-based alternatives.
*   **Lignin-Based Additives:** Lignin, a byproduct of the paper industry, has emerged as a high-performance additive. Recent studies (2024-2025) demonstrate that lignin nanoparticles, when functionalized (e.g., with ionic liquids or MoS2), can reduce wear volume by over 70% and friction by nearly 80% [cite: 25, 26, 27, 28]. The mechanism involves "reciprocal hydrogen bonding" which strengthens the lubricating film [cite: 25].
*   **Nanocellulose:** Ionic liquid crystal functionalized nanocellulose (ILC-NC) has been shown to reduce the coefficient of friction (COF) on steel surfaces by 77.9% compared to pure base oil. This represents a significant leap in the efficacy of renewable additives [cite: 29].
*   **Ionic Liquids (ILs):** ILs are being tailored as "green" lubricant additives due to their negligible vapor pressure and high thermal stability. They are particularly effective in forming boundary films on metallic surfaces [cite: 30, 31].

### 5.3. Macroscale Superlubricity
Achieving superlubricity (COF < 0.01) on macroscale steel surfaces is a major recent achievement.
*   **Carbon Nanotube (CNT) Coatings:** A 2023-2024 breakthrough involved using a sacrificial coating of vertically aligned CNTs. Under minimum quantity lubrication (MQL) with PAO oil, these coatings facilitated the in-situ formation of graphene tribofilms, resulting in a COF of 0.003–0.007 for over 500,000 cycles [cite: 7].
*   **Hydration Lubrication:** Inspired by biological systems (like cartilage), researchers have achieved superlubricity using hydrogels and hydrated anions (e.g., sulfate) on positively charged surfaces, achieving COFs as low as 0.003 under high contact pressures [cite: 32, 33].

### 5.4. Tribotronics and Smart Sensors
The fusion of tribology and electronics has led to **Tribotronic Transistors**. These devices use external mechanical stimuli to gate current, acting as highly sensitive active sensors. Recent applications include smart tactile sensors, logic circuits, and artificial synapses for neuromorphic computing [cite: 10, 11, 34].

### 5.5. Soft Robotics
Hydrogel-based tribology is critical for soft robotics. New "biomimetic skin" materials are being developed that offer low friction for movement but high grip when actuated, mimicking the adaptability of natural organisms [cite: 35, 36, 37].

---

## 6. Challenges and Open Problems

Despite these advances, significant hurdles remain:

### 6.1. White Etching Cracks (WEC)
WEC remains the primary cause of premature bearing failure in wind turbine gearboxes. Despite decades of research, the exact mechanism is still debated.
*   **Current Understanding (2024):** A position paper by the German Society for Tribology (2024) highlights that WEC is a multifaceted phenomenon involving mechanical stress, tribochemical reactions, and electricity. The consensus is shifting toward hydrogen embrittlement, where hydrogen generated from lubricant decomposition diffuses into the steel, causing subsurface cracks [cite: 38, 39, 40].
*   **Detection:** WEC occurs subsurface and is undetectable by visual inspection until catastrophic failure, posing a massive maintenance challenge [cite: 41].

### 6.2. Scalability of Superlubricity
While macroscale superlubricity has been demonstrated, maintaining it in "dirty" industrial environments (with dust, humidity, and vibration) remains difficult. The breakdown of structural superlubricity due to surface roughness and contaminants is a major barrier to commercial deployment [cite: 8, 42].

### 6.3. Data Quality in AI
The application of ML in tribology is hindered by the lack of standardized, high-quality datasets. Unlike image recognition, tribological data is highly sensitive to experimental conditions (humidity, surface finish, machine stiffness), making "transfer learning" difficult [cite: 9].

---

## 7. Future Research Directions

Based on the current trajectory, several key areas will define the next decade of tribology research:

1.  **Digital Twins and Virtual Tribology:** The development of comprehensive digital twins for tribological contacts, powered by PINNs, will allow for the virtual testing of lubricants and materials, drastically reducing development time [cite: 5, 24].
2.  **Sustainable Additive Design:** Future research will focus on the molecular design of bio-based additives (like lignin and cellulose) to rival the performance of traditional ZDDP and MoS2 without the environmental toxicity [cite: 25, 43].
3.  **Active Tribology:** Moving beyond passive lubrication to active control, where surface textures or lubricant properties (e.g., using magnetorheological fluids or tribotronics) are tuned in real-time in response to operating conditions [cite: 10, 17].
4.  **Standardization of E-Fluid Testing:** As the EV market matures, the industry must coalesce around standardized tests for copper corrosion, dielectric breakdown, and thermal properties to ensure reliability [cite: 15, 20].
5.  **Hydrogen Tribology:** With the rise of the hydrogen economy, understanding how hydrogen interacts with materials (tribo-hydrogen embrittlement) in engines, compressors, and pipelines will be critical [cite: 17, 41].

---

## 8. Conclusion

The field of tribology is currently navigating a profound transformation. The years 2024 and 2025 have solidified the shift from a discipline focused on fossil-fuel-based efficiency to one driving the **sustainability** and **electrification** agendas.

Key findings of this review include:
*   **Green Tribology is viable:** Bio-based additives like nanocellulose and lignin are no longer just "eco-friendly" alternatives but are demonstrating superior performance to traditional additives in specific applications.
*   **EVs require new science:** The electrification of transport has necessitated the creation of "E-fluids" and new testing standards (e.g., for copper corrosion) that prioritize electrical properties alongside mechanical protection.
*   **AI is the new microscope:** Tribo-informatics and Machine Learning are becoming as essential to the tribologist's toolkit as the microscope, enabling the unraveling of complex, multi-physics phenomena.
*   **Superlubricity is scaling up:** The realization of stable superlubricity on macroscale steel surfaces offers a tantalizing path toward near-zero friction mechanical systems, though robustness remains a challenge.

In conclusion, modern tribology is no longer just about "reducing friction"; it is about **smart, sustainable, and integrated surface engineering**. The convergence of material science, data science, and ecological responsibility promises to unlock significant energy savings and reliability improvements for the machinery of the future.

---

## References

[cite: 4] BookAuthority. (2025). *New Tribology Books*. Retrieved from https://bookauthority.org/books/new-tribology-books
[cite: 14] Zhao, L. (2025). *Tribology research in the twenty-first century*. Tribology Education. Retrieved from https://tribologyedu.com/2025/10/18/tribology-research-in-the-twenty-first-century/
[cite: 17] Farfan-Cabrera, L. I. (2022). *Current and Future Trends in Tribological Research: Fundamentals and Applications*. Lubricants, 11(9), 391. [cite: 17]
[cite: 5] Marian, M., et al. (2023). *A review of recent advances and applications of machine learning in tribology*. [cite: 5]
[cite: 9] Szrama, S., et al. (2025). *Artificial Intelligence and Machine Learning in Tribology: Selected Case Studies and Overall Potential*. Tribology in Industry. [cite: 9]
[cite: 24] SAE International. (2024). *Modern Tools for Tribological Optimization of EV Transmissions and e-Axles*. SAE Technical Paper 2024-24-0013. [cite: 24]
[cite: 35] Plastics Engineering. (2025). *Soft Robotics in Medicine: A Growing Trend Powered by Hydrogels*. [cite: 35]
[cite: 36] MDPI. (2025). *Recent Advances in Hydrogel-Based Continuum Soft Robots*. [cite: 36]
[cite: 10] He, Y., et al. (2024). *Evolution of Tribotronics: From Fundamental Concepts to Potential Uses*. Micromachines, 15(10), 1259. [cite: 10, 11]
[cite: 38] Evans, M. H., & Hosenfeldt, T. (2024). *Position Paper by the German Society for Tribology on White Etching Cracks*. [cite: 38, 39]
[cite: 12] Knowledge Sourcing. (2024). *Powering the Future: How EV Fluids are Revolutionizing EV Performance*. [cite: 12]
[cite: 13] Gahagan, M. (2023). *Latest Developments in Driveline e-Fluid Types for Electric Vehicle (EV) Transmissions and Axles*. STLE. [cite: 13]
[cite: 22] Alvis-Sanchez, J., et al. (2024). *Copper Wire Resistance Corrosion Test for Assessing Copper Compatibility of E-Thermal Fluids for Battery Electric Vehicles*. Batteries, 10(8), 285. [cite: 22, 23]
[cite: 15] STLE. (2024). *Feature: EV Lubricant Challenges*. [cite: 15]
[cite: 20] Lubrizol. (2024). *Lubrizol Test Method for Copper Corrosion in EV Motors Wins SAE International Award*. [cite: 20, 21]
[cite: 2] MDPI. (2022). *Green Tribology: New Surfaces, Materials and Lubrication Technologies*. Lubricants. [cite: 2]
[cite: 1] PCS Instruments. (2024). *Green Tribology Trends*. [cite: 1]
[cite: 44] Rahmadiawan, D., et al. (2024). *Alkylboronic acid esterified cellulose nanocrystal by an improved green method as an efficient lubricant nanoadditive*. Chemical Engineering Journal, 496. [cite: 44]
[cite: 29] Shan, Z., et al. (2025). *An ionic liquid crystal functionalized nanocellulose lubricant additives*. Carbohydrate Polymers, 347. [cite: 29]
[cite: 18] Asumadu, T. K., et al. (2024). *Robust macroscale superlubricity on carbon-coated metallic surfaces*. Applied Materials Today, 37. [cite: 18]
[cite: 7] Gamaralalage, C., et al. (2023). *Macroscale superlubricity by a sacrificial carbon nanotube coating*. [cite: 7]
[cite: 25] Shi, Y. (2024). *Lignin based green lubricant additives enabled by reciprocal hydrogen bonding*. Luleå University of Technology. [cite: 25]
[cite: 27] Manzolli, et al. (2023). *MoS2 nanoflower-decorated lignin nanoparticles for superior lubricant properties*. Nanoscale Advances. [cite: 27, 28]
[cite: 5] Aulin, V.V., et al. (2025). *Enhancing tribological system performance through intelligent data analysis and predictive modeling: A review*. [cite: 5]
[cite: 16] Rosenkranz, A., et al. (2024). *Recent Advances in Machine Learning in Tribology*. Lubricants, 12(5), 168. [cite: 16]
[cite: 32] Lin, W., & Klein, J. (2024). *Hydration lubrication in biomedical applications*. [cite: 32]

**Sources:**
1. [pcs-instruments.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6y_sxi4pDHsioTqnIaazx68S6rUTXMDgrEmRLGMUYyfgQtpBS2hqfwES4ILQGiznAqrzVKVlS3CfOSwcMfzT4gAzZPm9R4YLtQ1DgRjr22V4RLEcMu7V1elzlRuJ5phnh6uCEDlLWcfBFgusYGGbgQP8=)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrDowpVVwbgO-FUKX0C8ImJyght-E7-Zkbikfb1T9Smbx3-lbmNBNStzqOO6zvqjErcMu8o73qtq53aZsgxWunP7s12iwcGgi3Sx9kFC7dHksQE58g8cVie7iUuLnmAIA81tJlhPq0XcAsiJxlW8yFeyv5MZDSev14K0-H1EUlktktie77)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxGsNDDSlIU4B8N8R_WzJbEaVDRs_J4XgUbVs8ZdhEJb26RFIzmWkA2ifJ36Ij9JwD107r3YqRBZasLV1aCvVrY_XOuz0melXi2S_qaReAie2sio-cAgW5rbBVXpw9WbGMdiUBimpyAF2uMR6b6jIChV8SnotmLAmprvm1JshKzQ==)
4. [bookauthority.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4wPX4TaD7cO3tpUKtH9sv4pKS0w4kIg_2tHNVSGinS0xFykMk21x5ZHliJXXvhZGsEHvTpznTgMT6UUM5Vq1hevuaa5AwxNa0AIKT4jMTW3Vz5E_hhvJs2X_T0aEa4Cfee2m9hzfoxwE=)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjTzhq_IOeYkQcR5taWGxS7sR6s5auyHYDUlr1JvAm7W42sHBv0SdtdPg5-Lsu3SY6GVqz64H3g7MsCXNv4MvdXz-S5gXtUKrrvQ0-Ja5rB8qGel8JBPyF7Jw4e18SGMeX1tBCXaWX4iL-cwL28JNQoY4jGDAxA8WVxRJ88ja8lsL9uKAn-wgaV6SrCJ_SUc12CKkQvANZdcWhBZ6jT7iwGpF7zShuYJqLDlzsKiMPJWBFBoaTdtI=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMG0z2FvMF-KDhdOIgJPmgAuLrsj4jdWcO5UChDHxmngWeSB4KLLx81RHFaYkL83diEc1lELuWYE64v9jeqWZomhmD7hkRBTaL0fzyHHJ2kTyhoO9rc0AJP9-EeqBQPAcsrr0mD2l77hzV5t89xlAM84fxLB2H1udK6oFkKT0g1DevapSRXPgFBHhVg279Q==)
7. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqZu7GyIufECSy3jIVOGwE_ZQulk87qvSTHEvPQP0YoeBHmjYYKMPPY5QDCvERzF3t_elYWmfwzAU_bYuAU2MWN7cPQPYXZrkF9ksQTQW8rYO7NI6h5JmAXllqq8Wwcw==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlWPHX3BjU8cjvZWJndgOOjalEJGqFt0CjbOEE5y_NqItBpQK5BQ2z0eoefltU8of-nDrm1zc2jJcmI3vq8SF9uT7UBS7lsp0tWva5PhKDDlXeFYrSawc4UcEfxlJWVQhX3dFc1HAWyzo2RZyZmxLzyXhaDOErIidne-TrwOXcpzjq3qRBgCOpsnprKx6g3gFVP1jtgr_O7s_QeCg7EBkEIUefC4MT6a5ovso=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvkQ-L8Huoq1EGkX0adupoYq4OZ1_zTy7vHtQPvbJ57pMFiszbAmLiZE-FBGKROCqEnggKMKdL-D3df4K4TZGNCsDelUKh_jESLZGGcRM481jpyJx9kknH4gq66DoWQ8Ph8zHMs3gtMlEsbHtq011NTY-FweCRYNNxvEitK8YCUlnczYZ0TLIG818fA4Dp29_8ov-AKcoiYLCKAsORFvxvtreM8JmiVNMsHF1UzQQgzG5uL_XqmVV_NVB7BpeOh21XKENI-Fzhh5kUddBrrvw=)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2lg-e7TV9I60bg5KJgHE0tWRnCHn5ulKoTOL9_6nb42yRugT-BYBrsgLAJUEGatpxXKsTXJo9rb_1UYDviTB403cGY0cWwMQJsMPg_Fq9oozcWWO68BbQHCHtPWLEqw==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDIRzdNSzwWlZtjCp2-sCszcM_2nH4pHj6KG_TgVHnTHDHhG7zbd5-hNXxfB1KjxzKkXDdNUesjHLEKn0RHuS0LnHHrLI_vQ9lc3YOLSBbBvcwj4p4dT87nj5qX6Ck3EWSk2NsuzIPVaQ56aVv_OoSDL_dMioTBBncretx-SgoKo7IhT-8yqXCZA0na_AgE8oWr-5ZT6V9ZVZbacNdI-D1Sk-0Haeh1C4g3lbrSew=)
12. [knowledge-sourcing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsrVb53AZga_fTGNAN42w-4kdeAmVnupjZ9BnYyvn_h8LE-zfHTL_svYkSkHc4nGpYFQTNBRgvzG-LI-wQFeiEneJQ-1Hj1rS08ubeRp-O-33W5R1q9lvo0fEo27-Tn_yKuJGyZ7xKYb968exwTSL08vdP-8adK5O_EHcQdcnXJs6UFS2deptvcQuMr8kwak2F0qrrLs7_OaLQNF7YlFzGd9aBK0Rl5S4GwlF_uDo=)
13. [stle.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTlVaoj-r2hNTo5LpJgORWvRZNHdBX68D5okNmmbLaQ5RtxmVpr1TomX_uXYMdbgHP4b3978zeKh1KXpheAWsMmzw7EhC0WhUJC4bEGXu7z05Q7ePGgeS_E4xEQMoUoXLT2HerhAJuLlmhjPi6io_HSyahUjbzN4TriPmEDN2-189X4iBW3U9CZ8uHGRsy_vprwhie)
14. [tribologyedu.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVKYx6LUZVDO8PKOvjkDZoTU9YmLets9gjTXensriezPMyeTwNhwL6U6HnjYSKywKKUWAGc16z62Rr3bVp5f3zv8sNe-DuFQs7g6ipaBrw0g9_5Z_4arSenc1aoIk7OYkbRsZRnPhaUVU1QIC3Agr3OYaQJC7iBD29LyTx2Nze4KBgjAWTDK06BQ==)
15. [stle.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHorrWuFauC8522pSQymV_mt8Ptzmg6ZFSQaK1ilLfHgKP93UDsaE0eXANTKazOs7EFWgVqrP2sKzMIrS-Fqi1quuqE-3RRMdRYV9wzlIJVF7hiA6ibSYVYIkF1M45lZsA4sz0yYFLBBFU3JE7qbw_RlP5ekGeunzVn)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfj6gFfGpOqKkX7FhMtNGNxLJYTPO79Nn7q7Rx_sDmqQj2_p0Ci8g5qm3jK2qtYEUAOf37CQrqbXPuAc1KV9txLjHNBEOqzAs3zrFWdrhXTj5MOF1Yx6ToaJb9J-bxwdz25eorSNR03Jbjwp2bFi7mtqjxp7izFWSAnML_Dt2f03a92W-uUh7tQVErp-Lwe0u4p3jGApB4mDY=)
17. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9gNpqvxfbTURmHy_cxOQ8RmKiVcu-8OI0lbPP4dw_CGfGNYefuQX3Kr7Pg7gxjOtO8J-akfTgs3s02ofKErYAQnZyHkFOxFIpx0rHWheoOIDcyvP_SLPqjs_C1yw=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgqx7Tbq-aZiElHYPxp8I_-CMssrCQmPt_3O7oTXSXqVG5we4ZXaOPbsdDZeIYg26MoRw9nccBwvjEThGc5ZCaWSzYMALfxWl6jkAhiV-s76tB3fNvHJOn_1_HUlgpFj4zDQW6oItUpPKKqPUF2NgNjKujTicaAmAnG3mBKNhek7V2R-weRvQMDMwm_t7RRb-DS6oTH3DGWzhBfGqXr9KU1-Si5Rn2yUUwjknS)
19. [setcor.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRuQNB4lUoPy8UxUYbNsHbghMXA7UDPsZHIqzxxIJFsTzRS92DFqNtcd7NiZMetsuxEle_OD1Rv4i8qIyUxPj9_CtoCNxpKbrU_EZufcNeNBsCg7Z8nBegZ9yBXEilbywKzKr7gH930H86oy56etOl4ndUbad1lLMLdXSUpUBUFNQkIE8hVgJSOBkokcA7-mwpoP03XX2MErsjmdFl96OB09bIlGHzBru286Y=)
20. [ntb.no](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2zOFK7Iz-pTzY4glDRFB2DIDEOl1UB8Eq0rApTXGfReoyIXWf7llGAVNeh3mI4_Py0lkbRWraE9Z33fO9Nzy68RysoLbG2RwPX58asOZDbw2cCEljNLX1UAhxdZufsCa4MRAR6B5c8MPRM6oaU11im-FZoGejG24Ub5Pi1CUZlTYSOpTdMLLde3PS8a5HWW-yld_5RGzOwJXzPpnzK9x11yQc6Vu8JBkUiBEScJGfu3CBZzp-ZSdJDN9gBtbnyQpaVmF8nD1eliLyysIyrutw)
21. [businesswire.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRwSYKCr7cF74Y1y9c8R1XjcEAmOVVZcZcJlT5NV3pA1K7ifjbOGwtaqCyYS3qotrOrdkT_S5OARIXsw3hiErWBv3XK5DI3o_yKCuzerJB5QeShabl_wJB5kSnJQuYXYjLQryrSRfePoqQLSYwqBdmVidL9Mwk_Tn_BMSAn2_uZ3SpFRIQWCyRNxVA4ZUjsbCD3UrAX8olrrzzHOtWN7gzk6MM1-GskuQN421RlU1OKgIAzGuKJK-yBcb9Bq9QyjNd4EE=)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd5y-0j5JoMfDX53bK8tm3KMPz0ypBbrAyOeTKrWjSz50xqS1CUnXHIUqHkjDpqqJAbgk1fxnZy63IsC4DhXgNoXidOkcYY2g6275Yay4du9G0njmpnxM9t1Fert8=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLRc0iLBMtihAVJzW3HzhquOEAqfCOvIbVjSA3beS-l5pYgD52-4BLoAApemR3OnSQXB5UiczZ9cFSUVg1jBozstASyBJlUZ1PFQvzk4KXZkZ_qpnj8BZjnSvnKxmP0Yj32htL-O6dPnuIptuOeBG6P1-jSaUgXZL7zLSZrLERIdDvlYdUUBSRGiFBm5yvHtUMghLpc6BOgNLRdHIYbNbUVjTv_qYKIyMGzYaHyZJDjbNSuUhYMaRBEpNkqz6DbVJyezze_C6HXug5LzwZk6a1J91fQY0AS9PdysE6SdFeToo9K93YXIllUg==)
24. [sae.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnJTAveNIMsF0mi98hQCzI2XW2CXiK_0yRp2jnqDGUAhHIgEpY6uv7-L_FDhItBsnRZbFdehFxhgBZBzGbd-0VhDiJKGWu1N93NBeseBk4zdvtladh_GMXbMVeZdoFoQkpf6xIN1WJBWV1eEKQNlF9k-dn00ebkV8WhJcVy6CcJ0IxDbcfcAqL4ne72J07vLXATXZj--TfyrCEJh6u)
25. [ltu.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFi0EGHNHBA2bgbhyoay5Xp0ZUNY32ceFTy4Uu-GKSae_RaHD8D6GAaUFh_DQiASQ5ZQCYlDrXQ_auNh9jJEJit6T0dPZDT8Agb5Jc9lJdYrkFoHXp7GWRbO5x35KDlM0n3vpoK8ZHtiYvV6a16Bs0mJoGDoKqZW6BQQWqbG4nylnKQNJJdiiXe5Dkzi7rKxtb1q7-2a47qoiJFDWWPhf5rJ2xGuGSsYngIxrN2uL_f_7btXKnXfXFY41BElmGgHjV-1dVUTmbUtoIZ3bUsn821nOt8BZZ22nSuEPOqitsTUvWMN-SDinF3i_-mB9Ymmzc6xe2TSwOjxeMNEkyGBtOlbnV7ltycx50=)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD6uQomu1ovZzpSDZ-gRFoQGj_PGuOposjtq2vZ5bjbn74ndg4jV1koDJDFG3gFJt-Wefka22YDdAO8x60xj8b4jk55CxYQSu9MxygqCVhV16TKugP4IqjCoeRkgixBg==)
27. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY7dWeMA_VOIY2V-g8gSDP0XS53Q4yqeVPdpAYFBCPsc3ezoG2UeyRC9XX9B-F_03iN5un_97DRlaTe_bO_RkBKCEgbDSON4iR8l2UrBf10nudWnk0yNpXsZ-bFt8lNADGCAVCuDHhu_O3BR_-lLqzqwUm9LLEVg==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-PMIxMRAWT6586K2nju7BeRk1hVJ3n0JMYoZaX7PiHzGQOse3sa14DoFq5DSwE_VQsDknWWJTTjculrpdRUD1NN7qf2j8O2RID6RpxqBG9DzOmvsBndPOeDfqAJJwydwYC6NmMRdDTdTc-khiiF6Qw16Ou2kSV-GJb5f_0s5_qTrO24ggNEsVrWx8GlVVrn3SyW_-xTvTbyq7jVp-j-uXJ9-bM1KFi3mB1lPumCe-h4tVb_aYAYcVC90)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkEZnroFqrbApNfHSAAK11u0j35k4xu6nt5OxOa3D85T53uhtaL8U3GIGAfPzWV3P_nkSw6TOcusXe_St0zoNmhEEmUYrc_7_W4rKF5wI7GbNOZiDHAHmXq-l2Lmnmg==)
30. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-xwD6jlvDQyFDecAxYW9uVuix6dbvtcy2UWhf3u0n8gkslbd6Qn_vjEUKubhmrY2bGfO7fo0TG0oOztht4EZQQrSs-aQ1C7i-pVyVbOH5Rvhb7Z8ic-KrPfsctNepP--bFmryYRP7p0q_VM3kUQtU3s6yLW0LGsZk_I-2mXSLa34et5W1XGzMmirhNoL1Lad7VssV1Rxp_VDGOBnCQar_guV_gF2bCWVXI1xrqHMhm4P5kOxAMnPx469vOw==)
31. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCWSXv3N47OuZq0C6CWtOnEPBFgttkOtO4kiRzhjPYBeO27cXYIECtnbiKqsVN7h3kPZXqBjvIuLfzJtRbyhgfeKZzjEsoRsb9uJmp6jQjHhjpXAmDTZZ4unrMbmZlvwj_-5KSELhbYUL6)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUO1Som6121UG9BgIHiJ5l2wjr3ec_Q5Si551QtRHLTcgRecxsYHd0xm38QFuyVLFtuzHTH0XPmqOuEw-FAkzNZM8TuFv99-XaJl-VXxKBEqRhkrhKrllW5Aeqm9gpkNNLkO2ri_zV3A==)
33. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwy5p6M3ofwypKb8GZJXE4uxQDaneBKmnoMlZYgYfUDiy8fA0jRw6mdzznHEBlf-ISrEkokQaaE9hBQiq-vBfEr71pfSqGROTm0rj8rHD8tJjIBLF0WKkzk6pG2rsK_GRY5wz1QzfNqYE=)
34. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKXS02BmDClUPuNJceWp2_IgMiCBnHeeFqxOf6hwzToWIc82-fmCZOuTwuVr6ku5Gl3Gs5qnOWkD2OBq2dDO7rtk4SbAmI7RGCBDyi6faLdyezcBPEb5rqQ30bTRW9tw==)
35. [plasticsengineering.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGIdzHRCQvhUKU_p8pB1vw4qtEZbHqipC3W08vCtS0SuGTAXo6TRg4AAzqy0Si1nD0idpNDQNLsw9lU_2V10varHUwCNwRMbbtL-O32pt8FrOwnmbdZ2c3RftPOoeJz3QCaH4N2VHTzpLu8rG5Iu4qHCcJS_egh08wI0NofzF3Qsizjt1l-WHPSQKFrieUy-MxtEINTRmWAyzc3K5vz9uIcZ02LfL_bhA=)
36. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdNSFSJdDJ4pirCXUAL0vCUmNDhclsqmTEyB6Q9F4QsX-sALFoiyd1M9nm2LRQtEdE8TSpFM4CwVkXvrm4RT45Jm01zOK6dxayOdQSLTAjfRy2eDPECmgPe5fmpkQ=)
37. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNrZl8c16d9iSGEw0M8RemyKvyOx1iuPOMlR36LONXP6uBbqK3J_ts4la7Feopkw3gu0ZKyi_QH_MLduLh90oDAxR6FwhuD0Rsv2hqhXfKPQSJuGgLytoaj-Bn_gE=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9apN3A1TdADpgQBqVK1lzxo1arl1a5a-6JMEIu0hDzoHTLg7QhGEhluB_gT-qw0IQH4j195SivhIK2nxNIgUhSPZ6kHkllo9zol2mPTeE5HPYC1PA1aIjvdysMBXFM8WD_EsKNFelX8SCEHEjH3haBLQtaTzcvIftDNZDJCkkG8NLEzvPBJDv8Ftj7DQv6YMklFiLKjOxOMR7gvsGWTPbTMi1EepNhMRmzgw3oUSAgXTIEeU1qjextAQZCX1DkCaKX6vuvYY=)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiviV2stti4Dzo7sjfQtcO8NvddpbfSbE_W_Dh4jR8GKlB_qYjzlFEMtV5NlQ1w97LCnTXkbHERUXNTMA3xjxnh4E2l0Ax7m2XXfmcuHODtOzTfAXZFlUH8sfJb-UQl4oF9B9l91Zy4vT78rlo9WwwkIjhbxX6C3K5nJM317BLIPArrivYgjK9-Jh9kmixKyxuPs8w85W05WJNieeSgaVYXR4Jh2g4RTZV9HStvVnAz6tOHL6a)
40. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOA8Ak2Fxxiv4J-02pFvkdZZwQcoNHdjHUxSyYRUZ3OWSsiUM_m4aiG3ucHv5uSARsDby3ZqOw-z2VorEfHEJnwT6uiLJi53GZtjgWfisB5qH8TAlEOIhov8gKAVtW5oX6KK6ggnUxzuC7kBFo2vTgmmQSe-eF53B4heGIK2GBJNMf08hzumbr0Ub13D9d8YYwk88RazDbBA3g)
41. [mobil.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh1xpMmOiYDV8nM4iHQ7gb_Ix15CfeNF7raOLQ6ot56djN1epPeRmDrreA8sfVSTlHGVnRH8Tfu-eQIA1l9Ukg98U-XoiYEJHkJKenrb-9hAyB93AQCt1OD-yPvaMSG-UYP4L6wlnpgdN7uYa5pbeHJPEnGZrbKpyLxTQUfY8kpKQtk6ntqEuvVoR8-RwJow63ElzpAg5DEC6uSUOpp0c-f1RC_an8yBdms9-YRj6RZvL6DasgOyVCtTm27HmRQAFI)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6v58iNlvGw7sAW5wcspjuEPZwfjbGGJNwvl1_JwyS2JKRVyebJIeMtbdYXt-2hfuLTtaC2vu623-N8gvsHAlbz-XRB358huWcsUE9ASUbL8gpXZATS-2wOrsw1m716m7kTHCzvjKstQ==)
43. [infineuminsight.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Fo4VJIhuEN2hggldxhmDIjgUuThSpRZEP89ZBfF6YGeNDUyJslJ69YB-Mkg-DgMiFK0-UOqjd9xDpOcR35FNIxT8ezdmnTZW-cDUqsDHDT8qWJ0_F1b9HdE3V_430ylEwm2DQU4c8EyTuSj6MSaJ-4WhkNGTt1jwqspjvx6nhxbdUTIttpwHGA==)
44. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnK1rdq8iYt05P6V2Xt78xwwNeeWm6eUhjUDzrK4W-LZ7827MQgPguYL1M8qLn2njPHLvaMrTd1wdEGkM-3H3VdbqC92qiwq6n-NRBT4PZTLmPJjpbSVxNUDgSFbpHZ-hp1pSJanr-AolUb3CYDSDPsekllcChNd0mpRMnnl7Az5U5GVEKQ0AcQqlTePp5HUaP-7W6YoByKmdBuDjJbjpZmwfNDkicGCVKVRSKa29ggwbiL4CHcn54BkP8D9lN_dKlTenE6RH3oDrYA6k6j0mN-OCPhF_WYwgI3HdQ16jFQrBfCZsaXs6Tbymm_MKoZL1ArWW5YbgjLHYWRlre92U=)
