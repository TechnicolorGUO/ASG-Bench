# Literature Review: Heart Rate Variability in Psychology- A Review of HRV Indices and an Analysis Tutorial.

*Generated on: 2025-12-26 17:31:02*
*Progress: [6/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Heart_Rate_Variability_in_Psychology-_A_Review_of_HRV_Indice_20251226_173102.md*
---

# Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial

**Key Points**
*   **Heart Rate Variability (HRV)** is a robust biomarker reflecting the interplay between the parasympathetic and sympathetic branches of the autonomic nervous system (ANS), serving as a proxy for emotional regulation, cognitive flexibility, and psychopathological status.
*   **Theoretical Frameworks:** The field is dominated by the **Neurovisceral Integration Model (NIM)**, which links prefrontal cortex activity to cardiac vagal tone, and the **Vagal Tank Theory**, which views self-regulation as a finite physiological resource managed through resting, reactivity, and recovery phases.
*   **Methodological Controversy:** The traditional **LF/HF ratio** (Low Frequency/High Frequency) has been widely criticized as an inaccurate measure of "sympathovagal balance," with recent literature urging a shift toward vagally-mediated indices like **RMSSD** and **HF-HRV**.
*   **Technological Evolution:** While software like **Kubios** remains a gold standard for GUI-based analysis, there is a significant shift toward open-source Python toolkits (e.g., **NeuroKit2**) to enhance reproducibility and handle large datasets from wearable technology.
*   **Emerging Frontiers:** Research in 2024–2025 highlights the predictive power of nocturnal HRV for long-term health outcomes (e.g., stroke, depression) and the integration of Artificial Intelligence (AI) to decode non-linear HRV features for stress detection.

---

## Abstract

Heart Rate Variability (HRV)—the fluctuation in time intervals between adjacent heartbeats—has evolved from a clinical marker of cardiac health to a cornerstone psychophysiological index in psychology. This review provides a comprehensive synthesis of HRV research, focusing on its application in understanding the mind-body connection. We examine the theoretical underpinnings, specifically the Neurovisceral Integration Model and Polyvagal Theory, which posit HRV as an index of central-autonomic integration and social engagement. A critical analysis of HRV indices is presented, contrasting time-domain, frequency-domain, and non-linear metrics, while addressing the pervasive controversy surrounding the LF/HF ratio. Furthermore, this paper serves as a methodological tutorial, outlining best practices for signal preprocessing, artifact correction, and software selection (comparing Kubios and Python-based NeuroKit2). Finally, we explore state-of-the-art applications in psychopathology, emotion regulation, and sleep research, concluding with a discussion on the integration of AI and wearable technology in future psychological inquiry.

---

## 1. Introduction

The study of the interaction between the brain and the heart has a long history in physiology, but recent decades have seen an explosion of interest within the field of psychology. Heart Rate Variability (HRV) represents the variation in the time interval between consecutive heartbeats, known as the inter-beat interval (IBI) or RR interval. Unlike heart rate (HR), which provides a static average, HRV offers a dynamic window into the autonomic nervous system's (ANS) ability to adapt to environmental and psychological challenges [cite: 1, 2].

In psychology, HRV is not merely a measure of cardiac function but is increasingly viewed as a biomarker of self-regulation, emotional flexibility, and cognitive control. A complex, variable heart rate is indicative of a healthy, responsive regulatory system capable of rapid adjustment, whereas reduced HRV is often associated with rigid, maladaptive responses, psychopathology, and poor health outcomes [cite: 2, 3].

The motivation for this review stems from the "reproducibility crisis" and the methodological heterogeneity that currently plagues the field. Despite the popularity of HRV, the analytical pipelines used to derive indices are often complex and inconsistent across studies [cite: 4, 5]. This paper aims to bridge the gap between physiological theory and psychological application by providing a rigorous review of indices, a critique of outdated metrics, and a tutorial on modern analysis techniques.

---

## 2. Theoretical Frameworks in Psychological HRV Research

To understand why HRV is relevant to psychology, one must examine the theoretical models that link cardiac function to neural and behavioral processes.

### 2.1 The Neurovisceral Integration Model (NIM)
Proposed by Thayer and Lane, the Neurovisceral Integration Model is arguably the most influential framework in this domain. It posits that the heart and brain are connected via the vagus nerve in a feedback loop that facilitates organismic self-regulation [cite: 6, 7].
*   **Central Autonomic Network (CAN):** The model identifies a network of brain structures—including the medial prefrontal cortex (mPFC), anterior cingulate cortex (ACC), and amygdala—that regulates physiological, cognitive, and emotional responses [cite: 6, 8].
*   **Inhibitory Control:** The prefrontal cortex exerts tonic inhibitory control over the amygdala and sympathoexcitatory circuits. When this prefrontal "brake" is active, the system remains in a parasympathetic state (high HRV). Under stress or threat, this inhibition is withdrawn, leading to sympathetic dominance (low HRV) [cite: 7, 9].
*   **Psychological Correlate:** Therefore, resting vagally-mediated HRV (vmHRV) serves as a peripheral index of prefrontal cortical function. High resting HRV is associated with better executive function, emotion regulation, and behavioral flexibility [cite: 10, 11, 12].

### 2.2 The Polyvagal Theory
Stephen Porges’ Polyvagal Theory emphasizes the evolutionary development of the autonomic nervous system. It distinguishes between the primitive unmyelinated vagus (immobilization/freeze response) and the phylogenetically newer myelinated vagus (social engagement system) [cite: 13, 14].
*   **Vagal Brake:** This theory suggests that the myelinated vagus acts as a "brake" on the heart's pacemaker. Rapid withdrawal of this brake allows for immediate mobilization (fight/flight) without engaging the sympathetic adrenal system.
*   **Social Engagement:** In psychology, this theory links high HRV to the capacity for social connection, facial expressivity, and prosocial behavior [cite: 15, 16].

### 2.3 The Vagal Tank Theory (VTT)
Building on the NIM, Laborde et al. (2018) proposed the Vagal Tank Theory to operationalize self-regulation as a finite resource. This theory introduces the metaphor of a "tank" that can be depleted and replenished [cite: 17, 18, 19].
*   **The Three Rs:** The theory emphasizes analyzing HRV across three phases: **Resting** (baseline capacity), **Reactivity** (response to challenge), and **Recovery** (replenishment).
*   **Adaptive Withdrawal:** Contrary to the assumption that high HRV is always better, VTT suggests that a metabolic or cognitive challenge *should* induce a vagal withdrawal (reactivity). The crucial marker of health is the speed and completeness of the subsequent recovery [cite: 17, 20].

---

## 3. Key Concepts and Review of HRV Indices

HRV analysis is generally categorized into time-domain, frequency-domain, and non-linear methods. Understanding the physiological basis of these indices is critical for appropriate psychological interpretation.

### 3.1 Time-Domain Indices
Time-domain measures are statistical calculations derived directly from the RR intervals. They are generally more robust to noise than frequency measures [cite: 2, 21].

*   **SDNN (Standard Deviation of NN intervals):** This measures the variability of all NN (normal-to-normal) intervals in the recording. It reflects the ebb and flow of all factors contributing to HRV (sympathetic, parasympathetic, circadian, etc.). It is highly dependent on recording length; SDNN from a 5-minute recording cannot be compared to a 24-hour recording [cite: 21].
*   **RMSSD (Root Mean Square of Successive Differences):** This is the primary time-domain measure used in psychology. It is calculated by squaring the differences between successive RR intervals, averaging them, and taking the square root. Because it focuses on beat-to-beat changes, it is the primary marker of **vagal tone** (parasympathetic activity) and is relatively free from respiratory influences compared to other metrics [cite: 2, 21, 22].

### 3.2 Frequency-Domain Indices
Spectral analysis decomposes the HRV signal into component frequencies, usually via Fast Fourier Transform (FFT) or Autoregressive (AR) modeling [cite: 2, 21].

*   **High Frequency (HF) (0.15–0.40 Hz):** This band is synonymous with Respiratory Sinus Arrhythmia (RSA)—the oscillation of heart rate with breathing. It is a pure marker of parasympathetic (vagal) activity [cite: 2, 3].
*   **Low Frequency (LF) (0.04–0.15 Hz):** Historically attributed to sympathetic activity, this interpretation is now heavily contested (see section 3.3). It is likely a mix of sympathetic and parasympathetic activity, influenced by baroreflex activity [cite: 3, 23].
*   **Very Low Frequency (VLF) (0.0033–0.04 Hz):** Associated with thermoregulation and hormonal cycles (renin-angiotensin). It requires long-duration recordings (>24 hours) for reliable interpretation and is often excluded in short-term psychological studies [cite: 2, 24].

### 3.3 Critical Analysis: The LF/HF Ratio Controversy
For decades, the LF/HF ratio was widely used in psychology as a measure of "sympathovagal balance." The assumption was that LF represented sympathetic tone and HF represented parasympathetic tone.

**Current Consensus:** This view is now considered physiologically flawed and outdated [cite: 23, 25, 26].
*   **Billman’s Critique:** Extensive reviews by Billman (2013) and others demonstrate that LF power is not a pure index of sympathetic drive. In fact, during slow breathing (resonance frequency), LF power can be almost entirely vagal. Furthermore, the relationship between the sympathetic and parasympathetic branches is non-linear and often non-reciprocal [cite: 23, 26, 27].
*   **Recommendation:** Recent guidelines strongly advise against using LF/HF as a direct measure of autonomic balance. Researchers are encouraged to report RMSSD or HF-HRV as indices of vagal control and to avoid making specific claims about sympathetic activity based solely on HRV [cite: 25, 28].

### 3.4 Non-Linear Indices
The heart is a complex non-linear system. Traditional linear measures may miss subtle irregularities indicative of health [cite: 2, 29].
*   **Poincaré Plot (SD1/SD2):** A visual technique where each RR interval is plotted against the next. SD1 correlates with RMSSD (short-term variability), while SD2 correlates with SDNN (long-term variability) [cite: 2].
*   **Entropy (Sample Entropy, Approximate Entropy):** These measure the randomness or complexity of the signal. Higher entropy generally indicates a healthier, more adaptable system [cite: 2].
*   **Detrended Fluctuation Analysis (DFA):** Measures the fractal correlation properties of the RR series. DFA $\alpha_1$ is useful for detecting long-range correlations [cite: 2, 30].

---

## 4. Analysis Tutorial: State-of-the-Art Methods

This section outlines the standard pipeline for HRV analysis, contrasting the two dominant tools: **Kubios** (GUI-based) and **NeuroKit2** (Python-based).

### 4.1 Data Acquisition and Preprocessing
Reliable HRV analysis begins with high-quality data.
*   **ECG vs. PPG:** Electrocardiography (ECG) remains the gold standard. Photoplethysmography (PPG), common in wearables, measures blood volume pulse. While PPG is convenient, it is less accurate for short-term variability metrics (like RMSSD) due to the lack of a sharp fiducial point compared to the ECG R-peak [cite: 28, 31].
*   **Artifact Correction:** Ectopic beats and motion artifacts must be removed.
    *   *Kubios:* Uses a threshold-based artifact correction algorithm (e.g., identifying beats that differ by >0.25s from the local average) and replaces them using cubic spline interpolation [cite: 21, 32].
    *   *NeuroKit2:* Offers various cleaning algorithms (e.g., Pan-Tompkins) and interpolation methods to maintain signal continuity without introducing bias [cite: 4, 31].
*   **Detrending:** Slow non-stationary trends (drift) must be removed, especially for frequency analysis. The "smoothness priors" method is the industry standard for detrending, acting as a time-varying high-pass filter [cite: 30, 32, 33].

### 4.2 Software Comparison

| Feature | Kubios HRV (Standard/Scientific) | NeuroKit2 (Python) |
| :--- | :--- | :--- |
| **Interface** | Graphical User Interface (GUI) | Command Line / Scripting |
| **Accessibility** | Paid (Scientific) / Free (Standard) | Open Source (Free) |
| **Reproducibility** | Lower (Manual adjustments) | High (Code-based pipelines) |
| **Batch Processing** | Available in Premium versions | Native (Looping through files) |
| **Primary Use** | Clinical / Sports / Non-coders | Research / Data Science / Large Datasets |
| **Citations** | [cite: 21, 34] | [cite: 1, 4] |

**Tutorial Summary (NeuroKit2 Pipeline):**
1.  **Load Data:** Import ECG signal.
2.  **Process:** Use `nk.ecg_process()` to clean signal and detect R-peaks.
3.  **Analyze:** Use `nk.hrv()` to compute indices.
4.  **Output:** Generates a dataframe with Time, Frequency, and Non-linear domains [cite: 2, 4].

---

## 5. Applications and Case Studies in Psychology

### 5.1 Psychopathology and Transdiagnostic Biomarkers
Low resting HRV is increasingly recognized as a transdiagnostic biomarker for psychopathology.
*   **Depression and Anxiety:** Meta-analyses consistently show reduced RMSSD and HF-HRV in Major Depressive Disorder (MDD) and Generalized Anxiety Disorder (GAD). This supports the NIM, suggesting a failure of prefrontal inhibitory control over negative affect [cite: 2, 35].
*   **Schizophrenia:** Patients exhibit reduced vagal tone and autonomic dysregulation, which correlates with the severity of psychotic symptoms and auditory hallucinations [cite: 36, 37].

### 5.2 Emotion Regulation and Positive Affect
While much research focuses on negative states, recent reviews (2025) highlight the link between HRV and Positive Affect (PA).
*   **Resting State:** Higher resting HRV predicts a greater capacity to experience joy and enthusiasm.
*   **Stress Reactivity:** Individuals with higher baseline HRV show more adaptive regulation of positive emotions during stress recovery, aligning with the Vagal Tank Theory [cite: 9, 38].

### 5.3 Sleep and Health Prognostics (2025 Findings)
A landmark 2025 study presented at the European Academy of Neurology utilized nocturnal HRV to predict long-term health outcomes.
*   **The Study:** Analyzed 4,170 individuals over 13 years.
*   **Findings:** Nocturnal HRV patterns predicted stroke, depression, and cognitive dysfunction years before clinical symptoms appeared. Specifically, low nocturnal HRV was a precursor to depression, while erratic/high HRV patterns were linked to stroke risk. This suggests HRV during sleep is a "window" into neuro-autonomic health that standard sleep metrics (duration, fragmentation) miss [cite: 39, 40, 41, 42].

### 5.4 Resonance Frequency Breathing (Biofeedback)
HRV Biofeedback (HRV-B) is a therapeutic application where individuals breathe at their unique "resonance frequency" (usually ~6 breaths/min or 0.1 Hz).
*   **Mechanism:** Breathing at this rate synchronizes respiration with the baroreflex, maximizing RSA and stimulating the vagus nerve.
*   **Efficacy:** It has shown efficacy in reducing anxiety, improving depression scores, and enhancing autonomic balance [cite: 43, 44, 45, 46].

---

## 6. Challenges and Open Problems

### 6.1 The Respiration Confound
Respiration profoundly influences HRV, particularly the HF band (RSA). If participants breathe at different rates, HF power changes even if vagal tone remains constant.
*   **Problem:** Slow breathing increases HF power; fast breathing decreases it.
*   **Solution:** Some researchers advocate for "pacing" breathing during recording, while others argue this induces cognitive load. Statistical correction for respiration rate is another approach [cite: 3, 4].

### 6.2 Reproducibility and Standardization
The field suffers from a lack of standardization in data collection (e.g., length of recording, body position, time of day).
*   **Impact:** A 2021 review emphasized that without standardized pipelines (like those offered by NeuroKit2), comparing results across studies is nearly impossible [cite: 3, 4].

### 6.3 The "Vagal" Assumption
While RMSSD is a good proxy for vagal tone, it is not a direct measure of vagal nerve firing. It measures the *effect* of the vagus on the sinoatrial node. Factors like receptor saturation or cardiac structure can decouple nerve activity from HRV [cite: 22].

---

## 7. Future Research Directions

### 7.1 AI and Machine Learning Integration
The future of HRV lies in automated feature extraction. A 2025 scoping review highlights the use of AI to analyze non-linear HRV metrics for stress prediction. Machine learning models (e.g., Random Forests, Neural Networks) can integrate HRV with other physiological signals (EDA, EMG) to detect stress with higher accuracy than linear indices alone [cite: 47].

### 7.2 Wearable Technology and Ecological Momentary Assessment (EMA)
The transition from lab to life is accelerating.
*   **Opportunity:** Wearables allow for longitudinal monitoring (e.g., the 2025 sleep study).
*   **Challenge:** Data quality and artifact handling in free-moving subjects remain significant hurdles. Future algorithms must become more robust to motion artifacts [cite: 39, 41, 48].

### 7.3 Refining the Vagal Tank Theory
Future research should test the specific predictions of the VTT regarding the "3Rs." Specifically, does the *rate* of recovery predict resilience better than baseline levels? Longitudinal studies in sports and clinical psychology are needed to validate this dynamic model [cite: 19, 20].

---

## 8. Conclusion

Heart Rate Variability has established itself as a vital tool in psychology, offering a non-invasive, objective window into the neurophysiological processes underlying mental health and behavior. The field has matured from simple associations between "stress and heart rate" to complex theoretical models like the Neurovisceral Integration Model and Vagal Tank Theory, which explain how the brain and heart collaborate to navigate a changing world.

However, the field is at a crossroads. The reliance on outdated metrics like the LF/HF ratio must be abandoned in favor of physiologically valid indices (RMSSD, HF). Furthermore, the adoption of open-source, reproducible analysis pipelines is essential for the credibility of future research. As we move into 2025 and beyond, the integration of HRV with AI and wearable technology promises to unlock new diagnostic and therapeutic potentials, potentially allowing for the early detection of neuropsychiatric disorders long before they manifest clinically.

---

## References

[cite: 1] Pham, T., Lau, Z. J., Chen, S. H. A., & Makowski, D. (2021). Heart Rate Variability in Psychology: A Review of HRV Indices and an Analysis Tutorial. *Sensors*, 21(12), 3998. [cite: 1, 49]
[cite: 50] Stein, P. K., & Pu, Y. (2012). Heart rate variability, sleep and sleep disorders. *Sleep Medicine Reviews*, 16(1), 47-66. [cite: 1]
[cite: 51] Järvelin-Pasanen, S., Sinikallio, S., & Tarvainen, M. P. (2018). Heart rate variability and occupational stress-systematic review. *Industrial Health*, 56, 500–511. [cite: 51]
[cite: 52] Serafi, A. S. (2018). Heart Rate Variability (HRV): Analysis and Clinical Significance. *International Journal of Biology and Biotechnology*, 15, 193–199. [cite: 52]
[cite: 38] Review on Positive Affect and HRV (2025). *Systematic Review of PA and HRV*. [cite: 38]
[cite: 13] Porges, S. W. (2025). The Polyvagal Theory and HRV. *AAPB Conference Proceedings*. [cite: 13]
[cite: 47] Scoping Review on AI and HRV (2025). *MDPI Applied Sciences*. [cite: 47]
[cite: 39] Filchenko, I., et al. (2025). Heart rate variability during sleep may reveal early signs of stroke, depression or cognitive dysfunction. *European Academy of Neurology Congress*. [cite: 39, 40]
[cite: 53] Shaffer, F., & Ginsberg, J. P. (2017). An Overview of Heart Rate Variability Metrics and Norms. *Frontiers in Public Health*, 5. [cite: 52]
[cite: 49] Makowski, D., et al. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing. *Behavior Research Methods*. [cite: 4]
[cite: 4] Pham, T., et al. (2021). Which Heart Rate Variability (HRV) Indices Should I Use? *Psychophysiology*. [cite: 49]
[cite: 5] Laborde, S., Mosley, E., & Thayer, J. F. (2017). Heart Rate Variability and Cardiac Vagal Tone in Psychophysiological Research – Recommendations for Experiment Planning, Data Analysis, and Data Reporting. *Frontiers in Psychology*. [cite: 49]
[cite: 2] Pham, T., et al. (2021). Detailed breakdown of HRV indices. *Sensors*. [cite: 2]
[cite: 36] Tikkanen, O. (2024). The Role of Heart Rate Variability in Mental Wellness. *Medium/Fibion*. [cite: 36]
[cite: 3] Review of HRV reproducibility (2021). *Sensors*. [cite: 3]
[cite: 48] Kim, J., & Foo, J. C. (2024). Reduced heart rate variability is related to fluctuations in psychological stress levels in daily life. *Stress and Health*. [cite: 48]
[cite: 54] Sammito, S., et al. (2024). Factors influencing heart rate variability–a narrative review. *Frontiers in Physiology*. [cite: 54]
[cite: 29] Champseix, et al. (2021). hrv-analysis: A Python package for Heart Rate Variability analysis. [cite: 29]
[cite: 55] pyHRV Documentation. [cite: 55]
[cite: 56] Kubios Python Package. [cite: 56]
[cite: 21] Kubios HRV Analysis Methods. *Kubios Blog*. [cite: 21]
[cite: 34] Kubios Software Overview. [cite: 34]
[cite: 3] Limitations of Frequency Domain Analysis. *Sensors*. [cite: 3]
[cite: 25] Billman, G. E. (2013). The LF/HF ratio does not accurately measure cardiac sympatho-vagal balance. *Frontiers in Physiology*. [cite: 25, 26]
[cite: 37] Review of HRV in Psychiatric Populations (2023). *PMC*. [cite: 37]
[cite: 26] Billman, G. E. (2013). Critique of LF/HF. *Frontiers in Physiology*. [cite: 26]
[cite: 35] Koch, C., et al. (2019). HRV in Major Depression: A Meta-analysis. *Psychological Medicine*. [cite: 35]
[cite: 17] Laborde, S., Mosley, E., & Mertgen, A. (2018). Vagal Tank Theory: The Three Rs of Cardiac Vagal Control Functioning. *Frontiers in Neuroscience*. [cite: 17, 18]
[cite: 57] Laborde, S., et al. (2018). Vagal Tank Theory Application. [cite: 57]
[cite: 18] Laborde, S., et al. (2018). Vagal Tank Theory Abstract. [cite: 18]
[cite: 20] Vagal Tank Theory Updates (2024). *Taylor & Francis*. [cite: 20]
[cite: 58] Laborde, S., & Mosley, E. (2022). Heart rate variability in sport psychology. [cite: 58]
[cite: 43] Resonance Frequency Breathing Mechanisms (2025). *Spandidos Publications*. [cite: 43]
[cite: 44] Lehrer, P., & Gevirtz, R. (2014). Heart rate variability biofeedback: how and why does it work? *Frontiers in Psychology*. [cite: 44]
[cite: 24] HRV and Planetary Resonance. *OA Text*. [cite: 24]
[cite: 45] Resonance Frequency Breathing and Baroreflex. *MDPI*. [cite: 45]
[cite: 46] Schwerdtfeger, A. R., et al. (2020). Clinical implications of HRV. [cite: 46]
[cite: 6] Thayer, J. F., & Lane, R. D. (2009). Claude Bernard and the heart-brain connection: Further elaboration of a model of neurovisceral integration. *Neuroscience & Biobehavioral Reviews*. [cite: 6]
[cite: 10] Thayer, J. F., et al. (2009). Neurovisceral Integration Model and Cognitive Control. [cite: 10]
[cite: 15] Brain and Vagus Nerve Stimulation (2021). *ResearchGate*. [cite: 15]
[cite: 7] Thayer, J. F. (2000). Neurovisceral Integration Model Chapter. [cite: 7]
[cite: 11] Thayer, J. F., et al. (2014). HRV and Emotion Regulation. [cite: 11]
[cite: 30] Tarvainen, M. P., et al. (2002). An advanced detrending method with application to HRV analysis. *IEEE Transactions on Biomedical Engineering*. [cite: 30, 33]
[cite: 33] Tarvainen, M. P., et al. (2002). Smoothness priors detrending. [cite: 33]
[cite: 32] Kubios Preprocessing Methods. *Kubios Blog*. [cite: 32]
[cite: 59] Preprocessing methods for HRV time series. *ResearchGate*. [cite: 59]
[cite: 31] Signal Preprocessing for HRV (2022). *PMC*. [cite: 31]
[cite: 23] Shaffer, F., et al. (2017). LF/HF Ratio Controversy. *PMC*. [cite: 23]
[cite: 27] Billman, G. E. (2013). LF/HF Ratio Limitations. *Frontiers in Physiology*. [cite: 27]
[cite: 25] Billman, G. E. (2013). Sympatho-vagal balance critique. [cite: 25]
[cite: 60] 2D Representation of HRV (2017). [cite: 60]
[cite: 61] Billman, G. E. (2013). Citation in Motriz. [cite: 61]
[cite: 28] Reviewer Reports on Pham et al. (2021). *Sensors*. [cite: 28]
[cite: 4] Pham, T., et al. (2021). Abstract. [cite: 4]
[cite: 2] Pham, T., et al. (2021). Full Text. [cite: 2]
[cite: 49] Semantic Scholar Record for Pham et al. (2021). [cite: 49]
[cite: 5] Macquarie University Record for Pham et al. (2021). [cite: 5]
[cite: 40] Filchenko, I. (2025). EAN Congress News. *EMJ Reviews*. [cite: 40]
[cite: 41] Filchenko, I. (2025). Study links sleep HRV to stroke. *News-Medical*. [cite: 41]
[cite: 42] Filchenko, I. (2025). EurekAlert Press Release. [cite: 42]
[cite: 62] Filchenko, I. (2025). Brighter Side News. [cite: 62]
[cite: 63] Filchenko, I. (2025). Economic Times Health. [cite: 63]
[cite: 19] Laborde, S., et al. (2019). Vagal Tank Theory Review. *Frontiers in Neuroscience*. [cite: 19]
[cite: 17] Laborde, S., et al. (2019). Vagal Tank Theory in Sports. *PMC*. [cite: 17]
[cite: 14] Laborde, S., et al. (2017). Vagal Tank Theory and Polyvagal Theory. *Frontiers in Psychology*. [cite: 14]
[cite: 22] Vagal Tank Theory and vmHRV (2023). *Core.ac.uk*. [cite: 22]
[cite: 64] Laborde, S. (2022). Vagal Tank Theory PDF. *Bournemouth University*. [cite: 64]
[cite: 10] Thayer, J. F. (2009). Neurovisceral Integration Model. [cite: 10]
[cite: 12] Thayer, J. F. (2014). NIM and HRV. *Frontiers in Psychology*. [cite: 12]
[cite: 8] Thayer, J. F. (2000). NIM Book Chapter. [cite: 8]
[cite: 16] Thayer, J. F. (2009). NIM and Pain. *ResearchGate*. [cite: 16]
[cite: 9] Thayer, J. F., & Lane, R. D. (2009). NIM and Emotion Regulation. *PMC*. [cite: 9]

**Sources:**
1. [umk.pl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1ODAIO6lMaZqd_NyYAxTyrTW6LQ2ossHANB_iJmCSypShTSzYtFnfKwH9iwH_IQ5fQRT5bGafByA5aNZSyYn0YDyH46xkflK5hR3SNUtPZEAKxHiUouKkXH-tFsA_qGPi)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuC72T8KVy-ZxPITz07wGls3xOqD2kn0ho6oSRTmj8tZ5YFwc9Vbyf8XYtPK_BdLVehkT0iBQuKmS_FZnzj_J8RthgkGRQ6kz63nhpC74sLOa1-UJ-an-1v-kneahbWw==)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtw6D8V_mnED2K0k0v56Zh4qCl6B7lKDp_GQ2fnyW9wW6QPawZy_5W5XdUx9EViRsOxV2VnGTD-_v7_pVc4xt6wkgdZZlmlqNlFH1A7rMmTYj4Hyc_kWw_CLr3jiTuP8vdfrZE6mtN)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWNN0yF4hiShUgy63oplN7-DTmCD35Cn5W_IjLx4PaZ72PM_jOnz3df9J8cm_IjTiZMivsw0uN9AfOAJEn5DpyqApvif1xiDRL_lGDEbKECPhFGPxx-w68QQi91XTW3w==)
5. [mq.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5SrHyceg-ndrF0yuvNgHsRVgXv2RPLIAf_oa3RL5NZPKjdQec4-RYXNwM_-wTV8bUMbZ2pbBRmcpNYyhfPzByBo_TUHiRT_0tdPZkE7cYhn8dsJ-Hb6XZtFdYngLzEPnmmUJ__6yEYrred8xpERJ1dlG4AM1rek3DmY6__zZVuNfY0Mn_8-0NkakiF8ilvbVoF7zsRm0jNglNd82vLAcDxeTbshW4)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZvii8OqSVNxI5_V5oguamic5pFPDVLDBawZt6XpKU6r9DYwkx2FsX5cgFbk7diSFoEd8AySsSwWBYFoPiwtjDCkV0VWaq1xGPzijpFD0waJN7WAZSAzZNOqANPMoUSw==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkX-5IcX9qNMqa_5L0vtp6Ka92Z-GRerIJZRgHmZURkB7tXnDeuLxOIZynOsNCJ6wE5KM-QtZDICHjxG2JcRBf_ZKemQSVEGD438KWD1mXaogLjM-PHHcxqWRWBnTI7nT-VkiXEDJTsISw99grYI5SQqofPMiz)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYoz-Geyo-R4orXqAoASbvlJ7YeVK8yw4Za-j7D038FfnTVk4yNcIKeiE7EggrckIsu2QpgsFPJdn1jd5aNV7t5crLf-XKEmN0g2r0OiLCoiA4eXUFEhdcDM62jBfAmxTavA==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEDapDCmgXc-3H3y9MMRar4ePbYyjSuE-FA5AjAar7IqVacjbz3Dp5u2oz7Eg-Bfq81M_LP-bwHOPEtzG4OVaRmo5SEGrJ1NBjfurADxxMn1pOKH4rgMhNs30_I5xpm3Wch2CZSvWfOw==)
10. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsbVvwkOtnlV6DU5dtpAN5NupSTr7U5E8KzPjNNEdEdRKClGIaCjGSji_nQbnb_Us4db7jiKjpqhB05ztapnMmLsH45I-mRRiv9yAKXNZbX4h0Kxhh)
11. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEavXbdlLryl17oHsVdrhGntUtZATODTVmO37MMYEReSJivu7uiXunX_RnXsFy4UGDXQY4iBhlpovJx3ON4HzxhOJ_amhpdsMixR1OroMP6XrCroxQU--Ho4oTTMMnTTWdbLUEu3AP_gubh7g4GexIB)
12. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5NrSLyPdnKwP16NUzRj18V93Dz4nmyVRIRTGw-ldBd21Hu4ow8hUhpW4fQkfoYpGX3CPusumWY84zxbpl3Tw25l8-gmN1SVTmToQuF6VvUPURtik51_rUYbz4mdaqFUR4S4xBsOh-dEgk_DC4QrUqwPxoWFnI6qlXdTfygu5qvXlAvUcsIkb3cReD5Q==)
13. [aapb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAjWxvurLjVOP6VKkdjVSctDDAZzDdBaw4Q56khOhFUmHe8D9Qgvzh8hx_QI9h5HCwX45I7qCETjGRnLKjHI3D1hi-DyzyJNzbrS-qP7VHKbGHtvrRaATQ7doy9111-YCu1oBEMiPwYQ==)
14. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoGkDUwqiltyZRurX7Xtgj9ykn0lGsbgyC1r-36i2bJ9NlcgxX_K_udhdC_0tGhcQtHTZTqyhaEX4wZILe7yyjcXiQSiE8J89nRG3s-Fuoq8qH-bLyA95i1YsrKcvREheTmcN2IVXntWh_UfZKG8XaxiPVMGq3dDFa9unP3dgx3RVx04_lVKHyAkVQHg==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRoF_glbAnA3KtJboL5BK0G3MPJUmMeUEzdbMxARy5U-7CK33qMFGjlQb8FRV6JsgpexwzASF4f8SbRe4IZv6Xtt0vRKq6zP0A_-AYODRr42qmbq_WC9ADWLqODgq2T1dzHrRfu5qP3iTozLD5Kl_texHTADwPVW43ikOwJOpalgHRcca9lGoa-rSRCTFehWqD86DjRVW3JxJtLG2T6yAhi3dO20JqbFbC2WN2cUsl9dIb)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRBcPKjs8uIIQDVuO1IGxXmMN-gZSdTswHdNd67EbISIEfTkb-SoRlCTle0WD3xGB04er_DeAVs5WJdTkeI3CuDumlWCQMNwfEM7XDYuaosyP8Wwt9sAz03SAhhuOvU2Fdk12qIA0BIj_iNB-7pRVrwfNDnsFehh5Y2aN234jG9t_Qb7UYeDNArYEWjAmA12r0Y2TLwi3J0hOQnYrORupOWQ==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1m1ss7HQtGlbZOJf2OTnFHhUf3nCV-5cWd0VXt4bLNdutQ8--Oi8hdWxgbcjukB0zkMCvyCcFvJViQedYXwHcKMB7ZKN_sdXeCAuGI08YqztJRVn3uCbVQ-tF-3GL3cvid5MLwZ-h)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3XZhKy7VgqYY_rutY_9xSLQWwCSb_AwCHdb1Hx2lGqY40VW0qJQ8RRR_AVGltlhZsmERKzhrTWpGRfZC_Y0Dx5_5zpIq1uVYEehKO90OCIPQHPhI6lNvoSerwHott0xnCgU0IcmTd)
19. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdhK1NeWpG3JyGFj7Ty09wBNQ1KblJYgABXy_N0w4PyD1knb-f3HtjIZI_9jDW7zTTShyCtg9IhhIWZsmm-U42GIxo3cyk_DoZqtuXWTvdKMZXpdmJhChpGd-XT6K95r41IMMY4GnBxSKXGjqK-fQU0fitLubBtShQjRTyhG06FdNj7m-HNjF93BOuy-4O)
20. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKxu1pRMQiypHY5iCy-XH4KcvebuHphwyu61Dtk6cIzQtkNcslJ0XCqtkVElPBEzsV3fQjghoNSaz7d19T6fbC1wWMZBjH5T9DB_EOJwQzdFTxUBJswyItwJ3Jeb4VzfJL4xC3dunW1AtMWT8Lw7K9soe5T_wTQS8=)
21. [kubios.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTkgUmDmJdr7X0cZ62lJDTykfbjqPPfFp8cSTjMc4UDsQWHiUwbOKzW4HhVcfY4Y6Ptfbqjug_cbzF7_PIXPJgMLUvLqxwcyvZ-bKkJKGuRLHjtHGWusZe_zOHzmiynNlYNIcL_aXd)
22. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsd4AzWntXxfNVsCTdb0EHR9bIH2K8rky2L0hYOmM8F9VdSz-FVnzH9fj6IKfum7eqTGsT0e-8gnjzASYw1P1faXtxDdVUEF8v3GO7rtMngn3XD0PWJkmT98QP4wOXjq--hQwxqmoDqk=)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpHh7pqla2UfwwPRg1Ln1vhMWPMKFxledEEashiOaZch9T_cJSINSnqZH7mH-QcrR9PmMbuktwy04tZpPU2TkLpA13RcWLlp6U0byxvZMWZjJwE7GEaJe5zS94SZs9BYouEvXG29a)
24. [oatext.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqdorS7_7NM4HuoaOGHyFQfL5J9dqKUAyLfMo4YJNHaC_5bIg8vJAfOBC6PJBXBTI7MUpxkV6EhbLGg_qGE9e_gSdfiC9__TuvHG0VHnY2GVH0a92bnuCMZwgWtJJzmWBNCPPSyNo55M-fQCoseIQg8Sfkgph6t15-tPY9ZOTht__GIYMQSNN7nAqlRdg0pHy2A6nu0ImMsEfKQvoSiOtWukQfKogpKGFwIwJduDFGbZysOVKAmLgkqd3mz4znzBVju6c-v_giYmyB8gkmRdQB2g==)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy7hvTYDd9QwixmQW2I-ntSOluG39F59zkzHiGE01axv5_TjKQ5lYdWjfSGipmy_iHmWwGc0KIpkU_T7fxw_vEhmPorktH14qVX6D6MG_eNoJe62jZmHeUWfW4FJVegKrN7PnRPfp4uNlyMoHQ76pDlrF3ha9zwB76tsP9uPxZ4wZPPWBYTJwaXsh1nywptZ1wsjiDrmEDRvC4uQvZcxIwkcYzyxUS6p0HydLZ43gjLVQB)
26. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJtaWtJTkHDBfixsi0OdOXYDnoDW2PsifqRK9C1Bmfk3VjqG89iJNGQph2c48G5QLd0M5Ro4dd1vmp2T-qGiJYBrfAUA3IkvndPPB7xWKJ4KkLrgW5og6sLM31ViKTFHX0eYqCvY7cuGEnl3O59dJkx8REuL_STQTY7cYy8fr49jeO7jYjwTd9bscSdw==)
27. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE96QkXjmwkQtlcmERQAN4V8_C5cwUFQ_QC8JAjVfC1bD6IGQQfxdYVl5JoW_wTHEFubgIlpeU6i0TA495cmlZmaePLafCUnsNayWxF6bJ6n3o0ejQyBp0Gt4Xq_niI3CRvkczSDcVIjSdHIjqiGKADBVWYVGb-QW_taNtHQ9ismdHalhF-5wnTfzxfUA==)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrbMjozBLivA1nXXqDXudbRM8dsB50-WYSmIerW28TKMdmZ_oYAhUDUSIAln3r_iWkq2ZmEVH2eOEl7bjw2FDuWMKUmlB6vnxVcmUiIzRsV7rY9sV24BH3iUSyhphviDNcdymRjhW8D_nNyj7a)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCMBeASodl20lPtYWa67Y8JPDsy48qq8eR4seMfOy8XaRwppKTf3OPHQdUVEPmLIil-6AzWBPgDamMpZkPJ_-et6gFPK0JV01iWPXlnNd3k20U_iietAhT3hktwDGTl0EiitYbuoAeKFM761B8qDhrF9XjWTzqDpjNxOUMzkj7QhSuXUe99LwnylUYl3Gdq3CYtriEwrBOIBO3e7Lj3ZWiKl1vIQIN1CDSSsFeXN0nbhm5StydAbPLDJdYZYfGixkZnw==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN4abQEmEi5-FnDU1jiVJ8QXt9VEnkhboxhGIf_9MbdMzVzaTMrN9noecSRgPxWXcPfeaV0yEDNylkMbr2i7jRfpxjCZjktUN-AcMVVS14zQPlSHU_ZgRQzOq3we4t12xjhe_r06EtNF6215NclR_dX1ChO17dIzPtlXEedZ4DwnStWDXtuTll6Av4UCBD1MxELgKvYUS7_R86MYBeaILMF-UmqaJu)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1jBsGM3UlhEcslC1tzrEG09Yo4Htd62tMXa1KHYcN6EKUXy12J3SlanRPIGvza_WiBxuyhqgnhvzNWiFkEBs5Ahnq2MXRP-lL7j3aTnKC95pGgPpt_CNrixqJglbYY54oQbg9FPXe)
32. [kubios.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoo5Kk3v_eCB0PAkGwyvF88as6F3i7uECOGWjZp-iV9ZJCjixbacg-4bacxUq6k6lf8sfsl5Lo5ftl8jIi8Ww2D411EQ6NOVINQFWYhNK_LpKwb2bFzUYlLAR_lfeOWemPkcJBxsST-Q_izoM=)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9HEMPYhRmed3o7ic2WyfwC8zoKymEacfRyiUd10piKgVCSKTJrwXzvHT145iJCfZGaTSq8qJCNX0ZB7y1G0JkvUYi1d4RUHGxJJ2AlOeDpmip2Qtvk4qiMywfb_waxg==)
34. [kubios.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtMwKY6HtIgO7tjnmH-b3JXqBI3OkTob0zp3C2IF4ypgfDsIH-06_ySm5w08XBiTWQC6jMKzTS_Gq96T_pVA_C3RgI-gyNRx2NJG3VsQ==)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjovrFy33v9C5j615jotblrljXb37Kfjv-RjZ6ObQTGWUaoS2-yqtNYIM6USj1tMBzP65A7V8Nf2frDuwhfXXlwSAwylHe3zX4Dy1oCdhtPuDnyrt77zJdtp-4j58=)
36. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1vbSek3-LIo6UyVfOjGu3oVtBw2K9Doa1BDR5RZfmP1HUIGnqBWo3GTyqa7EoJabNP9CJXuEBa8I6Gkc7-0K3g53IXe9Qve6sYxBkYKDZxn2irS48G2jgTdqI3SgmrGsWU-aYFNnvpWHGJFlm961q2zhO2xu0u5aJ_cZDq5po30Vf86wg4KPDNf-1sSGo3P9xngbZuy6puIXyArh9ECSUjHZOE2lmphBpEnXCIfUlhRuqvdcloAoYJgD7Tg==)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEI1B_4itQjCa8_bcJ5SObLXP7Z1bOFsZoJam0NT_BlNm6Ld0jrsNnkP5b0anAVP-vxuol-E27bLjJ-v-eaZuuVsCWAPXZeCqFuRrWgYJBgtVdn18wzXoWKAcn9KHAuixb0gtGGAsAXQ==)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmjG6z3mKkD0OckRJru_cHBBn5gNQVrieSgOlsFxZxJ-CeZVPsyRJKnABnpCmQDQ-x6EQlWgxqOVr7OpNOuIGnlRF-pKlRGvRFlceqlgEaJUEs0dajUHSyZiyMFVMnf4YyaDNqGWXJGA==)
39. [neuronewsinternational.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg1WrXPc_9f01ZTUKdq2BcJtn0UXCGI2sxQGJLcOdULnT7nBJSPKngK8KpZHxcW9RAWvS3LCwLvAQ1O3TVug0NOuuaxrnBeFCoB8DTML1jQ9l56AkBFxf5dYwU0yWUz2gBirezQmB3yFBf6eCkr3WMWPuZei1W-DeCoz7YZTRKJhTN_oQLVFkrpr5C7qlxmmvcnydmPM3RlIlZjsFhkxXPFrYxKaXWl18gdxhi1XNPFj8jmXlM5H_TuX9nwVxc1KO-WwQGkTzFtfLB7J4=)
40. [emjreviews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_gc2h58XmHGzkiQo6415Q0ZwzhS8Is9foVhIKnYvqappsGe3mCBIrR2P2TI503aK8jveCItfsywFTCXznUdhhzkBc59kqiBDTbQRXRlgLoVx_r4M8eOjVRE0JnxQueQlOVQPDurv_fweJXCUeD_laSvl37RQw6jZK37TTtGdrn62F07xziFitxIMOpUelHOyH8fD-5JdAl6LlnbBqtYCy4iPTLfiyqeVZWcNsRt7rHz0=)
41. [news-medical.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcsm-NH6VjHN0yh6Rl_lPeHCujLsrzeGRHScATBvhc5QOpFGVibHsz-cXXhScnINbbuA56DIHRerhoTE7swmsuEQ-e3b3hbbzMJgfJ7a4VQfj7QvTc_TMFfiPCAOM_u8QJei3yqPVdXpfZlnljKh_6OtMOJWkC72KaI-_-L1x_3LMjyY7TqkokT94_S5Y20pE7bLkQbhoNhIy4TDZEiIfOw77TIpAqXFIT28zo)
42. [eurekalert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH41QTeoG5ZMOUG_jmqc7jaEjrmX-xR8CncU9fUsydJh14MCAP9G_7mrfRtPjuY68Z2ExesfhvRkTLdN73eC1ISQ9CbCqxHff5-Fm410ljbeap-QLzPw2cGAfab5PGHafojOoD-qRc=)
43. [spandidos-publications.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-XzYCFo2ftELI4OoEf7M3cCSQhqb-o_yeLqWpqaWnizYEf2zmPzJiE_VbaDyU1GlJmx66gClg-RsoxLSl8YBrAF50iwljI5zTj5jmVJnE4uOxcbahFWVR4ylL18Tjcuv2_dG0YpnqJSRWtp3kVu5a)
44. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkXsBGgxIikFU47j6OkBV4fzZ6TFVTkgHShlLIv08kYSPR3Jr95ffQnYG2JfpBicuT98jAWPh8mUne8OftmIrjNOxef8sDmJ2qj0adp9jAR_xAKf5xFWg2mIge3qmlYVBCtPZwOm64qzMpuCsQG8HcorQsjNQDi1nU046-OQ_EkgVyqYdqJvdViuzIFBRvuw==)
45. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUQ7SfBDTw-nHagNV0bMVBfF4hCGVb37wjQ6nDDU8ZhepoWM04SutQ1-6aQT1epM3574z7ufd5F72S250AGOgajqJ-dp27Tm7CzFF12vAmLRxiJOe9wboBuH6-G8nTEQ==)
46. [sci-hub.box](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtJVj32lzaHfViCshuzQy3JaeLLNJV0pb-9IKN0Nhs3j18ueKS01sJruz0wEwgiP_gb6dn6Wo856Xx1YWA2xE1Gf220xhCUHmGHEPEb9b5zz3HAqIwXipFawfnAKlFes9ZZa__gNgclRV0YevKP71VNDJ6Za174JmMx61dsR1SVie9iuGBzq9_h3I=)
47. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5rFdbE5EJQhNenvEi_diSKSuhvTnJRBDSnshYn6ZTwvbGSb0SgcXsiNfHAepL98ncUHVZEAMYuzYmmpQtQXciOGLeWMlFeIV0OXizDavBWkF7RkqQSSV0cNCMyw==)
48. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfyvdpi3PhG4qga2NbGoIj_Gufxbe-4j5bqqqfKu5aTrBbjns6gW9copXJ0R-Y1YMbq3IOMfV2OoYi1A5SICgG2RIFrFXLSsWIWVhBtOigID_6j-VjB-G0aIlxI4n8tYZZ8HH46D3t1anp9mL8o_HJTFtQZeqgVV02fn-ZeA7-ABsW3rGCFObgDSursRGWy6XybBgRsrXOSeBzUcpIBBSVkwGSntMxEqheI5SRkMZD3Apv_9C4OtyFX488FVzn3AWPz2JqRNry2rpnNPrsx6gx)
49. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbzg3THPCcxFL8nN2xwa626qFiPygTp-QUwdWQjGZ_XdYJacR-jj5FmfwFwgd9ya59D9InL8L0iNMrzcqVD-cfsJBgMFivTAhOhaEjGX6d95cNxOBrk7OS3ZHRwdfkeITVHPVTT4oaFjr0GFNnwR4w_Sm5J4-F6Jn_lbQrvpELlQXnuug4XLnp6mckFUXGj392-CKnEdTCjnU8L7bXwDkFC7uN-Xiu5cYr4Ji7pmEjpcLMUoLRyzjPFH-wZRU0_A0wrA==)
50. [koreascience.kr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYM-1XRf5dbqlw9Z2ynzoHuBSbCGzAY_nifoL_LNehtp1nNnEeiJLm3e5hZw34Q5kO12S5dnLe0si_6olURABuSclsrZust92Q8vecILtvFCwnf5Z9KCkT5qQMYi-f0adSeNn64L3FZMcrp2Y=)
51. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt7ZwR4Nunz4z6QZFEtF5MTwlBT679WnE-Kwmtm8Pc7uVxUJM33HRbVi-saOLmVtYKiLZRBsgIK-JpyOpBd2D-0qclm4LmqEUH3WU0zgfwSsBOOo4egjYEy7ocvydpQAzO8ISGoNFvIcLN0_wo98XyxttVtin5SR2vR8p6EQ_IZRA37GI6X59CFwvFgGCU)
52. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTAvU7E1r8V5DRXDBOnJR-b9OrxwHhAFqpZowwMUrKXfw6usuNYoabzLit54qP51gFfTSKZ94YSH9na6XHexBymEoq5XBZar2nQASKJcHLfiS2qvr5ClVKxABxI8Z-)
53. [Current time information in Kuopio, FI.](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-vYB6JEKTTQoF77R-iuBu9Mqs3oZ_jPis8X1dGQaGXOwJg2EipUVN7QTlUuhjJTX2fJ7LmTqe1Ojr0jWMiNpj7HTL0dvJzL5cFJts_bCJL8LrUMq_8sSh9i8IiFTE7Y7Mm4Hz8XE_OA==)
54. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9cvER_J84Qw4FO4yRUYi64_lxVQT7b6B_LLZK2Dt6aTrDCr6HAoIh1FM1TXYhxCWGyv5m5EGl5jfpNWvL4wUCgepgoWjWJjlGDEsEnyICGVSaD7iXfmY8H394gCeHhSuEFvNj2zbPrfVhb3wkjRPwCSFnkYz7iJXM7HssAHrxlfaWk13Xj2ff8Li8tSUz)
55. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNe80uVcYQakkkp1vUhHAKIuoVc-z_ZNpud7glWJkSPa6PfPhA2Crb-XKJ5m_FrY5JrLCwzR3pzOn3Z_FvxBxwp-y1QhTGZt2hyKb8_lf3_aOvIL75f8A=)
56. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMAyf-kvqVl7wW9tmmYF2xxGCipEsAH9VRDupFqWyZdd4r6Bak8ENmLzp3JX5QqCapo0pFkptOTyPdK5vBcWbM5TQvyXk1WyksJzloRNsmTy-lgp_1CZ-h)
57. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrsNWMrRWY3gOXRkJ4HvT_Bd6rLHdM32V167X2ComJD3KsQYxh6fmbDoB7jEhrA9fn9Quwhztdi85k47tGtHzi69sojhNGsDjKLIb-zxkf3OoIdKlK)
58. [solent.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfFJVFkIO-x4s4WRZENEUgkQ8WfLYZVRTiKQ7-cU4lF85X8gDjUfd3-nRAp1pp2QEidOr9kkj0m7bb1sJ57nPJbAd3_6KNlYBsWSZK6Hgo2H7VFQfu9XU745P01Gb3VYkZLjRArvUtjQtgDSIo1zYUa2mD3epp1Wa16PCrBq6SN-lGbv4-nyColc7-F_cfeYnc0JTCjZwUVOAkRT4jEsZIXOU=)
59. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGuHrl0S8JAUX7rM3ELlojcQtapaT_khXW4TwPwC3H0jclJStML6JX6DS7xzOby9NqF3cBAPY6aLyzMSuulELnGvmA-Yjt0SDS1TEoY9IigNYIfFNRHzdZvpmbK3ySTvgzlnGSrdJT5j4zWl65M8kfKmZpKX3rtXEVuhoegxUkECUa_NqwtSMuklvENQh1iaoPBCvaqeLYiilv8PnqCmYnwjt3IJE=)
60. [dtic.mil](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_8SLsmAAl5Ay7KY7AkY5ehM3eOdJ7RN2qA6CkiRJ_vdkhKkN-fKAwJbgJgFcAJQbCU_NUqhxgIX8mjjC5y76ZXHvm7kaQArRdJ_0MIZV1wnR_bXhOZ2TRxUWZso4LZ3tC-w==)
61. [scielo.br](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB6atlezeH_3M_6G-TxZYfyewJdOhsH64A1M4-P28rlVXI_IFPH2lZv6JdPFN2QGIkqVS7Ics1tOyGJMH0Dtw2-BjPinuzJTW2ej3-GzyI2SaaLkQqv8pjOaLC94-iTSCgy-xF_K4Q2RIAXwCuBrThNUgCvJzBxW7g0YMo7rL6cL78cg==)
62. [thebrighterside.news](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB_SpX23NreyRjv2-3AWsEt9BPYeDaFaZC_hGNUDLpWYz6-NcLak4DEaQeKH979-77fMMOaJAc8WvMFWsmADOUFJNR4O5EO6t2gKXcCPhHDyb2tZzDzasj8rpV9hHjnuGm2AD6j0vHwxLEr2J4u_Mgs4D6AN6vWUOR5aIHZzkxfyIDJ9iVngKXPM2xTCcnjRJduvwks5_f7ykLQVrMcSfGNIpwqgjKVVKF)
63. [indiatimes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0Z1D2J3UBLYTd1YiET5Cqmx9w84Za6Ym1wn4y3nWUue5jUN-O9fc_Z3tKSjkEzzFg_yCWUQluu2J4e35SMEJpIxQ3ReM-99c5V9kRvE81gDlKObvxszLMpBWnO0cYRcYrhhZfHLvl8HwpOfxTz5C_O60fR5HpCF6JDZzD84fJ-VZkM4x3xj8uL1LlOeb0s9dSMqXMzcOVMypVueMN9GrfTFOA-DiYNnMlYElWkHDQuzpXyck7bU-hPdSZpkM248PCxQLNQVQmGQ==)
64. [bournemouth.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjEDD5Xqtjidpo0rgimNFrM4gMFeWDN-23KxD5qCneNlY8hTwWzrZPWUwt0y4iwoKj8Hxkleu8avjOT5AuNQoXmxtqZjdEYAjzlYjqJ1wYg9I9bWiaQ1eRjywLcKn_7ml9MCWOSMyngnWYnzDfSM_cZ1srtXuDA==)
