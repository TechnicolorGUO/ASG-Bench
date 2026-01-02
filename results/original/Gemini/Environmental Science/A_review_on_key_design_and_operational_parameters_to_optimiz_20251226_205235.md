# Literature Review: A review on key design and operational parameters to optimize and develop hydrothermal liquefaction of biomass for biorefinery applications.

*Generated on: 2025-12-26 20:52:35*
*Progress: [27/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/A_review_on_key_design_and_operational_parameters_to_optimiz_20251226_205235.md*
---

# A Review on Key Design and Operational Parameters to Optimize and Develop Hydrothermal Liquefaction of Biomass for Biorefinery Applications

**Key Points**
*   **Hydrothermal Liquefaction (HTL)** is a thermochemical process that converts wet biomass (algae, sludge, lignocellulose) into biocrude oil using hot, pressurized water (sub- or supercritical), eliminating the need for energy-intensive drying.
*   **Operational Parameters:** Temperature (typically 250–374°C for subcritical, >374°C for supercritical) is the most critical factor influencing yield; pressure is maintained to keep water in the liquid phase. Residence time and heating rate significantly affect the depolymerization and repolymerization pathways.
*   **Feedstock Chemistry:** Lipids produce the highest biocrude yields. Proteins and carbohydrates interact via **Maillard reactions**, which can increase yield but introduce nitrogen into the biocrude, requiring upgrading (hydrodenitrogenation).
*   **State-of-the-Art:** The field is transitioning from batch reactors to continuous-flow systems. Notable pilot technologies include **Genifuel’s** subcritical process (wastewater sludge) and **Steeper Energy’s** supercritical Hydrofaction® (forestry residues).
*   **Major Challenges:** The management of the **Aqueous Phase (HTL-AP)**—which contains dissolved organics and nutrients—is a critical bottleneck. Valorization strategies include anaerobic digestion and catalytic gasification. Biocrude upgrading to drop-in fuels remains technically demanding due to heteroatom (O, N) content.

---

## Abstract

Hydrothermal liquefaction (HTL) has emerged as a pivotal technology for the valorization of wet biomass streams, offering a pathway to produce high-energy-density biocrude oil without the energy penalty of feedstock drying. This systematic literature review provides a comprehensive analysis of the key design and operational parameters governing the HTL process, including temperature, pressure, residence time, catalyst application, and feedstock composition. We critically examine the transition from batch-scale experimentation to continuous-flow pilot demonstrations, highlighting state-of-the-art reactor configurations such as oscillatory flow and supercritical systems. Special attention is given to reaction mechanisms, particularly the role of Maillard reactions in mixed-feedstock liquefaction, and the techno-economic implications of biocrude upgrading. Furthermore, the review addresses the environmental and operational challenges posed by the aqueous phase by-product (HTL-AP), evaluating integration strategies for nutrient recovery and energy efficiency. The paper concludes by identifying research gaps in scale-up, corrosion management, and lifecycle assessment, proposing a roadmap for the integration of HTL into future biorefineries.

---

## 1. Introduction

The global transition toward renewable energy systems has necessitated the development of technologies capable of converting diverse biomass feedstocks into liquid transportation fuels and chemicals. Among thermochemical conversion pathways, Hydrothermal Liquefaction (HTL) stands out for its unique ability to process wet feedstocks—such as sewage sludge, algae, and agricultural residues—without the requirement for pre-drying, which is a major energetic and economic barrier in pyrolysis and gasification [cite: 1, 2].

HTL mimics and accelerates the natural geological processes of petroleum formation, converting biomass into a liquid "biocrude" oil, a solid residue (hydrochar), an aqueous phase containing soluble organics, and a gaseous fraction [cite: 3, 4]. The process operates in a hot, pressurized water environment, typically at temperatures between 250°C and 400°C and pressures of 5–25 MPa [cite: 3, 5]. Under these conditions, water exhibits unique physicochemical properties, acting as a solvent, reactant, and catalyst to facilitate the depolymerization of biopolymers [cite: 2, 6].

Despite its potential, the commercialization of HTL faces significant hurdles related to process optimization, product quality, and waste management. The complexity of biomass feedstocks leads to intricate reaction networks, where operational parameters must be precisely tuned to maximize biocrude yield while minimizing char formation and heteroatom (oxygen and nitrogen) content [cite: 2, 7]. Furthermore, the inevitable production of a high-strength wastewater stream (HTL-AP) presents both a disposal challenge and a resource recovery opportunity [cite: 8].

This review aims to synthesize existing literature on the optimization of HTL, focusing on the interplay between design parameters and operational conditions. It integrates findings from fundamental batch studies with recent data from continuous-flow pilot plants to provide a holistic view of the technology's current status and future trajectory.

---

## 2. Key Concepts and Definitions

### 2.1 Hydrothermal Regimes
The properties of water change drastically with temperature and pressure, defining two primary operational regimes for HTL:
*   **Subcritical Water Liquefaction:** Occurs below the critical point of water (374°C, 22.1 MPa). In this region, the dielectric constant of water decreases significantly, allowing it to dissolve hydrophobic organic compounds (like lipids and lignin) while maintaining a high ionic product, which favors ionic reaction mechanisms such as hydrolysis [cite: 2, 6]. Most current pilot plants operate in this regime (approx. 300–350°C) [cite: 1, 9].
*   **Supercritical Water Liquefaction:** Occurs above the critical point. Here, water behaves as a non-polar solvent with high diffusivity and low viscosity, eliminating interphase mass transfer limitations. This regime typically suppresses char formation and enhances reaction rates but requires higher capital investment due to extreme pressure requirements [cite: 10, 11].

### 2.2 Product Fractions
*   **Biocrude:** The primary target product, a dark, viscous oil with a heating value of 30–40 MJ/kg. It differs from petroleum crude by having higher oxygen (5–20%) and nitrogen contents, necessitating catalytic upgrading (hydrotreating) to produce drop-in fuels [cite: 3, 4].
*   **Aqueous Phase (HTL-AP):** A water-rich stream containing dissolved organic carbon (DOC), ammonia, and alkali metals. It represents a loss of carbon efficiency if not valorized and a toxicity hazard if discharged [cite: 8].
*   **Hydrochar:** A solid residue rich in carbon and inorganic ash. It can be used for soil amendment, adsorption, or energy recovery via combustion [cite: 4, 12].

### 2.3 Reaction Mechanisms
HTL involves a cascade of reactions:
1.  **Depolymerization/Hydrolysis:** Macromolecules (proteins, carbohydrates, lipids) break down into monomers (amino acids, sugars, fatty acids) [cite: 13, 14].
2.  **Decomposition:** Monomers degrade via dehydration, decarboxylation, and deamination [cite: 3, 13].
3.  **Repolymerization/Recombination:** Reactive fragments recombine to form larger molecules (biocrude components) or solid char [cite: 2, 4].

---

## 3. Historical Development and Milestones

### 3.1 Early Foundations (1920s–1980s)
The concept of converting biomass to oil using hot water and alkali catalysts dates back to the 1920s. Significant development occurred during the 1970s oil crisis, leading to the **Pittsburgh Energy Research Center (PERC)** process and the **Lawrence Berkeley Laboratory (LBL)** process. These efforts culminated in the Albany Biomass Liquefaction Experimental Facility (Oregon, USA), which demonstrated the feasibility of wood-to-oil conversion but struggled with technical complexities and pumping issues [cite: 3].

### 3.2 The Algae Boom (2008–2015)
Interest in HTL resurged in the 2000s, driven by the search for third-generation biofuels. Research focused heavily on microalgae due to its high growth rates and lipid content. Studies established that HTL was superior to lipid extraction for wet algae because it converted the entire biomass (including proteins and carbohydrates) into biocrude [cite: 15, 16].

### 3.3 Shift to Waste Valorization and Continuous Flow (2015–Present)
Recent years have seen a strategic pivot toward waste feedstocks—sewage sludge, manure, and forestry residues—driven by the "negative cost" of waste disposal and circular economy goals [cite: 1, 17]. This era is marked by the transition from batch reactors to continuous-flow pilot plants.
*   **Milestone:** The development of the **PNNL Modular Hydrothermal Liquefaction System (MHTLS)**, which successfully processed diverse wet wastes [cite: 1, 18].
*   **Milestone:** The establishment of **Steeper Energy’s** Hydrofaction® technology, advancing supercritical processing of forestry residues [cite: 11, 19].
*   **Milestone:** The **Metro Vancouver/Genifuel** partnership (2018–2024), aiming to build the first commercial-demonstration scale HTL plant for municipal wastewater sludge in North America [cite: 20, 21, 22].

---

## 4. Key Design and Operational Parameters

Optimizing HTL requires a precise balance of thermodynamic and kinetic parameters. The following sections detail the critical variables influencing biocrude yield and quality.

### 4.1 Temperature
Temperature is the most dominant parameter in HTL.
*   **Yield Optimization:** For most biomass types, biocrude yield peaks between **300°C and 350°C**. Below this range, hydrolysis is incomplete; above it, secondary cracking reactions convert the biocrude into gases and water-soluble organics, reducing oil yield [cite: 2, 23, 24].
*   **Quality vs. Quantity:** Higher temperatures (approaching supercritical) enhance deoxygenation, resulting in a biocrude with higher calorific value (HHV) and lower viscosity, albeit at the cost of reduced mass yield [cite: 24, 25].
*   **Phase Behavior:** Temperature dictates the phase state of water. Supercritical conditions (>374°C) eliminate phase boundaries, promoting rapid hydrolysis and suppressing char formation via the "cage effect" of the solvent [cite: 10, 11].

### 4.2 Pressure
While pressure is primarily applied to maintain water in the liquid phase (preventing boiling), it plays a secondary role in reaction chemistry.
*   **Subcritical:** Pressures of 10–25 MPa are standard. Pressure changes in this range have minimal effect on yield compared to temperature [cite: 3, 23].
*   **Supercritical:** At supercritical conditions, pressure tuning can significantly alter fluid density and solvent power, influencing the solubility of precursors and the extraction efficiency of the biocrude [cite: 23].

### 4.3 Residence Time
Residence time determines the extent of depolymerization and repolymerization.
*   **Optimal Range:** Typical residence times range from **10 to 60 minutes** in continuous systems [cite: 3].
*   **Kinetics:** Short times may lead to incomplete conversion. excessively long times favor the formation of char (via polymerization) and gas (via cracking). Recent fast-HTL studies suggest that very short residence times (<5 min) at high heating rates can maximize yield by minimizing secondary decomposition [cite: 12, 13].

### 4.4 Feedstock Composition and Maillard Reactions
The biochemical composition (lipids, proteins, carbohydrates, lignin) dictates the reaction pathways.
*   **Lipids:** The most desirable component, converting to biocrude with high efficiency (>90% conversion) and high H/C ratios [cite: 26, 27].
*   **Proteins:** Hydrolyze to amino acids. While they contribute to biocrude yield, they introduce nitrogen, which is a contaminant in fuels [cite: 26].
*   **Carbohydrates:** Generally produce lower biocrude yields (10–15%) and higher solid/char fractions compared to lipids [cite: 26].
*   **Maillard Reactions:** In mixed feedstocks (e.g., sewage sludge, algae), proteins and carbohydrates interact via the Maillard reaction. This produces nitrogen-containing heterocyclic compounds (e.g., pyrazines, pyrroles). While this interaction can synergistically increase biocrude yield (up to 25% higher than predicted by additive models), it complicates upgrading by locking nitrogen into stable cyclic structures [cite: 28, 29, 30].

### 4.5 Catalysts
Catalysts are employed to enhance yield, improve quality (deoxygenation), and suppress char.
*   **Homogeneous Alkali Catalysts:** Sodium carbonate ($Na_2CO_3$) and potassium carbonate ($K_2CO_3$) are widely used. They promote water-gas shift reactions, reduce char formation, and buffer the pH to prevent corrosion [cite: 2, 15, 25].
*   **Heterogeneous Catalysts:** Transition metals (Ni, Co, Mo) on supports (ZSM-5, Al2O3) are investigated for *in-situ* upgrading. However, catalyst recovery and fouling/deactivation in the harsh HTL environment remain significant challenges [cite: 25, 31].

---

## 5. Current State-of-the-Art Methods and Techniques

The field has moved beyond batch autoclaves to continuous-flow systems that better simulate industrial reality.

### 5.1 Continuous Flow Reactor Designs
*   **Plug-Flow Reactors (PFR):** The most common design (e.g., PNNL, University of Sydney). Slurry is pumped through a long heated tube. Challenges include wall fouling and pressure drops [cite: 6, 12].
*   **Oscillatory Flow Reactors:** Developed at **Aarhus University**, this design uses hydraulic oscillation to create turbulence, improving heat transfer and mixing while preventing solids settling and clogging. This allows for processing slurries with higher dry matter content (up to 16-20%) [cite: 32, 33].
*   **Continuous Stirred-Tank Reactors (CSTR):** Used in conjunction with PFRs (e.g., PNNL) to handle high-solids slurries and facilitate pre-heating [cite: 9].

### 5.2 Pilot Plant Case Studies
*   **PNNL & Genifuel (USA/Canada):** PNNL developed a modular HTL system focusing on wet wastes. This technology was licensed to Genifuel Corp. A major demonstration project with **Metro Vancouver** (Annacis Island WWTP) is currently fabricating a pilot to process ~10 wet tonnes/day of sewage sludge. This represents a critical step in validating HTL for municipal waste management [cite: 1, 20, 21, 22].
*   **Steeper Energy (Denmark/Canada):** Steeper utilizes the **Hydrofaction®** process, which operates at supercritical conditions (>374°C, 300 bar). This high-energy state promotes efficient conversion of lignocellulosic biomass (forestry residues). They have successfully demonstrated the technology at pilot scale in Denmark and are developing a commercial facility in Alberta, Canada, to process forestry waste [cite: 11, 19, 34, 35].
*   **Aarhus University (Denmark):** Operates a pilot plant featuring heat recovery (up to 80% efficiency) and the aforementioned oscillatory flow system. They have extensively tested diverse feedstocks including Miscanthus, Spirulina, and sewage sludge, reporting energy return on investment (EROI) values of 2.8–3.3 for crops but lower (0.5) for sludge without optimization [cite: 32, 36].

---

## 6. Challenges and Open Problems

### 6.1 Aqueous Phase (HTL-AP) Management
The aqueous phase is often described as a "double-edged sword" [cite: 8, 37]. It contains 20–50% of the feedstock carbon and significant nutrients (N, P), but also toxic phenols and nitrogen heterocycles.
*   **Problem:** Discharging HTL-AP to wastewater treatment plants can inhibit biological treatment processes due to its toxicity [cite: 8, 37].
*   **Opportunity:** Valorization strategies include **Anaerobic Digestion (AD)** (to produce biogas), though this requires acclimated microbes or dilution [cite: 38, 39]. Other methods include **Catalytic Hydrothermal Gasification (CHG)** to produce hydrogen/methane, or recycling the AP back into the reactor to increase biocrude yield, although this can lead to the accumulation of inhibitors [cite: 40, 41].

### 6.2 Biocrude Quality and Upgrading
HTL biocrude is not a finished fuel. It has high viscosity, acidity (TAN), and heteroatom content.
*   **Nitrogen:** Nitrogen content (especially from protein-rich sludge/algae) poisons refinery catalysts. Hydrodenitrogenation (HDN) is difficult because nitrogen is often bound in stable aromatic rings (Maillard products) [cite: 16, 23, 29].
*   **Oxygen:** Oxygen content reduces energy density and stability. Hydrodeoxygenation (HDO) requires significant hydrogen input, impacting process economics [cite: 1, 42].

### 6.3 Engineering and Scale-up
*   **Pumping:** Feeding high-viscosity, high-solids slurries (15–25% dry matter) against high pressure (200 bar) is mechanically difficult. Reciprocating pumps are prone to wear from abrasive ash [cite: 23, 43].
*   **Corrosion:** The combination of high temperature, pressure, acidic organic products, and inorganic salts creates an extremely corrosive environment, necessitating expensive alloys (e.g., Inconel) [cite: 2, 44].
*   **Fouling/Clogging:** Char formation and salt precipitation can block reactor tubes and heat exchangers, reducing thermal efficiency and run times [cite: 33, 43].

---

## 7. Future Research Directions

To achieve commercial viability, research must pivot toward integration and efficiency:
1.  **Integrated Biorefineries:** Developing closed-loop systems where HTL-AP is valorized (e.g., via CHG or AD) to provide energy (biogas/hydrogen) for the HTL unit and upgrading steps [cite: 8, 38].
2.  **Advanced Catalysts:** Developing robust, water-tolerant heterogeneous catalysts that can perform *in-situ* upgrading (deoxygenation/denitrogenation) within the HTL reactor to produce a higher-quality biocrude directly [cite: 25, 45].
3.  **Co-processing:** Investigating the co-liquefaction of complementary feedstocks (e.g., plastic waste + biomass, or high-lipid + high-protein streams) to exploit synergistic effects and balance the H/C ratio [cite: 46, 47].
4.  **Techno-Economic & Lifecycle Analysis (TEA/LCA):** rigorous validation of the economic and environmental benefits of full-scale plants, particularly focusing on the trade-offs between subcritical and supercritical operation and the cost of wastewater treatment [cite: 1, 42].

---

## 8. Conclusion

Hydrothermal liquefaction represents a transformative technology for the biorefinery sector, uniquely positioned to unlock the energy potential of wet waste streams. The field has matured from fundamental batch studies to sophisticated continuous-flow pilot demonstrations, with commercial-scale projects like those of Genifuel and Steeper Energy on the horizon.

Optimization relies on a nuanced control of operational parameters—specifically temperature (300–350°C for subcritical yield, >374°C for supercritical quality) and residence time—tailored to the specific biochemical composition of the feedstock. While the Maillard reaction offers pathways to enhance yield in mixed feedstocks, it necessitates advanced upgrading strategies to manage nitrogen content.

The path to widespread adoption hinges on resolving the "aqueous phase challenge" through efficient valorization technologies and overcoming engineering hurdles related to pumping and corrosion. By integrating HTL into existing waste management and refinery infrastructures, it offers a viable route to a circular bioeconomy, turning societal waste into sustainable transportation fuels.

---

## References

*   **[cite: 1]** PNNL-27186. (2017). *Conceptual Biorefinery Design and Research Targeted for 2022: Hydrothermal Liquefaction Processing of Wet Waste to Fuels*. Pacific Northwest National Laboratory.
*   **[cite: 15]** Gollakota, A., et al. (2018). *A review on hydrothermal liquefaction of biomass*. Renewable and Sustainable Energy Reviews.
*   **[cite: 23]** MDPI. (2023). *Scaling up fuel production and overcoming high-pressure pumping challenges*. Molecules.
*   **[cite: 43]** Scribd. (2023). *Design and scale-up challenges in hydrothermal liquefaction*.
*   **[cite: 12]** Castello, D., et al. (2023). *A review on continuous biomass hydrothermal liquefaction systems*.
*   **[cite: 13]** MDPI. (2024). *Reaction Pathways in Hydrothermal Liquefaction*.
*   **[cite: 6]** Castello, D., Pedersen, T. H., & Rosendahl, L. A. (2018). *Continuous Hydrothermal Liquefaction of Biomass: A Critical Review*. Energies, 11(11), 3165.
*   **[cite: 32]** Aarhus University. (2018). *Continuous Hydrothermal Liquefaction of Biomass in a Novel Pilot Plant with Heat Recovery and Hydraulic Oscillation*.
*   **[cite: 33]** MDPI. (2021). *Design, modelling, and experimental validation of a scalable continuous-flow hydrothermal liquefaction pilot plant*. Processes.
*   **[cite: 10]** MDPI. (2021). *HTL is extreme pressure process with temperature ranges between 150 and 374 °C*. Processes.
*   **[cite: 3]** Wikipedia. (2024). *Hydrothermal liquefaction: History and Process*.
*   **[cite: 4]** WikiWaste. (2024). *Hydrothermal Liquefaction Process Mechanism*.
*   **[cite: 20]** Metro Vancouver. (2024). *Hydrothermal Liquefaction Explainer*. [Video].
*   **[cite: 2]** Basar, I. A., Liu, H., Carrere, H., Trably, E., & Eskicioglu, C. (2021). *A Review on Key Design and Operational Parameters to Optimize and Develop Hydrothermal Liquefaction of Biomass for Biorefinery Applications*. Green Chemistry, 23, 1404–1446.
*   **[cite: 8]** Watson, J., et al. (2024). *Valorization of hydrothermal liquefaction aqueous phase: pathways towards commercial viability*. Experts at Illinois.
*   **[cite: 37]** Watson, J., et al. (2020). *Valorization of hydrothermal liquefaction aqueous phase: pathways towards commercial viability*. Progress in Energy and Combustion Science, 77, 100819.
*   **[cite: 13]** MDPI. (2024). *Reaction Pathways in Hydrothermal Liquefaction*.
*   **[cite: 28]** ACS Sustainable Chem. Eng. (2022). *Elucidating the Maillard Reaction Mechanism in the Hydrothermal Liquefaction*.
*   **[cite: 26]** ACS. (2014). *Biocrude yields order: lipids > protein > carbohydrate*.
*   **[cite: 38]** ResearchGate. (2025). *Enhancing energy recovery via two stage co-fermentation of hydrothermal liquefaction aqueous phase*.
*   **[cite: 11]** Emissions Reduction Alberta. (2024). *The Conversion of Forestry Residue to Advanced Biofuels in Alberta*.
*   **[cite: 19]** Steeper Energy. (2024). *Commercialization Journey and Grants*.
*   **[cite: 25]** MDPI. (2022). *Catalysis during HTL: Homogeneous and Heterogeneous approaches*.
*   **[cite: 42]** PNNL-37209. (2024). *Key Cost/Process Drivers for Algae HTL*.
*   **[cite: 21]** Genifuel. (2020). *Progress on Metro Vancouver demonstration plant*.
*   **[cite: 22]** YouTube. (2025). *Genifuel Metro Vancouver HTL pilot plant status*.
*   **[cite: 9]** Energies. (2018). *Genifuel Corporation, in collaboration with Metro Vancouver, is developing a pilot HTL plant*.
*   **[cite: 34]** Emissions Reduction Alberta. (2024). *Steeper drives Alberta's leadership in next-gen renewable fuels*.
*   **[cite: 3]** Wikipedia. (2024). *Process parameters: Temperature 250-550 C*.
*   **[cite: 23]** MDPI. (2023). *Key Process Parameters: Temperature, Pressure, Heating Rate*.
*   **[cite: 29]** MDPI. (2021). *Maillard reactions hydrothermal liquefaction nitrogen biocrude*.
*   **[cite: 7]** Basar, I. A., et al. (2021). *A Review on Key Design and Operational Parameters...* Green Chemistry.
*   **[cite: 8]** Watson, J., et al. (2020). *Valorization of hydrothermal liquefaction aqueous phase*.
*   **[cite: 1]** PNNL-27186. (2017). *Conceptual Biorefinery Design... Targeted for 2022*.
*   **[cite: 18]** PNNL-30982. (2020). *State of Technology Assessment*.

**Sources:**
1. [pnnl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw80HXOg_9Oh2XA2kchWnMjnJhNUTT8lCq1juGJ7OIj0XA6bWs-tP3LiEk-DIXAB-z1kRgjTIIU51QzRs0_Ym1KkLAxFkvZTewX7_hugq94skd0llzmH_jCZLt3SymeNJb5oO_ZkZ_p9Fpr6BNygKZ5IYmZ9zhn6XcY1QPVrcooDkE5CwW)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHvWtdC3XCtlweUdwtzY_GR1FIL0QxPRumSBvcbBwO3XeWaN4iPn4d9456ZhoKAPSPY2K7iZNVqiRA8nkAvUf7G3pxvbrzIw2rYfdF2Z0faTycVYSgK21FjhN9w2uYoZiL9sbBfxQvogN1K49CY6VCXeDfQC6yUDgGpVJ6ajsUnmF5gEb28z0JVOM2NRf-tj7owYbCSTMLe58AWJZFQUsMVPfH-n7-6rmQSb5p5alKXnzeV11Nfc4DlWShdUFZHAZ-TlKCqpvUyAc35DpzpDJA1FxgOiqxrcdJB3WHTDYmeR7gLFXsDmCDjXwreeJxa3bQsxVg)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpVEqHtvyge3zplN2mUhS19R5iCi3SEjAnzP2xefyNFuud4LQYSixkuqczn69_DAUfA9Npv4u-8iNOZDY0qLIW4yVvtGDlgN35O6qHcQEMMexHJG35Vn0t534Y2ObUqWSlF0Bl1QRk-dUclTg=)
4. [wikiwaste.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXiUlVPyTDqBJQgDbbPQJ3NFwwjG4d5H1B-UoXtZbjDCyiwzDoumSakFfBhR5T4fIvfQghqgnb6i4x6X-fJ4sPXLFGxW291kLKSEoJ8p5IxQH7xcqbPeK-kGWW2fSUIQxnlr4io-nwy3XOmLQZ2JzWDg==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjoeWeiD33kuuCETMJx616xfCTrFVGI4Pta6ue4BxwmW2RaED0eVw0XdaOdiZmrLboCGRPpX2DbOTSODx2fvDIVV5F_btxW7fTrLi_ruMjBo7zhmNvRGtAHIZiFSxKL_Ej7oWSOtubB8m4dks90EiFuaWncMW84JNA27kXZKKx-2z-iblaavT2fabIQlEjTtDxIjXyyRZxupDSUA==)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmXsF_Log8Mj2A2BCD8cisz4meUXkBZIjy444p5nCFLx78LiWx0polewBqfiV3GpV-mjZ8ZGAs7YpW7xcPHCq6Ewlct3tWS42B-Qdz8x50AungIRZHo1EK-TTX-HN4)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQsWyZZEBMNgw9ENCCJIBhpnUqyrEtAGrfxVRD182KHu4lfaRl4nOyHyXaQyO_-7J4Yu0cHm4FcHNih-8ZC2O2l56fXyQm8UOeMLaQnHqWPksOIvHnGkqJG_IP9SlS)
8. [illinois.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBA_bLzDcXuw4q5MNbTbAFReq6NE256u7672EsqMmquR_1lTBaDwuSNEHTQRHg5nsmpJ5QUrYrpj6tUT_3jp7laQ3RglQsoktAI1zVYR2YF9GFC8PxCnFl6dAv6PSNxCPPecLqm-7QP3xvQOKmlOeD6BBHW1umB9-ZAUpO5F1PdPXYx8PuWrOihVBjNPwMslJpcqJbtpxssGBKv7Se4f2d5-OWJw==)
9. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRJWAzLXwKjE_bzCO2X515z1HuYhwxvhRJDPZx1SZR2gZ24G34i1TWS2eHEYuXfQ13V8OiksodZvczmLpZCy-ubT-yFEfeLBpGZNUoCKXbgkBDEXAPtyJUU54orvOT)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRj9Oxr9EzWofcOzPO-mBC2MdFCG_I9zztf0SUmr_6jlPv7LcT676k9Mumoed9VfcMjk3WYWaGml16ztobyjla22hf5jDn2ROC3NkFJN5QQKCNzTkyEhSBmRb)
11. [eralberta.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKfj-53opt1x54MaETyq7BAsPLdyjmpxVTd-ArBMwSuJH675cUzHa37g6hgR3DceBhMwg6J82I9Bngo41Cyqa-KskRlhBC7mGergT-HvpaUPQ2kKTnmF-M1F_AYvNw2fHRCuVNE4qHMcCu6wSCur9Q2MqKuPBpPzIAU75OnU88IfbjdWJ1TeCG5Qf3_H_9epySn59L_Ul2VRkOfCxHrMX9FS0=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeqkdHAH4_2aLb4ine-YajGJ-JNp9rkwZIyk062FssFaxNFZx0f7D33rSrHH5T2IqLAerp2HO9-n_xkdhPoZLC8bE0INPSoBzaKI8J7312uEuMLx7DOtQoWliupxc3X8IUUodiGSHe84_RRGyXk86QqKD7kaM9bvJyuQbY1SvfYxUnDkd6QaJkf0edygXQy6jUJmtJP4IPeaEGXNVVwtUyOB6cqcTgHSqwPLUCdw-dtu6X7MaTtR3Yl39XoUZzLFkMcToIWLE7Kc1wXI2FVthsz_4JjALNkr8n9mrK_MIOhpvLDeFH)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1RU0xpcEXHMzNHf6oPxErz5CbeFXSm8yM_xMg4JKH5Z-Cx4b3kNiaVm8GBhkSoEFQyPrxza3Rfj8_ARjcHkGKQkJOtI8xPc5SwtMMTdQAroLy5f7NHFm-rQ==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb4nwxdyq2a_1RPc_Y3kgi4tPItCdykHDQTEUIK0GHQdV3aERJazrIBrdXY3WJrUiHi2Yqn-0L45-YWq87lbcjUdVvd47_GhgKAlGjPNXdNy1nFotFtR2gkQcbMSdlRMNPcZsM6LSW3qkVQEMOmV4uqE_Sx-97TX-b3Y-U9tZIpuP0-0UahJztW4jAEGaYrrgtTeKYsj7HFL9PKG2Q0S4B1RD6muLN23j6LKHM__G4LcWQ64-oAAdWHXdAwxEn)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoid7MFUUe9aWv2W7LdslAp7tieAjmbdRP7rkJJusbPH-BtMR2d4wwWSEe-gmuWQrL_yzLvBxTlW9YdhtvrirlIfBXKLvJi5vpcW5uZF89behPfGc9QjGS9mjRv-BCHVrE3AMYZKgW2zQ2H_9UDfvnOMd1hAXI-q5OJ-9doMw1mOq4vpeTpqxmpSExOKpOV0e-z8kQbdOHGcYKvFzSMfiJz65kMssY_k7Z)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9I_HZdon35o2EUrzQFLsz3AxA4ZjN_Z-6hcRoA4lLL9NYFlXmDgQxQAOoSvgLLC85zaGnjCWNMHxNJe424_EoFiODrj3d0_ezaH7mNYKutMwYr_9CyFGjukmw3NihoLpodu7UNXWkfXS2yPVCdXOSjn0t8MBr8_tyDGkruoP5U7MH6wXB9NHoUN3-10Y0AU3NiWKM1z_MRW5co4BTfQ7IjIbXDaBXnRTmjJqHSLQPMCyDaKgSUESnNrX95y9T-_GoreQdjUmDxy6n0Vm9ioKOyBuZeJOulvGZnjYXgjagTho=)
17. [merrick.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8zHw5K-PQEkHUsB9dVgzZ4Dp9trM6OJZXxqew1-xuD-MpRQlJKJAJG2uEZhB6gXTBuAr9UT5QbrSJiDmrFPvt4JsbmKceKRaNoHERwoBLxGlocl0uF2e0kHSCw-YtwCeRz6Se-uQiMQ59isH_Xb0tSlIJlWWXNr2ET1o6iDVOCjzQHZdHxHW3UD3QEgY=)
18. [pnnl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQQRk7G17vymE15IA8cMMyf0_v97aSjGVp5WEnSRgirVnuMec_S46es-8-gclNUsaTbjkbbLBZrb3qZYaijfLOPjXfwDt-IVqUQzlKkhmlrdKwqtvWzgAAWbY5e9m4qlppud3ZgGNN6PjD_5G4mfqGYeJrH2HqrPWsq9_zV06Zga4Tty6e)
19. [steeperenergy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERTF7Sp1TDDaVH-rKUvPIo9buY9qMTVdn4rJ1K801bMoyO1rTEiH9BKq9EM8sb4X1dzJQlN4VxM2_hN0COdP2F7p9-iNwqeriI0iwLroMR1Htu3pSQFkDtHR08R91l8YpuoWH-QEjCCyse-11jb4ij)
20. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFi4kPgbBgpwrpc0F2XIFdjqic9d3Rk-v3I5P5yS3zgxrblYNUOcmtyil-LdwOlvrrbriTHrHCEOq_bJig0oPsaK1MCMS_4Hi6o3HVRgOf-p1mAXs5DUUNrc4Y_Vqm39zY=)
21. [genifuel.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJd39S7DT4vuNd-jU_cgfy_ggpqd6JtbN1-JbWhivyVn2suEbRfexPy0e7K9FE961H1R8Ee5fgvBa6YAE_bvLMeegB6egCqiUnD5HeGAI9D6E5qWcpdQ==)
22. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWIRSCu_LC4aVU3ay9wdIjdbLm1CULGKejyCP_L64iHUYfbn4DZT2OE25TsrmRB8NcqZC0Vd0oWmttgj68jnWfq7UggPQZ5PK-UomSh1V_3pJWKBo0ivxHvz3jBaq_hi0=)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlZdqwDlvy9pIgIAepZCwSO-_M3uSq9Fx7TCJx4LXZyf6kx24dVf8fuUQnik-0Dv_gg8e_8IKHaCvclHPamZNhCeTvNqemLbOkxRsUUJ9wVmw3_Kl5zCME7ndaDnA1)
24. [encyclopedia.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7q-ss47WAmq9X4wIuuhFYoO_aJFRPodrmZ3861IOUdAhK-evAdTenLJlYYsEtAJA75mnuKKV0IdbALWxvyjaA_J74IPt3wtKM7SctYpndAuVaJS8hs2iB8A==)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmEIQ1XafjCzvYbfRhIQrvIIc0zBmUM3Z8uwYPEp6zP1HWkxh5v79B1n7XKaTVxVKocSPXv-h_mLt3vlPNlGiD3KF7IYQKsHtyHpztdrwTe8QqTUzQm3rLFsFftQ==)
26. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2iOHO17NWJwbjKNpMTjoyFKxY1k5lJU9YFRj8thyBTTD-gliw80ijnyXfES0vp3QV5JUm6-KMda3tHouiv27_FGmGV4wwUAW7ngG_bmtcZM9GFZo6nu7g_V_3opVwpA==)
27. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw-JcJPEuiohy_iN1eQnDPNjgk4GhiOnFn1-U9vXTctqPYLqy19qm7K28q2nikGvfkgnIk4jWd9x9S76KDTQZK6norc6bR4g8fb6bbp-61fvhsN78xhq8ls32lYOVMQ4fJEqgvhnM=)
28. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUTqVBI6zSgyVsoseUgVpkaaD_tz6HEB00C65VPDMQmjnSPt4VfmTkDBAVLBSyBQaeDNmeLpqAxUupjERHE7GtMR6m2VJcvgLpl9ppB-Rp9O_mBQWYgtC5fNSLk1NfzNj3WPWVfvDKaL8ilxkxUgM=)
29. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHL2SEakH_i-Un7zLHyraJK-GHVf-YIAAvkmeFpgq5Lr4w3ax5K2-JIx4Os_hF1y5S7LO0YuEw12uS6gu7rio8zLbbUflxtGI_BiPmzKzihQbfZ3YiVpEzOZAt)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyjmtG669vKykjmCerLK5QUu4RV6bpuZ8C0ngrdXXrQ8JD78-2-f-DT0Ik7m4vPpsB6R2QWs7md-adxpFz8JN0WCV5hXfe1Dr4rq_0GXvjeErR3teamzEoNS0f_Ae6imf3b4G61ylHcTzk-IuWnTC5Ui7zo3ykHc3A7H93Z9i8699snmbjlrgfv8S7-F8p7BSx2o-2sLvDp-1bOcufMMy5Y6OrfZPqBrFCwhMRBBNIt1xBjqupgiQLpugwPWxZx9IKEvZLCMRMC_OvUKZE3lcrAH9Is1qq2w==)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpSVRNEGeuk3v0gcfywZyBSMnrp-eY9JfGMfWN_RzRZvGCAvDYJp7FqE6EIGz3VMVYsl4kYWfgBYj4QPydJTvNq9QTCNe1F8_uNNC6uYYBpFzwQkIXpptHZWq49r2TyfFkb60UmvEiOWUcOBafdILXkrWu4brS87whyD3CqM3XITbaA6CydL5wFeOk3y1N8lxFnxc3O95Hcw2x_69dcfje2mfce_hmN1pQcPiLP4lZKJ9Z5kd3y0YuSPzraCs7te7dxyxrxZrEet1WWpAI)
32. [au.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCJPVJi7bPmS_UIsCmCzZ_0UfDIhU6Y97a0l7V7CVdl4giEsVVWSimyQ4HJyslW7dlywOvu8z-1BRUzzP5_UuFbcaRCwREduEeU94q0p6DWXlmz4MYpUalwYT723A85HeOrtIlr_H9oeTCzxvJhjlrC8pTz8Ah2I0kB-5Rp6pgdXWVmeNtnze_9HMnR2IKgGCIs1XtBWttlrduzSdbA-237A==)
33. [au.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfDZApbv9OTQylxIXv4HtXTWqA7ezlVVeYRJGrS6HKqsG8UzfjzisqSOLF5y-8Om5octACGQseQ1gTfPLqm2m_X4DHcg1oOYW1k3CgsZCLfoID2nlXXnlR1ZSYo2FtaH5IckJ8Ad-mEscWdcr3ZYDrJQMdTiair8VJGdjfvMI7BJT5c09LpHh3O3-gzeCKWcjfkz3emSy6YYcsaSzL-wDJ)
34. [eralberta.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAEdjYQq1hHxDGpy_wPAwl8cg5JMNUHOZE7cATwlt1uPce0mcoyzexgP2e2qLrtwJ2byP5fWZF-SS_YCwqnd0PeWwT6fpYYjqZ6WVDIzDt2ZbN0YzBYJIr-RRil5_2f6Ho0lOxd9_XSVvqIq-WobYhm2F9DBVMGU2ZCS_xEpv7qkcQxHfb5pBDGvyFdHbpqvyu6AM=)
35. [bioenergy-news.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiFx19mPlL6vAgcbzslbckSJpYVCJdj575aeGWRH6hreip8TektYuq8e6ccqgd3cX4J9EcvsK4itzzCfN-GCImu89p_gX1SAChNAmMFX5fp6TuAB3tiiIh-WV6GhGlvpdH2wnIsFgS9IzQdNEYdN2BCDMjLFtjv7sTgROI2f57OdvwfQVmeSmKyELgkEtmFOIm639pIDNKslNDuFaS5DH1)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9cymTMHErFzmtPYfRCbJQzj_FuDKN3jL6rM9XEobUAqZ4Ll7EVEXo5C7e6GDOJrEjm6ToYnsQdXk_A0ztDxiCZ4-cNPg0lj-vasLWr_pvIRUwVss-N5iPi86TqK8WvTZ1WYeoxtHQTP94Wv2IAsPe48OYIrEhIHpLJBc81zF_IQ4Zp_bhuT4eVMf_gglj04P5foX3pBOx32SaSZXy4dp7-S1zVFkgx00WlO0VbDMDf_pCzaoAA7zXeI6PdiM2uOnpWSOoPbeySiw_S5GCvLN2a9BzXHnhissCOSJC)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQOHD0v-uP5DRxrglhpOdMTHdB-cNqWISL3_bpFhz5WPrHvZWanM2nzAKqDJdEKhzwnXk8i96CjErK2rFLTc5DWm7-Hrfu8Lx1VUOFp1cEauePZPU9lnHYQqlJgN9LZn80cZKeJbS10LyDxH9-fuJcU1X0ImMVdM1dr63rReKrfVAaCWexZbp0nkM0yzZ99Yl5nFz99Ecy0yfHp_gNwPrQruzhtbRpbWB9e9B7xF5P8J0wgnC2Lmo-Twouosz8hatI-AcNiig=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2lHLbUEF0BQk4cnoWyBpcmEtf5N5cGpNexIn67EDiHNjeVFNygPU17V6vUjabWCmue2AVgMqKAUkymj6xMKxbHu9FzEaemS33iPJvQGFEhs1qpdRCwnasZn5pCaSsEoTRy1AWN0V6aes8aXC5jvbF8k4Sw-gKqPA2LdjMPu-VQsgf7W8oN6Ym5aQevbmhnmskaQwEjk-NzQy_9xlCnvLJsyEYfTyd_b4DV5vpm0k_9J4PsoTZ4L_K3gViP9y--ZuNXqM-KF-B_9W3hW0nZAOdtCw3Vmtws0J7dSynpUA=)
39. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIjTe4IkK8xEIf0stlLLA5ZnrhujsTOMOdbTMuyl2jrCVQEcEOXpxr8hNdVHkMYJt3sYbECjV0P24UHJDLG1PHIlSWXNDVMPUaWIMYWR92gCJ9NetOaTwmprcgXqNw_BDyq9M3G3WsOlwqWZhcG8EqP88Q-uRE)
40. [ieabioenergy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUS9ZI4nR9YLlmNLp7Xh1qKWSca8QgdXGnqzrc7XDAaWSZt8Y3ckecSPJKSzxtOsxXgVFX87_byBKMo7-T9E3fgUOKoXE7JeGmrbJjT2C555COdDGxj3E6g748QjoVU_sbObUkfBa1RgG41M2Em-q20F8uOJFB9J-6qnpLq9-JbDn0lujtL_JZ3wSBqYB0xgDeL94bOK3Ne3M2z5N58FNfvI6Ib8_ONPNKryh0r-NhNMPh96WUB01umJaTw-R1tw==)
41. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrhdETnwA1IGnRQ4SvXMOoGp0PogtjDMhi0-S0L1Erj_3ryjAR4Yaf_AZBUqbJ6UZwfnyZbEWrcCSX5r7RkzqHF0b366toLi_GfQ1xzdQ3mOBzLeY0jxTxf3ccvgrizZDGCik=)
42. [pnnl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfnwKwLE0IwD6INSu5I61zS4F-k_i1VHUBo-VOrKlSJlEIGFGmHPJwwiN4gaV0VrnA7CDsFVisjyjlWa0fdUWlKp8AO--za_HhVsv282q93BwVjK-u2haAkqRuUZKBs5Vu5MJWrp0IRJezOLnrgKqp2Xo8RGGlrbURVWr5epO4o7iPfg8E)
43. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJw2mylj3ALtrcSgOgroutZ10UCM7X5MzptTtm8F-ue_Sfwdc_zOCeYfUoI4ZjrBK65R-8zf7a5LmmjjBZIr3n0lRJ5pDaeo4vZpaAVeasUfwQKSpTNyf7qc3vBQgaCdMIe8h2XiWYP33HoTaDyyBGJFnWoB4IFjLS3Fct5m9i0PGTJWFcT0x4mDCsF_Sws1Ii1XF9fqHNHzQC)
44. [uwo.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLlY-LhZryZcIZzF1H_LrnMY0TDyJkeqPZMw_EBu47DqjyZEhBu597j_jG9YAbGzoKvvS_p44ODUwaTKbs8uHCz5u0447EkyY29tKsaIwA8fsopxJIPciQ9gDOM59o0SUwUOBX6W7hymnjiatM7uV9n7jeVzJ8e2Q=)
45. [globalgrowthinsights.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3sI1NiNXCWSGTz7eZFFcW_LRzLX1E4Sj1BlOG2tNzlR8rPDsSGbt7Z12-agZT64Es68f0jGQs4yQZ4n_q4xrJxT-fquSe41MACuepwvUi5CYrsdpvJ4yr7fuir24nsuwfyfTpPxlay_U6Re7GwjPas-oA8gPIbgAtpabk0oJhsuqmFS1f2mHC4kfuFhiu)
46. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTSBomiPxgIkCGn0OyqGcZWiV32pKfOGRvuBsS0r36gMmhdmfA4LzLf2cIn_zC1kERSUbrsDCYi29pQX6tbdd8d1PxZBMtXMZJCsaS6Fm2GsBMs2j9LYBG_MnIpYrX5eu5clWYr5TZ9QIgmMLo-QFFZykfhbTYHGasd9w=)
47. [platformduurzamebiobrandstoffen.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxkPTyaf0ChspoKP8sjIUATgI6hjv0z3fAblgVVyMkWuaHPYhRnCutwRHg9r5yj7MvmgKjyl5i7mrswF5CqJXMlpgtvwBUF6ADr4Ij2HvTwFnQal5sYeJZ6v38gF3hRjXltXjp1-fb-VbrDILWH7bFJtErSZjFG4uz9F26GlXMTxQjse1GWc8sh3ijrb8a1aKIodf_fR0k8-MkSzccKRIAwdODNp6tP2xg3-g4A4CauQ==)
