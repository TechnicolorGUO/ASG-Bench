# Literature Review: Quantum many-body scars and Hilbert space fragmentation- a review of exact results.

*Generated on: 2025-12-26 15:12:30*
*Progress: [12/21]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Quantum_many-body_scars_and_Hilbert_space_fragmentation-_a_r_20251226_151230.md*
---

# Quantum Many-Body Scars and Hilbert Space Fragmentation: A Review of Exact Results

**Key Points**
*   **Paradigm Shift:** Quantum many-body scars (QMBS) and Hilbert space fragmentation (HSF) represent novel mechanisms of weak ergodicity breaking, violating the Eigenstate Thermalization Hypothesis (ETH) without relying on disorder (like Many-Body Localization).
*   **Exact Constructions:** The field has moved from numerical observation to rigorous analytical frameworks, primarily utilizing Shiraishi-Mori embedding, Spectrum Generating Algebras (SGA), and Commutant Algebras to construct exact non-thermal eigenstates.
*   **Fragmentation:** HSF is characterized by the exponential shattering of the Hilbert space into dynamically disconnected sectors due to kinetic constraints (often linked to dipole conservation and fracton physics), definable via the commutant algebra dimension.
*   **New Detection Methods:** Recent advances (2024-2025) have introduced "Fisher Zeros" in the complex temperature plane and Quantum Machine Learning (QML) techniques as powerful tools to identify scarred eigenstates without exhaustive diagonalization.
*   **Classical-Quantum Correspondence:** Emerging research is re-evaluating the link between QMBS and Unstable Periodic Orbits (UPOs), proposing a distinction between "thermal" and "non-thermal" scars.

---

## 1. Introduction and Background

The statistical mechanics of isolated quantum systems rests fundamentally on the Eigenstate Thermalization Hypothesis (ETH). ETH posits that for generic non-integrable systems, individual energy eigenstates are locally indistinguishable from a thermal ensemble, allowing the system to relax to thermal equilibrium solely through unitary evolution [cite: 1, 2]. For decades, the primary exception to this rule was Many-Body Localization (MBL), where strong disorder prevents thermalization across the entire spectrum.

However, recent experimental and theoretical discoveries have unveiled a new regime of "weak" ergodicity breaking. This began with the observation of coherent, long-lived oscillations in a chain of Rydberg atoms, a system expected to be non-integrable and thermalizing [cite: 2, 3]. This phenomenon, termed **Quantum Many-Body Scars (QMBS)**, involves a small number of non-thermal eigenstates embedded within a dense spectrum of thermal states. Unlike MBL, where all states violate ETH, QMBS constitutes a violation of the strong ETH while potentially satisfying the weak ETH (where most states are thermal).

Parallel to this, the concept of **Hilbert Space Fragmentation (HSF)** emerged, describing systems where kinetic constraints fracture the Hilbert space into an exponentially large number of dynamically disconnected sectors [cite: 4, 5]. While QMBS and HSF share phenomenological similarities—such as the failure to thermalize from specific initial states—they represent distinct algebraic structures.

This review focuses on the "exact results" in this field. While early work relied heavily on numerics, the maturation of the field has provided rigorous frameworks—such as the Shiraishi-Mori embedding, commutant algebras, and spectrum-generating algebras—that allow for the analytical construction of Hamiltonians hosting these exotic states [cite: 6, 7]. We further review the most recent developments from 2023-2025, including the application of Fisher zeros [cite: 8, 9] and quantum machine learning [cite: 10] for scar detection.

## 2. Key Concepts and Definitions

### 2.1 Quantum Many-Body Scars (QMBS)
QMBS are defined as a set of measure-zero eigenstates in a many-body Hamiltonian that exhibit sub-volume law entanglement entropy (often area-law or logarithmic) despite lying at high energy densities where volume-law entanglement is typical [cite: 2, 6].
Key signatures include:
*   **Revivals:** High-fidelity periodic revivals of the wavefunction $|\psi(t)\rangle$ when initialized in specific product states (e.g., the Néel state).
*   **Non-thermal Expectation Values:** Local observables in scarred eigenstates deviate significantly from the microcanonical ensemble predictions.
*   **Tower of States:** Scars often appear as a tower of eigenstates equally spaced in energy, $E_n \approx E_0 + n\omega$, facilitating coherent dynamics [cite: 3, 11].

### 2.2 Hilbert Space Fragmentation (HSF)
HSF occurs when the Hilbert space $\mathcal{H}$ decomposes into a direct sum of dynamically disconnected Krylov subspaces, $\mathcal{H} = \bigoplus_\lambda \mathcal{K}_\lambda$, such that the Hamiltonian is block-diagonal [cite: 4, 12].
*   **Strong Fragmentation:** The dimension of the largest Krylov subspace vanishes relative to the total Hilbert space dimension in the thermodynamic limit ($D_{max}/D_{total} \to 0$).
*   **Weak Fragmentation:** The largest subspace dominates, but exponentially many smaller, disconnected subspaces persist.
*   **Commutant Algebra Definition:** HSF is rigorously defined when the dimension of the commutant algebra (the set of operators commuting with all local Hamiltonian terms) grows exponentially with system size [cite: 4, 5].

### 2.3 Classical vs. Quantum Fragmentation
A crucial distinction exists between fragmentation in the product state basis (classical) and fragmentation that requires an entangled basis (quantum). Classical fragmentation is often visible in the connectivity graph of Fock states, while quantum fragmentation requires algebraic analysis of the bond algebra [cite: 4, 5].

## 3. Historical Development and Milestones

### 3.1 The Rydberg Surprise (2017)
The field was ignited by the experiment of Bernien et al. (2017) using a 51-atom Rydberg simulator. The system, modeled by the PXP Hamiltonian, showed unexpected revivals from the antiferromagnetic state. This contradicted the prediction of rapid thermalization for non-integrable models [cite: 2, 3].

### 3.2 The AKLT Model and Exact Scars (2018)
Following the PXP discovery, Moudgalya et al. and others identified exact towers of scarred eigenstates in the Affleck-Kennedy-Lieb-Tasaki (AKLT) model. This provided the first analytical proof of QMBS, showing that the ground state of the AKLT model could be "lifted" to high energies as exact excited states [cite: 1, 6, 13].

### 3.3 Systematization via Embedding (2017-2019)
Shiraishi and Mori (2017) provided a systematic method to embed non-thermal states into non-integrable Hamiltonians using local projectors. This formally established that ETH violation could be constructed analytically, moving the field beyond serendipitous discovery [cite: 3, 14].

### 3.4 Fractons and Dipole Conservation (2019-2020)
The connection between HSF and fracton phases of matter was established by analyzing models with dipole moment conservation (e.g., conserving both charge $Q = \sum n_i$ and dipole $P = \sum i n_i$). These constraints were shown to lead to extensive fragmentation, linking condensed matter topological phases with non-ergodic dynamics [cite: 15, 16, 17].

## 4. Current State-of-the-Art Methods and Techniques

The theoretical backbone of QMBS and HSF relies on algebraic constructions that allow for exact solutions.

### 4.1 Shiraishi-Mori (SM) Embedding Formalism
The SM formalism constructs a Hamiltonian $H$ such that a target subspace of states $\mathcal{T}$ is an eigenspace. The Hamiltonian takes the form:
$$ H = \sum_j P_j h_j P_j + H' $$
where $P_j$ are local projectors satisfying $P_j |\psi\rangle = 0$ for all $|\psi\rangle \in \mathcal{T}$. The "target space" $\mathcal{T}$ is annihilated by the local operators, making them exact eigenstates of $H'$ (and thus $H$) if $[H', P_j]=0$ or if $H'$ is chosen appropriately. This method allows the embedding of low-entanglement states into thermal spectra [cite: 3, 14, 18].
*   **Recent Extensions:** This formalism has been extended to open quantum systems (Liouvillians), creating decoherence-free subspaces that host scars [cite: 18].

### 4.2 Spectrum Generating Algebras (SGA)
SGA explains the "tower" structure of scars. If a Hamiltonian $H$ possesses a ladder operator $Q^\dagger$ such that:
$$ [H, Q^\dagger] = \omega Q^\dagger $$
and there exists a reference state $|\psi_0\rangle$ (often the ground state), then the states $|\psi_n\rangle = (Q^\dagger)^n |\psi_0\rangle$ are exact eigenstates with energy $E_n = E_0 + n\omega$.
*   **Restricted SGA (RSGA):** In many cases, the commutation relation only holds within a specific subspace or when acting on specific states. This "restricted" algebra is responsible for scars in the AKLT and Hubbard models (via $\eta$-pairing) [cite: 11, 19, 20, 21].

### 4.3 Commutant Algebras and Bond Algebras
To rigorously define HSF, one analyzes the **commutant algebra** $\mathcal{C}$, defined as the set of all operators that commute with every local term $h_i$ of the Hamiltonian $H = \sum h_i$.
*   **Fragmentation Criterion:** If $\dim(\mathcal{C})$ scales exponentially with system size $L$, the system is fragmented. If it scales polynomially (e.g., due to $U(1)$ or $SU(2)$ symmetry), it is not fragmented in the HSF sense [cite: 4, 5].
*   **Bond Algebra:** The algebra generated by the local terms themselves. The structure of the bond algebra dictates the commutant. This framework distinguishes "classical" fragmentation (diagonal in product basis) from "quantum" fragmentation (involving entangled bases like the Temperley-Lieb chains) [cite: 4, 5].

### 4.4 Fisher Zeros and Complex Temperature Analysis (2024-2025)
A novel detection method involves the **Fisher zeros** of the partition function $Z(\beta) = \text{Tr}(e^{-\beta H})$ analytically continued to the complex $\beta$ plane.
*   **Mechanism:** For thermal systems, Fisher zeros typically lie on the imaginary axis (Lee-Yang zeros) or form specific patterns. Recent work shows that QMBS causes a continuous line of Fisher zeros to extend off the imaginary axis, separating the $\beta$-plane into regions with distinct thermalization behaviors [cite: 8, 9].
*   **Significance:** This provides a "statistical mechanics" approach to detecting scars without needing to compute entanglement entropy for every eigenstate, linking scars to dynamical phase transitions [cite: 22].

### 4.5 Quantum Machine Learning (QML) Detection
With the complexity of many-body systems, QML has emerged as a tool to identify scars.
*   **Techniques:** Quantum Convolutional Neural Networks (QCNNs) and Variational Autoencoders (VAEs) have been trained to distinguish scarred eigenstates from thermal ones based on entanglement features and correlation properties.
*   **Performance:** QCNNs have demonstrated >99% accuracy in identifying known scars and have discovered new non-thermal states in models like the extended Su-Schrieffer-Heeger model [cite: 10, 23].

## 5. Applications and Case Studies

### 5.1 The PXP Model
The PXP model, describing Rydberg atoms under blockade, remains the paradigmatic case. While not integrable, it hosts a set of states with high overlap with the $\mathbb{Z}_2$ ordered state. Exact results here are often approximate or rely on perturbations of the exact PXP limit, but the SM embedding can construct "parent Hamiltonians" for which PXP-like scars are exact [cite: 2, 3].

### 5.2 Dipole-Conserving Models (Fractons)
Models conserving charge and dipole moment ($U(1) \times U(1)_{dipole}$) exhibit strong fragmentation.
*   **Mechanism:** A single charge cannot move because it would change the dipole moment. Charges can only move in bound pairs (dipoles) or by emitting dipoles. This kinetic constraint shatters the Hilbert space [cite: 15, 17, 24].
*   **1D Spin-1 Models:** The Hamiltonian $H = \sum S^+_j (S^-_{j+1})^2 S^+_{j+2} + h.c.$ is a canonical example where the commutant algebra grows exponentially, proving the existence of non-thermalizing subspaces [cite: 4, 15].

### 5.3 Lattice Gauge Theories (LGTs)
QMBS has been identified as a robust feature in LGTs, particularly in $U(1)$ and $\mathbb{Z}_2$ gauge theories.
*   **Confinement:** Scars in these models are often interpreted as confined meson excitations that fail to decay.
*   **Robustness:** Unlike some fine-tuned scar models, scars in LGTs appear robust against certain perturbations that preserve gauge invariance. Recent work (2023-2025) has extended this to non-Abelian $SU(2)$ LGTs, showing that scarring is not limited to simple Abelian groups [cite: 25, 26, 27].

## 6. Challenges and Open Problems

### 6.1 Stability and Perturbation
A major open question is the stability of QMBS under generic perturbations. While SM embedding creates exact scars, adding an arbitrary small perturbation $\epsilon V$ usually destroys the exact scar. However, the *dynamical* signature (revivals) often persists for long times. Understanding the timescale of this decay—whether it is perturbative or non-perturbative—remains a challenge [cite: 25, 28].

### 6.2 The Thermodynamic Limit
For some models, it is debated whether the fraction of scarred states vanishes in the thermodynamic limit or if they constitute a finite density of states in specific regimes. In strong fragmentation, the ratio of the largest sector to the total space vanishes, but in weak fragmentation, the "thermal" sector dominates [cite: 12, 29].

### 6.3 Classical-Quantum Correspondence
The relationship between QMBS and classical chaos is complex. Early work suggested scars were quantization of Unstable Periodic Orbits (UPOs). However, recent studies (2024) have found "thermal QMBS" that originate from UPOs but satisfy ETH, contrasting with the standard "non-thermal" scars. This suggests the need to refine the definition of scars when mapping to semiclassical limits [cite: 30, 31, 32, 33].

## 7. Future Research Directions

### 7.1 Higher Dimensions
Most exact results are limited to 1D spin chains. Extending the commutant algebra and SGA frameworks to 2D and 3D systems is a frontier. Recent work on "lifting" 1D fragmented models to higher dimensions using subsystem symmetries is a promising step [cite: 12].

### 7.2 Open Quantum Systems
Engineering scars in dissipative systems (Lindblad dynamics) to create decoherence-free subspaces for quantum information storage is a key application. The extension of SM embedding to Liouvillians provides a theoretical roadmap for this [cite: 18, 34].

### 7.3 Unifying Frameworks
While SGA, SM embedding, and commutant algebras explain many cases, a single unified framework encompassing all forms of weak ergodicity breaking is still lacking. The "group-invariant" formalism and "quasisymmetry" approaches are attempts to bridge these gaps [cite: 3, 35].

### 7.4 Experimental Realization of Fractonic Scars
While Rydberg atoms realized PXP scars, experimentally verifying the strong fragmentation predicted in dipole-conserving models remains a goal, likely suited for digital quantum simulators or ultracold atoms in tilted optical lattices [cite: 24, 27].

## 8. Conclusion

The study of Quantum Many-Body Scars and Hilbert Space Fragmentation has fundamentally altered our understanding of thermalization in isolated quantum systems. Moving beyond the dichotomy of "Integrable vs. Chaotic," these phenomena demonstrate that exact, non-thermal eigenstates can be systematically constructed and embedded within thermal spectra. The development of rigorous analytical tools—specifically Shiraishi-Mori embedding, Spectrum Generating Algebras, and Commutant Algebras—has transformed the field from phenomenological observation to exact mathematical construction.

Current research is rapidly expanding into detection methodologies, with Fisher zeros and Quantum Machine Learning offering new diagnostic powers. Furthermore, the intersection with Lattice Gauge Theories and Fracton physics highlights the interdisciplinary importance of these concepts, linking condensed matter constraints with high-energy physics phenomena. As the field matures, the focus is shifting toward harnessing these ergodicity-breaking states for robust quantum information processing, turning the "bug" of non-thermalization into a "feature" for quantum memory.

## References

[cite: 3] Shiraishi, N., & Mori, T. (2017). Systematic Construction of Counterexamples to the Eigenstate Thermalization Hypothesis. *Physical Review Letters*. [cite: 3, 14, 18]
[cite: 18] Gotta, L. (2025). Open-system quantum many-body scars: a theory. *Physics*. [cite: 18, 34]
[cite: 1] Moudgalya, S., et al. (2018). Exact Excited States of Non-Integrable Models. *Physical Review B*. [cite: 1, 13]
[cite: 2] Turner, C. J., et al. (2018). Weak ergodicity breaking from quantum many-body scars. *Nature Physics*. [cite: 2, 25, 36]
[cite: 14] Shiraishi, N., & Mori, T. (2017). *arXiv preprint*. [cite: 14]
[cite: 4] Moudgalya, S., & Motrunich, O. I. (2021). Hilbert Space Fragmentation and Commutant Algebras. *Physical Review X*. [cite: 4, 5, 37]
[cite: 5] Moudgalya, S., & Motrunich, O. I. (2022). *arXiv preprint*. [cite: 5]
[cite: 37] Moudgalya, S. (2022). Hilbert Space Fragmentation and Commutant Algebras. *Benasque Talk*. [cite: 37]
[cite: 38] APS Global Physics Summit. (2025). Fragmenting Hilbert space: Polynomial Factorization and Commutant Algebra. [cite: 38]
[cite: 39] Moudgalya, S., et al. (2022). Quantum many-body scars and Hilbert space fragmentation: a review of exact results. *Reports on Progress in Physics*. [cite: 6, 7, 39]
[cite: 40] City of Gold Coast Time. (2025). [cite: 40]
[cite: 6] Moudgalya, S., Bernevig, B. A., & Regnault, N. (2022). Quantum many-body scars and Hilbert space fragmentation: a review of exact results. *Reports on Progress in Physics*. [cite: 6, 7]
[cite: 34] Gotta, L. (2025). Open-system quantum many-body scars: a theory. [cite: 34]
[cite: 7] Moudgalya, S., et al. (2021). *arXiv preprint*. [cite: 7]
[cite: 41] ResearchGate. (2025). Quantum Many-Body Scars and Hilbert Space Fragmentation. [cite: 41]
[cite: 36] Serbyn, M., Abanin, D. A., & Papić, Z. (2021). Quantum many-body scars and weak breaking of ergodicity. *Nature Physics*. [cite: 36]
[cite: 19] Encyclopedia of Math. (2020). Spectrum generating algebra. [cite: 19]
[cite: 42] Kusnezov, D. (2019). Quantum Systems, Spectrum Generating Algebras and Non-Compact Lie Algebras. [cite: 42]
[cite: 11] Moudgalya, S., Regnault, N., & Bernevig, B. A. (2020). $\eta$-Pairing in Hubbard Models: From Spectrum Generating Algebras to Quantum Many-Body Scars. *Physical Review B*. [cite: 11]
[cite: 43] CBPF. (2023). N = 2 Superconformal Quantum Mechanics. [cite: 43]
[cite: 44] Sigma Journal. (2013). Dynamical Equations... Spectrum Generating Algebras. [cite: 44]
[cite: 45] arXiv. (2024). Hilbert Space Fragmentation and Subspace Scar Time-Crystallinity. [cite: 45]
[cite: 46] Will, M., Moessner, R., & Pollmann, F. (2023). Realization of Hilbert Space Fragmentation and Fracton Dynamics in 2D. [cite: 46]
[cite: 12] arXiv. (2025). Hilbert space fragmentation in high dimensions. [cite: 12]
[cite: 29] arXiv. (2025). HSF fractures the full Hilbert space. [cite: 29]
[cite: 47] ResearchGate. (2024). Tunable Hilbert space fragmentation. [cite: 47]
[cite: 28] ETH Zurich. (2024). Quantum scars as a way out of thermalisation. [cite: 28]
[cite: 30] Evrard, B., et al. (2024). Quantum many-body scars from unstable periodic orbits. *Physical Review B*. [cite: 30, 31, 32, 33, 48, 49]
[cite: 31] Evrard, B., et al. (2024). *Scholars Mine*. [cite: 31]
[cite: 25] Halimeh, J. C., et al. (2023). Robust quantum many-body scars in lattice gauge theories. *Quantum*. [cite: 25, 50]
[cite: 10] Feng, J., et al. (2025). Uncovering Quantum Many-body Scars with Quantum Machine Learning. *npj Quantum Information*. [cite: 10, 23, 51]
[cite: 52] SciSpace. (2020). Revealing quantum chaos with machine learning. [cite: 52]
[cite: 51] Semantic Scholar. (2025). Uncovering quantum many-body scars. [cite: 51]
[cite: 53] CoLab. (2025). Shallow quantum circuits are robust hunters for quantum many-body scars. [cite: 53]
[cite: 54] Zhang, B. (2025). Research Portfolio. [cite: 54]
[cite: 8] Meng, Y., et al. (2025). Detecting Many-Body Scars from Fisher Zeros. *Physical Review Letters*. [cite: 8, 9, 22, 55]
[cite: 9] Meng, Y., et al. (2025). *arXiv preprint*. [cite: 9]
[cite: 55] Semantic Scholar. (2025). Detecting Many-Body Scars from Fisher Zeros. [cite: 55]
[cite: 22] arXiv. (2025). Abstract: Detecting Many-Body Scars from Fisher Zeros. [cite: 22]
[cite: 25] Quantum Journal. (2023). References in Halimeh et al. [cite: 25]
[cite: 56] arXiv. (2025). Fidelity zeros and Lee-Yang framework. [cite: 56]
[cite: 57] Semantic Scholar. (2025). Dynamical quantum phase transitions. [cite: 57]
[cite: 58] Scribd. (2025). Fisher Zeros document. [cite: 58]
[cite: 32] arXiv. (2024). Quantum many-body scars from unstable periodic orbits. [cite: 32]
[cite: 59] Bohrium. (2024). Quantum many-body scars as remnants of stable many-body periodic orbits. [cite: 59]
[cite: 33] arXiv. (2024). Full text: Quantum many-body scars from unstable periodic orbits. [cite: 33]
[cite: 48] Semantic Scholar. (2024). Quantum many-body scars from unstable periodic orbits. [cite: 48]
[cite: 49] Harvard. (2024). Publication record. [cite: 49]
[cite: 8] ResearchGate. (2025). Detecting Many-Body Scars from Fisher Zeros. [cite: 8]
[cite: 22] arXiv. (2025). Abstract: Fisher Zeros. [cite: 22]
[cite: 9] arXiv. (2025). Full text: Fisher Zeros. [cite: 9]
[cite: 58] Scribd. (2025). Fisher Zeros. [cite: 58]
[cite: 55] Semantic Scholar. (2025). Fisher Zeros. [cite: 55]
[cite: 6] Caltech. (2022). Review of exact results. [cite: 6]
[cite: 7] arXiv. (2021). Review of exact results. [cite: 7]
[cite: 41] ResearchGate. (2025). Review of exact results. [cite: 41]
[cite: 34] Semantic Scholar. (2021). Review of exact results. [cite: 34]
[cite: 13] Shamra Academia. (2018). Entanglement of Exact Excited States. [cite: 13]
[cite: 10] ResearchGate. (2025). Uncovering QMBS with QML. [cite: 10]
[cite: 52] SciSpace. (2020). Machine Learning and Chaos. [cite: 52]
[cite: 51] Semantic Scholar. (2025). QML and Scars. [cite: 51]
[cite: 23] ResearchGate. (2025). QML and Scars (Full text). [cite: 23]
[cite: 53] CoLab. (2025). Shallow circuits for scars. [cite: 53]
[cite: 35] ResearchGate. (2024). Many-Body Scars as a Group Invariant Sector. [cite: 35]
[cite: 60] ResearchGate. (2024). Numerical methods for detecting symmetries. [cite: 60]
[cite: 20] U-Tokyo. (2024). Thesis on QMBS and SGA. [cite: 20]
[cite: 14] ResearchGate. (2025). Systematic Construction of Counterexamples. [cite: 14]
[cite: 21] ResearchGate. (2020). Unified structure for exact towers. [cite: 21]
[cite: 25] Quantum Journal. (2023). Robust scars in LGT. [cite: 25]
[cite: 61] Munich Workshop. (2022). QMBS in Abelian LGT. [cite: 61]
[cite: 26] INIS. (2025). QMBS in non-Abelian LGT. [cite: 26]
[cite: 50] Semantic Scholar. (2022). Robust scars in LGT. [cite: 50]
[cite: 27] SCL. (2023). Scars in truncated Schwinger model. [cite: 27]
[cite: 15] TUM. (2020). Hilbert space fragmentation and fractons. [cite: 15]
[cite: 16] arXiv. (2019). Ergodicity breaking from fragmentation. [cite: 16]
[cite: 17] ResearchGate. (2020). Ergodicity Breaking Arising from HSF. [cite: 17]
[cite: 62] Semantic Scholar. (2023). Local Integrals of Motion. [cite: 62]
[cite: 24] YouTube (BSS Physics School). (2023). Pollmann on HSF and Fractons. [cite: 24]

**Sources:**
1. [u-tokyo.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESZnsA-0JK0OpI1xWgjaQU83BjZMKGfZ0HPCDYhQoaGEeHSVa-vGwhlvA0nZJpKDu3IHQdSkjPZVWVIrqn2g7iFvcm7pii0vQf1ThZus1rvLc4VSWl2MFWb1vwpvz8QeytOwf0xczj8j98oIMZ7KUJs4niPwjPVp4hPeKT6A==)
2. [kyoto-u.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrIV-swrF2hVBiRsRc4P626QFu4Zu0qMui8eKgZX3rmxBDSEZQeylKCo39vvotLUwVxrnl9LpvU3oN6A9FdUW5lSaPTsm5hRmhuq6NN_mKZN26ghL9Y5LQ_b_cD5Jz5SF2cgjhQcgv0JiJR9Sj9zFd3EWYXnaMJs6b7r6DMoizhyFR_fbTIQL6)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEN_QVXUt_v1QyXasXdOCmYkqxhFBvHhNM9guQMCiDADCuh3H3dX4rlBGmIVJpXD9ZZuWHr9nhzi-iDCahczPh8n-2KYGgtbiI5DSC06u6n24Zc5aISysvAQQ==)
4. [caltech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGAU1qKrpp58raVd6sEbX4YT0Zrg2XrfqDIu0rD9oBRDhj4x9MjQhvso8L0pmiQMAyA6bcUkTAaHQOEpkrBqXlphcgswkzHe14f0x7JqyTcOUwpePMaihfy_O3dYBxlt2QNZEKCv4Ime5EC3Bp03n6CR6pZw==)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJdS3drdf0J7jgk77m4V_w46IA0HWSkgwkMrRKjECM0mxDClVpVsZoR2CKBAIXUQqGW4fOgztogwbNpd29-cW0A4HeWy2VLTS8DB1zbPcWSbMzmZKrAg==)
6. [caltech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHOmPtbhE1f0C_9YPnmdWf_Bng5B_8Bb7U3SsAfNpZcYXwXvwVO0wfX8kjRHTK-gM7QxBfvV93IcTjky71wkd23zRb_Zk3rFCjhY-PHk_ml2PDOtgnHOy4uIvgG93Hjfar53QcESPfe95ERqQYg-4w0y4-EQ==)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyXDy_Jtows6SnNqlulcN3U8zKLjQV_D6VrMDxzYUBPO2n77qkK9_t_RkKSbaVo2EzoA_9y8A1OHp1PntmJ3cRdjdEvSixz6qWh2bnCyKG__RS2NBwBg==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVZPnuOJP5uNRH6Q_715vsdmMeoj5341S-wFA_ps7mdACN-kPRzGP1A9JEJ-5v8NSdHWEcLbzqVBMxhiQop3MsYgOpZ4eHH3Af6A1l9rhEJReudyds9RjFuvLVR0AFRdZVh9Qg_oGcpYHoMI3lsPpLjci6CR9FE5Ae7cTkyQXTpdHUKxeE25pVIK7zXZf8kOO-ryv3)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-Zvkf3tmo1c2xdB5SjvlKaipKSP6rKi7H0he7eQ4KpK8b6fC3RBkvwKutymdf8XeV9gMsp5JBMjpFfwn1cpVj7WEFYznJ6_kfrp2xGbRZYEBZlovDge8s0g==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCFMdo0FKAqmpQQb5g6PlZPr5eojI8zG4pb1RtBNyJT95yHA5CDwlZGjGpeZiJ-BITu2ol7HB634sgXOxJ-ASpvywY-KvHM4aCPZVLA8-pZqB8Hy50_jc0xbMga29hTkd-r58AzYKm9MC1VkJzCEeTBmmDix6nQQHOcJcEyjnqMlagQhVzFlm4aRo-eyYk2Ux4MJFMAu8JTqgyMGdpH2JdmTcHx4q4XI5Y)
11. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlPNIkdFNYgTJwGN8l3ekLvguD8wrAIyZsP8o3UrvQ0IFq9_L0JBU7xXrSM1I309rSowI3m0E22X-Q7wEEcUkjAIW5gVodrEF9nSm5zBqgewV1jcRGwQ==)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT7UbiQEhO-1uovLBRgB4MSS7tKRH_Bjt_lhOu2iVBicE71r5NqC5LVZEo4nfDmDJAjb-Yqpi1B9TbkDLngGkLI0oxNo7h5bxYCEZSsWQXgY9BmwwYZGqcVQ==)
13. [shamra-academia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsk8bP2uBoN6ilk9t_IOcbM5fbTFviJPQhywaJeRrnfs_VKYFG2o9hv49U7gwiS_Z2z9CYIvJDltsftMISXGikE6hKS6akQEoDr34ZXMRyqJCumP-gEDc0oqaSY-hdaFTKfcaiag==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTINEdZhbKmVlB8g22DoHdvVO3wjxoAVKBy210lcfZFyBVV0qcgbKQo-BxvxLBsgTsO-TmoF2FLuryLZw0TsVde6GkLhL-cWFbx-qyes3ZBpBr26w-f7tLojxsMzUS4zZrabqt2U3gJx5X5A3xg4ikSGR0Ui52yvn4QYLxkmdjwXgd65TrVEryTEudP-Gvk5MXKaq0pAzcvThJreR5psAwb8HVfYKLu0ImSHYvJFByHHsIYPcrtha6NkzlmQ==)
15. [tum.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz4MeAVLvqWLayqTPLcUxFZjprNqsml8SvxVoakiVvOiEt-EEWpqRktRaMBdpg8gelgqxHlbK7BrmHRIWg10ZrmKHW-DRUDHHRkawfnGkZqV5FXHY_kfQ16qlsZTnDy1zTHw8GFw6xiA==)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUTtoO5-wUsvp9gesy2xr2ezZsy1GhHFHGVq0MsKryOw50DkAOCEmfk4Yjk-Ghfe0yCOTSWgDz_JjXLYM6LvH3cUfW0KyaN749WreWnqWy8EkOPDEJuA==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYQz_9KJLvk7nGYxE6ygoufCO1AQxFGmKoldCWQItQWnc6CykVeCKb2Ulmc6hpQ3B4zDEWS86I-04nCq8T5ftH4Gh4CfbgQNclm3MjnhVr_Hwhm7EP5S6xgU_LZY-yoDQlmMnc-osiLDGFxfFiFxmwxQoSVcPnK2HHaCkV2mgoY1QTT8mwyXQaMpEJdjuCPNN2z4iPpyc49IrEwXlaxTDdK3sU0gNI5_7Uv8p3LMJk_lbPf_9DEDnVNaC79J9gEqJstslLv0lbYQ==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEP6bPXB68VF9AHNRzxy2wz0VINLaxOaJb33Y2osVs27ldvHXbxFaxQPj3sa8WXvlDPFz6vWwgjk_hm9qPRgBZIqq-Alax5lkpwSDlqhALAnbEVlDqPSILXew==)
19. [encyclopediaofmath.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV6X7cILjN5K3O6Tfb7zEhy2Hr1xIeQKmisKdj8NQw9PDSRLi0IxsjAet2LAZPHKT4DF0vsAgPZ5tV4ezcCGJoLEGCiPAvPMrfTtEhE3uws9iS3kxP-PXHodvFG8kiJrCUTxDmdkZTF4t9RtZP9SMTQTG8pQ4=)
20. [u-tokyo.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_MIVDRFhVe4WCFPUh6ltWJQxKv0t4JxcOByzNZ1aakmxb4kM7P7_zk98M4myYalMlRK8PD15xpqwDbV2Nfzry4GThUIh5dWRpeHc7U2oLcYSOwmiA0a-cmlXVAFEA9qA1BNoYXAtL183un5nT8T5P0H__lKWvenwRUy2XBA==)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9556mcyraUu9I_s7Kr3p6NLpHWc2KBy2YC8CbXQ-ETU47OfDQAF0vemf7JwdLeJIHYz_Zfv1GY-ix2yTBO2EoM5Ay1GQKCLyZ82Fy7VEO2w4Izbl5EVF1VH1289BzOUd33DEs0e1P8HBX6DYymN9UpVyTl9PQD6FiabYzjsJNVwKsgLZwxYKf0YZ9MtrfqHWuoh502JhcefdYH3yAHNt9a_LpvmV4P5JAUcYU9XD55n3PY4Nn-ZAaV0onAoPBUptMguE9sZBJbWqdCJVVsVo=)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiJG3DBOdDOm7Xdm_0kigqWZOR2_0Xl1UAIB-9ukKQmrBUmWGSKmpzs9rP5wsMvLAsTjbzGnDGQzCILYNkYxJpQyLKlxcW5aoUdsbJ-7d7OxkwkuBVHA==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1CsYk2rYjLrunCVBrp1vIzmbL80Jfbs6T54WxQVWWBZ95k5uloQQAhxKJkqafNxJVdI-Tr6ZwvrQR4j6DUBw0-MmKJYiM8aB2rmS5_iIlKUObSCfp7T4bYkzn2Sp0pVszi6Vfjc0ugsak1HUQ1abEi9v_rAbpZz5GpD4aUUD1ULMXtzdjENHqbr8eJYTX7btktOXfWtd06chfAmx3RXLHS68H2AAdTsOG)
24. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Xs423_wNMMN9KD7D9wlje0ogc9GUb_L9CHt7T9VFABjNJarMmeTyIDaHIh3gRifldNoy0T38NLnDALl0XTO0zLiZhJiHOwrmluqIV8mEIUgCG_AjPk3TL3a6-oSABSlJ)
25. [quantum-journal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtkQz8bY42q2GiiZwu9_HSmnOoP_7KovqPEbYa0rJEPu0I_JeofqIvmADej5cNSx6Tyu96NeUgEgzYRPTTUW7FU8HP1QbcgxEFiAAuHySrFJvOhV1luaU1xYoGdxTPgvc-KLm9mmYxMl5zWg==)
26. [iaea.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGizMYXtfbvgaHPaOUblEqZcTEOABBUWr1EX3vRbzq7YLjXT1C0xp9JELx2ZlsLFf0KqLF1cnIhjyW05Q2l2hbQlRQbxoofzcNG39NroFK9i8MCHPPawXMxItW17S1gLyAf-FvKs2n1DrKavszFfex32n27i6xf0UbHOP3oQFjI0jyuSx_c-WCpx-o=)
27. [scl.rs](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXjV_vfi5CkXba-PQj188SRUgPegBWBmr_iACN2h3PWKWWlC4UFJQcUgjtwxgM1qj49J1G4EUW6L2v8B-QdboRrXlygaFqdeGzNcFGXirkYL8yMQQdckD8PjKi1lw6KcOcmaSaX1vx1-Mk5-xDOUpbv4Mh)
28. [ethz.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErEU8ROlo3cYYGXmMZdrxRrFuTpprNE-ZIdKmTXuAciFk7_51q0xrpuQ5akf_14EcZlQUqr9UWCHK6Dv7S-lmn3Uac1-5wrUg-UljZodtHsVJ2eiA23oKsSTU9loUrhBqyomp6kw6O_xPDE5v42rrAsG2bYiaModmIcA1icUSv-e9Qt9UjLK08u1xaQCx_BIPVZcWaTyJdoTjj5fbIyYp2ZbK12w==)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2S5VCX2BaY1N2vG_bZAzZdldhSvprWb689WkDDdp5iH6bHdtwTuDCon1TWan6gzcNTF0tb9NFUQ2jmL-j-TE4Hg1GgglvIsdMeQ7r-vi8XMAQcZ6WQsTbnA==)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAtIoEnPBHmLxnrywdH1vS4-I0Pw2lmAvOkCpFOrLDnKWdLoaEebhltvc5UbOS275MlwGh6_zqhvRbEq-hsWqFRmKZAirK8P9jlKDohWwUthD47knj-uqHA-udW8iF_TVo2SllMuAShw==)
31. [mst.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbEQPkFkiZbXMLrzv1xKQsi-xa4cOv4wtCDfCI0KJA1cOZNgH3fSV3vKOrlfwaRz8i3u0a-ELiIN9xRyzrvNLLKAsJ6eOOBnUidvsac-wqcJIx5NfqWoaPRQVWToOSoXvduDbDV8TA82suNnj2GSV0zHlQSMv-Cg6WSjNfjckMLlf7mg6sZ3gwxTK-x99qzVb1pCqhmmSSsRYv4lObE70bC1JitpgkER66DvZ9e2gPDIInoAk3QjcB3G74)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNBng7X5lB_bJFwTk04JbY_xwHNuyhoxk5E2V05GJN-nbMlu96zEIEPqRY1bPDagtx4rmSYt6CUzRQUjK4-ZDDF9alkMVrGKdnO7fOIc9RBXWA_1Cj4A==)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSR5GRUkKsYARQAFvPQarpyu97FsiCkS-ubL6-niuv96CwxLG5x9i-WdoQCqv3e34aJATU5arvFMfutpEIj3l_UsJpxdngUUmWE46jZ-u20XW1oSh3qM-Jbg==)
34. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBsLvAHAfeO7nTLlOZdsp-476tAlOQtZGM70sW1LyoLAQyZY-NxVCJTxxLoM0eSMIl8Aun6DtGyhr55KpTVl3GnIFYtc33983NWINa5kiIPwCd2kCAqHqNV8B6122295z9zJodQC2SImvJqsB34J2uuMXSYaqSDx62dNwUFL9027vlBvg=)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhfEOlx9UsHWSRiNtVezxdaHtAT2k3__TfoWcXiuDVDKtmyv8nTC6Qc7iXs72HjG9YovfohqQZnF62gngbQNiSrCVO1qmeCnqcLqiLjYZzkzdffyuAJ8m7TfZa0ssoj02uG7nhoGxZDYmK2G2uCW4E57gA3Oyk5D1LIncvyG8LfThRUUo7bAQGvYeWtWot96S_GpweXZHNJuvGVWTXNWFaCJfEPv4=)
36. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYI1N9LwBxi2-rZSLHruPnGgPsO_x81G9pPZwZrdaW0AMzqAUjy7djqhPCXLUapu6P9hFhuXxBjpDfCGYQ7EytHsLz-y3SagMjHECULGS7F1knQADwb82KHA==)
37. [benasque.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw66vqJuyArtSns3aRWLJCkIjkUJoJS-nZEfsIW0lCwqSOyWaoQ2kKYR7DtVhXBJMC-3UApGbNNMph9fl7Qn13DvwmVrH34SxeCufaGr0KiSk-1JQuOZl_cYnzU-0uGDPNzmG9ReSFJ5ro_aN4p935KxjCQslSwypZGPE8KTE=)
38. [aps.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6MCnVxrV-KMworSPyb68az6jLmjj5aIxaDcJNsKupwVe4Wq8_Da9wZvVzNuAzqD4bcd8SiiHDEX065TOCTrGZ6IpeSj4H22E9AJV9Q9XJpO0HRyOtg-HSZo8TQuCnLi1T)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJGUQyWhTz01XhkkixABsZz1Hkdl-jqckSCTJC5vszsbtqfNRlbPt1Qnak4EKgF8WPQ7-S6xAuJYG7mbbdMj8iDP_96qnloNJ226HjgAKFEJdQwtG2e96e_3d77ml50nol_jYurMeeFmeW4vdLtBYDLfBch1W__mHhkfW5ceWwDvuvqq4Cqd8TqKVEgOtCrsCCib7F5WO2lVtqMabFIdgnMFn_j0tvdmNYNMbQO2rXBSgshmiPboW7nHziZg==)
40. [Current time information in City of Gold Coast, AU.](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi6tJ7xO3Fw0aFnO5vysPag5C1WWIg-85yMHQDZzoNnYVnOWRE7fVsRkU1EOncc38bfzbarKjD57n3X80mv5rLERu7Ocd1x7FllLZmWogJNfuTZLszuAKxS-SADhfuh9uEeJb5eVwUXfAu5CFpBUiZlgBXhw==)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2CWupVMwcmEtFXcvG8sSEGC30b_va_NiHmW9tFFVsi0xFw9thgi40T9jS_gtwT1z1MSdzv6m1PXApnESkSfLIPgqbauiJTEVkVPyrojZSfIUOZRusE4bDS96Dbras1lWee7Qwi8BHlq32LTPPgeA_qA1ELu2WG-ws6Sc6by3cTqUHoaPAB0Qv3ODBa7Zs4WU-T2iMpxpAWhsLkSeRDRYnbhFkIL_WxytbXp3PluHZDLcw4rggubVZJiWS)
42. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI1CJdN6Cbmh0iIa-vewGz2y5gEUXpyA5hlaEZcGZKRgZe8Ep5t2GM-5wBeo43FKNPXEX9n5iBswxZ59VFbKKaYOfy4eEk-5Dx5riHz-vqhH8J-uAtTJLNw5xhpFw-xPKg5c6implf7LNGh6HFPnC9YH6xmZWGiSJUas_7SFG-AbTANNLqI47GA54PXRdHpdRLsvoC8BH_171NfJ_yuZn23Z3pxkhSa5MAigO-We2Rxm-Z)
43. [cbpf.br](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrGfRT1yGBXGu4qkCpat2MEqZ_AERhOuq3saknZEiaL4tiNSBRqDJ1gdWAq2q0oGyvcuoI185xr5sAmdU65cCm5TSvjNljNwjgcKM9ZcaSCBBQRCqA5Njdvbabexb52w9DuyKHN8GPKWu2dzS-OK-O8GazIEodYU7L8TiX-wmrVbqKuvsamiGTfLTnVuPnhRKWPbceZYAFmwc5phw=)
44. [sigma-journal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1rnNh1DFBLSwsLTEKSJ2Tn7G_NXGlW6zwxPna9O5GYV3_Vis3O-llwl-swrxG1jsPAJWm-2ZEWlY5AuzPBz_kBLZVDMbFHIPAL55v4bjh8J1dY1YPHLge8rn9qJIrd7Hb_GNZ-LJP0w==)
45. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbalX8XpZWXegzfDcjweHGOdXCJ5p-o2PasWCUiG7f8B_IzfA11m3yPXTf5r_szv1gBE6lxrHKsKzoIUksz_Wo-jRJdYvWaj699eh4l1k0t5LT7vEVtFlYYQ==)
46. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPATe-fhCboQw1ga2y7VEkivbg_ntcbcpe1B5bYhPQJlBA70uRvnTJBGmA1WHXf2lV3fWMhHecyAV4A8zx--5o3cmXmmF8PkT4rn9NWxLmSzjUGdKU_FfBX3r2OV9I9E75mzrG_A0=)
47. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAK4GxIjqd6mMM9M2qN818TZczUZsErxeJJ3vej_evw8GSDFVsGZZrBYD9QpJMNfOqOTdptZDdfjTfxtJi_V53UEy18l_0Onog4bLGzro00VKLzWyHtnoVJGOjz-7GTqp5FMbN-xadwp4_FoNfk5Sho67zjPByRDrEKc16DQnQ-0Ed20d3LhVSfePhZE4n8gzkfVRGpZ5voEv-Qwl33kPnRKRY_B1qd5Mh)
48. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED0IKgW-2Mg2KOf5KKrt0VXDqCicbv43ePH7S3DApywjVQ5d1VyuDYXKWHJp9_6-fqnzvxO7_O0UYO3P0i73-Udnx_2MLRkNVGR_BBnhWIcnYvDjLznIxDrdgECbUV0_-sj4DV914=)
49. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxT6yipfjj0Tepta8fa0vemEz7AG9UyAU4kN8e5UT-J2xB3iGWn2vy3PhaZN0iBxWtW8vV2sOJPkkyre7m6Wi61n96BIgFjuyXUN-dgi5KGx7XXuumJt84ypO3pRLUh4rOdC5goNovxAAO7Ew-QQ7JgyadW1hzuX131W6nRBhS4_ePKErDty4qhmqDM3PX1hjIDbfoZD5r-8hOmw==)
50. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3fvj-ehaR86IcR0MtkQDPctbpI05JMavA6fZ-lQKDa47WZKGms9FZqbqgrmFtZL2-pvJQEipA2VaqdcVFRGdQV8trEyHq2vvpY7fjFCnMMTz5r-a-Dobbflb95zzoHBoGKPRVikCcZXa244vICPdSqvG_CvNFFKG8yaHm71u7YMF3QZJM1S1KIFv_84xf3gqRa6gGGJBx5ab4xOZyCQtoSjdi1VY_kG4kTCGyrTfa_C6u_CUx170HX4Jkgu1MpX09iIzH9Y=)
51. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxKpCe7q-1Req8oC20kFTpIOkkGJLe0wl-F24inii0bLv6Nos9J3eHx8p-GpEk3xY58fpi8LE7mUJKlqnYRrWNJC9BEVrjm_ewc_7XSusmOOtHPzeCJR5NDn3OqIvv6_anClN-QQA2Rw2McGqVBACU74Darq36rHdsbB6H3lp8Wt-KinsZLNyAUDPFm4B4nuvYw2HbAnvZRD15skpzMjuFm3MAQa9asKwKdYRLWMD0J54T8EyXzmn5TV9zkMxfoss=)
52. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdSnNi8jc2Nd74VrguxZAd5Z0nHLI8KTb47clXuYXDqYma7QOPiKareNPkOBhSS3oXVmpPyVVrvGL4e83DQCypMdj6IhQlaLzjiXTEl-j2TkrxYmDHQ2lF_5x4qFJoohcDclrSUeMRi9ySQIzrHwMvkEyTNhdlCO0NBV9C16Xu-RU3xyHb1fXTK-Oc)
53. [colab.ws](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH72TE0PJK5Aa6rLYhPZlkOpsZpKbNoxwKxW6e4i_0iSzS2on2oHqljsK9-tp-ODarvDoX7NEFNGWpzCiVTcSUzsJd_qEGHjRXSVGGgxTAx--TNo-EziqABZJ5i-CmsvQjvogpwjdOtdfYMXJvnwmWUAD6i)
54. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJeZ6aukf_EfBbmhY3bXmZFBM14SFscTOiCVHAVIzUSp2JutGcVpat7nwRbmTPcttr31BsH5DI-sYxAgCK-IXItOzttQ_1bwhoIy91p5Jwx04OLlUdzB44YMK8gtYHc_wctRErNKoYa_Xe)
55. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPzKbRwuVEa90qkSHWfEonBgqYYL7qN3aNEPJARhpj-FqqLC_h8sqKsAflM34emrKt0YECpKHZdDIoVxxzkDzfl55tA8pwkT1_ZvBbBvpgfC1iME1t5gGcU6KIcQ33tq_7pNx8RBw5Sk79Zz7k48uwpn8vVOe6ryLgJWA8jYVegKEahNY=)
56. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfQs-T9VkaE9694YSo41Zas87t_dByC-Ya81iEvUZUoyIOHY52qT1bP3uX7NBQdQzlu9rGdpX6zCQHUi7FkviKuQDPrIZr9-8uPFngjKsG75Vzb7kQVrQ=)
57. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6jlpRp1ykGwep9bIdVFLM_55Aadefgx6HXPOwRMv0_V7GvKfYY8txGAz7KVvn-GPu156JvS8fFdcnc0chH68WPA_QxjTyHz96Wr0hryKt6UDmoax9_8lptK41Mi2pkl34tKT_ZRbnEW_tykMj8EERTFZbf1JXtAz8Fxs3GW_YGg0z7sk=)
58. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8B_Ws7C0DjuzJdwpge7sMMP3HEoiyDECwfYi2P7fpmixfI1JGeVRPOgZ5vqyoRvkSRnKVETBlRRS759PXjUzqleI3sADSNWE_AzCfKMfMObXl1zZL506ecE-X_asVGC99KKKOPll3OXAmQH8=)
59. [bohrium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZrwD_thVr1Qv8i5QmvPy0OmqoLTGRmV_qmt9H2S1_or8fQ77N39zTT-QshuOsW9LS2Yv-uLV7CdlSM797TLoZacpodPCvoj7wI-WnUeByljos8rbLYHfcHG5xCdqv5pBjbLdqdBUzdBfqoqI9y6P4HDPUe_Xq4wAWQEW1LOSDbZZJ_OIeMFtgYZ_PAZII63dg4OQAgyvRrajIkIlC-3MW_P94HIyzZtUk1MNgX1UIMZUJej8PvtjDql2r5itPyg==)
60. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFHgAqfigNdQMPf6h4LfVRxGbeTDSHloogtj2RkEdPUTfZxjcBRmsi6sl9EKgGWpTZlIJI8gXdbGhh_HHKr-mYBHIACHGJ1wlgSK-8wvbX77aymzOzIrBSrJnhBvnVJvaeKoFWZxTG1e6yoBIwN_HfUIfk6-bwfop_ESvdODt5fJxtO2qLydFH-BlGxsGMfV7HnJSFHN39uih8ZTM6KjOdpl_b69rBFQjhog==)
61. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHznh88VvrfTG12pS0tF3kD7eHgnqLTGDZhKw6YVY1qWyGveRiZAmjEl8Z-Fgo5qCzmrT6IVaXsUmB-MSkDIZpNNS6ge6l0pUI60B74O9EGnuULNg0I8N5P7g7BMbwi-1aMxSRaBUbwdvzoUTF9aHlUzs2rQiSC3yEX9hrDqlPTIKWZJ6xbZM-DMbmBOmbxmauGJ-SQm0diR8B2TQ==)
62. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0nphkHeI3Mq4fYTSuFhtjZckuWJxr1hxaZaDsKD-NFgPft6fLfBw0lza1_C4dMytrihQi07Ml9soG1-VYd5MiuJHIQsl12hKyTTWVDD34yoj_7nyMZ87vtzswB6PvAlJQh3vXOATbDvc0PaFlOua2an62mzk_jeGb7EY5mdMVku_7sk=)
