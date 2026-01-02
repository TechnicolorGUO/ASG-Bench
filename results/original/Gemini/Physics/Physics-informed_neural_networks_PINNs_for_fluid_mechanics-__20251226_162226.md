# Literature Review: Physics-informed neural networks (PINNs) for fluid mechanics- a review.

*Generated on: 2025-12-26 16:22:26*
*Progress: [19/21]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Physics-informed_neural_networks_PINNs_for_fluid_mechanics-__20251226_162226.md*
---

# Physics-Informed Neural Networks (PINNs) for Fluid Mechanics: A Review

**Key Points**
*   **Paradigm Shift:** PINNs represent a convergence of deep learning and classical computational fluid dynamics (CFD), embedding physical laws (Navier-Stokes equations) directly into the loss function of neural networks.
*   **Inverse Problem Dominance:** While PINNs can solve forward problems (simulation), their most distinct advantage lies in inverse problems—inferring hidden fluid properties (e.g., viscosity, pressure fields) from sparse, noisy observational data.
*   **Current Limitations:** Despite success in laminar flows, standard PINNs struggle with high-frequency phenomena (turbulence), stiff gradients (boundary layers), and chaotic dynamics due to "spectral bias" and optimization difficulties.
*   **State-of-the-Art Solutions:** Recent innovations such as Causal Training, Domain Decomposition (XPINNs), and Fourier Feature embeddings are addressing these limitations, pushing PINNs toward industrial applicability in fields like hemodynamics and aerodynamics.

---

## Abstract

The integration of deep learning with physical laws has emerged as a transformative approach in computational science. Physics-Informed Neural Networks (PINNs) constitute a class of deep learning algorithms capable of solving forward and inverse problems involving partial differential equations (PDEs) by embedding the governing physical laws into the network's objective function. This review provides a comprehensive analysis of PINNs within the specific domain of fluid mechanics. We examine the foundational architectures, mathematical formulations, and the historical trajectory from simple laminar flow solvers to complex turbulence modeling. The review critically assesses state-of-the-art techniques designed to mitigate spectral bias and optimization stiffness, including domain decomposition (cPINNs, XPINNs), causal training strategies, and hard-constraint enforcement. Furthermore, we explore diverse applications ranging from hemodynamic super-resolution to high-Reynolds-number aerodynamic flows. Finally, we identify persistent challenges regarding computational efficiency and convergence in chaotic regimes, outlining future research directions for hybridizing PINNs with traditional solvers and neural operators.

## 1. Introduction

Fluid mechanics, governed by the nonlinear and coupled Navier-Stokes equations, presents some of the most challenging problems in classical physics and engineering. Traditional Computational Fluid Dynamics (CFD) relies on mesh-based numerical methods—such as Finite Difference (FDM), Finite Volume (FVM), and Finite Element Methods (FEM)—to discretize the spatial and temporal domains [cite: 1, 2]. While these methods have achieved high fidelity, they face significant limitations: they are computationally expensive for high-dimensional problems, require laborious mesh generation for complex geometries, and struggle to seamlessly integrate noisy observational data for inverse problems [cite: 3, 4, 5].

In recent years, Scientific Machine Learning (SciML) has emerged as a paradigm to bridge the gap between data-driven models and physical principles. Among these, Physics-Informed Neural Networks (PINNs), introduced in the seminal work by Raissi et al. (2019), have garnered intense interest [cite: 3]. Unlike purely data-driven approaches that require massive labeled datasets, PINNs leverage the governing differential equations as a regularization mechanism, allowing them to learn from sparse data or, in forward problems, from no labeled data at all [cite: 6, 7].

The motivation for applying PINNs to fluid mechanics is threefold. First, PINNs offer a mesh-free alternative, potentially circumventing the difficulties of grid generation in complex domains [cite: 6]. Second, they excel at inverse modeling, enabling the reconstruction of flow fields and the estimation of unknown parameters (e.g., Reynolds number, viscosity) directly from sparse measurements [cite: 4, 8]. Third, they provide a unified framework for data assimilation, blending experimental results (e.g., PIV, MRI) with physical laws to enhance resolution and accuracy [cite: 9, 10].

## 2. Key Concepts and Definitions

### 2.1 The PINN Architecture
A PINN is a deep neural network, typically a Multi-Layer Perceptron (MLP), that approximates the solution variables of a PDE. In the context of fluid mechanics, the network takes spatiotemporal coordinates $(x, y, z, t)$ as inputs and outputs the flow variables, such as velocity components $(u, v, w)$ and pressure $(p)$ [cite: 3].

The defining characteristic of a PINN is its composite loss function, $L(\theta)$, which is minimized during training:
\[ L(\theta) = w_{data}L_{data} + w_{PDE}L_{PDE} + w_{BC}L_{BC} \]
where:
*   **$L_{data}$:** Measures the discrepancy between network predictions and observed data (if available).
*   **$L_{PDE}$ (Physics Loss):** Measures the residual of the governing equations (e.g., Navier-Stokes). If the network output satisfies the physics, this term should be zero.
*   **$L_{BC}$:** Enforces boundary and initial conditions.
*   **$w$:** Weighting coefficients to balance the loss terms [cite: 3, 6].

### 2.2 Automatic Differentiation
Unlike traditional mesh-based methods that approximate derivatives using truncation errors (e.g., Taylor series expansions), PINNs utilize Automatic Differentiation (AD). AD leverages the chain rule to compute exact derivatives of the network outputs with respect to inputs (space and time) to machine precision [cite: 3]. This allows the PDE residuals to be evaluated directly on a set of scattered "collocation points" without a fixed grid.

### 2.3 Navier-Stokes Formulation
For an incompressible flow, the PINN minimizes the residuals of the momentum and continuity equations. For a 2D flow, the residuals $f$ (physics loss) are defined as:
\[ f_u = \frac{\partial u}{\partial t} + (u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y}) + \frac{\partial p}{\partial x} - \nu (\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}) \]
\[ f_v = \frac{\partial v}{\partial t} + (u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y}) + \frac{\partial p}{\partial y} - \nu (\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2}) \]
\[ f_{mass} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} \]
The network is trained to minimize the mean squared error of these residuals over the domain [cite: 3, 6].

## 3. Historical Development and Milestones

### 3.1 Pre-Deep Learning Era
The concept of using neural networks to solve differential equations dates back to the 1990s. Lagaris et al. (1998) proposed using shallow neural networks to solve ODEs and PDEs by constructing trial solutions that satisfied boundary conditions by design [cite: 11]. However, limited computational power and the lack of sophisticated optimization algorithms (like Adam) restricted these early attempts to simple problems.

### 3.2 The PINN Breakthrough (2017-2019)
The modern era of physics-informed learning began with Raissi, Perdikaris, and Karniadakis (2019), who formalized the PINN framework [cite: 3]. They demonstrated the method's ability to solve the Navier-Stokes equations for laminar wake flows and introduced the concept of "hidden fluid mechanics," where scalar transport data (e.g., dye concentration) could be used to infer velocity and pressure fields without direct flow measurements [cite: 3, 12].

### 3.3 Expansion into Turbulence and Complexity (2020-Present)
Following the foundational work, research shifted toward addressing the limitations of vanilla PINNs. Key milestones include:
*   **2020:** Introduction of Domain Decomposition methods (cPINNs, XPINNs) to handle multi-scale problems [cite: 13, 14].
*   **2021:** Identification of "spectral bias" in PINNs and the introduction of Fourier feature embeddings to resolve high-frequency flow features [cite: 15, 16].
*   **2022:** Development of "Causal PINNs" to address the violation of temporal causality in transient flow simulations [cite: 17, 18].
*   **2024-2025:** Application of PINNs to fully turbulent flows (DNS/LES scales) using advanced architectures like "PirateNet" and self-adaptive loss weighting [cite: 19].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Domain Decomposition: cPINNs and XPINNs
Standard PINNs struggle with large domains or multi-scale physics due to the complexity of the optimization landscape. To address this, domain decomposition techniques have been introduced:
*   **Conservative PINNs (cPINNs):** Tailored for conservation laws, cPINNs divide the domain into sub-regions and enforce flux continuity across interfaces. This is particularly useful for flows with shocks [cite: 13, 20].
*   **Extended PINNs (XPINNs):** A generalized framework that allows arbitrary domain decomposition (space and time). Each subdomain employs a separate neural network, allowing for different hyperparameters (depth, width, activation) based on the local complexity of the flow. This enables parallelization and improves representation capacity for complex geometries [cite: 13, 14, 21].

### 4.2 Mitigating Spectral Bias
Neural networks inherently suffer from "spectral bias," meaning they learn low-frequency functions quickly but struggle to capture high-frequency details [cite: 16, 22]. In fluid mechanics, this leads to poor performance in turbulent or multi-scale flows.
*   **Fourier Features:** Mapping input coordinates to a higher-dimensional Fourier space (using sine and cosine functions) before passing them to the network allows PINNs to learn high-frequency modes effectively [cite: 15, 23, 24].
*   **Rowdy Activation Functions:** Jagtap et al. proposed adaptive activation functions with sinusoidal fluctuations (Rowdy topology) to prevent saturation and accelerate convergence in optimization [cite: 25].

### 4.3 Causal Training for Transient Flows
In time-dependent problems, standard PINNs treat the entire space-time domain simultaneously. This violates the principle of causality, as the network might minimize errors at late times before resolving the early evolution. Wang et al. (2022) introduced a causal training formulation that modifies the loss function to strictly enforce temporal causality, significantly improving accuracy for chaotic systems like the Kuramoto-Sivashinsky and Navier-Stokes equations [cite: 17, 18, 26].

### 4.4 Hard Constraints and Distance Functions
Vanilla PINNs enforce boundary conditions (BCs) as "soft constraints" (penalty terms in the loss function). This leads to a competition between the PDE loss and the BC loss. "Hard constraint" methods construct the network output ansatz such that BCs are satisfied by construction. For complex geometries, distance functions (calculated via Eikonal equations or R-functions) are used to smoothly blend boundary values into the domain, ensuring exact BC satisfaction and leaving the optimizer to focus solely on the PDE residual [cite: 27, 28, 29].

### 4.5 Operator Learning (DeepONet and FNO)
While PINNs solve a specific instance of a PDE, Neural Operators learn the mapping between infinite-dimensional function spaces (e.g., mapping an initial condition function to a solution function).
*   **Fourier Neural Operators (FNO):** Use Fourier transforms to perform convolution in the frequency domain, offering mesh-invariant resolution and faster inference than PINNs for families of PDEs [cite: 30, 31, 32].
*   **DeepONet:** Uses a "branch" and "trunk" network architecture to learn operators. Physics-Informed DeepONets combine the data-driven operator learning with physical constraints [cite: 33, 34].

## 5. Applications and Case Studies

### 5.1 Inverse Problems and Hidden Fluid Mechanics
The most successful application of PINNs is in inverse problems. Raissi et al. demonstrated "Hidden Fluid Mechanics" (HFM), where the network infers velocity and pressure fields solely from visualizations of a passive scalar (dye) concentration, governed by the advection-diffusion equation [cite: 12]. This capability has been extended to estimate unknown rheological parameters (e.g., viscosity) and boundary conditions in experimental setups where only sparse velocity data is available [cite: 8, 35].

### 5.2 Turbulence Modeling
Simulating turbulence remains a frontier for PINNs.
*   **RANS-PINNs:** PINNs have been successfully used to solve Reynolds-Averaged Navier-Stokes (RANS) equations. By embedding turbulence closure models (like $k-\epsilon$ or $k-\omega$) into the PINN, researchers have improved the prediction of Reynolds stresses using sparse data [cite: 11, 36].
*   **DNS-scale Modeling:** Recent work (2025) using the "PirateNet" architecture has demonstrated the ability to simulate fully turbulent flows (e.g., Taylor-Green vortex, turbulent channel flow) without turbulence models, reproducing energy spectra and enstrophy peaks consistent with Direct Numerical Simulation (DNS) [cite: 19].

### 5.3 Hemodynamics and Biomedical Engineering
PINNs are revolutionizing cardiovascular modeling by integrating sparse medical imaging data (e.g., 4D Flow MRI) with fluid physics.
*   **Super-Resolution:** 4D Flow MRI often suffers from low spatiotemporal resolution. PINNs act as a super-resolution tool, upsampling the data while ensuring the high-resolution fields satisfy mass and momentum conservation [cite: 10, 37, 38].
*   **Aneurysm Analysis:** PINNs have been used to estimate Wall Shear Stress (WSS)—a critical biomarker for aneurysm rupture—from sparse velocity measurements, achieving high accuracy even with uncertain boundary conditions [cite: 39, 40, 41].

### 5.4 Multiphase and High-Speed Flows
*   **Multiphase Flows:** PINNs have been applied to solve the Cahn-Hilliard and Navier-Stokes equations for two-phase flows (e.g., bubble dynamics), successfully capturing interface tracking with errors below 1-5% compared to traditional CFD [cite: 42].
*   **High-Speed Flows:** For transonic and supersonic flows, PINNs must capture shocks (discontinuities). Methods using adaptive sampling and specific loss weightings have been developed to resolve sharp gradients in compressible Euler and Navier-Stokes equations [cite: 4, 43].

## 6. Challenges and Open Problems

### 6.1 Optimization Stiffness and Convergence
The loss landscape of PINNs is notoriously non-convex and "stiff," meaning the gradients of different loss terms (PDE vs. BCs) can vary by orders of magnitude. This leads to unbalanced back-propagation, where the optimizer prioritizes one term over others, often resulting in convergence to trivial or non-physical solutions [cite: 44, 45, 46]. While adaptive weighting algorithms (e.g., GradNorm) help, robust convergence for complex 3D flows remains a challenge.

### 6.2 Computational Cost (Training vs. Inference)
For forward problems, PINNs are generally orders of magnitude slower to train than running a traditional CFD solver (FVM/FEM) for a single instance [cite: 47, 48]. The advantage of PINNs appears primarily in inverse problems or when the trained network is used as a surrogate model for rapid re-evaluation (though Neural Operators are often better for the latter) [cite: 30, 49].

### 6.3 Spectral Bias in Turbulence
Despite improvements with Fourier features, capturing the full energy cascade of high-Reynolds-number turbulence is difficult. PINNs tend to smooth out high-frequency fluctuations, acting numerically diffusive [cite: 50, 51]. Capturing the "inertial subrange" of turbulence requires massive networks and specialized architectures that are computationally expensive to train.

### 6.4 Extrapolation and Generalization
Standard PINNs do not generalize; a network trained on one set of boundary conditions must be retrained if those conditions change. While operator learning (DeepONet/FNO) addresses this, "vanilla" PINNs are limited to the specific instance they were trained on [cite: 34, 49].

## 7. Future Research Directions

### 7.1 Hybrid Solvers
The future likely lies in hybridizing PINNs with traditional numerical methods. For example, using a coarse CFD solver to generate a low-fidelity solution that initializes a PINN, or using PINNs to correct the errors of a RANS solver (turbulence closure modeling) [cite: 2, 52].

### 7.2 Second-Order Optimization
Moving beyond first-order optimizers (Adam/L-BFGS) to second-order methods (e.g., NysNewton-CG) could resolve the stiffness issues in the PINN loss landscape, enabling faster and more accurate convergence for stiff PDEs [cite: 53, 54].

### 7.3 Foundation Models for Physics
Leveraging the "pre-training + fine-tuning" paradigm seen in NLP, future research may focus on developing large-scale "foundation models" for fluid dynamics—networks pre-trained on vast amounts of CFD data and physical laws that can be rapidly fine-tuned for specific engineering problems [cite: 49, 55].

### 7.4 Standardized Benchmarking
The field currently lacks a unified, rigorous benchmark suite for comparing PINN variants against high-order CFD methods. Establishing standard datasets (e.g., turbulent channel flow, flow over a cylinder) with strict error metrics is crucial for maturing the field [cite: 8, 19].

## 8. Conclusion

Physics-Informed Neural Networks have established themselves as a powerful paradigm in fluid mechanics, offering a unique capability to blend data and physics. While they are not yet a replacement for traditional CFD in standard forward simulations due to computational costs and optimization challenges, they are transformative for inverse problems, data assimilation, and surrogate modeling. With the advent of advanced architectures like XPINNs, causal training, and operator learning, PINNs are progressively overcoming their initial limitations, paving the way for real-time, high-fidelity digital twins in aerospace, biomedical, and industrial engineering.

## References

*   **[cite: 3]** Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *Journal of Computational Physics*, 378, 686-707.
*   **[cite: 8]** New, A., et al. (2024). Equation identification for fluid flows via physics-informed neural networks. *arXiv preprint arXiv:2408.17271*.
*   **[cite: 56]** Cai, S., et al. (2021). Physics-informed neural networks (PINNs) for fluid mechanics: A review. *Acta Mechanica Sinica*, 37, 1727-1738.
*   **[cite: 57]** Sun, Y., et al. (2024). Recent advances on machine learning for computational fluid dynamics: A survey. *arXiv:2408.12171*.
*   **[cite: 1]** Sharma, P., et al. (2023). A Review of Physics-Informed Machine Learning in Fluid Mechanics. *Energies*, 16(5), 2343.
*   **[cite: 4]** Cai, S., Mao, Z., Wang, Z., Yin, M., & Karniadakis, G. E. (2021). Physics-informed neural networks (PINNs) for fluid mechanics: a review. *Acta Mechanica Sinica*.
*   **[cite: 58]** Wang, Y., et al. (2024). Multi-scale physics-informed neural networks for solving high Reynolds number boundary layer flows based on matched asymptotic expansions. *Theoretical and Applied Mechanics Letters*.
*   **[cite: 43]** Ren, X., et al. (2024). Physics-informed neural networks for transonic flow around a cylinder with high Reynolds number. *Physics of Fluids*.
*   **[cite: 59]** Eivazi, H., et al. (2022). Physics-informed neural networks for solving Reynolds-averaged Navier–Stokes equations. *Physics of Fluids*, 34(7).
*   **[cite: 6]** Gupta, D. (2024). Solving the Navier-Stokes Equations with Physics-Informed Neural Networks (PINNs). *Medium*.
*   **[cite: 42]** Punyatirta. (2025). Comparing Neural Network and Numerical Method to Solve Multiphase Flow Problem: A Review. *Medium*.
*   **[cite: 36]** Kumar, S., et al. (2025). A physics-informed neural network for turbulent wake simulation behind wind turbines. *Physics of Fluids*, 37(1).
*   **[cite: 2]** Luo, S., et al. (2020). Parameter Identification of RANS Turbulence Model Using Physics-Embedded Neural Network. *ISC Workshops*.
*   **[cite: 11]** Pioch, F., et al. (2023). Physics-Informed Neural Networks for RANS Turbulence Modeling. *Fluids*, 8(2).
*   **[cite: 13]** Jagtap, A. D., & Karniadakis, G. E. (2020). Extended Physics-Informed Neural Networks (XPINNs): A Generalized Space-Time Domain Decomposition Based Deep Learning Framework. *Communications in Computational Physics*.
*   **[cite: 20]** Shukla, K., Jagtap, A. D., & Karniadakis, G. E. (2021). Parallel Physics-Informed Neural Networks via Domain Decomposition. *Journal of Computational Physics*.
*   **[cite: 33]** Goswami, S., et al. (2022). Physics-Informed Deep Neural Operator Networks. *arXiv preprint*.
*   **[cite: 34]** Lu, L., et al. (2021). Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators. *Nature Machine Intelligence*.
*   **[cite: 27]** Liu, Y., et al. (2025). Hybrid Boundary Physics-Informed Neural Networks for Solving Navier-Stokes Equations with Complex Boundary. *ResearchGate*.
*   **[cite: 28]** Liu, Y., et al. (2024). Physics-Informed Neural Networks with Complementary Soft and Hard Constraints. *arXiv preprint arXiv:2411.08122*.
*   **[cite: 29]** Sun, L., et al. (2024). Physics-Informed Neural Networks with Hard Constraints for Inverse Design. *Applied Sciences*, 14(2).
*   **[cite: 23]** Sallam, O., & Fürth, M. (2023). On the use of Fourier Features-Physics Informed Neural Networks (FF-PINN) for forward and inverse fluid mechanics problems. *Proceedings of the Institution of Mechanical Engineers*.
*   **[cite: 15]** Wang, S., et al. (2021). On the eigenvector bias of Fourier feature networks: From regression to solving multi-scale PDEs with physics-informed neural networks. *Computer Methods in Applied Mechanics and Engineering*.
*   **[cite: 30]** Li, Z., et al. (2021). Fourier Neural Operator for Parametric Partial Differential Equations. *ICLR*.
*   **[cite: 25]** Jagtap, A. D., et al. (2022). Rowdy Activation Functions for Deep Learning. *arXiv preprint*.
*   **[cite: 12]** Raissi, M., et al. (2020). Hidden Fluid Mechanics: Learning Velocity and Pressure Fields from Flow Visualizations. *Science*.
*   **[cite: 50]** Chuang, P. Y., & Barba, L. A. (2023). Predictive Limitations of Physics-Informed Neural Networks in Vortex Shedding. *Fluids*.
*   **[cite: 17]** Wang, S., Sankaran, S., & Perdikaris, P. (2022). Respecting causality is all you need for training physics-informed neural networks. *Journal of Computational Physics*.
*   **[cite: 19]** Wang, S., et al. (2025). Continuous simulation of fully developed turbulence with physics-informed neural networks. *arXiv preprint arXiv:2507.08972*.
*   **[cite: 60]** Zhang, Y., et al. (2025). Physics-informed neural networks for hemodynamics: A review. *Engineering Applications of Artificial Intelligence*.
*   **[cite: 44]** Rathore, P., et al. (2024). Challenges in Training PINNs: A Loss Landscape Perspective. *ICML*.
*   **[cite: 10]** Shitole, V., et al. (2024). PI-GNN: Physics-Informed Graph Neural Network for Super-Resolution of 4D Flow MRI. *IEEE*.
*   **[cite: 39]** Fierro, F., et al. (2022). Estimation of hemodynamics in an intracranial aneurysm using PINNs. *ResearchGate*.
*   **[cite: 61]** Lu, L., et al. (2021). DeepXDE: A Deep Learning Library for Solving Differential Equations. *SIAM Review*.
*   **[cite: 46]** Wang, S., et al. (2021). Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks. *SIAM Journal on Scientific Computing*.

**Sources:**
1. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8igxul_TQHLAfDhkfpVwSGTIxwacDNF1i9R0OzGj5TTBGxLfDcz1FbbZ5cpkTuJunGAcmom5vjR1geDDJ7RZ2Ti4XH1k8s4I87KhtUD-idpghuSyWJZWEh56DOy6caYNewxRKgbrpBy2YixpbDQ==)
2. [illinois.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdUEYRrw5WKBJ8E4wxFvMrIK3CMi1BwP3vPrsPunhtn90n7QSJ1NyGEEA_S8Wlh87f9z1Dq5PZMFYJ1-bqtTz9KVs9Fuu32hprPtVa0sx9KTEAcZp3esfo9yyEAwdA-Hf-wdirR-UdzJREqmbeVoL3QWcklAYGCDygF-0CpJ77qsbg6ig=)
3. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98zf1_MWhNQLwzbumtoPO1qSOBWzOpPjtjaFoyOeQ3rTnzE_Tw6lXLfqDBP-C85bJ3K3dfFcqTnSoTFAvJuTEAkKVso-Od2RE74h9xuvulMVADi5JiEiPSGZlaDNrw8Xx)
4. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF66m4kJwPAfEX9FqCU8IywCx7Xeb93-Es2o-tBAtE9kQ4avRQVuJ-qXpbSlGOgiysWkXkGAHOG4DuvSQayG6iETigxlnNYuy6vTYQDrZ0Q9Rf5mXVwMDJtcLB-gll-aDMvjU1gxPi1eUbiq9jKXIAZqieNb3UDKNn1PIK__f7JOLdJdsupzjthj2OaW-r4eFGrj6Mxwh3u8pnfYlrH1qVtuzuBKwB3ANQCZOG3lYNIHC9tLUU2dh3Df8MC1jy3TXQ=)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_qTG1UEfnUdJclHPBrfx5fsHZG4UFh0tXDfT9iV9IDby-OLbyQAIq_51xXjWauETSpbqlAFClQP25wEUafOSCKhHZvuwhIesrpaxiNFISU6vTdPB32g==)
6. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYUyvb9zmmjUxH_OPWAP1bjd9qz2Lg2J9f5RKhxCaUmRE1G9wL7Ooijs9ujVVuIWS4H0Y4kIfn_QJOHUBTWAvOaGlFfyC3Ok5Ws_RSlUvkC2NySxN4ohAqmlDGWKZBFGjkyfqKgN3DCrFN4jS2pVL6dB6_kIyCg390h1ZqVW0rdMfSek8aZHYR5YwwFgIAWpLlBuxfIXIoQm7GZDuI5XhupLcpXIP0jcQEns924gt1vzNElLvIh43FQ==)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTal2kGtE9TVRcPbRmD8mTKaOW3hEBKB5qNVHyv1wxrHvYBfOvtV_a-wnXd7Xjp9f6kpn-947LnoXWyUayCpk3cglsbRrBVWrH8s_eBLzn37zcPcKr95lySg==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBEcurhC6HYaAldeOAk82J7plczhexs-ZAxUqeQwJR5C9P6gcy2iDQQhGkEzbk6jEtT5eY3B-nKdEjAlugJ5Qah76jKkjgPTznQcBWT86Ot92AFc9nUw==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtJPo37nzYrNyOcu8NGTavSGSuZf3sZWdHygLIpEZVIAtZ-b-zZIUlnOLP3soYkF9xOzxHkIc2fbooDOzlwL-X55LtMOTeeHvj61HkgtOnuF1aw54sK0fKfk3ox3xQ9VVmZ2k3ZfXq)
10. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2a5Qj8bxGkjLNHEcRTOVYMzXXfak88ZtSr2J69lfzyNbSdRYO9ksf955MhMlwcjc_G8UP-at33VCujrbP5LCx3OfsioywRenKqP0IYxKVaRqMY-92Uhm9TP2C0ATkmTDFFuLD)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_ix_TAEtP5wNQS5e1rjZbqnBMCKX-rSLQMGAKGQ14GpYTSNw3ULS6gaOwkkMzS7gYIAI7Axcfat9z62f954UgJ4qqnFsCva0uw1N6oH3O_56pmhBnhWaMadT)
12. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYMdPH6FZptZHDbJxj_1GWriSgI88ZVP88OXHm1HlzSkPvbf73__nLrJGN66ukJs6MBrNMLCUhLgNDlkKpcMthFLR08Wq27xqiAbhZoDN0-Vbu_his66lHvQbttQ==)
13. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRZt8SOI7N_ZuyGvDtEULN8JpudwNL9j1xNvaAApU7Ygo7fWEkklQbKSwH14lNpHq6wAlodAfDisoRqE7ngspXM2sbKdqzjrCO0ydLJfaqGxeUuvHWyMPMa9Qa)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTadOgS4Sn21LakX8ECDg9ox0-0AD4cqL31e495WCEqfwuSCL9jLbWD4MXdAMiinjJ4xZtlcvjR3ldiHIeM2K4mluyU0JJq_pZfNB8E3FITFILoIieOiJBeW_5LrMcK3VtLnElEFDNeZz5Gfd6V8D7ypg_Aj3U7fHKn37duygiJ8nGQZHj9rJmBG7Z3QoblHC9IihKywrRrmFROYM0LmmBfY298xz1LKiVPg4=)
15. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_ZAOjIcLiO05-j-RObp7-LKIChucHRvUSIWYjn8NC25eGUn6mjNyXi7qvHIK9vyJnxoG3eeEu87uhIkJ9szTV3X0VOL-QBKZ2MKDIBTrDvB9XtmvonwfyHxGwlVKnTqq_bxoKcr-xiT4wBN7t-0wRpno7aPFTOkExFbGWeEJYex0a5YTtnobl3_Hfc_oE3TnMDXPCwJvqFsTCW7NJrw9TzmuvptXarBCHsJB22LUoaOIDswWHPaUsWZLHVjLEUI3vMGUjNE5jGdUMrsZy1nVn4POCw==)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtn_Bk_SNkcAg0hoaX0MtF0Pm2P0RYe0GwdVt0f7yxH4ZwERBNyDhq2CTFVRjc8dUvQUx97KonHBowU1xvs-LOQVIkGDZIw_RILBYrGY6Y0Y_HxMcutQ==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5_HCLoUvqMPFgbVh0kaPsqUe5TrXY-bOsAU3Ju2VYIULOX_DDV-gXO39DNyQ9xLycFr-WYXAwf_HRny0981CywPHFuJPDUgcppXs0L_6t73WOlTVRPJhRYnAVsqLyP0CzZvseYSEyQUwxrQv0MDgxRbuQqoMd9Q_9wDoaMHvwYQiMaoYlBMKspvLCKI7ehGd6_Ug1iHIKgBnNw05ydgCP_G76LVJ2dte7Vgr2kuOOpVrbtrpQmXB0hC7awQ==)
18. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhDI45mjr4aU9J5sTbLxYN9SLXfDFmgodPBAxGbyknWARKtxtjy-GzXZjVOzFKyNoMyv3vQ3HfJP_VXHCKdky1vBKiGat3A2c_uMMg07Gz5d6Ce6c73DWqeyAL-z6UoyvuR_WzNa0=)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF1sNBpZcJrBwViClMS_jUH4lreg1TcP6APU5PePnY22bJBaS9_kjHw-ZYg-Ejhq2V6lz_M3Qoyd2FF_--_hKosszATbvuoq6YzEtaP3O3WQFGwjlGdgO9Rg==)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw4QDRXmFoB0OzJHr5GtcaJVJm-f8WCQw5zsWAlDf8YSdX7yZ8AOHon3V85xo1ueXUAtTQyV9f-N9LWQqVdcBC4ZJY6AYKQdEvrCAxcFbuIaT7l9J6jA==)
21. [ceur-ws.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVvfqCEC9tlaU9RrobdZfNxKmIeYLly7E36XXFmQhn2zmfduiQeRbvITMjVYoCNjEliwY684MnNYwjFlvZF-1lH-DfMGufZ7Tn7cRuDP7aEvP0Flm2es_zpz-BXVy8C-xt)
22. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGibZ6eZfZy2TJz6HAIkjwDwVXf-bSIHr5FIqHOX74OZnp6hXLrZFiH6fB6GVC9EYq-zzR8J5r6xK53WONDSAUzw0SiHYb2XH9jleJG51DHaVrkky2koJZ2Msp6bChYYwqm)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwYDcwTLahjTAi_QHWDZYUY6aKPQu1zqmiuFvNHbHLl4Fa0JyIOdtpaY_W1gJZHgdPwYYmdVkFm4lfDaXcuW1dhJv7DAH5lf35n9LrZZ5oSMTYc2Erim2oC8OEnBnqhsqU3e7S-z1imM5IcZX7fNvVLCq-2uYvJebl5i2nodW9aouAc_Z0cweJbatNw9yKcDruVtn3n0QETD1CRYteyxpSXtGDrm82JD2kRCNrexI6n4QHA6P5SUX58WX0_JEu-4bndui6Mwr7AKBwsXTC-8v8Yq4GEDl0nxaGVaseyu7TROkY)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdJhpPTiNXBHk-BQ8LPAN9gbwBZ73zs4R4Djhm4XYENNlVAJZCSbHuCXI4WOe3mhGI_hDgeYNk4DE94CTOU5tab-a2XJLYwBWKV70h5crGrLSko4rhh6QDsA==)
25. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFROuuYm092eqUIZoC8YXiZWTlC0yRxFHkeT5Mp3IeA-_9duwHX2Pa6A80TKwl2OGhRIEARSwD8D71jFr5drWG35IeYy_Cz52njeodK3ve_Ti_T2mijRi9GzMt4ccZMHtYOyeCi-3E=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhSPssnbeREvnnPRCrv6txV7w-5ZYmvdzrPAfXgu_qOdd6-vY7tfXVPHleDf6qycAWWeTRLSDTW26mWFbr9oWrOAzIaXChezD331s33EyNMXvUKXoavJHeFHJyEQHNRUWBmA==)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIE4RwXUlRFMjz1IC7m-idyQl9hTCjf1sdHT1rh0Hr47gC1lS2pqnT3zSLOhwxqUrO4cEz9Fbk0zvKcVVLg69FreQ4HJrCXJXaqhjccjQXc5FFcBlU3pyVdtjeg4t8dNH97-zhnkMSlCGto-ZQHWHY7f4wieVhA3eJRPlylDbOyilrVRA6NIuVsPBTM_6mpWe0uqFkISrVX1MrNXUddJrj2xVXMNOlIyiOabuC95GQcccWTrgap9_8kyqEqH6dZDx0lQm_LX2dXa4cqHXaOJhz1MxyShVIDZTTrg2h3i8wsd3f84Edzd_GfYTm5g==)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLiTlmGLzKvaSkvQLf9ptYkic2LwIyQOhP6kRGDwJHOROjaPnk_4e0M4RwN1pali_DlLWXl7DLGncK8v5geLq01yRM3NHruOKJbBXIYJN22LHT_VHoYQ==)
29. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_lguEom_N9rR5kBvSQ3HYzWXLSoMRjA1i_Qwc0LmEvp0BO5LAp6wkIcSQFi2DWqjrC5UZsbMapcw3zBDcmiZDiGRETtakyqKg_lOLCMBgnQ8gd0r9fBgoOhAl4JM=)
30. [onepetro.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMSKMEr9gt2jon-pvdCfbYnKF26-Ygt3xpoxMuwIl-dzYHpDEP_Oyexs8CBeVTXMAQqCXPqlyzeVrNdY_PREytk2buLJX_aFliv3K-myAr_dwf1FNW84ysWLdBNxmOPerdx_SfAwDPMFYpKFyv9bPt7pikhP0iK64scx5WvgVGueqPHYvyeeXqcbJgxp3CU9uz3vHY1zyPqUyW)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4QCcseJtM7Qhtdz3WWvJrH3FLEeSIqsZw0JJpSC0ZBGlnUCJ7uo_wcsWn-qbD8ZPnzEnnkO33W6cHEP7auujYHX5kh_QJ5Ik4H2nsULymWoZtK8wSwG4T9E99hA==)
32. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJ0L8eXKWqqbld7GPmJEyTYWb3SMefSXk0nzaX07W55JGBoCg1sov5UJcKj7Hc3ADGfJVkWvgyOqLJ6Qd2447QVu860RfvlsKb5VA51Ax60bS9mstHmRIFtPNh5owc)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElPQTnaUAohWNrDAueK54JHcuIQGxBsfwV-PrT9a-UBpborgV1S9JWSXXfrcqol665fLY3XKlduWzVKb7xcTSrZfdWyPoOrx25_lkwqZn9SkVPWAvQqIbhdP4MmlsyrFPYzf7V2G74i9mCUEtzlt_ksBFs277Ry_CoCzbaSTsRc8VkoQyRDgOJ042ZXPjHMlFHtJexp_fshN5PKRdCiv1kdesH4OBzhIsgGsxngxxI-j-JfZTMwv6CPRczMnUd2Q==)
34. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy6Wbt9M9cbmzzpHJzjbcp38YTw21YxbFxY6cZkScR_Ltsg8z3zm81BCYcf4asXk9DWAhchFHkTLSuL9S3hwkkomoczA13F6Tgx_ebiP_o85lsL2MfAuNILXETKTq_ff_WWIFYTBV-JNCMJz5ezE0dXzfZtp1p9ns8jlLKT0IbaPJbtj0ubG0BrwSKrxjivzyxIDRtmwmm-L0Kcg1Ik3234Uz8YHOUIyNjGKKjiLuhe_I=)
35. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpxRWTE8KVp8baoCE4VQleziE9gaLaJ-7YHvRUDNzt7FgyhhxikXy858dcebEAm-jfDKJod78mM6Tp5SQ0YYHPB-kb_srJooY2WTDyk5txnTJeeOv1F6C8q4QsLR38pdaz)
36. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGabpk2NYAEgewjKCcWoWns4PaYO1zjO2GWdsBU1YtSrVToa4rzLyQaGSEQ_RRURLa4hSdZh7Y3KQV3EaRmnEa8KKpqP7oWVdbj0eRhMR_lzALvVNqNqEJsOGKN4B4DxISujVnXN62sSkcX94Nkn0Db_i77bqfpEGjmpHDv_29Uvj4iICs71_d_G1-PV3UEHe87Q8G03Ur90oTtO6Lz8A==)
37. [whiterose.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIwopra4kIahAHLE4ugHzAyscNdpiOwizTBOyqWsF_rrUzVhbcv4_rtDEr9RLC_B5Ah-3KPrYG5BDXmhfyOxhgO8NiulEO0hob6OaRQ7vUpP1PbBZ5armSi2yHnL4QX0uTPvoQay4ZPRYE1psOIcH6Rkv9WBuNzrt3oyQ=)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTF3bAfiHDtIRT21vLt3VmOGk2p4W4NL_R_wzK5IFV1_aUEyJrmb7fUcXqzlwkWgEV09D-LWPJYApf9KVS7s8Xtyelha9Xx3lrlS5_eF6LyqT0EWAaULusEyXif-j14Q==)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHZaBBB1NVcnrMuro3571sjEmsC5gm0T22YPqhpD7yokG1rFzAQkf_mdT5Afjb8YEp0C4kBotcZPZNBbGJaF00YFFZeNJhg5MQdF5iBjGSZMPkQ1Z064vDsoo4rGwu0yrfX3DFqwx08RUWccoUSvj5eSggLFAZBvKU3dxLtiYIiUiwRYqlyJnWih4JTxFHrRRnDFMH4YQGBXPnR87OEflz2ryb73YcwG6i8fd7MBaWhKpasxSo0ii0ZPwlxg==)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAgjTQt2FtR4sRRqhz1dQUP9izTgEcXfCDy9YKYWkPE9qnwMMu7vR_-7LlIR90UnTBHmoWAMaY9xgtxKDYjymTtAc8IBuMzEJV71UD9tcePK3K_6hZnw==)
41. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVhtm6K4wpvegP67oIvYwhcL_MxESbfnjMt6_7QIRPIiPE8yV35ToXtOm8jL0X96uTUHXepRIqVNODn8PTmmKZn-IoPN6N23MNcT8IeCbmHFn3WCK7bP-s2LV-ua8lRPDiPoqe1uGx1WmxfUEx6V35UBNlaT50tGiICsscdcbe58zxJcOIRI8gcfk88PcGBPeLOBI5Lt5H9ewBWVximfBxjQ==)
42. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMWA73QKgqhtzntDc0edPShD6Tm21LUMoax-WvfSC6xjnQK6vjyYEWUHZeoc92Q459GRVLwQlAXaiLERTPmesI5GLJn34opaRKaGZtfjjmZ_YvqQLcnZzzhDjnFB35chTkeoVWV1je64U8fCWd7yabwQ5cGeE_JZ3GSOnmvisHXE0s3FuuBYqtR0srIghP9haFINcDW4kUIMDjcd74Rsjlst-VAuTVOpU9zhmxkAR2Lzkc1iH8s9ubIA==)
43. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGnSyFwzLjUOqfiRc2Osqmn6v42jUw92APxOZ8uOhrSP9kC6E41cSzQS1TS-iAmif2JP2-SNOUfI3iYH2lnjKT5WOiUHv77RiN7fl2TIunJeM6Y4cz6KTz6LzQyQCnNtVZLYrR9eLZcI7AzBJPvJKcnvd6RH7ziZ_gXx7KSEOTYGY-9fygjYN89o2qP-z7CRps0ICLtNtDIfJY_c7JTjj9ZMBvfESa0U61PP3CKEWwAadOWEOnzV39esRpXRVpNlE=)
44. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7-_k4OaYWiFvfIqlTIKNZlFPyMA2REloWfEc32Bkk7PzpLbQ9PBYwr1xoY3jBDrn29AXTkbVevIv-af4v3f5tHRSZXZ10CmBFRnWalcU9zMUYLTQlx-KGTg==)
45. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkg8BfqQm0OY2Yr2VUuV5TSg-tr16zvtwDZloHNU9QF3Ev-t6o_O70hE9-ivmZY54cZOEOfitWv1ZGmH7CzEjcoQl8Aw97oWkUAznlqbd8zuezWezp6KFyouPQW2WX5gb)
46. [siam.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMD3rx8Mmo3v8qHqLH9XEKpg9hnQQNbRcG96ry_DsXfdzueCr7wbDrgIwCPhSjj6WPnoFBI5EiZE7otlhFfC4LvEdm7DXe7YuZp27MFwWKGx7CRvburSKqv51u9z9yiRsGc28=)
47. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHecnbfKD7uYzqXa_iDtJgdPfk4N8JZu54m0Rtah4ScUmVbtdG8WTAH3F6sUNJOx6s_bkta6UdJguOy1ayCoiz6jYP-XSTtXqXpnBFiLTvBhdgmbxgJuo9M1hpGvSS-d59wNbnMqACz7Fpl9JgAGO80FwAZx6iMnYj1U8sXlG2gFNQ4ZAYwHdmkXFxAPW7soIuIvtVm8xXMW3sKNn4k_DH9NlHSlCeHqsl8O9udwYI-xlVfq2JH0qBNHjB90P28cfzl)
48. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIZhymGS8Z1HCMpRkG4vznefCYIp6GtKexSyHKlMYnlSEnkNRvkTDrOIXRhVxJg5CnFyggRew1F_62-Tq-KDltB0v98B0oRRHFBRCJN9HnEY-CJyJ13oZYOxsg8M3kpJEUSan6e6_vzw==)
49. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtzY1tpElDNJ53Pj2364UPxf5BQ9Urr_P-vhN6C6NuuOSTALJWK96b7CRW3nhVvZ1FhTTstdRu4G3iObbcx9BPS0PJiVMHlscIAHdHn6E-r_p5P8Ibdb738w==)
50. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9lSkrq8bKmwm7Loyy78QlNpvSjUzMZazbL1Am-lCRzRmaFI4vsa-TxD1FgIQJSlBUqncsbPsoEspntrImbnZnX5RReMYMNOch0P1p9CJUliThm2i-G0ItA-hcnZc5lDGnOH-C4d7EJO5L6DMwwWYHs7BRWMZXf8dpIruqm0U65stGTKdXrVi-7OzM3HcUstXh14a6wBb16Q9-5-le-e_kjHUw5dAD588iAYs4C4LAEjWX8gwXT7A=)
51. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErkKF-9hUWjHBo0mB8iwP9pKhUgpSdV2NaUDfTmjRgbXwARIVqMe3WZpCBvlfmBVVz1N3GS9gB0foKGXJPySaUSZYooiJ4Xj5dSqRQKv4LrZ_Rq91lng==)
52. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESbFRtHhjrNa0xm_L_VgTtzrOAc9O3Z5PAfRccUs8vIQG7u0xV1jT7jlR3hD8exCl9dSfveIf45o8plGIMuPE3kEVwdVUYhV5FkzLMp-QEcvHtIkzdi0NkQeZFcbjD1jEvFLsYu7dIeX1n0CBDc0FfNdvYyIbf7REy1O3Sb0OWkM95ArFOAEblk0kJXj4W1-e0l8ogT8ACf6LE8TkVLtX0)
53. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQrBraea20zJs7hwqpEjbJgR5O8GKXbKsUyMsUZflhnlD07wtA3iTgiFZUPxuKy0Hs-f-zyDSaN_d5hbcfTjpzOUqsdfEZWXY8r4Wf62eqzcx2ujhCaPho-A==)
54. [mlr.press](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzQIi_FyntM_SjhLfVfDAwux2JK1D0iY82nLvhlXKRHh0WJIjUmjPKmTW_U_E6raHpHpcL2enfTipTd5oO1DLZ8aECAvg0grAhGVfYG3zvdMTvQbF81KudZgcBcdNhc2nDQgKniAkDYg==)
55. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz6hitVxuHS6_l_Ate_6ecF0A_icQFhBttivb_YsueL6-HKJBMdz6kVmWXdcha5sgO3RZScT-qe7vgURf4pI5mYsrCYxqbihCsdT1TYePW5-l15T_11_Tuqw==)
56. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNm1kz4dlMh6qaGwIsygvJIObxgeU1E-Sx1Ih8Tnc_Rt-lO4LXEkndsN4u-VpnSTgehujGDEg-Sh0fvXhpexloISTWXu5-CNNgUVZfLeEpCYhyjK2uxhEnvryQK0nvHdkG-ZPzjGBhMHzdsOAHFKOFUtz8yuuoV_36oPpmzx0x2KkB8wRz-q_BqCeU_rDEw2eAw3YM75ErmKRFzkq)
57. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuruSIxGN-xdt3LS6eHGqrNHsvjj3s3rAhMDFVKOm8S4_pqA1RCd_ZfLIQ9XfBzyz5TP2_mcSB9kTCsraJgKALYgEoKLH76bq7YQ3IQJneHpDpHt73Q3xoAOe3WBm_l2FwKXGHyUIHWjkHodHYcWkxKRYQ2tbkSPmQECj1l1n1_obLa5cwXjAANXnmShCfHG-Axhh49ZXvV90tNnjO4PIyvQ==)
58. [cstam.org.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmOnj-1DQkl-G5xUkPIsuroVW1EVzvpc6nfQwmH0F1dwxbDeioGRrRDzofxoC5OfQ0g28kwAmgwcIxaHJtxUxt4YcMLrHVkgPLMjLvocY3WXnR6PcRtwtDPRMSdI4FL6zJQtG_p9SMu4I9rgKXKDSPe_hml5UF2gqM6PGQbQ==)
59. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmodi4YWacCXQD5uwjByArFe_-g81p5bxTAiOxRPobKSVIRDH00Mc2QBfl7NM5KgL1jRU_esFvwjyWzUF1qpV7-UfpPUMnC0MPcCwJDRF_YylAVfWHt83zqS22YsHM6zubWv3FruCnWCXckEIrI9uMnvUIN8MgjRxUAtok6mdDCUTEgLR9Je3EbT2R89ihpxHtgMNNDXasND3MaA==)
60. [colab.ws](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5cZKRdaHOp7sQjHOvfwI3P0Uz2-hxCpuAtLsrRVunxei7Ry9eMVSMd91wNotteJLfoQpejBIckU-Aje8Ka1M5jW-OQiiHct20ohViW92XlzW_xzCpklcZgPtc_SjhWsGXKCHoNs0AzxR-mv3BzDLS)
61. [pnnl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0B5O0R-ScQtqaWY4FXW0dOpFKrZ6p0tNeCJaIJGOAp7_1m1J0yih3pviBr5fEu868HucyZiBHHnesFU3DnN_dU3slpzvrYn7_4qgDwmRlw4tQATUkUurBMYiKdoDglkXdhWs=)
