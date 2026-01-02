# Literature Review: Computer vision technologies for safety science and management in construction- A critical review and future research directions.

*Generated on: 2025-12-26 22:42:45*
*Progress: [40/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Computer_vision_technologies_for_safety_science_and_manageme_20251226_224245.md*
---

# Computer Vision Technologies for Safety Science and Management in Construction: A Critical Review and Future Research Directions

**Key Points:**
*   **Paradigm Shift:** The construction industry is transitioning from reactive manual safety monitoring to proactive, real-time automated surveillance using Computer Vision (CV).
*   **Technological Evolution:** The field has moved from basic image processing to Deep Learning (CNNs) and is currently integrating Vision Transformers (ViT) and Generative AI.
*   **Core Applications:** Primary use cases include Personal Protective Equipment (PPE) detection, hazard recognition (e.g., the "Fatal Four"), and worker behavior analysis.
*   **Integration:** Cutting-edge research focuses on integrating CV with Building Information Modeling (BIM) and Digital Twins for holistic safety management.
*   **Future Frontier:** The next generation of research aims to solve data scarcity through synthetic data generation and move from detection (Level 1) to predictive safety science (Level 3).

---

## Abstract

The construction industry remains one of the most hazardous sectors globally, characterized by dynamic environments and high accident rates. Traditional safety management, reliant on manual inspection and retrospective reporting, often fails to prevent incidents in real-time. This paper presents a comprehensive systematic literature review of computer vision (CV) technologies applied to construction safety science and management. We analyze the evolution of the field from early image processing to state-of-the-art Deep Learning architectures, including YOLOv8 and Vision Transformers (ViT). The review categorizes existing literature into three developmental levels: detection, assessment, and prediction. While significant maturity has been achieved in object detection (e.g., PPE compliance), the field faces challenges regarding data scarcity, occlusion, and integration with safety management systems. We critically examine the emergence of Generative AI for synthetic data creation and the integration of CV with Building Information Modeling (BIM). Finally, we propose a roadmap for future research, emphasizing the need for predictive models that incorporate safety culture and behavioral psychology.

## 1. Introduction

The construction industry is a cornerstone of global economic development but is plagued by a disproportionately high rate of occupational injuries and fatalities. In the United States alone, construction accounted for 20% of all work-related fatalities in 2024, with the "Fatal Four"—falls, struck-by incidents, electrocutions, and caught-between incidents—comprising over 60% of these deaths [cite: 1, 2]. Traditional safety management systems (SMS) rely heavily on manual observations, checklists, and post-accident investigations. These methods are inherently labor-intensive, prone to human error, and reactive rather than proactive [cite: 1, 3].

The advent of Industry 4.0 has introduced digital technologies to mitigate these risks. Among these, Computer Vision (CV)—a field of Artificial Intelligence (AI) that enables computers to interpret visual data—has emerged as a transformative tool for safety science. By leveraging cameras and deep learning algorithms, CV systems can provide continuous, non-intrusive monitoring of construction sites, identifying hazards that human supervisors might miss [cite: 4, 5].

This paper provides a critical review of CV in construction safety, motivated by the rapid technological advancements seen in 2024 and 2025, particularly the rise of Vision Transformers and Generative AI. The objective is to synthesize current state-of-the-art methods, evaluate their alignment with theoretical safety science, and identify gaps preventing widespread industry adoption.

## 2. Key Concepts and Definitions

### 2.1 Computer Vision in Construction
Computer Vision involves the automated extraction, analysis, and understanding of useful information from a single image or a sequence of images. In the context of construction, CV is utilized to replicate and augment the visual capabilities of safety managers. It involves three primary tasks:
*   **Object Detection:** Identifying and locating instances of objects (e.g., workers, helmets, excavators) within an image [cite: 6].
*   **Object Tracking:** Monitoring the movement of objects across video frames to analyze trajectories and interactions [cite: 7, 8].
*   **Action Recognition:** Classifying the behavior or activity of workers (e.g., walking, falling, welding) [cite: 9].

### 2.2 Safety Science Frameworks
To be effective, CV technologies must be grounded in safety science theories:
*   **Hierarchy of Controls:** CV primarily supports administrative controls (monitoring) and engineering controls (barriers/alerts).
*   **Behavior-Based Safety (BBS):** A proactive approach that focuses on identifying and changing unsafe behaviors. CV automates BBS by detecting unsafe acts (e.g., not wearing PPE) without the need for constant human supervision [cite: 10, 11].
*   **Swiss Cheese Model:** CV acts as an additional layer of defense, plugging "holes" in safety protocols by providing real-time alerts for hazard precursors.

## 3. Historical Development and Milestones

The application of CV in construction safety has evolved through distinct phases, often categorized by the sophistication of the underlying algorithms.

### 3.1 Early Approaches (Pre-2012)
Initial research relied on traditional image processing techniques. These methods used hand-crafted features (e.g., edge detection, color histograms) to identify objects. While pioneering, these systems lacked robustness against the complex lighting and clutter typical of construction sites [cite: 12].

### 3.2 The Deep Learning Revolution (2012–2020)
The introduction of Convolutional Neural Networks (CNNs) marked a paradigm shift. Algorithms such as R-CNN and early YOLO (You Only Look Once) versions allowed for high-accuracy object detection. Research during this period focused heavily on Level 1 applications: detecting workers and equipment to prevent struck-by accidents [cite: 7, 8].

### 3.3 The Era of Transformers and Generative AI (2021–Present)
Recent years have seen the adoption of Vision Transformers (ViT), which utilize self-attention mechanisms to understand global context better than CNNs [cite: 9, 13]. Furthermore, 2024-2025 has witnessed the integration of Generative AI to create synthetic datasets, addressing the chronic lack of labeled training data in construction [cite: 14, 15].

### 3.4 The Three-Level Framework
Guo et al. (2021) proposed a seminal framework for categorizing CV development in construction safety, which remains relevant:
1.  **Level 1 (L1): Detection, Recognition, and Tracking:** The foundational layer, focusing on "what is where" [cite: 8].
2.  **Level 2 (L2): Assessment:** Interpreting the visual data to assess risk (e.g., determining if a worker is too close to an edge) [cite: 8].
3.  **Level 3 (L3): Prediction:** Forecasting potential accidents before they occur based on behavioral precursors [cite: 8].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Advanced Object Detection Architectures
The **YOLO (You Only Look Once)** family of models remains the industry standard for real-time detection due to its balance of speed and accuracy.
*   **YOLOv8 and YOLOv11:** Recent studies in 2024 and 2025 highlight YOLOv8's dominance in PPE detection. It features enhanced feature extraction capabilities, allowing for the detection of small objects (e.g., safety gloves, chin straps) in cluttered environments [cite: 6, 16, 17].
*   **Performance:** Custom YOLOv8 models have achieved Mean Average Precision (mAP) scores exceeding 95% for PPE compliance tasks [cite: 17, 18].

### 4.2 Vision Transformers (ViT)
While CNNs process images in local patches, **Vision Transformers** process images as sequences of patches, allowing the model to capture long-range dependencies.
*   **Application:** ViTs are proving superior in complex scene understanding, such as identifying worker activities in mobile work zones or detecting subtle cracks in infrastructure [cite: 9, 13].
*   **Hybrid Models:** Researchers are increasingly combining CNNs (for local features) with Transformers (for global context) to improve robustness in dynamic construction environments [cite: 19].

### 4.3 Synthetic Data and Generative AI
A critical bottleneck in CV is the need for massive, annotated datasets. **Generative AI** is now being used to synthesize training data.
*   **Synthetic Datasets:** Tools like "Segment Anything Models" (SAM) and generative adversarial networks (GANs) create realistic images of hazardous scenarios that are rare in real-world data (e.g., specific accident types). This allows models to be trained on "long-tail" events without exposing workers to risk [cite: 2, 14, 15].
*   **Impact:** Models trained on a mix of real and synthetic data have shown performance improvements of over 10% in specific detection tasks [cite: 15].

## 5. Applications and Case Studies

### 5.1 Personal Protective Equipment (PPE) Compliance
The most mature application of CV is PPE detection. Systems are deployed to verify the usage of hard hats, high-visibility vests, safety glasses, and harnesses.
*   **Case Study:** A 2025 study utilized YOLOv8 to detect multiple PPE classes (helmets, vests, masks) on a standard laptop, achieving 92% precision. This demonstrates the feasibility of deploying low-cost, edge-computing solutions on-site [cite: 6, 20].
*   **Granularity:** Modern systems can distinguish between "wearing a helmet" and "wearing a helmet incorrectly" (e.g., unbuckled), a crucial distinction for safety compliance [cite: 21].

### 5.2 Hazard Recognition and Geofencing
CV systems are used to create "virtual fences" around hazardous areas (e.g., excavation pits, swing radiuses of cranes).
*   **Proximity Detection:** Algorithms calculate the distance between workers and heavy machinery in real-time. If a worker breaches a defined safety zone, the system triggers an alarm [cite: 1, 22].
*   **Fall Prevention:** Cameras monitor leading edges and scaffolding. If a worker is detected near an edge without a harness, an alert is generated. This addresses the leading cause of construction fatalities [cite: 2, 23].

### 5.3 Behavior-Based Safety and Ergonomics
Beyond static compliance, CV is increasingly used to analyze worker dynamics.
*   **Ergonomic Analysis:** Pose estimation algorithms track worker skeletons to identify awkward postures that lead to musculoskeletal disorders (MSDs).
*   **Unsafe Act Detection:** Systems can identify specific unsafe behaviors, such as smoking in restricted areas, using mobile phones while operating machinery, or running on site [cite: 19, 24].

### 5.4 Integration with BIM and Digital Twins
Integrating CV with **Building Information Modeling (BIM)** creates a dynamic Digital Twin of the construction site.
*   **4D Safety Monitoring:** By mapping real-time CV data onto the 4D BIM model (3D + time), managers can compare the "as-planned" safety measures with "as-built" reality. This integration allows for automated hazard identification based on the project schedule [cite: 25, 26].
*   **IFC Standards:** Recent efforts focus on standardizing this data exchange using Industry Foundation Classes (IFC) to ensure interoperability between CV systems and BIM software [cite: 27, 28].

## 6. Challenges and Open Problems

Despite the technological progress, several barriers hinder the ubiquitous adoption of CV in construction.

### 6.1 Data Scarcity and Quality
Construction sites are visually chaotic. Changes in lighting (day vs. night), weather (rain, fog), and occlusion (objects blocking the camera view) significantly degrade model performance [cite: 12, 29]. Furthermore, there is a lack of large-scale, public datasets specifically for construction safety, unlike the general-purpose COCO or ImageNet datasets [cite: 14, 30].

### 6.2 Computational Constraints
High-accuracy models like ViTs are computationally expensive. Processing video feeds from dozens of cameras in real-time requires significant GPU power.
*   **Edge vs. Cloud:** Transmitting data to the cloud introduces latency, which is unacceptable for immediate safety alerts. Edge computing (processing data on the camera or a local server) is preferred but limited by hardware capabilities [cite: 31].

### 6.3 Privacy and Ethical Concerns
Continuous surveillance raises privacy issues for workers. There is a risk that safety monitoring tools could be repurposed for productivity tracking or punitive measures, leading to resistance from the workforce [cite: 12, 32].

### 6.4 The "Black Box" Problem
Deep learning models, particularly deep CNNs and Transformers, lack interpretability. It is often difficult to understand *why* a model classified a situation as safe or unsafe. In safety science, explainability is crucial for trust and for designing corrective actions [cite: 33].

## 7. Future Research Directions

Based on the critical review and identified gaps, the following directions are proposed for future research:

### 7.1 Generative AI for Data Augmentation
Future research should extensively leverage Generative AI to create "Digital Twins" of accident scenarios. By generating synthetic images of rare but catastrophic events (e.g., trench collapses), researchers can train robust models without relying on sparse real-world accident data [cite: 14, 15, 34].

### 7.2 Vision-Language Models (VLMs)
Moving beyond simple detection, the integration of Natural Language Processing (NLP) with CV (Vision-Language Models) offers immense potential.
*   **Semantic Understanding:** Instead of just detecting a "person" and a "crane," a VLM can answer queries like "Is the worker standing in the crane's blind spot?" or "Describe the safety violation in this zone." This aligns with Level 2 (Assessment) and Level 3 (Prediction) capabilities [cite: 21, 35].

### 7.3 From Detection to Prediction (Level 3)
Research must pivot from detecting hazards to predicting them. By analyzing temporal patterns in worker behavior (e.g., increasing fatigue, rushing), CV systems should forecast the probability of an accident occurring in the next hour or shift. This requires integrating CV data with other sensors (IoT) and historical accident records [cite: 3, 8].

### 7.4 Holistic Safety Management Integration
CV should not exist in a vacuum. Future systems must integrate with the broader Safety Management System (SMS).
*   **Automated Reporting:** CV systems should automatically populate safety logs and incident reports, reducing administrative burden.
*   **Safety Culture:** Research is needed to quantify the impact of CV monitoring on safety climate—does it improve compliance, or does it create a culture of fear? [cite: 7, 11].

## 8. Conclusion

Computer vision technologies have reached a pivotal moment in construction safety management. The transition from experimental prototypes to robust, commercially viable solutions is well underway, driven by advancements in YOLO architectures, Vision Transformers, and edge computing. The ability to detect PPE compliance and recognize "Fatal Four" hazards in real-time represents a significant leap forward from traditional manual monitoring.

However, the field is currently plateauing at the level of "detection." To truly revolutionize safety science, the next generation of research must embrace "prediction" and "prevention." This will require the convergence of CV with Generative AI for data synthesis, BIM for spatial context, and behavioral science for understanding the human factors of safety. By addressing the challenges of data quality, interpretability, and privacy, computer vision can become not just a monitoring tool, but a proactive partner in ensuring that every construction worker returns home safely.

## References

[cite: 4] VisoSafe. (n.d.). Revolutionizing Construction Site Management: AI and Computer Vision Innovations. [cite: 4]
[cite: 1] Detect Technologies. (2024). How AI and Machine Vision are Revolutionizing Construction Safety. [cite: 1]
[cite: 36] Kim, D., et al. (2023). A new neural network model for safety management... *PMC*. [cite: 36]
[cite: 16] MDPI. (2024). Evaluation of State-of-the-Art YOLO Models for Safety Hard Hat Detection. [cite: 16]
[cite: 22] Murari, H. (2024). Building Safer Construction Sites: The Role of Vision AI. *Medium*. [cite: 22]
[cite: 7] Li, H., et al. (2018). A review of the applications of computer vision to construction health and safety. [cite: 7]
[cite: 10] Guo, B. H. W., et al. (2021). The potential of computer vision technologies for safety science... *MDPI*. [cite: 10]
[cite: 8] Guo, B. H. W., Zou, Y., Fang, Y., Goh, Y. M., & Zou, P. X. W. (2021). Computer vision technologies for safety science and management in construction: A critical review and future research directions. *Safety Science*, 135, 105130. [cite: 3, 8, 10, 11]
[cite: 3] Guo, B. H. W. (2021). Computer vision technologies for safety science... *ResearchGate*. [cite: 3]
[cite: 37] Guo, B., et al. (2025). Integrated approach for near-miss accident identification. *ASCE Library*. [cite: 37]
[cite: 24] MDPI. (2021). Computer Vision Technology for Monitoring Worker Behavior. [cite: 24]
[cite: 38] World Construction Today. (n.d.). Computer Vision to Change the Outlook of Construction Activities. [cite: 38]
[cite: 39] ResearchGate. (2024). Computer Vision for Safety Management: A Case Study. [cite: 39]
[cite: 29] Costa, M. D. D., et al. (2025). The Impacts of computer vision technology in construction: investigating applications and challenges. [cite: 29]
[cite: 40] CIOB. (2024). The application of Computer Vision (CV) is transforming many industrial sectors. [cite: 40]
[cite: 25] Li, et al. (2024). Framework integrating computer vision, ontology, and NLP. *MDPI*. [cite: 25]
[cite: 5] SciSpace. (2023). Computer vision and IoT research landscape for health and safety. [cite: 5]
[cite: 41] Emerald Insight. (2024). An advanced exploration of technological advancements... [cite: 41]
[cite: 33] MDPI. (2025). Systematic analysis of AI in construction safety management. [cite: 33]
[cite: 26] VJOL. (n.d.). Integrating computer vision-based detection with the BIM model. [cite: 26]
[cite: 27] MDPI. (2024). Cloud-based system integrating IFC standard with BIM. [cite: 27]
[cite: 42] MDPI. (2025). Integrated BIM-AI platform for sustainable construction safety. [cite: 42]
[cite: 43] Infotech. (n.d.). The Structure of BIM: Understanding IFC Standards. [cite: 43]
[cite: 28] IAARC. (2025). Estimating and managing construction site safety costs using IFC. [cite: 28]
[cite: 21] ArXiv. (2024). Vision transformer-based safety hazard detection. [cite: 21]
[cite: 9] ASCE Library. (2024). Detecting construction workers' activities using Vision Transformer (ViT). [cite: 9]
[cite: 2] Ionio. (2024). How we built an AI pipeline to reduce hazards... [cite: 2]
[cite: 44] MDPI. (2025). VisualSiteDiary: Vision Transformer-based image captioning. [cite: 44]
[cite: 19] MDPI. (2025). Real-time behavior recognition network based on Transformer. [cite: 19]
[cite: 14] ObraLink. (2025). Generative AI and Synthetic Data in Construction. [cite: 14]
[cite: 15] MDPI. (2025). AIGC-HWD: Helmet detection dataset using generative AI. [cite: 15]
[cite: 45] Medium. (2025). Synthetic Data and Generative AI. [cite: 45]
[cite: 30] ResearchGate. (2023). Synthetic Image Dataset Development. [cite: 30]
[cite: 46] RandomTrees. (2024). Synthetic Data with Generative AI for Computer Vision. [cite: 46]
[cite: 6] SciSpace. (2024). YOLOv8 utilization in occupational health and safety. [cite: 6]
[cite: 17] EC3. (2024). Enhancing Construction Site Safety Using AI: Custom YOLOv8 Model. [cite: 17]
[cite: 20] IJISRT. (2025). Automated PPE Detection Using YOLOv8. [cite: 20]
[cite: 18] ResearchGate. (2024). Enhancing Construction Site Safety Using AI (YOLOv8). [cite: 18]
[cite: 47] IJRASET. (2025). Enhancing Construction Worker Safety Through YOLOv8. [cite: 47]
[cite: 39] ResearchGate. (2024). Computer Vision for Safety Management: A Case Study. [cite: 39]
[cite: 48] Motive. (2024). Computer Vision Transforms Construction. [cite: 48]
[cite: 23] ABC Carolinas. (2025). AI in Construction Site Safety. [cite: 23]
[cite: 49] IEEE Access. (2024). Review of Computer Vision-Based Monitoring Approaches. [cite: 49]
[cite: 12] ResearchGate. (2025). Computer vision techniques for construction safety and health monitoring. [cite: 12]
[cite: 47] IJRASET. (2025). YOLOv8 PPE Detection Accuracy. [cite: 47]
[cite: 31] ASCE Library. (2024). Enhanced YOLOv8 for real-time PPE monitoring. [cite: 31]
[cite: 50] VBN. (2024). YOLOv8 construction safety PPE detection. [cite: 50]
[cite: 51] ResearchGate. (2024). A YOLOv8 Approach for PPE Detection. [cite: 51]
[cite: 20] IJISRT. (2025). Automated PPE Detection Using YOLOv8. [cite: 20]
[cite: 14] ObraLink. (2025). Generative AI synthetic data construction safety. [cite: 14]
[cite: 52] Evotix. (2024). Revolutionizing Construction Safety: The Power of Generative AI. [cite: 52]
[cite: 34] ActiveFence. (2025). The Role of Organic and Synthetic Data in AI Safety. [cite: 34]
[cite: 35] NYU Tandon. (2025). How generative AI could help make construction sites safer. [cite: 35]
[cite: 32] Tenna. (2025). AI in Construction Safety Management. [cite: 32]
[cite: 13] ResearchGate. (2024). Fine-Tuning Vision Transformer (ViT) to Classify Activities. [cite: 13]
[cite: 9] ASCE Library. (2024). Vision Transformers construction safety applications. [cite: 9]
[cite: 53] MDPI. (2022). Vision Transformer-Traffic Accident (ViT-TA). [cite: 53]
[cite: 54] Viso.ai. (n.d.). Vision Transformer (ViT) in Image Recognition. [cite: 54]
[cite: 55] MDPI. (2022). Vision Transformers for industrial visual inspection. [cite: 55]
[cite: 10] MDPI. (2021). Computer vision technologies for safety science... [cite: 10]
[cite: 56] SciSpace. (2021). Computer vision technologies for safety science... [cite: 56]
[cite: 8] NSC Polteksby. (2021). Safety Science - Volume 135. [cite: 8]
[cite: 11] Monash University. (2021). Computer vision technologies for safety science... [cite: 11]
[cite: 3] ResearchGate. (2021). Computer vision technologies for safety science... [cite: 3]

**Sources:**
1. [detecttechnologies.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKyEwg9Mm1Nttg5VOJtHKgW-m-wFaouhmtbZgK4nH2LFooYhlETK2lJ4W7razjLelm043tdPnyMWlOhQ2sgI0xcy899fDbJsIp9SW4xywl9bo-HYYPsw4t5fdtpIxqYu7GI4bu2zaGgAHpc16NWza12ZzKCZ1MarQ-Psi7FyOH7QPE5AEgSe49EbaWEpoZvqFkJT-WYa4=)
2. [ionio.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnrCC_sCRQZN7esJ9mkSE7H9OVpBqIA9qVABZM_YhD9iBlUbNaSluIHG-XH74LVVQt_O2zhj83ZtHQn0m2J9FuJMuPdzoEdhyAk_YU1S_h6pkLoBpa_sr_2cfxl0a4Ub0pS6f02asS0vxBRNXtNjPBNcqeivnkRLH9H_lZLH6I2rdyJVJKq42bAVF_gPi_NZUBZTD77eA-2ZLmJa_Zrj5T8I_-RFYJyDXc2GFc7qjMuYZuX3CJqjrdX_kZQ8mtb_zBxJA3I3SudJBooNIN18JO9tCdFcc=)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKAIGIx2B4WSG23h-dc0jtK06NEzqEqvuUvdAL_GNxDrYXcIN0e48pU7_QIY-Hjfv9wZrmZGFGoRuVZn9BiwCNp0wmRCo7QQ28R0CfdPm0cajcm2Ft4XWtZNm1PhUEUzTV_wL52czhr9aSKSjHcbv_x4TUZSlteL09AjfCpakwFeyxiM6uwnwaPcNk-UGjBHoJu6dubaodQ7U0WFKbKv18GM7KW9ligV_bGerbkZud1vV2pHtx0NAnScMlA7FZveoTEVsu46-JuVsjxtMfMQfZJM43z87T2jtzPFKc8n_80iWxtCFLhx5h)
4. [visosafe.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1BF_PNBr8QWB2WCNI5MmjwHP45KTPXpCNT6rAMjYbQoayLGU4HGGGvA82io4Ave4oU8imtGBi-d9F6EUlwnjXlaUqysUbUIF9JnXU_adJ_o-pXtYVyqvY2h3l8SJxvqksFpRA-hJWJ0_7CiEuF5ENxFchPE6hl8rfBylmkCpstFaIp_rJzNOGfN3D8W9QUT7IoFWlbL6X7bs=)
5. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGgDFVrOiAf5u0Nw0Uo-Go4BB6thnPd0MRgYB8Hx1R1qO_Xo9xVtmtrbX2BynrafsJCMzc1X0RimdbNqxHdtK0QuZoDPH_v4J85mUuevmDHfTrzONwMHvs9sU-gx4E1aFOByeB-Lkis0D4kdNdkP4rHVSKO5m7pfTY5m7Pb6Eso95JCxcHxAzZM_LpxOOeiOSLnGA=)
6. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQd9nR5fqPMjOFvBqzvNhReD_80uWD4B68FEHPFRwkMNECEego6281o6pPz-GAi_hcdhURjBxxGhJoKhWYmxIWDSxCoyePtw3DmZsBGdjfpzG9EjmH063hDf9_rHXWgRoqU7jQiFLJBa8jSWkFAwmIXIfVNIFOQdsKm9uwaQhZeiWtSTyNwyC3Oj9uIcQWisg=)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSabqu4Dcrjq1cOi-FneNL0n2ZdE7Sra-wWDUkNnHLRmi5G6tcdbQkJuDgGhS_28AASjPbZ93uPC1XqxWIwJ9wHBWBKqg4dic7qrR7haLHDMYNhcw5-XXhf1OAtYHbs2O5u1H7ATbdYp9CkLX0nLRPcpO4RU3b5LlCNqhtjeFCJTuehm_Py1vIku9MhJ0AjeTv59QuogwVKxTtO_SCoyBfzeY7rQBbgYKCDbUNPYK3fPpPeo4qs_7NdCU=)
8. [nscpolteksby.ac.id](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF367pDlhH6UgNVsNoAF9uGnUtlPUhLIkZI7nlW-1yS_aNQ9-Jg61ioKN3xFsQ991CxwtakO-XeB1-oBIUXsW2fMGGU81nQ43su2zNS7F8Srat4rCbv3HHpmQcXOMxTjvdt-JJud2LwQ7G9sFFZYg-VYDM2YXsDaltDl-XSk0MQWu2h0FoT7iBPUfq1jYfCVfFFSMQgGnVgP1dWJOLBMo4w392FOVERSP3AapfMVH47Ugjk5VXQZVw8yDf2mY9kHJAl8maDLmPPfWyOXn-Y9PHSEo3UcsoGDA==)
9. [ascelibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELZLOI49oq8MwtCAPsyN3_1QTwnGl0zuhZ8bwa2FIknUl0tjg7kPAkClv26mXQj9HzMgOpEGq-mc0FTGCstQfTNPyeeWtsg5br7aimSdVASmCn53h21QLk_9hA52dXbE19_GvYPFP2KDRf)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ7gtQTXS45874-J-5yE2Np8027W9W11kES7GU1XrTJn3vMzSHTvfEziIld2cyBWaJ5OE0RWDO8ZnTrcGEKvm6Yh4JiGMogYuGW7MfFmuzfITIGf0NkW1LThodvIg=)
11. [monash.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Y0tLmzk4aRDJ8sx4RIFTUIPwyu6vpK_7e96jNGXd1pZ_ccON2IoI1E7j9wIGKFJMuff8oqgUtIvyst-10QrjwbwplPBQINXzdleAP3L9TuJLxW2y3sDkxdBeJEIrowBIgEWEz-NtGDrNwnPTuQw30ExzmGeGMnzG6CAhup1Evd6dKvkqYLTrgLeNoGZFDHG7EiBmIxEV70ndvseGn4VjbtOt)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoCyBZRkuIXjS89HnhZx4l-S46NPecml0LeNaYzquS_EpuD8l2K9v0pZnha5_w4ZH37uGvo38ksq7cbFpPctyxx0cPpKE5ujkoqVW6y3eDvjEdVa9rNcsPsyNT3hgyaliV5yWSvd4uVDpH0g0QYnzirRh2NlbHBOOIBgpDIJ-qpE3iccQxp7x6qqZ0p8G6wXAxlzWAHNpDlVOZM2prMc7WlMZUxmab1FfBVEid9rg9Vg==)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHWqGDl976T3GRI24qP1BVnUw3zX5U_Aikpitev6tM1INp6eOWm_UhWv9hHh6UI6Bx06PTNhZ0A95VJ2t_vyKE_9eh0kjsRjgjRGK8cF53YubPIxrCVwJvbMN68Mx5xyoTpB6Ee9emqnf9_UmSsW-KuIIqQTgmcju8PyLrEpfe2owIXEEm_0jQvBtpf7hDvaZBvnkPqq4ZEMfeRTxmrohRaVUwWbq1FTkMawLtLvLIWBAhVE0YK6ot5Xz2ECWp5a8=)
14. [obralink.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGifCtCLXxdBZGrBWWGL3rkzeBp5lGAa8OPeHwigrAfS7MEDK5mOYFuA9rE14kMSGlTRoMbeOKKRgc_K5XBPvF8J5yYZwrtJUiBQF2aE1gkV1x5tLu2g1jOoH2XRFcJnEGCp32xILZP_-C3iZlWrzXe1NS5CTF8juLvFUEhDBqG)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXRgsuie7CSDGjfyHfkk0VXTuNm7o8j49z9L1bDRdkE9WlLypkKeMXkSH-GspspEUL3zDfMORkgSvHUdE-eNUIN6mM7ni0ZqFSi3e_KAGa9k9f1lVliWSKnv-8wmYC)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECqSDt4C90mbriRTJYaVMeqYN7kRbIVMPgoExLaWQkoyClJSVuj4yGFct-KEeCECGM30kWVT6C75HvH9Q5smmctO-riQxea5Sur1FkngBVrgOX1sNSFUV_GFc=)
17. [ec-3.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHknbr3P1GANeaOyxY8573L9N46155ZYhIV06iztYMBwfBH18SnVd24-3I7tjWrkYsqsG-3JNoUKyqYS6EApogFbJCfixbhMEHx4m9sBXxYQM64fDNn5tVB93A4pH2_qqV9w87th1P2jhQ5myp4dmsUaZFJ)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9mwgd84D6FU968VOAW-uDPtJE2M4ACtDJmFeoxhFQMjebsRNbjI4lS-61gI2bu3nzIqokSOAHXhyJw7FPsyXD0n_Gv9p2sShNSscPMTj6f_K6fUPcvBorj_liwMwpvc3USVyhyLUfufTR2xl4anBKQfL5FYGg0xQK4Xya1euj0P9B4VxNx9r0zOS9H-GhlEo3HWO9_CDVS_R_BB5MBF87L4hHe9lnrq8uGQaZhOfREj7c2nU_snztaJxtQKHJE_J9WNA0CQwp0TrIyeN_tuapS2mTOFXHlV9slg==)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX-P2B6gqpaG43woceVvlnESrxc9GtLGxSTXVJhhHZXtKQmDyDV1dXYIuzyAAPU3LZ4tgnxwfyANh0cfzG4BlQoTZcbCanB0wuLoeAtsX0Qr2Sj3JdvmQP9v1ZVtRw)
20. [ijisrt.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwGk5cEgcpzWg9fg4v0xR96FbpOWzWD96rSN8Uagzl6dpyPQMODyjb5mvziFQ4nWSyr89k0TW84UD6V18h7Yd5U3vhEFVF5lxwHekRvePaIk_qejoXP2IOSCkWhXGihqmRSciZYTzWUyI4cu4SlHcmIFG8UfZgPNMSdCB7fEJTtOnzHAEXaoHJ1tu2KwPUsWgY2_LjXsbzgKc=)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfIyyF5rCYAroK3f_d3P-CcA_nHY4cQztDec1mSVHLjc9d2aOdEIEkYUadTzX6QLr3kUG7QXPePgwo9frPTaKTme9dEPYu7Ql14S8pkXJc--tjj8-OD9D)
22. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYtDT9yWomGYm37gkunvPFIw48iFAATg1rG7ishLvYGbtjiISN9bkeBFrq9HpM1T-_o1SDgeyCbmtMy3FGY_-NkU4DQsbv7gfmJfYbPhCr53a5kijCIODxKOqYsqhk-UXaxaozObC7ezY1Zi59ARO_FR7m45JHUVG0imwsDdRLQsftYdFX_clOQEQLlB0UUucorG4cwIFZK9tEFVQbmE1BY7kLedH3nlcD-nws1z3I3YzRnw==)
23. [abccarolinas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgWLMEhkB50vOGvduViGTVuLh46bM2NaCGpqxze6EVQ9FURwPZCXzlGDy9hfVICYPXzAIxFiSJnBNpeVr5EqTUcy38K0F3-AwqJDVp1YHAnCRGNdUmT7SBbWNjN7kvEcGWwy9MRjC-QCt1bOXh)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGad10ivJQPMmTxRmfsNSsm41XTbB_DlXV5mOMSogQy2WCI2_tY6EsIf88IeqXCsBkuJaUFdD_3HXkWjsHcjIETefVgSAN8cUFwwOtK4AMoQO8BHUktZ5eAe8Lk4Q==)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9BL6HB5vfIwFaltEWShzR1AAg8Dso3wz019n49_E6IdOPGOjg1xhEIUh4AcfyzqQIHyulg9B81v38cuog9_Eytn8C79xrp4ByoAw7Lo9xefS-iPAVzZXlMXk8d9sm)
26. [vjol.info.vn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjSjd8GMVISThxASksTt60Ic0C_BrwiaIcz82iR5cZBHCPv7sR7uyA33OwxipnuYSmKa8kyKc2a2GuToenAO05bnCtylxd0Z2QNhhCxtyWLsT9EkIHUN0C1qOp2EzIuQLRCY3Cz4retQyMfxH_rUeWl3c5yHPPf1VcThg=)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOvBttoMkQXKRJxR7nuUazWXmDzRkFYnRhU1JOzp3ZV_OH8ajem4R3uVBNImqKlEIZDs4XEeHZ6LT_eEwOrZiYSPWQo6pAuAlv-XedUvj2GIyFdnj0OvR5Bp2YJzMG)
28. [iaarc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjpGBtSOejpT36uZXQNgBfJc2vPlw8DSo8P-_opmsypehWVHrYm0P-ipjbRUV9vfyNDB2PtDTSmEsOGCvwdUkyG85SOxiEg7L2tdTHWlc5DpUiLHI9p923e7S7zmg0rcNNcdjewNcy_dYSOcud_twieJ1-zf3j5o=)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjUXP0UlEaICgXvSt_pYYboXsD33RLVuGfhrZU5eNBV0xgZOcQSS-0SeDYDWPbO7JuU1R76hfI9GkaBKXiUsfaWcTOZrZOCfSjGX1yeRqlab63ISKFEchk9Pu3dRpaEMrSe553eCeDbcIlBaTjycWHeQG6CLL8wUBNxiQ25AsO2U1GlA0Fv7IsN9zO7d_qZ1WH4k7PoPhGFEVf7g8KOTVeuomJrCBASE6MGggnwBjsYWBw4lu1-76RjSgkQjgOBpkFvBboOwkPt3Wxleg=)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfH2McClawalXeeU7BThe_jppvobJZ7XTiF0tPYHPZ2rS_GK2ydozWRZReIOwi1ZfGhOWcz8fc-LAlAAtmoPfnEGPfzjNTi13J3Wo8LpKejbMKftxmMfHVVsxcUNJJVWxHL1fERTTe7DfYdpjoMZ2-hXEDkFJRWGMMpwSQ5Oku9XRstH3eTkXw4HymOMGib44J2viM5EE58ekz-8e0k5sxewxNzawrfVN2m55GB5a92ghle2d9nopNQisF7cVm)
31. [ascelibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI8hzIj7J1Ykssa9Cm-7N24pjLoZExGKhlcF-WV6lu1Hh8ojgVoRBRbIQgelA3TqrOzM81B9TLV2uE4yqHoB55m-DoQrkvRuYtDYMRL2crTvm1IehzVHzdY-__srcJoqTCxz79cp82F-7v0E2CSHQ=)
32. [tenna.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_bka5VYbEKfIwfbhw_Djuctet-TtjmSKfDocz-S6RqoMje1vWj_xq9xwyzrkehF7uTgSIaD1vOYXIDPLLQ73p6hJoHcp-xH0lTZHOkKJE99HJK_pqIp3qMEn_xKILPvjRSl5rbDvr-EdkTIcxqGJbA4NfZas=)
33. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtM2VEG6fJKxjrE9ZgcqXbAIL3la32CGSnyds4jWEihI6WS21zN9f0FBYbLMOB0aPOOnIdDnKCbSzlTcg-od1MYZAfvAkEttAZvxWQwkH3uHE_tOfVI0Zu6nWKGHQe)
34. [activefence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOY1SdSLIP0DeAwUnJWyVFX5bgTGFzEFYnoPQyCy05zVODW0zde98uYIcoIbfSThn0z0ktIy5VzW9VfqoR5DU5Z9L9cr_7RYdI7hvbR24jKOYTrlAEZ5vaYc8CQxLgjMpCy_We-BocqRjaVtHZsPmzgoi_hgwj38QQzK4OqA2yov5jvOWPX38yxd2zjvrOltyfHA==)
35. [nyu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvoVnP-VWPm13ub9qP5ebCgW2IVyHaOqlKsDrdJhy-q7DRJE6bXYZV1MhfiLN0FYT_e4t3d1caDDbCquLEQiMXF3QxeGM4k_NnW3tC9x5E_XapLDO0cpcOqbULgKoO01WEe6bgs7QBRf2ag0nRh-NugKk74VinP9fBNcqGSPdR9VUWk-_5qkcr7NMOyfQcOPo=)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBoSeKl9xOxE5AlATdr0t1ZMYSvVHH22mCRumN1c0DiYN_TppdCmYY9VzbffsS1gElnAn5CCrBqlmp9HzpoRmieI8kXTHgRJWsHthqm608UOpVKZB4zQEW2HEkVe-CfB4KKDaKvfU=)
37. [ascelibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG76_KBVagLRPqAfDiob3Wy5eg3xsSo-zVUEA76Pyn5-4UNwfO0d_Hr57RpyaC3u-SY0LMSxvoPx7vL58nBMj5a-hg2cRUHet1A-2_hIKEdaa3v5IEnoY6XMaySGofU3vyNafJoxKZE3OuD)
38. [worldconstructiontoday.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs2LHWjgWbzysIIc5Z0jyDT2nf7DUydcQDg89zopc04OK6MduFh0sfjKGWFBo2O7sfT7TpNTRQcw384jUh57yL_CJHCYZ28l1L9pVcfpgEf_ML4HBUq6qNst8OJ1TqFCXllVBaQa07dcQkur5Jy54GFJjLXYcnRMbUTKNU4rL1HZM6ogEDN1A1uj7fsp0oUk1zl9uhAJlsbkaLTsjpjYqRVsw=)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsF5yJtGUVjlQdWIfxFKLXxMIBb9WZdSAfSJDqvKLG9jENsjt6TjjKgFAh3f_SQfbtjUM5VC6h6fEmFesv9b0X7E1ACjby-yjNBfSOYGfpGul9afeCyX-GdiAvhgo0wK2XscFT6gs_ayKY0TIrlgZJpp6_cX4dHuTraygPsG4ylPGaklYyw8jCbDLwXSkiIjkZxzBiDyXNrzkblD0jtAPWo3_fdwFO0EANJNN8xYkDa8YXxclMGcG8)
40. [ciobwcs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5Hnujb6oy2ERZpGodipYdvELSQnE_GPZ-2EaBn0GqU3zdsEh423zRiBDDO6g4o-UrxOhKhy8eWUvluEd4EM95dPsCcs8lPkPeKhO-eVItCD6c458xqbTZn0_A3x2VTfQIDbD7UGQ=)
41. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLSDhOpdMcLWk6NemtThHrp2l4YzIHmI5LMFgNGqZxvmQf7eGazE-vWGWo8_MKChu1ibNnrlCT0-A0CrnuCZHzd3CLhoIeeyvO9mxpua-T2jWfm3aICW5pniURfQESg4kUqW7TjPW9qA2Eg8ikM-gP9vi1oRdjsdBcPvoUjteds_o9bXUSsoFeTI8ujXh9IOOQXMxaiwqtY9pdt-zCKuEIE44qa8_fQtYX-tcGjKQhpWRE8VHtd3KOUnk=)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsbDYJQDklY1DHbrUkHAjwAGjABJreGYbuxL1xPgKuwk6Ri7Oy1Qb20WjZTLvZaZuUY02qzm3TxCW-2Rr_gl01XuOQIMxjnathOR0y8MJmow5X0bZoaj5nguf5kOEe)
43. [infotechinc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUSjYVxBi3QTlL8z2r1BGoSB5dhk1-fts4Vgup1gY0GXhu3AmjTy9_ZONdavilfC1RAP0KFTmPM1aqjm1GEKdCh3DlHkbh_cJrJz783u4MYYRBqlQd4OmRIt6T1Z_owYCY613Bbv6CXdDU3Cq2DhNswHL6BmZAlrcht9UQonfQITkA10umNJe42WTzk4AGTIjl5Ywx1lVngqc=)
44. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN3YgmlxknekvdO6Dw3XJQCW2-iAf3Eu1sXyZWFhEc82wh4CZj5z4U_HzqX1dEeQIGeG4dYawxMBEddwH-gFIPX4YxsvYgumpRhxL5BY5JZEJXIjKEXrnW7AHENNgy)
45. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtJ4Y4blkFvqDcBAhUrC3QksMGwKCDPgnt9BNz2_KuHUtvlgSO7wvYXDJ6WLPmyBTOfbdpmkK5ElKgAc7Cum9C9VqSqJZDcXjPfiTAJZHgKcrsCVaBNm2AN_XdoaKrGx7JHZX6dHFztr4WD7_7Io0wN3GyxHbjBZl_XfPywwlyJ-d1wiY=)
46. [randomtrees.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoUPtj6_jCI4YtNawrDFNBGMrTxBOZabZQl2UGydWaQu3xpWIr57JGcL35vC8ic5ZPAmVDAMBcCiIuVzyqrVMRSoF5FYEqfaU2QjNk16TDSbS8Y5eyQKUTDfSe0DREXlZz5DiFf9FVL8oJwo2QocLDNIXqcpi3z-op4Z795q0gyof062iC8Vn)
47. [ijraset.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYGoIADmECu1dbxyn2pBjwdL3BwKlhTkJlHfU56EEwhenVzg5ejSxLqU1VBFGUXeLIwQWwin_cfTbFG7GsdHcW7al337TECHHNt3MRBAUT-EHaoRDCVOEp52_rBityXsO4fnlpDIxwM1QVVwS4WdXpIVhbr0kGoAUbZm2EhIS4i7OFsr_xXhLypb3bEALYH1sMET6AdTFWTJNA4zcaoaaRGFcZ)
48. [gomotive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFITGA1tpfFmXABQSq57ZdTQV8s_tp6YtPltlS_XvVEScIjMn7KVvS-fIL_eAEYLEmAMxA2bAjfqFgmgid8VXT7p9k6UpOTF_pMmV8qm7h4Ejm45bAVo9U4xlTZrGMMBbBSQ2wvRNWbCcP6ZpnlzsifkwUhentbHw==)
49. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnt-qXjmUBSh5If2cl_TSBrJrTcgOYLr01dNCZ7Wt9fPi5aHZmiJTI1862hM27yCw6tXcmE6-ATytCfOiTzlJHCTf7bOb86CaFLSaN_iwlIsFRzdxNQqeHEjevTc8W0d3kMjY=)
50. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF01L2c7RVPke_HHzWyY2lNUtnyMMNQi0lrnnevqy9dErtIN6joBgBsJWTYtZu5c3QqmNN0DAN55yqJg0F2q4R-knr5Z6dXndoDVtE4sk36OLDCCimm7lrd2YSedNmeSmtA1l14myxbdfMoE798x9wapulnvtg_kg==)
51. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRGhScgxD3htvCo8CymLXqd4pSWbzAeob3eFnfqU-ocrHah5ii8QDwBdbvoq3GfWPd6LCNDVgLhAYminVkTvgpNqiCg9GC12MguxAb9QWf-8jcpHl900kaED2vgSaOJzGXjzmCDJoQjcOG0V9Z_jXo3EJFEVZu407BwYKXh1bqyuOjGaRJeeA59Udl2FEKpMosLxOC8swbY4mlceOiycu7lgpcDHGJYP5ujNAG6V-4dLfa5bLjuZonqD0zg-wjWTEesOFg)
52. [evotix.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFErnsR3Hy3DLei24lJWNlvTRLL81T2uLE-9CXix7Ne1EnbFHXNOjiEi7XPhQGN-30qDLYhgyw12iPGIB6YTLAE8xyaWDeOLt8xp3ywyw8MPXcUwnoNlMNQsDnJygDJxDzVmj2Tu326eh17OPybumX04d1ygH3g8_KSrnGrUmwR-LxjYWDJGT1u17tcb5LTHBJvb42fBbuIC7A=)
53. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDjJ7R501swUEJXjWpf5mXfNI22TiSRhn9Y-ygvBHHNfBw2LGj74ZYEuiLrc9J2dOfCTk7WtYw1Wb896BGqe6uHj7-gB7d6ga2vK2hyVcYbOhAbgAjSGe26JssXzMH)
54. [viso.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWRFrClOVY1Ymh6odpYFggIhEQUyXVCLd9OTCghNeW10_h43ulQwNSEmVDyfXiSQTeMY6e_fFutVMFCU32jItRrdP5mhn6QfPyUtW98JOyKE_h6nAQKO0eZkwRAId5xlpCFobqWx4YpCcZ)
55. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjDWfXmObu9G9JDYdu7tzDxhUTr8xnRO9v8C2Onsnv7M6acFq3efb2ErNaPv6ffUDPTfKi9hXQOgrY0hwdFjZAPl-czPlvKrwklgilVmVNFmOdYHMFq5RGuRmW707g3g==)
56. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-CiZfC0Md4FUQTczcLExKaTnW15BBsGe_uCfGHxlJjFDvqvim3PmyjRp8t0JVTWnDBeHYdoV5yWxM5c7Xu7GU4OrtyejqIMxm3jRM8VdVv8PqGwCQ-TrQjovwxMQlTSkRszfJHg7_Wso5VdC4SOA=)
