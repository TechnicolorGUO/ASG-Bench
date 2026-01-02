# Literature Review: Review on model predictive control- an engineering perspective.

*Generated on: 2025-12-26 18:39:06*
*Progress: [14/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Review_on_model_predictive_control-_an_engineering_perspecti_20251226_183906.md*
---

# Review on Model Predictive Control: An Engineering Perspective

**Key Points**
*   **Model Predictive Control (MPC)** has evolved from a niche petrochemical algorithm to a dominant control strategy across automotive, robotics, and power electronics industries due to its unique ability to handle multi-variable constraints explicitly.
*   **Historical Evolution:** Originating in the 1970s with IDCOM and DMC, MPC has transitioned through four generations, moving from heuristic impulse-response models to state-space formulations, and now to nonlinear and stochastic approaches.
*   **Current State-of-the-Art:** Recent breakthroughs in 2024-2025 focus on **data-driven MPC**, integrating machine learning (Actor-Critic frameworks) to bridge the gap between reinforcement learning and optimal control, and **distributed optimization** for high-degree-of-freedom systems like legged robots.
*   **Engineering Challenges:** Despite theoretical maturity, practical implementation faces hurdles regarding computational burden on embedded hardware, the complexity of system identification (modeling), and the need for "dependable" software architectures in safety-critical systems.
*   **Future Outlook:** Research is pivoting toward "Neuro-MPC" (combining deep learning with control guarantees), hardware-accelerated solvers (FPGA/GPU), and plug-and-play solutions to democratize advanced control beyond expert circles.

---

## Abstract

Model Predictive Control (MPC) represents a paradigm shift in control engineering, moving from reactive feedback mechanisms to proactive, optimization-based strategies. Unlike classical Proportional-Integral-Derivative (PID) control, MPC utilizes a mathematical model of the system to predict future behavior and optimizes a sequence of control actions to satisfy performance criteria and operating constraints. This review provides a comprehensive engineering perspective on MPC, tracing its trajectory from industrial process control in the 1970s to modern applications in agile robotics and autonomous vehicles. We critically analyze the transition from linear, unconstrained formulations to contemporary nonlinear, stochastic, and data-driven methods. Special emphasis is placed on the "engineering" reality: the implementation challenges on embedded hardware, the trade-offs between model accuracy and computational speed, and the integration of machine learning to address modeling uncertainties. By synthesizing literature from 1976 to 2025, this paper identifies the current state-of-the-art, highlights the persistent gap between theoretical stability and practical robustness, and outlines future research directions necessary to make MPC ubiquitous in cyber-physical systems.

---

## 1. Introduction

The landscape of industrial control systems has long been dominated by the Proportional-Integral-Derivative (PID) controller due to its simplicity and ease of tuning. However, modern engineering systems—ranging from renewable energy grids to quadrupedal robots—exhibit complex dynamics, strong interactions between variables, and strict safety constraints that exceed the capabilities of classical feedback loops [cite: 1, 2]. Model Predictive Control (MPC) has emerged as the premier advanced control methodology capable of addressing these challenges.

MPC is not a specific algorithm but a family of control methods that make use of a process model to predict the future evolution of the system [cite: 1]. By solving a constrained optimization problem at each sampling instant, MPC determines the optimal control inputs that minimize a cost function (typically tracking error and energy expenditure) while strictly adhering to system limitations, such as actuator saturation or safety boundaries [cite: 3, 4].

The motivation for this review stems from the rapid diversification of MPC applications. While early reviews focused heavily on chemical process control, the "engineering perspective" has shifted significantly in the last decade. The availability of powerful embedded processors and efficient numerical solvers has pushed MPC into millisecond and microsecond domains, such as power electronics and automotive powertrain control [cite: 5, 6]. Furthermore, the intersection of control theory and artificial intelligence has given rise to learning-based MPC, a frontier that promises to resolve the longstanding bottleneck of model identification [cite: 7, 8].

This paper aims to provide a rigorous, systematic review of MPC with a focus on practical engineering implementation. It covers the theoretical foundations, historical milestones, and the latest 2024-2025 advancements in data-driven and distributed MPC. It further scrutinizes the practical barriers to adoption, such as computational latency and hardware constraints, offering a roadmap for future developments in the field.

---

## 2. Key Concepts and Definitions

To understand the engineering implications of MPC, one must first define its core components and operational mechanics.

### 2.1 The Receding Horizon Principle
The defining characteristic of MPC is the **receding horizon** strategy. At a current time step \( t \), the controller predicts the system's behavior over a finite prediction horizon \( N_p \). An optimization problem is solved to find a sequence of control actions over a control horizon \( N_c \) (where \( N_c \leq N_p \)) that minimizes a cost function. Crucially, only the first element of this optimal sequence is applied to the plant. At the next time step \( t+1 \), the system state is measured or estimated, the horizon shifts forward by one step, and the optimization is repeated [cite: 3, 9]. This iterative process allows the controller to compensate for disturbances and modeling errors effectively.

### 2.2 The Optimization Problem
The engineering implementation of MPC generally revolves around solving a quadratic programming (QP) or nonlinear programming (NLP) problem of the form:

\[
\min_{u} J = \sum_{k=0}^{N_p-1} \| x_{k+1} - x_{ref} \|_Q^2 + \| u_k \|_R^2
\]

Subject to:
*   **System Dynamics:** \( x_{k+1} = f(x_k, u_k) \)
*   **Input Constraints:** \( u_{min} \leq u_k \leq u_{max} \)
*   **State Constraints:** \( x_{min} \leq x_k \leq x_{max} \)

Where \( x \) represents the state vector, \( u \) the control input, and \( Q \) and \( R \) are weighting matrices defining the trade-off between tracking performance and control effort [cite: 1, 10].

### 2.3 Implicit vs. Explicit Control
In standard (implicit) MPC, the optimization is solved online at every time step. This requires significant onboard computational power. In contrast, **Explicit MPC** (or multi-parametric MPC) pre-computes the optimal control laws offline for all possible state combinations, mapping the state space into polyhedral regions. Online execution is reduced to a simple point-location search (lookup table), enabling MPC on low-cost hardware with microsecond sampling times [cite: 11, 12].

---

## 3. Historical Development and Milestones

The evolution of MPC is a testament to the interplay between industrial necessity and academic rigor.

### 3.1 First Generation: IDCOM and DMC (1970s)
MPC originated in the process industry, specifically in oil refineries and power plants where processes were slow enough to allow for online computation.
*   **IDCOM (Identification and Command):** Presented by Richalet et al. in 1976, this algorithm relied on impulse response models and was one of the first successful applications of predictive heuristic control [cite: 13, 14].
*   **DMC (Dynamic Matrix Control):** Developed independently by Cutler and Ramaker at Shell Oil in 1979, DMC used step-response models. It became the industrial standard because it could handle multivariable (MIMO) systems intuitively. However, early versions handled constraints in an ad-hoc manner and did not guarantee stability [cite: 13, 15, 16].

### 3.2 Second and Third Generations: QDMC and State-Space (1980s-1990s)
*   **QDMC (Quadratic DMC):** Engineers at Shell developed QDMC to systematically handle hard constraints using Quadratic Programming (QP). This marked the transition from heuristic control to optimization-based control [cite: 14, 15].
*   **State-Space Formulation:** By the late 1980s and 1990s, algorithms like **SMOC (Shell Multivariable Optimizing Controller)** adopted state-space models and Kalman filters. This allowed for better handling of unstable plants and integrated disturbance estimation, bridging the gap between industrial practice and modern control theory [cite: 14].

### 3.3 Fourth Generation: Stability and Nonlinearity (2000s-Present)
The academic community focused heavily on providing theoretical guarantees. Seminal work by Mayne, Rawlings, and Morari established conditions for **stability** and **recursive feasibility**, often utilizing terminal costs and terminal constraints [cite: 16, 17]. Concurrently, the rise of fast computing enabled **Nonlinear MPC (NMPC)**, where the internal model is no longer restricted to linear dynamics, allowing for the control of highly complex systems like aerospace vehicles and chemical reactors [cite: 12, 18].

---

## 4. Current State-of-the-Art Methods and Techniques

As of 2024-2025, the field has moved beyond basic stabilization toward high-performance, adaptive, and learning-integrated architectures.

### 4.1 Data-Driven and Learning-Based MPC
A major bottleneck in engineering MPC is obtaining an accurate physics-based model. Recent trends focus on **Data-Driven MPC**, which bypasses explicit modeling by using input-output data directly (e.g., using Willems' fundamental lemma) or by learning dynamics via neural networks [cite: 19].
*   **Neural MPC:** Deep Neural Networks (DNNs) are used to approximate complex nonlinear dynamics. However, ensuring stability with "black-box" neural models remains a challenge. Recent work in 2025 has focused on providing systems-theoretic guarantees for these learning-based controllers [cite: 8, 19].
*   **Actor-Critic MPC:** A 2024 breakthrough by Romero et al. introduced "Actor-Critic MPC," bridging Reinforcement Learning (RL) and MPC. In this architecture, a differentiable MPC layer acts as the policy (actor), while a critic network estimates long-term costs. This combines the data efficiency and flexibility of RL with the constraint satisfaction and robustness of MPC [cite: 20, 21, 22].

### 4.2 Distributed and Hierarchical MPC
For large-scale systems (e.g., power grids, swarms of robots), centralized MPC is computationally prohibitive.
*   **Distributed Optimization:** Recent work by Amatucci et al. (2024) on legged robots demonstrates **Distributed MPC**, where the robot's dynamics are decomposed into parallelizable subsystems. Using Alternating Direction Method of Multipliers (ADMM), these subsystems reach consensus, reducing computational time by up to 75% compared to centralized approaches [cite: 23, 24, 25].
*   **Hierarchical Control:** In the process industry, hierarchical structures are used where a high-level "Economic MPC" optimizes plant-wide profitability and sends setpoints to lower-level tracking MPCs [cite: 26].

### 4.3 Finite Control Set MPC (FCS-MPC)
In power electronics, the inputs are often discrete (switch positions: on/off). **FCS-MPC** exploits this discreteness by evaluating the cost function for all finite switching states and selecting the one that minimizes error. This eliminates the need for a modulator (like PWM) and allows for extremely fast dynamic response, though it requires high sampling frequencies [cite: 27, 28].

---

## 5. Applications and Case Studies

The "engineering perspective" is best illustrated through the diverse applications where MPC is currently deployed.

### 5.1 Automotive and Autonomous Driving
The automotive sector is a primary driver of modern MPC research.
*   **Autonomous Driving:** MPC is used for trajectory planning and path tracking, handling vehicle dynamics and obstacle avoidance constraints simultaneously. It is superior to PID for lane-changing maneuvers at high speeds where dynamics are nonlinear [cite: 6, 29, 30].
*   **EV Energy Management:** In Electric Vehicles (EVs) and Hybrid EVs, MPC manages the power split between motors and batteries to maximize range and battery life. Recent 2024 reviews highlight MPC's role in Vehicle-to-Grid (V2G) systems, optimizing charging schedules based on grid prices and user demand [cite: 31, 32].

### 5.2 Robotics
Robotics requires handling fast dynamics and unstable equilibrium points.
*   **Legged Locomotion:** MPC is standard for quadrupedal robots (e.g., Boston Dynamics' Spot, Unitree). It optimizes ground reaction forces to maintain balance. The 2024 integration of distributed optimization allows these robots to handle more complex configurations, such as adding manipulator arms, without sacrificing real-time performance [cite: 23, 25].
*   **Agile Drone Flight:** MPC enables quadrotors to perform aggressive maneuvers by predicting aerodynamic effects and respecting thrust limits, outperforming human pilots in time-optimal racing scenarios [cite: 20, 21].

### 5.3 Power Electronics
MPC has revolutionized the control of power converters (inverters, rectifiers).
*   **Grid Integration:** MPC controls the synchronization of renewable energy sources with the grid, handling fault ride-through and harmonic mitigation better than classical linear controllers [cite: 5, 27].
*   **Variable Speed Drives:** In motor drives, MPC provides faster torque response and lower switching losses compared to Field Oriented Control (FOC) [cite: 27, 28].

### 5.4 Process Industry and Water Systems
*   **Petrochemical:** This remains the stronghold of MPC. Modern implementations focus on "Economic MPC," which integrates real-time economic optimization (maximizing throughput/profit) directly into the control layer rather than just tracking setpoints [cite: 33, 34].
*   **Water Networks:** MPC manages open water channels and urban drainage systems, using weather forecasts to pre-emptively lower reservoir levels before storms to prevent flooding [cite: 3].

### 5.5 Building Energy Management Systems (BEMS)
MPC in HVAC (Heating, Ventilation, and Air Conditioning) utilizes weather predictions and occupancy schedules to pre-cool or pre-heat buildings. This shifts energy consumption to off-peak hours, significantly reducing costs and carbon footprint compared to rule-based thermostats [cite: 35, 36, 37].

---

## 6. Challenges and Open Problems

Despite its success, widespread engineering adoption of MPC faces significant hurdles.

### 6.1 Computational Burden and Embedded Implementation
Solving an optimization problem at every time step (e.g., every 50 microseconds for power electronics) requires substantial computing power.
*   **Hardware Constraints:** Implementing MPC on low-cost, low-power microcontrollers or FPGAs is difficult. Standard solvers require floating-point arithmetic, but embedded hardware often relies on fixed-point arithmetic. This can lead to numerical overflow and instability [cite: 17, 38, 39].
*   **Solver Efficiency:** There is a constant need for faster, "embedded-ready" solvers (like ADMM or Fast Gradient Methods) that have a small code footprint and deterministic execution time [cite: 12, 38].

### 6.2 Modeling and System Identification
MPC is only as good as the model it uses.
*   **Cost of Modeling:** In the process industry, identifying a sufficiently accurate model (System Identification) can take weeks of plant testing, which is expensive and disruptive. "SysID" remains the most labor-intensive part of MPC commissioning [cite: 34, 40].
*   **Model Maintenance:** Models degrade over time due to equipment wear or fouling. Adaptive MPC schemes that update the model online are theoretically available but risky to implement in safety-critical industrial environments [cite: 3, 34].

### 6.3 Dependability and Verification
For safety-critical applications (aerospace, medical), software must be verifiable. The iterative nature of MPC solvers makes it difficult to guarantee the "Worst-Case Execution Time" (WCET). If the solver fails to converge within the sampling interval, the control system may fail. Developing "dependable" MPC architectures that can guarantee safe fallback strategies is an open engineering challenge [cite: 17, 41].

---

## 7. Future Research Directions

The future of MPC lies in reducing the barrier to entry and increasing autonomy.

### 7.1 Integration of AI and Control (Neuro-MPC)
The convergence of AI and control theory is accelerating. Future research will focus on **Physics-Informed Machine Learning**, where neural networks learn the residuals (errors) of a physical model rather than the whole dynamic, creating "Grey-Box" models that are both accurate and data-efficient [cite: 7, 8]. The "Actor-Critic MPC" framework suggests a future where controllers learn complex behaviors via trial-and-error (RL) but execute them with the safety guarantees of MPC [cite: 20, 21].

### 7.2 Hardware Acceleration and Edge Computing
To enable MPC on faster systems, research is moving toward custom hardware architectures. This includes **FPGA-based solvers** that parallelize the optimization steps, allowing for MHz-range sampling rates [cite: 12, 39]. Additionally, "Edge MPC" architectures are being developed where heavy optimization is offloaded to edge servers (e.g., in 5G-connected factories) while the local controller handles safety [cite: 40].

### 7.3 Standardization and "Plug-and-Play" MPC
Currently, MPC requires expert tuning (weighting matrices \( Q \) and \( R \), horizon lengths). Future tools aim to automate this tuning process, making MPC a "plug-and-play" technology accessible to engineers who are not control experts. This involves automated system identification and self-tuning algorithms [cite: 33, 34].

---

## 8. Conclusion

Model Predictive Control has matured from a specialized algorithm for oil refineries into a versatile engineering cornerstone essential for the autonomy of modern systems. Its unique ability to explicitly handle constraints and anticipate future behavior makes it indispensable for the next generation of cyber-physical systems, from self-driving cars to agile robots and smart grids.

However, the "engineering perspective" reveals that the challenge has shifted from *theory* (proving stability) to *implementation* (computation, modeling, and hardware integration). The current state-of-the-art is addressing these through data-driven modeling, distributed optimization, and hardware-specific solver design. As research continues to bridge the gap between rigorous control theory and flexible machine learning, MPC is poised to become the standard for high-performance control across all engineering domains.

---

## References

*   **[cite: 7]** ACM Transactions on Autonomous and Adaptive Systems (2020). *Adaptive Systems: A Systematic Literature Review*. [cite: 7]
*   **[cite: 3]** The International Journal of Advanced Manufacturing Technology (2021). *Review on Model Predictive Control: An Engineering Perspective*. [cite: 1, 2, 3, 4, 10, 26, 42, 43]
*   **[cite: 35]** MDPI Buildings (2025). *Review on model predictive control in BEMS*. [cite: 35, 36]
*   **[cite: 9]** SDEWES (2025). *State of the art model predictive control methods*. [cite: 9]
*   **[cite: 18]** IFAC NMPC (2024). *Nonlinear Model Predictive Control Conference Objectives*. [cite: 18]
*   **[cite: 23]** IEEE/RSJ IROS (2024). *Accelerating Model Predictive Control for Legged Robots through Distributed Optimization*. [cite: 23, 24, 25, 44]
*   **[cite: 20]** IEEE ICRA (2024). *Actor-Critic Model Predictive Control*. [cite: 20, 21, 22, 45, 46]
*   **[cite: 29]** IEEE Transactions on Control Systems Technology (2024). *Special Issue on MPC Applications*. [cite: 29]
*   **[cite: 26]** MDPI Applied Sciences (2024). *Hierarchical Coordinated Control Strategy*. [cite: 26]
*   **[cite: 13]** SimulateLive (2015). *Advanced Process Control: A History Overview*. [cite: 13]
*   **[cite: 14]** IJETT (2013). *Model Predictive Control: History and Development*. [cite: 14]
*   **[cite: 15]** Chemical Engineering Process (2003). *Review of MPC History*. [cite: 15]
*   **[cite: 16]** IEEE Control Systems Magazine (2025). *Interview with Manfred Morari: The Genesis of MPC*. [cite: 16]
*   **[cite: 36]** MDPI Buildings (2024). *Special Issue on Practical Applications of MPC*. [cite: 36]
*   **[cite: 8]** Reviews in Chemical Engineering (2025). *A tutorial review of machine learning-based model predictive control methods*. [cite: 8]
*   **[cite: 19]** Annual Reviews in Control (2025). *An Overview of Systems-Theoretic Guarantees in Data-Driven MPC*. [cite: 19]
*   **[cite: 5]** Recent Advances in Electrical & Electronic Engineering (2020). *Comprehensive Review on MPC Applied to Power Electronics*. [cite: 5]
*   **[cite: 11]** IEEE AEIT Automotive (2019). *Model Predictive Control: A Review of Its Applications in Power Electronics*. [cite: 11]
*   **[cite: 27]** IEEE Industrial Electronics (2013). *Model predictive control: A review of its applications in power electronics*. [cite: 27, 47]
*   **[cite: 28]** Springer (2017). *Model Predictive Control for Power Electronics Applications*. [cite: 28]
*   **[cite: 6]** MDPI Applied Sciences (2024). *Model Predictive Control in Automotive Systems*. [cite: 6]
*   **[cite: 31]** MDPI Energies (2024). *Review of MPC for EV Integration and V2G*. [cite: 31]
*   **[cite: 32]** SAE International (2024). *Review of Production Multi-Motor EVs and MPC Techniques*. [cite: 32]
*   **[cite: 30]** Springer (2021). *Review of MPC for Autonomous Ground Vehicles*. [cite: 30]
*   **[cite: 17]** IEEE Systems Journal (2017). *Toward Dependable Embedded Model Predictive Control*. [cite: 17, 41]
*   **[cite: 12]** IEEE ACC (2021). *Offset-Free Approximate NMPC on Embedded Hardware*. [cite: 12]
*   **[cite: 38]** Optimization Online (2013). *Embedded MPC Solvers*. [cite: 38]
*   **[cite: 39]** IEEE Transactions on Industrial Informatics (2018). *FPGA Implementation of MPC*. [cite: 39]
*   **[cite: 33]** ABB (2024). *MPC Industrial Implementation Challenges*. [cite: 33]
*   **[cite: 34]** ADCHEM (2015). *Monitoring and Maintenance of Industrial MPC*. [cite: 34]
*   **[cite: 37]** ACEEE (2024). *Practical challenges of MPC for grid-interactive buildings*. [cite: 37]
*   **[cite: 40]** Reddit/ControlTheory (2024). *Practical considerations for implementing MPC*. [cite: 40]

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAW-aAi3qz6TjMr9RcWt79NNR-ZCAtawgDt4F8mh20sKCCeQBZbIhngUzS9O05Ph5NDFUue_ktHIi4CD9NnphJAdGp--0bJNLLpH7wyC9mYfGWswz1SDuqqEgqYZdgaftzT63D2IzlvOfKdtQtWNH-OQifS6IiIxWuPjmwAj3KujQCI4Q6omZoz56X4p7Bh8udsg4Dd-L-PkYNWEB0Ju_4hgqWqGM=)
2. [researcher.life](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98h0ooE1PP-MeZ6rEiUCxcXpYWQvqKozrJ2rJnVccR0RHB3nliCvYTTDUJ8FV1MygluYMco6hkvtB-F8j8btvhVXajbGvpfIh2NtD8KauyLnV196zzPVjO5D1ScLZuJd7LrNkvFzT_qVlN1hig_qH-f1eaJaCwh07ffNYa4CxsUHCFUyS11Sk-3kXbrbjmY4pskBR6irFz6N8-mwRlAiPZimxTknVDtqoYZcE3k_xJFE1G-i2HqICKQihswVT)
3. [tudelft.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1O0OYzU9HWjsHTP3CYymUkz8icnCNKDaS2mz702-VfC442Z_KocMgnWWguQMRBfORwNx_linIsxD8tKdWqC1NnVaXn9KUz9Z8GtE6lnnM5dh7nYhU58gtEwjpPPZj6--DBC4WCVNVJePIe_M_LBty)
4. [fraunhofer.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2EZCUC-gCUzKkkwv6fyNzJABa_tEkbss-rHCUXo8z5-5JypMi2wVhS0A2WKsozp0Y3lzqiVjBjB4fGRxDT2RDm4k0bkxqkCjfRKgWsler-rBGzUbhKbJMomQB_Z2bu-KewmxjUY2TSlWudm6lHXVbPujekgWs6s_S28dfctDlVZpp9KfBgAzKY5y3pQ==)
5. [benthamdirect.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNsRmWsAOrY5ZUnu_U8bQ_4VvQSq7MT5wcEAvIG2BgZTv7mBNGF6pJp8-3FlPo9HbrcQ3hU6LBm7NG9E1rpUN3EJWa_JC8cKoj2l8xjUZeyjZvng10lJC7LiHlyOVU3DNlbR6ObFOZBLIwVn06qXMKGjB6_9iGsV133xIlPwH_fTdGPLYkCngwoY1iXw==)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLmqGFkuDHClz_8cidFs2b_6H6TV8qv2UpqYF0jxkvzMBOcCIZoZY-oJH_GLRCxgIc8PKOHndqHJoyUQJ6mTDf1Oi3tTT0zyus44w9VJS4yypEdo5VwhvKODp0-E4=)
7. [rwth-aachen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1kqjuFK8q-GaZ1LtW-HGx83yiMMDC8F5jtZHzkd5yxbR81FHr_9DlvtEWlWUcPr6bunjaxytQ3IcRo8hcbV4jppnhUd8hPNFAHgSAIiguu6WvojWPQrTzTTXudWifTfaLuDdp-ktxH-H2xmJAO737aW6BVdn6pg==)
8. [ornl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj8-M9QZAMQm0ugDJDaiHkQptrEqI-JXkpGy8X9_rowAQzioLWGWUIQfHFU26rmMlHxWM2i9MyAgffX7NcJTnrhDBhT6zMpSoglNjAfY6ckXQGIa4Xd_ywwtTSnkIcYsTfVJdM6RygNexX9SBsbC7IULkJnUu6RQVBxmywISPwYvcjMBTnXd8mSsAVCnjISjoiZVZI0b0DsUU4GPpfm_0=)
9. [sdewes.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwy1NKkdWpaNt-LCEJ-CwDW8wEDRc8_4XQUDE4T0I3-y0QWPzzpfxPR51b-e1c-m7OuKfKVe_Lw75deOdVHSrwI4bBOmoHpExJ9J0GZRJlGbldm3gGM90JCakrcHI=)
10. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwxCvBcbNkJlap1DnRHdGFnMwvBAvcJObKW8i79Lh_e9fczfWgTepeoqucR8sr5CCwVC-exYIQHOxw76PfOGvUNNOXKIEkVAR3jIep94quuigkj0RT2X-oBclg4lKtZEkrknMaVxoAhiTw9qCMzknVPtnwP6ZO4EUZbnwCv2LLEkrz8d83IKNe_RO3EmVok5APDp0QapVv8YmZaz1ZyKf5ZLwvmyOqNH-hHIQRQ8RbA0kImNOatZSINa6SPhWsyz-fZ_B5keI=)
11. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwoanJ9zRNynQDunuXgNm6yEj_8wE6lzA-2ChYB5fL_wGOeHPWBjZDicnl2kQetrwumesldH3cFxlM5QLzkUJzqGtwr84aZwiNFYrmVT1_rY0FAFQOiwgNu6xp1XoEUCDrKA==)
12. [squarespace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbEe-G1Wl7kpQvGkfP7Ge5_GVVyL4LA8qQ1bvgD5kalJjhshHriSwbk52EUthJR7tO77SoNgsu8f-1mlYO-wgr4LtHTh85UdeSur7aO_P4L5Rqb0gA3zP4OtlEEx79yQmeal4sNqMvvW3WRPMGIQgv29U=)
13. [simulatelive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwcmrEn_jvh4nYZo2f8gvc2j0EoUp13B4BPk9nvT0NWvcGGmGjB9CLDSScF9E20ZgVuL8y-83qHSYCorJ7VOdiqvi9iOrsoS0_cdMBNBEzBfVPBCw2U76m1rSduQZ5zZIxlJ8r3DMsiMYck-VzioD5-fnVSMa5LDB38xizzyIRVCZ8mZUTPSkUyUox7JExjk_BkAusfP1Y1j91SA==)
14. [ijettjournal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBIhgEB41U3pAT5KB17OS_dAAhawARRU4HYfsjauC56Si2lPU4eDjxNUgfA0bMsAdqL9HMxDbFJpJmgui8G_X8pkIIfoQphKfjabdpeVKmV751RVMoHI1mpZqdr6-2Alj5BmJxgYcDrdzrLqRb3Y4_On7E-vbaUxU=)
15. [cmu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsMZnQbmzNFsc8AVtKMJ3IXW9bbfFzzgkAJ4yj9mQaNAqp9XgK6XmeuGwzYeSpaUzoEPKVr17-tiT0HpSFH8o0V0OwjhKr9SGhXTZLTewsNo1C42r62q3ylyYioDuPzxp1riiLVaxDKLq4jaWSneUX2_CCGB2xaug3vHdJBQA=)
16. [ntnu.no](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgIzfPJq0zea3gEqQVBNm1PUITGcDRa5FU-LhVvKcB0rtYiLmgp0XxrBJgeJzpeOdN0LD49BDDGWKc5jZrksMsGfhIJas2OUTAYTq4egY4Q-gQJi3qeGCMtglmS0MAo4d1ZYU93GKe3FqtOFEde9AFBvsiNSKgHT-mO5X6v05Fb4EYrKqLvqNs2hsT5YE3HkoiMWj5m5-cHCo8dceaFieCjp-GXFElPitHJ6iFYGZdwcmIEfh4IZlbJIVwqm_YdA0G51ZkT02Ph9gXKNloF2aCGO9uspl1rRnuYrDzHr_n0pey6LY=)
17. [ntnu.no](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3TgJC09LY_D7xOlQHd9yieQYdHJ-VOS8Ob3533CazHLHQ9y8ePAfLdYCQcMxf-iwsLpV08Soenz2pi6Q8NqGSRYHYX5Wu7uaQE5ORBvDz3XX55TsIHt5dBZVB)
18. [nmpc2024.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCSJpygSVEES9wxms4-_32gdTfHFoXKFklcI67DOIzp5ZYS7aczO16s8kGAc7F53j6ORAU5EHT-nTCPnox39j1_ZmYzSHqk9jhL8fcKiWkmZf82rL_4ghN0SE=)
19. [annualreviews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3yjhXsxzVnvj8EyKuhxjwg6fi9lsNFNeVT7W8UvMDfLijPStIgQUjdMlni7aMVEDXrErDBqWgzbujkyJZ3oiIgz-i0RYeb8moiszVtaQMkL9U-2JPMhUlwD65Fsq5nsM8UQzvhl71Bae0McWXFR4EDEdmV_WTz51EhxcHJJLGw7zfrIahY0WdgA==)
20. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9U0IxzBRuX-TkKvqYiHGQXH10tHAA6Ll4rB0zUORYb9F5O2VkzuSdJEtYhA4OmpUrEblFvXE9mE452U5H1q4taNoorq43VxeZcK6NhaJqIR5Q2_SX2JuLBXeeqzmFIv0=)
21. [uzh.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqbCf3H4G3o2PASyFervbUnZXwR-x00GxrEX48mxqXMb3Essig8Auce8lcKp3bKyOeaf2dtKWUIcsJNPrleRo0YchTnTZAAKRm93XxUlXtb0PI1mvMzzx6t_w0rIaksangpg==)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtrl_tYIqx2N8wVxLlL_Ukk_NI6M8LnIlkWkyI9i5SZl2R9seGlitm8o6V5nDL584wAGoKkjEg9uy_UKnDZJ2JvfZRstohhFbKIsq9m96t0b1_VaOcxxqW)
23. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmIYHzBaPmeMFgf3N1fnkz30pr_2qyV4oJpA2g5WUpOPMMb4eh-flXBqSyD-neqg-S-HvAjjSmC_8XynIP0xCPzTKFL_yGUlGT0coium67a8DFrlzwvUC2s1g-vJBpLCQ=)
24. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJHYRUm7K_VUbxfn2eotVE8EYLjUo0XSTDGhvqEihk4JoJrYvdxzP4BIy87yBS37bFVrFhm2wKQMYYzYmgDyNgfbvzIlQf1sQbVeRhlfZNWX2ocKp4ctFE9VFqu-mDlrY3tz8nd5mAN7dcodL988h1vA==)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw4qE9wPpBnIVkfu3J_HiOXb2qV-6qbh_NhCbHxdHTlorQhzlENMl24VM_qyWZVYye_Ozccp9fc5VHDIBCsE10C4FKyZRZIMi__xNJSDRV15woCes-SFGB)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQmZ25SZ94i_b1HKLP86QP9GxBGuPJcnGFjTRIPsggaQCb6exkWEfxjom87liKl7KjA99WpsXSRsdzvdQrScifx24cwOg5wM6Ws48lwk-c04ACBzl5rovqPIiINFMm)
27. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGURGN_KLKq7ItEJkQClQVEcX2z3zq8Dn8J8ZHQ4XngmD-EkRdh98n7tHUn38rpuC6is_liH4ZxTDsrINahI_Cq-GntVXlghGDGIdMtWMn52B4I05udQNGKIPA6XQqdYIdr)
28. [tobiasgeyer.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHzx_yBhgObut-Ca20kb5oj0mLh-dbJX5IRM3IYn-PHHN6fX1iBtDks-fTM8ZBNJiRwE0d4tcghEkDNW81J5Ah-zVM-U01kRPNl48Xz12eUCRZOKFzDUcXCGJWU97N)
29. [cnr.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8HcYClFDMFhe2MLi-XLrcsys8xOktibcdJU7P7BANP6N0yVxTKyPB7-3Ry5DPqowgdmjFZVaBDNRBAHdBL75H4LNf98xWPpCTQQVXLE-ByFBnDvnDVipESAlybxCn5H8OV_CE9HKsYJQ-jIEkse8PQ4Ej8q-R1W5Zv-QwF9FCfciZ83m-dg==)
30. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWtgRE8Y2Auu-34of_OR7Q2pYP5sgmqpz8CbQrFQoABQY25P2bu2MjW3S5CU6JDo-hOh660Xg3TPHND3YZIRKtCRwAhLY6SfTcKiuPbOBny3fKl5E=)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy0w-dKXB1vtgs-dBo-3-acRSfb78ZVR21MfYaNoEG7YYjj1TZxOj5RvygST-j6gPvxv7nufNRFNlYEYl5NJlHEzQTE3w-Ttj8czAKvu5H18dKU5JascGO7IY=)
32. [sae.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFXAaOSyiXZNb_GlQbnffq5sg_r0688EqvXL6its6zirE9ky2ghZqDwhNcwF3RN8kOCL0sbaE_gjcGPIP0htDOLLY3PXT-fdXe6n8gSTW_W42kps48_72ndICG3mqk1RM9Jp4a9VTMgmERqg9yQJXts8nah9asjP9YTSdYW4X8ziut-7sOs08-DbEZEo0FBClhKGGV1KtxXzqfecVe70IvkcujyS-fb7K1hB33KK3AnwxznDrxodAeFIwWcU-eJ59RB2aGA==)
33. [abb.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7O4FnNH8IMyBa46WJKQv6FBpqq3EpSklaJ6FlpxvZfjHafPiX706Awm93zMeA6ioY5mJIwV07ty94dKShn4DYooCAGqDw0f-x3n31szKqBiJbfqUgc0AP8ViCCcxGmnDQNyl-yQ2bcZtjxT4L6gSWNndc97KqReAfmFpTvx_MU0c-)
34. [ntnu.no](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9rqTV4jeCUo1KF0KgaPqiPRi1t4Qp1ZgIiinawJxJkzMe2jUcEOIFNERieQdeMVIxTafywlaPcpKm8KhU5PlscNF39uB5Q6J0VpFpLnlpDwVMo3srEsdRaBeCA5aF_JgdMaincdsTHjmlcPrtYYTSZgK6b_9LabfJyFy8PwPv99Wc)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER8sP3vnWPCcV7DGoD7DwK8iSZvAOgyBqg2I6fZij3qSM_lwWMGCuy8R2eWBkgjfAfGx9HCRDkbwrzGmWWrB_jxx7UoccKLr5ufkdiIkI8sKsFq62ApiyCCXPHSFNE)
36. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdYnierEWTd_KYn6uf-xWz7mBSrSpOGUK4EPiWbdg_1d8-iwfIlYlPQUi3-4n5X0Tb6KOHk86aaI6YuM7ybYEx_pHvQhrkznzinlLYxIsUpRAWcS9Hu2S0GSyAhA==)
37. [lbl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMYsfT0pmIrAbBMUq38MHoGHBv048xsYa-YPKtveevFHqqTONcWQqvR964CvYTkw_kmA9asxVzf4tSG2yBZDB9_mciwBVgNBf6qHswjk-ohbySJA0BbuCgMsX7CGMWVoTBW_QBcQu4Kci8c85180-AZqclbzP9JuUOVTq9Igm7Ae2ZZi5cIvz1R71Ds1mvxsx6ypUYSiByCCD2QKlS8nVrHYIsFEPHEveiSp5MJG8ngJZDTALc3CqgiUMDQg4Z1sUFDjRs_nS7L8cg_a3DSMpiQ6CqQi9uSx5R_qBX1wqIPP7jDlwAN74n)
38. [optimization-online.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_vZlqKEFvzD2DEQlRPgbycUxIUNQoo_dq4JZabJsDVXAPg2nR2KqjV4A4u0AhWSFcFgeVhs6ceBx8mnHFGGlcOpqzEfpdR356e7s_Z4se4ZxAkHIqW9Jt8LfCvR7T6P_d24IwYVYsW_Js1MdZqu5L-NJQT9w01nU=)
39. [unizar.es](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6DYL7TtJUccGSOGBfwsUIQusGuq-77jKTROQKgtsvMW7I9bbj7VBa6Ip5IRu-xSQhDGYbegWXJ3ii-30kX8_LSG-qSZC-T5Md0B2ZWkcqhlHt5WrGftLlv37hKEfYm-1jr97HjC0SRlpVarMl-xVveUzY)
40. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO6-8RBzQupPQ57h3Kbvnxd8joI2u6YcdbtParZHGG7N85UuLHYzVm36qnSJ_ISJTym_Jpu-w3G1QrYZ3-Am3n-cWs0tJo4ekeVjH0Kzrb3flPO9XZLEMCcceVLE-8QWWNeRadAAB7H9Swr-u0IgPYm1ceBwUkCDV-ZfntTGKbbPJvFQXJ-Cvg-b5Acu7LAyd87LNn_9hmEk6HsvZaBQ==)
41. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNlWGqvrLwYrWY9w-tK1CcHzvjHBbnQQpxBjlWziIjxITRhEbA-Kjsgy4vCrjHrD7L0KPlykGqpqRoMKZ7xCRQvPx5eeU9AIIY5Xbhcvw31nXF8JBISpgnFPRH-RsgCEERLw==)
42. [exlibrisgroup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFPiy_rWyq32aK42B2iysR3LCO0B57Less2ezz_deZk6eXvXvWjpVlSadalaNeUwNVecLyO5SogRkwmJ9HWkqQPI4R9bBE9M_Nu2kjdcLTfyghCl1XmY5VV5NUM9rCWKwSGdM54ymcsHXl1phmFsBiIS6BIBmWyyi9xBIXM71-NJQg27n3aAZRpZRTrbUEmM03jgbiuqPV3NEFUWVQ5A9Cf8thtVAMpAsIkt0CLb759zbdHbuhzdaj6-ArR0IYr9dSyJTFDur1NLfww4P7bwq9pKa58x0fygAZp3YhN3vafIuhHrbr9QnxsaAdlJCpBBe9Crasx2soWOT2bTPQI8IbM6tZ7WWoAmyR66nahPGe3PAy1Kt-1VgwmOI57hq6-ls3JQgdeQUAUeCaEwF0lmAX4rczGJndOUXr_NvYXwql7gCSydzXFL3x1wM1YnrOejwg1OuGZsWw6ApjVPIKwocIxiXCBM2aQ9ltK78_2wFxuvxOWyASlC2yM8IwbH2ge7WMnVNFziiQGEQEJkfRffEdLs1AnJK5ixXdBydb18qBuPEn94GSGOR_b3dQ)
43. [dntb.gov.ua](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdzQLftY396nytBhvoVPWrzUP97S4sBOmI6NUnvYFM6oIy3_B6j-Cdl2Iw3m9mmIqp-LpvyNDi3Lpn5WJVLV26bSFksRsifw9GdUSYJg5dj4k6qX9JttgXfbv2PKIYt7c=)
44. [iit.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Q-bTp6S3OcZuc_Z7xx4opOpgQPmKieysbKvIR_Qt82U0efb7jdKH4QpbPYCbS6TYrj2qPGvJUsEpJZsy0WajikdAYgFBCfUwM463nWABXvc6y5BUZ4FPRl00w19NshZbH4_f7A3noUlYuPuMvcPvHUKD)
45. [bibsonomy.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdJSw640KXvXuh3ehIIdDq8YC9QhUtuouXlP19Jxx2hCFhP-ERc7qpVlNO28pmo5oACw7AyqKXghRF_hmCT4mIMPz47zW-Fd5pRO3IYQ2QX6ryAwsTHXdKDB7xwZE5ubOquRSnH0xJ2INiJP3asQu79EY_Lx8QSLF02SSExtc=)
46. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_q2EPLsrE0MZ_t42I8pt94n-5pQqEO0W-b7xDXs8LhdI6C-cP37F40AC94m1oHGsNKKGvIZdNsVQbeSptYMefYgqxSDToUMummJ32xxWD_bosdjZTZ2AfCQD9LsppTHhKzKzSVZCHnRk5yhe0Gb0o4xa8QZOH37n73iu6UXxv7Yd8J_9fPNppAFv0Q7YhKSrt2gxtBWtX6QXkOBb423eczh9S9CqrSMnftSMQ_wEh-yWxzSwoIg==)
47. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMf29hf1nvzS01PhJ_9F45Yz9BKN8RMNajJfO2L2FTmm3IW_o3Eqje6_Ll1bG-PwDJAfWxjAHEBwzIf9-deeV9zZfOHceatuOX1v8nMd_P647w5cv6CK-_DCDdNIQd4KhcMA==)
