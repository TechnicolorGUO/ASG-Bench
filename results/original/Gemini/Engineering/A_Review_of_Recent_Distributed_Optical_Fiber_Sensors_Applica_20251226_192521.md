# Literature Review: A Review of Recent Distributed Optical Fiber Sensors Applications for Civil Engineering Structural Health Monitoring.

*Generated on: 2025-12-26 19:25:21*
*Progress: [18/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/A_Review_of_Recent_Distributed_Optical_Fiber_Sensors_Applica_20251226_192521.md*
---

# A Review of Recent Distributed Optical Fiber Sensors Applications for Civil Engineering Structural Health Monitoring

**Key Points**
*   **Paradigm Shift:** Distributed Optical Fiber Sensors (DOFS) have revolutionized Structural Health Monitoring (SHM) by transforming the entire optical fiber into a continuous sensor, replacing thousands of discrete point sensors.
*   **Scattering Mechanisms:** The technology relies primarily on three light scattering mechanisms: Rayleigh (high-resolution strain/acoustic), Brillouin (long-range strain/temperature), and Raman (temperature).
*   **Recent Breakthroughs:** Recent advancements (2020–2024) include the use of Distributed Acoustic Sensing (DAS) for dynamic vehicle weighing on bridges, sub-millimeter crack detection in concrete using Optical Frequency Domain Reflectometry (OFDR), and real-time seismic safety assessments of high-speed rail infrastructure.
*   **Integration with AI:** The field is moving toward integrating DOFS data with Digital Twins and Artificial Intelligence to handle massive datasets and automate damage detection.

## Abstract

Structural Health Monitoring (SHM) is critical for ensuring the safety, longevity, and resilience of civil infrastructure. Traditional monitoring methods, relying on discrete point sensors, often fail to capture localized damage or global deformation trends in large-scale structures. Distributed Optical Fiber Sensors (DOFS) have emerged as a transformative technology, enabling continuous, real-time measurement of strain, temperature, and vibration along fiber lengths ranging from meters to over 100 kilometers. This review provides a comprehensive analysis of recent DOFS applications in civil engineering, focusing on developments from 2015 to 2024. We examine the fundamental principles of Rayleigh, Brillouin, and Raman scattering, and their implementation in state-of-the-art interrogation systems. Detailed case studies are presented, covering crack detection in bridges, convergence monitoring in tunnels, landslide detection in geotechnical engineering, and leak detection in pipelines. Furthermore, the review critically analyzes current challenges, including strain transfer mechanisms and data processing, and identifies future research directions such as the integration of DOFS with Artificial Intelligence (AI) and Digital Twins.

## 1. Introduction

The deterioration of civil infrastructure due to aging, environmental loading, and natural hazards presents a significant global challenge. To mitigate catastrophic failures and optimize maintenance strategies, Structural Health Monitoring (SHM) has become an essential discipline within civil engineering [cite: 1, 2]. Historically, SHM relied on visual inspections and discrete sensors such as electrical resistance strain gauges, accelerometers, or vibrating wire transducers. While effective for localized measurements, these "point" sensors cannot detect damage occurring between sensor locations, leaving vast areas of large structures unmonitored [cite: 3, 4].

Distributed Optical Fiber Sensors (DOFS) address this limitation by utilizing the optical fiber itself as the sensing medium. This technology allows for the acquisition of spatially continuous data, effectively providing thousands of sensing points along a single cable [cite: 5, 6]. The advantages of DOFS include immunity to electromagnetic interference (EMI), high sensitivity, durability in harsh environments, and the ability to monitor long-distance assets such as pipelines and tunnels [cite: 1, 7].

Recent years have witnessed a surge in DOFS applications, driven by improvements in spatial resolution, measurement range, and interrogation speed. Notably, the shift from static monitoring to dynamic sensing using Distributed Acoustic Sensing (DAS) and the achievement of sub-millimeter spatial resolution using Rayleigh scattering have opened new frontiers in damage detection [cite: 8, 9]. This paper aims to review these recent advancements, categorizing them by application domain and sensing principle, while highlighting the transition from laboratory validation to full-scale field implementation.

## 2. Key Concepts and Definitions

DOFS systems operate by injecting light into an optical fiber and analyzing the backscattered signal. The interaction between the photons and the glass medium results in three primary types of scattering, each useful for measuring specific physical parameters.

### 2.1 Scattering Mechanisms

1.  **Rayleigh Scattering:** This is an elastic scattering process caused by random density fluctuations and refractive index variations frozen into the fiber core during manufacturing. It is sensitive to both strain and temperature. Techniques based on Rayleigh scattering, such as Optical Frequency Domain Reflectometry (OFDR) and Phase-Sensitive Optical Time Domain Reflectometry ($\phi$-OTDR), offer the highest spatial resolution (down to millimeters) and are increasingly used for dynamic acoustic sensing (DAS) [cite: 3, 10, 11].
2.  **Brillouin Scattering:** This inelastic scattering arises from the interaction between the incident light and acoustic phonons (sound waves) in the fiber. The frequency shift of the backscattered light (Brillouin Frequency Shift, BFS) is linearly proportional to both strain and temperature. This mechanism is the basis for Brillouin Optical Time Domain Analysis (BOTDA) and Reflectometry (BOTDR), which are ideal for long-range monitoring (tens of kilometers) [cite: 5, 6, 12].
3.  **Raman Scattering:** This inelastic scattering is caused by the interaction of light with molecular vibrations. It produces two components: Stokes (weakly temperature-dependent) and anti-Stokes (strongly temperature-dependent). Raman systems are used almost exclusively for Distributed Temperature Sensing (DTS) and are insensitive to mechanical strain [cite: 13, 14].

### 2.2 Interrogation Techniques

*   **OTDR (Optical Time Domain Reflectometry):** Uses light pulses to determine the location of events based on the time-of-flight. Spatial resolution is determined by pulse width [cite: 1].
*   **OFDR (Optical Frequency Domain Reflectometry):** Uses a swept-wavelength laser and interferometry. It provides exceptionally high spatial resolution (sub-millimeter) over shorter ranges (<100m), making it ideal for crack detection in concrete [cite: 4, 10].
*   **BOTDA vs. BOTDR:** BOTDA requires access to both ends of the fiber (loop configuration) and uses stimulated scattering for higher accuracy. BOTDR requires only single-end access (spontaneous scattering), making it more practical for field installation despite lower signal strength [cite: 12, 15].

## 3. Historical Development and Milestones

The evolution of fiber optic sensing in civil engineering has progressed from point sensors to fully distributed systems.

*   **1980s - Early Concepts:** The first distributed sensors were developed, primarily focusing on Raman DTS for industrial temperature monitoring [cite: 13].
*   **1990s - The Rise of FBG:** Fiber Bragg Gratings (FBG) became the dominant optical sensor for SHM. While accurate, FBGs are quasi-distributed (point) sensors, requiring multiplexing to cover large areas [cite: 4, 16].
*   **2000s - Brillouin Sensing Maturity:** The commercialization of BOTDA and BOTDR systems allowed for the first large-scale monitoring of dams and pipelines. A significant milestone was achieved in 2006 with the demonstration of Brillouin-based sensing over a 100 km range [cite: 17, 18].
*   **2010s - High-Resolution Rayleigh:** The refinement of OFDR allowed for "hair-thin" sensing capable of detecting micro-cracks, bridging the gap between global monitoring and local damage detection [cite: 10, 19].
*   **2020s - Dynamic and Intelligent Sensing:** The current era is defined by the adoption of DAS for real-time traffic and seismic monitoring, and the integration of DOFS data with AI and Digital Twins [cite: 2, 8].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 High-Resolution Crack Detection (OFDR)
Recent advancements in OFDR have enabled the detection of crack widths as small as 0.01 mm. By bonding fibers to concrete surfaces or embedding them, researchers can measure strain distributions with millimeter-level spatial resolution. This allows for the precise localization of cracks that are invisible to the naked eye, satisfying regulatory standards for limit states [cite: 9, 20].

### 4.2 Dynamic Monitoring with DAS
Distributed Acoustic Sensing (DAS) has transformed standard fibers into arrays of thousands of vibration sensors. Recent applications include tracking the natural modes of bridges and estimating the mass and speed of vehicles moving across them. DAS systems can now sample at kilohertz rates, capturing dynamic phenomena previously requiring dense accelerometer arrays [cite: 8, 21].

### 4.3 Hybrid Sensing Systems
To overcome the cross-sensitivity between strain and temperature, hybrid systems have been developed. These integrate multiple scattering mechanisms (e.g., Brillouin for strain and Raman for temperature) into a single interrogation unit or cable design. This ensures accurate strain isolation, which is crucial for long-term monitoring where seasonal temperature variations can mask mechanical deformation [cite: 22].

## 5. Applications and Case Studies

### 5.1 Bridges
Bridges are among the most critical infrastructure assets monitored by DOFS.
*   **Crack Monitoring:** In a 2024 study, OFDR sensors were used to monitor a prestressed concrete bridge, successfully detecting micro-crack width changes below 0.01 mm during load testing [cite: 20].
*   **Dynamic Vehicle Identification:** A steel-concrete composite bridge in Austria was equipped with DAS. The system not only monitored structural vibrations but also successfully identified individual vehicles, estimating their speed and mass based on the dynamic strain response [cite: 8, 23, 24].
*   **Seismic Monitoring:** In Taiwan, a 1 km span of a high-speed railway bridge was instrumented with strain-sensing fibers. Following earthquakes of magnitude 6.4 and 6.8 in 2022, the system provided immediate safety confirmation by comparing pre- and post-seismic deformation profiles [cite: 25, 26].

### 5.2 Tunnels
DOFS provides a comprehensive solution for tunnel monitoring, addressing convergence, settlement, and fire safety.
*   **Deformation Monitoring:** Brillouin-based sensors (BOTDA) have been extensively used to monitor strain distribution in tunnel linings. A notable case involved the monitoring of a railway tunnel in Italy affected by an active earthflow, where the system detected localized strains and joint misalignments over a two-year period [cite: 27].
*   **Construction Safety:** During the excavation of tunnels, real-time DOFS monitoring has been used to ensure the stability of the lining and surrounding soil, providing data that matches well with traditional strain gauges but with vastly superior spatial coverage [cite: 15].

### 5.3 Geotechnical Structures
*   **Landslides and Slopes:** DOFS embedded in soil or attached to soil nails can detect the onset of slope failure. Pulse-Pre-Pump (PPP-BOTDA) technology has been applied to monitor landslide surface deformation in the Three Gorges Reservoir area, successfully identifying strain accumulation zones [cite: 28].
*   **Pile Foundations:** Distributed sensors allow for the measurement of strain profiles along the entire depth of piles, providing insights into soil-structure interaction that point sensors cannot reveal [cite: 12, 29].

### 5.4 Pipelines
*   **Leak Detection:** Distributed Temperature Sensing (DTS) via Raman scattering is the industry standard for leak detection. Recent innovations involve "internal" fiber deployment, where fibers are placed inside the pipeline to detect leaks via vibration (DAS) and temperature anomalies with higher sensitivity than external sensors [cite: 30, 31].
*   **Strain Monitoring:** Brillouin sensors are used to monitor ground subsidence hazards that could buckle pipelines over distances exceeding 50 km [cite: 31].

## 6. Challenges and Open Problems

Despite the successes, several challenges hinder the widespread adoption of DOFS:

1.  **Strain Transfer and Coating:** The accuracy of strain measurement depends heavily on the transfer of stress from the host structure to the fiber core. Soft coatings (acrylate) dampen the signal, while stiff coatings (polyimide) provide better transfer but are more brittle. The selection of adhesives and installation methods remains a critical variable [cite: 4, 32, 33].
2.  **Temperature Compensation:** Distinguishing between mechanical strain and thermal expansion is a persistent issue, particularly for Brillouin and Rayleigh systems. While hybrid methods exist, they add complexity and cost [cite: 15, 34].
3.  **Data Management:** DAS systems generate massive datasets (terabytes per day). Storing, processing, and extracting actionable insights from this "big data" in real-time is a significant computational bottleneck [cite: 2, 35].
4.  **Durability and Installation:** Optical fibers are fragile. Ensuring their survival during the harsh construction process (e.g., concrete pouring) requires robust cabling (e.g., steel-armored cables), which can conversely affect strain sensitivity [cite: 3, 36, 37].

## 7. Future Research Directions

*   **AI and Machine Learning:** The integration of Deep Learning algorithms (e.g., CNNs) to automatically recognize damage patterns in DAS/DVS data is a rapidly growing field. This includes automated vehicle classification and anomaly detection in real-time [cite: 2, 38, 39].
*   **Digital Twins:** DOFS data is increasingly being fed into Digital Twins—virtual replicas of physical structures. This allows for continuous model updating and predictive maintenance based on real-time distributed data [cite: 25, 40].
*   **Smart Textiles:** To simplify installation, researchers are developing "smart textiles" where optical fibers are woven into fabric patches. These can be easily glued to structures to monitor cracking without complex cabling [cite: 9, 41].
*   **Standardization:** The lack of standardized guidelines has been a barrier. Recent efforts, such as the 2021 DFOS manual by the Photonic Sensing Consortium (PhoSC), aim to standardize installation and data interpretation practices [cite: 15].

## 8. Conclusion

Distributed Optical Fiber Sensors have matured from experimental novelties to robust tools for civil engineering Structural Health Monitoring. By offering continuous, long-range, and high-resolution data, DOFS overcomes the fundamental limitations of discrete sensors. The recent successful deployments in high-speed rail seismic monitoring, dynamic bridge assessment, and sub-millimeter crack detection demonstrate the technology's readiness for critical infrastructure protection. As research addresses challenges in data processing and standardization, and as integration with AI and Digital Twins deepens, DOFS is poised to become the standard nervous system for the next generation of smart infrastructure.

## References

[cite: 5] Specialty fibers based BOTDA technologies and their sensing applications. [cite: 5]
[cite: 1] Fiber-optic sensors for structural health monitoring of civil infrastructure. [cite: 1]
[cite: 12] Recent progress of using Brillouin distributed fiber sensors for geotechnical health monitoring. [cite: 12]
[cite: 3] Applications of Brillouin Scattering-Based DOFS in Transportation Engineering. [cite: 3]
[cite: 10] Rayleigh backscattering distributed sensing for SHM of bridges. [cite: 10]
[cite: 15] Recent progress in DFOS implementation in large scale civil engineering structures. [cite: 15]
[cite: 11] Rayleigh scattering based distributed sensing system for structural monitoring. [cite: 11]
[cite: 2] Recent advances in distributed optical fiber sensors for structural health monitoring. [cite: 2]
[cite: 4] A Review of Recent Distributed Optical Fiber Sensors Applications for Civil Engineering Structural Health Monitoring. [cite: 4]
[cite: 7] Practical application status of FOS technology in SHM of civil infrastructure. [cite: 7]
[cite: 32] Challenges of distributed fiber optic sensors for strain measurement in concrete structures. [cite: 32]
[cite: 34] Distributed Optical Fiber Sensors for Structural Health Monitoring: Upcoming challenges. [cite: 34]
[cite: 13] Structural Health Monitoring Using Distributed Fibre‐Optic Sensors (Raman/Brillouin). [cite: 13]
[cite: 6] Distributed fiber optic sensors for civil engineering applications (Smartec). [cite: 6]
[cite: 42] Application of Fiber Optic BOTDA Sensor for Fire Detection in a Building. [cite: 42]
[cite: 43] Monitoring deformation behavior of long GFRP bar soil nails using BOTDA. [cite: 43]
[cite: 28] Landslide monitoring using PPP-BOTDA distributed optical fiber sensing. [cite: 28]
[cite: 44] Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review. [cite: 44]
[cite: 27] Long-term monitoring of a railway tunnel affected by an active earthflow. [cite: 27]
[cite: 15] Monitoring tunnel excavation using DFOS. [cite: 15]
[cite: 41] Smart textile with embedded fiber optic sensors for bridge monitoring. [cite: 41]
[cite: 8] Static and dynamic bridge monitoring with distributed fiber optic sensing (Austria). [cite: 8, 23]
[cite: 25] Monitoring a Railway Bridge with Distributed Fiber Optic Sensing in Taiwan. [cite: 25, 26]
[cite: 22] Hybrid distributed optical fiber sensors for multi-parameter measurements. [cite: 22]
[cite: 30] Distributed fiber-optic sensing system detects gas pipeline leakage (Internal deployment). [cite: 30]
[cite: 31] Pipeline leakage detection using Brillouin-based systems. [cite: 31]
[cite: 16] Comprehensive collection of research on SHM using DOFS. [cite: 16]
[cite: 29] Optical fibre sensors in geotechnical works: a review. [cite: 29]
[cite: 45] Standardization activities for fiber-optic measurement systems in SHM. [cite: 45]
[cite: 17] Brillouin Based OTDR With Measurement Range of 100 km. [cite: 17]
[cite: 15] Photonic Sensing Consortium (PhoSC) DFOS manual. [cite: 15]
[cite: 37] Long-Term Performance of Distributed Optical Fiber Sensors Embedded in Reinforced Concrete. [cite: 37]
[cite: 21] Vehicle detection and tracking using DAS data. [cite: 21]
[cite: 38] Automated Traffic Signal Recognition in DAS Data via Deep Learning. [cite: 38]
[cite: 9] Fibre Optic-Based Patch Sensor for Crack Monitoring in Concrete Structures (0.01 mm). [cite: 9]
[cite: 20] Crack detection in concrete bridges using OFDR. [cite: 20]
[cite: 24] Distributed Acoustic Sensing for Tracking the Movement of Road Vehicles. [cite: 24]

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9-PGiWd1QJ6BRO1Kht7xu6ymOON3ACSkWEgcOWnegmtgeUPFrzhwSyRKTMKy07xtID06LQtjQRSwWfhXQukHIBDMNeTSCuAK6jWhvPyBDfvuc4DkzcxkNxLwbwWff)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRG1ow8s8A5pnR3sPMU2qN0Pwl1OLJz3xMnzXuPubpCNZHzgjscbsRpcyfqV-aQ4K9BlVzOiZ0sHcgFq31FFWXqVz3-GQm02ySLuw7enDx3awwNIaXoOLOsgAlPA==)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlLkqeCkr66SgTF1XKxVD2MJNekv_zug3moEA1QMipM8zAzXNxE1SlKP2pQfaz8laTB5CUoubnvU34LzlcUc3a6f0xO_O3A2O533WS94xtlqRxpvq_QN8Jmws3FA==)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFHpsuwpPLyik0u4EOaHNx2uL4eqxM9HuNu0NMIw1lNonvCmqdyUc222cL3QHcw5PioFT0vSescTw6mPsV_5LBOXgpjuyEtY0f3sspbxpyiQxrkvuj8Ugo6MSIFHc=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZw6JWnbz2mThSqjGFhniwDQlMb6XskCODvR4BCgNwNMXom9G2LYkFBVAW5HYXG5nN__GMNwC_MLCRjmMXgKIN2Q5NNsKVIv1sAoLAk3g8tOXvFEbwRQmbR0uoRA==)
6. [smartec.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFeHuhbiRT1AgpvIXQuUbyMacIKWgwSM4A9N0dmkN0V7pTvzlCe2zG_E1I9-DhHNApdHmXkc1zY4-HwU4Mf6bS6y9KSHi77ylBw-Yx06jZjf0sQQzzcJuDxACIrfXQ0vwXF49k6G0DI-PR5Q==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHti9Cm-h9zWTuLuTNP441nn-5B5XuO6EHLG0FEcd7mYmoP0hDn8ZhuSFjh7gF8WcUYdNr4cv3M26lvs4LpRe86RIMhDd1JDP6-ay0woOohnJAQmGweUhochabkbl1F0Fyjs93b4QM=)
8. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZqM2yKBk062Mjy3HcVXCb3L6_LAU8jY9v4zx1-5ReFE5714bejpCm6oFkgJY99WBKlvrh7N5DQxpPqjx7ZuLxULnD39wy_KoANUaStnha0d4wVLE51Y63X-Q99DfaoXA=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnerCWMK76E2dhcIyTKWmx4UcCcCy3Ot6Y8SH_WBPttpkLm3yv-fUUnk-4mFcFYBLN53mHd-jVR66JYVcZlLa85ZMMA47gN81GouuLIgTati_AnTSjpfnd_5bFnsJv0ral4bFZH_cVP3E0yYMgjSKF6bqcQKRQfBglfQ_dJFuhjZy7ZIsY-MM04Tw4_ZpQkxAyRiG3S40-aIT-4mjRSHNNEkbVL0H4YUIn7RqDfbbDZAxx)
10. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHS300ekh0nPPtF1m48wZOLQ4azlySoh0JGrl8nG86VWv3Q9rnH_c1O93X2_hHtkuAfYiTC9yXiRocNmuSPlezVbVdL7n5jJBlVy2-cNoK9nNS4oblZHVB0_weu7ws5A-Eps91XLeyRzFMATYlDUwxuwj52HrekmWIqu8CnOMvhQeWe4miUvZiRNO-0a4t64nUtrg==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGiAFBqGXNObV9eq7YmagEVSZrS6tZ5IYMyt8R6XeyIGJUYAkJ7d-fBjnuWFWNl6B1HOEnVe2ku5Xs3h2wGS1jhZCSAFG2K1HZEl_VNcN0VGWgETDw6LJ7JDJms9RvhX9HJ39HnOBXCbZI5WDbe7Ere275dQR7LBYkaGTJBaT1HaO9rjogUtI0U_xx30p5i98K11BV4QiyWNbeusQu24CZlWqq1ruafJnwoMODPkJ-JgKgzdzhrp8=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxis3m2g_1wly88wM-C0LsgUklIHWih5kG1lkMC5o_nM0lbe-m4BDv6O8tfP0K2srGbVzdfrIsIWe4I-xLw4VJtARvrOakwxws89PaS3bfBzULA5_5McVAnLmKojUtJNEOEygK-BSp7mgpw3AAgPPZksZGHogMwDCAYC8lv_37wsncYQpbt5K30_9o4NK5SF37gvlI0Hgihl4Uvpq75I8JK639as9c0BBF36FQjt42gWQ34_jps2XylER9SLoCNMbjzlGyx9lhMA==)
13. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnWdKYkqtHRwOxAoyK6X__7DKTTug7DDy7wgF0mJOdz7UqArKlBGFNwUOdHWMfF2yrCzYQJBi-SjquT0VIxyNgNyucMo6L3J0qp3imSyv5jVBE4ZuXMAGuhpo8NZEIeWuBOg==)
14. [bibliotekanauki.pl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt8OZVD7zOdS-A81AfIm9miO-gIS09F2qqej0IMxKefguUZHnIqrtrHw-3neYpbSxzipVzckiuYbvP4gmI1KASpNE3ez2DH4XCjeRUz2O7LC1cDBBYaqU8fnCT_i_oAlpmoXw=)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp1XxWJlFDUy5NayexEmYVWqdww7uBTNde5UitFcFnNvTVjSS_7XxUXGz-tFUR94azAcMBqIVzhPakFY0ZEqk1pc7oPUyXCodB1OmhCxDjuCPA68Zr-nFSvEpKxYW_)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-fBa2FDT0FPCUwi2kUZO04f19lK0RhfcTpMvHRPp9a639xzbJh2xudtVLLS3P5mTftJ1ZMEYHfcffdJDS4jfFr6QLkP9QrCR0nxd-ep6d6Bf99Iq3Iz7S95ow1SR77gXTZ4gav3A=)
17. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz49vHWyS6fAGshya-Xt5w8qPIjfN86ZP3uxhmVL6nw-piYKxzHA_U6FA7n1P7O6O9VxTue8lYsX5EVWGPd29VwrOS-XxIoSdPRGBYfZV-LYKQdYSu82T46qz3DAqB4S2did0AO_-J7lgk)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1kFccO2sbXUJ3_i0VyWJIqW18hWpvgp2kb5oY6fv7ysZNkuFNZyIXxx6OaWC1gCPpxkVcc8XAE7imduz2cPHMXB0LPV-oOejc5eXVTFuCDPUWK7J4UgI-5rtHkecV8k2sWzxRrv1nTH8ilQ7R8w-DpVWTAUg6hOd9gm0qlH94mm4sxXSW2PJ1a1jroD7fQhpMiNSPPql1G4U4DIAvxuMsj0UTPwt9aq4aDEXXGC3Jh2Z7zpq4c4rvFsSPuNgyZPjSIVwRUTa15lKaktOl3UInrSli_u8zY_uj_ctR6hiM0-ZncHpI-EH958-gMIu2H8ib4iQYyk2mRUivmrNgOZwrqdckzUUwYjvdc8ShAoROgMWHBiXn7SYsfS_Atj_AtG-r-KRKbDCdNqREE9_CnKCAJQ==)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_jEsrrUgzEHL5KEA_pmTJFH67aYEaeXX2TJkHM6S8KeGRTOdcS1Bigjxp625_3OXEDUb-Wi3Ald1thUD08jRkHvIXykrICYMlTKmATOHeQizncSha79wNnGiLaw==)
20. [tugraz.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTyliUauoh4Mt8YcjZ-h8lO9OE6gAjGX42cW5zJyCljUz9Um2DWpefMtf0ycQNwl55QQVF6jnKQn9w5CzxMbfIp-YxQ86va28BKJ5j4nUQYAnap_TKu-_gkL1C1_kRRe8H4ky6vO7i28ePX3C0Ytf5VXAs0KJIUxwGncnI)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEg4WvJ-aTG7HGkAIYed6JHGvtfp5Q0zht7DH1nxYJBYn-fUn9U9y-qESIYI1jQnVF5FtNR3uWZAPzL4cjEtFqvAUTWTGoo3fYuUYScpA_Jh9eXtkN2U-yz)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwPIucAXhnKki6u94QlSqHAndHWawyzikF_Iec0ThEVIf3hc5bAxRINhJGxSXivlN3Zncm0J_IR8AdZgv9DIfWSvJrGaRuZ2LDOjr0NzEAci2RXqBAejLknHV75D0O)
23. [dpi-proceedings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBRxfGMLYWIUw3Vqf58YcGBR3zxf39DUTZPDNmo6VDwUczGD47eBSSo14hKIeWepoNPBiW-oQePWUTuchHva2la7WZ_5ss7zeSOCYybmHraA2XG3-FLaRZLr_2eekQ38dz-Tp3iB0pwysr3j4YuUGendT02wR5KGX1Wio=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExPh2E5P-siU0wDgQGNXNEcArEidp7rDZWmlwhrGPMSGcc_cYkI2Gs6JXXDXlo2F7Z6_PhJL7g8wKifwVKRgkiubj5V8ZHaiEDbmUdM-UUykomH3kK_cDFJhcspD__K2el0AK0vmbAw97Mfho_A849IQlkvu-wFVPn-jcLkaNVY7kv3VgiSpT4CPMHbKj84g3ZwM2MVGocnf2CqW-q2BZaz6-wjeo_2hA0Go_oVjlQ_WI3YbP_yh09)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjkT4nxAoAPI-R9FbU2__2BAOAIl98fLDo9h5t_uLzc_CnqbnLpP5NcgKX06b1sU1oxlHCY5e7nLQt6bMVdM0dnERxpCPLPJbx284YJmsJdS_pcEP5Q6dXIo3i)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ6YdaMOCnEnlu6gdHL5Q04JhwzluCneJmMCWs2g23dGxk_a-JSi6AWETRFTGeVp0PftpesBJdpfH-8HE1WqaOY6lAs7PEf2iEFJljrD_0-6gibc6D9o06SjV5DI5T94ygrifZKxLyHsMzSXbJAZfP9OKoB-Yrs7Rw_oxrmyCtZwQhdLnsGALKeirxAwiWYM6gQMIDQia1JOGLJgevdFlgk6Fz3RHF0t3JPT1cEAYnfkYoK4eN1pDzxn_ReFv6WePlDKO6kH7PaBmw)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUhdX8_MTOvm5DYaDsG92FjKYU2muLzQDgAhQbv9KZMVLVlDH2__YA_42STCM11dMjpgzIzOvHj9emmBqiLrg-G89WWstLOBraQrQj_S3ET_PQ2WpG-qFvIiGA01k=)
28. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9XlLU1BE3VeSuZxG0gSPFtwf8fIi7I5rL7yc3KeDuBFSX2Bkk9oVsLoVc5mTjOafrNO8EoFC2IFcXtycpp9ujiCztRaya2y7VRlUdLVvXxSvBBNObc3RGyuBjCZNM94pnkQunuSei3PYYfOzC-ZMYHzBbH-3XDdfx71GZ7yKn6--KNjgeVokMk9ebALpooA==)
29. [issmge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmCIl8hvD2uadRs35paRK33U_eRnlz-e7r8T8OPDyEHdTwsCkpn9SQSJfF23bU9hOB2XzirYuwoi2Z9-9rxlHOQnxuJHNrfRQXliRhAH8LjNnjBThdpQ8axq6DEKQ3oE1MF-VpKvbChWK0bUmy1WenMfyTmn7zCcr6MO562qBGepFjUPtc9iQ8woHEYFU4AGwmc3aiquOURtOanSeWwhT2vDKmGg==)
30. [spe.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyYNeznvNxdfeHpQZ1CzDO5NIuGn7ItKKrDKvsZ3KAUUAwuD-qL4hdKR_2BsvBOLHsGT6mUCZ_ERrjMC8CJnaqTJ_Ky5PhsR4Xq7qqtSwBZrNV7ww2Uk-vLHTmP_IDTzv8vrEwdUUDnq8Sn_qIW4h-GIx5517Y_IZxo7rRMeI1nm-u4xEk_iiV9xgl5g==)
31. [roctest.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjUbVBy6ynptU7rCJWvTXlV8SAl2veCcSjxZrNPYbKyJTg3UA0hKMt9fNlPJp_rR1OjmUZamFCAERqoyj-EXCvfhTgyWzdspuvNej2k6SDbukd7NhmIjHlvH9HZ-dMWmxlGDwdHglui0lM3kY=)
32. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH15haIus80OLWQ6u2KhSxulsJUbJd2swVrq7XD3rEgg5BimoVWS-N9ZU6h2bl_mcrhr48jVVgBzAafHCgy9RzdWDF6FpSP6MRy7ZSVI_dlEK3q1V4SB7_s6V8V7tAE)
33. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6CaNyMsW3Pd4PYqTGPD4YkjG9bD54jRCRZ_rfmyCOOT646P8CJq9yzzL52D9IvPJFHBpzJ5rEyeeu_gla0VKwKpuHDXcbFtAHSToL4ExTBvXsmGTZGXN28EV6cw==)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqPJbrRVzx_AGw1fimUUUo-RadPbkuKmquPpEPW67chz6QfDlw1oSssVN17SItxP835CaNc-3ml9nKHQ1wKSYrAtIlUvTGFPkBfHKieZfRInVuicg885C4sCRrbJgPcZDJxlWhcrOc4fOcopLy5_xkcPzjZzE7YTXWMR9RQ8a9HXH5zGiCVJknwP-raA-ymOatGAWgbc_OgvqyEik_psQu8Y1ryqGRdc-9RdmDZXqWnhtWv_s1SNtE9s3J6PFphMK-8Tic98h0iPPnqurV3FFdgKRsd4YZ-yazhDFUcMqRF4yasTJ0VA9yTrqs6g==)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELRQNEUSfm414s9QEUovhRQ-XqMPeJryv94pSRCXATkPl071k_aZLirutjtPUBg0W2qNDkXOU-O4BuV2gsHt1obwMWIHV9aAx1GDXUchBHmScjeblO9pA6awQd3g==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7Qehu5Zv9lkNT8hrWjOxwCfFnzbIUBeoIH6kV7ILf0QSu5VmJCsnB-ODG-8tAwB3QlVxS-lcyC4478wFjPKHUGMdG1MuPMfv2H1GTNml2OUcR5oKkBYE6eV4okP_A5VQJ3HOmlniaqtj9IjuEpHg0ijXEPz9McFkfUP6H4Vycjtjf8w9Cz79vMvrhSH9Mrg-xpuu6Xalvy_5a1icHWCpdigrDA182BPxMO4B8GA==)
37. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcz_sfUmiVyyAxFxkyB800U9AZs5KvK6q4VM3mGf8cWvSBt4IPlR52FIACjLdcR84FOJQXle5kGU4DWPGiUkOEt9y7vDixhPs2xjP_mDlCkDnUP4TsEhbnM3Xdo66P)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB6tQPkx8_h3Wc_pa639qKDH9OsPo0z0U4xKxQ1UVwxlt1iAmvlHC9406Sn283hPAot9PbfUz1CBj4rnYbkUZ2aHpnJmkKj-pJbUEFCuEinfbjylowIt3gL0ymkePQHYe-fTboUGkgG9Kt2PAknD5FvMC8E0zvB1L--uaRYjRblRXGRv7QDx7ToIEfu4u2XT-dIcH0yPAhGcVGBn2BecxTixRqxz_jnSxObKqPlGg0Yh_9SXdcIDJmZ1KZVqK69A-74V0=)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhKH58gZN_-ZpZZ1TvVpgFM7ko-VW5jlYtsbR_-wpXeO6AL_7UglcCAqH-JrTxqhbwwfGbkrxM83e-kTkpj-dwlXF8LDKgHRRcaV6pA5b9r1BmSDZn4uueFERXXA==)
40. [uni.lu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFZMBcjDjCU_20lik6Ymk0ZzarF9rR_mozLZtsgHwII7eYAVlZWddhorg49EPNA2ibQBghPtZQI8DmJvgX5Na_vqXDCew7QWVP1N1og_3d-lz2Urr2Jjj3r7zGEM=)
41. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvxa7SqnE1h7m80TcL-Xkl_w1mW2CEeZR-cZ751Vi4R8PPhSwYQqjHB1Tn08Lhc0tSrNP53eWLelkuGZreO9mzlIBC5uSNe433X4XZowcCRSINGwl-VuEjy7C8SCc=)
42. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESxQf351yYO1QhsdHc3eaK1it-jG9zhBrD15fSaapKu6SiR9g2yOQBfERQBhegXBSASe39hNZck4i_qb8hFo-p0YxqzfwtQYvFEguXdq-HYZp6y-9dzErhreeCcbRFslFNA2N8z330VbwJKMtrm8S5W0rJg0sOOuy2OEYsctaFUgXxi5mygAoWJ_O5fDQwaJujHjtEtyvzpg5v_YV1Pz7EmmjSD-ni8BUStv9p_wnk6A==)
43. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEepP8fg8exSJCFCPCGfuXiHibLR8Adpp0nGB7AMgM8KCyOv54aPfZyORN8jL7ZOSYm-CPqLg4p5vh-mhasEgKPuixxTGbq5BEbOmmSWLjzI_JEHrQmVURcrDMFzappkYocJ2kbeiEoG70q9Gkb-hydI6v68wqnueq8c0IN27B-WrDPCs2qO0tuk78LHE3z)
44. [tudelft.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXSr_cPAX2KDBozG2uSWFFr7ndAVrj_PK5TZtLXzR7qWA9bBKAut6UeFWloA99ZeeTucxxtC3rTWg8NVSMRJrOrZv5qZGqj8f9GRnKKz5pDUW6_wr2vipu-XFJk7BL7RnxYnPEttH219iWi1JsDC39L_j8lFC0y59JkhmJguRdACFayl5QlyE4FeioyEvBTmb5WKjDOylvHVMgTSYVTfp4N9hK)
45. [empa.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfmRH_VgjvcV7qG6DWnJhBL_kXXa4ZZg7WeoXgGlxW0O5TTNuVNTUJp_0gDIvKEQJP7Y9OcgS7v2rrGGMzhKVgrZ4ym-Lit4VYHx-pvYuJ2mxOQMzIsPxwDRKsGH9MqerKPDMtKPodDJPdGmp2yJpd0IKhkIBoglMaoejlrOS_Sp_OlA==)
