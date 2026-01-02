# Literature Review: Non-Hermitian Topological Phenomena- A Review.

*Generated on: 2025-12-26 16:36:44*
*Progress: [21/21]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Non-Hermitian_Topological_Phenomena-_A_Review_20251226_163644.md*
---

# Non-Hermitian Topological Phenomena: A Review

**Abstract**
The synthesis of non-Hermitian physics and topological phases of matter has emerged as a frontier in condensed matter physics, photonics, and acoustics. Unlike conventional Hermitian systems, where energy conservation and orthogonal eigenstates are paramount, non-Hermitian systems—characterized by gain, loss, and non-reciprocity—exhibit unique spectral singularities and topological invariants. This review provides a comprehensive analysis of non-Hermitian topological phenomena. We examine foundational concepts such as Exceptional Points (EPs), the Non-Hermitian Skin Effect (NHSE), and the distinction between point and line gaps. We trace the historical development from Parity-Time ($\mathcal{PT}$) symmetry to the 38-fold symmetry classification of non-Hermitian topological phases. Furthermore, we critically evaluate state-of-the-art experimental platforms, including topological lasers and topolectrical circuits, and address the ongoing debate regarding the fundamental signal-to-noise ratio limits of EP-based sensors. Finally, we identify key challenges and outline future research directions, particularly in non-Abelian braiding and interacting non-Hermitian systems.

---

## 1. Introduction

For much of the 20th century, quantum mechanics and solid-state physics were built upon the axiom of Hermiticity. The Hamiltonian operator $\hat{H}$, representing the total energy of a closed system, was required to be Hermitian ($\hat{H} = \hat{H}^\dagger$) to guarantee real eigenvalues and unitary time evolution [cite: 1, 2]. However, this framework is an idealization; realistic systems are inevitably coupled to their environments, exchanging energy and particles. Such open systems are effectively described by non-Hermitian Hamiltonians, where eigenvalues become complex, representing decay (loss) or amplification (gain) [cite: 2, 3].

In parallel, the discovery of the Quantum Hall Effect and Topological Insulators (TIs) revolutionized our understanding of phases of matter, classifying materials not by symmetry breaking but by global topological invariants (e.g., Chern numbers) [cite: 4, 5]. The intersection of these two fields—**Non-Hermitian Topological Physics**—has revealed that non-Hermiticity is not merely a perturbation that destroys topological order, but a fundamental modifier that enriches it [cite: 6, 7].

The motivation for this field is twofold. Theoretically, non-Hermitian systems defy the conventional bulk-boundary correspondence (BBC), leading to novel phenomena like the Non-Hermitian Skin Effect (NHSE), where bulk eigenstates localize macroscopically at boundaries [cite: 8, 9]. Experimentally, the ability to engineer gain and loss in classical wave systems (photonics, acoustics, electric circuits) has enabled the realization of devices with unprecedented functionalities, such as topological insulator lasers that combine robustness with high slope efficiency [cite: 10, 11].

This paper reviews the current state of non-Hermitian topological phenomena. We begin by defining key concepts, followed by a historical overview. We then discuss theoretical methods, experimental applications, and the critical challenges facing the field.

---

## 2. Key Concepts and Definitions

Non-Hermitian topology introduces mathematical structures absent in Hermitian counterparts. The complex nature of the spectrum requires a redefinition of energy gaps and topological invariants.

### 2.1 Exceptional Points (EPs)
In Hermitian systems, degeneracies (Diabolic Points) occur when eigenvalues cross, but eigenvectors remain orthogonal. In non-Hermitian systems, eigenvalues and eigenvectors can coalesce simultaneously at spectral singularities known as Exceptional Points (EPs) [cite: 1, 2].
*   **Topology:** EPs are branch points on the complex energy Riemann surface. Encircling an EP of order $n$ results in the permutation of eigenstates and a geometric phase accumulation, often exhibiting a $\epsilon^{1/n}$ spectral response to perturbations $\epsilon$ [cite: 1, 2].
*   **Significance:** This enhanced sensitivity is the basis for proposed EP sensors, although the implications for signal-to-noise ratio (SNR) remain debated [cite: 12, 13].

### 2.2 Complex Energy Gaps: Point vs. Line Gaps
A defining feature of non-Hermitian topology is the classification of band gaps. Since eigenvalues $E$ lie in the complex plane $\mathbb{C}$, the definition of a "gap" bifurcates [cite: 14, 15, 16]:
1.  **Line Gap:** The spectrum does not cross a reference line in the complex plane. Systems with line gaps can often be adiabatically deformed to Hermitian or anti-Hermitian limits, inheriting conventional topological classifications (extrinsic topology) [cite: 14, 17].
2.  **Point Gap:** The spectrum does not cross a specific reference point $E_{ref}$ (usually $E=0$). This allows for a non-trivial winding number of the complex spectrum around $E_{ref}$, a phenomenon with no Hermitian analog (intrinsic topology) [cite: 14, 16]. Point gap topology is intimately linked to the NHSE [cite: 18].

### 2.3 The Non-Hermitian Skin Effect (NHSE)
The NHSE describes the extreme sensitivity of the spectrum to boundary conditions. In systems exhibiting NHSE:
*   **Periodic Boundary Conditions (PBC):** The spectrum forms loops in the complex plane with non-zero winding numbers.
*   **Open Boundary Conditions (OBC):** The spectrum collapses into lines or arcs within the PBC loops, and an extensive number of bulk eigenstates ($O(L)$) become exponentially localized at the boundaries [cite: 3, 8, 9].
This breakdown of Bloch's theorem necessitates the **Generalized Brillouin Zone (GBZ)** formalism for accurate topological characterization [cite: 19, 20].

---

## 3. Historical Development and Milestones

The field has evolved through several distinct phases, moving from mathematical curiosity to experimental realization.

### 3.1 The Hatano-Nelson Model (1996)
Hatano and Nelson introduced a lattice model with asymmetric hopping to describe the pinning of magnetic flux lines in superconductors. They observed that under OBC, eigenvalues became real, while under PBC, they were complex. This was an early precursor to the NHSE and point-gap topology [cite: 5, 16].

### 3.2 $\mathcal{PT}$ Symmetry (1998)
Bender and Boettcher demonstrated that non-Hermitian Hamiltonians respecting Parity-Time ($\mathcal{PT}$) symmetry could possess entirely real spectra [cite: 2, 21]. This triggered a wave of research into "balanced gain and loss" systems, particularly in optics, where $\mathcal{PT}$ symmetry breaking leads to spontaneous symmetry breaking transitions at EPs [cite: 1, 22].

### 3.3 Topological Photonics and Lasers (2018)
A major milestone was the theoretical proposal and subsequent experimental realization of the **Topological Insulator Laser** by Harari, Bandres, Segev, and Christodoulides [cite: 11, 23, 24]. They demonstrated that topological edge states could support single-mode lasing with high efficiency, robust against disorder, bridging the gap between topological physics and active device engineering.

### 3.4 Symmetry Classification and Unification (2018-2019)
While the Altland-Zirnbauer (AZ) classification governs Hermitian topological phases (10 classes), non-Hermiticity complicates this picture. In 2018-2019, seminal works by Kawabata et al. and Gong et al. established a complete classification of non-Hermitian topological phases [cite: 25, 26]. By accounting for sublattice symmetry, pseudo-Hermiticity, and the distinction between transposition and complex conjugation, they identified **38 symmetry classes** for non-Hermitian systems [cite: 26, 27, 28].

---

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Non-Bloch Band Theory
Standard Bloch band theory fails for non-Hermitian systems under OBC due to the NHSE. The state-of-the-art method is **Non-Bloch Band Theory**, which replaces the real Bloch wavevector $k$ with a complex one, $k \to k + i\kappa(k)$. The locus of allowed complex wavevectors forms the Generalized Brillouin Zone (GBZ) [cite: 19, 29].
*   **Technique:** The GBZ is determined by the condition that the characteristic equation $\det[H(\beta) - E] = 0$ (where $\beta = e^{ik}$) has roots satisfying $|\beta_M| = |\beta_{M+1}|$ for a specific ordering of roots. This restores the bulk-boundary correspondence (BBC) [cite: 20, 30].

### 4.2 Topological Invariants in Non-Hermitian Systems
*   **Spectral Winding Number:** For point-gapped systems in 1D, the winding of the complex energy spectrum serves as a topological invariant predicting the NHSE [cite: 14, 16].
*   **Biorthogonal Polarization:** To account for non-orthogonal eigenstates, topological invariants like the Berry phase are generalized using the biorthogonal basis (left and right eigenvectors) [cite: 6, 31].

### 4.3 Experimental Platforms
*   **Topolectrical Circuits:** These are among the most versatile platforms. By using operational amplifiers and capacitors, researchers can engineer arbitrary non-reciprocal hoppings (violating Newton's third law) to realize NHSE, 4D topology, and non-Abelian braiding [cite: 32, 33, 34, 35].
*   **Photonics:** Coupled waveguides and ring resonators with controlled gain (pumping) and loss (absorption/radiation) allow for the observation of EPs and topological lasing [cite: 1, 36].
*   **Acoustics:** Active acoustic metamaterials use microphones and speakers with feedback loops to simulate non-Hermitian Hamiltonians [cite: 37].

---

## 5. Applications and Case Studies

### 5.1 Topological Insulator Lasers
Conventional semiconductor lasers suffer from multimode instability and sensitivity to defects. Topological insulator lasers utilize the robustness of topological edge modes to enforce single-mode operation.
*   **Case Study:** Bandres et al. (Science, 2018) utilized a 2D array of coupled ring resonators acting as a photonic topological insulator. By pumping the perimeter, they achieved single-mode lasing with a slope efficiency significantly higher than trivial counterparts [cite: 24, 38]. Recent advances include electrically pumped variants and vertical-cavity surface-emitting laser (VCSEL) arrays [cite: 22, 39].

### 5.2 Exceptional Point Sensors
The spectral splitting $\Delta \omega$ near a generic degeneracy scales linearly with perturbation $\epsilon$. Near an EP of order $n$, it scales as $\epsilon^{1/n}$ (e.g., $\sqrt{\epsilon}$ for $n=2$). This "infinite" susceptibility at $\epsilon \to 0$ suggests ultra-high sensitivity.
*   **Implementations:** Microtoroid cavities, nanoparticle detection, and gyroscopes have demonstrated EP-enhanced frequency splitting [cite: 40, 41, 42].
*   **Critical Analysis:** While sensitivity (signal shift) is enhanced, recent studies indicate that eigenbasis collapse at the EP amplifies noise, potentially negating the Signal-to-Noise Ratio (SNR) benefit (see Section 6) [cite: 12, 43].

### 5.3 Topolectrical Circuit Simulations
Circuits have realized the **Non-Hermitian Haldane Model** and **Higher-Order Skin Effects**.
*   **Case Study:** A 2023 study demonstrated "skin interface states" in circuits, where domain walls between regions of different winding numbers localized voltage modes, confirming theoretical predictions of non-Hermitian domain wall physics [cite: 33, 44]. Another recent breakthrough involved the realization of non-Abelian permutations of eigenstates by encircling exceptional arcs in a 3-state system [cite: 45].

---

## 6. Challenges and Open Problems

### 6.1 The Sensitivity-Noise Debate
A major controversy in the field is whether EP sensors offer a fundamental advantage.
*   **The Problem:** While the signal scales as $\sqrt{\epsilon}$, the non-orthogonality of eigenstates at the EP (measured by the Petermann factor) leads to an amplification of quantum and thermal noise [cite: 12, 46].
*   **Current Consensus:** Theoretical and experimental works by Lau, Clerk, and others suggest that for fundamental noise sources (quantum shot noise), the SNR is *not* enhanced compared to diabolic points [cite: 12, 47]. However, EP sensors may still offer advantages in regimes dominated by technical noise or readout limitations [cite: 46, 48].

### 6.2 Instability in Active Systems
In systems with gain (e.g., lasers, active circuits), the NHSE can lead to an accumulation of energy at boundaries, potentially triggering instabilities or nonlinear saturation effects that deviate from linear topological predictions [cite: 49, 50]. Understanding the interplay between non-Hermitian topology and nonlinearity is a critical open problem [cite: 50].

### 6.3 Intrinsic vs. Extrinsic Topology
Distinguishing "intrinsic" non-Hermitian phases (those with no Hermitian analog, protected by point gaps) from "extrinsic" phases (deformable to Hermitian systems) remains subtle, especially in high-dimensional symmetry classes. Recent work has attempted to formalize this via homomorphisms from line-gap to point-gap classifications [cite: 14].

---

## 7. Future Research Directions

### 7.1 Non-Abelian Non-Hermitian Topology
Unlike Hermitian systems, where band gaps are simple voids, non-Hermitian bands can braid around each other in complex ways.
*   **Direction:** Research is moving toward manipulating multiple EPs and "Exceptional Lines" to realize non-Abelian braiding operations. This could lead to new forms of topological information processing where the state of the system depends on the non-commutative order of control parameter variations [cite: 37, 45, 51].

### 7.2 Many-Body Non-Hermitian Physics
Most current work focuses on single-particle or mean-field descriptions. Extending non-Hermitian topology to interacting many-body quantum systems (e.g., via the non-Hermitian Hubbard model) is a frontier. This includes studying the fate of the NHSE in the presence of interactions and the emergence of non-Hermitian topological order in highly entangled states [cite: 29, 52].

### 7.3 Generalized Non-Hermitian Skin Effects
Recent theoretical proposals suggest "relative skin effects" and skin effects that defy the current GBZ framework, driven by real-space non-Hermitian terms or critical behaviors. Exploring these generalized localization phenomena will refine the non-Bloch band theory [cite: 53].

---

## 8. Conclusion

Non-Hermitian topological phenomena represent a paradigm shift in our understanding of open quantum and classical wave systems. By embracing non-Hermiticity, researchers have uncovered a rich landscape of physics defined by exceptional points, complex energy windings, and the macroscopic localization of bulk states (NHSE). The field has rapidly matured from abstract mathematical classifications to concrete applications in robust lasing and versatile circuit simulations.

However, significant hurdles remain. The practical utility of EP sensors hinges on resolving the SNR debate, and the extension of these concepts to the quantum many-body regime is in its infancy. As the community addresses these challenges, the interplay between topology, symmetry, and dissipation promises to yield next-generation technologies and deeper insights into the nature of open systems.

---

## References

[cite: 1] **M.-A. Miri and A. Alù**, "Exceptional points in optics and photonics," *Science*, vol. 363, no. 6422, eaar7709, 2019. [cite: 1]
[cite: 54] **J. Wiersig**, "Review of exceptional point-based sensors," *Photonics Research*, vol. 8, no. 9, pp. 1457-1467, 2020. [cite: 2, 40]
[cite: 40] **N. Wu et al.**, "Recent Advances of Exceptional Points (EP)-Based Sensing Applications: A Review," *IEEE Sensors Reviews*, vol. 2, pp. 292-303, 2025. [cite: 41, 55]
[cite: 41] **S. Liu et al.**, "Realization of a non-Hermitian Haldane model in circuits," *Frontiers of Physics*, vol. 20, 044204, 2025. [cite: 32, 56]
[cite: 2] **E. J. Bergholtz, J. C. Budich, and F. K. Kunst**, "Exceptional topology of non-Hermitian systems," *Reviews of Modern Physics*, vol. 93, 015005, 2021. [cite: 52, 57]
[cite: 32] **Q. Zhang et al.**, "Experimental realization of non-Abelian permutations in a three-state non-Hermitian system," *National Science Review*, vol. 9, no. 11, nwac010, 2022. [cite: 45]
[cite: 52] **A. Banerjee et al.**, "Non-Hermitian Topological Phases: Principles and Prospects," *Journal of Physics: Condensed Matter*, vol. 35, 333001, 2023. [cite: 6, 7]
[cite: 45] **X. Zhang et al.**, "A review on non-Hermitian skin effect," *Advances in Physics: X*, vol. 7, no. 1, 2109431, 2022. [cite: 3, 8, 9]
[cite: 6] **F. Schindler**, "Hermitian Bulk – Non-Hermitian Boundary Correspondence," *PRX Quantum*, vol. 4, 030315, 2023. [cite: 17]
[cite: 8] **N. Okuma and M. Sato**, "Non-Hermitian Topological Phenomena: A Review," *Annual Review of Condensed Matter Physics*, vol. 14, pp. 83-107, 2023. [cite: 4, 5, 58, 59, 60]
[cite: 9] **K. Kawabata et al.**, "Symmetry and Topology in Non-Hermitian Physics," *Physical Review X*, vol. 9, 041015, 2019. [cite: 14, 16, 18, 25, 26, 28]
[cite: 3] **S. Guo et al.**, "Experimental observation of non-Hermitian higher-order skin interface states in topological electric circuits," *arXiv preprint arXiv:2306.13454*, 2023. [cite: 33, 44, 61]
[cite: 62] **H.-K. Lau and A. A. Clerk**, "Exceptional-Point Sensors Offer No Fundamental Signal-to-Noise Ratio Enhancement," *Physical Review Letters*, vol. 132, 243601, 2024. [cite: 12, 43, 46, 47]
[cite: 57] **G. Harari et al.**, "Topological insulator laser: Theory," *Science*, vol. 359, eaar4003, 2018. [cite: 11, 23]
[cite: 7] **M. A. Bandres et al.**, "Topological insulator laser: Experiments," *Science*, vol. 359, eaar4005, 2018. [cite: 10, 24, 38]
[cite: 4] **K. Yokomizo and S. Murakami**, "Non-Bloch Band Theory of Non-Hermitian Systems," *Physical Review Letters*, vol. 123, 066404, 2019. [cite: 19, 20]
[cite: 5] **H. Hu et al.**, "Exceptional Non-Abelian Topology in Multiband Non-Hermitian Systems," *Physical Review Letters*, vol. 130, 157201, 2023. [cite: 37, 51]
[cite: 58] **R. Li et al.**, "Observation of impurity-induced scale-free localization in a disordered non-Hermitian electrical circuit," *Frontiers of Physics*, vol. 19, 43209, 2024. [cite: 63]
[cite: 59] **K. Kawabata et al.**, "Intrinsic and extrinsic non-Hermitian topological phases," *arXiv preprint arXiv:2509.06879*, 2025. [cite: 14, 64]
[cite: 65] **R. Rafi-Ul-Islam et al.**, "Topolectrical circuits: Recent experimental progress," *Applied Physics Reviews*, vol. 12, 021503, 2025. [cite: 34, 35]

**Sources:**
1. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsxjV4oZ5el73KOX_WGTuCSMMx3M3ZUoLjV8i4nGSWmjbRmP8UqvmDpYthMtpNEeUVEdBXusUHBUDcL2M_b_O4G8r3iSTBSnAfdj_zKN_Yc5BLy3zkD0n31cGgCXUiEnsQ_fzk25hYlIYoN7fx2B1i_mWgsUFPvJFsb5kf16YWWs8oY9RHQLE0ZLVOdfjJWrqALskpzcoOCGDRSg==)
2. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENZS-cES_dhwsYqzwPmuOa_7Vwh3KZpTAyKuuCilLNXHGDmbdshAjaMAOReJ0F1A0Ia3H5nY3WxE6ciHpP3oTiTO90TzUXqaH_dfwv6wfXRSTz1tduoAEYNvqHh5q2zs6sw_cFODC11QAe_DfGjw==)
3. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeUansvqyLpNr7VxcEXsNLoVw0RN93RmyxySvllOfiOcor--yQ2XEBS4yOcJaibTnlIsWYWC6choGbeTndX7-pU2SEQyqPvRvk-z4ZE5vWk5Ntx0iAXI1x-5qkBcRmTeixRrb3boqJinKw8jqPx7l2nvg5ZMBI-yY=)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmURYoCnilpediCzdE1PStVkaN-3XfvdOGpRhd2k2KpRCqGHHyV_E5iDztuzCcPGvxmXTLltCETj2dRsSw-Q0-Nz0kB0L5ESxzRNovUcK6EaUj72Tz1Q==)
5. [annualreviews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpOFx2Jww6vgTgdo7nZJERqKxR0g9saNBNgFjqUzJkRG7WeBgxvF3hWfXcJ2B2CbpR89jrd3f6Kb0h2jWl7JotLRvWkikNmkb9uWWOYTPKh9yMgnc6e1_YQGG3yrSMDjCC5oPS6HKCN65OrO1hz_V29W91vC2pbr0sEM437_NWsT0YUdjwrVHKTutAtwc=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEe3Qtnr1piewOdyB58yd4-1jafmcOGbIuZfTMdyLUvWMUdTw3OTYj2QHBLnUImdqvXh4fI6sBbncK6aIkYdbhgpfNKc3QMJceObhzHO91Bm6HyR8F7rPabYGzeWX9l-pejiLcXGolbj4uym_Lx5XsoAWy8EizDxqpytkgw_KJyPjjPXXjaFcS78uANKLHz9_ipkXx1AMTduvgTxTvB7U8f3c=)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcu_2pRHlaLAwUFXRBWDdQwWSD-h1Anyqf_5atirfazhNu5EOxG7XKmlJiwJi8WJ6V-cZzWcLP2g5gGFygJHqQmgj5V9f88Odud6Nf6UUREgz_vmcjeg==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeOybQ2KLqitk7FEK4AdTLCjMHOI9VpXok6ZN_Xf8_Pbdp_ny1je_dHSY1qG0ZzplyVJILK4YdrpKdxaI2PitfLi6MduajElcxGWYzTCWKwL3GYztXsg==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTqNNL0cn_PU43jqSX5fF6C5gqi3o6trlPFMr5VhsruEgqWCnwu21ixG_LIEKNj0qGI8tyFfnJsxgBPDW6QdU1FXm_3YReNk-oGvsBcBiI1E_Q1zqs3XMP24C-2lw0CQ3o668nhQOGczquuecWRzY14rX6zb5tYc3q55f4O_j5lUyQ0N0RpRHvCS0hffQG)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6XWsygWgPJaaP-ES46s0SAARRxjUe_9Xds1mV-J39cijwzmE0hV8I5UC7m_LLGAub8nNTQSWlTx3mciVYcI-FMkjUuau0DogAir51t9Av-dCaRj9J_8nnSwt4e3r0t21G5L_8k3zrHJh4i3pbCB2uNadG3RS5aGF4lQ_FCqAPiPTlacFySr3bCMcDximpWhs=)
11. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDNbFVeyzn_r8uCEs-VZ1szUyWzf-s8_ZitbRAWTJyJRkcNqo3jWUka4tCDje_G3fpu4TVMWqlvTWHJcshxbn6oTgrR2Uy6a2is3R96d3dRvjdNXSR7SVw8F93gU28b_y27F1wOPL7zGCK-44dh3iXhc-3XFOlCenoO-o8WQ8xjam7rxa0yODToEQFrKUI_uPCkC1AsVoJbMfBpTlhVFwFNXWWu7h9X44p8akTz3b0UWJhM9iWRHPniR0=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHNFq-e3NrLWTz7e1sWvYylMdCY_mP-MOofKV1dHQG6iBCjdk2c6ZtfhZHeSA_4pgGwfmnTZaQE0ugzT9aylWCzvzOmxwGfGMMD6DKntKRlyWx_a8_KdmG-PnsuZgUmq5aMdk0VFzgSfCp7gLfXAdX5a2aYRlXkpPE2ZBI14HshvZkqVSxhOafbLevcNberc7u7KXKysLya9wpubVb8-rYruyyYiCOTcDn8ZeQ-KwNyat8Hpq5alMyshA=)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs3YSFMXcMgHILEa8CStOoTOatuX6J4iZKl8_wyVRxosnkUkICNtwvAJEB3PZ8PBffpAiJBOFX2AKukmPjYEpD91A0tJaW42g6hMn6Xemny6p-uvabkHAiLuIhixEFng==)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8W8ukV82PsUU_VQUJvcagRSAdD7TscwAXFS52fBk2-UAWLIj_g5MRhqnN0ci-sjk-Z2xnvSFxdPw3ZUBxjWjP6gdKMjCDDx0WZZaf5Ixe33ktqBYvAA==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa1KcbvRhKP19l20W8cE797Q1iCZ7kWRSfdSVeqeTY5cXeyraFbA43RWwkxHcv_uWIcjbNu9NpS6BO0aqcl8D7xVuk0Lsm7KDZoN5B58wxL3V6EwNZ_F7yLA0oyxIrUdGolAz6OMYJt7aMVQHTvxlrTWDTIyCfUgDwjSdyFtzdX3Vd3usrhFh3ow6myqZ5F4KDwZyjSbyKaahvSsREynm4Sc32FDVULTHFz_a6RXWWj7J1P7rH1DhKJpjER_U3bQ==)
16. [kyoto-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYmdZW-MGULmerFirEVhGlVqAQZhHkHhHZf5ritODl2wdpudovqi_mWonN9PKIvjWoDAw8FLV0w5OkXlqjKT9WvdNkskqPYF6J893UHibGeJXiPw4m7pwOIPm0thS0JVhb7GmQCrMNGAlmz2oVbsC08HYs5KE2lgQF0ZRbg-QDD0WeHD2eog==)
17. [imperial.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr3XqW4j5fl6uFqCQQ9dxVqzB9mogrMZ5k90ZLQBpUR90nVnlkh-oxji92qt7fAWRc5deritF8FKgqqaWwHoGkOQtX9LDeh2fl-F-V9Y5XaXxihrnSIY2LqB3LLJRLHgT0pIzTXNwp_u0N3FNyMCksf8SkClYQgRopPmn_Tvq3nfJ8qK0nwMWSLMvJjuqpSRytLr_gi3cqbsKN6g==)
18. [u-tokyo.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Auk170X7N-uIAMZ7J6_ezSf7BpE9FTqN4zxgkJ54JW6scFdxqD_wyO6cjP3uz-I4iyPFpmOvOUO5qaj9NtHYcNXGjEHlqWkL3_WGn_ut8lkeuDnfBYzB46AGIv6WzuM5XcAUtTkSUsD4x8ZeQfYAGw==)
19. [iphy.ac.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVb9diEvX1ik3-AgL33XxED4-xklnBaDj9nCoReoGsKa3weMXduS8wDnENYzg9pDTEvJ8BYqQTF2R74tZTsscMX5Kj9tykjRivQGUVf9xJb8yjouLzryqeUukL0FEft7RoMrsMTiR-jHxOmv1_c8yyjm4QDcwn)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERnVezJLO8ueyJUcMy9avjRgRj0j9fRr5uYMMf-z2J6Kc07oOSPE-tHTqwYK8hGq3-whwPdrKUUAPRsLsK5DUBe-GN3aq24E4NWYG1L8a2GuWPmDOJlx9zi_H5OtPbhR6t3-t8p1C2tOtqdfjpdQXCBPzZ8ln1IT7guG59eO9KdsgUwjJQI7qW1L1UgiHntq4owOX7czWXDuXqRyFfHzRmUg==)
21. [researching.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpIoBhsEAHnWwe3bYB3mf_LCZ1KilomMEJ7aW38ZWVHZXa5h65X9TWTZzaXi3XvAGtbIW0bDcOlxLc9FFV5pHqsaqN4s-axb0aDPPmZ-h4oXkq7VqdcEnjG5eicz1eT-I1TloHHQ0HG8kbTTk=)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjH1Qxqb5NY1ITu1qvez0kr0_9cq9R7Joe0hRfZvMJN3cIIekJlC5nCprPosP09gZmsjXBi6HxFWu4ZcmN6uAc9aWX1TG7QdBnFCImxGeOXT_911XUA1a5bH5h1qDK8yCOJoH9YAh4Z8uXAp7CEug3xHBt-FU9Wt6_GTJfWvUc7aY3xAFEjkq7m6HagQBaCHfExYa5rVn3e6po3BDcH8AUJ2yhX-ykRIGHfqh-9xUQ)
23. [semi.ac.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPkUhjFwaa7vpJ7JN4aEU-4DsBe9gy1t0TFOC-zY77nOnH1_6JBrPBogL57sCMRlaarTC8sNHZDiM4_tHGdTTUF6psnAM-z-f5E5GJj5qvmd3v-D1Efji6dzPqmmjh0HFo74GL_8b4rFGw--HixWYoi2tC_a-3oA==)
24. [technion.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqcpX8THZwxDPM8rVZzlLj8Gux6sdB8g0MGdcOkv-qh08BwMINEWyUhXvHBtPLiJaifnhTN6VSCQ9QO4-eo0GSjVQWT5_XqucekBV4glijQdefg7tR3sjBlI3tj0XwE3VM3jNpdIN5njkZjv3tKCIl2A-E-__CTogVg-D44Gf2uKManJ71cwosMTI=)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyc0vLDPnuU-UaPXbxMW4MG34xRdIzAQpEajsL8jl_S1systJWnnatKgCMXbIr3LHeeVA0ib4sYJAp3_vsKJE_8ocu_O47sRhm0uMcppZXsS2L5By-HA==)
26. [kyoto-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ0fjx4wwwsQV4bilN87kJ_rkSB-SFAhxEWSeHGFf-Wwyada4uxnQ91kBX--fwRAuLJGnXjmQiBdQDPVUZQKPavEkZDdELIGpH6-Cr1MbxOo7c5nJU6NulM8fLlkTj1kfHNCJGO3u6xy9PQjiSdAgldh3elx7M9WNZYq3BGYfeU6n82VpcSVbAZo9cJm4TpxX8)
27. [kyoto-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8hHpSqOAAFRSTmgsUMGKzpfUDz6Md0URuQe9_Iux24jhonXPPHqNsKFtwGxueqixP_yQ2lbExC-giVzHUg1-Shdf2mG_6axJDFHNYhyp0eZRbyeCky1mMdCZkGEx7Dv07hT9vzbfmooKZb7Jz96sSGb6a6gFyOfjAsyhjY2wplgYgUKLroC80lrWmc6_4RspX5w==)
28. [kyoto-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHryIxJvO7b2DxeqbKZqrzpuik32nLfCu1XYZi743jJqcgYiU7w-XWkUKf6Nz1zMJIwdwxj3W9aZYqJW6pBj1aHx8GtXSVC-sOKExxR3oOvuke0Cq0qbekd_qlsPB7o29E2ZAXzWSfJm5MqrfDv2RqDQWaixr_ze3im3O9MaaE_MtFvHoGFTfLKIOA=)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC4s-4oCISvC9abKojwudZncvLlujhlnCc8tpHlxQYDTY7CbXj5aknBiTxKYHQV9TW_oFQfs-uZR3daRd4jthMqUQ2fJ6EvzOLPPXjXvYpj1mwkZL72If0LLeoee0Echc6UUFjSvBZUyhbr-jm1yf_CMD77bSCI-9S7xLScOq8Y0q93YgjalGc9VEMPtk9)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZGegHmQ5w1zO1fPSxQGEZYxvrxolUA8cW5kNtJ-lRLyFO_zv-oyUX9nJLDuVrUADTTjOFTzsA5J_j60WhzibfrIrm2PoFwK9wj3Fm_uXa8_Ki9if3ze2DtNsBjZjfFS1cxxySEe0w)
31. [nju.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7INzpZN95ezL8mVOheVs7XTvHt-14gihSRzJHVkeowY7zsSU47-X1gOFgLKgaCwG4hKRVR4RNiw_XFu68GvIl2-_QcFaaip-DgZmU3TX55MP_21w3zBeL5iUCLqOjh9wnW2PV_V3-OHYiJYzrxjokdIZaPQUDzo0f-QslG1X45fFuN_WN4NHBjYYkuF-Q_Wi-4fJGbnu4r-C8fNmchYr7pYg3rwSjbR9DX4yWFiAZ7PNAfrtKeMRXzgg0phKQy18L6pq8CxOItAUPzw==)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWWvVO2XOT8FKtA4iT7gUTi4_CSaugdfMMEI5Jwq7eA2GBhFuPXfuHeWKpt4_n8xueuGzDDKmFBTdBw4-THlS9fgi23QOhq7JzbEDg2W4rPwVa4HQdgg==)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLKaDlT2xof5nS6TFnG_dRahJubcE3ve1UtL2ESbWBQqEJ9kSOrTIYXgPDLjPZH4Y8nJWrsic6zvByFODab229z9Iujny2UlldVLZJEtCJHfNz9JSqp6h5o9shwek7RA4Lx5kAZgWL4JVNdkXW4W5EUT_8rvlpowPrNbGy3Dp_mIyGddU8PNQntnOp80RiLZDkIlh7G0TB_ReOYhlaVmZajWwbi3DyUVkkIRedoxC3s4OpOu6Uu6Dcoqy5xjgPrnDsGqCpVcwp5J49jbwITiOA705M1IIuyQ==)
34. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9rzdU36AMkHOm1Z3b53Sq4OQWLhvRy03-NceSxPsdrksKKU6rwiHvCV0IljDpw4M_-0xZF7I4enWD1CXRN05lIxR4VWOJcHaP706NBFcbL3aLgyTJOO75JofLfpe9W_iXTY5nbHAp1SJLNHCtC9MNaqntlbd9KfV5hMevGJfVwzrbK4gow_1X581eraA7Xkl1c3k2ncaYiw==)
35. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5EEuSKElx3UfOqimcdFipAqu7GqdP8_veJp1PkaJgBnwE5hArPaJPbU_n8fkFpUrHppRjpcyFDyi5og-TILnx-WjGgJBBiPh2icwKcjQDAcAUn2GAAQzvLA==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGErbpIjOBaYFBTM3ulzvnDovhZaoe2AI60G8sMFh-DQSOKptuGcpV_v0ftjdQ00MaG_5yeAGLqlzM2df8F3RzohNEPX_PfNMntD9nhbAGBv_nCfR_Wzqtunb7gy4O7VbLu1tBdTAdzKtboz56Yp5jwqrljkDhklaXkIY7u6MtCbbYSyubchPsBjfZEQ==)
37. [cas.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtzxQFREKGNUyaldkums1fFDPIRbElsqRWnzRipwuo2NKvTqYJc0FILi0H4gQIiQGqbo9vh8z3kZJyE3ZaQ_GMD7H4QOMU_yS5Zlrav8AVQLt6LZGTEwI5VT1CjVyFbxn3PD1elipX-9p3mgXTlWHxqveA9eUcL2w=)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxtQFSyZdD__vGZdJbURSfeq2JljMMgqrbPrkK5vY6ckocD5U9qKF6dl0eumIKkMTVF922yz-HprVSwaau7kTfJ4pYSd4cSJMfJk3W2USm9gtsj-x7WHKW4p5x1P2UWw==)
39. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwppNWJrNk1WZlytbDf-6Lm2X1PgImA-p_jV5u497gsA0S_OwUomU96F0HorT5EEv0lsCt3i9md01yj9ukSst9i7dwfGx8wUDl5Uj3waSDEd6qYRSBiqU5PZYxVIkeJBWuwQbUcwywqPl4)
40. [researching.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxjYC0RBg8O7DnOj_yP9Z38YVgpMw8-ZAqD3qhmrxODRaA9kNOlLH5wuu0PLqenIDehZbuLDmMZrdjVX1aPyUD4Y51reTOdmVWd3_MBmSYLpRAcFDnfN-MD3L0vzXgR0TOjFH9gyvCxIIHU9A=)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvBa1yPK_NpqNoMCsDkynvLE-KmsZUidW4MYWEzKueEkLGW2ltQz38OOGuCqg5gkcCpcRJDlhFhTcavWqbo-OqX79RgCkgH_sHTFbbamYaa-IFJr0Em66i9JCODLsMTzB-8xE1sdjfyvs8yolaKu0y4fizlxy7DcYh37KR33z8Lve3wGtDYcIwlBBROrVqxHPbxvz6q4CvkeJnMFoXTtaehO4j06v1SfQmkCH4o3UeHUnjOYek)
42. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyGDcja8q9DxtDJKfVv_Pu1NTzyhsW5GELmh9QKoAWhZOWTuvQD4bwSVQtck3ZF2DqQhbyZGk0GuwG4OpEHl4OsF1eSJkiyznxkOHlLyM3-Nzgfmg7ZKwy0GBEXMFCdeZ6NEfWEBX3qdqkWodsFdbn-GT5FkE=)
43. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElpOWcG9vEXRTunpmc_G5DbhBTp51SALGuybqFSWKOLr7tQ5LwCVltbICuhFAfFL-YT2mvJNOy1cyiiIEoH9cRpRNdligcFbGsUUktM3FGfFvZKUWHwYgLSsB4EfdOsDd5-ur6aPOlpcawkQ==)
44. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXi33UneF1h1rbaqt_-qTH8rOba2RgvEdlvpQKQG6ClEOBuE00MvOKcS2Fz8wlztV52KgYSsH7PiTLws1Z4a0GWoB7VMiE1Phl8onysSVePl2RRhPYHXuV4NBle66LhYFbvkEL)
45. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLrnVbB5wlZ5mft1H_nfqoL4WY___w9Y00yL12HiKV5A426GwkUg0KZuN_6EybgcJbe8c5XDhLT5wrx7cdRew91o9bb2Qq1JEQtJeAISDhpKxJNbJGwdyhP5NwBGnBYwT0bw66hykwFcYztP5P4Gw=)
46. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe5_9CqmFymp4KCElNxcOQs3t0ncx2QrtoXtWtyHdWpMXvp20TNCsQxhhkyzXCNObFAmNd6nY7Wir6I-zgWcG6xpIAj-HxKGfUkd-zDOvQ-6pZUUXpjA==)
47. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLsIB60XIvDwdtmi6qmiRImSDFR8_F1BwgPL8qo_l87HilElUfBkq119_mr8QYzaCyPGuQ_q3DL3OrWn0BXFlHVcPw46ChH2AXQ5SqkggftPjODo2482xFk27sRTLbUgpI61fHZeZ6f1T-2wenUj931-v_BqKad_JXT8Ea-OHCWF36tzU9i815h2LNvSGOfEjPF0m4lFRInkjxk5KIwWHGAVAU4lXGkbCY-6fzNbTPyXJUDoE=)
48. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF__fVLdNDdr6LsIWK7p7uOimAYAqytEsd4aLTM26hSCus-U7t5BvX9nJTS238YlxmVPoVtjKoBw2ERt2Oa4TguUvW1UTSEAYhJXsf2-S_ug09b9B99nLgvVKCEwlmu1KBl2OGNwgsjVA==)
49. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFh2WQHQYHRigxPPwhNUzgYJbkrDbldq1P4pwq2raOf2cxPg4FjDz1g85XiMQ8O1YBnsrJwazx10uDwHDVMa00hUaXlj9mOI6G8YgJx1uRpxDLmtRcR4zqPkZWNIY1f-HiLwPpl1Y-b25OyQA=)
50. [opticaopen.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgkfmb1eBiz5kwc_HYRNqkeNIZbbvQkE4KZbEmOvExGJwGacgIi05AYBsSsvrUQF_YZEfla70Odm-iyhzmpEaVITP2b3o6yJk2HYVnw5-JdUA7A1PNCn_YTQgsnMWT24xisyM3NL3-DacgNi5kpUE99OIFEJEECUGDyzPQ3rz8Q73TzgTzVd2XHbmPWao9HU3F076SD4OdmUowiEuPjxiSI86eMhFoBSQ=)
51. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJq80_oFXA9vbWTM0TjMxZ0iOYKShVYWUXYft60cx8XbNiXszWshRt_jpzOk16pLumPlNZ8Drm9zQMmdQkPHF_CX6nlkYWEsjfS8iMyE2AcufxEbzmdA==)
52. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6oYSWdkf8fB1UYNKdO3XRXqYYEh5N7FfWHN4wvGEMrjxJ4AkVQ2XTCQnEifdPRFFpS7WtRYPWWSSoSILATlczxG__Oov1hz0PoCFv4SoKZpAEhu5-I-0BlvKnNsZSkpEBRl0jx7WYeiJYpAZph00QJtFeYINDbNXuTA==)
53. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEAAViQM9wVuwfJMI2xMs-WvnSJ-9uljlZXMbDi_5IaaUNLVpMg3aZ4phJAcwCDCUgx4kJ_T48tBCK8ycRcm8CuyqBAdkOrbLTe5ZeNmrmHtXFnEsRGQ==)
54. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDkNcjZCuGGAdQ5yoPOGASd5MmTtgrmYq2i97OjUMyFD8vfZ0jttffCyMqLWoYzqCw_Dj0yS75J5KHrdbFyg7a8rMrr_NjCJo7OSnNlivpz90ESGXGSg==)
55. [paiyenchen.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHck1ER3K89c4RiZJNDnbAkWiWl9rk9jvtQ7FCTfX0kBr29iLYWU6vO-FzbDSqDt5hO3ODo7-sMRjYuzi7Gp6NmgDtrR-Ww8sjXkWWuNbew0RdNkoGqiE2gPKoq)
56. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED0UAG3Vh9rEx2KylIPbbQjuR79RPq7_xF9JNefIrU3zRYkbAlQnHmfpWC9-z2Njfc6NtFyPj41TG-ZKITwwKiH8ARlbiSa-JKd9vglhvRJbo-Av6QKqGp5w==)
57. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVID09eSkuzJ0nmsVEJv5GwmKzFtUtTJ1AQWBxYYZ7eZ3hF7KHwdm3b5rDFppvKgcxeS9rXCVOoLRkUPKcsHjfy4q2sgDUyJT5M0hJXa2LWQT3uau3_ShJ03nrG8tx3TMnrDTbEWx50xzsXnA1NIq2BFC3_a4D795B7RpeUKFMlyP1l1mn9SrASZA0YX2yaW4LJUQitaonVQlkN7BAkXa8Omm6kISuQXXwmjq7cp5umooOszYh-yg=)
58. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1AqX1O5nUJLwTZfkAALZ3HBeMWO3Kby7mkPa4aPRapFMJ2-oUJiVn3w0UcWcgN1GXQImkoZmgdoTzP19fqI1E963GYH0JhhRX1yDyHXGQJ-sddvJrSA==)
59. [kyoto-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJfA-ZEFwEGsFrpWl53_dxAhXKez-D2H5KZIBaxFDsBUrR-VMsIlMaO6LRC5apTYD-NCbZM4gAENjNSTGmPftrw2oQoHnj2ydKGMi9xnObkmb2JPiZan-TElChRihI1yArOsQqeeob1J-u-z-ymXf0DXL94RbuD1JbV-CHB12_wzsEBO6xm6AC2Uavy-_x1ivlQrR50KwTMNk=)
60. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHItUhqNaA4bF-NvhZNG3QOp7NrFr1NujQpV2aE1O2Ok5_sC_DauWyu_UDzESx-1-hshg2KyWrXalmvcySJwEEQqQpkTtVqgoou638ycrle5v1iBETOhg70-JEzVokKzmNTa--EM-t3F5PNpSi5S3wijH2HSLWhE-pi-BXDAelSS2BJRInyGTHh)
61. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3znPMQjfJRK9GwdHPbfEuQcPr7RX6KOi5EoufMljf6Fmg2IdKlBRedJz0I-7ER4Ihwgt64niIXhCO0eFa58OB4yLbwBmECrSbWOHyAGOzEhpkEImHiw==)
62. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6Hp0D-w8flQhXcgcoe78PV_jkS4fyNfbFI1XzKcJSAGgM39daj_UgByj2-CbeBR_EIR6t46wAP6aBQWzqAyTSWbjP8O8dPd7jO2tZevePY66dP6hLJv5Cig==)
63. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHawDAo_mbgGFvnfRjqG0ZbqIQW7Tga9ChqA_dUn1_cSLCAlG_144f0uMU0Ye1WyaD1Fzms6797idH_D5j7ID4PJsBgbS5OhWI8qUnTGeFiggec3oPYYY_cIafv71iiebAj-E3TmNZix3m6SzBFhpE6YArKj7_B0KQN3xa6xzOOK1yqBTMkDCgn24TPt_FLqgmAeueq4JQHjiNNzoB1QjQQKd6u5no-wqE2w_sQZ8wx0J3IgnUM0XgH0eq44LxpFkej30Uesy2UxT7-Zk33ZfhsK9o=)
64. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2gYgWK1qQ3WtPWmT5d-RURlLEUVz1YYeO53Q5-lQ8zyMihksTU25__-LhreVpKSrhIzjRmkY0nETdQH8E3dHRfuNc3-rpFptAccXbryw_G2dgmzSMiWEC-zgK-6IaFP3e3zQqqGvOw5cREJBQPVI2fdhtloBNOUSzFq6xFYfckvJlIQQnvHgyLnB3_sO5-tjxT7k=)
65. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFaAZT-C2pj5mVm1vsVj017sqRpvDhKlJv_q1CbYyD2aQZEkoqkgBfcj8d1-a0iogomi3et14gcn3JJ7vI4FgxAR0I4HfADtdDdrvw0VFJvQj8Fi_jphyuH_zQcxesScyHOaOXH89N0Vwi_Ufb-g==)
