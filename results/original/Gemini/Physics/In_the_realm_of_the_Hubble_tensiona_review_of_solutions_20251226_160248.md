# Literature Review: In the realm of the Hubble tension—a review of solutions.

*Generated on: 2025-12-26 16:02:48*
*Progress: [17/21]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/In_the_realm_of_the_Hubble_tensiona_review_of_solutions_20251226_160248.md*
---

# In the Realm of the Hubble Tension: A Review of Solutions and the Post-2024 Landscape

**Abstract**
The Hubble tension—the statistically significant discrepancy between the value of the Hubble constant ($H_0$) inferred from the early Universe (assuming $\Lambda$CDM) and that measured directly in the late Universe—has evolved from a curiosity into the most pressing crisis in modern cosmology. As of late 2025, the tension stands between $4\sigma$ and $6\sigma$, depending on the specific datasets and calibration methods employed. This review provides a comprehensive systematic analysis of the field, building upon the foundational "H0 Olympics" and the seminal 2021 review by Di Valentino et al., while integrating pivotal developments from the James Webb Space Telescope (JWST) and the Dark Energy Spectroscopic Instrument (DESI). We categorize proposed solutions into early-time modifications (e.g., Early Dark Energy, New Early Dark Energy), late-time extensions (e.g., Phantom Dark Energy, Interacting Dark Sectors), and observational systematics. Special attention is given to the "S8 tension" trade-off, where solutions to $H_0$ often exacerbate discrepancies in matter clustering. We conclude that while no single theoretical model has yet emerged as a definitive successor to $\Lambda$CDM, recent observational data from DESI hinting at dynamical dark energy, combined with high-precision JWST calibrations, suggest the resolution may lie in a combination of new physics and refined local measurements.

## 1. Introduction and Background

The standard model of cosmology, $\Lambda$ Cold Dark Matter ($\Lambda$CDM), has been remarkably successful in explaining a vast array of cosmological observations, from the temperature anisotropies of the Cosmic Microwave Background (CMB) to the large-scale structure of the Universe. However, as precision cosmology has entered the era of sub-percent accuracy, a formidable crack in this edifice has emerged: the Hubble tension.

The tension is defined by the disagreement between two distinct methods of determining the current expansion rate of the Universe, $H_0$. The "indirect" method involves measuring the physics of the early Universe (primarily the CMB) and extrapolating forward in time using the $\Lambda$CDM model. The Planck Collaboration (2018) provides the benchmark for this, yielding $H_0 = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$ [cite: 1, 2]. The "direct" method, or the local distance ladder, uses standard candles (Cepheids, Type Ia Supernovae) to measure the expansion rate in the late Universe without assuming a cosmological model. The SH0ES (Supernova, H0, for the Equation of State of Dark Energy) collaboration, utilizing Hubble Space Telescope (HST) photometry, has consistently found a higher value, clustering around $H_0 \approx 73$ km s$^{-1}$ Mpc$^{-1}$ [cite: 1, 3].

By 2021, this discrepancy had crossed the $5\sigma$ threshold, rendering it effectively impossible to dismiss as a statistical fluctuation [cite: 4, 5]. This prompted a massive theoretical effort to modify $\Lambda$CDM, resulting in hundreds of proposed "solutions." This review aims to synthesize these efforts, updating the landscape with the crucial observational breakthroughs of 2024 and 2025, particularly the release of DESI Year 1 data and JWST's scrutiny of the Cepheid distance scale.

### 1.1 Research Motivation and Objectives
The primary motivation for this review is to assess the viability of proposed solutions in light of new data that was unavailable during the initial surge of theoretical proposals (2019–2022). Specifically, we aim to:
1.  Categorize and evaluate theoretical extensions to $\Lambda$CDM based on their ability to resolve the tension without breaking other cosmological constraints (e.g., BBN, BAO, $S_8$).
2.  Analyze the impact of recent observational milestones (JWST, DESI) on the validity of the tension itself.
3.  Identify the most promising avenues for future research, moving beyond simple parameter fitting to physical consistency checks.

## 2. Key Concepts and Definitions

To navigate the literature of the Hubble tension, several key concepts must be rigorously defined.

### 2.1 The Sound Horizon ($r_s$)
The sound horizon at the drag epoch ($r_d$ or $r_s$) is the fundamental ruler of the early Universe. It represents the distance sound waves could travel in the primordial plasma before baryons and photons decoupled. In the inverse distance ladder (CMB/BAO), $H_0$ is inversely proportional to $r_s$. To increase the inferred $H_0$ to match the local value (from ~67 to ~73), one must *decrease* the sound horizon by approximately 7% [cite: 6, 7]. This geometric necessity drives the majority of "early-time" solutions.

### 2.2 The Distance Ladder
The local measurement of $H_0$ relies on a three-rung ladder:
1.  **Geometry:** Parallax measurements of nearby anchors (e.g., Milky Way Cepheids, LMC, NGC 4258).
2.  **Calibrators:** Cepheid variables (or TRGB stars) in galaxies that also host Type Ia Supernovae (SN Ia).
3.  **Hubble Flow:** SN Ia in the smooth Hubble flow ($z > 0.02$).
The SH0ES team uses Cepheids as the primary rung 2 calibrator [cite: 1, 8]. The Chicago-Carnegie Hubble Program (CCHP) utilizes the Tip of the Red Giant Branch (TRGB) and J-Region Asymptotic Giant Branch (JAGB) stars as alternative calibrators [cite: 9, 10].

### 2.3 The $S_8$ Tension
A secondary tension exists in the amplitude of matter fluctuations, parameterized as $S_8 \equiv \sigma_8 \sqrt{\Omega_m/0.3}$. Weak lensing surveys (e.g., KiDS, DES) often measure a lower value of $S_8$ than that predicted by Planck $\Lambda$CDM. Crucially, many solutions that fix $H_0$ (particularly Early Dark Energy) tend to increase $\sigma_8$, thereby worsening the $S_8$ tension [cite: 6, 11, 12].

## 3. Historical Development and Milestones

### 3.1 The Divergence (2013–2019)
The tension began to crystallize with the release of Planck 2013 data, which favored a lower $H_0$ compared to the concurrent Riess et al. measurements. By 2019, the SH0ES team had reduced their uncertainties to below 2%, solidifying the discrepancy [cite: 5, 13].

### 3.2 The "Realm of Solutions" and "H0 Olympics" (2021–2022)
In 2021, Di Valentino et al. published "In the realm of the Hubble tension," a comprehensive catalog of proposed solutions [cite: 4, 5]. This was followed by the "H0 Olympics" (Schöneberg et al., 2022), which rigorously benchmarked 17 different models against a unified dataset. The "Olympics" concluded that while many models could alleviate the tension, few could do so without degrading the fit to other data (like BAO or SN Ia) or introducing fine-tuning [cite: 14, 15, 16].

### 3.3 The JWST and DESI Era (2024–2025)
The launch of JWST allowed for the resolution of Cepheids from their crowded backgrounds, testing the hypothesis that photometric confusion was biasing SH0ES results high. Simultaneously, the Dark Energy Spectroscopic Instrument (DESI) released Baryon Acoustic Oscillation (BAO) data that, for the first time, showed a preference for evolving dark energy ($w_0 > -1, w_a < 0$) over a cosmological constant, potentially reshaping the theoretical landscape [cite: 17, 18, 19].

## 4. Current State-of-the-Art Methods and Techniques

Proposed solutions are generally classified by the epoch in which they modify the standard physics: Early Universe (pre-recombination) and Late Universe (post-recombination).

### 4.1 Early Universe Solutions
These models aim to reduce the sound horizon ($r_s$) to yield a higher $H_0$.

#### 4.1.1 Early Dark Energy (EDE)
EDE introduces a scalar field that acts as a sub-dominant dark energy component prior to recombination, injecting energy and increasing the expansion rate briefly before decaying.
*   **Mechanism:** By increasing $H(z)$ early, $r_s$ is reduced.
*   **Status:** EDE was a top performer in the "H0 Olympics" [cite: 16]. However, it struggles with the "coincidence problem" (why does it peak exactly at matter-radiation equality?) and exacerbates the $S_8$ tension [cite: 6, 7].
*   **Recent Developments (2025):** Adi et al. (2025) have explored EDE's imprint on the 21-cm signal, proposing that upcoming radio interferometers like HERA could definitively distinguish EDE from $\Lambda$CDM [cite: 20, 21].

#### 4.1.2 New Early Dark Energy (NEDE)
A variation involving a phase transition in a dark sector, triggered by a second scalar field. This avoids some fine-tuning issues of canonical EDE and provides a better fit to CMB polarization data [cite: 15, 22].

#### 4.1.3 Dark Radiation and $N_{eff}$
Increasing the effective number of relativistic species ($N_{eff}$) increases the early expansion rate. While simple, this is tightly constrained by CMB damping tails and Big Bang Nucleosynthesis (BBN). Recent analyses combining DESI 2024 data suggest that dark radiation models (fluid or free-streaming) can reduce the tension to $\sim 2-3\sigma$ but cannot fully resolve it without conflicting with other bounds [cite: 23].

### 4.2 Late Universe Solutions
These models modify the expansion history at $z < 2$.

#### 4.2.1 Dynamical Dark Energy ($w_0 w_a$CDM)
The standard $\Lambda$CDM assumes a constant equation of state $w = -1$. Dynamical models allow $w$ to vary.
*   **DESI 2024/2025 Breakthrough:** The DESI collaboration reported a $>3\sigma$ preference for evolving dark energy ($w_0 > -1, w_a < 0$) when combining BAO with CMB and Supernovae [cite: 18, 19, 24].
*   **Impact:** While this relaxes the tension by widening the error bars and allowing for different expansion histories, it does not automatically produce the high $H_0$ required by SH0ES unless combined with phantom crossing ($w < -1$) at very late times [cite: 3, 25].

#### 4.2.2 Interacting Dark Energy (IDE)
IDE models posit an energy exchange between dark matter and dark energy.
*   **Mechanism:** This interaction can alter the scaling of matter density or dark energy density, effectively mimicking a higher $H_0$.
*   **2025 Status:** Zhai et al. (2025) found that including DESI data introduces a mild preference for energy transfer from dark matter to dark energy. However, the interaction strength is constrained to be small ($\epsilon \sim 10^{-4}$), limiting its ability to fully resolve the tension [cite: 26, 27].

#### 4.2.3 Late Dark Energy Modifications
Friedmann (2025) proposed a modification where dark energy within gravitationally bound structures does not affect internal space expansion, claiming to resolve the tension by reconciling direct and indirect measurements [cite: 28]. This represents a class of "screening" mechanisms.

## 5. Applications and Case Studies: The Observational Battleground

The "solution" to the Hubble tension might not be theoretical but observational. The 2024–2025 period saw intense scrutiny of the local distance ladder.

### 5.1 JWST: SH0ES vs. CCHP
The launch of JWST provided the capability to resolve Cepheid variables in the crowded environments of host galaxies, a long-suspected source of systematic error in HST measurements.
*   **SH0ES Analysis:** Riess et al. (2024) used JWST to observe Cepheids in NGC 4258 and SN Ia hosts. They found no significant evidence of photometric crowding error in the HST data. Their JWST-calibrated $H_0$ remained high (~73 km s$^{-1}$ Mpc$^{-1}$), reinforcing the tension [cite: 1, 9, 29, 30].
*   **CCHP Analysis:** Freedman et al. (2024) utilized JWST to measure distances using three independent calibrators: TRGB, JAGB, and Cepheids.
    *   **Result:** They found $H_0 \approx 69.96 \pm 1.05$ km s$^{-1}$ Mpc$^{-1}$ [cite: 9, 10].
    *   **Implication:** This value sits comfortably between the Planck value (67.4) and the SH0ES value (73.0), statistically consistent with both (within $\sim 2\sigma$). Freedman argues that the tension may be less severe than claimed, potentially an artifact of unrecognized systematics in the Cepheid rung or calibration differences [cite: 10, 31].

### 5.2 The DESI 2024/2025 Impact
The release of DESI's first-year BAO data provided the most precise measurement of the expansion history over the last 11 billion years.
*   **Findings:** DESI data, when combined with CMB, prefers a time-varying dark energy equation of state. This challenges the "constant" $\Lambda$ in $\Lambda$CDM [cite: 18, 32].
*   **Relevance to Tension:** While DESI alone does not yield a high $H_0$, the preference for dynamical dark energy opens the parameter space. Some analyses suggest that this dynamical behavior, if extrapolated to $z=0$, could alleviate the tension, though others argue it merely shifts the discrepancy to the supernova absolute magnitude calibration [cite: 3, 19].

## 6. Challenges and Open Problems

### 6.1 The $H_0$ vs. $S_8$ Trade-off
A persistent problem in "solving" the Hubble tension is the "Whac-A-Mole" effect with the $S_8$ tension. EDE models, which successfully raise $H_0$, typically increase the growth of structure (higher $\sigma_8$), worsening the discrepancy with weak lensing surveys [cite: 6, 11]. Mixed models (e.g., EDE + Interacting Dark Matter) have been proposed to suppress structure growth while boosting expansion, but these require fine-tuning and additional parameters [cite: 11].

### 6.2 The Coincidence Problem in EDE
Why would a scalar field become dynamically important exactly at the epoch of matter-radiation equality ($z \sim 3400$) and then disappear? This fine-tuning remains a theoretical embarrassment for EDE solutions, although "Triggered EDE" mechanisms have been proposed [cite: 7].

### 6.3 Systematics in the Local Ladder
The discrepancy between the SH0ES (Cepheid-based) and CCHP (TRGB/JAGB-based) results using JWST data indicates that systematics in the local distance ladder are not fully resolved. Until the difference between a $H_0$ of 70 and 73 is understood, theoretical solutions remain speculative [cite: 9, 10].

## 7. Future Research Directions

### 7.1 21-cm Cosmology
The 21-cm signal from the Cosmic Dawn and Epoch of Reionization offers a pristine probe of the early Universe. Adi et al. (2025) demonstrated that EDE leaves distinct imprints on the 21-cm power spectrum. Future data from HERA and SKA could detect these signatures, providing a "smoking gun" for early-time solutions independent of the CMB [cite: 20, 21].

### 7.2 Gravitational Waves (Standard Sirens)
Gravitational wave events with electromagnetic counterparts (like GW170817) provide a completely independent measurement of $H_0$. While current constraints are loose, future runs of LIGO/Virgo/KAGRA and next-gen detectors (Einstein Telescope) are expected to provide percent-level precision, potentially adjudicating between Planck and SH0ES without relying on cosmic ladders or CMB physics [cite: 1, 22].

### 7.3 Next-Generation CMB
The Simons Observatory and CMB-S4 will provide high-resolution measurements of the CMB damping tail and polarization. These will tightly constrain $N_{eff}$ and EDE models, potentially ruling out the entire class of early-time solutions if the standard $\Lambda$CDM predictions hold [cite: 1, 13].

## 8. Conclusion

In the realm of the Hubble tension, the landscape has shifted dramatically from 2021 to 2025. The "H0 Olympics" established that while early-time solutions like EDE are the most promising theoretical candidates, they come at the cost of increased complexity and tension with large-scale structure data ($S_8$).

However, the observational developments of 2024–2025 have introduced a new paradigm. The JWST results from the CCHP suggest that the local $H_0$ might be lower (~70 km s$^{-1}$ Mpc$^{-1}$) than previously thought, reducing the statistical significance of the tension. Simultaneously, DESI has provided the first strong evidence that Dark Energy may be dynamical rather than constant.

We are likely approaching a convergence point. If future JWST data confirms the lower CCHP value and DESI confirms dynamical dark energy, the "Hubble Tension" may dissolve into a combination of modest new physics (dynamical DE) and corrected systematics. Conversely, if SH0ES is correct and $H_0 \approx 73$, the failure of current models to simultaneously solve $H_0$ and $S_8$ suggests that our theoretical imagination—perhaps regarding the nature of gravity or the dark sector—is still missing a critical piece of the puzzle.

## References

[cite: 33] Friedmann, D. E. (2025). "The Change-Driver Account of Scientific Discovery: Philosophical and Historical Dimensions of the Discovery of the Expanding Universe." *Journal for General Philosophy of Science*, 56(2), 153-198. [cite: 33]
[cite: 34] Riess, A. G., et al. (2024). "JWST Observations Reject Unrecognized Crowding of Cepheid Photometry as an Explanation for the Hubble Tension at 8σ Confidence." *The Astrophysical Journal Letters*. [cite: 9, 29]
[cite: 35] Freedman, W. L., et al. (2024). "Status report on the Chicago-Carnegie Hubble program (CCHP): three independent astrophysical determinations of the Hubble constant using the James Webb Space Telescope." *arXiv preprint arXiv:2408.06153*. [cite: 9, 10]
[cite: 36] Planck Collaboration (2020). "Planck 2018 results. VI. Cosmological parameters." *Astronomy & Astrophysics*, 641, A6. [cite: 1, 2]
[cite: 37] DESI Collaboration (2024). "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations." *arXiv preprint arXiv:2404.03002*. [cite: 18, 19]
[cite: 9] Di Valentino, E., et al. (2021). "In the realm of the Hubble tension—a review of solutions." *Classical and Quantum Gravity*, 38, 153001. [cite: 4, 5]
[cite: 31] Schöneberg, N., et al. (2022). "The H0 Olympics: A fair ranking of proposed models." *Physics Reports*, 984, 1-55. [cite: 15, 16]
[cite: 1] Adi, T., Flitter, J., & Kovetz, E. D. (2025). "Early dark energy effects on the 21-cm signal." *Physical Review D*, 111, 043515. [cite: 20, 21]
[cite: 38] Zhai, Y., et al. (2025). "A low-redshift preference for an interacting dark energy model." *Journal of Cosmology and Astroparticle Physics*. [cite: 26]
[cite: 39] Poulin, V., Smith, T. L., & Karwal, T. (2023). "The Ups and Downs of Early Dark Energy solutions to the Hubble tension: A review of models, hints and constraints circa 2023." *Physics of the Dark Universe*. [cite: 6, 40]
[cite: 17] Yashiki, M. (2025). "Simultaneous resolution of H0 and S8 tensions with Early Dark Energy and Interacting Dark Matter." *arXiv preprint arXiv:2505.23382*. [cite: 11]
[cite: 18] Friedmann, D. E. (2025). "Resolving the Hubble Tension With a Late Dark Energy Modification to the ΛCDM Model." *International Astronomy and Astrophysics Research Journal*, 7(1), 1-14. [cite: 28]
[cite: 3] Wang, H., et al. (2024). "Dark energy in light of recent DESI 2024 data." *arXiv preprint arXiv:2404.18579*. [cite: 24]
[cite: 23] Seto, O., & Toda, Y. (2025). "Reduced Hubble tension in dark radiation models after DESI 2024." *arXiv preprint arXiv:2503.xxxx*. [cite: 23]
[cite: 24] Riess, A. G., & Breuval, L. (2023). "The Hubble Tension." *CERN Courier*. [cite: 1]
[cite: 4] Simon, T., et al. (2025). "Toward alleviating the H0 and S8 tensions with early dark energy-dark matter drag." *Physical Review D*, 111, 023523. [cite: 41]
[cite: 42] Giarè, W. (2024). "Inflation, the Hubble Tension and Early Dark Energy: an alternative overview." *Physical Review D*, 109, 123545. [cite: 43]
[cite: 8] Shah, R., et al. (2025). "Interacting dark sectors in light of DESI DR2." *ResearchGate*. [cite: 44]
[cite: 45] Cruz, H. A. G., et al. (2024). "21-cm fluctuations from primordial magnetic fields." *Physical Review D*, 109, 023518. [cite: 46]
[cite: 47] Madore, B. F., & Freedman, W. L. (2024). "The Hubble Tension." *Sky & Telescope*. [cite: 31]

**Sources:**
1. [cerncourier.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8PDFDnMgAaWhYcEG9h1zetSfeuLgzySPk0mCpQjM4nu1EnN6r6CnCes5bfhPDD9FFgGclc270KzJI8ElLxv4K4nlu8Zm0P98iG0WKn5WG7saPUAfgD9oYUKEwkjFezIAbM_Y=)
2. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsGhh462YQwih65mk_t5nAohqn2fq_UzaeUPZEcW7FmsX6j7zW4kkyorVfEdXt8FIKuvWZ0mL1WxL2DBUuADptqoj0QE5z7fA6awem8UIRRYULSsCDlA==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF54AvwvxvJCU7QNmwWqTOOLj5jX6QnKt2KZ59WePffY2iPHTTSDGOrGDuHvGep7rvQWtPFhjacO8nhRbPc3jlV51r7WSw4mqIOAIIbVxDVf6dG7cmOkMlD2g==)
4. [lucavisinelli.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnsfQvAfq7mfnxqEIaf_McBlkmhbWti1JX_FsQ-B9KlliwGHe3OsS94_l0ED0htIZ-PC2PjZIKNnxkuURLJhHH9JoNO2tO3n4GBIpbUcwJ6gLiwMacde9P4p9MhkfN8mNS-gtAHlbC5OBpxTgcDN4=)
5. [unesp.br](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQprxxukvZWPw9Yl2BFYBgn_q_5OSPdloFPv0_aafrjdk-y65iIUiiHZKnBGu2bBaGjwlzgBt_gsUTybuLMWGIzn86ZiYgJ8eJ_xLOUFDcO4MTFS0hNCHSaz6IQkJXfLDYvoKfoyoxNEXZlik4u8cJnPyI1jqL1VKom8PrjNzGukPWV380VDn-9If1cYRs9Xj9fJ2ra8Fkt7_OFJ7FS1LWGbuoQuGPmt0RQv55GWbGQ4OYVwCOD5kuhF2iHavGvKmb_UDHc7v0GVOPGlaNZ48st1fUEh0aCSInTywP361Y6QMBdOFpqadvdY_pWKfJqqUQuPPaMKyBtl9Wx4K3F7MlmtpzRl7WtYp5qFpCWeJQUxK7l-4hpD3n_U_cTUm4NbAZl7i8n3bBHRZ2JxCsBpkOTRo=)
6. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz8Sbg0z3np6jgCUif_ryYT3r7txIp6J261eS0KRAv09bJI-pZzIpX3FznHS10WYE5p2JQsNHccM4ul2Pfz2d1yFMtue8WxUK-CfIYAg0wHToXTrxCXQMUM4C8DfGrfGwcEy6Z6Il1jWlbNM5ztjkA_8WXuFQuD0haZoUK4vINYM9Pgu3z6aNLGEpwtJGY5KMR52Y=)
7. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfVUFQ737bM1qzhMXUXH7efEVK5TazbergVSeKSp-GptaMKVN3ZuRCf_bZt48i6wHX8vZNFoNAwITh0vMkns-J_GO2C5iHNmULcW5dQiDu9PAUljNHDr0bKnterrmvIOc=)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFGGfaSjutvpu_JfULYOUETp2TYh4eXjkv-ft8V2LJ1jzpZEWb25MovubafzODttLOPRhSx61q5_ZjRtStGUofPM5dGCu4rcM1-EAkGY7LebXbrqNl2Q==)
9. [quantamagazine.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZzVXAtl9FgDtVw1pv6kBHBqdSf8shARoPdgLQRrABB6QdnKKq7tmD0160wFU4ednwRz1f9-VgWkXeN8HdE-DvZ1p4O9S4jGPcisjKDzEUrsZS0x_b_TyuGy-QNgH49ZS6PM8ZoLiOGLuXXfJ8zhLD5cljC8ZrxOaN7lZtwmXp5McAu1z0GMDVA0jAb6UwJX23EJC4xGHWTcfukmUvj3WYI2Yboy6c)
10. [telescoper.blog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxbyW_wvYifw4Yard3U4U6wlRPXD1whPylpdWg0oiJcvMFVIgADI8NSy01CWifI_qMfMsm_uxj5KYinsbaVO414aBbj5tXLo2DZ_S864_6N-bcXuvF5X2E4k35djeKJegqs_73SxNytcxTmhiLULEJ)
11. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG21czp_Sth4185KmvViN2mh1wpVN2t4yDIwtwT0y2n046ip9ExThXUx6oVHP2ge1WPIGta0Gl5vcZGYQ_XjhBUlFYjokwDLJkl_ZA2TDDJNV5oD__CAQ==)
12. [whiterose.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeuzToiEJhDj3RZT6NarQBzX255vz82yDMtQQDmXyhK6KlCDB120lZIGyKbeuM5byYIBt4EfTfKwQkMaz3W0uEhkyTbn4ryWu3s18d7JT-0-T3P-k68Fr7FznwBE_nGnP6nL6TCVn6W-hfA4W7wc1G-iWgt0qD-OJ_YnKB3IbxpKR7RdAD3hWOIPKozm9cwONd0c3BCs5C7Ge8yG7DkwUXMn6q8qmAlLU=)
13. [swarthmore.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVjVoFkgM_x-PBhfUL-F-iCcJ6a4wvWnGn1SO45Q8QdpBwTae5DfyPgv33myKPfPvE-aytGkmYHJZmXPdXoQf1rysvzju_wenae6WSGp7sJwqrOOxelkjVTweaXonxvcJL3iOvdTD31WSWy9NTobsXDkcJojsSH2-XAyAUCKGjAOLJP0nRHcA=)
14. [smu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeGWnjfQV9h4x8NmQElUVhCJ6Sw8kANcW4paK-8Yod0Bd9i4_JOLuwTLbQrQzj2WYN9WQpLJzdBuS_dcsgZck8wykSjMACNvu4y-6KG59uexygxotDb_-zBEM2l6_j27v1uTDwqpH_TGCkuJnmFp2raJB4srZ0T96Yuuk519J43E2tRcVqmEyJMrL61uBBdgLucDyS-1dZnLKQigEZtMS5M65HproECfZtviIL6udistQr69ApsX4sH939I6wyu50A4E0RQ70DRwzW)
15. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiOkhxlNtQDl7MEkhsxPGE1lxcCebzBshZKBUcIUk_C2_Nz9OyPbnfrUIKpfNzdae8oII7jLttLXt11x_WbNC8N0cmeq1whk3bay-5ZrWJeFTOeM7S8HOefg==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5g7oTBgqn8MBJlzmvNNpt0bHtaiRCFreezYCGK9tJfZrxRBM7Mdks9Rrto5OPxXHnI72UfqtrH9gCjOS_J4cU9SHibiaLWVwqle_OedxoG5u8PcbAkYbDs2rF2QfimyyZDaKIUrJmrhRkQSbaz15txKJhfLTErZjUb8AqohdOYyjc3uDnQzre_MJDis8AdG0uF651FqeXaYyVWQ==)
17. [hawaii.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRAo2y5JlQ5dcuw4ALTB1D1FB0BakvB70bJ2wko01GxMGo_Ab3oT4wyzE7sBOWDdgHhO2-w7TCgH2KIMhj3fy0hL5Cfem4Rwrc4FPv3G80LRMcIby7l0xweEBTpO7QL9cm1pyLjZC4l84eGVpGuQGPnvOKOHKHRFGZILXpHq4vt5ai7Kxd-WBZOWWkbh2REA==)
18. [cerncourier.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh9IyuKyaG5hj_dVTHTc48zXkpC-LvlhmyhVB9_4K8UeLXOL1GGJYDVsyN7JKss_gAmiPD7Md8ew2VGaBOpUBIQqqLNq7VQE2WCh1ewiH2FjFuPv4tvCjX5cAj7X2xuw9bdPCJc1fUoFHvFfu2WCDfU1bT1KH8W-BGRpdWOcqnCouNAA==)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdar5QVfNOsBjdidGjCQEsjsgUSVZeamXArKrs2F3mWyfxTtv0OxQ5L2dYPjlUWst-Nf8FevBe9bt-Vy1Jo5EB4lBe1lBNWjGf8nKmamYRM8KaEF4liwUc2Q==)
20. [aanda.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkA8HrLwVTx_hNh-ecSDxZ_H4XSQE4-KnC_6p1IWhwtO5FO4EElKQeiw7R5Mu6fTd0bcvEh0KGT4Tpx3VZvg7cytwVPcyITdhI32nPgaiPdbECKAmWtXFP1kd8VKcy8iSeXm33bvEDMoDripjTZIuH6yVv9yUwrBJSARG61EZ5Q6ZqjH4=)
21. [bgu.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzgWhQU4DSoo03kWhPrLrl5BaeOfuK5wiRqOG7__KXanHecKo04eKA1Vng62y12AEdt6EdyyPYagt_FNNlPJivoBECJpTb-vU9qu4rLgCLtklu9Q5ST_wakpWj3r5sN2reqcJYomtGNH9AzZ3DoAwQt_tXL3LOKFL-sGKz0geTN5tlt4bzMXPlAplH)
22. [cern.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDsZzJzsMYoFpTAq7bZI0_kyZobAdffCGrpCFFKmxliVbUqTEs0Lk4gCkMW4J3qGrMC04ms-dvNYrraJASlBIxDMmz1bUQ2Z0uws5FJ8ILgBvAJtzk0UUDe1ILMuRYb4xbD7VT0XwlwOhZMetVJEByss0G-6_CmqdSXlsYKbr9C4CZSvS3de-mLpPiImewpUocq5KgMWqfv2JRmw==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXSS0uICiUzyh0GOz1cKP8dRx0FfUYvmLXs6RMoVXAB73bWj_HHeyxdg9Qj6qWwnQJ0CSuzyWDtAEn3rBG5AxpNLvpy3RA-b9Krd0p3NEjf8EcUGEXeNHgDFByhZ-vV6419_u59ZeYmzPoHbW8PaGy5OZi_XRF1SUkXBnUA6bJHtzjkoVUjDgUPuL7vxBNsl97y_kzyY9FlfVL9p2Et0vflpUh1D5qZcA=)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7mEnnN87CtVjAGm3jL9sxBl6Eozp8cH-SDEAJTEjgmJu1XiercsB1jWJetHWknrsX1VAcrU01V6pJScQbkBpJjq3JEolB5VF4-vDjw_kWjNKDX2Jlxw==)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExX_7_tpj1Pjuw4MxwyVg0E4IK7tE-GsSYgGX5AAb9P7qhqw3v_7Czx8tsOHgYmfRz7Nv1mX86iL07tmH8qhNqykCkGC4fUTnfn9q-9bBu9IEv6m3ULbCkOA==)
26. [whiterose.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETjPh1E6MqbXobVCniuClFIrnPQUBEC6ubFGL-Gs9i_n5XpF6TDi2tIhTNaOIixXZHYUKoKVHJfLpRBsbc12YpT42zqHAD4D_5y3g1PZrjeiIgaOerUEwvfW3SXABqOHWj-sir_obQDrJDt2941i9hVAvZ-CYOrdAlAGRYsRpA4fjZWLrBlotjhABy3-S5IFeeyeLtxP9KxlpN6g==)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0xQ89FgrDS3b3l6C3CWg1ANsyV54wc-w-5LQe1HU7htERMkmW1BqoJ5yBKGxqwnFDg1VidsMCbQMfmA63ONe8DBhuXjHONgTkLTTPj_YZZ6w9DCFNcg==)
28. [journaliaarj.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgo7ff8QdCBv-IfxYUvgY9fjYqawUC0S8gCCpNuzUJ5pEi0OYKsyrSrWzARYTaD13PUuVjy06dlgeoP26atuOzNgyNo7GmJocU7Zv8SV3f2UF1sOH9Cm9LgM-dBA_qO5DOaXYgomL6BAR7wXYO5tGkBhfD)
29. [columbia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxRHZxllQ4OGKty6wyhdpsNJaIFeuLycaX_-pWp5XpyQCKbrvvB8wJ6-frFdW8tzi-T5tJHxEjZyxAhU4eMrZVAlGJDE9H8CeLOL4uGpqkBjdhHwo-dhX1tfjn4O0hvPxAUBUu0YRg-Q9QETmTBduJKw==)
30. [esawebb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhcV5U9skk-qHQeyDfgHn5NwvEJJ5bl9quPQ9s6a5o3kWPMxkxtbSbDiPLNHISxLVRxd9nhBHFpfFfl-xEFsyqAOMnAi-s9qSdh2_mj_RH51-Cb7wFr5ZU)
31. [skyandtelescope.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEDiH711_aNiSBuiQ5MaQ9xof80GecHwQ5dd2yAZSTge_ohGmZOn_0C5eCNbdfhrnNK3iuBPG4_7ZE_MEwMt7Gy5pvzSekINypOv54t4dZQIyekWC7oS3dfeL50eeBC_ltKE3AbVdzn5Sb_4DfXrSWzdp0HaQ-TefcCaxNPUQ=)
32. [lbl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqsxH7QqWowpYaDdLX2_sYj2HAOTmphoeCogLqmh0UJq6KV_W5JHKDxP8K-vyTA3Te99FpbWrRpmEWoN5AY1T3si8EbleZdtPB5_1kqBvhOVOkl3YmOun--FSiALaVrEk3L0Nknl67r_SuBxN3P_s5rjhW2Ip3LgUQNjVmBxdctWTdeaV56YK_KdJSn8EyGjPTpccKDV1z6AZlntpfTrUuCiAgUJ7vpuqi8H7mwJm6a2o2OBTIpuhwMPBi3EkL1OlPh5dG3B7UDcM-)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAFJCovmovljky8k4PdMzaHvNJ_lcfqnLmevpCSiExUOlWZhwTipb8tsmSiiH4TI7qUeJF94o094l0sYhF4ztr1gQE16-2AEnmofGzgcKMMLqQfB1Bj0fMTXhskqX0T5F2Yx-dXEnClqWBgZfwE5F7J5ztO1xqyD2KTaphZRqyQBxcsfWn7UacR4DnzJmLNT2vtsv6HhsM7gAwTNld_2QJf3xIU-3N1GvBRhOiuOe-iVhLJZDbcYBaD8BO_Fqbm3dV4RMGi1ZrauEmmIfJA3WRwE3CKFad7PZwmoUo_Gi5Qb0ITzyyn8jfYlukFPGg)
34. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHaZiAK_kMPtT_-vissxoWCNaedIBCCCV3XdgABeLM75cNtOVn9_79Vv2_hPRtsX0KnR4kog5m0c3EzmdbKVYTptPxjQvROwGqWD_Ox2M7heL9U_4ZDdumbxWKNgLDaKMcf246XacMn6NHDZxZWvIGbUP5dbgehyrakkz_V_wCnKUDTaGtNJjZFJBP2E4xC1YQ)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjOm0paDFcKZPhhaXLwwFNUNVxbdVChcbYhCqBh4A7L_Hggwjx2J60t5THXvaWcwOV4PgNSS6xJ5y7wbPpaGEyn31QA2nnt1j_s0PJLZlsm6u_3yx1VVB8_eVwH2P0J7m7MiMZxNIOGxCpFOr8OCPNyPP26B6dngT6_GBwNEIYeC9zUVYvNTXqxovHXfGqDAIN7So=)
36. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYyTpv0A2qFeJ_CGrszsdjZB5unwf2rVu7faFNWBlHq6v6l7lDfad5qYvWnq2zFDK2R2nF9d09LTJHuXALDl95n4G3a4DqfE4oBHDHKGLH48i21stVdw==)
37. [usp.br](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwVzmuVrmJFFHQqNRNigIR7gaLDCbgTo38i2xoUU2iHnJgnl6z3s3TqPU1imijVmj27XmQai61YRZ1XmbKD_5A8X5yaoM8QpqTjNIvuqdJMC1Nr3bGjuuuAAWc7UWNeltb6JpUuZyvUWtxB8NEGuqvv_j1LjqUd8TfZ2Z-wtBgRitWz7NTF5Cf_2raSzjvei76aYKzP9Q=)
38. [washingtonpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsn7obmeOcMoc-nH8tisGRmRPPlYwQm3xzDl7ZZj_-8JVc6SCgNOkYwpeqt9_3oueuN_ts71NYKwZf26vCA8K9wnNeQbIVb-p84myVW6yY3LOprEptBiPt4a2vmjIjNvQGfD2Msu3reppJq5rYlVjHYLY75bf7CSXd_VsKLqfh68ylVB44IeQHbS23)
39. [centauri-dreams.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8kBh57_jTqwC5zptQkrGjPjVbJdiNJ8uZs_LCxacuhP09-WnNpCLoE7ryt-wbLluhCWNaTkb4Ksk8-Pm_TWEmPcjgYFcBV3KrCKzjUt2V8ydsfcBh6CozKQLsYktzVMQ8gnKJJ8F5fqxZ8NvFZsrUqGfqGuXcw0XZUFr9FAEw23EWlchIcJSg2hsRlkmvxsa7NmzodH9UAw==)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEB9i6D3aN8HZRhTvpMvqI6KuIacezPj39z_x_9UNPyDGxDOgud9CCPauC8tQ56TZD3H7gx0I60DjJHetHvJrRsG7vmhLIHEjBh6RGFmqG3R7v0I0-UGScu-A==)
41. [iucc.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbaO2xxoty_S5olo_26tisy_sJN--eO5r-3SgiQXOOUUj4zVWlyGuM1UsJyB5BOM46TILyWZBEGU03v8kAVmq2o3XffJyrLOIt5EPWQu1XJKFtiDTElLzmUXRWCC1HUr2yZ_s=)
42. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDM5xuVXTVAq77ElFin28akP8vtDGuv_igmCi4uEoEVNe3aCXX2cerxzhZkU3nXfIgjzOL97UPE_teJXEhL6EXoyf5seGcf9bm6GQXpcZWPo8KChd-IAmA-hrJu4fzwPZNvuEwnsKMH4tCL1FS_k8KUQhdOFan_bGE3JktBVGNGfePzoo=)
43. [williamgiare.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGAh1mna_lDXF8VBX2r2YvNETZvtbohHcSmZrX3mZq6W0A79UtGacYAcMXqwO2olymwVyioAo1H1Y0VXnAoaXnNYgkgNYhVoRDO0MZxifvJobNXVW0VVshZqJ41cGhNQ==)
44. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy1OKEHVFX8nUIZ8bTr1EWCzmUEUerxD2qI5sWT21w1k9RyfZ0r9dELxuJf30X8non3AT_muiQo3tQ4UdKJdKm6iyCNZsx44wgESn9ogOeXTv1V5393t16A0tC_NLpc40IDGdqYpnKIifg3DB8bxtHhLYEne7YrzBBeB8Bx9irKX0uWQwChiImBcvqvfPuDquJpXI5PIgHLLS3h79fC4sb9g_zGlIUIQ==)
45. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELH24OE5zE_JmqYt67v5BqVgOuW1a92K-SGjK6UaLrjjK6faG01oDiTpNXCGH-qSWRPnhmAtju7egIPJ21hgrQ8z0bsUevLQ5NS3YJ5YTj-W4xiTB6IyuQDQ==)
46. [bgu.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7dTVr_bjaCZx4k9fQsL6fHo-wz12RncjECT_l4e2QkotQOdnr68B4l0mx8HPiGwNDm-QRHR5jgpR6p9M5WU0A4yY8Q4_jY_rJY-QDkL3SzfN2TDpYLa2xqkO_xctRs5V3Al0=)
47. [york.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpiDzZ4vVuH6wliwLdREdWIk_y1DnFd8xDRAvXWVQrZA6MiXlnm-Eg9VyLJucZ7YrEmv1YdOg3aMrP65fCe5z1Yf2ZKZ-K-RUnui5zytRs58mLyUE9gDzKe2Lh_-sMwjDHlT4r1tQc_N-4j8HNyqWyhjUJjrL3cpYkDW0JrJkm1_hbwSdRhngXCNsenJDWPEmfTq6eZQWfETnfoJedHar6n2PHYuoGk4GQa5I8eLDHwykXO_Lg5NBY3QXmiQ0FBgrxVR9Oxlu2Jjlmsg==)
