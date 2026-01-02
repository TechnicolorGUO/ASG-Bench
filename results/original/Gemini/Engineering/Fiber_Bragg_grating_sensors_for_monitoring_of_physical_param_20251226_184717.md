# Literature Review: Fiber Bragg grating sensors for monitoring of physical parameters  a comprehensive review.

*Generated on: 2025-12-26 18:47:17*
*Progress: [15/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Fiber_Bragg_grating_sensors_for_monitoring_of_physical_param_20251226_184717.md*
---

# Fiber Bragg Grating Sensors for Monitoring of Physical Parameters: A Comprehensive Review

**Abstract**
Fiber Bragg Grating (FBG) sensors have established themselves as a cornerstone of modern optical metrology, offering unparalleled advantages over traditional electromechanical sensors, including immunity to electromagnetic interference, multiplexing capabilities, and suitability for harsh environments. This comprehensive review systematically examines the evolution, theoretical underpinnings, and state-of-the-art applications of FBG technology in monitoring physical parameters such as strain, temperature, pressure, acceleration, and tilt. We trace the historical trajectory from Ken Hill’s serendipitous discovery to the latest femtosecond laser inscription techniques. The paper critically analyzes current interrogation methods, ranging from passive edge filtering to active tunable laser scanning, and evaluates their performance in static and dynamic sensing. Furthermore, we explore diverse applications across structural health monitoring (SHM), aerospace, and biomedical fields. Significant attention is verified to persistent challenges, particularly temperature-strain cross-sensitivity and packaging durability. Finally, the review identifies emerging research frontiers, including the integration of Artificial Intelligence (AI) for spectral demodulation, "Lab-on-Fiber" technologies, and the role of FBGs in the Internet of Things (IoT) ecosystem.

---

## 1. Introduction

The monitoring of physical parameters is a fundamental requirement across a spectrum of industries, ranging from civil infrastructure and aerospace to energy production and healthcare. Traditional sensing technologies, primarily based on resistive strain gauges, thermocouples, and piezoelectric transducers, have long served these industries. However, these electrical sensors face inherent limitations, including susceptibility to electromagnetic interference (EMI), signal attenuation over long distances, and the risk of sparking in explosive environments [cite: 1, 2].

Optical fiber sensors (OFS) have emerged as a robust alternative, with Fiber Bragg Gratings (FBGs) representing the most mature and widely adopted segment of this technology [cite: 3]. An FBG is a periodic modulation of the refractive index within the core of an optical fiber, acting as a wavelength-selective mirror. The reflected wavelength, known as the Bragg wavelength, shifts linearly in response to external physical perturbations such as strain and temperature [cite: 4, 5].

The motivation for this review stems from the rapid diversification of FBG applications and the recent technological leaps in fabrication and interrogation. While early research focused on basic strain and temperature sensing, contemporary studies have expanded into complex parameter monitoring, including liquid level, inclination, and vibration, often utilizing advanced materials and signal processing techniques [cite: 6, 7, 8]. Furthermore, the integration of FBG sensors into smart structures and the Internet of Things (IoT) represents a paradigm shift in how critical assets are monitored [cite: 9, 10].

This paper aims to provide a rigorous, systematic review of FBG sensors for monitoring physical parameters. It covers the theoretical background, historical milestones, fabrication techniques, and interrogation methods. It critically evaluates applications in Structural Health Monitoring (SHM), aerospace, and biomedical engineering, while addressing the significant challenges of cross-sensitivity and packaging. Finally, it outlines future research directions, emphasizing the convergence of photonics with deep learning and nanotechnology.

## 2. Key Concepts and Definitions

### 2.1. Operating Principle
The fundamental principle of an FBG sensor relies on the Bragg condition. When a broadband light source is injected into the fiber, the grating reflects a narrow spectral band centered at the Bragg wavelength ($\lambda_B$), while transmitting all other wavelengths. The Bragg wavelength is defined by the equation:

\[ \lambda_B = 2 n_{eff} \Lambda \]

where $n_{eff}$ is the effective refractive index of the fiber core and $\Lambda$ is the grating period [cite: 5, 11].

External physical parameters perturb the grating by altering either the refractive index ($n_{eff}$) or the grating period ($\Lambda$).
*   **Strain Sensing:** Longitudinal strain ($\epsilon$) elongates the fiber (changing $\Lambda$) and alters the refractive index via the photo-elastic effect. The wavelength shift ($\Delta \lambda_B$) is expressed as:
    \[ \frac{\Delta \lambda_B}{\lambda_B} = (1 - p_e) \epsilon \]
    where $p_e$ is the effective strain-optic coefficient [cite: 12, 13].
*   **Temperature Sensing:** Temperature changes ($\Delta T$) induce thermal expansion (changing $\Lambda$) and alter the refractive index via the thermo-optic effect. The shift is given by:
    \[ \frac{\Delta \lambda_B}{\lambda_B} = (\alpha + \zeta) \Delta T \]
    where $\alpha$ is the thermal expansion coefficient and $\zeta$ is the thermo-optic coefficient [cite: 11, 12].

### 2.2. Types of Gratings
While the uniform FBG is the standard, several variants exist for specialized applications:
*   **Chirped FBGs (CFBG):** These have a varying grating period along the fiber axis, resulting in a broad reflection spectrum. They are used for dispersion compensation and sensing over large strain gradients [cite: 14, 15].
*   **Tilted FBGs (TFBG):** The grating planes are tilted relative to the fiber axis, coupling light into cladding modes. This makes them highly sensitive to the surrounding refractive index (SRI), useful for biochemical sensing [cite: 15, 16].
*   **Long Period Gratings (LPG):** These have a much longer period (100s of $\mu m$) and couple core modes to co-propagating cladding modes, offering high sensitivity to external environmental changes but lower strain sensitivity compared to FBGs [cite: 1, 14].

## 3. Historical Development and Milestones

The trajectory of FBG technology is marked by two distinct eras: the discovery of photosensitivity and the development of practical inscription methods.

### 3.1. Discovery (1978)
The phenomenon of photosensitivity in optical fibers was discovered serendipitously in 1978 by Ken Hill and colleagues at the Communications Research Centre in Canada. While studying nonlinear effects in germanium-doped silica fibers using an argon-ion laser, they observed a permanent increase in the refractive index, forming a standing wave pattern. This resulted in the first "Hill gratings" [cite: 17, 18]. However, these gratings could only reflect the wavelength of light used to create them, severely limiting their utility.

### 3.2. The Holographic Method (1989)
A transformative milestone occurred in 1989 when Gerald Meltz and his team demonstrated the transverse holographic method. They utilized two interfering ultraviolet (UV) laser beams incident from the side of the fiber to create the interference pattern. This technique allowed for the inscription of gratings at any desired wavelength by adjusting the angle between the UV beams [cite: 1, 17, 18]. This breakthrough decoupled the writing wavelength from the sensing wavelength, paving the way for the mass production of FBGs for telecommunications (specifically Wavelength Division Multiplexing or WDM) and sensing.

### 3.3. Modern Fabrication Evolution
Following Meltz's work, the **phase mask technique** was developed, which simplified the manufacturing process and improved reproducibility by using a diffractive optical element to generate the interference pattern [cite: 1, 19]. More recently, **femtosecond (fs) laser inscription** has revolutionized the field. Unlike UV inscription, which requires photosensitive fibers (often hydrogen-loaded), fs lasers can inscribe gratings in almost any transparent material, including pure silica and sapphire fibers, through non-linear multiphoton absorption. This allows for "through-coating" inscription, where gratings are written without stripping the fiber's protective polymer coating, significantly retaining the mechanical strength of the sensor [cite: 3, 20].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1. Fabrication Techniques
Current fabrication methods prioritize mechanical integrity and thermal stability.
*   **Draw-Tower Gratings (DTG):** Gratings are written during the fiber drawing process before the primary coating is applied. This results in sensors with high mechanical strength, suitable for high-strain applications, as the pristine glass surface is never exposed to the environment [cite: 21, 22].
*   **Femtosecond Laser Inscription:** As noted, this method enables the creation of Type II gratings, which are stable at extreme temperatures (up to 1000°C) where standard Type I UV-written gratings would be erased (annealed out) [cite: 3, 20].

### 4.2. Interrogation Techniques
The interrogation system, which extracts the wavelength shift, is critical for sensor performance. Techniques are generally categorized into passive and active methods.

#### 4.2.1. Passive Interrogation
*   **Edge Filtering:** This method converts wavelength shifts into intensity variations using a filter with a linear spectral response (e.g., a matched FBG or a thin-film filter). It offers high-speed demodulation (kHz to MHz range) suitable for dynamic sensing (vibration, acoustics) but typically has a limited dynamic range and lower resolution [cite: 23, 24, 25].
*   **Spectrometers (CCD/Linear Arrays):** Light is dispersed onto a detector array. This is robust and allows for WDM (multiplexing many sensors), but the scanning speed and resolution are limited by the pixel density and readout electronics [cite: 22].

#### 4.2.2. Active Interrogation
*   **Tunable Lasers:** A narrowband laser sweeps across the spectral range. As the laser matches the FBG wavelength, a reflection is detected. This method offers high spectral resolution and high signal-to-noise ratio (SNR) over long distances, making it the industry standard for static and quasi-static SHM [cite: 23, 26].
*   **Optical Frequency Domain Reflectometry (OFDR):** This technique allows for distributed sensing with high spatial resolution (millimeter scale) over tens of meters. It treats the entire fiber as a continuous grating, enabling the mapping of strain fields with unprecedented detail [cite: 27, 28].

#### 4.2.3. Advanced Demodulation
Recent advancements utilize **Fourier Domain Mode-Locked (FDML)** lasers for ultra-fast interrogation, enabling dynamic strain monitoring at rates exceeding 100 kHz [cite: 26]. Additionally, **microwave photonics** techniques are being explored to translate optical shifts into the radio-frequency domain, leveraging high-precision electronic frequency counters [cite: 29].

## 5. Applications and Case Studies

The versatility of FBG sensors has led to their adoption in diverse sectors.

### 5.1. Structural Health Monitoring (SHM)
SHM is the largest application domain for FBGs.
*   **Civil Infrastructure:** FBGs are embedded in bridges, tunnels, and dams to monitor strain, crack propagation, and vibration. For instance, FBG sensors have been successfully deployed to monitor the Golden Gate Bridge and the Shanghai Tower [cite: 30]. Their immunity to lightning and long-distance transmission capability (tens of kilometers) makes them superior to electrical strain gauges for large structures [cite: 15, 31].
*   **Geotechnical Engineering:** FBG-based inclinometers and tilt sensors are used for landslide monitoring and ground movement detection. Recent designs utilize 3D-printed probes and cantilever beams to enhance sensitivity to tilt angles, achieving resolutions as fine as 0.002 degrees [cite: 7, 32].

### 5.2. Aerospace
In the aerospace industry, weight reduction and safety are paramount.
*   **Composite Monitoring:** FBGs are embedded directly into Carbon Fiber Reinforced Polymer (CFRP) composite wings and fuselages during manufacturing. This allows for "smart structures" that can monitor the curing process (temperature/strain) and operational loads (wing bending, impact detection) in real-time [cite: 28, 31, 33].
*   **Propulsion Systems:** High-temperature stable FBGs (e.g., sapphire or regenerated gratings) are used to monitor exhaust temperatures and turbine blade strain in jet engines, environments where conventional electronics fail [cite: 20, 34].

### 5.3. Biomedical Engineering
FBG sensors are increasingly used in minimally invasive surgery and physiological monitoring due to their biocompatibility and miniature size.
*   **Smart Textiles and Wearables:** FBGs embedded in flexible polymers (e.g., PDMS) or woven into textiles monitor respiratory rate, heart rate, and body temperature. They are MRI-compatible, allowing for monitoring during imaging procedures [cite: 35].
*   **Shape Sensing:** Arrays of FBGs (often multicore fibers) are integrated into catheters and biopsy needles to reconstruct the 3D shape and position of the instrument inside the body without using X-ray fluoroscopy [cite: 35, 36].

### 5.4. Specialized Physical Parameter Sensors
Beyond direct strain/temp measurement, FBGs are transduced to measure other parameters:
*   **Accelerometers:** FBG accelerometers utilize a mass-spring system where the fiber acts as the spring or is attached to a cantilever. Vibration causes oscillating strain in the FBG. These are used for vibration monitoring in machinery and seismic detection, offering insensitivity to EMI and high sensitivity (e.g., >500 pm/g) [cite: 37, 38, 39].
*   **Liquid Level and Flow:** FBG arrays measure liquid level by detecting the temperature difference between the liquid and the gas above it (using the self-heating of the sensor or ambient differences). This is critical in fuel tanks and cryogenic storage (liquid nitrogen/oxygen) [cite: 6, 40, 41].
*   **Pressure:** FBGs are bonded to diaphragms or bellows. Fluid pressure deforms the diaphragm, straining the FBG. These are widely used in downhole oil and gas monitoring [cite: 42, 43].

## 6. Challenges and Open Problems

Despite their success, FBG sensors face technical hurdles that limit wider adoption.

### 6.1. Cross-Sensitivity
The most significant challenge is the simultaneous sensitivity of FBGs to both strain and temperature. A wavelength shift can be caused by either parameter, leading to measurement ambiguity [cite: 3, 33].
*   **Mitigation Strategies:**
    *   **Reference FBG:** Using a second, strain-free FBG in close proximity to measure temperature only, which is then subtracted from the sensing FBG [cite: 11, 12].
    *   **Dual-Wavelength/Parameter Matrix:** Using two FBGs with different sensitivities (e.g., different cladding diameters or materials) and solving a matrix equation to decouple the parameters [cite: 27, 33].
    *   **Superstructure Gratings:** Utilizing complex grating structures like Tilted FBGs where core and cladding modes exhibit different sensitivities to strain and temperature [cite: 27, 44].

### 6.2. Packaging and Strain Transfer
Bare optical fibers are fragile. Packaging them into robust housings (steel tubes, composite patches) is necessary but introduces "strain transfer" losses. The strain experienced by the FBG is often less than the strain in the host structure due to the shear deformation of the adhesive and protective layers [cite: 1, 45].
*   **High-Temperature Issues:** In high-temperature applications, standard epoxy adhesives degrade or creep, causing sensor drift. Metal-embedded FBGs (using ultrasonic additive manufacturing or casting) are being explored to solve this, but they introduce thermal residual stresses [cite: 46, 47, 48].

### 6.3. Interrogation Cost and Complexity
High-speed, high-resolution interrogation units (tunable lasers) remain expensive compared to electrical data acquisition systems. This cost barrier inhibits the use of FBG systems in cost-sensitive applications like residential monitoring or simple industrial control [cite: 3, 24].

## 7. Future Research Directions

The future of FBG sensing lies in the convergence of advanced photonics, material science, and data analytics.

### 7.1. AI and Deep Learning for Demodulation
As sensor networks grow in density, spectral overlap becomes a problem. Traditional peak-tracking algorithms fail when FBG peaks merge. Recent research utilizes **Deep Learning (DL)**, specifically Convolutional Neural Networks (CNNs) and Gated Recurrent Units (GRUs), to demodulate overlapping spectra. These AI models can extract accurate wavelength shifts from complex, distorted signals, significantly increasing the multiplexing capacity of FBG networks [cite: 8, 49, 50].

### 7.2. Lab-on-Fiber Technology
"Lab-on-Fiber" aims to integrate functional nanostructures (plasmonic metasurfaces, biological recognition layers) directly onto the fiber tip or grating area. This transforms the FBG from a physical sensor into a highly specific biochemical probe, capable of detecting biomarkers, pH, or gas concentrations at the micro-scale [cite: 36, 51, 52].

### 7.3. IoT and Smart City Integration
The integration of FBG interrogators with IoT modules is a growing trend. "Smart" interrogators with edge computing capabilities can process data locally and transmit actionable insights (e.g., "Bridge Integrity: 98%") to the cloud. This is vital for the realization of Smart Cities, where thousands of sensors monitor infrastructure health, traffic loads, and environmental conditions in real-time [cite: 9, 10].

### 7.4. Additive Manufacturing (3D Printing)
Embedding FBGs into 3D-printed metal or polymer parts allows for the creation of "self-sensing" components. Ultrasonic Additive Manufacturing (UAM) allows fibers to be embedded in metals at low temperatures, protecting the grating while creating robust sensors for aerospace and automotive components [cite: 46, 47].

## 8. Conclusion

Fiber Bragg Grating sensors have matured from a laboratory curiosity into a robust industrial technology. Their intrinsic advantages—EMI immunity, multiplexing, and durability—have made them indispensable in structural health monitoring, aerospace, and energy sectors. The field has evolved through significant milestones, from the holographic inscription method to the current era of femtosecond laser fabrication and AI-assisted interrogation.

However, challenges remain. Decoupling strain and temperature effects requires careful sensor design, and the cost of interrogation systems must decrease to compete with legacy electrical sensors in broader markets. The future of FBG technology is poised at the intersection of hardware and software: advanced "Lab-on-Fiber" devices will open new frontiers in biomedical sensing, while Deep Learning algorithms will enhance the resolution and capacity of sensor networks. As these technologies converge, FBG sensors will play a pivotal role in the digitalization of the physical world, serving as the nervous system of next-generation smart infrastructure and intelligent machines.

## 9. References

[cite: 33] Hong, C. S. (2016). Applications of FBG sensors in structural health monitoring and biomedical. *Zenodo*. [cite: 33]
[cite: 1] Li, H. N., et al. (2004). Applications of fiber Bragg grating sensors in structural health monitoring. *International Journal of High-Rise Buildings*. [cite: 1]
[cite: 53] Optical Society of America. (2016). Applications of FBG sensors. *APOS Conference*. [cite: 53]
[cite: 30] OFSCN. (2023). Structural monitoring of bridges and wind turbines. [cite: 30]
[cite: 31] Kahandawa, G. C., et al. (2012). FBG sensors for aerospace applications. *ResearchGate*. [cite: 31]
[cite: 16] Hill, K. O., et al. (1997). Working principle of a fiber Bragg grating sensor. *ResearchGate*. [cite: 16]
[cite: 2] Sensuron. (2023). Fiber Bragg Grating Sensors: Principles. [cite: 2]
[cite: 12] Tempsens. (2021). Fiber Bragg Grating Based Sensors. [cite: 12]
[cite: 4] Wseelink. (2025). Fiber Bragg Grating Sensor and How it Works. [cite: 4]
[cite: 5] HBK World. (2023). What is a Fiber Bragg Grating? [cite: 5]
[cite: 14] Sahota, J. K., Gupta, N., & Dhawan, D. (2020). Fiber Bragg grating sensors for monitoring of physical parameters: a comprehensive review. *Optical Engineering*, 59(6). [cite: 14]
[cite: 19] Sahota, J. K., et al. (2020). Fiber Bragg grating sensors for monitoring of physical parameters. *ResearchGate*. [cite: 19]
[cite: 3] Braunfelds, J., et al. (2025). Fiber Bragg Grating Sensors: A Comprehensive Review. *Sensors*, 25(7). [cite: 3]
[cite: 34] Propulsion Tech Journal. (2024). Fiber Bragg Grating sensors for monitoring. [cite: 34]
[cite: 54] Sahota, J. K., et al. (2020). Fiber Bragg grating sensors review. *Semantic Scholar*. [cite: 54]
[cite: 21] Canning, J. (2016). Historical development of Fiber Bragg grating sensors. *Optica*. [cite: 21]
[cite: 17] Wikipedia. (2024). Fiber Bragg Grating. [cite: 17]
[cite: 55] SPIE. (2018). History of FBG Device Development. [cite: 55]
[cite: 56] Laser Focus World. (2023). Leveraging three decades of FBG technology. [cite: 56]
[cite: 35] Ali, M., et al. (2023). Recent advancements in FBG sensor fabrication for biomedical. *PMC*. [cite: 35]
[cite: 20] MDPI Sensors. (2024). Recent advancements in FBG sensor fabrication. [cite: 20]
[cite: 46] ORNL. (2024). Embedded FBG sensors fabricated by ultrasonic additive manufacturing. [cite: 46]
[cite: 47] DOE. (2022). Low-temperature ultrasonic additive manufacturing for FBG. [cite: 47]
[cite: 6] MDPI Sensors. (2018). FBG liquid level sensor review. [cite: 6]
[cite: 40] OFSCN. (2023). FBG Liquid Level Sensor. [cite: 40]
[cite: 41] Pereira, K., et al. (2021). Liquid level measurement based on FBG. *Sensors*. [cite: 41]
[cite: 42] Semantic Scholar. (2022). FBG liquid level sensor system. [cite: 42]
[cite: 57] ResearchGate. (2025). Liquid-level sensor using FBG. [cite: 57]
[cite: 27] SPIE. (2025). Strain temperature monitoring and decoupling. [cite: 27]
[cite: 11] MDPI Batteries. (2023). Methods to decouple strain and temperature. [cite: 11]
[cite: 44] Optica. (2022). Decoupling strain and temperature in FBG. [cite: 44]
[cite: 58] SPIE. (2008). Decoupled temperature and strain measurements. [cite: 58]
[cite: 59] ResearchGate. (2021). New Method of Temperature and Strain Decoupling. [cite: 59]
[cite: 23] IEEE Sensors Reviews. (2025). Interrogation-Based Fiber-Optic Sensors: A Comprehensive Review. [cite: 23, 60]
[cite: 26] IEEE. (2025). Interrogation techniques for FBG sensors. [cite: 26]
[cite: 61] ResearchGate. (2015). Interrogation Techniques for Fiber Grating Sensors. [cite: 61]
[cite: 22] MDPI Sensors. (2017). FBG Sensors and Interrogation. [cite: 22]
[cite: 24] MDPI Sensors. (2017). Low cost FBG interrogation. [cite: 24]
[cite: 37] FiberGratings. (2024). FBG Accelerometers. [cite: 37]
[cite: 38] ResearchGate. (2025). Comprehensive Review on Sensitivity Determination in FBG Accelerometer. [cite: 38]
[cite: 62] ResearchGate. (2025). Fiber Bragg grating based acceleration sensors review. [cite: 62]
[cite: 39] MDPI Sensors. (2016). FBG based accelerometer working principle. [cite: 39]
[cite: 63] Safibra. (2024). FBG Accelerometer. [cite: 63]
[cite: 3] MDPI Sensors. (2025). Future research directions FBG sensors. [cite: 3]
[cite: 64] PMC. (2024). Future research directions FBG sensors. [cite: 64]
[cite: 9] FiberGratings. (2024). FBG sensors in Smart Cities. [cite: 9]
[cite: 10] ResearchGate. (2022). FBG sensors driven SHM using IoT. [cite: 10]
[cite: 15] Springer. (2024). FBG based sensors review of technology and SHM. [cite: 15]
[cite: 7] City University of London. (2023). FBG inclinometer probe. [cite: 7]
[cite: 32] ASTM. (2019). FBG tilt sensor inclinometer. [cite: 32]
[cite: 65] Ramalingam, N., et al. (2024). Cantilever-based biaxial FBG inclinometer. [cite: 65]
[cite: 66] ATGrating. (2024). FBG Tilt Sensor. [cite: 66]
[cite: 67] Technica. (2024). T510 Static Inclinometer. [cite: 67]
[cite: 17] Wikipedia. (2024). History of FBG. [cite: 17]
[cite: 18] Hill, K. O., & Meltz, G. (1997). Fiber Bragg Grating Technology Fundamentals. *Journal of Lightwave Technology*. [cite: 18]
[cite: 68] Semantic Scholar. (1997). Fiber Bragg grating technology fundamentals. [cite: 68]
[cite: 29] MDPI Sensors. (2018). FBG strain sensors review. [cite: 29]
[cite: 3] MDPI Sensors. (2025). FBG sensors for monitoring physical parameters. [cite: 3]
[cite: 54] Semantic Scholar. (2020). FBG sensors comprehensive review. [cite: 54]
[cite: 19] ResearchGate. (2020). FBG sensors comprehensive review. [cite: 19]
[cite: 64] PMC. (2024). Recent review FBG sensors. [cite: 64]
[cite: 43] MDPI Sensors. (2025). FBG sensors for ocean temperature and depth. [cite: 43]
[cite: 14] SPIE. (2020). FBG sensors comprehensive review. [cite: 14]
[cite: 69] SciSpace. (2020). FBG sensors review. [cite: 69]
[cite: 70] Scinapse. (2020). FBG sensors review. [cite: 70]
[cite: 25] PMC. (2017). State of the art interrogation techniques. [cite: 25]
[cite: 71] Semantic Scholar. (2015). FBG Interrogation Method. [cite: 71]
[cite: 72] MDPI Sensors. (2015). High resolution interrogation method. [cite: 72]
[cite: 73] MDPI Sensors. (2021). Interrogation techniques for FBG sensors. [cite: 73]
[cite: 60] ResearchGate. (2025). Interrogation Based Fiber Optic Sensors. [cite: 60]
[cite: 36] Frontiers. (2024). Lab-on-fiber FBG sensors review. [cite: 36]
[cite: 74] ResearchGate. (2019). Lab-on-fiber FBG sensors review. [cite: 74]
[cite: 51] PMC. (2016). Lab on Fiber Technology. [cite: 51]
[cite: 52] Core. (2016). Lab-on-fiber FBG sensors. [cite: 52]
[cite: 75] MDPI Photonics. (2022). Lab-on-fiber FBG sensors. [cite: 75]
[cite: 48] Optica. (2023). Challenges in FBG packaging for high temperature. [cite: 48]
[cite: 76] OFSCN. (2023). Challenges in FBG packaging. [cite: 76]
[cite: 45] ResearchGate. (2018). Packaging and Temperature Compensation of FBG. [cite: 45]
[cite: 28] MDPI Aerospace. (2025). Challenges in FBG packaging. [cite: 28]
[cite: 77] ResearchGate. (2025). Improvement in temperature sensitivity of FBG. [cite: 77]
[cite: 13] PMC. (2023). Typical sensitivity of FBG sensors. [cite: 13]
[cite: 78] ResearchGate. (2013). Strain coefficient versus temperature. [cite: 78]
[cite: 79] FBGS. (2024). How is the DTG wavelength changing. [cite: 79]
[cite: 80] METU. (2024). FBG strain gage. [cite: 80]
[cite: 81] PMC. (2021). Long-gauge FBG strain sensor. [cite: 81]
[cite: 49] MDPI Sensors. (2024). Machine learning FBG sensor demodulation. [cite: 49]
[cite: 8] MDPI Sensors. (2025). Machine learning FBG sensor demodulation. [cite: 8]
[cite: 82] Researcher.Life. (2025). Spectral demodulation of mixed linewidth FBG. [cite: 82]
[cite: 83] Optica. (2025). Machine learning FBG sensor demodulation. [cite: 83]
[cite: 50] ResearchGate. (2022). Spectral Demodulation of FBG based on Deep CNN. [cite: 50]

**Sources:**
1. [i-asem.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrGHav1BmjJ21b0LF5EVu7Sr_7kI37WXiCtYhvXLzoltlpjtM-TlmZi7ukmTQsmbgJmf_dgbspl6SVdeHo211TNJxGOZgWq3JTCZLUj_0ruu81zVFSoyfcjeqkTbTdbiFl685IUY5MePyrEG2YSiZ8CgUNHYhck1OKbFGC)
2. [sensuron.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3zgOPIl2vbxwOGjOm5J9PsnzYmIKlxeJLJrgvQtCglppWddlX5Gh-Bz15OPYqDbWzI2e_NdjBsIxvsdpOUqv6uWwA_r_qh5n7nOj-oDEhIJkeT69PLg2yvTDp8GjSvd8g9WqWRR3s0XKZE8Xv8asWi6VWx8VD8j_4GA==)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuCRwrqCHHZowAy0sBGZeUccKGG2sO1oY2ViZDtwdT0MgokLmHB2S5uLdxB60ewi4R7KTudVnjSjVXNSL_4uCFCfebja7QZda4HOpXjRbN7nQGOahBp8Y8bsW4mto=)
4. [wseelink.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElOAdjxA_YlqfLv3CGI3fdJp42cyV_G2r0VT7wurAnomneAv9J4tPFJ8YtOM64ocYRr1l3SKWT7sNj6bFtIhljNfjMHlcKycRCEWqO2qA7Ew_U7Jd4uNJ1NPD7ATtLbkRfE2l4ee9SkUW4tBwWB6mJbfEBEWuOpML_6CMj1aV5)
5. [hbkworld.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7gbd5lXXbHlU5uS1pW0VQi1TFIAmMijXpgeG3TXqbVx34aYsed-81MnQt4kC8VhFy0DWIq9esRDqANO5K4XR2GPFS7FEHUfprmcAp2zzr0aymoSHq4QoXjGovFoivj00p9iftbQ_6pmQqw9FmzvtnQ3BEvwbiwatYijepssaYIRGe1Nj72ouLj60cMsdpdlL46yWEnGyFO9o8nIFbjwUkJtXEymDwO1V8LlL2q5kTluXUSSwVHQIJqvQVgetzTEZEzDDsHsR4b8AaFiLP1eU=)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYzH3cyBoRu465Js1L06iUd2JK6VkNHzrxSuTrf2TidhkD3FNW0sCJOxdtpiAc1OY0Tp6QcusKmf4_fuWfReQKuNotF43MtC9kAX2dDzuOgu__YCTJHaaR79MjwVo=)
7. [city.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx5MPwDvRD6SDVRxCY35aVBMnZNO_CqpEuZU3cn1AZT7013LXuLAzytJ8yE22YLW_yAPbUqUUeJG_gKDHjvYwhwhniyZcE04-_8S7RcvrYBXMViuqZQHQGanG5TJuG9q6_ojmZBzSD4B_ohNYoQYkkxNrDY-dt5uH-kGGGm_fVB5vlGsbnrge4fFimcYQkGP_tvjBEhyeM-MTn_Os=)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6seTgJYKj6jWAcAn6O1BfOCux182CgDNKIiWBKeB1_J90PLwo6i0eZaCRb7nNkfkmPzVVxpWLm8BEEGLKsLUL3-htY7edtTdb128i4aqglxC647zFrwfmRRB7JWME)
9. [fibergratings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZrFVpY4gttnGxmX36u2REUXjLf-4tZFjpPnMZ-RjaGs_uVi6krD-ZYbSHxyRFvU0Hf3MbmoKY_FI6-J2CxZ1Fom_BQB5LBHr1FajPOwMFWTzjC-guCowjT_VL9SeBEFINhkDRExDrwUs_sS2tsooZBVS41Xni4TSN873JiYQz7Huh6Qty2-tVSIu0GtKe1BIbvOJlbkwuNkpauw==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0OxG6ifD5q2lFH8ap5yUN0GeMHcMrr77LFIo8NnV21hK36_VX3L02PJ5G6mfNDzngs0qjHFWjJwRriZ3RmroSPOKiJ9BuAQKqtujLZSJyBgbutu1gKwhaUOH2rAwbYgod5BnYGlrkj137JlL9WSL-Jksn5-M0ohxbaCkQh48oack7EcYEc_a5VtfjOcvwCSaLXrJo3xgd1NL9rGpJTo-Ie2xjWt3MPxdZYyP-Gu5YCsSrZRE6eWD_53CUwfS3hRqAABPDDXdP6rgEgp52wO4rN0XiFxF2U9PPg42DtsqOZ8iS2m7Z8JjHqirNFuTxx792NDU-YMOMHkAFsNTtCOE0y3mfpfLNFGJiZsMtMHivdffVesH03zwGJEWl1bcMcWeNLX5m_yBpWtj6Iu-VKAE0MA==)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgUjdGlU9Vhj0z9BOJIt42S8qf_lvjQsrcpq1FR2U8cX3vecMcBGQkjta0cqe2p_8B0iGVCw5ALJIeJPFi8d8aAsFV71dzImRy8OEY36QMfyRtFMPDqIB_6sI=)
12. [tempsens.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2p39YbUdv_FDZSqcxQ5Sx5b57ModF8NljVoqiaEEPWECkDz2yC1DsnJ40tBXWB7isHkU9ZkcdBDervzACCq6smTK2nqQgtJlk84YoC_yPXsPReTzWcJHALXaAvHz4AGv3_8xZDlKk3MDJOKg_E1S4xg==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEirqrgKOGViJxmwGoKMuS_ot4cCOIBFiaaGqct_yGtWDGBMFJizdHIVIgYc8WzVuuxBVniN-yOB0BdO0gIMLe6nDUvYPxZFVY6BUHKG0zjZTCs9N7GuCCaBG9-kzl2kA7kVFvQqMHp)
14. [spiedigitallibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFl1QK8delDndjglS6eRjqjuq4clqSSwa4F5ZrgSIQtlvW5FANQHYoKCmmp9gElrI8kZYV0iM67Mj0qZRdzrv2t0ofxmSjgoU9dn8Up73cKe9jzdffJHRhrTfXGkqPEo-9NfwJkBls4EjMpzIjmMlrpnzJcrIeX5zQnhKCvGw1EcwgtCyGlNWNQF3D_pXixvqs1IOjVu8HU7v4fZTDMfqcSSuAKYmNKEWN9E4ahrlu396vfWlxqCrIMJhc6EFnILGgkW95FEQJTyytJX9JvR_jeo-8hYZ-0jD2lItAzh35E8GVwnmcZlzMdnMSGp7EF)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJJYHta_TYS2xUQR6rLmPqO35Mmc4iBDKI8eh6MCtKSW4wjVsbsIdB21d9_NyPJI1-b4F0JWh-aLJOuTpHjm4bgc-T2Kj_ONo9UblNqxqx4Yu-ITiCuffJDrNvb22JI1h9JxTRbid1dfgTUH4ecCcyqNSF1_G7H9ySFZj3m9jcqKCBTkT5BRXAY0lO5tlEpWhBdMDxOkOv6Vipa0-sPBKgS_MiRXqNcCNnGjoa19PInG6ZLZahLxysqI4KnUCVSYhlrAMqJQBZTeerTleLFrzb7C_iY8byjPLg08JwrMfzQqS62BQLSjctvLV84gs3cd7UjbhA33LvOWOpiyJmzaeEkw==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnFQC0WE9QTzu7WmbQ6TpWBn5tnP4NjkSU7UD88-GyRBMq0WrkHumr96FL-4I93ahS2OoiovMRqHGjc5BTzLW96Kq2qh8CuuKlO3Om3Lezc-_wPMwvsk8w8oXz_w4opEieK-VW9vqOVV-xu1vhEac9zocxxEvX8C_IKwMNwU2nCeldQddXM6k47u77vMNhqtIUVeSGFOCxdLyfQNZv7ljAgAYrs4FddMa8n-12N_fxbNw7RJKgk-Dw50_AV_c=)
17. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Grb6SArIvz0JKBtuJDuocbUrTWtYcY2CKCjwH_oUFVYIrXLN6Y9VB4SoBVZASCUUwRx-XCaq-PuPRVY0ot_DTgh-CnESyS7Uz_0sgb9OXvIBdxhe6SDnUHeLBMHzQOi6XoWxBj0=)
18. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0B01sPnhu7xqpOUbBjQDzdeZ_8Mw_rQPNxp2uecNW_3Dj2XmQWpfaAmfwAl3wWPaoQLYgg5Dl721ZZiel6XQ2Tx4lWEKQM4vAaK1b78pimgVEgDpiONvmQoYlSr0QoLFWlfEXDqzNeeoRA==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAH9m0B4qfT72Neeq5pHQfzzBsnZRp8N93rizqYR0e-HqewwpXLS6p7B8NEOI6n6TlF4k4kylmJ54qElEer-u4PkV9PKNeGgp2khDVvoEr6kUFIGVg5KCF7ho3IzflwtTcHOfseW3u0pGF2GHCDuMJSijja0VSb2AxciWJpX_lVCIcdw-IIX6YtJ5KqworF813a5NULwx-QqzFzF-WfeE1cIPccwdH5IihkSukiekBgapiV-OO4gTGIA5jP4nulC9P)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRi5phmV5dp8UdjT7ElKfoJWAVDWZiIWZ5Jo6LnT3eDw-Mk3_YKVIqJqXdeXTUpe-id-hsZ3IMVv3JhvCuGvw8BRZ6qn6odYiUVh1okrfKFiZNErE5dAvPucRtw==)
21. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuw_g35pKZDgSDdHK7-7t6YVFot3q8fytohqoHZspyTnSVWudeIDffT60FjJE357EOLW6El_50nKjARsK0fK1QxAAHYZFBFx9tyKXtM7t8DUdKwtAjamb0sJkxW8WtI2v_HW5uaKNfH7tF5w==)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLl1aMovL9ujpMKbA-evMcVXcem5j0QgCVbKOwO2zPzDGLo1E6DLigqvA7MEGSr9QTCv-zL77IHM57gdS_ALp8ep9NJUB1-AOVM8rwAa_spC4dxXvmK5lOq4eYXJk)
23. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkYBu7riL8wC9qIAv56iTK3DUYk4LV2GigmXDw04HyF8JEQtEy_IivZjem3EW1m7ihNgzvJGdIdoMeThJ38KSmGe3-ta2KQdweH37AzSizFediCX8MZErrSpQM3jVpPK74t0E=)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEljWEEdVXWnRO65FDdWNOz1aGZidu4TFdQSodlQeaQxjBpZ9T9pD_Qp85M389SVPG119vDSpmsk38f3PieB-teUyaRrXesGJk4k_FZKlWV7gH7NnawfNjU1kqwcHb9)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4J8a6vwhlxTvyJur2xv596Vhs7ouyKjejxG_DK8et1d8fTkMmHmhsOCfBAWgaxxZTdl5C0kEeF0zmqu5GFqHCLjHlt2FK0zF5Swd4rwWePcqUhgkcG_ng2kflpTDGYTaNRjVrilc=)
26. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqaV34wcB58GjhOrBclpdCqeMsYt-plq4pCL2yXD38Tll5fYSg4rUmHXP8JMVhbFJlAgJnywAw2L30soff0E4YmzyUTgVa1QVXhuLS2mb_f6bOFd23Tsi5F_bdylO4CoxAEyUHzSI79ePzfkrHup0uU_r1Pg==)
27. [spiedigitallibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8mQUJhN-OoTEAIiof5n6IkKpb9g1v6UKHdtPR3wHkvvi3DktpRqcJWkxLD-qHrFxzOfJW4hvRkzkLEo_WJ59q50SwFZNZZTCoiHND87jTmnXjm8UYLR6JIbRonlugqR9NyiC476GQQrXlhMvCraW6756j4CErN2Zq-1QinuGQA2GzWrOjDJ4cSPVCsiqZjVyU_Hx_ne46uuMchQx4JYDbMg4FdXQ-b_sBer7KZCIYre1HUYTF3lSGGLA1AIgA0GU96EJ0gkN30nYCJUkFTCGc1sVfxHCpVtggfmMHw5vAm1SEV_oyafB0sNX9YI=)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2lZIBXIGhktP62dw_GkLbjZ_VdVtYrD3tqM9qRAx0Zc6zxY-pyj2Ef565fHKv0bS5VNK8z0jOrHZ1dOn2UoPZhCX7JsW6FaQnQa6Uww7Y_sW8dlsKgDdhCqSI)
29. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeEwIPFDsYBIswxMzxMRN5DSQVQKXNzqfMGINKfu3gdgS1mRzj2dBoYIOvcIHZm642ioTum-neSxe3iJRhfZhB57x2AQOrySu6FXO7DZgMhMdDkXeld_P84LSgz7w=)
30. [ofscn.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ8KJhRKAX7B2fvFWJG98-auA0cZYOwVC7h17myU4saT71B4462DxnNNxhWU0ZZRj-kwXWtAH8EYXBKMTRpk0CZpk5Sfb0cZbMNAalOpAVa6fq9CRfBZqWGAOsuBwJytxocXLp5sqCyrRLN0LTjeMe-Q==)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmunO_RLc7a3g5oZt_5gRjov3idsZ6FOPgOtBKniaTF5upS8HvxWYeKNpSMWGIaOrhnwB_JngoiVJoiwoOHOF8Ry3ueQoqhaTbmfqBORvIP5tEfTrWKw1pmOLJUmzwBsrEVflKOEH_TsSB-oXIWUr9PQt-2-XrcN6wkbLm6GFQuCFHMBvOtPtqseJNWkAetvgsELiN2WGL1H4KSIQMin8LldlS8SWkNfRyg7SfnuLTyw==)
32. [astm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsreG-1FnkqqvBJqcdvBp1f1w4_o1o17v2kS6Jcrt_YENrPi9VT_zhf9x2DWO4GApxkdA2S6YSAMU3yi_Jd1ijYaeLh6Ji7QCx3SMr-kt0dXcF65UvsYwFLBI=)
33. [zenodo.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC5363z9JV-vezad51P0h9ewrYM4cjcnW5Rc80ffCUE3hWX-Do4Hc0vhA5oie61aIoBinKUtKbx6C3blLMHntn5YbvD_dBSX-TccLXMIziY4IIxk4WWH2NjvIofhoaIu7xgvnG1Qvd-ZkIYkBVZBZHL8l1o7bnYw==)
34. [propulsiontechjournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XWLQ5vQfAZA0t-rlpwJM2lmkPRjJzah-gbYsZH83eLQdESe2jKZoEZeEQkYG2hF22APPFBeSF76CtWUTtva42Az7CY6ehBDcs7QZaKR_zxJ2cNH0Bo90o_vVhisYHp8Ic8nya_EVeeWgIUekM-wZ_LUvdZsY0U3uggEISMMoiI-Ph9ZFLuYOW5FU82g=)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG70WC1FhIx1biMTA6OlZvgxMqEKWYSHHFbqYvWolyZxfN9CRtrDUxbII3YUqOxO5_nCeyJ2LngwXlVYKMXqbC6zje0HeC79DeqcPov_Y-eOAJGDk7RJeHJdsumMrn-OSnGScx8qGs=)
36. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj7yu9cbDiCyY-mJouxHS89E8vuiIsefxLBzqWwUk4X75rw7sl2njl4zoYYpnwLpM78_thdVw-FQuFRuMEBIkSmgbibiYSthKZAzCmeQYXCKqZHsIckYtPVtJS8S9L0Ef1F9vWIWSRacLlh-k2uTfoCnq5jkB6AbBOabnOl1uQCcmwX3yQX4XLaPeA0J5lqD5jc2gjNmibYpay_rOjCz_PMp6w)
37. [fibergratings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENYDZ1f2S0sHo9KZamV3RlIxyalBfqJ1xbP7yc27a99ycALSNp0ppHJiOVIxoBOgoMR-sjESOgtiyT8IVLgIgec99ZpPuR8dp9HX-iNTvcrj6teUHoaVlYkR2pXPQ4I-8M8vNYH63oq4dbSHWqyFfHeAixPjkgMQ==)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEzNZZEiVWV410leGXeTG9LuNYhH6IAlknbn_MFfJTEMeYKJvJl9t84LYLhfbIfsHEtw8_kO5dc4XGRuQvCushozvI0YDe61DKF-QqJn18NH0O_IARavCQEvl23ZZLlTHnvGcfSsbhhaJ0U1QlvFzcwgoxVV73nw1-o04SLYExC4QsUdjvCUprC7sMz3kl946cKaRRyjMRmdriCr8FA1xCHzTWsE4mdhi0637K_9J9j4KpQcvVXN9ZiZGtMuF1UQ==)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0y-hY-wcDkKRFlC9B5rTcXAA0_TJGLH7iFLguOXcWAOYAwp51FtOwTe8PIYOeUmSQsJ8K8jhBuwMPluJyaawSe_KdfHuSeJzbOO_0t2bGhrAKyTVh-iKJiCGL9Q==)
40. [ofscn.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZOv7DeiVywppU78nOwzDowQ1s2kLUUZTPPRS8Eok2pUHa8KnKb0DqavpqE3QrZjYSmyqd5hoZfqf1-vlPogHtayymQITd2uL36pNKCF_VF4nxqfyPdEkVz9GpeR4JRJ5w09c31U9zs1Y=)
41. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX1tjCL6_b-a-y5mUhFXMIh3sG60CX1cPtpKiNWHtzC9c2hpyhLZFI7iXvTGGSjW431coq1VCAaK5BCWHOmBsCQmk_533jPwytp5F_Ln2LXguO1ezICbQb3L7Jy-2s)
42. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTrwr5jdLb1mo1qYlng0VzMk8pRCAur8QnM6qwndyn-eGIUT5e4Q0vDt4W7t30Lod8wAy0hWNv-IzDyM7CVqt-3VuJSaL9s__bQbjy2X1KUELKme567ZKc_Gy2w6hhfGfh1q6T3ZSdWoFXzz4ARtCM9Q6Fa7QfE-EIfqtMMi1r4VhInw==)
43. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNsL0ik6T3A7qDYSUW4YDsY8ZA3GC4AKvLgKZR23-6-afqv2SeuYZR8w1GbnfG8h1RqqgdmwYZozo_X6TFirsfCuuAX4X4rKxBda0rZFc5qr5J-hfISCNMcirPPA==)
44. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGpl2MEp4LurrJ-UqhzpCvNhRToHOyW8ebwNHTfPea-s77OHjTqrmFREwQnLJyimfEANLX_8IbKSMkerJhI3nofDVIjqX49W0nTvZ5ic7kt6fK_9l1Hk-SGlzAVFypniaeHxNYnVfL5m05lA==)
45. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2R07xrLzz4xNoXLK-btRBZXJXkccBVys9hPqalBKwnBW_3IJGcJB3IyLvUg6-2_GscEbzKLjHToCstUnZvgwF38He1L4I7LAGzdiN30XdX7yS3J2JA5DiD2yisOcIbgPe_KfDBv8ASvwRONSOyNtd0mFpQpgd500xE-GBLkjYRpVZuXDmFoE8W1xXc5yp-ZD0m5hMTb3WTZHLmuwR8jJkH0PhDJjTTbr8wuM_4euESyevUu7Nvc_ib-4KlgbdJU4Bfw==)
46. [ornl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXeTv0-TTp9_0RE113ufdB4AsUzeZQ_0aD7KnApWgRwY2da0CkdjMo-CBe9xqiOq0chJQviFcLruSdDbrxbvtDIXj57cjJqbYbBsRfPwl2iBMZ2JEj0_WrOro0qo7V4Xfr1ltkS0yMr3Dk752w1FeI03gY0bUti6xlxB60mel6w049PgrNv5PxsjEFrzJ8S5Av56dHHLv9gkYgja7G_yc=)
47. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4EOn9wiMC0Hpf8mi-CDcVz3uSbsb1bUmVfLLHtOwuqq2sOiwK_1cLKCd9wjHvDfMPW2FtK7Kq64b1pqnl_vynWoXQSfGPAYG5BVgixoaqvbw3QHBen3i5KujbIA7nFQ==)
48. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjqI0ejsFqrYNfYLrfnHGNdTFJc2xX70n_fjCr904D9TYBpnmmxBsUL6akbaG3_x4A9ExrpG_A4QHDSC4NMM2zllMIgzajuwrscRXlmPCyRLW1PkrsrrcQD8W-LYtVM0HCLdOuDrkrLLyjA==)
49. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi0JBviw9zGi2BqNV4njmV_0MAZ4EVIyxgkTcu8CPa2xk00fBLp4WFiC78w-voXSxPq10D1jYIWkbGPtDhpltf2rFOjUQWhB0qZVMbk1VFNyyp-W07EbXYlkHbNC_r)
50. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6jHnNYkR4yFAC0LCxtXCkcpTj1Diz9DxVgA2_E0uCowV4OI1VKJhBCaEzc_J-s9Sob8oMzmbCxC2HcLdGF3o7AO4S8XBFXt4ihXhySmrcosS4rfSKAKURuOYCBzwWgta3-AHD8B3xZuwdsuvizRRE-m6AWEek3xXsdDr95fTGjTJRPqyLhIEEqiC7JrequQ-9yqmNORH9Mt-UfLa9DFUIy5B6t6tqw9yncNCtDDuJcZAJrFk5irJdgtVVUZwYH4GWXkSGvnLJEA==)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZecmHZSjuupE9GQvoOnQIEqCtPV5g4SQjSL9gLaG29qWXNlmnPW4Px3YOjTi2m9Rm1p4yfDw3KRuefTaxBSSzoqjK-tOu2-C4N5SIqL-0XE47fJPh6zByuGD_g_AfE0u1err3Wf4=)
52. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY0VNv61VBZ4mUKOoHjBhImnU5wU76lTFP1ADEpg_m5vXngkCaUInM_-0iZEKBgObA_nP9hZD4DQK8F28mid9OPerWWqs1fu6XOhZAXNAOjoLSrLbh-QATnuLZkHpj2vpS)
53. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6SPrGZvDLU_MdFP1YtVH1M9c98xstgceFfUMpecQN9QZ6dnKPikndaMlcZTyfzU8Mu_CkyQ__BOV27axHSf-EgkQ-6I2zLWjHHelzDpvfszShdy-kxB1RzM3IuTS9wLV1bThltMgamtfVLsJ0)
54. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW4pfOv375ApgcAZeQPQSaRcjA3gRtYZNQrzSP9Pi6pNfx2ArTZKVpJNLew7keYYd09ncOo40hy89NOyBWcVlpoOB8YAIei2Xpck172sLq4YSuFSGfbaOeDqzOlAvkbaIPZjMIN5dONZxt1NWo67u2f0-E1PNJTJJtlSTKQF_16c8V_cHccuKKA6MfpnD1saJRQrE1PpPoZcjACDqqLvSVKf7490_1IOPi_TpdNunj112mtfR2boGBN_5BvCMXW0Kb)
55. [spiedigitallibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsqGG6VXEQ_zzT5WLpF4seItqDlcuoNVvaUyClNjxw3K2W5qDl-RUUYSvWFgZ7_Prh1kB4RGbXBuAoh8YFZXqTv7RNnsl01HKOLdNnen7zGBlEJY72XjmX93QzfbS671NZmaOJULZa1ljNSqjBWx5jC0Q-t4HNguZB95W1mnfnuSvkAcAqRBjux3FiCUqRWboz9WnSnY81WGZspa8d96Gg7tvefWaM9pkPET3EUI0Bib-AgtIVnXEK8wo2Fl9_OZt-WYQ9MSehqLGvfZ6cVkpkr2v6c96LwU_aGcSS)
56. [laserfocusworld.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDJKo2OvUG5NeTitk53gQrCd_R95dxkyegwDnsEdxhwM-nQDa18EW0JfXXgmL4CdDErAjIAna_cwo7iJAwEZiOcML688v70VzE9rRqcPRdLkH_7iqOoRU5cBbpNeKg6WszwEINrU1gemoNlH3KKpCQxeg3diwZtngBmfdoZLMaK8f2Hun6lYj1pXmIhC9JyJqDkJ0JhurgptEWWLXbGDrY2IMSzeSyPu-_8G6aFm5rZH53iFH-Hdyuzzc_jC7BA67TTCdpZe9h2WU1)
57. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELpYyFKxC9I5_M7LLzmM2btgYKzgngD5mIDlajB1Gi3qvtBwIMNgDDXko5A_1AfFKFJv1bHzS6GK3qIwbXTMKXxebcRKSvNCba8TQpwoowbzL5p-MiljhRw9pKjDYAe5U9mZcQ89CUDROqwoRmEJrYUBrE5XtMcYxyVT1b46PyDhzHmGxQZy0IiRz0H6buRp721Uv6Vmq7NkXauP5jhKuzOqV6BqzcPh5Ga4FFVOd0xUrvEiGdWvlGHE4K6OU=)
58. [spiedigitallibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED6Wje8Xk-ND1w2AX0KCg3C8xnWqEEoQOXphaaeKj0J8wwJsyoR32lnr8oqmyySFsg-JP7FhzGLeb4zmoZxavUcRxP2zUFThOe4_LfK65bAiucpUmef7IJc6zu5dmLKhMi-GxxaZYPK6rEwcH4u0OHipIOPQgfZwI0AIdB8OSZGxsdEvhr516j-4Oyx41RMrlTGOK3032ydu88Mb-297aOfqRi-6qtSZtAjrblwcchpDYZ71nDWjj8xDZxKOCc7lJIAvghCLjzyd6BV7PZjnsFdPIBs6n9DJGWVEZ1lWHeOBBWgOWkYXKuNWk=)
59. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXG9wdUTxoBnIQM0AqvaERva9YK1mgOwqddsaUAFJmHa-MWQGZ5VHTArOboy26hSn-Odiu2ewo1bVtyzlBuvtfFpRZBb0V4t7NanCdDMQIDpYva8ZV9fz1X9I9trvER2uiBqPIL3n4QOMerej2_soTmV1ClnVRfEq5GO8PEWpEC3kvvVaHoCAAdFhMzR63mIVLpQ_9580PvEIZ2cr87flRv09PrRvjz2P3PVO-zJlLz8YKk9Ui6qSoueiyOQQK6pwLNkUR4W5Dnnb9BKQ=)
60. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErro4r0iw3Six75Lomi3cPMHWhlgY0AMoIKiMJSf4pd7UMbonWmZdtjjWvdbqIaSXXhQS6dCr-ecVH0Nvbr6tYPmzK7TfblVRTmdP-m6XZapAsTp9gk2LX18WqTJGMYhOtTuW1rufOXYp7V-quunOCpDapweePFPB05latiLNNEUbWUXlL0gg3kOOIKCflVPJAKdoXYMoKm4n6hC2I5JD4D01BHT2fei--HNgI5uX4XyB8jPIuzSO0NyarVJxFsHas2q_X-_J3NcFVjJHW)
61. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzTfnlb_R7j_xXtXCYPK89d9_TsRPGxUFrMTHRb8u6iFnPMQpYFva1WTOGmfUe4DbnLWknRacQo9zWd_GAu4GdXFaM5hGte17vWBTMjiDE_k0GT76IwCz3AHtW3DcGHbls4U-nQqEbtduZlzeNYeUkvbWE6gYjL0VHmCrDtDKnxwG7-RUrIDmquirOddYhu_me7KvIrIN_-DNss_uBVWLLI1W0BREVf2HWFvw_-6rpbIsEtBjyHY1qR0Soig==)
62. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz2lydM933aKy0w_PDz5rCIgvokTAaGMng9S2zCatFLG-4YWW2ZgxiDIE_e1jvS94Dd20k5eA2OIPku3inBoUHuN7Xq45nfPHHCJ_Or2gF0VKmULVfkz2AAfktoeeoCfYixTPqEfjQaG8e7kJO0L3vCUjedsYoKlfhWEc2_9DdtNk7erU4FG4iftDRxGumltfnaUnKGCxT9h5Lizkhd0=)
63. [safibra.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgNBMlyEC3WWgXi3loVR71fP0OSiXdvUqKjwnUS4ptQuKPzzSXMBUaWyHqz70jrlKYACQsOhfZy6WSl1v5-pHa5nV0MiK_0wPcoIcoUk0ksnSLp_ZduxQ2iniKqKxcIPFyaAi4)
64. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnBbsrZakOZB2bgkrzmRFfBLgnduGTwiAbFhBMTY81NrCeqeb2LwY33B1X5Z0wnkeP5H525cjt-IaJnps8XbII7bMj-a0pdh5I-JdrhD4vHR66bbVmtCpqciRSGg7UErB2W3JjKue9)
65. [icm.edu.pl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY9cTh1vGv2UqC9tFjCN3DpvTdBDy1VABTWiuSTPlkGqVUYwDcCnCko_Qx8WduiVQBwbYrBuElfi8ZwFF09kFTIRPSHdXpFNY2OxkedHF3AmpVT5tIDy5Po3mj-Q4DDnDvrUh8DpgIw-GcWfVvge_qf3EKPvmxfnCHKuPYRVRQdDBq8HzxHby51zZCIwftoxBHT9N-h2_AohPXBykFvhYQk1DDnKKtJvyxDfPpE4OGMJtDpEhepmsG0-G6t174tKEa)
66. [atgrating.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEpKBxZkYDBUmawD9NAxUjLT-TLXzWCZdkMXGDKWYoTf28ffzkzZ35GZANA1PFnhyWkE2iWD-7lfCZviMVFZqCBHM0YOXvzONE7cvPi8TnhzD1K_g1swJVBAOPvisX0A4EqrjfAlx7Tr8DbCs=)
67. [technicasa.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh8BbF3M3lR7m27UmTbaGfaQWJw0wre6oGowQiGe5if8flhsGa2RGvNragYTizp8_WV7GOhXn7N_8Ynh7MgBZIvL2sFZmk-IwXan8cs0jhBaCdj8EFD_Itg3pdLXfZXoN4dklntUiX6_NYh3GLqz3-f-h1)
68. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrlhU8fslSNb0XHGpM2gDptAH6Vy9KUuGQU67V-bz1zm7xzpMealzap2t8jfD4wUaJO42x2CgOZCNH_qeIb9bJtpzSfJ4-FeDHOj0mM0V3CXcwyd55PFhd167nkg5jsuWOjcpj0PSakSf0jIluJVDXIIM9QnMSCs3yaJKpPXI5fORCWKrASjvD_7U_p5P3j9XxolnHfR9mdgLRA83gM1gKQ1p_S2rL-2QSJzAS6wMwF0-q2WGv73Iii8eE1-zJKQ==)
69. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG715vEzx3106tMiVJlMxwj8eZhE_IfV1wKCoP3wu_M9XjYqj8zkbfRXHJhRoe_6fnKS6DG0RyxJX3D_jWwF3xAn9Sx1HXBY8BNkPsl26llQvhQyLbPylrEJRnEBGIXYQVxwHwVvyj6qt5kTO4MBCvvYezWaxYEiz7s2AXjmCc6jUe1bKPdiwNoMrGO9ZqeJIJVgg==)
70. [scinapse.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKTKbCtY3MtATt-7F4AYPoPiCWkrPj2CslbOg3MNT68FJLjqWhyobUQwow7i2z-y9EonREbdqn7w_4cBsD4WQ6SAyjseG_-PhxYkX4EFF_SQl175_WY11vNJByQxle)
71. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhWCnz8MB1-d7IK2GCA7U1JN6zE_958m4nCALF5SAYnstQgemq2Aza-au28FkvLBbZNkIzbjlsUc_jUXHa0b2liUO0MLpcrK6LzPXUzt2fBVI139c1cVCFFVaqVIA2q6SbOR2HtsqWSpNM5rOFAeqWDZJoLUc3nFtB0GcS4_BC9JhEE0u2byTPuCBsy_IBEme6MatNsekZlGRxnXPd9QSEwhJvCzJL07zQRkbtD_LpDqodxLCj6TBhscr71IGH7g==)
72. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHszls0AdHYeRv2Wim9ccXUvcr64ymB73byYhMIUiDcMn94ymCNtqSkzwygmbpppkkb9PQ4hJ1Z2V3m-x0r6hoE-SqMHD-I5ZbXPazAdWVTzdCQ0ZOI5yi0B9nadnlX)
73. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQpAbDEnWOYmV8icqqwxWXIc4G_1zSSywIO3Gk1IoFiuO4jJNqLTozkkLdSQpzkpGbZyZoo6Jqtb79Scwz0T2cnALPAqQ-aW3DLK3lUfiVvNp933VhRRwBk-KESNu-)
74. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz_K6HjdlUuG8iOZdibEBnWBlZTOCXFNRxlTWi1BlFhu83GVX9WXegz3dLrTWvbLn4-QM4s_wRcMvGfgCtako2s-ERMBPYnCeWxSsjfhIofgTmDysWZUSJjaVY6H_OLx9QakM07_DiTSWSUlDYsnyTkVf3VR85AiuHbi_GuHJS3ZFb-ZQXHbcWEZ1L1plSjMraaMQODJWtPhgQ2KFyNaTxTwGXdEXMQDb_)
75. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3O06IrqPZz9UBQwQPk6fo9ZPnP3RzirPSaXODF-2qm_PfL7fOTjp7MTgzi3xmf3VaWC02nrZYPWWjKSs2YAqh_10RsNqYaGD_RbsnVBHddsifIEjOJEoK24g=)
76. [ofscn.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERy26Ane7OPXMCESVXt5vWykLxtryt9DTXX2afEJ09-c4e9W2rRLQBbRJIk4qTFh7GKmsSqGMRN4gsTEA6ikQgAQza79s23Bc-IaHLmIC86wXs4_X7c--wi-hh-Bs5cJoUkUkaNvwecnfZ)
77. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhDgI80jfADE7XPFSiHW9SXs0rPDav4ADs9ZqqrggYFMQ2fd-M3AjF7efNzNSwU9GrhliVDABKnMKqUStqMCKKIbJsbfvjwkC1KZ-KWz7IOJ7rOhkWwhUIHP6aJu2-p9HQkS5taZ7Zp7JjWyAgBwq0piSzGpefkjU4VPcBJaCrmo6UGv77PSzzCuKFpaFmY_k_CwNVzeuhMk0wmBzwTgWxSGQXGou5ChBEMIx3HeUnAWNXtvqFFAy6)
78. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFybFganC5cbWxIh7LjD7J1MqlNP-INNPCm72aEKjzyrIJsj08LlUTRcYJTT-zTjt0xhGIyWXeWg_nU2uPv5UZREvSAwGe3mYTpsEe0OpvssIhb3VrJ_8uW1l8SW26sYiOCsjNnM9okX-7EVgRPc_wPXBAWdGRAv6aDC8llTtRxUmz6erXEHuukQGvkX1yWTqiQR79O1Ko1CUKunhx2pXNDR3EjR_eko3iYNd0hD5MtOWg1ymsFeBlVRemA-Jlv)
79. [fbgs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpl6B_6UyLSMZqYgDmNsWc3powl_0lYKB4FDU7NQWUof7EypagA4LeRsmsdOUQxZqIXEaejvtBDC0DepSiPeFxGLEl9dE2RVG-V__4KH82x1AKvc0mPrTQnwf9otukYofWoeJFplItgMzI3-1IwI5vKW4767Tgy2O_fRBr0D4HmmltXNTaUspGXA==)
80. [metu.edu.tr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExE0Vx1yqv6oefot2bMlsUoGynot72ajijnLZuAPIHhgMN1wHfFryBe7nBGyTIupgUUjYlegyggVTXBV1dl1WRycy6EUtwYTKkW4seYx3JPTNcmwg56i-OgL7XvkC35ybPcUFlvS3o0Xt3)
81. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNxMMXCNK_lyRqFEIi1vDB8irt1hv_US6L_KsY0tBsoYn-oSu91zSj3GEqmCE8NP42g2n8nS4YN3UsAHKQBA2IrokLufSLOqYuHfrOGANYfRycVn-0XJjL4l6dfnC8B5yLI9tQDM=)
82. [researcher.life](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcGdi3aqwfOVRTNNTq2kMtx6fO2np1cACQ_iVoGrwS3ecLGdfzp_w91_iRSjr8kLsh62DI_DeM_DM5HHySZexhUDrCrTXA-EVMkTxYB13O-1I8TLW1eT6t0ldpkHFPj0XzeMq_vyS-S8sOOUGAZUjl_l64bmrUasOdbttuzSoJjnECgJZNxa4YCe0u69-Vc22dTaUll3afRuLeblvL4--EdT7xy8eDZWy-L_YLw39qSPkelNaga0lnhIwKFepcHs-wS-DZjJMC6BWKpRs8t_IldZcI9MzrYMACdVYUXLzB-YENMFyG5JxErX2x1S0ZhJTz)
83. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfjgJyPLzEOPXbEJcycGCI5oHMEJuipVACWFLAyVs2VP_7_aAiTW_4mvPRNAu3BvpQk-ckbVpCQzAVX0Lxc6izcd9IjvchTrfT8q5haVGEqN4L4VYfPFGo62BZ4BCu9ipNncGebvV7S72tcP6U)
