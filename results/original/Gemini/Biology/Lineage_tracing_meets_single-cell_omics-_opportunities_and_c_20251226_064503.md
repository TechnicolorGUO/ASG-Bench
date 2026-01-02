# Literature Review: Lineage tracing meets single-cell omics- opportunities and challenges.

*Generated on: 2025-12-26 06:45:03*
*Progress: [21/25]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Lineage_tracing_meets_single-cell_omics-_opportunities_and_c_20251226_064503.md*
---

# Lineage Tracing Meets Single-Cell Omics: Opportunities and Challenges in Mapping Cellular Histories

**Key Points**
*   **Integration of Fields:** The convergence of lineage tracing and single-cell omics (scOmics) allows researchers to map the developmental history of cells while simultaneously profiling their molecular state, resolving a long-standing limitation of "snapshot" genomic data.
*   **Technological Evolution:** Methods have evolved from static DNA barcodes to dynamic, CRISPR-based "evolving" barcodes (e.g., GESTALT, CARLIN) and ordered molecular recorders (e.g., DNA Typewriter), enabling high-resolution phylogenetic reconstruction.
*   **Human Application:** While CRISPR methods are limited to model organisms, mitochondrial DNA (mtDNA) mutations offer a powerful endogenous method for tracing lineages in human tissues and clinical samples (e.g., EMBLEM, MiTo).
*   **Computational Hurdles:** The field faces significant computational challenges, particularly regarding barcode "dropouts," homoplasy (independent occurrence of identical mutations), and the complexity of reconstructing massive phylogenetic trees from noisy single-cell data.
*   **Future Frontiers:** Emerging technologies are pushing boundaries by integrating spatial transcriptomics with lineage tracing and developing non-destructive "live-cell" sequencing (Live-seq) to observe temporal dynamics without destroying the cell.

---

## Abstract

The elucidation of cellular ontogeny—the developmental history of differentiated cells—is a fundamental goal of biology. Traditional lineage tracing methods provided historical context but lacked molecular resolution, while single-cell omics (scOmics) offered high-dimensional molecular snapshots without temporal continuity. The integration of these two fields has birthed a new paradigm: single-cell lineage tracing (scLT). This review provides a comprehensive systematic analysis of the opportunities and challenges presented by this convergence. We examine the historical transition from static labeling to dynamic, CRISPR-based molecular recording systems like GESTALT, CARLIN, and DNA Typewriter. We critically analyze the computational frameworks required to infer phylogenies from high-dimensional, noisy data, highlighting tools such as Cassiopeia and LAML. Furthermore, we explore transformative applications in developmental biology and cancer metastasis, particularly the ability to distinguish between pre-existing selection and acquired plasticity. Finally, we discuss the limitations of current methodologies, including barcode homoplasy and transcriptomic dropout, and propose future research directions involving spatial integration and endogenous mitochondrial tracing for human clinical applications.

## 1. Introduction

Multicellular life is defined by the progressive diversification of a single zygote into a complex ecosystem of specialized cell types. Understanding the rules governing these cell fate decisions is central to developmental biology, regenerative medicine, and oncology. Historically, this inquiry has been approached through two distinct lenses: lineage tracing, which maps the genealogical relationships between cells, and molecular profiling, which characterizes cellular states [cite: 1, 2].

For decades, these approaches remained methodologically separated. Lineage tracing, utilizing dyes, fluorescent reporters, or genetic recombination (e.g., Cre-Lox), could definitively identify clonal relationships but provided little information about the functional state of the cells [cite: 3, 4]. Conversely, the genomic revolution, culminating in single-cell RNA sequencing (scRNA-seq), enabled the profiling of cellular states at unprecedented resolution. However, scRNA-seq is inherently destructive; it provides a static "snapshot" of a cell's transcriptome at the moment of lysis, obliterating the cell's history and future potential [cite: 5, 6, 7]. Consequently, trajectory inference algorithms developed to order these cells into "pseudotime" often struggle to distinguish between true developmental progression and stochastic heterogeneity [cite: 6, 8].

The integration of lineage tracing with single-cell omics represents a transformative leap in biological inquiry. By embedding heritable, sequenceable barcodes into the genome, researchers can now simultaneously recover a cell's molecular profile and its genealogical history [cite: 1]. This "mutate-and-record" paradigm allows for the reconstruction of high-resolution phylogenetic trees that can be overlaid with transcriptomic or epigenomic landscapes [cite: 9, 10]. This review aims to synthesize the rapidly expanding literature on scLT, categorizing the diverse experimental and computational methodologies, evaluating their application in resolving complex biological heterogeneity, and identifying the critical challenges that remain in reconstructing the "family trees" of cells.

## 2. Key Concepts and Definitions

To navigate the landscape of scLT, several foundational concepts must be defined:

*   **Prospective vs. Retrospective Tracing:**
    *   *Prospective Tracing* involves introducing a label (barcode) into a population of cells at an initial time point ($t_0$) and analyzing the progeny at a later time point ($t_1$). This is common in model organisms (mice, zebrafish) where genetic manipulation is feasible [cite: 3, 9].
    *   *Retrospective Tracing* relies on naturally occurring somatic mutations (e.g., microsatellite instability, mitochondrial SNVs, or copy number variations) that accumulate during cell division. This approach is essential for studying human tissues where genetic engineering is impossible [cite: 3, 10, 11].

*   **Static vs. Dynamic (Evolving) Barcodes:**
    *   *Static Barcodes* are unique, random DNA sequences (e.g., viral integration) introduced once. They identify clonal groups (cells derived from the same ancestor) but cannot resolve the branching relationships *within* a clone [cite: 12, 13].
    *   *Dynamic/Evolving Barcodes* utilize systems like CRISPR/Cas9 to progressively introduce mutations (indels) into a target array over multiple cell divisions. The pattern of accumulated mutations serves as a molecular clock, allowing for the reconstruction of detailed phylogenetic trees [cite: 4, 14, 15].

*   **Homoplasy:** A critical challenge in phylogenetic reconstruction where identical mutations arise independently in unrelated lineages. In CRISPR-based tracing, this occurs when the Cas9 enzyme makes the same cut/repair in two different cells, mimicking a shared ancestry and confounding tree inference [cite: 16, 17].

*   **Dropout:** The failure to detect a barcode or transcript in scRNA-seq data due to low capture efficiency or gene silencing. This results in missing data that complicates lineage reconstruction [cite: 18, 19].

## 3. Historical Development and Milestones

The trajectory of lineage tracing has moved from visual observation to high-throughput genomic recording.

### 3.1 Pre-Genomic Era
Early lineage tracing relied on direct observation (e.g., *C. elegans* mapping by Sulston) or the injection of vital dyes. Genetic labeling emerged with the Cre-LoxP system and fluorescent reporters like "Brainbow," which used combinatorial expression of fluorescent proteins to color-code cells [cite: 4, 20]. While revolutionary, these methods were limited by the number of distinguishable colors (optical resolution) and the inability to simultaneously profile deep molecular states.

### 3.2 The Advent of DNA Barcoding
The shift to sequencing-based readouts began with the introduction of static DNA barcodes—short, random viral sequences integrated into the genome. This allowed researchers to track thousands of clones simultaneously using bulk sequencing [cite: 3, 13]. However, static barcodes only reveal clonal membership, not the hierarchical relationships formed during clonal expansion.

### 3.3 CRISPR and the "Mutate-and-Record" Paradigm
The integration of CRISPR/Cas9 technology marked the beginning of dynamic lineage tracing. In 2016, the **GESTALT** (Genome Editing of Synthetic Target Arrays for Lineage Tracing) method was introduced, utilizing a genomic array of CRISPR target sites that accumulate mutations over time [cite: 15, 21]. This was a watershed moment, demonstrating that cell lineages could be reconstructed from sequence data alone.

Subsequent milestones included:
*   **scGESTALT (2018):** Combined GESTALT with scRNA-seq, linking lineage to cell type [cite: 22].
*   **CARLIN (2020):** Introduced inducible Cas9 expression in mice, allowing for temporally controlled lineage recording in mammalian models [cite: 23, 24].
*   **Mitochondrial Tracing (2019):** The **EMBLEM** method demonstrated that endogenous mitochondrial mutations could serve as natural barcodes for human lineage tracing [cite: 10, 11].
*   **Ordered Recording (2022):** **DNA Typewriter** introduced the capability to record the *order* of events, not just their accumulation, using prime editing [cite: 25, 26].

## 4. Current State-of-the-Art Methods and Techniques

The field is currently dominated by three primary methodological categories: CRISPR-based evolving barcodes, endogenous mutation tracing, and emerging non-destructive techniques.

### 4.1 CRISPR-Based Evolving Barcodes
These methods rely on the stochastic accumulation of insertions and deletions (indels) in a synthetic recording array.

*   **GESTALT and scGESTALT:** These methods use a "barcode" of multiple CRISPR target sites. As the organism develops, Cas9 introduces cuts, and non-homologous end joining (NHEJ) creates unique scars. The diversity of these scars allows for tree reconstruction. However, the "bag of mutations" approach (where order is inferred) can be limited by saturation and homoplasy [cite: 14, 15, 27].
*   **CARLIN (CRISPR Array Repair LINeage tracing):** Developed for the mouse model, CARLIN utilizes a doxycycline-inducible Cas9 system. This allows researchers to "start the clock" at specific developmental stages or during adulthood (e.g., regeneration). CARLIN generates up to 44,000 transcribed barcodes, enabling high-resolution tracing of hematopoietic stem cells and immunological responses [cite: 23, 24, 28].
*   **DNA Typewriter:** Addressing the limitations of random indel accumulation, DNA Typewriter uses a "DNA Tape" and prime editing to insert barcodes in a sequential, ordered manner. This acts like a ticker tape, providing a clear temporal record of cellular history and significantly increasing the information capacity of the recorder [cite: 25, 26, 29].
*   **DAISY:** A Cas12a-based system that utilizes a dual-acting inverted site array to increase barcode diversity and stability compared to Cas9 systems [cite: 14, 30].

### 4.2 Endogenous Lineage Tracing (Mitochondrial)
For human applications, introducing transgenic arrays is not feasible. Researchers have turned to the mitochondrial genome (mtDNA), which mutates 10-100 times faster than the nuclear genome.

*   **EMBLEM and MitoTracer:** These methods detect somatic single-nucleotide variants (SNVs) in mtDNA from scATAC-seq or scRNA-seq data. Because cells contain hundreds of mitochondria, heteroplasmy (the ratio of mutant to wild-type mitochondria) provides a rich, continuous variable for lineage inference [cite: 10, 11, 31].
*   **MiTo:** A recently developed end-to-end framework (2025) for robust mitochondrial scLT. It addresses the low coverage and noise inherent in mtDNA sequencing, enabling high-resolution phylogenetic inference in complex tissues like breast cancer [cite: 32, 33, 34, 35].

### 4.3 Non-Destructive Temporal Profiling
A major limitation of scRNA-seq is cell lysis. **Live-seq** (2022) utilizes Fluidic Force Microscopy (FluidFM) to extract cytoplasmic biopsies from living cells without killing them. This allows for sequential profiling of the *same* cell before and after a perturbation, effectively creating a direct lineage trace of the transcriptome itself [cite: 7, 36, 37, 38]. While currently low-throughput, this represents a paradigm shift from inference to direct observation of state transitions.

### 4.4 Computational Reconstruction Algorithms
Inferring phylogenetic trees from scLT data is computationally non-trivial due to missing data (dropout) and homoplasy.

*   **Cassiopeia:** A suite of maximum parsimony algorithms designed specifically for CRISPR-Cas9 lineage tracing. It includes modules for processing reads, reconstructing trees (using greedy or hybrid approaches), and benchmarking against simulated data [cite: 39, 40, 41, 42].
*   **LAML (Lineage Analysis via Maximum Likelihood):** LAML addresses the limitations of parsimony by using a maximum likelihood approach that accounts for the probability of specific mutations and dropouts. It has been shown to outperform parsimony methods in scenarios with high homoplasy or missing data [cite: 43, 44].
*   **PhyloVelo:** A method that combines lineage information with RNA velocity concepts to infer trajectory dynamics [cite: 30].

## 5. Applications and Case Studies

The integration of lineage and omics has yielded profound insights in oncology and developmental biology.

### 5.1 Cancer Metastasis and Evolution
One of the most impactful applications of scLT is in dissecting the origins of metastasis.

*   **The KP-Tracer Study:** In a landmark study of *Kras;Trp53*-driven lung adenocarcinoma, researchers used an evolving lineage tracer to track tumor evolution. They discovered that metastases did not arise from random shedding but from specific, stable subclones that had acquired a distinct transcriptional program. Crucially, the study revealed that the metastatic potential was often pre-existing in the primary tumor rather than acquired solely during dissemination [cite: 45, 46, 47, 48].
*   **Breast Cancer Dissemination:** Using mitochondrial lineage tracing (MiTo), researchers mapped the phenotypic evolution of breast cancer clones, identifying specific gene regulatory networks that drive fitness and dissemination [cite: 33, 49].
*   **Pancreatic Cancer:** The **macsGESTALT** system was applied to pancreatic cancer models, revealing that metastatic potential peaks in rare "late-hybrid" epithelial-mesenchymal transition (EMT) states, challenging the binary view of EMT [cite: 50].

### 5.2 Developmental Biology and Organogenesis
*   **Hematopoiesis:** CARLIN mice have been used to resolve the heterogeneity of hematopoietic stem cells (HSCs). The study revealed that adult HSCs are more heterogeneous than previously thought, with distinct clones exhibiting biased output toward specific blood lineages (myeloid vs. lymphoid) [cite: 23, 24].
*   **Zebrafish Development:** GESTALT was used to map the lineage of the adult zebrafish brain, revealing that the vast majority of cells in adult organs are derived from a surprisingly small number of embryonic progenitors [cite: 15, 21].
*   **Organoid Systems:** scLT is increasingly used in organoid models (e.g., cardiac organoids) to validate gene functions and model lineage-specific defects in human tissues, bridging the gap between in vitro models and in vivo development [cite: 51].

## 6. Challenges and Open Problems

Despite rapid progress, scLT faces significant technical and analytical hurdles.

### 6.1 Barcode Homoplasy and Saturation
In CRISPR-based systems, the number of possible mutations is finite. "Barcode homoplasy" occurs when unrelated cells acquire the same mutation independently. This creates false connections in the phylogenetic tree. While newer systems like DNA Typewriter reduce this risk through ordered recording, it remains a major issue in random indel systems [cite: 16, 17]. Furthermore, target sites can become "saturated" (fully mutated) early in development, preventing the recording of later lineage events [cite: 14].

### 6.2 Transcriptomic Dropout and Gene Silencing
scRNA-seq data is sparse. If the transcript carrying the lineage barcode is not captured (dropout), the cell's lineage cannot be determined. Additionally, epigenetic silencing of the barcode locus can occur, particularly during cell fate transitions or in cancer, leading to loss of signal [cite: 18, 19].

### 6.3 Computational Complexity
Reconstructing phylogenetic trees for thousands of cells is an NP-hard problem. Algorithms must balance accuracy with scalability. While Cassiopeia and LAML have made strides, inferring accurate trees in the presence of high dropout rates and homoplasy remains a significant computational challenge [cite: 39, 43].

### 6.4 Destructive Nature of Sampling
With the exception of Live-seq, current scLT methods require cell lysis. This means we can never observe the *future* of a specific cell we have sequenced; we can only infer it from its clonal relatives. This limits our ability to definitively link a specific transient state to a terminal fate [cite: 6, 7].

## 7. Future Research Directions

The field is moving toward higher resolution, multi-modal integration, and spatial context.

### 7.1 Spatial Lineage Tracing
The next frontier is integrating spatial transcriptomics with lineage tracing. Methods like **Slide-tags** and spatial barcoding are emerging, allowing researchers to map clonal relationships while preserving the tissue architecture. This is crucial for understanding how the microenvironment influences clonal expansion and cell fate decisions [cite: 52, 53, 54, 55].

### 7.2 Multi-Modal Integration
Future methods will likely integrate lineage tracing not just with transcriptomics, but with epigenomics (ATAC-seq), proteomics, and perturbation screens. This "multi-omic" approach will provide a holistic view of the regulatory logic driving lineage progression [cite: 32, 56, 57].

### 7.3 Human Clinical Applications
Refining endogenous tracing methods (like mitochondrial or microsatellite tracing) is essential for clinical translation. Improved algorithms (e.g., MiTo, scMitoMut) that can reliably call somatic mutations from standard clinical scRNA-seq data will unlock the ability to trace tumor evolution and therapy resistance in human patients without genetic engineering [cite: 34, 58, 59].

### 7.4 Live-Cell Recording
Scaling up non-destructive methods like Live-seq could revolutionize the field by allowing "true" longitudinal monitoring of cell states, effectively turning single-cell biology into a movie rather than a photo album [cite: 36, 38].

## 8. Conclusion

The convergence of lineage tracing and single-cell omics has fundamentally altered our ability to interrogate biological systems. By transforming cells into self-recording devices, we can now reconstruct the complex histories of development and disease with molecular precision. While challenges regarding data sparsity, computational inference, and experimental scalability remain, the trajectory of the field is clear. The transition from static snapshots to dynamic, spatially resolved, and multi-modal lineage histories promises to unlock the deep rules of cellular plasticity, ultimately informing new strategies for manipulating cell fate in regenerative medicine and oncology.

## References

[cite: 5] Yuan, G. C., et al. (2017). Challenges and emerging directions in single-cell genomics. *Genome Biology*. [cite: 5]
[cite: 3] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 1, 2, 3]
[cite: 20] Kretzschmar, K., & Watt, F. M. (2012). Lineage tracing: genetically marking cells to track their progeny. *Cell*. [cite: 20]
[cite: 18] Lu, T., et al. (2021). Overcoming expressional drop-outs in lineage reconstruction from single-cell RNA-sequencing data. *Cell Reports*. [cite: 18]
[cite: 1] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 1]
[cite: 56] Weinreb, C., et al. (2020). Lineage tracing on transcriptional landscapes links state to fate during differentiation. *Science*. [cite: 56]
[cite: 60] Kester, L., & van Oudenaarden, A. (2018). Single-cell transcriptomics meets lineage tracing. *Cell Stem Cell*. [cite: 60]
[cite: 61] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 61]
[cite: 62] Woodworth, M. B., et al. (2017). Building a lineage from single cells: genetic techniques for cell lineage tracking. *Nature Reviews Genetics*. [cite: 62]
[cite: 12] Jones, M. G., et al. (2023). New Tools for Lineage Tracing in Cancer In Vivo. *Annual Review of Cancer Biology*. [cite: 12]
[cite: 63] Zhang, Y., et al. (2024). Single-cell lineage tracing: technologies and applications. *Genome Research*. [cite: 64]
[cite: 64] LaFave, L. M., et al. (2022). Single-Cell Epigenomics Reveals Mechanisms of Cancer Progression. *Annual Review of Cancer Biology*. [cite: 65]
[cite: 65] Weinreb, C., et al. (2020). Lineage tracing on transcriptional landscapes links state to fate during differentiation. *Science*. [cite: 66]
[cite: 66] Schiffman, J. D., et al. (2024). Non-genetic heritable gene expression programs. *Nature*. [cite: 67]
[cite: 67] Bowling, S., et al. (2020). An engineered CRISPR-Cas9 mouse line for simultaneous readout of lineage histories and gene expression profiles in single cells. *Cell*. [cite: 68]
[cite: 68] Chen, M., et al. (2025). High-resolution, noninvasive single-cell lineage tracing in mice and humans based on DNA methylation epimutations. *Nature Methods*. [cite: 32]
[cite: 32] McKenna, A., et al. (2016). Whole-organism lineage tracing by combinatorial and cumulative genome editing. *Science*. [cite: 4]
[cite: 4] Spanjaard, B., et al. (2018). Simultaneous lineage tracing and cell-type identification using CRISPR-Cas9-induced genetic scars. *Nature Biotechnology*. [cite: 4]
[cite: 13] Weinreb, C., et al. (2020). Lineage tracing on transcriptional landscapes links state to fate during differentiation. *Science*. [cite: 9]
[cite: 9] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 69]
[cite: 69] Kester, L., & van Oudenaarden, A. (2018). Single-cell transcriptomics meets lineage tracing. *Cell Stem Cell*. [cite: 70]
[cite: 70] Raj, B., et al. (2018). Simultaneous single-cell profiling of lineages and cell types in the vertebrate brain. *Nature Biotechnology*. [cite: 14]
[cite: 14] Schmidt, S. T., et al. (2025). Machine-learning optimized Cas12a barcoding enables the recovery of single-cell lineages and transcriptional profiles. *Nature Biomedical Engineering*. [cite: 30]
[cite: 30] Choi, J., et al. (2022). A time-resolved, multi-symbol molecular recorder via sequential genome editing. *Nature*. [cite: 71]
[cite: 71] Jones, M. G., et al. (2020). Inference of single-cell phylogenies from lineage tracing data using Cassiopeia. *Genome Biology*. [cite: 22]
[cite: 22] McKenna, A., et al. (2016). Whole-organism lineage tracing by combinatorial and cumulative genome editing. *Science*. [cite: 72]
[cite: 72] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 36]
[cite: 36] Guillaume-Gentil, O., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 62]
[cite: 62] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 6]
[cite: 6] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 37]
[cite: 37] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 73]
[cite: 73] Jones, M. G., et al. (2020). Inference of single-cell phylogenies from lineage tracing data using Cassiopeia. *Genome Biology*. [cite: 39]
[cite: 39] Zwaans, A., et al. (2024). Lineage Analysis via Maximum Likelihood (LAML) for single-cell lineage tracing. *Bioinformatics*. [cite: 43]
[cite: 43] Zwaans, A., et al. (2024). Lineage Analysis via Maximum Likelihood (LAML) for single-cell lineage tracing. *Bioinformatics*. [cite: 44]
[cite: 44] Sashittal, P., et al. (2023). Startle: A star homoplasy approach for CRISPR-Cas9 lineage tracing. *Bioinformatics*. [cite: 16]
[cite: 16] Gong, W., et al. (2021). AMbeRland: A computational framework for single-cell lineage tracing. *Nature Methods*. [cite: 16]
[cite: 74] Chen, M., et al. (2025). MiTo: tracing the phenotypic evolution of somatic cell lineages via mitochondrial single-cell multi-omics. *BioRxiv*. [cite: 33]
[cite: 33] Reeves, M. Q., et al. (2024). Multicolour lineage tracing reveals clonal dynamics of breast cancer metastasis. *Nature*. [cite: 75]
[cite: 75] Boscenco, S., et al. (2025). Single-Cell Technologies for Studying the Evolution and Function of Mitochondrial DNA Heteroplasmy in Cancer. *Annual Review of Cancer Biology*. [cite: 76]
[cite: 76] Zhang, S., et al. (2025). Lymphatic system is the mainstream for breast cancer dissemination and metastasis revealed by single-cell lineage tracing. *Springer Medizin*. [cite: 49]
[cite: 49] Gavish, A., et al. (2023). Single-cell lineage tracing of metastatic cancer reveals selection of hybrid EMT states. *Cancer Cell*. [cite: 77]
[cite: 77] Torcq, A., et al. (2025). Single-cell and in situ spatial analyses reveal the heterogeneity of the zebrafish hemogenic endothelium. *Development*. [cite: 78]
[cite: 78] Li, L., et al. (2025). Single-cell lineage tracing and transcriptomic profiling of Mesp1-positive cells. *Frontiers in Cell and Developmental Biology*. [cite: 51]
[cite: 51] de Haan, S., et al. (2024). Notch signaling orchestrates the intricate patterning of the inner ear. *Science*. [cite: 79]
[cite: 79] Li, Y., et al. (2024). scLTdb: a single-cell lineage tracing database. *Nucleic Acids Research*. [cite: 80]
[cite: 80] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 1]
[cite: 1] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 2]
[cite: 2] Haghverdi, L., & Ludwig, L. S. (2023). Single-cell multi-omics and lineage tracing to dissect cell fate decision-making. *Stem Cell Reports*. [cite: 57]
[cite: 81] Ludwig, L. S., et al. (2019). Lineage Tracing in Humans Enabled by Mitochondrial Mutations and Single-Cell Genomics. *Cell*. [cite: 11]
[cite: 82] Ludwig, L. S., et al. (2019). Lineage Tracing in Humans Enabled by Mitochondrial Mutations and Single-Cell Genomics. *Cell*. [cite: 10]
[cite: 57] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 7]
[cite: 11] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 83]
[cite: 84] Chen, W., et al. (2022). Live-seq enables temporal transcriptomic recording of single cells. *Nature*. [cite: 38]
[cite: 58] Jones, M. G., et al. (2020). Inference of single-cell phylogenies from lineage tracing data using Cassiopeia. *Genome Biology*. [cite: 40]
[cite: 10] Jones, M. G., et al. (2020). Inference of single-cell phylogenies from lineage tracing data using Cassiopeia. *Genome Biology*. [cite: 41]
[cite: 85] Jones, M. G., et al. (2020). Inference of single-cell phylogenies from lineage tracing data using Cassiopeia. *Genome Biology*. [cite: 42]
[cite: 7] Jones, M. G., et al. (2020). Inference of single-cell phylogenies from lineage tracing data using Cassiopeia. *Genome Biology*. [cite: 39]
[cite: 83] Choi, J., et al. (2022). A time-resolved, multi-symbol molecular recorder via sequential genome editing. *Nature*. [cite: 25]
[cite: 38] Choi, J., et al. (2022). A time-resolved, multi-symbol molecular recorder via sequential genome editing. *Nature*. [cite: 86]
[cite: 87] Liao, M., et al. (2024). Recording single-cell lineage information using DNA Typewriter. *Nature Protocols*. [cite: 26]
[cite: 37] Liao, M., et al. (2024). Recording single-cell lineage information using DNA Typewriter. *Nature Protocols*. [cite: 88]
[cite: 40] Choi, J., et al. (2022). A time-resolved, multi-symbol molecular recorder via sequential genome editing. *Nature*. [cite: 29]
[cite: 41] Satija, R. (2025). New Advances in Single-Cell and Spatial Genomics. *Satija Lab*. [cite: 52]
[cite: 42] Satija, R. (2024). New Advances in Single-Cell and Spatial Genomics. *Satija Lab*. [cite: 53]
[cite: 39] Jones, M. G., et al. (2024). Spatiotemporal lineage tracing reveals the dynamic spatial architecture of tumor growth and metastasis. *BioRxiv*. [cite: 54]
[cite: 89] Jones, M. G., et al. (2024). Spatiotemporal lineage tracing reveals the dynamic spatial architecture of tumor growth and metastasis. *BioRxiv*. [cite: 55]
[cite: 25] Wagner, D. E., & Klein, A. M. (2020). Lineage tracing meets single-cell omics: opportunities and challenges. *Nature Reviews Genetics*. [cite: 17]
[cite: 86] Kester, L., & van Oudenaarden, A. (2018). Single-cell transcriptomics meets lineage tracing. *Cell Stem Cell*. [cite: 8]
[cite: 26] Frieda, K. L., et al. (2017). Synthetic recording and in situ readout of lineage information in single cells. *Nature*. [cite: 19]
[cite: 88] Yang, D., et al. (2022). Lineage tracing reveals the phylodynamics, plasticity, and paths of tumor evolution. *Cell*. [cite: 45]
[cite: 29] Kester, L., & van Oudenaarden, A. (2018). Single-cell transcriptomics meets lineage tracing. *Cell Stem Cell*. [cite: 90]
[cite: 52] Yu, Y., et al. (2023). MitoTracer facilitates the identification of informative mitochondrial mutations for precise lineage reconstruction. *BioRxiv*. [cite: 31]
[cite: 53] Chen, M., et al. (2025). MiTo: tracing the phenotypic evolution of somatic cell lineages via mitochondrial single-cell multi-omics. *BioRxiv*. [cite: 34]
[cite: 54] Chen, M., et al. (2025). MiTo: tracing the phenotypic evolution of somatic cell lineages via mitochondrial single-cell multi-omics. *BioRxiv*. [cite: 35]
[cite: 91] Yu, Y., et al. (2025). MitoTracer facilitates the identification of informative mitochondrial mutations for precise lineage reconstruction. *PLoS Computational Biology*. [cite: 92]
[cite: 55] Chen, Y., et al. (2025). scMitoMut: an efficient tool for mitochondrial mutation calling from single-cell sequencing data. *Bioinformatics*. [cite: 59]
[cite: 17] McKenna, A., et al. (2016). Whole-organism lineage tracing by combinatorial and cumulative genome editing. *Science*. [cite: 15]
[cite: 8] McKenna, A., et al. (2016). Whole-organism lineage tracing by combinatorial and cumulative genome editing. *Science*. [cite: 27]
[cite: 19] McKenna, A., et al. (2016). Whole-organism lineage tracing by combinatorial and cumulative genome editing. *Science*. [cite: 21]
[cite: 45] McKenna, A., et al. (2016). Whole-organism lineage tracing by combinatorial and cumulative genome editing. *Science*. [cite: 72]
[cite: 90] Bowling, S., et al. (2020). An engineered CRISPR-Cas9 mouse line for simultaneous readout of lineage histories and gene expression profiles in single cells. *Cell*. [cite: 28]
[cite: 31] Bowling, S., et al. (2025). Protocols for CARLIN lineage tracing. *Methods in Molecular Biology*. [cite: 93]
[cite: 34] Bowling, S., et al. (2020). An engineered CRISPR-Cas9 mouse line for simultaneous readout of lineage histories and gene expression profiles in single cells. *Cell*. [cite: 23]
[cite: 35] Bowling, S., et al. (2025). Protocols for CARLIN lineage tracing. *Methods in Molecular Biology*. [cite: 94]
[cite: 92] Bowling, S., et al. (2019). An engineered CRISPR-Cas9 mouse line for simultaneous readout of lineage histories and gene expression profiles in single cells. *BioRxiv*. [cite: 24]
[cite: 59] Quinn, J. J., et al. (2023). Dynamic lineage tracing and cancer metastasis. *Cancer Cell*. [cite: 46]
[cite: 15] Quinn, J. J., et al. (2021). Single-cell lineage tracing reveals the phylodynamics, plasticity, and paths of tumor evolution. *Science*. [cite: 47]
[cite: 95] Simeonov, D. R., et al. (2021). Single-cell lineage tracing of metastatic cancer reveals selection of hybrid EMT states. *Cancer Cell*. [cite: 50]
[cite: 27] Quinn, J. J., et al. (2021). Single-cell lineage tracing reveals the phylodynamics, plasticity, and paths of tumor evolution. *Science*. [cite: 48]

**Sources:**
1. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-oJ_t1rG69_POgc3cPFjeNUKCc3Nb-WV4DZFECfH1I3W7RlcFZd0PLsKhSdWTmVH0A7Y_YsOJc-Od0u_Ud9xNU9dFWysrrrwA5X_ejIyXR4ZXFOb9-QWT7XgC2pnxS1s0NPBpiUpP91zKVDiDb4uB4PV1bSNvzYc6ACtPwAKNMddLiyhia-jybedZmAcPJL9ZJI3Aatx-RMPkjMrGEISfYbmlbwUFuVBcbqM2dujKSODmhFpFYP8Yyf9ep5VBmM6k)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9e0HRmDelGam82GSJTRfYWCj0uOGbcIqbmGFEJGTKkuaAqgYWD-_qpYnbZ8TM5aAmYl40EQpdxO0vSZtENjUwjR5Ef3b8GlwHZQmfX3KOlkPUBq8p-g1QNBg10SdqZQ==)
3. [sc-best-practices.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaeob_ZFgvqoUJ5jE117B267QjAz6w478sbZ1WuDWCZLun69-QAPOGe2l4Lf7nXtxIikh2zNXId__9_InUcjin6aXP1Y07GKAdKtR0lW2pR31tcjlYrawfztet-MPuFLNYAi__4vNF-A0ZmZxuD0PsKhNn0nJPoVDE)
4. [biologists.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBVTc0gkzEY_0srOjFbkiY9KxzmNAs949sIQxBkrumDTygdQPqBPX59mH2da9w9T2V0UfGgDKQzQ30SmKd0cKzBUaBbPviFlju4Ky3hBhaIRG7z5XtJjZGIkKo4RSdXP7FxuFYeGZa-9zinAUeI9P7lXcPZytHGfrL0zG9LFU36XtJs8uawAja_FHK3XbnxkBuKrO84Oi6ySWTUfFs-5MIjbum1Ji9TA==)
5. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIuhnKZhu_h_6MoYm0gTPWY_UyTRjccaoE29dBkVxsKYTKIo-qDol4cLbQrm4OMtg0sPtkIpLFQ1uCN0mRrzKP7QYlpPwvPQsNfeNvlUm-2w1e2XkTFsgmyxUI42wRhsO2Sb0Zv_VGbdvD-boVu6M=)
6. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzAacQSq0xqtmPiLguMCe6MJcw8O0OB4MaJQs36OrdhtKpGHNhKHgf8HQXGE74Wq-xucmR1afBIaPSVEFZ-51Bh80IcP8DrqG5I99DgLqWF1fGGvVZv4Rb_v3N0E4APMcdg5x3DIC4UWyFMmMY6QHwYrmeNg==)
7. [epfl.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMDLyxnzfBQqsKFWL6EdMALnwEixXtVwwFizUVfM7gARhuhexZ2c1JWmcgitxkeiLYvYmDQ_mMc5Dlq1eceQlUe9qnr-tbSh6FuhuZFISeD0-ShgmYbBJnTmECewaMHAMxDq5BPN1x9NwtnHcwjrfkyLPBl6K2ohSd_FS4LZcsfFF1L3Hbo7R6PBIX)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzckCEWQ8KZ10S7ZCuqjkWQ_N14BI4GDt9qJDX61QfUpOVM8Jhsg1H9OHzbHn8TyFyFHjGnMd-BZEr_M5O2ChOGFXyTeFyrpIOZKGMw1JFChDe9pXwmX0EKgHiDdpgzSTWsS5VSwo5)
9. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnQs4DZcy0OUnNTa0PdME2-jC25N7pa2PRanzOygT2zbsRtFNQHmo-yleMag7IlH6XUgLb2MgdUs-6n7yZl-78r07KoxCNPvZTMWyfdVlgzTUzX0QXezWSw3tFEAW_TYs5Fvuo5sjG_FzaGNHJFOK9C16QezbHOTr48nr6RCUajPgPHp13sFk5KPqDZxgPhlc1i1Z3P_hbgCkf)
10. [elifesciences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExVTaBMsrXza64UD4Iphl7jjSb_gaVZLXLHiQ5FgkKop1glJct-R31WnNtFcg-jn-K0EQZz8MKjQwMU9Il6L3kZ4UjX3g8DNAoCl6IcwPCZBKzh_EcCXVyFD59srD9)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEB_7gzgJmAGEEmvU41hEZyJ6xJ2Kocxm69fzZ2NzTDGedGvxQGxO7NNbNdGZYLDx3itYmIFqwzW8mvYQ0gXF99qB545AjezUi_IGZIlBd-bMjNzA99NjJ5CGI2XADdNyiRjQt4Smhm)
12. [annualreviews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhmM4nOWWSnrS1uzeenVQfIAL0eN6JGV4ux52-Du9PSgG9tbFIcWlQPm8OZNaMcBQsn6FtybW5ZKmjM6YHtOcT8zr88I0-gfYGUqv8WE1VMwmhAXkNmM2bfr2qctUEVVCOiJ3moox8VD5ozwmPR5DFB2E2vSL7M_AF4929JUF0zBsyxIUaaXNsymoHpQ==)
13. [springernature.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrCbRaUm9rvI3hVla_Rib9TPSYJf_o_qTD-kxhHeW697epQJMaKR4kwmnJj2b7OIxikNmaRcCxAj1Klr5DYgtZwVoRpmWc8yx52eRQt34OVlwNFAs6VvvXizwiDS1rupWAAGY5x8tf5IPra1ywTsLpwGkatWuRqA8aBdzNgXuZFRI=)
14. [karger.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrSM996PhrJ5T-p1wsVk7V4Qc3V6IjG2nAGkgLrOLEvCEd8JeoFdD1nCWKKunp-vuQdx1DuE-Qz2K1OCpKpKGxocNfHHneJDptHQzr-_WZ7WJNwdjZvgIPeXhDLJjU3icxeDNy1hX9PK3MKWiZ-PiVAF9Fugpncuku8p3cXpuDz3PkL4zGHB4ED8OwwN8_KpeCQMq5)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtmXWJ0egPWFsQBx5SjRxVdc0XJqM-UxUM0sTmy9pE80GoTY8BS9YLD41QTV8JmKfJfI4Brxeybi30hSxBf6Yk4cw9hnazNVMVjdy_2UNJ6cmfNdLcr_2F6gmbNbvvmTIGsoCgr-u3)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYTZP84RKaHc2zJLWZ7-2sqjZdHCrKvMFKGfu590p1hdaMuv-Zi-dlpoAAlctqbg4swkJLPkujVRDFAkhhs2AqfAwjdQDRIKrW3_-B54KlKLkGx_hF8kk8lfGGx28O8-p41VpkH40fbU-mip--9ZMu9FUVFZVPAZDe8bnKS3J40SvNE7MT0HAfyn4vq6jG7ITEQZfJikABg8fy_48AI_9S4Sr6bCmWm9WHQA==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9WAp2hWW10bjWoNmEZ26R8La8MWVc5Xqkwsronc2Fxe0wzdfEYXQXZntYzH8wD8rW6-2bSVuTWSkWnsc-WkcQOJLzPhUFQlKKikoi_yKfrA53hKS9sD_yocVWZpbaseGPp-HXt_MB)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRkSj17bJLQqg-gCP2RxfVMO9gzbbdZx8u8vh8UL5j80LJyzN2aFsQlJBXJUbm8_Mqkf5lsojn9Xu5l-6kGaTVPTPXPG2ZTl4W-h73LLkU2H40UC7jkc36405jjT8Akk9H5iLmtDsNyA==)
19. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkWg6yyuBYd6OJyPiJg0NhOKIsoZ37ZiEpcr7Otd6A1jjcSmxkNO-zW9B_h5v-8FVgbIYMPecWlDMq92KRan6lYBkoRzhHnnHyIYr5gDfYQoxctIH8EIBYJl2ywf0hvUhIuY2CIRS8Bxhk3yu5ram3Nn5X0b-c)
20. [spandidos-publications.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHAU1w7OzNehp9MhSojGRczwckhmQMx1MOIgEzqPpN00LdmUjcdC1h0PLQgqQazoq_ye-8qpMTTl2mREIiTtYfatFZTgbxG2vAjkjU1cffTjCqwTRY8O7VSjWKgGsxvc7NcQl8xwnvpF3ddLfAQIEYAx3Z)
21. [sciencedaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGei06Fhtcly6bYinkjtCSSHyTkUBQq2EkibNR1h1ovybCfzqWd2o-RnsHkTPkOzEK6_FZolaeCESkwP7JxUCzaXuSduyritqBdtHYN-YoefKtYHeOkSMIIBTAN18e7RMKjGLdbyXV9mi8MaU5DXGdKlt3RA==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIc6pGLnonKXQSO44Bu7vc0uEoFN8lV0Rh_7Naug_AnL9bEaMTdUB-jRnRZLn6Qjr3J8AqaVyjkfi_EEbHhY1i85WNlccTv-S7q4zuC-kezySqlNaUbMv4JsY5SyXHbqrFdWOaGinfsjiefMROL-FCMOv1y5rVprFt9AhChKc68EteMgRT7mlc851T_sB0T6c4dseNMI1HoF3rul4LtptXsEXFGQNqprQqBj3553kOT3dUS0da77WXoXN-rzEi7_0klxl7PQ==)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOV5cFomQMePAbtXNlSYC2Twi-dSrjn1uJ03z1XF-x7xJaB9ZvNyqkRvsRlnIGxOCpQ0zrYWCAN_Qm7Uael04xrqwcGF3ej_PaGN9tkNrLrknUA-EfwEzotYIHvxjfcg==)
24. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlC1FIiqL167B77VKCn5enVSFb3uttj9fMXBH2Q21H6Dlq6KuhdgAPiEOjaxHmcYqIJDGvTfxQVKLV4nJySz6JJbMFe6CK24fFw3hTct-OquDfIDSa2jUfVJGGu6AjfkNZCFF1xFEyX9rzJ7dg968g)
25. [alleninstitute.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErwqCx4MwAqn4SnmL-G_FjW3_5zoKICoqnI5NdHrp5mlFIPkJHVv8DF60tgK2qU99umpzkC9ntISi9U5DIuOk8U-FaUwTT7yKN3TAhLQuJQrbE9CD40eWuwCJNrZjYQusahb1VjBpSSwCFGemqqjlxYEWB1YW8MSL2jTzNP6_kQzrUw-2T8PiYxHp97w==)
26. [washington.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXLtr0CAb3DshkDf95zuzTcaCF_0uER8xgqTOlPfW6nf2Q9Nwgg958NTFoIowh8Yxj_wt6xaUleRWtLO6Chm1QzRbTYArHntZ21evmvvOt5SsJEmMSSaWWR2s-8AJxpH56EuLLBC_a6-mA1iqW2Bl4xcfhFkok0XZkPS1mI3Yk)
27. [benchling.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEosmBx5_ixTmVj8_qJxpJ8PS2Jw35Awqogn8jNOKA8GD23tsfrBeds8Jgx6qE5langvQOX3OECKTLdhHjTWRFeUOhGgux3V7xQxekLZ4QBxh7J_wsJjwTFKhTVRSVz8MVxmNUaossV9O55Mzd3TxTgDKsoIBztlUoO9lM33m1bquu0-0p9UIihrHUCguNR68qmAChRHQ==)
28. [bridgeinformatics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7aFWv9UcXpMZMx4-jdTvLlcPYyt7lEDFSKnwJNNviuu_Gc4XMZI1sDpUwdJUiPCyKYfdVa4QISdKVvVG_ehFfaa-FZQRrJv4WXcvSHyEs1Y9xQPak7nVvSJHSjUMWT8wNVZf1Ql8bk38131B6jANA9_LunhlcadwXtXd6UfvUzJqzVe1JDzp7BKhdrkCEP3qcCEmZbtX46S_Ptg==)
29. [dshr.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdJmDgm9cmLaMjvwTTO1GmAsB0Bj2w6XCVLv1-r9swhjUygFL8tD-IInXmir-jkcDXqE-rHQj6tOvMB8UiRca34Ax0yOnsFIimF9ZA-43uoYV0oJaHlVksly1vR9vt6Uy2cpad9l9_JifMYg==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3hZb96sV6ccCaEqotAxPB-mjixVCOcZk7vgRyV5qZ38ScfEgM8YI8ZJFMBhEx7FNoz6k6rj79JUBTqD0a5Gah1VAXrwHrIpaSz0Yyi9KhgIenIn7XWFG2jhDfnD_rRzQIhfC6mbZk0xGV_yq-3ZWRYOkyW7m2BqIpz1M2ktF1Mk8q02NgFM-73x1tpGU-QA8iPfcO-6_6-pmC8eQdHEShZ98cdYT1ChNh0OY81A4AWfe1Qq2ufedMgxFxc3TMNkCaJUJtXHkeupJlGdLLUndVUv84Ni819lSPc7jihWF8)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbVlbCBwXZD2rZUrxhwe2UvD5uobJemF97L8j5eFobg0UNsBWJs1f9e6c_UX_FEbU_01TrSsD3XDze7IKB-Dx3-xqkgTaJLbpM7aPOS5-4aOAkdyp1PqPGWNVytuVL_OSeZiH70LHjxQ==)
32. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZHaFbjzjbTWY2Trd8pGPEgZsO4JqUIPiD8ePc1NGdaGmS6Gl8Y4zmRuSKil5_x8k_SM245xIOVFtGE-jxjOoQ9ToqCFFv0o_uikWkdyRrQgriGbivkrmVMfEhzX5tn-flBJUTjVCcT4dA0XG_60W1UNesy9Mh9eIrng==)
33. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECUDQpHD4KUghUCTFWROi6ozsMCXYLMz5ztEjwS5T1Cp_6wsq2XDGmHBzz4kidSH8HisdgQgY2B8D9pgBS9zAcwAyJf6CijUi3QsZkUCvtGjr68t_Ayug-7KkOnWCr0je-03ipepTKHA1cIxvfO6sK03xIvsB-RUPkCzw=)
34. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5GDjvIMUnPXmqQ2XJwOof5CwJ-uepK87L0xb9AYJ7M3496MEO-tZ07fLQc8D2GzUneHlD7MiRld_GWpT2FnDgl-FVfDfIwbHqVfBJrZxrCQu00-CbjvtVu0sApnvt4TgmEXBC5MtUKXVEunOYA_mB4g==)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0H4amGlamfn2MkmUVqkgP7-bC9jW30WycDFElWriBD7T4Nb2eQpVQt9CiRCB4W7LnN4Ud68gYfEe6YJcPbXgHM62ZG_jiHcnLQ5FkpznTes8JbZeGyz6wD5A8sdl6xNZh8NCtFomTlg7y3kq3furZApv6NHAaupMKw5MDUm91CgMPJxDb5ZVc5OWgQJK1ZqlIRT4wWxgUm-T7wPTBJAQQCu4M4kNX9BUTPwjZ1LNENrZQVjqT1t7gRru0B98Qoakl6KCNfQEELPogPAN6Ni8Chcs=)
36. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa5vXXdiB8f0c3Inf4m-MBO82fmsIV8wdVA2AQCbM8eX-D3XOZ6C7Kdh_7aaSyo6IYWQt45YlgeKGcknBHqHstO84irxGoThBnJMysLgeyPNJJNzX3DgoqBmCE3qkwfJMX-i-G3LMLXL-ZX6cvvGFYarV2C-caojpfbBQ=)
37. [cytosurge.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaB8LSWC1PFbl8vW2JMZWP4TwJSLvKdXeAiRxxMtpPeUCsFMzhNN_1pgr_xpb_jGLgPRalDz-ou-44G2M-RP_iD7jHeH8tjcnfCNY_VO-cCMJccnvtOFFe7BbpqfcMLnMxmHU2aZgdBvM5-RiQMvk=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl_xFsGrENZeH8zHABJSBYKM5Oegiz3NLWsQR9EaBDfAFtUNqCvLV5a8eUVF5-QlkI_iPlfuooSFtYFI6Re3qZVCFgl1MYh093gertBrXe8bh-j150BxziW3Qs-7_EYlgoQia1xGt19OULBMhMyL2206ENNeDtXIGZS-dpsSIqoRYtFTr8t6XVTCm7GUkqOdZOVzIbMdB-sC2id0d8UBAULuy9i-IdHuvKlZs=)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESiEbpfzh9oGlU-S6iw4iZ8j4_Pmn6Lru8my2jLQVjFfVYCmjnYCOdgzk0FlXQSIeFmaHcgAiR07ZaRWDEL5SJcfXOnpJxwPdQetMwbts8p4-CUMnHct3g2Y0B0QddFuvZ19alDo5a6piYVeWsyen1gUK6q2vEQYGWStIbBSa83SNl172eRgjHeAg2OapqZyvueapyi7n7OTnzILaTehlHX4w9njTAKy4yqK9TWqQ9lIRJ5jym6odqtZPy-e705JTF)
40. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFye7EhOnPQAxVEiN5vsA_ack6MWGZk8vEy1NHkmv0w1MKYZX2F_q8Sc5IMKk_eZG36hfwZDuC9jLYCDQ0SIjNe70xjMgo7-OPApPxnRR59Se7arfEPniEzGBPS9G2TEXA2tpdHLHGKkjqeiEnahj6L-6mkdbsoleXLPshHaUNqV0micZQ=)
41. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3wW8hUXlIMAkACC34j6ZsrZtJ0HkewjLxaCNkblyufMtnG6qQwtgsDgCe03W6C7NCwgLAxdmXQYxJxDPDoJOUrsECxMq9faeN7r_VdlaybgcEJwQfu3ZGr-18ew==)
42. [princeton.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6f0k5gSWuKgYz80KQXKhuiPC0lSNQi0_vaLMCBpEPTu6UUvYOiFw4b1Z-IDb5Y1lyLEPXSbfkSstSQjkIlblbBM85SOW_MTCgFqcNqpRWF1Oy_0j282TZrMrrxkgy0D98adKm_newOp5oi5HrFfQOqN_b3fT8Eo5Xr7crfnXTbtjWhmnTwBUasBqLD48SsY5f_OIIe-hBteza9RKyNjSS7__CYtE1-dRwljJqVw==)
43. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT8aS9vFsKqStRYZKPYljzyOsdqtG9j-Cjse3sTQihEpSlvcJfxgTDhxu6bVY-Cx4jkDPHftbOkerNHxyGAApUVgP5pOWBL5be0b97_-ZgnfukV5NzfxhOkY5Zm71bSRP44KNN3yLosA==)
44. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBhTRUh8KOCGaeh8w87aFYx3cPU460EJbG2UXHm1E3eBFZiD0uxMlwTo3XhfROrgEv4g4RdiZRoK1joVWgX-H_17BM8y0gb7_lasB0BRzkTD-a1c2VNIA-_6u62a8A2lWqMODrIafcYnKEAYfB20eFW4oEQjn19WFp-UU=)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUPXxmIxjdZY_f5wyOa4Px76xofm7YX3qZDKiBhGGGeY9DTN84AWtNTWKbQQZXCZ-lB97VARJJgPLGgh9UiVq4UOejhKeqNP4PD8JM4uG3uoVngfX5WpfuXk4b5UAbMxSCa9HOVYo5)
46. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERFgsea5PJROXOpmvdLJvIRe1UHPg-DK2GpmplQ_qtGQj-AlBK8muvJyL-MSX0QDbgrVZ5VjbbnJJ_AAYYwqN7--mt5M2VNCGfx4mcf09A5VRV5LasqJcpi2ACCuyEtU0vPM9eAQ8m)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvxQ9n1At0yu_HJzhlBrcG9lePU0YX4kHMA48YHbgxdgm1x73MXCj-JCH9eWUq26CTXrgnQTN5JmJTn1u7LMejth31De3UUMzRIHHj-lwDvsZWM3b7aFHG_20-nXj0oNCd7SD4d6C0)
48. [ecancer.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWDZpmwT3qjqGrCA9kQwOeuqsWXfp7AhGWiARe-ICvQFrgPkvhtZwJD1QLpk18c8-MreUgQkn9qC9bpQLG1fiiqivDC2dWPGz30cblidEMLacItxmSuzNFWyi2fkT_arRg_GQaMIhPjLYBULF9zmADPE23DOiPbQZSBJC5R45XB2Hr96ttsUuHJvY4IQqx_mrvsJ3SXrVkp2KgPyw8f9Q4cnBZZvvrCwHJmDuExosCfD_MkRvs)
49. [springermedizin.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENtsHDH-ibIQQnAhOChs31oLlmMTX4SCJyQeiJptfwIq_ORJ1vsdtnKZwyC4ffzpth-plkqILFnbok6_GN0ztlx6AJWP4zT630YLEfAcq6i7mwrOhikZgbBojYLm6CFTvM1foP3K0Y4zHXiveKzyORqMJtD_AqvV4Mg4fwmbR26XKBEcNcklvPJZM9Z-O-T1I-AqZZJgA8ZwkgDajbkQ==)
50. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWg8mfG1vV6JHvzb9LKtTidT-lynog8YNSoQsxySqDWGtwSHC-yebAkGCPb6KXXwSR6awePC6A2sjnOkSyNqyETf5xErEXdj8VikEYEsVWhUbtqiSoYFiW3Xyo1JpkXbTDl-tuA31p)
51. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNR5hwF-fYvpMiyn6ALnLi42F8-Bzps2DSsZMRI4DYptNDR7-OLZ-6YdspJBPFiMpXW3xjWJzk4ZcQn1MZu53p4F1C9WatRNFZXYvV6kfEPVEWzJb8lECtQ8iYE6QdAhXHStqAmKRvyDkqjKmKRLpP4SQVtWyxQnnoYN3iVfnEBKoQZmeW9DFsLuc_jKL3O_BQb3gvbr1qRJRv_ehbg7aw0Uk=)
52. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpf75Rix9cYc6Fi-TJgstoy73EGjvkRyyVaUcpOKW4jym1JD1p0mHbJ7mPZrxeBaifeY-kEfvTHh6yIaT-SdTf3xMmNom7CuHowOKUgyLMlq81PpjGKq0ePS62P7z5jw6_)
53. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuZXvUhaUyt3LMtJ6qsvHRMxJ5i-dNeQ8xbz6ytkPSPD-kw90drGWotlZduldnIuRzDDcGnRLVsRN1AvTqkIn64vPlZ-VTs07wyvuCU8kdWu_-xH47UJyBKDPzjZhOQT7W)
54. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhMlv4-JbRv7rz7pWVnZlDpWSPbGSNQQO4Jpn_23yNJCcnOmYmQ0gWCserLaXkshOvI2vKWIvzxbCEKoibmB1DGFDwj66wiiJy6OhS30JlzaT7vo9cHyt1LUm4ixJ-Bw==)
55. [thejoneslaboratory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnsNEUrz6zfQzm0R5gQFid7b1V7cCeuZIb5oBaPMGWUCvQlQMPB6BdameI5smR4-UWshbB2BbELduIxWERTKP9NfzBqf_ZFAEGV1AaTY2urm-th06d_D0_0t2-sVNUBi0fw-Piyw==)
56. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsoW6Wz_Nfvww8jNY2nsRcKR2Jnz2RRqtOk3YJGvy2IWHLbysINivlIKMGaYMLHvLKU-Icdf-pLpMQrUeYGj4EPjLum7-TzLOFfRnGBoSdWmDwTGyybMj3SvEtfDY3VqG12n-EF0QH)
57. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJQp-AGAu4s9Yu83eliA__OcYjA-S16jjqoHTywRODQJS2srHDnACtSLCTzXSToFe7trA_yglgGBEzVdw7n1ngzjZW87Vlh-v0RMXwkw2fK-xMPlFJLqvSKVoF2ut_nQ==)
58. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWQkJ1_FTfFX03ONIHi64Fi6sMz5_kToyZGN8Xl41_ovEtBjwoMV1L2uAgfl7J03qTaxJLSCciJ30lkIpTRXadMTXol6Bb4RfUI924C15NlwEqTywYC3_r_LK21UJm_BGorICCKgSvDY6p-juxhQ4Cr9SFvaY6Ffd8yVOPVn2gBxNpBLai9b1bmrCDI-o9cNhU0OSkkZvfy0vJUK_uwtg6Gzeu0QT2Cf9KriIpvwP5)
59. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUEKf30aW5i1rGouhwQRvmK8GIcEea4vzUpMHxJtA7r91EwpL5heeV5Vo2iSuC-205kj2nx0rjnGk0thmiIq3i9pZPnxyDsPEFBtynKIcvvTcNZUwcyLg4CDD3DGc6A8jR64tXeAJ9Sw==)
60. [techscience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgx5ODBO6Pn77sZm5arUTdPm5NFPIIAxZdkvWcbKYhBsGCX_SFzKV2DJp71OG2ABBkeH-fbCfNrbraF9n7oPzetRAmy4lZH9uLdXWPWeEmYJJ7eSjJCpJCGCCTwmJ900a28L0Ce6ogSywb)
61. [ucsf.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP9lNX4NV5OH83_IOS8WtFQcw7cr3S1o_IcnAIA4VAVEblWe7gBzgRODvNbDI4H4IGO2mfupPhzv8CcyTXgRRbc-pGdW0lzMaw6R_M7pKjhyg1J6DAwwj80Q==)
62. [cytosurge.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkCyLI0kywoLGODwWB2dAtxjeLNA1HwHTbkokIETTSjKVaIOGf0IZ97SmG5beeO26exeiyNte8SccVEV1KW8Dtxuk37XqNpuoCkAGsA7pJR9kwL_90mvrN2TF_5rMVcDrxG8CtdwO84OvrMECqNy3qzA==)
63. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3141bdV29djhuSTdRKjpjQMmZuUoJoB8Ef2Fs1x_og9Esr313tmIzFxdZQrJrImBYdxvmdqqg_ZimoRJ0AuA5X_PHPaL0yOmX2h6fUSpviMBKiLSmfN2mPNQBJ2FUtW9i_sAHNz6j)
64. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQxYTbDfJGP5x_nhLOrJG_-3QbPohb1LpN2eGVpF-5Z0Gp73bbdon6kPwZuS6_oZ1fmv0EPl77ir4fmjsbRZ5d7od6UCCV2dP1XSELYzSdeNN4vkkxB1sEmaTpT47V2w==)
65. [annualreviews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY_iDSdUmRkzSrj_YFfoT01QmL6QR2AXe_YQzqeCpALh8RfVB3sXxjfjmgpKZSogy3qncrTPbqZahNPUFOgylmAh7_cy2Nf4cTgvZ86cvP4XfzSJ597Py2QLJpvp3gm6KBIdNDrDKzfGIREdGD2AUZnTnfWfAaJNBoQbihptw2)
66. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_pAzlEI3XxXlYnYmiLA_StS326pB_I9yavieQSKOn4b9ClBE1xUq9Ee79lm6ezZAnEIdFfwQ4CTSJQ2fNjGuV9osk4X04pDU3reox5AX-UXtKP4wZBZ20x8H1svgTddZhG0oMP_oGMc63yQPQEQprIRcAgaaW9fRPtBKXfIyP0eA1Z4uljjGelymQ2uQ4HHRNbfTFbgWapKPS_GjE0Zc9zjLYi0ZCqu6QLMAY_X4N)
67. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0eNTyS30V_N9h4C3yNdFrUhMhrjV7DP-wKY6jBmtn0OdvyTpmSFX3bbkYpaidBi1IaEFAYJNnFqlpIvRqmxj9hIkexYasnO3Zz3rGUGSE7GVTsJIbFpJYzHtlg2EKKvyoqxAtjNKV7w==)
68. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIfq1i5YvDJUwx8_lDTQznmLpHh8YC1rnPSlZZtY27_CnxARewAe3YIVtMdxYBT-llVnWRJDO97HKY6zeOjfHP1Xy9dnpKXbugln23getYq9Is0JMp_hiQpCcLqKxw7nEbgWkCyD42JQ==)
69. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZcxmh-HvkO2kaTo1nmIiRERBzGK03WybzbxpdcZ2WAKC-CmtfzCNyH_sdr1vvKVBG0bhZtIPL5cQzNbq72P0VYsLLYtFYBh1NROzN_GYbTGL1mNtkPIYfukmVopf8JvizxYTWsB9gnccV7myw6DHl-_oliebl8HPE0i-0p3o0ApTR834EDBdGT_SX7Mu4wsqi8kNLLs08J44X5J5ht8ndaP0YeicQHw==)
70. [hubrecht.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfId_Ib9VGLy8-AcEnjdg79DigMVwnwvICDwy4O_NBRyoRspdJif-IWqhSFDL0K6WohSB6VVTN4WLX3Hp_IZKSCCAWHDMwj8SZ8GOyyALRN5CrGNj3oNen9xfDkhuzx-Udy7tT4yfQ4ve5iuL6)
71. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtjv5bVNwibOigIoHrdJSlzIjwq1aigtgn_lO0jXy5SpRe_MGs6aQMHFXu7LQ_NTvZu90SrF5lsavBkU4Tsyj5X4L_UoUITeubA6lX2zXGU-WkZx996LHB72pnuPlmaa48HLcjN89wgpCyqa8CmTLDpSq8mkhr_-eY9lT9-34Q20PrhfaH10WxwGnRvU4OFWcYoRR5lkMlWomUBFiR94_fO5fiX5a6du-xYP0pKt5KfERVhNAaZnU3Tsfl-PiEAiuHG_UST__42B7cXG9a8e26ay311_rDJ5X7WiTKGsq-M7BfENg=)
72. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbamp5iguvZPLhxfWNzgygl6c44qbaQs_AITzpEIKki4yEVpvb2OKlviuA5i7UY3ik49fDgUV6oXnn0ACrw2KN9aUjZ34Oq2PgxNpScJGQKdJhEB-3OlUU_6AkObG3kttLrkfjSm_TXIJgG8J_C71eLkpufUjySLUV6SrZDeiNvPBrJgB_-TOmGEcEn3qMNkyL33uKmJu3PnY2S7-W3GL3Qzl5PxLXoTj4JlcLx1fzya1z6RVRmWk=)
73. [sc-best-practices.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhdtQgeGcOssfIRusul4jhbweU40Uf7TIF94hW0ASaXdj51gTnoBYHDIWqu2tMDYBxlUa5qS6Rco5l00Ds0w_ldD8sfBiwbhYWZz2Y_WI6AoRSILO6pPuq_LsfTdCZh2PI1bofmXAZeiLwQkfC3mTuhN6qlFmnsVA=)
74. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZXObW1NXQTST-XqCy8U4b44FHVEXB8QsRspzS1HnK-gnrLcBti_OY4zzXT3B81_fvQ15zA-5zDKLyrKILuSk8jP-SB1qtTEFU44Kdt2jjW3wEjeqfTvev-alEgej6xyAwu3iQd7kavA==)
75. [jci.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU-fRr3I2gqDkrPP7v4sVyzecZReZ0VIQsTYxsWm2GEitFh4bIDVdmoHG6lDdInuHz03Xo_ki6DUsssdn9N6wgakn6IpA3XPnH_GFqUUz-H1FIEsc5aDiRLf2LQGCg)
76. [annualreviews.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8TMQphe-4xJ5q9DYcHQOOhFtr3YGi39VZu91JXLUpJRZb52dE4jBQde7lKvCTmVHIlDPGpyxDKo5H260tRByt-2g1_uP57QWO25qprVzFi0DEXVZyy4ypnUeCiLgyME8rhbrVdWy6YN-FbNBeg2g6YILsWLpAOvD_Gix-OQm75RarStAUb4jlPhp3QQ==)
77. [rug.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER8XWZQgWBTR3XhtRC9jkssATTODoI9l__dcYM05wto2tsHstNn17xk_5ILZs_iw7AZlEDwBFoDX6eotLx6I2pgb5g6SGl0qJmcoQ6eTsCWvRAr2UVzvo6gu6be4p5QKB7R2PUxziYnGig)
78. [biologists.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGcW20-gteK7u3Ibh5ScvI3enJAoLCZ7jLVKIoF1dd6AXa_qnLGDqfVyErOp7n_Px8b-Hu-vWWudNPmu85bWRTbcmg-Z5Oc8DGBY35HB3wWrdVg4vyvysfPbcFzBHjHHA8EyMKKjhIPSVAoJQgq2mfk03axzoN8XTRWXUp12AkbI_0_nCRw8GyrG1XUZ3DaArbyplAXO7Y41gEcnL_m-ivSXR3JyvV8nzo)
79. [anderssonlab.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2362MZaYLrIq1EYrJNtJEn3h60xf2FxU_7mzn-3kXrsDC5f02H-XxK9GQ1zZ-jOgY2JkESbjZTVAdwfhcTD1gWvBLoYdLOymmX2rIYak=)
80. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0De1ccKWb3aLGM2M6tQpMoTCIaImGnJ6tOzA_R3vGGygRvz41Du7o-cgiHl-0pVh5njlKODlAhuPFa0syR3VB0JNPT2of2pGCPgDSzZ3jK_e1y4udkEXUmjHbAEj1HIWi4ZwGI8iw7CCryrIIaQ==)
81. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMGT4fWMHeU_soCzokoImM6f-UrZZvUNEnWwcJJ9f9FBaT1YtvYu0nvb7KH3YWqah7m6x4SQexaIZvff9CWWO_k1GGWKSgepiR7HK2yzZQ9GEHZTlfcCGh2Jd5iszcOYGFnXKpkbfRIr77w012ItiJrqG0YUlCCmmIgGyvApMy0TfKJwlL7hJHj7J4Eh8kqpVb500yLAE=)
82. [consensus.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRrAa5TTgCYRqcCQAD4JAW-iSCRO8pWJVBYDyFISrn1X16pyJxLpOkt3gCdlkLd-PhTzsUdrhB8aBm5P9mdKkB5iz_b1Q-tBVNgej0q80of2C5Qpe6rxrybSLUiThEkpZKMl8Nx3yX0OQ_5O3p0GYOXRbrfrlplD6SmFX24-dogeHhkEDp3hVtigeErHzjUKZLgbUcCJmidOpdUHzdPOl-GVP5teKQDhnbgXTAyifClHsbp-RRvZsR2cMU)
83. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFauAe8RB2HJi0Lc1b9RhTIb5LxBXEBgdpkvCTXtv4fgKQX-ZZek2FFcFGUkql86jzaj5gu-l16ATM2Go0OoDdUzN0pE9lRf-iaMuan7wSCESPjKR12Pc5RD9PK0AbsEbkn9_1ONZaIooMLhJGGkZluAJoLu3i7msYpCQAqFyt5VkBOR_kAjAxLz-uRU-MdSifYvZ2StE1OPWCq-L1nKHVleopaj89kEgFouTObbZqiEqCAQbXE7HS5tIXGlc3prm7sowXIdoz_VJmgxuhbmg==)
84. [advancedsciencenews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH22QIq6kLByXmUFeYTbdeFyxPYbJuzRKF3wOoE5X-iZqTzVy9ns8zVgbMwRRDzMoPwSJzW9Zi5UvIQyX_5X1VMe3AKWexEYkbih9sZa708iNNflCcnZMG0TRD1G0BD2NJ_5O0nW3viH1XX49Rk7wM5fe83ax_zFTdTam9ddH9pTrqek_tLWJRxgZVeniVszpizkTqTfW9QDjCGvClHRgMdjE5fVgtV3A==)
85. [mdc-berlin.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU6oyBMAlmSx_6kPkoEfJdUlU_FA3xbxdPGTSDiA8k1wGSw0FIFMF9A3_Y8gIHuFYnQ-BWkgINYLyq8anoguBNHK2PqEVd7wEwBzXDtcPWOQo4g0Yhpvl6LYnvZHPF4Pjkm8ZkPPsP3zQN5Z75rpqivS0d2-XD0mVMB9IuVFXkLww3-5mHQQn4ehmD85ZKLc26wH5Z0XnrpkWKZ0jk4kXL)
86. [mskcc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlH6yt9HdmDCy59GFcezyjdbnV-hlwBomcvUlWBRls9amVwjk25wPFrmTrnrPvCIBS7S_KGxA0QlKF3T3AHmCDSr84mcy_5Vtn2eDvyzXljWkQrYbdeutDOTq_Cexn44SPdHGVeyYZZQDPWRL9RkRw5L2FD2E_6Pf_)
87. [dntb.gov.ua](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwGgN0WCHRjG-wbrDX3Lr3pqmIPc94dMp3xao4mWAZgHC3oy6aJGch4PZ819zjT5aLHb8AmMnZrIjdaM5DVIhj8QducuSKcfWtuU0eRC1KvT63NkuLcouJkjTJwZYvE3Yp)
88. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbkGoRYTKUiXMgRkb-uHcvre9aUS8SBO7KdI9n-4ruTnQJtevf-F5AuNLIeQdvKmHWCCOLrjnEhs1P621YhNzo6jjd51M1ItgOME4oQ1wazPYhMW94GPYHPi3v4HO08w==)
89. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTMf-cDV-XpQc-NNHjHUqWDr3vb9quI7CyXFTU9J00ffo_gXHYJ03QJ9CrssHKjUZ97d2OBJhJsoL1Vxdm1w66iPj5afV7CZuNGK6CIVqRukY7xP0mx-B8kWxJ13OI9g==)
90. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvYZ5Fy-ONpKiSZtwb5ZJCc-p1FL25RW92y_QwciUEGwk3kzIm4dpzwEl7Mu_14G20gtGSZcvxLxdN7afqpNvaFcVi3ndlHXYT7osAlJ9vNfP2R0oa0RcDsBRfzO3_LELLYMVAplJR)
91. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEG65OB-e6wjEvgwBVcTAF-IrEYgebMGfrSN4MJ9RQ35M8RCAOPlIG3OZ1ajYwxSUlJUZYxFjdtxHZwaiDP7FatVKeJo43SoYf-aszN9u2142PdWRAZIEAzIHECyOjiI2Z)
92. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvftnH7dk5X3jczX-eZ0e1UKfU1pPVSQHf4L-Y6fHiAVD3f8P2CO_1oCthIdrdr6Ryq0FYneyNn2sbZvHXj-gH2cwUm5Ep8z_r4A3PWd1x0uQtzFNmGpuAlbdYiWuy6Q==)
93. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-h1kO1GByQGB99kwwhUtqf6rG5NUulqhedoAB6WMSkvLNrJbDSnxfaMIvhKDtYVdbtWIuF56Sfzk8SPWyMY9CHfA-smg8pMgA-I4durkEZ95Hf9sjInysSJVrQWVdGw==)
94. [springernature.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_5jctgeBRtdKR-wRah6z3d8sudCnIAgwqoIYBuEqvRdIm6Vji71-is7CUMhMU8--6CO_ggNwDCCxaL9772Us7AvdgKTLqVZyd0PzBErcprl3UWdaDmrvhtO3FxSX7fOYwfRzgqm7SEq0GITbDdhCLg85KzGUTBh7thUEoKYS2blyQ)
95. [washington.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr4lw4dx_rzwPP8UojZhmNkf2jweRFNwBPAtvdAgk3a8tHa-2XBdQkEPBr7TpRTGS7JNN0ZKiD-H_yKRpXIDRw6_6z4dLCiMAdS2PdciJW1p6KcoYgZaQd)
