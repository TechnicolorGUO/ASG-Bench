# Literature Review: Dipolar physics- a review of experiments with magnetic quantum gases.

*Generated on: 2025-12-26 15:25:18*
*Progress: [13/21]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Dipolar_physics-_a_review_of_experiments_with_magnetic_quant_20251226_152518.md*
---

# Dipolar Physics: A Review of Experiments with Magnetic Quantum Gases

**Abstract**
The realization of quantum degeneracy in gases of highly magnetic atoms has opened a new frontier in many-body quantum physics, characterized by the long-range and anisotropic nature of the dipole-dipole interaction (DDI). This review provides a comprehensive systematic analysis of experimental progress in magnetic quantum gases, tracing the evolution from the first Bose-Einstein condensates (BECs) of chromium to the recent proliferation of lanthanide experiments (dysprosium, erbium, thulium, and europium). We examine the fundamental properties of dipolar gases, including the competition between contact and dipolar interactions, and the stabilization of dense phases via quantum fluctuations. Key milestones are critically analyzed, including the observation of Fermi surface deformation, the realization of extended Bose-Hubbard models, and the discovery of quantum droplets and supersolid states. Special attention is given to the very recent observation of quantized vortices in dipolar supersolids (2024), which provides hydrodynamic evidence of superfluidity in a modulated phase. We conclude by identifying current challenges and outlining future research directions in dipolar mixtures and quantum simulation.

## 1. Introduction

The experimental realization of Bose-Einstein condensation (BEC) in dilute atomic gases in 1995 revolutionized atomic physics, providing a pristine platform for studying macroscopic quantum phenomena. For the first decade, these experiments were dominated by alkali atoms, where the interatomic interaction is isotropic and short-range, effectively described by a contact potential characterized by the s-wave scattering length $a_s$. However, the desire to simulate more complex condensed matter systems and explore exotic quantum phases necessitated the introduction of long-range, anisotropic interactions [cite: 1, 2].

Magnetic quantum gases—comprising atoms with large permanent magnetic dipole moments in their electronic ground state—have emerged as the leading platform for exploring such physics. Unlike alkali atoms, which typically have magnetic moments of $\approx 1 \mu_B$ (Bohr magneton), highly magnetic species such as chromium ($6 \mu_B$), erbium ($7 \mu_B$), and dysprosium ($10 \mu_B$) exhibit significant dipole-dipole interactions (DDI) [cite: 2, 3]. The DDI is fundamentally different from the contact interaction: it is long-range (decaying as $1/r^3$) and anisotropic (depending on the orientation of the dipoles relative to the interatomic separation vector).

This review aims to synthesize the rapid experimental developments in this field. We are motivated by the recent explosion of results, including the stabilization of quantum droplets by beyond-mean-field effects and the long-sought observation of supersolidity—a paradoxical state of matter possessing both crystalline order and superfluid flow [cite: 4, 5]. We further address the expansion of the "dipolar periodic table" to include thulium and europium, and the application of these systems to simulate phenomena ranging from extended Hubbard models to neutron star glitches [cite: 6, 7, 8].

## 2. Key Concepts and Definitions

### 2.1 The Dipole-Dipole Interaction (DDI)
The interaction potential between two magnetic dipoles aligned by an external field along the $z$-axis is given by:
\[
V_{dd}(\mathbf{r}) = \frac{\mu_0 \mu^2}{4\pi} \frac{1-3\cos^2\theta}{r^3}
\]
where $\mu_0$ is the vacuum permeability, $\mu$ is the magnetic moment, $r$ is the interparticle distance, and $\theta$ is the angle between the vector $\mathbf{r}$ and the polarization direction $z$ [cite: 2, 9]. This interaction is repulsive for particles side-by-side ($\theta = \pi/2$) and attractive for particles in a head-to-tail configuration ($\theta = 0$).

### 2.2 The Dipolar Length and Interaction Parameter
The strength of the dipolar interaction relative to the contact interaction is often quantified by the dimensionless parameter $\epsilon_{dd}$:
\[
\epsilon_{dd} = \frac{a_{dd}}{a_s} \quad \text{with} \quad a_{dd} = \frac{\mu_0 \mu^2 m}{12\pi \hbar^2}
\]
where $a_{dd}$ is the dipolar length and $m$ is the atomic mass. When $\epsilon_{dd} > 1$, the dipolar interaction dominates, leading to phenomena such as d-wave collapse in BECs [cite: 2, 10]. For highly magnetic atoms like $^{164}$Dy, $a_{dd}$ is approximately $130\,a_0$ (Bohr radii), whereas for alkali atoms it is negligible ($< 1\,a_0$) [cite: 2].

### 2.3 Beyond-Mean-Field Effects (LHY Correction)
In standard dilute gases, the Gross-Pitaevskii equation (GPE) adequately describes the system. However, in strongly dipolar gases, the competition between the mean-field attraction (from DDI) and repulsion (from contact interaction) can lead to a regime where quantum fluctuations become significant. These fluctuations provide a repulsive energy correction, known as the Lee-Huang-Yang (LHY) correction, which scales as density $n^{3/2}$ (or higher orders in dipolar systems). This correction prevents the collapse of the gas, stabilizing high-density "quantum droplets" [cite: 3, 9].

## 3. Historical Development and Milestones

### 3.1 The Chromium Era (2005–2010)
The field of magnetic quantum gases began with the condensation of $^{52}$Cr by the Pfau group in Stuttgart (2005) [cite: 1, 2]. Chromium, with $\mu = 6 \mu_B$, was the first species where DDI effects were observable, although $\epsilon_{dd}$ was initially small ($\approx 0.16$). By using Feshbach resonances to tune the scattering length $a_s$ to zero, researchers achieved a purely dipolar regime, observing the anisotropic d-wave collapse of the condensate, a hallmark of the DDI's symmetry [cite: 10].

### 3.2 The Lanthanide Revolution (2011–Present)
The field accelerated with the introduction of lanthanides, specifically dysprosium (Dy) and erbium (Er), which possess larger magnetic moments and larger masses.
*   **Dysprosium:** Condensation was achieved by the Lev group (Stanford) in 2011. Dy ($10 \mu_B$) exhibits strong dipolar physics even without Feshbach tuning [cite: 1, 2].
*   **Erbium:** The Ferlaino group (Innsbruck) achieved Er ($7 \mu_B$) condensation in 2012. This opened avenues for studying complex scattering resonances and dipolar Fermi gases [cite: 1, 11].

### 3.3 Expansion of the Species
Recent years have seen the successful cooling of other magnetic species:
*   **Thulium (Tm):** In 2020, the Akimov group utilized machine learning optimization to achieve BEC of Tm ($4 \mu_B$) in an optical dipole trap [cite: 8]. Tm offers a simpler electronic structure than Dy/Er while retaining significant magnetic character.
*   **Europium (Eu):** In 2022, Miyazawa et al. reported the BEC of $^{151}$Eu ($7 \mu_B$). Eu is unique among magnetic lanthanides for having a highly symmetric S-state ground state (zero orbital angular momentum), minimizing anisotropic collisional losses and potentially simplifying spinor physics [cite: 7, 12].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Cooling and Trapping of Lanthanides
Cooling lanthanides presents unique challenges due to their complex electronic structure. The standard technique involves a magneto-optical trap (MOT) operating on a broad transition for capture, followed by a narrow-line MOT (intercombination line) to reach microkelvin temperatures [cite: 2, 13].
*   **Machine Learning Optimization:** The complexity of evaporative cooling sequences, particularly for new species like Thulium, has necessitated the use of machine learning (Gaussian processes/Bayesian optimization). Davletov et al. (2020) demonstrated that ML could optimize evaporation ramps in optical dipole traps where human intuition failed due to unknown loss channels [cite: 8, 14, 15].

### 4.2 Feshbach Resonance Control
Magnetic lanthanides possess an extremely high density of Feshbach resonances due to the anisotropy of the interaction potential coupling many partial waves. This "Feshbach chaos" allows for precise tuning of the scattering length $a_s$, enabling the variation of $\epsilon_{dd}$ across the entire phase diagram [cite: 2, 11].

### 4.3 Vortex Generation Techniques
To probe superfluidity in dipolar supersolids, advanced stirring methods are required.
*   **Magnetostirring:** As demonstrated in the 2024 observation of vortices, a rotating magnetic field is used to deform the trap or the magnetic orientation, imparting angular momentum to the cloud. This technique requires extreme precision to spin up the supersolid without melting its fragile crystalline structure [cite: 4, 16, 17].

## 5. Applications and Case Studies

### 5.1 Fermi Surface Deformation (FSD)
In a non-interacting Fermi gas, the Fermi surface is spherical. In 2014, Aikawa et al. experimentally observed the deformation of the Fermi surface in a degenerate gas of fermionic erbium. The strong, anisotropic DDI stretches the momentum distribution along the direction of the dipoles (an ellipsoid). This was a direct observation of a many-body effect driven by long-range interactions in a Fermi gas, confirming theoretical predictions that the DDI competes with the Pauli exclusion principle to reshape the system's ground state [cite: 18, 19, 20].

### 5.2 Extended Bose-Hubbard Models (eBHM)
Optical lattices allow the simulation of solid-state physics. Baier et al. (2016) realized the extended Bose-Hubbard model using erbium atoms in a 3D optical lattice. Unlike standard Hubbard models with only on-site interactions, the long-range DDI introduced nearest-neighbor (NN) interactions. The experiment demonstrated that the superfluid-to-Mott-insulator transition depends on the orientation of the dipoles relative to the lattice, confirming the anisotropic nature of the hopping and interaction terms [cite: 11, 21, 22, 23].

### 5.3 Quantum Droplets
Around 2016, experiments in Dy and Er revealed that when the mean-field interaction is tuned to be slightly attractive ($\epsilon_{dd} > 1$), the gas does not collapse but forms stable, self-bound droplets. These droplets are stabilized by the repulsive LHY quantum fluctuations. This marked the discovery of a new state of matter: a dilute liquid that is self-bound in free space, distinct from the van der Waals liquids (like water) which are 8 orders of magnitude denser [cite: 2, 3, 9].

### 5.4 Dipolar Supersolids
The most prominent recent application is the realization of supersolidity.
*   **1D Supersolids (2019):** Three groups (Pisa, Stuttgart, Innsbruck) concurrently observed transient supersolid properties in dipolar gases, where the gas spontaneously breaks translational symmetry (forming droplets) while maintaining global phase coherence (superfluidity) [cite: 6, 24, 25].
*   **2D Supersolids (2021):** The Innsbruck group extended this to two dimensions, creating a long-lived supersolid state in erbium. This 2D geometry is crucial for studying vorticity and isotropic superfluid flow [cite: 5, 26, 27].

### 5.5 Observation of Vortices in Supersolids (2024)
A critical milestone was reached in 2024 by Casotti et al. (Innsbruck), who reported the observation of quantized vortices in a dipolar supersolid. While phase coherence had been established, vortices are the "hydrodynamic fingerprint" of superfluidity. The experiment involved rotating a 2D supersolid of dysprosium/erbium. The results showed a fundamental difference in vortex dynamics between unmodulated superfluids and supersolids; in the supersolid, vortices are pinned within the density minima (between droplets), confirming the coexistence of solid order and superfluid flow [cite: 4, 17, 28]. This result connects cold atom physics to the hydrodynamics of neutron stars, where "glitches" are believed to arise from vortex unpinning in the crustal supersolid [cite: 6, 29].

## 6. Challenges and Open Problems

### 6.1 Three-Body Recombination
A persistent challenge in dipolar physics, particularly in the droplet and supersolid regimes, is three-body recombination. The high densities required to stabilize these phases lead to rapid atom loss. While LHY stabilization works, the lifetime of these states is often limited to hundreds of milliseconds. Understanding and mitigating these losses, perhaps via Pauli blocking in fermionic mixtures or specific optical shielding, remains an open problem [cite: 2, 14, 30].

### 6.2 Temperature and Entropy
Achieving the extremely low entropies required for certain magnetic ordering phases in optical lattices (e.g., quantum magnetism models) is difficult. Dipolar relaxation heating can be significant. The recent work on finite-temperature phase diagrams of supersolids suggests that thermal fluctuations also play a complex role in the melting and formation of these states, which is not yet fully understood [cite: 31].

### 6.3 Complexity of the Spectrum
The dense Feshbach spectrum of lanthanides, while offering tunability, complicates the isolation of specific interaction regimes. The "chaotic" nature of these resonances makes theoretical prediction of scattering lengths difficult without extensive experimental mapping [cite: 32].

## 7. Future Research Directions

### 7.1 Dipolar Quantum Gas Mixtures
The realization of Er-Dy mixtures [cite: 33] opens the door to heteronuclear dipolar physics. Future research will likely focus on:
*   **Sympathetic Cooling:** Using one species to cool another to lower temperatures.
*   **Miscibility/Immiscibility:** Studying how DDI affects the phase separation of two superfluids.
*   **Dipolar Molecules:** While this review focuses on magnetic atoms, the interface with ultracold polar molecules (e.g., NaK) is growing. Molecules offer even stronger electric dipole moments, potentially allowing for crystallization at higher temperatures [cite: 34, 35].

### 7.2 Quantum Gas Microscopes for Magnetic Atoms
While standard for alkali atoms, single-site imaging (quantum gas microscopy) for magnetic lanthanides is an emerging frontier. This would allow for the direct observation of spin correlations in extended Hubbard models and the microscopic structure of supersolids [cite: 14].

### 7.3 Simulation of Astrophysical Phenomena
The observation of vortices in supersolids strengthens the link between cold atoms and neutron star physics. Future experiments aim to simulate "glitches"—sudden spin-ups of neutron stars—by studying the dynamics of vortex lattices in rotating supersolids under controlled acceleration [cite: 6, 29].

## 8. Conclusion

The field of dipolar physics with magnetic quantum gases has matured from the initial demonstration of weak dipolar effects in chromium to a rich domain of many-body physics dominated by strong, long-range interactions in lanthanides. The transition from studying simple BEC collapse to engineering extended Hubbard models, quantum droplets, and 2D supersolids highlights the versatility of this platform.

The very recent observation of quantized vortices in 2024 marks a crowning achievement, providing unambiguous proof of the superfluid nature of the supersolid phase. As the "dipolar periodic table" expands to include Thulium and Europium, and as control techniques refine, magnetic quantum gases are poised to unravel further mysteries of quantum matter, from the microscopic origins of magnetism to the macroscopic dynamics of astrophysical objects.

## References

[cite: 1] Chomaz, L., et al. (2023). "Dipolar physics: a review of experiments with magnetic quantum gases." *Reports on Progress in Physics*, 86(2), 026401. [cite: 1, 36]
[cite: 3] Chomaz, L., et al. (2022). "Dipolar physics: a review of experiments with magnetic quantum gases." *arXiv preprint arXiv:2201.02672*. [cite: 2, 3]
[cite: 34] Veljić, V. (2019). "Ground state and dynamics of dipolar quantum gases." PhD Thesis. [cite: 34]
[cite: 4] Casotti, E., et al. (2024). "Observation of vortices in a dipolar supersolid." *Nature*, 635, 327–331. [cite: 4, 17]
[cite: 17] University of Innsbruck. (2024). "Quantum vortices confirm superfluidity in supersolid." *Newsroom*. [cite: 17]
[cite: 28] Casotti, E., et al. (2024). "Observation of vortices in a dipolar supersolid." *arXiv preprint arXiv:2403.18510*. [cite: 28]
[cite: 16] Choucair, C. (2024). "Chasing Impossible Vortices: Supersolid Discovery and the Future of Quantum Technology." *The Quantum Insider*. [cite: 16]
[cite: 6] Poli, E. (2024). "Vortices in dipolar supersolids." *YouTube Seminar*. [cite: 6]
[cite: 36] Chomaz, L., et al. (2022). *Reports on Progress in Physics*. [cite: 36]
[cite: 2] Chomaz, L., et al. (2022). "Dipolar physics: A review of experiments with magnetic quantum gases." *ResearchGate*. [cite: 2]
[cite: 9] Chomaz, L., et al. (2022). *PubMed*. [cite: 9]
[cite: 5] Bonazza, S. (2021). "Our 2D Supersolid now in Nature!" *Erbium.at*. [cite: 5]
[cite: 29] Lab Horizons. (2024). "New evidence confirms supersolids' dual nature in quantum physics breakthrough." [cite: 29]
[cite: 26] MacDonald, F. (2021). "2D 'Supersolid' That Flows Without Friction Has Been Made For The First Time." *ScienceAlert*. [cite: 26]
[cite: 27] Langen, T. (2022). "Dipolar supersolids: Solid and superfluid at the same time." *Physics Today*. [cite: 27]
[cite: 18] Aikawa, K., et al. (2014). "Observation of Fermi surface deformation in a dipolar quantum gas." *arXiv preprint arXiv:1405.2154*. [cite: 18, 20]
[cite: 19] Aikawa, K., et al. (2014). *ResearchGate*. [cite: 19]
[cite: 35] Bigagli, et al. (2025). "Exploring dipolar many body effects in a degenerate molecular Fermi gas." *DAMOP*. [cite: 35]
[cite: 7] Miyazawa, Y., et al. (2022). "Bose-Einstein Condensation of Europium." *Physical Review Letters*, 129, 223401. [cite: 7]
[cite: 10] Griesmaier, A., et al. (2006). "Bose-Einstein Condensation of Chromium." *ResearchGate*. [cite: 10]
[cite: 8] Davletov, E. T., et al. (2020). "Machine learning for achieving Bose-Einstein condensation of thulium atoms." *Physical Review A*, 102, 011302. [cite: 8]
[cite: 14] Kumpilov, D., et al. (2023). "Learning from machine learning: optimization of the Bose-Einstein condensate of the thulium atom at a 1064 trap." *arXiv preprint arXiv:2311.06795*. [cite: 14, 37]
[cite: 13] Davletov, E. T., et al. (2020). *arXiv preprint arXiv:2003.00346*. [cite: 13]
[cite: 11] Baier, S. (2018). "Ultracold Dipolar Erbium Atoms: From Scattering Phenomena to Quantum Simulations." PhD Thesis. [cite: 11]
[cite: 21] Baier, S., et al. (2016). "Extended Bose-Hubbard models with ultracold magnetic atoms." *Science*, 352, 201-205. [cite: 21, 22]
[cite: 22] Baier, S., et al. (2016). *Semantic Scholar*. [cite: 22]
[cite: 23] Baier, S., et al. (2016). *ResearchGate*. [cite: 23]
[cite: 20] Aikawa, K., et al. (2014). *Science*. [cite: 20]
[cite: 18] Aikawa, K., et al. (2014). *arXiv*. [cite: 18]
[cite: 7] Miyazawa, Y., et al. (2022). *PubMed*. [cite: 7]
[cite: 12] Miyazawa, Y., et al. (2022). *arXiv*. [cite: 12]
[cite: 10] Miyazawa, Y., et al. (2022). *ResearchGate*. [cite: 10]
[cite: 17] University of Innsbruck. (2024). *Newsroom*. [cite: 17]
[cite: 8] Davletov, E. T., et al. (2020). *ResearchGate*. [cite: 8]
[cite: 15] Vendeiro, Z., et al. (2022). "Machine-learning-accelerated Bose-Einstein condensation." *Semantic Scholar*. [cite: 15]
[cite: 32] Davletov, E. T., et al. (2019). "Random to Chaotic Statistic Transformation in Low-Field Fano-Feshbach Resonances." *SciSpace*. [cite: 32]
[cite: 33] Durastante, G. (2020). "Dipolar quantum gas mixture experiment combining erbium and dysprosium atoms." PhD Thesis. [cite: 33]
[cite: 24] Weiss, et al. (2019). "The low-energy Goldstone mode in a trapped dipolar supersolid." *Nature*. [cite: 24]
[cite: 25] Tanzi, L., et al. (2019). "Supersolid symmetry breaking from compressional oscillations in a dipolar quantum gas." *Nature*. [cite: 25]
[cite: 31] Recati, A., et al. (2025). "Finite-temperature phase behavior of a harmonically trapped dipolar BEC." *arXiv*. [cite: 31]
[cite: 38] Baier, S., et al. (2016). *ICTP*. [cite: 38]
[cite: 39] Pollet, L., et al. (2010). "Study of the extended Bose Hubbard model." *PMC*. [cite: 39]

**Sources:**
1. [erbium.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdB6NRHiBJOhMhamp_8pyOfMKTyjq6cq-r1XA4xS6nmi237A_y8O-K02L77on4mscdEiF142md3MiLImSLkMTNn0sy4fIjCiEIBfGerVYGb4IXyK7klCQ1npK2LyYl4HGsmou7Jg2u015un8iK8ZUupl9yZ5kGDQHVvqU4_QI=)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHCT10U-UOpnKlmlejfd4_i9DCwlqp1IuqNk8sXRZ7RqJDghdJF4_1PYtVKt5_MY_qpxsYXGhmRbkbzoeTptsxAM6zQl2j0mZiNL4sRdo6uECCoLGQjZYXXCN9hRIGDlO5466Xr9VFr5VtBqCEfAUI80M3joiYOUcioqfVxwzAHaK2Qcnsm7lI7IgGWMf22c0bdrmuPjl0-Ws0_Kxka2ENgJi9-H1hvg3favM=)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFprHjakft3IWFKg36DrhuY2h0Akn_XXmcTnCYQOUgZK85W12VvukT7tOsKZds86L-cj0WYr9PEUa7XSS9MlUw3HgzAj28a8Lc41ut7t6ZLveWCTyLHjkCjc9hDMYbbFviFH3Ja5a6NHJYZ9qMXEoQyg120-cCRHhaPbbIXa112L8K84vhsUKo9kyx7_xaL6BkauCBIhx5zVlL4ieXQcmrtOwWpkn80o8oivxCLRzMq_5uD)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb0Jym4kckk367L2YGAV3qjrkbJoprj7pA8djKcy-pSAOqfo-qAGs5qJ6FVHtTLJepa_mzs5Hd3seZlVNziajlqmcwQyO3DiT_K3j7YytRLMDAx6bS)
5. [erbium.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4pjokhc6oy-j6qo2FYqh1lN7ECW-Pa-xl60k77pzSahKvWC-Z0xHPhKTE3DZDa6KEzGbwe6zI0clL3c-kQuX48K1DSc6d5HBwGTvI5D9FvqkgPsNzY4s6jfiYSKqomeuVuc6neecJ_0gPYfY=)
6. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLwMpyRTdZ2mTjcIyX1jzeqCb0jOii1hBBzyjlVqOOh_3C8fVlLwO2yhoZGj1F0yUfF9HW_wMtrnKPE8ybs0AD6ieMJOHmfGLGRCkC0jDdnKhfRl4NDZowKfd8hpbfQhM=)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrkp6kM5l9EJjdxL7OjlVWEAmvqeQ2C5IV4IF5fIVclrK3hOdI3dxk39nsEae4p7LZDAXpF3nUm6CGdqE94bkOn0NBze7KBn28liI0aEO2qDvdeyJTNXht2uewz3cK)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhikW4r7Ox0w2NkA0EHM3ZQhxlp8ID0fapUjKZVeNDqmM86IuxqoRi2jRtCnTGhwA9SRyCbOa1fbOMZz1wW35UWieJzt7bEVeldmVfqwewccCh1101H1KXfBwie6c3yOhtsjzExyWo5l3SZlTJJFNcCImGLgbIVo8jIIQbFgNpQ38AJlHELH8EuyCQBfi9o4ZAu4XW8cyNyI-QPeDKFvgfyl8XQjNS-oXEtBW1IBIz3OR2)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPl8z2456CS408uZvqFV7s79MHtuy6HZirGgFvkq9sqLv1o4_Nc15O6gAa5DcuRiKBB7qVzV-120Jm0XKdyIP4t3-yr6FXtAbz0buLwGt51vzu-00ER7a4iX6qmlt_)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2eMMjRbAcjUiArkcncHxVZgkLa-mIlotOFA11DhhnUdaaQZb2LuMRQFxSAYiMrMROi3yfRrCjlYprz6ObNdpccVR0xWoHL86Drgh7rkWpeIuIz5E_TeGsZqbz2JsB9_0d16Qe1Ou3h3FJJhZKWkFMl1D8IBb0q2oX1dMfwCi_NC9iQCMx1dd7CDN7_DiZ)
11. [erbium.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2o7bwRFcHIXAKu1xxHqxIQPc1z9tQoHemnuBswE4s9IW5H6FSGpjwHE3qUKnu2AGGnoOTb85rDRRGFqnB1UDV1pY-UsTOwA2l70ilTyTQdXHRbA-_sWQkvn8NDyvXqXFEssHIVrv_)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFntaohN_ehOWbC2Rbpxwc9bLbAU3sUXZxz2NfU5us5tgto6SPSTRJ3n0uo_e5LqfLZ-SJZrOXFV707kizCDPVhNjjygFaj-7bGAMQ7vhK7cJfq6SM8)
13. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcZn3cjpU2UDtbPJrDlhjw5Ky6hWhISJfekEDMnYewSLduAwDg9W_PJaPYLi7Ew-i3AWIe0rTMVQwuDLZtWPS7MJXqKRVd9BFy1c-Ib3Kq75sNHQni)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb9BhAOMoo0HMLmug8FwuoaOm0OLeIO7TcQ0Ay8KKFk1EHtMuVh0dlcyIquBBUMb_5fWNOina8BIhR47COESYjjYstPfXDZ8T6XpzSxRYyyVXEQF30)
15. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEB8DSAHUDkS7dmCBTnQ0yTgxoJS2ubqgPZ-7ELxvYiFbiV01iBrv0FXc0IqUggw2GZVp9x4yf03hExUpPNA19MrB84bubDZqwR7sOdycSdb8YeO3ShKFy-noCnFJO9p6QdUtRNuG5k_ozfrFyd8AxtSfTpGkydn8652bZ-JocbTz59b5RLNrVOz2owPjk4BNOAF8GLJ6F7fEOss0i8G_yMWPrGW1VPuFfqsldkqRkxvPIobpeZhAYfUSHtZZWe4fQ=)
16. [thequantuminsider.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE4GJ_2auzt4IhN9iIxgcW0F0Tt3Ge3kIcOb7QJZp6OlJHRZcemsSFTxZ7hlL88EvPFj1foQx4CCf5ycEuIIG5eFmunJmcULm_3GGeSAoBF1fgecgh5xFoTAtqalWtO1UpgB2JI-aS_jnvKMJ_3hhJjxHOSHVeR4X-mhcXkZYhT7gIxizGnuR5viReG26ZTrsHQC4NRgnVJ7bKDcG1AvX5rcu3NGLJT5Qv8IxdBSn5Ic_U2q8=)
17. [uibk.ac.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDLOZdTXUuMoCWCO2MSTGWU2XdoAqKCcJaU026Vw-VebDadiDmU9vSfN7WZMKXFOu63FUFh_VgibxBhebjeZEqHJbveefLFoQZZOJ6DfaeJMprHLuC5Wx5db3ncqq8xg-4m5ELmqvu6FB2uqIzoaIGuYYC1e4oAFIqPdsexdQ_YoxEcb7p2TrqWM2LQ1rmkfTfoA==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOQ6RmUiYRop0_Eulq2UeSHwNWnzyHiPVs7tTKbkssvOJbgmVs3M5ZCHJadSxmtoMutpnX7gcnS4Pu0qkzxsOpqupoXc_xU7fOg0j8wKBBL1hA0EI=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaddVguq8m13XTWzK66FH9UkB-jAXPAuRDKARD4XWwYKZTkhNS1g-s1uMZLlI2z_CZWrw_PPqvKjQcNPFP7zM4VrwgaClhaXaRv9eeLWw-Ds5AnS8LYPxBXKgMTZJ8xvTBgeh1EaqNGNQjwiVjlLxndghQqcr1a86xBtHo3opn6oysM02ndDxrmTuIuL1BcATo7fN_PCh1RpeKzntpbyzxZgu9hoMCsf6N)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqQehRVh3s5bCNKazFJaS00YzacuQaGkTniFQWkGn_Ci5yVhwky4O2qbvPvxk0vb9ILe9Kjzg43abM9TLcxIa7WRN9rXbi0jc0pjz_oz78iy2fYYg=)
21. [erbium.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEegvRSIEeNYahB71z_CBICZPlqafscgITQEtw2FSbWBvYX-Bled4odOGjjQKo-O2SsOYBAmoA1yPH31x1C28ArYZjedBOfpkdPWf9-i6BnIJImhAXtBK-iZpTPJ0umNfI2nyt0wAYQ)
22. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYhgf8UQcv87BdqbLyzKUNgarofR3BoFUTVRssmbR8TWt4iWRpJo-fzSduAw9nekD0AXU7HKIxRhScEIk5JRLpEsLpE3rkEVqJTDmxaSUwDU62Yr3rQDeMLU7IyQjX8tXIjxCS9ohJ1PvGtiFZPJKvi80lBvT9BOoQmbxnA_8LJVheriNc6F6bvYd4I8hXEJZ-gQrH9Azx4VHVDBJZffxSGZuUWl9bcXD9me1DiibQqz8Qir90RId12LCEurIpkTwH)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfokPyPnXkDPnMZ-G7-24SOyWKu7ti91aqQgVLl8vewNoxeAr5hGYeO13Kx3KrvtuqvsjMD84j01NTXOgDonxAwqywAzdskajOsGdjbvlHN_4KzM11S6-RPl3-Naf05KF9Ntk8_Lk4aKXWccE3itufIj1Suw3QRqj60FHK44gJDZir0c-WAXZXV-osliuOQjaUsjEe0KJWbGJn8Xt3hZJ1FdQ=)
24. [ifpan.edu.pl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED_hE1qpEop2Mi9GOBP3g0qgyV-VT5sJfxXlgMKIZVCgBWPZKUQUMRP9y1eFsfNt6EbP9QLuf8mDc712cjN1GhnCKFHcm-5rOuus5drPX4kOT8TecmLjqk8hHA-XxyQt8Fv2ZxI5bRZ2-JE3j1XlF_9lE=)
25. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnViFOtZzujWKu-1WyEQEiuXVk7K4eI--h30JDYZP8H75HWWfY21Tz2T416DkoYeDTWu1cv5ZfzQT57d4fzfqcbeeSzeDNcNcdfvoUbN6YTFdDHSHXXjfAA0zurDO0t-wpsWWDnXyYuFRAUCqMDxleHkxmRDsgnu33zQ-7wLNB3HLDRxOboYr8oR2-qf3diKcEKGiRQ1eix-ydgl0wtqNukSBUG5-VhUj-O7H8UeWqjnFFPfPs3Ku9KZIda1gxI9wmYUA2x5UmHJQk)
26. [sciencealert.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENTgvUCS3UJjQQvo08RON0JA1VUcYyJ32Hv_k7RBvXr5N9yboPGlVuE3gynac2chrGg0MOa-Fj03jJWOiQLWrgbwf4kPfElxoo3wJNJ5irIz_Y0A7PaFAXw4SJUJlaY9Jxs4yvILnMns210e-n0HSxeBoQwSZSNJZJpU39tw96D8p7V37YLLIQGrpzJLqjxKd1VKGaAFEfTvdO6duspw==)
27. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5dpZnVoLXcZzy19PwmB5Fy9RVG4jDPqqHFhT_qwXwPaEwBjUHFhaTz8ZuYPAf1ln3sNJEVV5spiI_PnII2vgRNOpfntMfzsqhUYd6UvF7ByJnZTm6rxFz8z1ejG2bVenaosZNxQzLSrfbNEO2xHuXPJjJ3KiiBYrmJ4qThhgo542RG5t2vBNvtAwJBP-L_S019vza)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVQgUGrQXXjCOl559kRJLs5Kr4oQPPTUWm6kR78I3lgS4HJCgKTNbJ3jgpoIB_6UVOgGp9D3lGqMeB5eiciQJuPF85uKPplClDS35LHmb9qVRP3xJY2LjT)
29. [labhorizons.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlPiA2_Y6hbJyWhGSf0WjYWkALBraCH_bR-M4iwWc2zFhw7QIe6F0dBQXWoA9xLQMcRTn1uMKV3QLNybN1BlN3WiCivToH0K3cirxDKnzT1m6_n72H61RG63yVEbEStRVIBREC6ZbzU5tlLdYActGdFlj2o0TkSY33A_8Noo5rkz4Ej0aajZ4Gk9eL-uaFqbdBz5gLlUl2_xX0ZyJ7pFHF2C-FHB4=)
30. [ox.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEon_PII_PglpIIo-GUlryllgyC7uYLyitXVBf96big2O_pCB57N0JWd8lo42wQeDA68vwkzebEfCuXPa8Wa7E-L4Yn1emB9fgLebHtmlQLnvbdoDO3KXInIXEyLlhDHZ9j3jQ2mayOnqoL7Rr-GgOJRV3ZZ1vuwAFbeux0T74l0H6b1gDtcM3uPLv3YtuFjbvlsiavRXzB8RuBD3O4ivp2lxszJZ_cPX4lBOI5WeyvIdvtmg==)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE5V_lgiMLUIxqgMPi1zyrfYPEFuDYFn50osQd0SO4A0PHT73TbxsKloXVykJ8V2OoAt9CRvLW5uwJfTDKAGmsjG2wwGeXGCNUbLo1VHtkTzGe3kgJ00HLgw==)
32. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkCYAm_-uqtC55KFcuBDQsGg3PR1RR2_wYa8u2Qmd2oDdzK9fhyqookGrGJfd0cgFYDV06JMLZhvSfkDHG986eokgJxJBRIYLYteUtDZ58mKT4iM_4B0G1X8nQFs-SYatlja75Qk3KXfocWoYqzxOPzyFqxCes4CazpIWPaufU-pSo3JXjOuJwr128i1S02TDlx1WNJQhNyUJBHg==)
33. [erbium.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwMfRnVekS1Gw7mA0iv6KUvS8lCunfqX34vryc0_b54Y2jW_Hk6nxExPk3_fjXv5n4fFXafZcf4b4MqZoCCTMzIvib-o7PryLi-4SAT7607Xvu3TY5LtswDwOAo6-OqMusA-h22FBgaYCZ-2KhAHLd8boSDrTof_STUDZaw_2wjmLkEphyvmz0U0JH9mc=)
34. [scl.rs](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECQ88ai-0H6l1dhkM2AL0-WaaQ-ZB6wxOkGvbPBbW6Ewo-kSwpRgomf4Iz9aiImEAuc_JWp9hBdmVGX5xC3hWUQsex05ziJCKJrevmx_r9RMXZVlhsb5Zb2XvbjGhY)
35. [aps.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFklgVLfDD3vs83FqrsOjo6W2QKb9fo2Y063mPkTkdtX2HOQg9dVo42o1id9m7WDBaxap8wmn1R1be8i0dp2SVmM_stz2vS4Lku4ywV84EiO__z6Pc7wlHDYwIA74V1)
36. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgOF4tppepChA_oH7SSxt8_XYyJERVmuK98Mauw07FbtbC3utxbBDizD562K8BlTbxuCLeCiVzVdCvAJ07QBmNTnYi2cOLcaXWxEAI1gTSLkWre5LpCBx8IYIalWaSIQGpNoByDSunVa3bIcqGilR9ng==)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdXle4szwBaNKQeNHhuomY89GDO7oTz0QQxtyRpda3Ce3gmmXFojLTsrmd3zyC-Qh8kMFEnEnVOOdeC8WfnPbqccngEk0J91oDVJfVU1igGFFo2W3wGQCLCBAlTEYa1hdhB22GZqD2WmNM8sPLyfWhJvWHiNUwcwPeYNIvEbNBTQ9v4MugxL8QVF8jKl0l1la2vaG-7lehQtCMcu4ZMVj-63lpKgFjqD4aNFxtzlrpqMpR9Sh-XYdFDbqKV2e63RWoP8Wlk1dcQIPkL0TXmudg_yF6JEtgjg==)
38. [ictp.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHP-znJkWLDXVf200AUvMqnoWgAXjk4ifZMWog6oyQOECrGnzICI79QCn-ISICqA-Rz2jWhGHCkL_jmPUurwP-3HQhCckS2E2YeYLDSnBiBkBsFbavZJVP7thzD0UplLiuriZXAJa_7INs6Wi7wG8r51udAgyjUfH9OhKHHUhjczIG)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoQ2Q8Gh3kHgSO0BH16C4qdzpHAMBaiuqrkQVF9XVxel-JyJRGjBxQwEyzi4SQjsAvsP576BAuwvIag2eQNJlc5NGtKk8dTGeKFWCC6RCXdHsGuvMjCZSgHT0UHw8miusPybcKXEo=)
