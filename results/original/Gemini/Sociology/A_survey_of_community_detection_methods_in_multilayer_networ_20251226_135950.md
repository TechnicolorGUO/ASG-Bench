# Literature Review: A survey of community detection methods in multilayer networks.

*Generated on: 2025-12-26 13:59:50*
*Progress: [4/21]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/A_survey_of_community_detection_methods_in_multilayer_networ_20251226_135950.md*
---

# A Survey of Community Detection Methods in Multilayer Networks: Foundations, State-of-the-Art, and Future Directions

**Abstract**
The analysis of complex systems has evolved significantly from single-layer graph representations to multilayer networks, which capture multiple types of interactions (layers) between entities. Community detection—the identification of densely connected groups of nodes—remains a fundamental task in network science, yet it faces unique challenges in the multilayer context due to the heterogeneity and interdependence of layers. This systematic literature review provides a comprehensive examination of community detection methods in multilayer networks. We synthesize foundational concepts, trace the historical transition from monoplex to multiplex methodologies, and critically analyze the current state-of-the-art, including the rapid emergence of Deep Learning (DL) and Graph Neural Network (GNN) approaches. Furthermore, we evaluate benchmarking frameworks, specifically the evolution from the LFR to the mABCD models, and discuss applications in neuroscience, finance, and social media. The paper concludes by identifying critical research gaps, particularly regarding robustness, scalability, and the handling of bipartite multilayer structures.

---

## 1. Introduction

Network science has emerged as a powerful paradigm for modeling complex systems across sociology, biology, and computer science [cite: 1, 2]. Traditionally, these systems were represented as single-layer (monoplex) networks, where nodes represent entities and edges represent a single type of relationship. However, real-world systems are rarely this simple; they often involve multiple, distinct types of interactions, time-varying connections, or hierarchical subsystems. To address this, the field has shifted toward **multilayer networks**, which allow for the representation of diverse interactions as separate but interconnected layers [cite: 2, 3].

A central focus of network analysis is **community detection** (or graph clustering), which aims to partition the network into groups of nodes that are more densely connected internally than with the rest of the network [cite: 1, 4]. While community detection in single-layer networks is a mature field with established algorithms like the Louvain method and spectral clustering, these traditional algorithms often fail to capture the rich, complementary information present in multilayer structures [cite: 1, 3].

The motivation for this review stems from the rapid proliferation of multilayer network research and the concurrent explosion of deep learning techniques applied to graph data. Recent surveys have highlighted the "untapped potential" of this field, noting that despite significant strides, the area remains underexplored regarding robustness and unified frameworks [cite: 2, 5]. This paper aims to provide a rigorous, academic overview of the field, categorizing methods into direct, indirect, and learning-based approaches, while critically assessing their strengths and limitations.

---

## 2. Key Concepts and Definitions

To navigate the literature, it is essential to distinguish between the various terminologies used to describe layered networks and the nature of communities within them.

### 2.1 Multilayer and Multiplex Networks
A **multilayer network** is generally defined as a quadruplet \( M = (V_M, E_M, V, L) \), where \( V \) is the set of nodes, \( L \) is the set of layers, and edges can exist both within layers (intralayer) and between layers (interlayer) [cite: 2].
*   **Multiplex Networks:** A specific subset of multilayer networks where the set of nodes is the same across all layers, and interlayer edges only connect a node to its counterpart in other layers (diagonal coupling). This is common in social networks where the same users interact on different platforms (e.g., Facebook, Twitter) [cite: 6, 7].
*   **Temporal Networks:** Often modeled as multilayer networks where each layer represents a snapshot of the system at a specific time \( t \), with interlayer edges connecting nodes across consecutive time steps [cite: 8, 9].

### 2.2 Community Structures in Multilayer Contexts
Defining a "community" becomes complex when multiple layers are involved. The literature distinguishes between several structural definitions:
*   **Pillar Communities:** These are communities that extend across all layers. For a group of nodes to form a pillar community, they must belong to the same community assignment in every layer of the network [cite: 7].
*   **Semi-Pillar Communities:** A more flexible definition where the community structure persists across a subset of \( k \) layers (where \( 2 \le k < N_L \)), acknowledging that community membership may evolve or disappear in certain layers [cite: 7].
*   **Multislice Communities:** A concept popularized by Mucha et al. (2010), where a node \( i \) in layer \( s \) is treated as a unique node-layer tuple \( (i, s) \). This allows a physical node to belong to different communities in different layers, coupled by a parameter that controls the penalty for changing community membership across layers [cite: 10, 11].

---

## 3. Historical Development and Milestones

The history of multilayer community detection is rooted in the expansion of classical graph theory to accommodate heterogeneity.

### 3.1 The Single-Layer Era
The foundational work by Girvan and Newman (2002) established the rigorous study of community structure using edge betweenness and modularity maximization [cite: 3, 12]. Modularity (\( Q \)) became the standard quality function, measuring the density of links inside communities compared to a null model (random graph).

### 3.2 The Multislice Breakthrough (2010)
A pivotal milestone in the transition to multilayer analysis was the work of **Mucha et al. (2010)**, published in *Science*. They developed a generalized framework for network quality functions that allowed for the study of community structure in arbitrary "multislice" networks [cite: 10]. By introducing a coupling parameter \( \omega \) to link node instances across layers, they formulated a multilayer modularity function:
\[ Q_{multi} = \frac{1}{2\mu} \sum_{ijsr} \left[ (A_{ijs} - \gamma_s P_{ijs}) \delta_{sr} + \delta_{ij} C_{jsr} \right] \delta(g_{is}, g_{jr}) \]
This formulation allowed researchers to detect communities in temporal, multiscale, and multiplex networks simultaneously, effectively launching the modern era of multilayer community detection [cite: 9, 10, 13].

### 3.3 Divergence of Approaches
Following Mucha et al., the field bifurcated into distinct methodological streams:
1.  **Aggregation/Flattening:** Early attempts simply merged layers into a single weighted graph, applying traditional algorithms [cite: 6, 14].
2.  **Ensemble/Consensus:** Detecting communities in each layer independently and then merging the results [cite: 14, 15].
3.  **Direct Multilayer Optimization:** Algorithms designed to operate directly on the supra-adjacency matrix or tensor representation [cite: 6, 14].

---

## 4. Current State-of-the-Art Methods and Techniques

Contemporary research has expanded beyond heuristic modularity maximization into probabilistic models, matrix factorization, and, most notably, deep learning.

### 4.1 Taxonomy of Traditional Methods
Current literature categorizes non-deep-learning methods into three primary classes [cite: 2, 6, 14]:

1.  **Flattening (Aggregation):** This reduces the multilayer structure to a monoplex network. While computationally efficient, it often results in information loss, particularly regarding the specific topology of individual layers [cite: 16].
2.  **Assembly (Ensemble):** Communities are detected locally in each layer and then integrated. This approach respects layer heterogeneity but struggles with aligning communities when node identities are not strictly consistent [cite: 2, 15].
3.  **Direct Methods:** These are currently considered the most robust for preserving structural integrity.
    *   **Generalized Modularity:** Extensions of the Louvain algorithm (e.g., GenLouvain) optimize the Mucha et al. objective function directly [cite: 17, 18].
    *   **Information Theoretic:** The Map Equation has been generalized to multilayer networks (Infomap), minimizing the description length of a random walker moving across layers [cite: 18].
    *   **Tensor Decomposition:** Representing the network as a tensor allows for the extraction of latent community structures via non-negative tensor factorization, often requiring the number of communities to be known *a priori* [cite: 14, 16].

### 4.2 Deep Learning and Graph Neural Networks (SOTA)
The integration of Deep Learning (DL) has revolutionized community detection, offering superior handling of high-dimensional data and node attributes [cite: 19, 20, 21].

*   **Graph Convolutional Networks (GCNs):** GCNs aggregate feature information from neighbors. Recent models integrate GCNs with modularity optimization or Markov Random Fields (MRF) to perform semi-supervised or unsupervised community detection [cite: 22, 23].
*   **Variational Graph Autoencoders (VGAE):** These probabilistic generative models learn low-dimensional embeddings of nodes. The **VGAE-ECF** (Enhanced Community Detection with Structural Information) represents a recent advancement (2024), incorporating community structure information (from Leiden or Louvain) directly into the learning process to improve latent representations [cite: 24].
*   **Deep Graph Clustering (DMoN):** A significant recent development is the Deep Modularity Network (DMoN). Unlike supervised GCNs, DMoN optimizes a modularity-based objective function in a fully unsupervised manner. Recent robustness studies (2025) indicate that DMoN maintains stronger resilience against adversarial attacks and perturbations compared to supervised counterparts like GCN and GAT [cite: 25].
*   **Synergistic Approaches:** New frameworks (2024) have demonstrated that integrating traditional algorithms (like Louvain) into GNN architectures (like GAT) significantly boosts performance in downstream tasks such as link prediction, exemplifying the trend toward hybrid models [cite: 26, 27].

---

## 5. Benchmarking and Evaluation

Rigorous evaluation requires high-quality datasets and synthetic generators with ground-truth communities.

### 5.1 Synthetic Benchmarks
*   **LFR and mLFR:** The Lancichinetti-Fortunato-Radicchi (LFR) benchmark is the standard for single-layer networks. Its extension, **mLFR**, generates multilayer networks with realistic degree and community size distributions [cite: 28, 29]. However, mLFR has been criticized for computational intensity and limited ability to model complex interlayer correlations [cite: 30].
*   **mABCD (2025):** To address these limitations, the **Multilayer Artificial Benchmark for Community Detection (mABCD)** was introduced. Building on the ABCD model, mABCD uses a "biscuit-like" latent layer to manage node assignments, offering a faster, more scalable, and analytically tractable alternative to mLFR. It allows for precise tuning of interlayer consistency and is implemented in high-performance languages like Julia [cite: 29, 30, 31, 32].

### 5.2 Evaluation Metrics
Common metrics for comparing detected communities to ground truth include **Normalized Mutual Information (NMI)** and the **Adjusted Rand Index (ARI)**. For networks without ground truth, **Modularity (Q)** remains the primary internal quality metric, though metrics like **Conductance** and **Surprise** are also utilized [cite: 1, 3].

---

## 6. Applications and Case Studies

The versatility of multilayer community detection is evident in its application across diverse domains.

### 6.1 Network Neuroscience
The brain is intrinsically multilayer, with connectivity varying across time, frequency, and subjects [cite: 17, 33].
*   **Dynamic Connectivity:** Algorithms like GenLouvain and DynMoga are used to track the evolution of brain modules during cognitive tasks. Recent studies (2024) have focused on identifying "redundancy-dominated" modules, revealing how higher-order interactions support the balance between segregation and integration in the brain [cite: 34].
*   **Disease Classification:** Multilayer community features are increasingly used to distinguish between healthy controls and patients with neurological disorders (e.g., Alzheimer's, Schizophrenia) by analyzing fMRI and EEG data [cite: 35, 36].

### 6.2 Financial Systems
Financial markets are modeled as multilayer networks where layers represent different asset classes, time periods, or types of correlation (e.g., price, volume) [cite: 9].
*   **Systemic Risk:** Community detection helps identify clusters of highly correlated assets. A 2025 study on "hidden community interlayer spillover" demonstrated that trading volume layers impose hidden structures on price return layers, which are undetectable by single-layer analysis. Ignoring these multilayer interactions can lead to underestimations of systemic risk [cite: 37, 38].

### 6.3 Social Networks and Recommendation
In social media, multilayer analysis aggregates user interactions across different platforms or interaction types (likes, comments, shares) [cite: 2].
*   **Link Prediction:** Hybrid GNN-community detection models have shown success in predicting missing links in scientific collaboration networks by leveraging community structures to overcome scalability limits [cite: 26].
*   **Deep Learning Applications:** End-to-end frameworks using GCNs on email datasets (e.g., Enron) have achieved higher modularity scores than unsupervised benchmarks, aiding in the identification of core community members for forensic analysis [cite: 39].

---

## 7. Challenges and Open Problems

Despite progress, several critical challenges remain, as highlighted in recent surveys (2024-2025) [cite: 2, 5].

1.  **Robustness and Adversarial Attacks:** The sensitivity of GNN-based community detection to graph perturbations (node attribute manipulation, edge deletion) is a major concern. While unsupervised methods like DMoN show promise, the general understanding of robustness in multilayer settings is limited [cite: 25, 40].
2.  **Scalability:** While mABCD improves benchmarking speed, detecting communities in massive real-world multilayer networks (millions of nodes) remains computationally expensive for direct methods like tensor decomposition [cite: 41, 42].
3.  **Heterogeneity and Bipartite Layers:** Most methods assume homogeneous node sets. Practical scenarios often involve **multilayer bipartite networks** (e.g., user-item interactions across different domains). Existing algorithms for undirected networks are not directly applicable, necessitating new models like the degree-corrected stochastic co-block model [cite: 43].
4.  **Parameter Sensitivity:** Methods like multislice modularity rely on coupling parameters (\( \omega \)) that significantly influence the resulting partition. Selecting these parameters remains largely heuristic, lacking a unified theoretical standard [cite: 9, 36].

---

## 8. Future Research Directions

1.  **Integration with Foundation Models:** The use of Large Language Models (LLMs) and foundation models to enhance graph embeddings and interpret community semantics is a nascent but promising direction [cite: 44].
2.  **Unsupervised and Self-Supervised GNNs:** Moving away from label-dependent GNNs toward self-expressive and unsupervised architectures (like DMoN) is crucial for real-world applications where ground truth is absent [cite: 23, 25].
3.  **Dynamic and Higher-Order Interactions:** Future work must better account for higher-order interactions (simplicial complexes) and the continuous temporal evolution of communities, moving beyond discrete snapshots [cite: 34].
4.  **Explainability:** As deep learning models become more complex, developing explainable AI (XAI) techniques to interpret *why* a multilayer community was detected is essential for trust in fields like medicine and finance.

---

## 9. Conclusion

Community detection in multilayer networks has matured from simple aggregation strategies to sophisticated direct optimization and deep learning frameworks. The field has established rigorous definitions for multilayer structures and developed robust benchmarks like mABCD to validate new algorithms. While the "Mucha et al. (2010)" framework remains a cornerstone of the discipline, the frontier has shifted toward Graph Neural Networks that can learn complex, non-linear representations of node connectivity and attributes.

However, significant hurdles remain. The trade-off between model complexity and scalability, the vulnerability of deep models to adversarial noise, and the lack of standardized parameter selection methods are pressing issues. Addressing these challenges requires a multidisciplinary approach, blending the theoretical rigor of physics and mathematics with the computational power of modern machine learning. As multilayer networks continue to provide the most faithful representation of complex real-world systems, the refinement of these detection methods will be paramount for advancements in neuroscience, economics, and social computing.

---

### References

*   **[cite: 1]** Huang, X., Chen, D., & Wang, D. (2020). A survey of community detection methods in multilayer networks. *Data Mining and Knowledge Discovery*. [cite: 1]
*   **[cite: 6]** Roozbahani, Z., et al. (2021). A Systematic Survey on Multi-relational Community Detection. *arXiv*. [cite: 6]
*   **[cite: 19]** Su, X., et al. (2021). A Comprehensive Survey on Community Detection with Deep Learning. *arXiv*. [cite: 19, 45]
*   **[cite: 8]** Kim, J., & Lee, J. (2015). Community Detection in Multi-Layer Graphs: A Survey. *SIGMOD*. [cite: 8]
*   **[cite: 3]** Huang, X., et al. (2020). A survey of community detection methods in multilayer networks. *Springer*. [cite: 3]
*   **[cite: 12]** Girvan, M., & Newman, M. E. J. (2002). Community structure in social and biological networks. *PNAS*. [cite: 3, 12]
*   **[cite: 2]** Boukabene, R., & Benbouzid-Si Tayeb, F. (2025). Community Detection in Multilayer Networks: Challenges, Opportunities and Applications. *arXiv*. [cite: 2, 5]
*   **[cite: 44]** Guo, J. (2023). An Analysis of Community Detection Methods in Multi-layer Networks. *escholarship.org*. [cite: 44]
*   **[cite: 14]** Zhang, Y., et al. (2023). A Joint Method for Community Detection in Multilayer Networks. *Mathematics*. [cite: 14]
*   **[cite: 7]** Hanteer, O., et al. (2021). Overview of communities in multilayer networks. *Frontiers*. [cite: 7]
*   **[cite: 16]** Chen, D., et al. (2020). Community Detection Algorithm for Multilayer Networks (MSH-LPA). *Symmetry*. [cite: 16]
*   **[cite: 17]** Puxeddu, M. G., et al. (2021). Multilayer Community Detection in Brain Networks. *Frontiers in Neuroscience*. [cite: 17, 33]
*   **[cite: 15]** Amelio, A., & Pizzuti, C. (2017). Modularity-driven ensemble-based approach to multilayer community detection. *DAMI*. [cite: 15]
*   **[cite: 9]** Bazzi, M., et al. (2016). Community Detection in Temporal Multilayer Networks. *SIAM*. [cite: 9]
*   **[cite: 4]** Atzmueller, M. (2019). Taxonomy of models for community detection in social networks. *ResearchGate*. [cite: 4]
*   **[cite: 3]** Huang, X., et al. (2020). Comparison of some classic community detection algorithms. *Springer*. [cite: 3]
*   **[cite: 10]** Mucha, P. J., et al. (2010). Community structure in time-dependent, multiscale, and multiplex networks. *Science*. [cite: 10, 11]
*   **[cite: 9]** Mucha, P. J., & Porter, M. A. (2010). Communities in multislice voting networks. *Chaos*. [cite: 9]
*   **[cite: 11]** Porter, M. A., et al. (2009). Communities in networks. *Notices of the AMS*. [cite: 11]
*   **[cite: 17]** Jeub, L. G. S., et al. (2019). A Generalized Louvain Method for Community Detection. *Netwiki*. [cite: 17]
*   **[cite: 18]** De Domenico, M., et al. (2015). Identifying modular flows on multilayer networks. *Physical Review X*. [cite: 18]
*   **[cite: 16]** Strehl, A., & Ghosh, J. (2002). Cluster ensembles. *JMLR*. [cite: 16]
*   **[cite: 41]** Wang, J., et al. (2019). A fast algorithm for integrative community detection of multi-layer networks. *ResearchGate*. [cite: 41]
*   **[cite: 14]** Paul, S., & Chen, Y. (2020). Spectral and matrix factorization methods for consistent community detection in multi-layer networks. *Annals of Statistics*. [cite: 14]
*   **[cite: 46]** Wilson, J. D., et al. (2017). Community extraction in multilayer networks with heterogeneous community structure. *JMLR*. [cite: 46]
*   **[cite: 26]** Liu, C., et al. (2024). A Community Detection and Graph Neural Network Based Link Prediction Approach. *arXiv*. [cite: 26]
*   **[cite: 25]** Tsioutsiouliklis, S., et al. (2025). Community detection robustness of graph neural networks. *arXiv*. [cite: 25, 40]
*   **[cite: 27]** Han, Y., et al. (2024). Synergizing community detection with GNNs. *MDPI*. [cite: 27]
*   **[cite: 28]** Brodka, P., et al. (2020). mLFR Benchmark. *GitHub*. [cite: 28]
*   **[cite: 29]** Kaminski, B., et al. (2025). The Multilayer Artificial Benchmark for Community Detection (mABCD). *arXiv*. [cite: 29]
*   **[cite: 30]** Kaminski, B., et al. (2025). mABCD: A new benchmark for multilayer networks. *arXiv*. [cite: 30, 31, 32]
*   **[cite: 5]** Boukabene, R. (2025). Challenges and Opportunities in Multilayer Community Detection. *arXiv*. [cite: 5]
*   **[cite: 42]** Li, J., et al. (2024). Deep learning for community detection: progress, challenges and opportunities. *arXiv*. [cite: 42]
*   **[cite: 43]** Qing, H. (2024). Community detection in multi-layer bipartite networks. *arXiv*. [cite: 43]
*   **[cite: 24]** Patil, J. H., et al. (2024). Community Detection Using Deep Learning: Combining Variational Graph Autoencoders with Leiden. *Information*. [cite: 24]
*   **[cite: 20]** Liu, F., et al. (2021). A Comprehensive Survey on Community Detection with Deep Learning. *IEEE TNNLS*. [cite: 19, 20]
*   **[cite: 47]** Liu, F., et al. (2020). Deep Learning for Community Detection: Progress, Challenges and Opportunities. *IJCAI*. [cite: 47, 48]
*   **[cite: 35]** Guo, Z., et al. (2023). Improved brain community structure detection by two-step weighted modularity maximization. *PLoS ONE*. [cite: 35]
*   **[cite: 36]** Bassett, D. S., & Sporns, O. (2017). Network neuroscience. *Nature Neuroscience*. [cite: 36]
*   **[cite: 33]** Puxeddu, M. G., et al. (2021). Multilayer analysis of EEG-based brain networks. *Frontiers*. [cite: 33]
*   **[cite: 34]** Varley, T. F., et al. (2024). Higher-order redundancy-dominated modular structure in the brain. *bioRxiv*. [cite: 34]
*   **[cite: 10]** Mucha, P. J., et al. (2010). Community structure in time-dependent, multiscale, and multiplex networks. *Science*. [cite: 10]
*   **[cite: 7]** Magnani, M., et al. (2021). Community Detection in Multiplex Networks. *ACM Computing Surveys*. [cite: 7]
*   **[cite: 21]** Jin, D., et al. (2021). A Survey of Community Detection Approaches: From Statistical Modeling to Deep Learning. *IEEE TKDE*. [cite: 21]
*   **[cite: 25]** Tsitsulin, A., et al. (2023). Graph Clustering with Graph Neural Networks. *JMLR*. [cite: 25]
*   **[cite: 22]** Zoghlemi, C. E., et al. (2024). Contextual Multi-View Graph Community Detection Using Graph Neural Networks. *ResearchGate*. [cite: 22]
*   **[cite: 23]** Wang, P., et al. (2021). Community Detection Based On Graph Neural Network. *ResearchGate*. [cite: 23]
*   **[cite: 5]** Boukabene, R., & Tayeb, F. (2025). Community Detection in Multilayer Networks: Challenges, Opportunities and Applications. *arXiv*. [cite: 5]
*   **[cite: 39]** Zhang, Y., et al. (2024). Deep Learning for Community Detection in Social Media. *Applied Sciences*. [cite: 39]
*   **[cite: 37]** Kazemian, B., et al. (2025). Hidden community interlayer spillover detection in financial multilayer networks. *PLoS ONE*. [cite: 37, 38]

**Sources:**
1. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2oEpDEOT7XQg7lMVpForY5dJg6nbh6UykQhbGYXvSSYi1njoZpOhPBa9xIvXJJo7C7gWYt4ATv9RiqDTs8gtQ-mKZ5UhcbTkLH8i8q-bNRlBXhT_WzoIDGBK5XztdH0r29RDNbR3eaxcGna_f3WNRAJTk2d21YfykaHL24vx9jJKMqcg-CPZ4VtoeeyOjPyrqg5JWGihf-yjTcAs8mAh5j5csA1d0aL79LRH9tbXzaLAE3OowO6zgKr8hSiyT9EA0OzU3)
2. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV8epALgIwRt8HO3wbpYFpTWRHq-s3hs1-_l2MYud0-KtVc5Dxuo3MJy-J1N0I_DvwhgZYxvOhX5XFQGaO4LatvI3xD4tPo5kkM3d8ygU9BlUEXd0gNLPudw==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTzKERrWjdES6e1NitcP-Qj3IbWRMmCqKgArTIK3MfBtMIYv3ErCrprgaootYwaB4o8pgxNJM5LutlT8YJ7jk4tw_kpooEErtxpunLQ_V12_2cUqqbo-DUhuwosis5IQ0pk7NC2CEnN854s_uATP6vTwnPRk5HKijyTcwQDUPmLkCB_3zvj6bCNu16TTuKRjyI5w2r_eeLb7A3wwQN0yvh3uDeryBEPQ==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHZ6DYx6mzpMcm53OORi98E10KPq4knDG9cNgmYDe8L8mAdRSz-Q-cJ_t7z8wwUc9l89e2TQhoSoTyjCVnoikoQdL_Po7bSufhluFWflThkPGi4LXVXrtcLh8QSJO7aKSNqz9XsbtYJ28bENX_zNufzaZIMdwYeS-7mYvNuBXBKV-2s_qvIwvjaxpXjjVqkRwidHBSphOPChmVg5VxayWhm0OUIvyw)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSHz8PiL48cbfvz7APVy1y0jKRyB5uuSETbqZE4HAENO15GXAyO09vjU_jh6RxNXXVVqLT4UYj-By30_MjshGr5tgEcd6ZzIDKE5387X9MvsxI3MF3rZPQ2Ss=)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2YbCO0MUsjM1DJEClQscZdHHno8nFozqraJzppwzeUQTUc_i-dSrNpUyIYXQTGK83cYSD9ru6b34TLYublzDYmwfN-JAJdcef5nGxEb8YryfzzNNbSg==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvh4AyW5bqs7GbRbSJ2j-0fL12M_R4ssXjQ_3z7Spcm3fcXLSGQ0iNw_MJvTzyFOjIOyMLlUVE6Oo6TLO2ydy--VwWy1rMtKpVnTai8FQzD4DbzP_3kB6ALFa_HKHmTMOQjo0iOIbk4g==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_oaV7v2ii0wxW_9HdIeZK0Q9Quvu8vVqZSzPBpJeX0s4TnEd2pQ4QHHXsH-YIOYyBdLLkEB9JmCMxUtycxzsZGXfR9MdkSFGuMLR0X5gZOpVb52KhI5PN3bOoD0NdVnIgSHl5i70i1TydBBq1JnzhXKeJpTQU0QLu2axOSFaW_kyttWHuoRu44MCuTBzRQyBodUH3TUyIfFdetA==)
9. [siam.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlQ6iv1U_hHVYnx0TklTHpnUZqgi7DCQD57Jimk0O2WG9CEq273HZsAlSLoB0xH4uSrp-kVmBCJv6-y8fCyVkw1a_l3Y_MXgPn32Q40eQ3cloOi8X7_VKCla4HZMQH8vqDvyk=)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2WrE3TDnr1DRHP1zjm0XWHRbDr_yK3MyYLRvTNf5Y8usulnSxXorp9fgDrHU4AjY9nnL0gUtgnxTqd0GCUBz-lNgGX24bGyr04kjUKxcVyGDDKvjHpVjcx03uuD0fNg==)
11. [ncsu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-FD7fzn33qMdofCCh8757etNrg5TbZdGAFLfLCu4066U-VuOGwkwrFT4T7xocdyFWcjDnrdxyPukp0VtvOgUVbBZGUPmygC1e952IhI5G0wiR41wH4NdKJxq4bnxWntbn2eP61TOIRsZruQUNYS-HgaJp2-hsMAW5NaN3LsRd8Eb0p3raHNoArc-s_fhX)
12. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFVPL1pia1A5HwRwz4DXkw5Ytw-vYDa8Bims0uU94aO58th6OqkY73aXe0fjgF3Vy1eLjWI446LO6RtFVatc0wGu59TQwTwv7dB0jcTrf5xmY_TE96)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhHWpu5coTz1ilhbrDn1V3hyYBkER9hE7ip8YFYVVnEWUjeeKcgT7KM0th1exgY45-5UwS2199L7tnKDV4F2O9rxcD1xu0LXIuOIk7EoiBD1UoGGYf-MSSNSfJhK0WjF9qAxPXyZrfFT7jTAeRr9dFk4aTBOtGsYRRdDhcyD6he67S8c83JkOxLL3s0EhHhHBY0fPmrskX5AvvmVDqbMvzBEkYft6q9sOpgW-PdUwT)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl3QztKggXjRrSwb4eMivl0ns7x7EeXbPTKFevtTFIkCOrV6j5P-cSTnz1GCLaA4O-_jMmuSu6n8sbnDAx2wMvLowFHhvfCPdK-ny0_XAN2KKwEjg5MnkB2HtepVY-)
15. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuLtFAu1uBy4LOswrGWdsPvGcWd2BeiV51wtDIUsKudE2y2vR0EjzrJZy0_15Yt2Of5xl0MaMqy0CI1I2550PzqbLfdMvbPghvwyCiV3tLW_s9r3RXY7E0KF0FICYpaHYlU6VJqtY=)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzZ5QgzQnot8-qylUbkLuM-CS1VrGvgoaCQe9aCmryufzNVT8GzUzDvF8LiOxjJwHoDlbfLKfx4-cE7AWbfC3kOl3fqwQk6JBH1pwbgapmkhTYOME_4mP6z94X9Ts=)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZMWEs8g99GCdLzOYVjwowYQ20fLo4e5hp-5uw9z_5Eyr7gkx0M8cQTKwd7WrjbF2Y2NSTw5VIxjagvwi84Vrbq6U_awEU93fy553E5d-oiOL-vj8ztqrLozicT7Cbng6BWa2wSEtv)
18. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEP1XpXIkykIM2sMCUL7g5HCq6z9WicfeowOkSAbyJb4WueF6PCxdmQr6Sl8e-BznTIY7Mu1AS_7wFcxGTy_VLhxIxSEaPDG-9_YstBtB4wEz-BQIiabYc7KkhVJq7KxBOXVfiJzLsneA7BRA1vhJ7AOks=)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvfUE4o1sDjsQ42EHtNGnwLeef-RKbH_LebtaJN-0fOKQWgmFURjHx2gPZoqbW1m_KXOdfY4nYzEWYtjGkc5vaWpQKBXZKWEjfP9KBK-0XSwbCHwVoCw==)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsbDYjtTisU1qklYlIeytU56gSJ0_t6z-dRK1ZICcTOzWdeZIseevCUf1mUWMzgqU6s6WTWFdE-paeM6Cp2UA9CZbMpDUtgA66ZU-F8WrX2SOSuvs65w==)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_sX-LnaFSKcQeEl4RaPWprz9WtL72uagJB4tvVYHBA_toWDP09B1g4iUYhbdfDaPUwA0fW1N3culizTymfId0sKxIyi8tAsXJyOYBT9g7vhpHidJiTw==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs4fnJ7P-OsiXRNbI7JD86UobKpBcFrK160UICcIn7m49IYTAC-oHS_7XURe8iWZMf549KizFlkM5ITNIWeib4IMH2BXDMGQ7I21sNtLaw5KpDj0gs6HLJ0VMFHS_-Qci5e7ffYe2qCq1OmhSSsZb970uJzKzvfvRXgqKzlW-ehQ0dxls2yR3vS4uytOh11OOQhN0tqV5x6ZwWx41j5KwRnWNlR69sF9woC9n_Fr6HOkWgXDg=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVOWnvbnnWGp674RUjnF2tZvHWDTbm8OKMPFDL1eSus1vpRHYu3zNTLKjHq_5R_LehOiOBbcBZK0IQ_blT2vCvWAf1CMZLKFrevHpg7OOTfzYbtSU8HcQYwBkrR2P3lAyRrPZOEGWjpaXM3K5I2fjFzrT9-2E8AUZM2CNZoGTZdX5crnoqObtXVWhxqGr7ntFqeAEJuXc22Uet)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaaKTPsfGTxAtDOSoS4FcZo921JF_d2jKWQ_lhrISDHfdIdkcOXHXeb3kYytXjoWKP8Y_DzocBVn8XhwEhGx8_DZgdhUUHKgsWejcWNQxGQE0_KMzPh8DaE2zeRYg=)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMpqsVXo00LN02JMyfdB34hZPXzEx2WF8f015eix5Nyqfxzd7uMWXxYAxlGtWq8O3LXZ-9K3UEmfIZwu1nzsjgAIhCqHXGhnD5FF5SufEU_Y-aFWO6eA==)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU4qV84RzkC3NF9ikM0rnAQgfg0ICcxxfTQMsRmIZ2SSe3zJFbHgc1eOgNrSi5QIA7KN2TV0b_y4S9A0TntoT4UGVxFfDTeby72Lo_aobx2jbV_BStLg==)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUvN2j-mmfqK_ZZn92rAo1gxn5C3hWuDPYqXEMNWMR9is0k9zObQ6F0_XTdGNMfKg-WKUtopg7UHn1T2zvqq8fl91GG-Pt-ai58xByj2wa_gumVs2U3pqYvDVry-Y=)
28. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ETTIpbv0iW4Of1NJfK5tv5XgdsuNmwIaoGDRiC9GnZ1BuuVzEfcYKrXPK8HD6zgAdB4fm71sOq_6HpuTVpS2YGTZHZ3E-RQx5AHVolq2LNfmz2HHZoCRanJyctVqNg==)
29. [ryerson.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG_e8Q93PzhuJuoCYV57Dto6IfgmBgNnmInCnhUzAd3T9o8LRXXJqjGviPlJu6dMdY8IjE4xsmn7l_STEE00Bl-jUTvLFiEXO_4zhd51PEUR7rLm6ghZCdHUjnSEBjl4x5tNmhSgTsoUWLXYefWJf-mqXT)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz0ZY7X324IIEw-ECbSDEw9m1jO2BV_89V6mKAOI_t0aQD0HFeZXqRc4qBPR6r9bAmA4KosjhclDtXcsJqNMJziXgZgqvxKG6OO2mLWUTs761CNrvzbOw=)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9Zajl4BB0Sr-EypmcTRbjILGlZzKGBtqJRw3GfBADJHfqt4vj6_UxJsx8tEjmxLo0kLKRC5wYe87cNWOU3gZJkneC9fy3DTFDTahe47sYvLFv-VBzPw==)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAfMwu-x91wcNKQ9GACn9z8vvtq36ovNGJkXvSUsHnDu3R5TagCN4T5fJKrEiilTKdeahgBuJKPyI8b42Ulv45u2IBWHuxU6L5rdDBk-UHOXrhMOoeeyBfxg==)
33. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIoXGlEDroWQmxOgCLqfolc4X5hy58BYevfIQAHx69McvRbIokMZ5HrCtqBxZugitKp1z64sWCsKJJuP3QW_VtQIetqQbYqJg23TGmwG103hPG8Gga6LU8xtM_Jk2uQT6ygIcvst-zdXLh2BINX_W4FJN5P75bw5Syta-sjaAvO3wV5BWhawsxlEc559nlUFq4O9U37gGJ)
34. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLcv3930Q3nanCIJ82Vanb4WZnhlkRVzj1LVWPEdIeFFSdXBYZUQDuD4-a52rZ_QTS1PXrgmsCKNSiGk3D68ox2Tpk_KcHcXhkXluXeYrKtZ37ADu-xHcJaC823xsJu8HAWUP6VrSlCc3HDjphN8K34L8WSHHPGhzIrHg=)
35. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBn1bDtF6O9PWAPYhzTFuqfLFP57WNOuyLe36oE8LgKxmaCxmk_GsCboK1XsN09f9ralc-FTE2Ql9vPmOLRY-NDKlez9oRGV8RTkMSshfcTSY6h6GM3yo4XCql-pF76cG-AV7ti8X5qb20RDvoUJGkcGHwSpch9jfhJZdPkBaj)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi-dHpm-PgzCPrsqntXxpy57YoExPOlMmMuykJ49lOkXGuw2jGO81Cy5UTqYEy0tyIvY5RWav78Si8k_excVPoq0N9pOeGNh78Hd46XreTKaL9Uc2wfYHZ2SiBRvfq3kxRT4QN--tO)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMaEfo2LaFPIxyA2quEyfh1DTwSBl9ERFaibKrt1AeZ0eMcv-QaQrc_6so-K7gsKofo3XKzzTRFloZQ0KgMY6ndkKOFAZfpqlK15iPYiQE0oYcjPiQWZVdw9Yo-rR9kI4pw1NzhrRLaA==)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVQkmSiBx9so4Q7HnO5O545iIItzGnkgtvUCfDLw8cXy2XDVG1iSE0dPUA2URpNIhdotiZ2mr_Q389uBD_ffxt3vAFN6YW3guDU1uKia-1CJduDdKAyDVUhwspHVczCtQR5Rj7hp0DGK2x_ChBYwvs8WBD4H9Wk-nqML8G3oEPG_pUkNvowCpXmG9J4D2BewtQs31w7u4uGAH8mc7wjnxeUV9sB51zLK-E9NVqOKBFNwEN4q7hVQj2dAOimM7sJZ3K11g36IJjmPdM4nbeujAW2jbRIX7uZg6bYQUsMNfsVV68EnSgk5238U3KgOqWQorStSd46Hqu6d4gBw==)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm1wvKdasiLFvTO45jeT0pNnAczg5KDPDSUszSvajYWD6DBjFtI9iwT-rw9vi0ItQNoLQcklXlIOzyxCdstIGM5Z9FLZ3MgPjcoqLueB3AHnVNCLW91cekbi91j5E16Qs=)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm1mVJ-WlDo9qcAq9L2mPOdpsm_lLVp7pov5ArHYjarUTCf-EcGWUwVUzaw36VvCLisLlVfZjx_d4BCaPUELQiJZhvUtAHkS7tYLGK7GgmRX3VO1faww==)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESw3Q-BcCq1Ag35IH6gmvjx0ffwuIlJrtUh0jq0hndQQNLjT53Avi4SGKC12BP_ie7gOIpnzl4IDj2S0UuWteLMtqbLvfcKpQ-4xC3mxdk4gWJCzIxSbV_YKyrZNn54VVnQiIVA-F-MwgBTFIVi6qnDD0ITiomGx7PjGAb2PSKmiF5KTh5MAUu80Io2DHq6c9Yb9VF-YBeDCLlATw4-HMJznRPbdUeFVBX09OkMtgm8i4IU26i)
42. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1YhorKLAkMJcEYfdeQg-1XksDFFJl4NrLlqLiCPvpY5K5D4BGYBmPUjjcuHLzmm1PUH72tB5erN6UTDiva-DT_Pd_VbYvnZiDZgoDV9rDef3AP8JEsA==)
43. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3miiMWnbbxOyllhFoZ0s571WPVH22KEn_o4m5x7xkcoc_QkeBDQ_tyPmt_KzIu_fA1fTd5T2ShBfXhP_vvrDbM9YFn9ZpLlNqNrw6gj47ioUnObP2kA==)
44. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3JFvYnPDsQPYS77ZQaSDmZvJqh_iAZ8PnE937h9oxpKbcl9AK2VQ84C0PZVaaieyLK2w-NTTW14bP0j9f6jjuj6AbJlQtXuEWN5C8ndyhhCkib1DHkhHiYKzOn49nlA==)
45. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLNlRYp-AXn-iW_viy-Zmo8LvNMaSBDAt6mKNohJfrPta_i_KZWQK2ThjFa0BCFllrQSd6doQdbn-aGhyrsUd91qIxn9U4W8WhbwwR77FgS6CVWSU9Gl8hgOk0zHU2DaGFDXBcaY0wQxTy8VxvJ3oiv9RYBOe1lZE5GoV4wVlPAi-i04C77dHkYHCdc5lpVT5ZGygBca6hL_Pd7XqFhMUiAwCzju7qNbcG)
46. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIXJQL7I6s1HGbf3aGs8CxXyDk4swIvhs6-GfemrkOMtrKLRKcDvsGglcrESit2Mn-JeuLJoAvNLeboaHg4P8HHXElAgIeC_RH2Wrhbd-GK0GpPBTwSDxPHjtkw1YFkjFO)
47. [ijcai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC5nzzAwTflFhAiUmq2P5s1xGOSfIVFyUhEIqSspfYtrmTte9SE2taGWmWy9TX9OPOCsCQUe8BNnD3TDV8QEHC9C2hpYGISEkqFJGwNXk4Kh94Bee69Vel2v-nAT3FZKC8lGwwFw==)
48. [ijcai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGurPsLpRXMb5Uakf-7QLElH1uPhL8TQwnHqoON1Iqb8ae3ZCHNLqiHZ2R0E10XUxqZqhWRCNUo-jn4UuUFMPcUQVN3Wn8rBqUmG5nswqOy-N-IQe97OfPUNm8s6MvO7dk=)
