# Literature Review: The multi-modal fusion in visual question answering- a review of attention mechanisms.

*Generated on: 2025-12-26 22:05:00*
*Progress: [36/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/The_multi-modal_fusion_in_visual_question_answering-_a_revie_20251226_220500.md*
---

# Multi-Modal Fusion in Visual Question Answering: A Systematic Review of Attention Mechanisms

**Abstract**
Visual Question Answering (VQA) represents a quintessential multi-modal artificial intelligence task, requiring the synergistic processing of visual data (images/videos) and textual data (natural language questions) to generate accurate answers. The core challenge in VQA lies in the effective fusion of these heterogeneous modalities. While early approaches relied on simple concatenation or element-wise operations, the field has been revolutionized by attention mechanisms. This paper provides a comprehensive systematic literature review of attention-based multi-modal fusion in VQA. We trace the evolution from early spatial and channel-wise attention to bilinear pooling techniques (MUTAN, MFB), co-attention networks (BAN, MCAN), and graph-based reasoning (ReGAT). Furthermore, we critically analyze the paradigm shift toward Transformer-based architectures, examining state-of-the-art foundation models such as BEiT-3, Flamingo, and BLIP-2. We also explore domain-specific applications in medical and remote sensing VQA, discuss explainability via attention maps, and identify open challenges regarding computational efficiency and neuro-symbolic reasoning.

---

## 1. Introduction

Visual Question Answering (VQA) is a testbed for evaluating an AI system's ability to understand and reason about the world across modalities. Formally, given an image $I$ and a natural language question $Q$, the system must predict an answer $A$ [cite: 1, 2]. This task transcends simple object recognition or text classification; it requires a fine-grained semantic understanding of visual content, linguistic syntax, and, crucially, the alignment between the two [cite: 3, 4].

The fundamental bottleneck in VQA is **multi-modal fusion**—the mechanism by which visual features (typically from Convolutional Neural Networks or Vision Transformers) and textual features (from Recurrent Neural Networks or Transformers) are integrated into a joint representation [cite: 2, 5]. Early methods utilized "shallow" fusion techniques such as element-wise multiplication or concatenation, which often failed to capture complex, high-order interactions between specific image regions and question words [cite: 6, 7].

The introduction of **attention mechanisms** marked a pivotal turning point. Inspired by human cognitive processes, attention allows models to dynamically weigh the importance of different input features—focusing on specific image regions ("where to look") or question segments ("what to listen to") [cite: 8, 9]. This review systematically categorizes and analyzes these mechanisms, ranging from early spatial attention to the sophisticated Querying Transformers (Q-Formers) used in modern Large Vision-Language Models (LVLMs).

---

## 2. Key Concepts and Definitions

### 2.1 The VQA Formulation
VQA is typically modeled as a classification problem (selecting an answer from a candidate set) or a generation problem (producing free-form text). The process generally involves three stages:
1.  **Image Featurization:** Extracting features $V$ using backbones like VGG, ResNet, or ViT [cite: 1, 3].
2.  **Question Featurization:** Encoding the question $Q$ using LSTM, GRU, or BERT [cite: 3, 10].
3.  **Fusion and Reasoning:** Combining $V$ and $Q$ to predict $A$. This is where attention mechanisms operate [cite: 2].

### 2.2 Taxonomy of Attention
Attention in VQA can be broadly categorized into:
*   **Visual Attention:** Assigning weights to spatial grid features or object proposals based on the question context [cite: 1, 11].
*   **Textual Attention:** Weighing specific words in the question that are most relevant to the visual content [cite: 8].
*   **Co-Attention:** Jointly learning attention weights for both image and question simultaneously, often in a hierarchical or dense manner [cite: 4, 12].
*   **Self-Attention:** A mechanism (popularized by Transformers) where elements within a single modality attend to each other to capture global dependencies [cite: 13, 14].

---

## 3. Historical Development: From Spatial Attention to Bilinear Pooling

### 3.1 Spatial and Channel-Wise Attention
Initial attention models in VQA focused on **spatial attention**. Instead of using a global image vector, these models generated a probability map over the spatial grid of the CNN output, allowing the model to focus on relevant regions (e.g., a specific dog) when asked a question (e.g., "What color is the dog?") [cite: 1, 9].

However, spatial attention alone ignores the fact that CNN features are also distributed across channels (filters). **SCA-CNN (Spatial and Channel-wise Attention CNN)** introduced the concept of attending to specific channels (semantic attributes) in addition to spatial locations. This multi-layer attention mechanism allowed the model to select *what* features to look for (channel) and *where* to look for them (spatial) [cite: 11, 15].

### 3.2 Bilinear Pooling and Tucker Decomposition
A significant limitation of simple fusion (e.g., element-wise product) is its inability to model complex multiplicative interactions between modalities. **Bilinear pooling** addresses this by calculating the outer product of visual and textual vectors, capturing all pairwise interactions. However, the full outer product results in prohibitively high dimensionality [cite: 7, 16].

Several efficient approximations were developed:
*   **MCB (Multimodal Compact Bilinear pooling):** Used Count Sketch projection to approximate the outer product in lower dimensions [cite: 7, 17].
*   **MLB (Multimodal Low-rank Bilinear pooling):** Used Hadamard products with low-rank constraints [cite: 7].
*   **MUTAN (Multimodal Tucker Fusion):** A major milestone that applied **Tucker decomposition** to the interaction tensor. MUTAN factorized the massive bilinear tensor into a core tensor and factor matrices, allowing for a parameter-efficient model that could learn rich, high-order interactions [cite: 7, 18].
*   **MFB (Multimodal Factorized Bilinear pooling):** Further refined this by factorizing the projection matrices, becoming a standard benchmark, particularly in medical VQA [cite: 19, 20].

### 3.3 Co-Attention and Dense Interactions
Moving beyond attending to one modality conditioned on the other, **Co-Attention** mechanisms treat vision and language symmetrically.
*   **Hierarchical Co-Attention (HieCoAtt):** Proposed attending to the image and question at three levels: word, phrase, and sentence. This allowed the model to reason about the question hierarchy (e.g., "red object" vs. "red ball") [cite: 8, 12].
*   **BAN (Bilinear Attention Networks):** Combined bilinear pooling with co-attention. BAN considers every pair of question words and image regions, utilizing a bilinear attention map to seamlessly fuse information. It significantly outperformed previous methods by capturing dense interactions [cite: 4, 21, 22].
*   **MCAN (Deep Modular Co-Attention Networks):** Addressed the depth limitation of previous models. MCAN consists of deep cascades of Modular Co-Attention (MCA) layers, which model self-attention (within modality) and guided-attention (across modalities). This architecture paved the way for Transformer-like deep fusion [cite: 4, 23].

### 3.4 Graph-Based Attention
Images are not just bags of objects; they contain structured relationships. **ReGAT (Relation-aware Graph Attention Network)** encodes the image as a graph where objects are nodes and relationships are edges. It models two types of relations:
1.  **Explicit Relations:** Geometric positions and semantic interactions (e.g., "man holding cup").
2.  **Implicit Relations:** Hidden dynamics captured via a graph attention mechanism.
ReGAT demonstrated that modeling inter-object dynamics is crucial for answering semantically complicated questions [cite: 24, 25].

---

## 4. Current State-of-the-Art: Transformers and Foundation Models

The advent of the Transformer architecture shifted the paradigm from specialized attention modules to unified, large-scale pre-trained models.

### 4.1 Early Vision-Language Transformers
Models like **VisualBERT**, **ViLBERT**, and **LXMERT** adapted the BERT architecture for VQA.
*   **VisualBERT** treats image regions (from an object detector) as visual tokens, feeding them alongside text tokens into a single Transformer stack. This allows self-attention to implicitly align text and image elements [cite: 26].
*   **LXMERT** and **ViLBERT** employ a dual-stream architecture with specific cross-modality attention layers to fuse information from separate vision and language encoders [cite: 27, 28].

### 4.2 Unified Foundation Models: BEiT-3
**BEiT-3** represents a convergence of vision and language modeling, often termed "Image as a Foreign Language." It utilizes **Multiway Transformers**, a modular architecture that enables both deep fusion and modality-specific encoding.
*   **Mechanism:** The model uses a shared self-attention module across modalities but routes tokens to different feed-forward networks (experts) depending on whether they are visual or textual.
*   **Impact:** This allows the model to be fine-tuned as a fusion encoder for VQA, achieving state-of-the-art performance by treating image patches and text tokens in a unified masked modeling framework [cite: 29, 30, 31].

### 4.3 Generative and Few-Shot Models: Flamingo and BLIP-2
Recent advancements focus on leveraging frozen, pre-trained Large Language Models (LLMs) and Vision Encoders, bridging them with lightweight, trainable attention modules.

*   **Flamingo:** Designed for few-shot learning, Flamingo keeps the vision encoder and LLM frozen. It introduces the **Perceiver Resampler**, an attention module that converts a variable number of visual features (from images or video) into a fixed number of visual tokens. These tokens condition the LLM via **Gated Cross-Attention** layers interleaved within the LLM, allowing the model to generate answers based on visual context without retraining the backbone [cite: 32, 33, 34].

*   **BLIP-2 (Bootstrapping Language-Image Pre-training):** BLIP-2 addresses the computational cost of end-to-end training. It introduces the **Q-Former (Querying Transformer)**, a lightweight module initialized with learnable query embeddings.
    *   **Mechanism:** The Q-Former interacts with the frozen image encoder via cross-attention and the text via self-attention. It acts as an information bottleneck, extracting only the visual features most relevant to the text before feeding them into a frozen LLM.
    *   **Significance:** This architecture decouples the vision and language scaling, allowing state-of-the-art VQA performance with significantly fewer trainable parameters [cite: 35, 36, 37, 38].

*   **PaLI (Pathways Language and Image):** PaLI scales both the vision (ViT) and language components (Encoder-Decoder) to billions of parameters. It treats VQA as a generative text task, leveraging massive multi-lingual pre-training on the WebLI dataset [cite: 39, 40, 41].

---

## 5. Applications and Case Studies

### 5.1 Medical VQA (Med-VQA)
Medical VQA faces unique challenges: data scarcity, high class imbalance, and the need for precise anatomical understanding.
*   **Dominance of Bilinear Pooling:** Unlike general VQA where Transformers dominate, **MFB (Multimodal Factorized Bilinear pooling)** remains highly effective and popular in Med-VQA due to its efficiency with smaller datasets [cite: 19, 20, 42].
*   **Attention to Regions:** Recent works emphasize localized attention to answer questions about specific anomalies or regions of interest, often outperforming global feature models [cite: 43].
*   **OMniBAN:** A recent innovation, the Orthogonal Multi-head Bilinear Attention Network, combines bilinear attention with orthogonality constraints to improve efficiency in medical contexts [cite: 44].

### 5.2 Remote Sensing VQA (RSVQA)
RSVQA involves analyzing satellite or aerial imagery, which differs significantly from natural images due to scale, rotation, and object density.
*   **MADNet (Mask-based Dual-stream feature mutual Attention Network):** This model addresses inter-class interference in remote sensing. It uses a dual-stream feature extraction (global and local) and a mask-based attention mechanism to filter irrelevant answers and focus on specific land-cover types [cite: 45, 46].
*   **Segmentation-Guided Attention:** Recent approaches embed segmentation maps into the attention pipeline to provide contextual understanding of specific objects (e.g., buildings, roads) in high-resolution orthophotos [cite: 47, 48].

---

## 6. Challenges and Open Problems

### 6.1 Explainability and Trustworthiness
While attention maps are often cited as explanations ("The model looked at the dog"), research indicates they do not always correlate with the reasoning process. **VQA-HAT** and **VQA-X** are datasets designed to evaluate this by comparing human attention maps with model attention. There is a "black box" problem where models may predict the correct answer based on language biases (e.g., answering "white" for "What color..." questions regardless of the image) rather than visual evidence [cite: 49, 50, 51].

### 6.2 Computational Complexity
The shift toward Transformers and Bilinear Attention Networks has increased computational costs.
*   **Bilinear Complexity:** Full bilinear interactions are computationally expensive ($O(n^2)$), necessitating factorized approximations like MUTAN or MFB [cite: 7, 16].
*   **Transformer Scaling:** Models like PaLI and Flamingo require massive resources for pre-training. Efficient adaptation methods (like BLIP-2's Q-Former) are attempts to mitigate this, but inference on edge devices remains a challenge [cite: 35, 52].

### 6.3 Neuro-Symbolic Reasoning
Deep learning models struggle with multi-step logic and counting. **Neuro-symbolic** approaches (e.g., on the CLEVR dataset) attempt to combine the perception power of neural networks with the reasoning rigor of symbolic logic (e.g., scene graphs, logic programs). Integrating these explicitly into large-scale attention models remains an open research area [cite: 53, 54, 55].

---

## 7. Future Research Directions

1.  **Efficient Multi-Modal Fusion:** Continued development of lightweight fusion modules like the Q-Former and Perceiver Resampler to enable VQA on consumer hardware [cite: 35, 52].
2.  **Neuro-Symbolic Integration:** Hybridizing Large Vision-Language Models with symbolic reasoning engines to improve consistency, counting, and logic-based VQA [cite: 56, 57].
3.  **Generalized Foundation Models:** Moving toward "One Model for All" (like BEiT-3 and PaLI) that can handle VQA, captioning, and retrieval across multiple languages and domains without task-specific fine-tuning [cite: 29, 39].
4.  **Reduced Hallucination:** Improving grounding mechanisms to ensure answers are strictly derived from visual evidence rather than language priors, potentially via reinforcement learning or better calibration of attention weights [cite: 50, 58].

---

## 8. Conclusion

The field of Visual Question Answering has evolved from simple feature concatenation to sophisticated, attention-driven architectures. The trajectory of research highlights a consistent drive toward deeper, more dense interactions between modalities. **Bilinear pooling methods** (MUTAN, MFB) solved the dimensionality issues of early fusion, while **Co-Attention networks** (BAN, MCAN) enabled symmetric reasoning. The current era is defined by **Transformers** (BEiT-3, BLIP-2, Flamingo), which leverage massive pre-training and learnable query mechanisms to achieve human-level performance on benchmarks. However, as models grow in complexity, the focus must return to efficiency, explainability, and robust reasoning to bridge the gap between academic benchmarks and real-world utility in critical domains like medicine and remote sensing.

---

## References

[cite: 1] Tips and Tricks for Visual Question Answering: Learnings from the 2017 Challenge. [cite: 1]
[cite: 10] Taxonomy of attention models in VQA. [cite: 10]
[cite: 12] Visual Question Answering with Hierarchical Question-Image Co-Attention. [cite: 12]
[cite: 8] Hierarchical Question-Image Co-Attention for Visual Question Answering. [cite: 8]
[cite: 5] Visual Question Answering (VQA) is a significant cross-disciplinary issue. [cite: 5]
[cite: 2] Visual Question Answering (VQA) is a significant cross-disciplinary issue. [cite: 2]
[cite: 59] Visual question answering has been introduced in RS. [cite: 59]
[cite: 3] Visual Question Answering: From Early Developments to Recent Advances - A Survey. [cite: 3]
[cite: 13] Attention (machine learning). [cite: 13]
[cite: 9] A Survey of Visual Attention Mechanisms in Deep Learning. [cite: 9]
[cite: 14] From Multi-Head to Latent Attention: The Evolution of Attention Mechanisms. [cite: 14]
[cite: 6] The initial model for VQA employed deep convolutional neural networks. [cite: 6]
[cite: 60] Learning Visual Question Answering by Bootstrapping Hard Attention. [cite: 60]
[cite: 11] SCA-CNN: Spatial and Channel-wise Attention in Convolutional Neural Networks. [cite: 11]
[cite: 15] Channel and Spatial Attention. [cite: 15]
[cite: 24] Relation-aware Graph Attention Network for Visual Question Answering. [cite: 24]
[cite: 25] Relation-Aware Graph Attention Network for Visual Question Answering. [cite: 25]
[cite: 4] Deep Modular Co-Attention Networks for Visual Question Answering. [cite: 4]
[cite: 61] An effective Dense Co-attention Networks (DCAN) for the VQA task. [cite: 61]
[cite: 62] Dense Co-Attention Networks (DCAN). [cite: 62]
[cite: 23] Deep Modular Co-Attention Network (MCAN). [cite: 23]
[cite: 27] To address the task of VQA grounding in transformer-based architectures. [cite: 27]
[cite: 26] VisualBERT: A Simple and Performant Baseline for Vision and Language. [cite: 26]
[cite: 28] Results of performance for the three VQA models-ViLT, ViLBERT, and LXMERT. [cite: 28]
[cite: 7] MUTAN: Multimodal Tucker Fusion for Visual Question Answering. [cite: 7]
[cite: 53] A Survey of Neurosymbolic Visual Reasoning with Scene Graphs. [cite: 53]
[cite: 54] A Survey of Neurosymbolic Visual Reasoning with Scene Graphs. [cite: 54]
[cite: 56] Neuro-Symbolic Visual Graph Question Answering with LLMs. [cite: 56]
[cite: 55] A Neuro-Symbolic ASP Pipeline for Visual Question Answering. [cite: 55]
[cite: 57] A neuro-symbolic ASP pipeline for visual question answering. [cite: 57]
[cite: 32] Flamingo Simulation Variant. [cite: 32]
[cite: 33] DeepMind Flamingo: A Visual Language Model for Few-Shot Learning. [cite: 33]
[cite: 34] Flamingo Intuitively and Exhaustively Explained. [cite: 34]
[cite: 63] Understanding Flamingo Visual Language Models. [cite: 63]
[cite: 39] PaLI: Pathways Language and Image model. [cite: 39]
[cite: 40] PaLI: A Jointly-Scaled Multilingual Language-Image Model. [cite: 40]
[cite: 64] PaLI-X: Scaling up. [cite: 64]
[cite: 41] PaLI: A Jointly-Scaled Multilingual Language-Image Model. [cite: 41]
[cite: 45] Enhancing Remote Sensing Visual Question Answering: A Mask-Based Dual-Stream Feature Mutual Attention Network. [cite: 45]
[cite: 47] Visual Question Answering for Remote Sensing (RSVQA). [cite: 47]
[cite: 48] Segmentation-guided Attention for Visual Question Answering from Remote Sensing Images. [cite: 48]
[cite: 65] Medical Visual Question Answering: A Review. [cite: 65]
[cite: 66] Medical Visual Question Answering. [cite: 66]
[cite: 42] Medical Visual Question Answering (MedVQA). [cite: 42]
[cite: 19] A Co-Attention Mechanism for Medical Visual Question Answering. [cite: 19]
[cite: 49] Explainable Visual Question Answering. [cite: 49]
[cite: 50] Guiding Visual Question Answering With Attention Priors. [cite: 50]
[cite: 51] Attention-map-guided visual explanations for deep neural networks. [cite: 51]
[cite: 35] BLIP-2: Bootstrapping Language-Image Pre-training. [cite: 35]
[cite: 36] BLIP-2: Bootstrapping Language-Image Pre-training. [cite: 36]
[cite: 37] Inside BLIP-2: How Queries Extract Meaning from Images. [cite: 37]
[cite: 38] BLIP-2: Bootstrapping Language-Image Pre-training. [cite: 38]
[cite: 29] Image as a Foreign Language: BEiT Pretraining. [cite: 29]
[cite: 30] Image as a Foreign Language: BEiT Pretraining. [cite: 30]
[cite: 31] Image as a Foreign Language: BEiT Pretraining. [cite: 31]
[cite: 24] Relation-Aware Graph Attention Network for Visual Question Answering. [cite: 24]
[cite: 25] Relation-Aware Graph Attention Network for Visual Question Answering. [cite: 25]
[cite: 7] MUTAN: Multimodal Tucker Fusion for Visual Question Answering. [cite: 7]
[cite: 16] Multimodal tucker fusion. [cite: 16]
[cite: 18] MUTAN: Multimodal Tucker Fusion for Visual Question Answering. [cite: 18]
[cite: 21] Hierarchical Question-Image Co-Attention for Visual Question Answering. [cite: 21]
[cite: 22] Bilinear Attention Networks. [cite: 22]
[cite: 17] Bilinear attention networks. [cite: 17]
[cite: 52] Flamingo: a Visual Language Model for Few-Shot Learning. [cite: 52]
[cite: 44] Efficient Bilinear Attention-based Fusion for Medical Visual Question Answering. [cite: 44]
[cite: 43] Medical Visual Question Answering. [cite: 43]
[cite: 45] Enhancing Remote Sensing Visual Question Answering: A Mask-Based Dual-Stream Feature Mutual Attention Network. [cite: 45]
[cite: 46] Enhancing Remote Sensing Visual Question Answering. [cite: 46]
[cite: 58] MADNet for RS VQA tasks. [cite: 58]
[cite: 20] Co-attention Mechanism with Multi-Modal Factorized Bilinear Pooling for Medical Image Question Answering. [cite: 20]
[cite: 67] A Co-Attention Mechanism for Medical Visual Question Answering. [cite: 67]

**Sources:**
1. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8C5ylXQcVG2kZCSdTmdDbfIxdwfiRChEjm8XrymBU43aRHYv3IXXpRfrwQCYc5gSIWxzkgPDcSWEI8bQpVOLuKyG7lDbNG9dLn2Uo2fzVwRLfFuvK2LxGwgWPIewU8Wl2LYYx7eGslfA4Qh_ffTqaclVt3_09ph-CKOjMhy1A-ocbQioaU8p0fb3moD_QGQ==)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCRNkF39f-zFyUqCd_PqeINoJdxBpN0NSma3kgNhI6vo-DAFspRKa5O0NaPd3I77_h1620J97l9m6k2axM5WrySz1e3M_9AAG65zqXH-38Je9A9a3El5f49eqDH2AqomA1W2p87VWVfg==)
3. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6IhS_BHL6i-LgbXkzEf9t78ZsuvXcZvQOecNQgHP9cxBdPbnoO7iBKOKzZlFbw7aHs8mzEZw5sqAWHs2vYZ6NKd-XUa8P5-YuNp0Sm21wWv5z-EJXDyRgmRKcimDJcRtxbO2n)
4. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgffwDedGybE0DYNsHrj-yNAfQB5GSnWxsenf_P7-Yv8apg7LTmlQhvtQgyuHkkD_8MqIOYHOppS66pGAwxT0D57AVMxhBNVikcNfjkrcq0bAM8yySY3eHJGZy1l1wtahMZuGgY1cRRuzKIYwE6f1uCg0t6egqXpd_pSBqavMN12ETrsu1WVdOdNHdJOzdLtAvzlBeAXVMRuHpsro6d-Cr94YSYHLNwQr8NPiOtJHm4kN4TffIJfQVrVqDdODkxolEWjYuQ==)
5. [scilit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPc6IeTRTrflY0NyzMiCMa0dpfb5knNWpV0R6Zyq-BpmEf6RfoU3uyQsfbSi5gDDirpkcxfDcGiQ4pNt7VRmM8GgFlfBqcPGNnNfilD3RpP2v5VTr-qRzvShMtWfUFsuzbgRU1EnQU4DUkbY8QEzGnmVScgS8HttaRw==)
6. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5snoRzraNMOQY-y7a084-Iux5MkFCqp1NRDo_pPyVpDC3mPudRcpfyGPF9-mv5iN3x3hhD1i8TNzUGkQlGx-Hpba20G9QBrHidAWO-7SNxemNpJzXE5GeE__SdGzejTPk6wEjH4MhDmpWOjCWpQs=)
7. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFQoVCl_38Q9aXGZ3Ffe0sN-juvUImovaDkugU0pi7aJlfb6_xfch0p2ugI9sxjtG-0PlweYsdbNspU4VcmVmP8UUXT0Z1D6D7pBIKyJ3w5RUJWG93D3S2el5Aczqe8BmVZy1jO_KXBHDdw7WL5Y7qUawHQ6CIzrKHowbaOl4Dd-nV0L04XzHQjefNn7IBJTzt9oL_Wb38MjcPpXZd0gEpuJfB)
8. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNDePQJbwYzo3d8JaU7UBxl-w_4dOBRxb2UTy6VRsf3MwrSL5Bq1SB1PtzjOY1GvU8VbjjS1GB17vMw4rhdfiVsTs6196w_AiF9EaO2lHQI7tRnImwvqq9N1jrnzvc9kNjrdOKSUltTuGb9sZvPgztA_t1ESRTGby1YMw9lJs37jSK10mRPRQdEk7IjfkQAg==)
9. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Xu-KJt-f5p0rCD2zPr-UIqdiO5j_m1k7NJ80AIizW8DkbykBe6MnOdxY7cpqas-pFOebJL4TAx54zGy6g9hAhZRhOhFdP_LxJ9hfjym1wFW7PoxYhrYiUa_WDh-dUTFhHVTcQrprFbktOmGUjRSF4pAfaZNV8fKK4NUdLHiTdgLUVugjL22Q3WQ7YBeET7DKRhWmmsV5zgXdazc=)
10. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbgqr6swy2DLAdRoOa-AvNoFnlljsLUx1YhbqN8wM2u7TiPfcKOYpXWfiGU4I0DS0RougSdm-_mR8fXTphCWfbNJDN6LynDhi9mmGE6O88msuNsCQH6GOFhgrLWOUChGWho7TlpfNURcF-wNzLyOOLej5_IvbAx7mxRnBNLfFNbiUEgkl_fQ==)
11. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb2AF5ceJxixdE6i9a9QYXoZcpdeSjN3hHKaReXJWVmN7MGwhQSwnx2jm6yDUPlf6qtdPqWcu2F5PAvth1bJigX_XGZKuuWyqx2DLXZLNS-Vy0W35VMsKy2Ge4Q8vxIDW_4-neYjvPuZvn6ETVOhg3mPRoGHzkv1X7cwOGk3knjI_NY-8sX-m9XZ5MVwSn4MR8Q8c1ZVrj8D8=)
12. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyEbfnznED5MH6LP_sTYJkKnWFs9sLAW6bUF2v08Yxm0457nKfpL96M_U7Os_Vs8KPIn3U_7Kgu_4tYHB-1sGqdCR9rWsJESjrzIlSfikbIgUd7xn__F8UZtKSPxDe6VqAT7T58NAhWxJQg8Vod-5wqNGzPFwQiVaCCWLba4bLW4FIBtb5DMcIMHmAUHIjVCfuZrb2d3eaTYv27DPcbTmE6yZ4LdU23nCK8zuPdLj2Ql06ig==)
13. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhCgPEreEFmxvSkgLVGnRcJngwsxQqx1hbZCAEX9c3WVVUlNBe7Mk4gNsZaW0IQ6Hq3SHSJfmRPZ0nOEW-p_hP96QzfbVYAH38a5M3_d9d2mKyDdVJb554aScV-n-g_WlUcDiBHOVhNordeA_drnYC)
14. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Mrm7zgpmZ_P4QUpFJgna_nDrVvlOdsAGQvn4iRFXpLDTzG8-J9AxNpKa2uAuDJcZ1dp1uuEGSQlsVTIIzYXbCVskLpgGBef_wrlzBr25TB_UNGKNhEmQ8i1QwyQg7lppoO6GbFEsqGp3SCG8eB9qNJFgw-F6EE33MZ9MJ0CbJfY3s83x83wtqetQ_c2JOcPzcp047Y-z83HHcA3WFzmEGj8L7Kkw5WBn)
15. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-mx3wLgKx5MQWdEYmgb2Oz55-P469bI2o7wEjdPPJgpsMrC_iYr77RY17qnEPzZ0zhIefDah8CIAZm9S5MF9Nt_vEZrFBzeJGozwl23ydYGtNxu0RX82qCywaO0znXcLNJZ1wmno8cHwzZrB3zYM9AnMN8FBfv99T2O3shg==)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG34uvPTELRr4b1lv-1AytgNigcRPCfub4I2q5xEHRCk1cww-VL3s8AhYyZvvtgBG7J7skBTZCB8bpg4wO1w1vMk_bNrvTycb_nX5qCY3eIM0Xgy7iQAUqOTGynYPaJN1CBQfMiVwSE)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDGUHm4KB98py90jF8VDAarUDbyO315VuCtu0bT5XYPNK3lAm6WHO9lioMa3Hu2lpNHRA58VdTT85HhUxr3VGuHFZX_qWZ2c4wBa8YQc7zpkp8lG2zsOgz4dnmhfcI9Y74jKhnz0iRHw==)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNyg9oSTA9_YL_EbFFEOqt6FeFiAd-KU32Djyz08DCiYfsZ8TJh2P4uSHyNwLka_mNtftrUHKgVoU0CfatRYprp7U1hllZX7uoInx06mItCuFrF7-ZPoVkSmF1O_H8lcZRMKIZ6vEQ2Ve_svuj_zVldkFEYWOdg44OtMxfWTR6pt_ARSdzkEakGWAP3ZlSSewHnPvRwNSeDRnY-v2Xkwyojtav39E=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWevJOiKMhq3hsdJfGGt_DT2MueTxgDgvzAbloZ821SLJpNgn1YJZmM8xOYMwjndtZS0eRR7FfcTJScxjyyrAgifjvopksfEyjkYEDgB3db0LZ1vQ1pnkdccOVU-7p8quWgVrQsBFFKJ4Sdh8cSG_ajJswhSHhEYiwiBHCDKg_q8U_4EXOPNUzOlY_J80czz1btj8x6Ik9QIXCLfUquQ4KBiMtQss03-0fRVVrL3FI9-dPLahpzp53nUk1CDJcy3sYOuYK)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGDka5EgK0Axvz2lYzUObTQZro12AHhy2zoV5jii-33iK-pOrikKh_6iV-1KvpPCmTM40GjIG6sW0O6bmLsiY-H9ZB9la7gJnCn34JJBmdvd2p2eGUJS0BTlT5X3R6ckUVTwq9USvhJCwjgTFixUv0u5nscP7V7TQ6anjEvuTvrqXqy0zox-vYJTUfSePqwQl4mdqZh_jBkzeYZYmYMwLHsYBQ4K8Xxys3Z442FD9s7R54KQ8eZ1sgBIyCKjxi5Jl-RNjIceEmsgdpyF_fFexNYbo=)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTYoXg4exUnqhU42Ji-vo1qpD2-6_6IbW5f5AuKTUKjWn4b-hazQTCAg9SJL6TEFfhzZT4D6igwrZU8JNJhSCp4h5m6IIUyA2JzWO7Hfl1W8TLiUUmPQ==)
22. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7hO_wPIpzZRIJI8lOULGjwIiZzsiQ50FYXpFVdKGVMmy4Vc3kjf2k5GOj_DRQQWJisWTGxDncWms8QVriwHaw76k6zNuoCtykUBXERHKxi0dl0c2yJru2jusU9MPxyZTA2Mt-qiLwBws8ZgJiPnm6nIQvmhIKv14_W947DaTu3b551aK5axTbLYe-s-4HvcotUEev1SvYUpJ_X2RED_L7ltgmR9eFIv4=)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLuKI4vtaKunXPAkvO3E_zOoW5JzqPx8SB5KaKpcfidlgXFnZDJNHmVQy-VVudNmaUls3ZziBVsU_wazYy8wLwAR6btGSnxlxKDVBAsK3auUKoVM5yXw==)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnIRA2OmIUl9OY6mZPwM6eWXDldVBRhWD0Qt8tcbv48Qu3w1P-UMabL6JeBK5TRD8LXAtUP4I1ECk2jtM8Yznfj2wPaYfYUvJvr2eKKxU9a04yPgNe7g==)
25. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJkWUwc1ju_XGvgNPx7jvLpcv9bWFgg-aBwlVszK1BRThdyMGroD8q1qKwaLE02zTdf7KiDDlfb6UteKulcU7asznniPSYsOyEwQPXOBiUbz8xXeiLXo3uhotOWM9DZU-USxVqQT5Xz1qGfFWTwkm8g1YK66aNSDCikMuN7_WRut3SHedNPBanzOOk75Om7MRBSB7xnJ6L6QnoPPon10Nwek2P92SXfnxsb1EAqQ_tFNkA-colxZB8XLZghj5Pbp2Y7D2zAw-Y1dQ=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQdu-6clgrIrpLbauvrAs5eOu_DA6Qx2d1lRS9uTebTHje-Je8JyDcKURcSNKQOVA8NMMWFBBHVK0c3RgrydVDMgkpk1Gd3Rv_TizIgj_HlvnrrQLJ7Q==)
27. [ecva.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcKmxVtv50PnyfwWyktXHpjDC0SZ4D6QZk8HRfbgA4u0GNdaVonWPst3vUOaDCJYWgtlP6fw6B4RksOoCkqLAx9LV-7TB5DJT9D48dN0MPbBVfub13PV9AzrtzM8K9LB7cYtOHu6XpIsVHs8iQn4nlWJAtz4XbURIvxF_d)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjM8LvwROH4WbM4FvTK_7tnaxHcD6o9kud-sREC1vMVemdta-e74VY6-Njq0He6ZNpFoZ64UNNQcBOTmset3ultNKdIPobERU2lKF2tIl52tayOgMjRsQ3F8TRmGObDaIxECSXQiL5MqXXKtBkUraBGl9bjxODBZ7kwMq4vxfGfYHlwRfTuE2LUS5BZjGHisrAmOMsYUPvJjLlXzpWCVOzqjXFOV8HG1bz7yl-HtWumEy2OSUeSCGnPvQmwOeaoEge)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEOM_qLDtXLVudpnbmp8wAcDCW4_H7ObkRjy0BMq6Yt15JJq20O2-ek6sdE4PegrxMD4WSLG8tzuV_lYsgwdTmyeRrVNAUZ6pOHnEFKsKGJ0MvAtg8yw==)
30. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmSrp5Zxya5HpGprIa23ymQJ46DIlSbkWp_28En63tgN8g3XszLnSFvQL81-LZxm3EOKUbJPCLjEEglfjs1nNO_b1oLOP697laMU35GPmKDR-3PfpNLdQod3IUdP7QKpL0miT_bOVluVqRBRaIEgQHAg86G2LhrRFysfTHGKg84vjHFk3C18LNnfCGiCtzXPIjN-TTHrMin0AzHyNSdYg-0v_-KKK_HbuAsmgzc2fZ1zw8o4zfigzamGWuTb-NvfSB)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqylr-22gQHZZFEjU9QAKpXHjBIispu6bgjZPDCQ7boSJB1GZqdK5imXgCEQB4CxcliOzxnrH1Ol4jKwxqlZDp9BZCBWG8Q17AiBE4RgQNqxS6CVLZng==)
32. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl2PNvwdbh4advanzoQSf7fXjV0QUJ6zmVVgk3kZtsZ2YKOZS6_1AzfESdpiyJ-SampWHlN25lO6ICOpiRKhfOJiloFxlPkXP1faRk8PwJAm_pjFm1GgnMT8KK0fg3J7xdgtT2x99wrqFD4m608RJhwLLJ9Ho=)
33. [wandb.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8rm-zAE2vRuXRZ8opt9IwUOc5PJQ3oURrsMX14hhMZSMakgs9rJCwVg2HB3aJ2sZGQUFQcej--9HA1SbL2L3alhPJ2zFnqyF0q1BZPbZzCvP1QD9dWZeNPZk3VrPr8z2QV23QH1EGGjiQ0n1HDs07emglHIknhupV9_DIVXfDg3xPVIL9-V2JnlKdVzHPRgYMjjFOR8DpOexhXYgmljHW-N9qqnYaFBnKbn-NFCKN-4KZLK4YKrk_vec=)
34. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUyK6FMLAxBzGaUEzwt1onG_WJdtWSJCVYv6VbAu3LOii5U135s3CuAXBefIWQeT4eYJ3UCve-68E5XGvzCJpbNHvjXFx-xgk7q-u5gnjEB96qcoPq5bZw1XO4Ro3alsc8rntRZmwv2M-7M_0e5t8qsV0j4vc-kepkTZ86ePoQkTGUG5204c0NV1fxsKQE)
35. [wandb.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8JNBWSTuXZgtuZ7m7zFz-3eW7ZbQRlAhyO4ZpaPzXrfjnd8wqs_wbhV7qiEF7bDhupQJg9CSG6kvNCY2CzxXEyrUY-R9lFohitfgF4ODmCNUr4Mqum8UkkN2jSN5givTvuO45eHeRjoKcod600FMpbOJOAuKcFVDY-cDCCx2MpRHJ5EGhcVq3zD2EExSS5LFSo-7GPqkfeuIkDymP3Pwp3-Q=)
36. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzOxYc_X96d2TqZZ73o4e7iCdqq0bipk6X8oQxCBu-dsQ7usbFUl1pkhv4uixryg4Tqlh_10P1qAcqL2a0ABLw2y8wrLtIEw8SHrbvwBI_jzoQfhtTfu1_gr0gnPOfS8NObVRyok-I5CJLvBFskXJwdlM6JhOUz3XFmw==)
37. [towardsai.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuI1xjXHwy8inoLefFqYXEHUSHVEN5HxIbxolZx6EmA1qgqwoc4OOSOIWS8QvYIFMUnYtSN7vTVtHwfGQMW2OQQyQSmov_o37spYeEyNhv84z94WXM7J7uHHwfrBRAZk5S0d3-4gCMtLFODKID0haDGnA39y2XL8WjZfHTn8ewYUvPu3iGfUkhDJSsXArE5_vR8A==)
38. [docsaid.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOXMLgQ9xBqb301Nx7FpW3KV0kw8fnpm9iGY26GWdUPYxLGVcZ9dMspUubsvOO1_Stl3ZLsN3Wl8PpkpNi-pXo_Jqjnd7R-lugXQlfMuWP5H0Q6kf4Vw10HVE9xQOkcjImLDAApdz6)
39. [research.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4ejGKeRYpA1v68VUAdP4qEP-PROwgKQmbL4N7XacgESaz9K5u0G6-6AFolC--awpk3D_BsPDjZ8tALHx04V9UmUsBTAkAgXQpe9OQqxWuNdX3xno5nY3Cng==)
40. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgo2C6ABBo21c8VueS38-H4fZWfMIqMlGJKHviht9phBGM2n-wwGyPmDifjEDDFtTce9i8LGVrbJzeZKQMenLDI1RzkP5mQ7OV6X83qYEu9Jb5gN18Z1uu2LI=)
41. [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfDFk_83wl5sOm_HrnRZAx4pHFCFAc4T-L4y5lQA02tifq-72Ca5e00U-400iaMbEKb5yNzIdAehq3rVLT2-vVUeN1d7lLHL9vvOo8txW13eSELPC_v_BhqsRqkESI)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjyHB_GkTiiXhaPpaT4QXQYgx_sakcvaphKLOpCNSGs1c3ycrc6fy6wrEc0Gv6rNbQekR-OoX1_wPBKinpqXEVUOHSwtrSw5aqU8C_lWgoyv0sI7QrRmPAdZI1Uz7E)
43. [miccai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsWW_UQRAR96H4-CcsGX7Dx3E9q5Yj2I8LVG4AGXfDtn05w0p1Ep4Tv4WA-AEfMwNtg6Y8FUzGz2_gxegbkQx2KWSQMts_IHp4waQ7Te5EWCA-Xv6127CQSbtq1HzJ_JyG1raDRm4Mz-Mo0DSKUKxvXgwC)
44. [themoonlight.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIWnmZq-7CHlhe4sDnOltbrxjUW5IpZCMI6GWOgRKIXwb8o-5ZW7wH0a30fvqjGM3sIaS1wupRIY3Yz59Z2uU18n-6yRxHyo8UONw7jrdKJl0cFyIV-Kvk7RmlxZPmkZJv6_2cYHT-IdTrfrWYYzRQfL5sHBUzbnaht6XClNn1XfaNH1gBY_mlKBF9UdnynYIvyWwXxzUZ7YEb44GaNMKkxtlvHaRwiw6gI1M=)
45. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxg7jXhXV2h132bguOXO8fWbUBEQ4JuLYXB4gWTr7UM21Mww4vodw9y-VqTAbi5IsycVTKQ35uFDxgQxhd4LkAmtggiD4KBG26cAtz7RXvJgbWaaD0tYkPwpYiC_V4DS1OOSnG)
46. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjfeJdaO0zCZnKciLi_kAUzAP5A4JBExhzLPhYjoYk5yvXCXfkMjpsgSOm1JuFoe7l3O51HcZJ4a4fRaij8ur0bDCw_40vdxq6tK3VZk84HOIkPPuAtf-Sjfxl5SioEQ-74KVb4J30ApoExCJeMT56edSjk1bWA8Ez7UQpMMuiuw8b5aOVNGTRe8kqRP8IlfY8K49iHvkLDB2yrxi9H7LmYzLQvjNrGk9kIvB2ZZ2Id-IaekPExXNWC2nAAq-NUvLw8Xa34PYCR5_bAbuVt037653ujZIO)
47. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqAoJFqVIs6dOjFd0AWNmao-84VDVYrNhObat4FjpxAg9-LkM7A_2ft3atIvlq-v6Q5cgQS-XI748z08UsRM_kav-ksgFhgCaX6HDvuW5ATZIYCchfVw2f4cKW_XzX9Gr6fnePg_UJSxprPQzGRvS4PjR7SWM=)
48. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUR403zA0eICPg8uKWHghNs1Czvkdhyk7_iwDzhT3DXVKlyERsN0YpklnQPxU1Jap2ijrhbsP_fymq7d2z152kUd-zqdv7H4sqU3AlPAtEI2bqZTSqnw==)
49. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-TLicNqU-iY7d4YsD3EmUbitoNY7kx9QIogOSGSsHgtnRXkv1St2KqRN7s7p3GYnlXuobFYON29_-to5OK7nhnRlGPdBxvAvVv_ittxjo5wDe6WnNjVBYbQ==)
50. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtyFogr8mI3J-xIhykie0UXN-g9-T1aulR-v2VKMAmRttF8UHz4AZwXgMwTNkmjYecoU3ZJ5welJzqxDUVYoYvPCPfjXnhLoke6btZmSc9V9BEqCRksylfSKV9w_htaOaPoW8l-v_7SGPgppbulZXUJ6lV0t7FePG9Y3sMU5y92o3sTU0TW-xDjhHSs74ERhxZC_7LozSEPqcVwNXKbF5Q2WeBtl8Q0MMvo_X9o2NHqjPdFbtXzcYTyNE2)
51. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGilVeNWxQjfdwS2vQgSF-au8HEvp0RuIGP7gWSFcgpc5jd0og1jr45zz7sOcTeVYCP1zAOdGBNNNsqUqeg9UNOeL_MoY8ba4ZsCD3qkRLPbZP8lXDEaQp9A2ZtyYLh)
52. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-xE7AaS-cof3CcauTxKqWDHlEJ6pMUKOxJtEY8OFPMx1IbGsFlkgc4qmNTfCUK_TJobNoqsqL9GkT-2LkNWSTUuh2gbxGZjlzrc-FnxMO6oVxkZNshplWjo2vp-ZsrHHvbpnsuf6k2j-i8XTjBf9wDNkwmUfBWb1nQD2mE0WAtBspakrHnvlmbU9pYV3GS3mGH8QCbAaiFEOOzIN1VzQ=)
53. [neurosymbolic-ai-journal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH83gYd9eL8AYnal2jKTYWw7q7o3d1jWwDMa-ZCyGLiFH8uz3yLMumLf31NXXToW_jczVp3-Xc8cOZd1Bvo3M6fHFDQ6txjZu3mVYlSB1PNkWUnYHpF21wtUAV2EinsRdIhjbWUI6HChJUu3EyjZQmkZ-5Pj2lUJN6W)
54. [neurosymbolic-ai-journal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLktBQ0OQjeVNkzEPoLE5KExeMkMn4pRezoIPSOdklBadD2eeWqInz2znMANq3nZ_WG0A8t0C2P6zJCVgOZ1B-jbnRzc1PcCGL3JV4du-b88qX5bqkchHEEso5-BoOsM2Cl8_QAnpAiNrrnAt0sx8ieZ7473ht1faT)
55. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF786WQtz6lhP_ce6Wu-fRf1sZnZcPdo3ul3PE96WAsq47NVSn3pA4KkgOfvDtvLjvAOzVi5SA1nKd-kvwM26FauZy7tnVy9KE1ln6qI2wttSgb_QYhiA==)
56. [tuwien.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_sHn7ezJCKUCHWqDF6ykIgegYshSRjk0W3uGpIFTkmSJWDQGVAe9tI9owa07IaaZVb1xJP7-hQbOAuowY3Wk6dWJf67fIzIqEf1y_pv9D3RMoLBMo1A0JeW67KhSNqJxL_iG_MUfTOrrGFMI0yb5XM-DiKsLpPqIP3kJ4K8mzD30Ua4wKpSxXfXXOYs9ePz0xc1DqIfTNOgTi1XlBNsDiuVoir7Ky48EZsv8LFY8XhXMTsB1Vv_Z4F38UO5FwifrmvYruCErTCQNO5w3YcJ5q87V7ecCRQg==)
57. [cambridge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMtnWRqRZ8g--6wFGxu3bk55k4kBeqUmhj--W5cNv_7uft0m_0bf9AS4e4nWDww7iqmFcS2K-g05wkEdoAxFxdvmJP5IdsNuwi3dUvCsEpVsT1fhr89BpU5bsS8KbJJmBkn9qEdy1jLiHvG4WAHvhLBVuJRwKUS1MZzv_jUaO3xmr61GcriQzqLmpFCtDpl0imyPxaHFmsWIvWQbvzPqjb1N2IDeW_XnC2h_41SnfsowkfsqpzgF5Ts5zhvViytMrQm0TVAF2wI28qzminyZCzgpK4L7lgAb2CRV08d92xHr0IJflHi8grZg==)
58. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTk9-qQtCJgzJzrTFHV6RpJXQ51tO5nikvFl9_t7xNrnG_qC2wVxXpXImUqs6oYvieWkz0xHGxulqTUnhMo9kC6ff_UDHz-sthxVSgpdovOnA5uRAGdl_kWIleaZk=)
59. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxQoFVBdCm6xvOC22YynLS0GZRSYhNHvA8paOftR0QIIanhPvgygudLLQ2HxjltPoSqyFdKt0x7zliSejbc-W-RDnJQ_Pa6cLBAYmHGylZYpSlwEF3Zw==)
60. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgN3crC5sM7MKssyKINS0biHisNXRp32jWusEbQsQjxUjFQOa8EM3w9-Vi1rLtx6zpk4M5G6KxMHpaqm1_eRx_aSI5TzN0PuK_5wgU9d4WcoEuj5V9z1_i5Ka40aPVyC4tRonxRc-LmB1rGEg_TEUc-mUTKXcuMM2JFxDg2tkr7BeToBt26OYs7P_Csad5wKXfhZfX2R_M9S3M0ZM1mRmEf5a1wa0IfVieQo1_)
61. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVqEUSKXBcblPiA_nisWOZ6wAC_TfXcUltmOkjXFUAZpyQpLTyycQYlq1Mp9gwq86oND6lNjPvoIMpziypKOqSIMFmc9dcVcvJyLp7QY-bfLoa45n3SAnxHdGoZVkVDQ==)
62. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw0tvkfFo1F_cFxs2UH3afum1FaVIDdea3OAA708kVmmER6J5i_Hs-mXF2Kf7sGwxDdlj_jOj52GuLSbIMF31NuvIzXWieo1KsCnFu0Kbikb47zhJtHoYbU22bTRcU0A==)
63. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOhfpJUmpt7Drf30V1c5p5czFIaO3ADXT4C1q3nYmnUQeoJh4iplBK2Wg7oTfbImP5W58-8iQQV03C1zy1FyXpzwy_6vQZ9v1qywHeYPcOAn7CJYagZqGSRBIfWBsgeS9VAHlyYSsks7D5SWx3S_Ovee9CwPMnoodxJRRkryxPNwM3PTkmlA2VwEYZS0o2)
64. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG277K16SYn8r1N30Yn4wso4WUoyBmez-4jIph6JgR-q6ldlyu9p01Tf8eIxtT4lTTfI2adv4Q2JwF2QTXpBu8wxJ2auYqUqv4ZHkO2quOmznjHHjvObiwDF_BiLoAWXH9lBTIve6ieTTlPUOGGj_isN0pcvvVK8IV0Tg==)
65. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHtSCZryZiPnoum9_xQdc1ct1HwDudsmimkTPop01uhskX5GGWfUUA7OqtYs7yPqpe2IwfV2YrsXhatwwEOOBKxry7zyVw4DR9sJZ6MlxsVtVumMG2-68PmtIAD2-yXAFxt7yyQv1Gt4cM2U_ddAETzcjGZHmX4H0OgY_kHAN6H12-rtICEqEYNqa7NZzomClQ7Mc=)
66. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKwemOsXO4tnp22bgoivLyg4mVHWTr74yFXOQLL0sdUlMO0TVpgSA3I-HKkr3rZ1fyTZdkn7aby64Vv4RIr2KMXn-RdQBmh50oGRmHFTrM_Pto7Kh8XyvkTq8erRjrVZUgDC3CLtur)
67. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGymOIkOq_U6AFnxEl4069GvkcsZADbUowH20zIfgKrNCRjTLeohjbK73LWCacU4VtMCzruXfCb7CjTcxoUddx_msGOpgUSEm6V2M-TvckxBLxiz13JLGj9gkkwc-tE7JiHcGvF)
