# A survey of community detection methods in multilayer networks

# Abstract

Community detection is one of the most popular researches in a variety of complex systems, ranging from biology to sociology. In recent years, there’s an increasing focus on the rapid development of more complicated networks, namely multilayer networks. Communities in a single-layer network are groups of nodes that are more strongly connected among themselves than the others, while in multilayer networks, a group of well-connected nodes are shared in multiple layers. Most traditional algorithms can rarely perform well on a multilayer network without modifications. Thus, in this paper, we offer overall comparisons of existing works and analyze several representative algorithms, providing a comprehensive understanding of community detection methods in multilayer networks. The comparison results indicate that the promoting of algorithm efficiency and the extending for general multilayer networks are also expected in the forthcoming studies.


# 1 Introduction

Network theory is an important tool for describing and analyzing complex systems throughout a variety of disciplines. Community structures, defined as groups of nodes that are more densely connected than with rest of the network, are widely existed in many real-world complex systems, such as sociology, biology, transportation systems, and so on (Newman 2018). Discovering communities in these systems has become a primary approach to understand how network structure relates to system behaviors. As an effective technique to unveil the underlying structures, community detection has been utilized in many scenarios, such as finding potential friends in social media (Zhu et al. 2017), recommending products for users (Li and Zhang 2020), analyzing social opinions (Wang et al. 2017), and so on.

With the deepening of research, more and more scholars come to realize that simply uncovering communities in a single network is insufficient to analyze the structures and system behaviors in real-life applications. Unlike the community structure in single-layer networks, communities in multilayer networks are comprised of a group of well-connected nodes in all layers. For example, individuals in social networks may have various interactions (e.g. sending emails, participating in the same activity) among them (Ansari et al. 2011). As a result, the conventional studies are encountering with an essential problem of how to utilize the multiple views of the network (Papalexakis et al. 2013). There are also similar scenarios with relevant notations such as multiplex networks (Verbrugge 1979), multilevel networks (Wang et al. 2013), network of networks (Gao et al. 2011), interdependent networks (Buldyrev et al. 2010), multi-dimensional networks (Berlingerio et al. 2011c), which can be generally regarded as multilayer networks (Kivelä et al. 2014). As more interaction information implied, community detection in multilayer networks has been introduced to leverage various relationships to get more accurate results (Liu et al. 2018).

# 1.1 Background

The research of complex networks oriented from graph theory, which is started from the “Seven Bridges of Königsberg” problem in 1736. Although naive in many respects, this approach has been extremely successful in many real-life applications. At the end of the 20th century, by employing the graph model, the famous small-world (Watts and Strogatz 1998) and scale-free (Barabási and Albert 1999) features were discovered (Newman 2018). In 2002, Girvan and Newman uncovered the community structure in networks (Girvan and Newman 2002), which opened up a continuous upsurge of relevant research. The so-called community structures are groups of nodes that are more strongly or frequently connected among themselves than with the others. Therefore, community detection is proposed to find the most reasonable partitions of a network via observed topological structures. Several conventional approaches are listed in Table 1.

In recent years, a sea of improved algorithms based on the above approaches are proposed with fruitful results. However, with the exponential growth of data scale, community detection on large volume data has encountered a serious of problems. For example, some datasets are changing with time, which brings challenges for traditional research on a static graph. In other words, traditional methods are incapable of dealing with large-scale time-varying networks.

<html><body><table><tr><td>Name</td><td>Parameters</td><td>Complexity</td><td>Strategy</td></tr><tr><td>GN (Girvan and Newman 2002)</td><td>一</td><td>0(nm2)</td><td>Removal of edges with maximum betweenness</td></tr><tr><td>FN, CNM (Girvan and Newman 2002)</td><td>一</td><td>O(n²), O(n log² n)</td><td>Greedy modularity maximization</td></tr><tr><td>LPA (Raghavan et al. 2007)</td><td>i</td><td>0(n)</td><td>Label propagation</td></tr><tr><td>EM (Newman and Leicht 2007)</td><td>k,i</td><td>O(nki)</td><td>Probabilistic mixture models</td></tr><tr><td>SCAN (Xu et al. 2007)</td><td>ε,μ</td><td>0(n)</td><td>Structural clustering</td></tr><tr><td>Louvain (Blondel et al. 2008)</td><td>二</td><td>O(n log n)</td><td>Multilevel modularity maximization</td></tr><tr><td>LFM (Lancichineti et al. 2009)</td><td>α</td><td>0(n21ogn)</td><td>Local optimization</td></tr><tr><td>INFOMAP (Rosvall and Bergstrom 2008; Yiapanis et al. 2013)</td><td>T</td><td>O(m(n+ m))</td><td>Information compression</td></tr><tr><td>NMF (Zhang et al. 2007)</td><td></td><td>0(hkn2)</td><td>Nonnegative matrix factorization</td></tr></table></body></html>

depicts the number of edges. GN is short for Girvan–Newman Algorithm. FN is from Clauset, Newman, and Moore

Lancichinetti et al. (2009) raise two problems: The first one is about hierarchical structure, which means large communities are composed of small communities and in turn, large communities group together to form even larger ones. The second is overlapping communities, for example, people belong to more than one community, depending on their families, friends, professions, hobbies, etc. Nodes belong to more than one community is a pervasive scenario in networks.

Besides, the interactions among nodes are becoming more complicated than ever before. The conventional monolayer network (i.e. single-layer network) has provided plentiful cases in which a unit in a complex system is charted into a node, and the interactions between units are straightly represented as edges, no matter what type or weight of the interactions are. With the development of network modeling, we are starting to realize that the existing models cannot fully capture the details existed in some real-life problems, which even leads to incorrect descriptions of some phenomena taking place on real-world networks. Some representative problems occurred are listed as follows.

(1) Multiple interactions among social networks. There has been an increasing focus on social media such as Twitter, Facebook, and Google+, etc. People share their opinions on daily affairs, chat with friends, or even make trades on these platforms. The main problem for analyzing social networks is the multiple interactions among individuals. For example, relationships between two individuals may include friendship, kinship, or schoolmates. If we regard all the relationships as undistinguished edges, the differences will be ignored, which is probably leading to incorrect results.   
(2) Interbank trades. Online payments are replacing traditional cash payments and credit cards, which offers a convenient lifestyle, meanwhile, providing a new way for financial criminals. For example, in money laundering activities (Colladon and Remondi 2017), criminals use different channels to conduct trades. If we simply analyze the transfer records from a single bank with a graph model, the result may be unconvinced. Thus, it is necessary to collect data from all possible trade channels with a multilayer network model, in which each channel can be regarded as a layer.   
(3) Urban transportation system. The study on the urban transportation system has caused wide public concern in the last decade (Black 2018; Sultana et al. 2019). Citizens travel in a variety of ways such as bus, subway, tram, and so on. In analyzing the public transportation system, the characteristics of various modes of transportation should be fully considered, especially for some hub stations (Zhang et al. 2018b) that should be given more attention to solving traffic congestion problems. When bus routes are blocked, numerous passengers select subway alternatively, which results in crowd subway operations. Inherently, the urban transportation system is a multilayer network model.

By tackling the above problems with the multilayer network model (Kivelä et al. 2014; Boccaletti et al. 2014), we are able to get a more reasonable result, i.e., the community structures in multilayer networks benefit to identify functionally cohesive sub-units and reveal complex interactions and heterogeneous links.

# 1.2 Main contributions

There have been numerous attempts to address community detection problem in multilayer networks through diverse approaches, e.g., identifying communities in temporal networks by modularity-maximization (Bazzi et al. 2016), where the authors emphasize the difference between “null networks” and “null models” in modularity maximization and discuss the effect of interlayer edges on the multilayer modularitymaximization problem. De Bacco et al. (2017) propose a generative model for multilayer networks, which can be used to aggregate layers into clusters or to compress a dataset by identifying especially relevant or redundant layers. The proposed model is capable of incorporating community detection and link prediction for multilayer networks, and experimental results on both synthetic and real-world datasets shows its feasibility. Analyzing multilayer networks is of great importance because many interesting patterns cannot be obtained by analyzing single-layer networks. That’s our motivation for summarizing these approaches. The contributions of this work are:

(1) We build a taxonomy of community detection methods based on various techniques used.   
(2) We provide a detailed survey of works that come under different categories.   
(3) The evaluation measures for community results are categorized and summarized.   
(4) The applications of community detection in multilayer networks are introduced, as well as interesting directions for future works.

To the best of our knowledge, this is the latest work that provides a comprehensive survey on various community detection methods in multilayer networks.

# 1.3 Outline of the paper

The remainder is organized along the other 5 sections. In the next section, we start by presenting the multilayer network models with several real-world datasets and give brief comparisons on different definitions. Section 3 summarizes the existing community detection methods in multilayer networks and provides some metrics for quality evaluation. We introduce various applications of community detection in multilayer networks in Sect. 4, such as temporal networks, social networks, transportation systems, and biological systems. Section 5 offers concluding remarks and perspective ideas.

# 2 Models

As mentioned above, numerous researchers dedicated to solving the problems in their own situations. In the 1930s, sociograms (Roethlisberger and Dickson 2003) were proposed to represent social relationships in a banking room, which contains 14 individuals via 6 different types of social interactions, as shown in Fig. 1. Such networks are known as “multiplex networks” (Mucha et al. 2010) or “multi-relational networks” (Cai et al. 2005) in which edges are categorized by their types.

![](images/4f92dd2b2a70baefc2da4000df6aa73237f80e05bb94c0a7944c432c27d25c23.jpg)  
Fig. 1 The sociograms proposed by Roethlisberger et al. contains 14 individuals via 6 different types of social interactions, observed friendship ties and cliques in a factory. Position reflects the location of their workspace

In recent years, great endeavors have been made to unveil the basic mechanisms for the generation of networks with specific structural properties. The analysis of networks has profound implications in very different fields, from social media analytics to biology (Newman 2018). The conventional graph model is incapable when the network is differentiated, multipartite, integrated, and dynamic. Thus, a series of more complicated models are proposed, such as temporal networks (Kostakos 2009), multiplex networks, $k$ -partite networks, and so on (Boccaletti et al. 2014; Kivelä et al. 2014). However, the sudden and immense explosion of research on multilayer networks has also led to a great deal of confusion (Ahmed et al. 2018; Farooq and Zhu 2018; Kivelä et al. 2014; Paolucci 2018). The multilayer network we focus, in this paper, is not a neural network but a mathematic model which can be utilized to represent the complicated network structures.

A multilayer network is a network made of multiple graphs, called layers, which share the same set of nodes, but differ in their edges. To distinguish the definition of a multilayer network from a single-layer network, we intuitively compared the representation of a real-world dataset between the two models. Al Qaeda cell was isolated from a safe hiding place during training and plan terrorist attacks, which forced the organization to form a relatively dense social network, in which the Hamburg branch planned and eventually participated in the implementation of the September 11 attacks (Silber 2011). The social relationships of 9/11 terrorists are represented in Fig. 2.

![](images/220a79d1505227a3cd3c73ccbe8e8aed5a7ff340c620e7735892fb2a5e4d5c99.jpg)  
Fig. 2 The social relationships of 9/11 terrorists represented by a graph model. It is a single-layer network, which consists of 69 nodes and 159 edges. The size of the node represents the number of the neighbors (i.e., the node’s degree)

If we classify the closeness of the social actions among the terrorists, we can obtain three groups of links, abstracted into a three-layered network, as shown in Fig. 3.

It is obvious that the multilayer networks reveal more detailed information than the monolayer network. The multilayer network model contains nodes and edges from different layers, which represents the different frequencies (or types) of interactions among them.

The nodes in a multilayer network are consistent in that of graph model, which represents individuals across multiple layers likewise. Specifically, some works indicate that the nodes in a multilayer network can be classified into different categories (e.g. bipartite network), thereby the network composed of these nodes is described as a node-colored network (Baltakiene et al. 2018; Brummitt 2014; Kivelä et al. 2014). The different colors represent different types of nodes. For example, the urban transportation system mainly contains buses, subway, and so on. The bus stop and subway station make no difference in a conventional graph model but differ in a multilayer network for the different manners of transportation, thereby they are printed with different colors. Inherently, the layers’ information has covered the different node colors, i.e., the multilayer network model is a capable solution. The transportation network of Chengdu city is plotted by Muxviz (De Domenico et al. 2015b), as shown in Fig. 4.

![](images/50cea32f3d6e7e068e3eb2b5f7b9881e5517dab342771a45dcf2f06286b063e3.jpg)  
Fig. 3 The 9/11 terrorists’ interactions represented by a multilayer network. $L _ { 1 }$ presents confirmed close contact, $L _ { 2 }$ shows various recorded interactions, $L _ { 3 }$ contains potential or planed or unconfirmed interactions

![](images/4fd99933194b4618c6dedc42bcbb1fcbf0e9dcd0194498a2017291017d2e6f54.jpg)  
Fig. 4 The transportation system in Chengdu city of China, where the left layer shows the bus lines and the right layer shows the subway system. The nodes from different layers are connected by interlayer edges if the corresponding stations are within $0 . 5 \mathrm { k m }$

The edges in a multilayer network are classified into intralayer edges and interlayer edges (De Domenico et al. 2016). The intralayer edges request the two nodes of this edge are in the same layer, while the interlayer edges (or crossed layer edges) connect nodes among different layers, as illustrated in Fig. 5.

A layer in multilayer networks is composed of a set of nodes and edges, i.e., a graph model. The layers are also organized into two categories:

![](images/771f3bda2354beceb91102a328592b28e3d6587a458c6b6257ce6bf38930474c.jpg)  
Fig. 5 A three-layered toy network. The edges in each layer are called intralayer edges, as marked by solid lines, the dashed lines crossed adjacent layers represent interlayer edges

– Ordinal layers. The layers are sorted by a certain order, in which the interlayer edges connect the corresponding nodes in the adjacent layers. Take temporal networks for example, there are numerous layers representing different snapshots, but the order of layers is decided by the time sequence.

– Categorical layers. The layers are classified into several groups, where each group represents a type of interaction.

# 2.1 Definitions

There are many terms for describing multilayer networks, such as multiplex network, multi-relational network, edge-colored network, node-colored network, multilevel network, multi-dimensional network, independent networks, networks of networks, temporal network and so on (Boccaletti et al. 2014; Kivelä et al. 2014). Table 2 summarizes the main notations used throughout this paper.

As we have known, a graph is a tuple $G = \left( V , E \right)$ , where $V$ is a set of nodes and $E \subseteq V \times V$ is the set of edges that connect pairs of nodes (Bollobás 2013). The model of multilayer networks is more complicated and there are mainly two kinds of explanations. One is summarized by Kivelä et al. (2014), described as

$$
\mathcal { M } = ( V _ { M } , E _ { M } , V , \mathcal { L } ) ,
$$

where $V _ { M } \subseteq V \times \mathcal { L } _ { 1 } \times \mathcal { L } _ { 2 } \times \cdot \cdot \cdot \times \mathcal { L } _ { d }$ , $E _ { M } \subseteq V _ { M } \times V _ { M }$ . They employed a sequence $\mathcal { L }$ , described as

$$
\begin{array} { r } { \mathcal { L } = \{ \mathcal { L } _ { \alpha } \} _ { \alpha = 1 } ^ { d } , } \end{array}
$$

Table 2 Main symbols used in this paper   

<html><body><table><tr><td>Symbol</td><td>Scenario</td><td>Description</td></tr><tr><td>R</td><td>General definitions</td><td>Set of real numbers</td></tr><tr><td>G</td><td>Monolayer</td><td>A graph or a monolayer network</td></tr><tr><td>n</td><td>Monolayer</td><td>The number of nodes</td></tr><tr><td>m</td><td>Monolayer</td><td>The number of edges</td></tr><tr><td>V</td><td>Monolayer</td><td>Node set in a graph or monolayer networks</td></tr><tr><td>E</td><td>Monolayer</td><td>Edge set in a graph or monolayer networks</td></tr><tr><td>ki</td><td>Monolayer</td><td>The degree of node i</td></tr><tr><td>r(i)</td><td>Monolayer</td><td>The neighbors of node i</td></tr><tr><td>Q</td><td>Monolayer</td><td>Modularity (Newman and Girvan 2004)</td></tr><tr><td>D</td><td>Monolayer</td><td>Modularity density (Li et al.2008)</td></tr><tr><td>S</td><td>Monolayer</td><td>Surprise (Aldecoa and Marin 2011)</td></tr><tr><td>L</td><td>Multilayer</td><td>The total number of layers</td></tr><tr><td>g</td><td>Multilayer</td><td>A multilayer network comprised of graphs</td></tr><tr><td>C</td><td>Multilayer</td><td>Collection of interlayer edges</td></tr><tr><td>α</td><td>Multilayer</td><td>Aspect (Kivelä et al.2014) or layer</td></tr><tr><td>Gα</td><td>Multilayer</td><td>A graph of layer α</td></tr><tr><td>Va</td><td>Multilayer</td><td>Node set in layer α</td></tr><tr><td>Eα</td><td>Multilayer</td><td>Edge set in a layer α</td></tr><tr><td>L</td><td>Multilayer</td><td>Collection of layers</td></tr><tr><td>LQ</td><td> Multilayer</td><td>Elementary layer α</td></tr><tr><td>M</td><td>Multilayer</td><td>Multilayer network model</td></tr><tr><td>M</td><td>Multilayer</td><td>The supra-adjacency matrix</td></tr><tr><td>Aα</td><td>Multilayer</td><td>The adjacency matrix of layer α</td></tr><tr><td>laβ</td><td>multilayer</td><td>The interlayer edges between layer α and β</td></tr><tr><td>K</td><td> Multilayer</td><td>The degree of node i in layer α</td></tr><tr><td>Qm</td><td> Multilayer</td><td>Modularity for multiplex networks</td></tr><tr><td>pc</td><td>Miscellaneous</td><td>Redundancy index</td></tr><tr><td>8</td><td>Miscellaneous</td><td>Kronecker delta</td></tr></table></body></html>

where $\alpha$ is called aspect, and $\mathcal { L } _ { \alpha }$ depicts an elementary layer. The layer is a product of elementary layers, which can be represented as $\mathcal { L } _ { 1 } \times \mathcal { L } _ { 2 } \times \cdots \times \mathcal { L } _ { d } .$ . The illustration of the multilayer network is given in Fig. 6.

Another model is proposed by Boccaletti et al. (2014), defined as

$$
{ \mathcal { M } } = ( { \mathcal { G } } , { \mathcal { C } } ) ,
$$

where $\mathcal { G } = \{ G _ { \alpha } ; \alpha \in \{ 1 , \dots , L \} \}$ is a family of (directed or undirected weighted or unweighted) graphs $G _ { \alpha } = ( V _ { \alpha } , E _ { \alpha } )$ , which represents layers of $\mathcal { M }$ and $\mathcal { C }$ depicts the

![](images/fa98b9c03e408d579931cc78dc4e3f268d71e4ef171c06287a51e54b21e92914.jpg)  
Fig. 6 The illustrated multilayer network model proposed by Kivelä et al. As shown in the left panel, the multilayer network has a total of four nodes, so $V = 1 , 2 , 3 , 4$ . There are two aspects, which has corresponding elementary-layer sets ${ \mathcal { L } } _ { 1 } = \{ A , B \}$ and $\mathcal { L } _ { 2 } = \{ X , Y \}$ . Therefore, there are four layers: $( A , X )$ , ( A, Y ), $( B , X )$ , and $( B , Y )$ . The right panel shows the representation of the conventional graph model with multiple labels of nodes

interactions between nodes of any two different layer, given by

$$
\mathcal { C } = \{ E _ { \alpha \beta } \subseteq V _ { \alpha } \times V _ { \beta } ; \alpha , \beta \in 1 , \ldots , L , \alpha \neq \beta \} ,
$$

The two models differ in the definition of “aspect”. Kivelä’s model takes into account real-life situations, e.g., a social network contains relations among various types, timeline or situations. Each relation set is regarded as an aspect, namely a classification of layers, providing a comprehensive perspective. Thus, it is more considerate. The structure with aspects concept is much richer than that of ordinary networks. Possible aspects include different types of interactions or communication channels, different subsystems, different spatial locations, different points in time, and so on (De Domenico et al. 2016). However, Boccaletti’s model is a general form that easy to understand. Specifically, the supra-adjacency matrix is a distinct tool for representation of a multilayer network, defined as

$$
\mathcal { M } = \left[ \begin{array} { c c c c } { A _ { 1 } } & { I _ { 1 2 } } & { \cdot \cdot \cdot I _ { 1 L } } \\ { I _ { 2 1 } } & { A _ { 2 } } & { \cdot \cdot \cdot I _ { 2 L } } \\ { \vdots } & { \vdots } & { \ddots } & { \ldots } \\ { I _ { L 1 } } & { I _ { L 2 } } & { \cdot \cdot \cdot A _ { L } } \end{array} \right] \in \mathcal { R } ^ { N \times N } ,
$$

where $A _ { 1 } , A _ { 2 } , \ldots , A _ { L }$ are the adjacency matrix of layer $1 , 2 , \ldots , L$ , respectively. $N$ is the total number of nodes, which can be calculated by $\begin{array} { r } { N = \sum _ { 1 \leq l \leq L } | V ^ { l } | } \end{array}$ . The non-diagonal block $I _ { \alpha \beta }$ represents the inter-layer edges of layer $\alpha$ and layer $\beta$ . Thus,

![](images/e4f7088560777d5cf1ad5a0274d068ca03d2cf12b54732da1c96850a129159aa.jpg)  
Fig. 7 Supra-adjacency representation of 9/11 terrorists’ network. The supra-adjacency matrix is represented as a block matrix, where the rows and columns depict the terrorists. The diagonal blocks indicate the interactions, while the non-diagonal blocks represents the that terrorists are simultaneously active on different respects of observed social actions

the interlayer edges can be represented as

$$
I = \bigcup _ { \alpha , \beta = 1 , \alpha \neq \beta } ^ { L } I _ { \alpha \beta } .
$$

Take the above-mentioned 9/11 terrorists’ network for instance, the supra-adjacency matrix is represented in Fig. 7.

We also list some specific networks that can be represented by a multilayer network manner in the following.

Multiplex network is a special case of multilayer networks (Solá et al. 2013), where all layers share the same set of nodes but may have multiple types of interactions. Some works also use multi-relational networks, multidimensional networks (Berlingerio et al. 2011b) or edge-colored networks (no interlayer edges) for substitution. The underlying limitations exist in the network is node-aligned, i.e. each layer has the same nodes but merely differs in edges. Multiplex network is a special form of multilayer network, where the number of nodes in each layer is consistent, and the nodes are one-to-one correspondence. This network model simplifies the complexity of the general multilayer network form and is therefore widely used to deal with some special problems (Kanawati 2015).

Temporal networks (or time-varying networks) differ with conventional dynamic networks, which focus more on the ordinal variations of connections (Kostakos 2009).

![](images/c508b0712bd207b2a1c9d9a9e3c730612cde0c862b5dc55e4bef80b5557d9e67.jpg)  
Fig. 8 The monolayer network representation of the relationships of characters in “Game of Thrones” of the first five seasons, which contains 796 characters and 2823 links among them. The size of the node depicts the degree centrality, e.g., Tyrion Lannister, Jon Snow, and Daenerys Targaryen, as three key roles in the story, have larger degrees

![](images/5c52b41cad4a89b6a3e2cd1754a2efd26a1ab76009a4cce03ed092a17029cf17.jpg)  
Fig. 9 The multilayer network representation of the relationships of characters in “Game of Thrones” of the first five seasons. Each layer represents a season and the links between the ordinal layers represent the corresponding relationship of characters across different seasons

The temporal network has its own set of research models (Kempe et al. 2002; Kostakos 2009; Tang et al. 2012a), which can illustrate the dynamic characteristics of temporal networks. But it must be mentioned that the power of a multilayer network is that it can be compatible with the representation of the temporal network and can also describe the dynamic characteristics likewise. For example, the multilayer network model we have introduced (Boccaletti et al. 2014) can regard the network structure at each moment as a layer, and the arrangement between different layers is in chronological order. We collected the relationship of characters in the Game of Thrones (the first five seasons), as shown in Figs. 8 and 9.

The study of $k$ -partite networks starts from the complete $k$ -partite graph (i.e., a set of graph vertices decomposed into $k$ disjoint sets such that no two graph vertices within the same set are adjacent) (Brouwer and Haemers 2012). Thus, the $k$ -partite network is also described as node-colored networks (Kivelä et al. 2014), where the nodes are unacquainted in the same layer but have the other layers’ common neighbors with other nodes in the same layer. A sample of $k$ -partite networks is shown in Fig. 10.

![](images/a34e169ad53e17190755aa86b66f37b55e86ff32cbbbd118987a9e31417715f2.jpg)  
Fig. 10 Illustration of a $k$ -partite network, where $k = 3$ . There are no intralayer edges in any layer of the network, while the edges are all inter-connected across adjacent layers

![](images/26d75f2552b8da3458f877c0c1442dbff59f214484a9f10f19dea57f9dd61e13.jpg)  
Fig. 11 Illustration of South women activities network, which is a typical bipartite network. The qualification of the binary network is to check if there are links between nodes in the same type. All the links are connecting nodes with different types of nodes, corresponding with the non-diagonal elements as shown in the middle panel. The right panel presents the corresponding supra-adjacency matrix

However, a special case of $k$ -partite (i.e., $k = 2$ ) networks is the bipartite network (or two-mode network), which is more accessible by us. For example, a customer’s transaction records of products can be represented by a “customer-product” network. Fig. 11 presents a classic bipartite network, namely, South women activities network (Davis et al. 2009).

# 2.2 Features

Many basic metrics such as centrality, node similarity, are commonly used by community detection algorithms in monolayer networks. While in multilayer networks, the metrics need to be reformulated and adapted. Thus, in this section, some most important features of multilayer networks are introduced. Studies of structural properties include descriptors to identify the most central nodes according to various notions of importance (Battiston et al. 2014; De Domenico et al. 2015c, 2013; Halu et al. 2013; Solá et al. 2013) and quantify triadic relations such as clustering and transitivity (Battiston et al. 2014; Cozzo et al. 2015; De Domenico et al. 2013).

# 2.2.1 Centrality

The ranking of nodes in multilayer networks is one of the most pressing and challenging tasks that research on complex networks is currently facing (Lü et al. 2016). Many centrality measures have been used for single-layer networks to rank the importance of the nodes, such as degree centrality (Bonacich 1972), betweenness centrality (Freeman 1977), closeness centrality (Freeman 1978), $k$ -shell centrality (Carmi et al. 2007), eigenvector centrality (Bonacich 1987), PageRank (Brin and Page 1998), LeaderRank (Lü et al. 2011), Local Centrality (Chen et al. 2012), Bridge-Rank (Salavati et al. 2018), and so on. The above measures are widely used in the monolayer network model, while the study on nodes centrality in multilayer networks is still an open issue.

Before introducing the centrality in networks, we will first cover the neighborhood in a multiplex network. There are two definitions for the neighborhood in a multiplex network: One is given by a restrict aggregation concept that $j$ is a neighbor of $i$ if $j$ is connected to $i$ in each layer. The other is loosely defined as $j$ is connected to $i$ in at least one layer (Kazienko et al. 2010). Alhajj and Rokne (2014) give a tradeoff definition of the above two methods: $j$ is a neighbor of $i$ if it is connected to $i$ in at least $m$ layers, where $1 \ \leq \ m \ \leq \ L$ , and $L$ is the total number of layers. This definition may be capable of analyzing the node’s centrality in a multiplex network with numerous layers, but it is not ideal enough for introducing another threshold on the number of layers for consideration. However, when applying the concept in a general form of multilayer networks, there are also some problems to be solved. The first problem is the nodes’ relationships in a multilayer network, i.e., there may be no corresponding nodes of $i$ in other layers, e.g. in a $k$ -partite network where the nodes of each layer are totally different. The second problem is about the presentation format of the node’s neighborhood, the degree centrality can hardly distinguish a node with the same amount of interlayer edges and intralayer edges. The third problem is whether to give equal consideration of weights on interlayer edges and intralayer edges.

In monolayer networks, one of the main centrality measures is the degree of each node: the more links a node has, the more important the node is. The centrality of node $i$ , e.g. the degree of a node $i$ in a multiplex network is the vector (Battiston et al. 2014), defined as

$$
k _ { i } = ( k _ { i } ^ { 1 } , k _ { i } ^ { 2 } , \ldots k _ { i } ^ { L } ) ,
$$

where $k _ { i } ^ { L }$ is the degree of node $i$ in the $L ^ { t h }$ layer. We can also convert it into another form for simplification, given by

$$
k _ { i } = \sum _ { l = 1 } ^ { L } k _ { i } ^ { l } .
$$

Another solution for the centrality of multilayer nodes is through the diffusion across multiple layers. Examples of this measure include influential nodes identification, viral marketing, information diffusion, and so on (Lü et al. 2016). The network structure is more complicated with higher computational complexity. Some scholars believe that the interlayers edges should be under consideration discriminatively when calculating the node centrality, while others insist on the viewpoint that the interlayer edges make the same contribution to the centrality calculation. Likewise, the degree centrality measures used in multilayer networks can be substituted by other measures, e.g. Eigenvector centrality (Solá et al. 2013).

Above all, in a general form of multilayer network, the nodes may differ in each layer and we cannot obtain the corresponding nodes and calculate the centrality of the nodes directly. This problem has drawn much attention in recent years, including some popular endeavors such as user identification across multiple networks (Carmagnola and Cena 2009; Feng et al. 2017; Liang et al. 2015; Yang et al. 2018), social network coalescence, network alignment (Bayati et al. 2013), and so on.

# 2.2.2 Correlations

Multilayer networks encode significantly more information than their isolated single layers, since they incorporate correlations between the nodes in different layers and between the statistical properties of layers. The correlations of multilayer networks include interlayer degree correlations (Nicosia and Latora 2015), layers overlapping (Kao and Porter 2018), and so on. Some scholars point out that the communities in multilayer networks should consider for overlapping features, while allowing the communities to affect each layer in a different way, including arbitrary mixtures of assortative, disassortative, or directed structure (De Bacco et al. 2017). A definition of local overlap (Cellai et al. 2016) is defined as

$$
o _ { i } ^ { \alpha \beta } = \sum _ { j } \theta ( \omega _ { i j } ^ { \alpha } ) \theta ( \omega _ { i j } ^ { \beta } ) ,
$$

where $o _ { i } ^ { \alpha \beta }$ is the number of overlapping edges that are incident to node $i$ in both layer $\alpha$ and layer $\beta$ , $\omega _ { i j } ^ { \alpha }$ and $\omega _ { i j } ^ { \beta }$ are the weights of intralayer edges $( i , j )$ in layer $\alpha$ and layer $\beta$ , respectively. $\check { \theta ( x ) } = \boldsymbol { 1 }$ if $x > 0$ and $\theta ( x ) = 0$ otherwise. Based on this concept, Kao et al. propose a method that grouping structurally similar layers in multiplex networks and find meaningful groups of layers (Kao and Porter 2018). Considering the degree in undirected multiplex networks, the connection similarity is defined as

$$
\phi ^ { \alpha \beta } = \frac { 1 } { N } \sum _ { i } \phi _ { i } ^ { \alpha \beta } \in [ 0 , 1 ] ,
$$

where $\phi _ { i } ^ { \alpha \beta }$ is local similarity, defined as

$$
\phi _ { i } ^ { \alpha \beta } = \frac { o _ { i } ^ { \alpha \beta } } { k _ { i } ^ { \alpha } + k _ { i } ^ { \alpha } - o _ { i } ^ { \alpha \beta } } .
$$

The correlations of nodes are of great importance in analyzing multilayer network structures. Zhan et al. improved the community detection algorithms in multi-relational social networks by utilizing triangles and latent factor cosine similarity prior methods (Zhan et al. 2018). The local topological correlations between any pair of nodes from different layers are also utilized to calculate the centrality of nodes in multilayer networks (Kuncheva and Montana 2015).

# 3 Methods

Communities are known as groups of nodes that are more strongly or frequently connected among themselves than with the remainders (Aldecoa and Marín 2013). Although connecting patterns with other members are possible, they usually have higher linking probability within the group (Fortunato and Hric 2016). Community detection is a fundamental issue in network science, and most existing approaches have been developed for monolayer networks. However, many complex systems are composed of coupled networks through different layers, where each layer represents one of many possible types of interactions.

# 3.1 Problem statement

Communities in single-layer networks comprise a group of well-connected nodes, while in multilayer networks, communities reveal the relationships among nodes in various layers. The comparison of communities on toy examples in single-layer networks and multilayer networks is given in Fig. 12.

The problem of community detection algorithms in multilayer networks is to divide the network into a set of disjoint cohesive modules $C _ { 1 }$ , $C _ { 2 } , \ldots , C _ { k }$ where each module $C _ { k }$ is comprised of a group of nodes densely connected inside and loosely connected outside the community. It can be described as

$$
\cup _ { i = 1 } ^ { k } C _ { i } = \sum _ { \alpha = 1 } ^ { L } V _ { \alpha } ,
$$

with $\cap _ { i = 1 } ^ { k } C _ { i } \ = \phi$ for non-overlapping community detection and $\cap _ { i = 1 } ^ { k } C _ { i } \ \neq \phi$ for = =overlapping scenarios. Dalibard (Dalibard 2012) gives the three requirements about community detection works as followings:

(1) The community detection should allow for overlapping communities. (2) The detected results should be statistically significant, which means applying the algorithm on a random null model should return no communities. (3) The detected results should be hierarchical.

Specifically, most of the existing approaches can scarcely satisfy the requirements and hold reasonable efficiency. Besides, the evaluation metrics are also varied from one to another, as introduced in the following subsection.

![](images/ab726d0f02c9960bdc61da3560e7dbd5bc5e6ad930995caed348082afce73ec4.jpg)  
Fig. 12 Comparison of communities in monolayer and multilayer networks. The nodes with different gray levels represent different communities. (a) Communities in a monolayer network. (b) Communities in a two-layered network, each community shares nodes in Layer 1 and Layer 2

# 3.2 Evaluation functions

Quality evaluation for partition results is a complex task due to the lack of a shared and universally accepted definition of community structures. A wide variety of quality functions have been proposed to solve the community detection problem from different perspectives. Several representative metrics are analyzed and classified into three categories (Cazabet et al. 2015):

(1) Single score metrics (2) Evaluation on generated networks (3) Evaluation on real networks with ground truth

Single score metrics employ quality functions associating a score to the community detection result. For example, the number of edges between partitions can be utilized to evaluate the performance of a given algorithm. Popular metrics include Modularity (Newman and Girvan 2004), Modularity density (Li et al. 2008), surprise (Aldecoa and Marín 2011), and so on. These metrics are universal but often criticized with no consensus of the several meaningful levels of partitions. The comparison with generated networks, e.g., LFR benchmark (Lancichinetti et al. 2008) is widely used to compare the partitions with the community affiliations. It is easy to recognize a good community and capable of evaluating variations in usual communities. However, sometimes the generated networks are not realistic and differ from the partitions we want. The comparison of real networks with ground truth seems to be a reasonable solution. Normalized Mutual Information (Danon et al. 2005), Precision, Recall, and $F _ { 1 }$ -score (Herlocker et al. 2004; Perry et al. 1955) are representative methods. However, these methods depend on the priori partition labels, which are probably unknown in most of real-world datasets.

# 3.2.1 Modularity, modularity density, performance and surprise

In 2004, modularity (Newman and Girvan 2004) was first proposed by Newman as an evaluation for community partitions, defined as

$$
Q = \frac { 1 } { 2 m } \sum _ { i j } \left( A _ { i j } - \frac { k _ { i } k _ { j } } { 2 m } \right) \delta ( C _ { i } , C _ { j } ) ,
$$

where $m$ is the number of edges, $A _ { i j }$ is the element of the adjacency matrix, $\delta ( C _ { 1 } , C _ { 2 } )$ equals 1 if $i$ and $j$ are in the same community, otherwise 0. In 2010, Mucha et al. proposed $Q _ { M }$ (Mucha et al. 2010) for evaluating community in time-dependent, multiscale and multiplex networks, defined as

$$
{ \cal Q } _ { M } = \frac { 1 } { 2 \mu } \left\{ \left( A _ { i j \alpha } - \gamma \frac { k _ { i \alpha } k _ { j \alpha } } { 2 m _ { \alpha } } \right) \delta _ { \alpha \beta } + \delta _ { i j } C _ { j \alpha \beta } \right\} \delta ( g _ { i \alpha } , g _ { j \beta } ) ,
$$

where $\mu$ denotes the number of links in multiplex networks, $\gamma$ is the resolution parameter. $A _ { i j \alpha }$ represents the adjacency matrix of nodes in layer $\alpha$ . $C _ { j \alpha \beta }$ represents interlayer edge connecting node $j$ among layer $\alpha$ and layer $\beta$ . This metric introduces a coupling between communities in neighboring layers by allowing interlayer edges, while different $\gamma$ enables the detection of different scale communities. However, the range of $\gamma$ is required to be manually determined, which may be unable to obtain reasonable results without an appropriate $\gamma$ . Afterward, a variational version of $Q _ { M }$ is given (Pramanik et al. 2017) as

$$
Q = \frac { 1 } { 2 m } \sum _ { i j } ( A _ { i j } - P _ { i j } ) \delta ( \psi _ { i } , \psi _ { j } ) ,
$$

where $\delta ( \psi _ { i } , \psi _ { j } )$ is the Kronecker delta function, it equals 1 iff $\psi _ { i } = \psi _ { j }$ , i.e. $i$ and $j$ belong to the same community and 0 otherwise. The penalty term $P _ { i j }$ is the expected probability of existing an edge between nodes $i$ and $j$ if edges are placed at random as

$$
\begin{array} { r } { P _ { i j } = \left\{ \begin{array} { l l } { P _ { i j } ^ { 1 } , } & { \mathrm { i f } i \in V ^ { 1 } \& j \in V ^ { 1 } } \\ { P _ { i j } ^ { 2 } , } & { \mathrm { i f } i \in V ^ { 1 } \& j \in V ^ { 2 } } \\ { P _ { i j } ^ { 1 2 } , } & { \mathrm { i f } i \in V ^ { 1 } \& j \in V ^ { 2 } \mathrm { o r } i \in V ^ { 2 } \& j \in V ^ { 1 } } \end{array} \right. , } \end{array}
$$

where $P _ { i j } ^ { 1 }$ can be calculated by $P _ { i j } ^ { 1 } = ( h _ { i } \times h _ { j } ) / ( 2 | E ^ { 1 } | )$ and $P _ { i j } ^ { 2 } = ( h _ { i } \times h _ { j } ) / ( 2 | E ^ { 2 } | )$ and $P _ { i j } ^ { 1 2 } = ( c _ { i } \times c _ { j } ) / ( 2 | I _ { 1 2 } | ) . { } I$ $h _ { i }$ and $h _ { j }$ are the intralayer degrees of nodes $i$ and $j$ , and $c _ { i }$ and $c _ { j }$ are the respective coupling degrees of $i$ and $j . | I _ { 1 2 } |$ depicts the amount of all the interlayer edges among layers $L _ { 1 }$ and $L _ { 2 }$ . Likewise, the multiplex modularity is also criticized by resolution limits (Vaiana and Muldoon 2018).

Modularity density (Li et al. 2008) was proposed to solve the resolution limits problem, defined as

$$
D = \sum _ { i = 1 } ^ { c } \frac { L \left( V _ { i } , V _ { i } \right) - L \left( V _ { i } , \bar { V } _ { i } \right) } { \left| V _ { i } \right| } ,
$$

where $c$ is the total number of communities, $\vert V _ { i } \vert$ is the number of nodes of the $i$ - th community. $L \left( V _ { i } , V _ { i } \right) = \Sigma _ { j \in V _ { i } , k \in V _ { i } } A _ { j k }$ denotes the number of edges among $i$ - th community and $L \left( V _ { i } , { \bar { V } } _ { i } \right) = { \cal { \Sigma } } _ { j \in V _ { i } , k \in { \bar { V } } _ { i } } A _ { j k }$ denotes the number of connections between the $i$ -th community and other communities.

In 2010, Performance (Fortunato 2010) was proposed as a community quality function, which mainly considered the number of correctly “interpreted” pairs of nodes (i.e., the nodes belonging to the same community and connected by an edge, and nodes belonging to different communities and not connected by an edge), defined as

$$
\mathcal { P } = \frac { \left| \left\{ ( i , j ) \in E , C _ { i } = C _ { j } \right\} \right| + \left| \left\{ ( i , j ) \notin E , C _ { i } \neq C _ { j } \right\} \right| } { n ( n - 1 ) / 2 } ,
$$

where $E$ denotes the edges set, $C _ { i }$ and $C _ { j }$ denote the $i$ -th and $j$ -th communities, respectively, $n$ is the total number of nodes. Specifically, Coverage (Fortunato 2010) was defined as the ratio of the number of intra-community edges by the total number of edges, given as

$$
\mathcal { C } = \frac { \left| \left\{ ( i , j ) \in E , C _ { i } = C _ { j } \right\} \right| } { n ( n - 1 ) / 2 } .
$$

In 2011, Aldecoa and Marín (2011) proposed the “Surprise” as a measure for detecting communities. Different from merely considering the number of edges required in a partition, this metric takes the number of nodes into account, and it is capable of resolving the resolution limit problem and detecting small communities (Fortunato and Barthelemy 2007; Lancichinetti and Fortunato 2011). It is an interesting function to measure how impossible is a given partition compared to a null model, defined as

$$
{ \cal S } = - \log \sum _ { j = p } ^ { \operatorname* { m i n } ( M , n ) } \frac { { \binom { M } { j } } { \binom { F - M } { n - j } } } { { \binom { F } { n } } } ,
$$

where $F$ is the maximum possible number of links in the network (i.e. $k [ k - 1 ] / 2$ , being $k$ the number of nodes), $n$ is the observed number of links, $M$ is the maximum possible number of intracommunity links observed in a partition. The parameter $S$ , which stands for Surprise, indeed measures the “surprise” (improbability) of finding by chance a partition with the observed enrichment of intracommunity links to a random graph. The authors declare that surprise implicitly assumes a more complex definition of community: a precise number of units for which it is found a density of link which is statistically unexpected given the features of the network, and in 2013, they also designed surprise maximization methods for detecting community structure in complex networks (Aldecoa and Marín 2013). As an effective metric for evaluating community structures, experiments on the human brain network (Fox and Lancaster 2002; Laird et al. 2005) have also proved its priority to modularity (Nicolini and Bifone 2016).

# 3.2.2 MDL, Pareto frontier and redundancy

The fundamental idea behind the MDL principle is that any regularity in a given set of data can be used to compress the data, i.e. to describe it using fewer symbols than needed to describe the data literally (Grunwald 2004). Rosvall et al. convert the community detection task into solving a coding problem following the MDL principle (Rosvall and Bergstrom 2008). Analogously, the objective function of community detection can be considered as a multi-objective optimization problem. The optimal partitioning for a multilayer network is achieved by maximizing a local evaluation indicator (e.g. local modularity (Chen et al. 2018b)) in each layer, i.e.,

$$
C = \arg \operatorname* { m a x } _ { C } [ f _ { 1 } ( C ) , f _ { 2 } ( C ) , \ldots , f _ { k } ( C ) ] ,
$$

where $k$ denotes the number of communities. However, calculating an exact Pareto front is, in general, a challenging task. The most popular approximate methods are genetic algorithms, which employ biologically inspired heuristics to attempt to transform randomly selected seed cases into solutions on the Pareto front using propagation Multi-objective Management (Caramia and Dell’Olmo 2008).

Berlingerio et al. define the redundancy index $\rho _ { c }$ (Berlingerio et al. 2011a), which captures the phenomenon that a set of nodes constitute a community in a dimension tend to constitute communities also in other dimensions. The redundancy figures out the fraction of redundant links in a multi-dimensional network, defined as

$$
\rho _ { c } = \sum _ { ( u , v ) \in \bar { P } _ { c } } \frac { | \{ \alpha : \exists ( u , v ) ^ { \alpha } \in E \} | } { L \times | P _ { c } | } ,
$$

where $c$ represents a community, $\alpha$ is a layer of all the layers $\mathcal { L } = \{ 1 , 2 , \dots , L \}$ , $P$ is a set of node pairs $( u , v )$ existed at least one layer in a multilayer network; $\bar { P }$ is the set of node pairs existed at least two layers. $\hat { P } _ { c }$ is the subset of $P$ appearing in $c$ ; $\bar { P } _ { c } \subseteq \bar { P }$ is the subset of $\bar { P }$ only containing node pairs in $c$ . The more layers connect each pair of nodes within a community, the higher the redundancy will be.

# 3.2.3 Purity, NMI, and ARI

The clustering accuracy measures are widely utilized to evaluate and compare the performance of community detection algorithms on real-world networks with given ground-truth communities. Suppose the computed clusters $\mathcal { Q } ~ = ~ \{ \omega _ { 1 } , \omega _ { 2 } , \ldots , \omega _ { k } \}$ with respect to the ground truth classes $C = c _ { 1 } , c _ { 2 } , \ldots , c _ { k } .$ . Purity (Zhao and Karypis 2004) represents the percentage of the total number of nodes classified correctly, defined as

$$
P u r i t y ( \Omega , C ) = \frac { 1 } { N } \sum _ { k } \operatorname* { m a x } _ { j } \left| \omega _ { k } \cap c _ { j } \right| ,
$$

where $N$ is the total number of nodes, and $| \omega _ { k } \cap \boldsymbol { c } _ { j } |$ depicts the number of nodes in the intersection of $\omega _ { k }$ and $c _ { j }$ . To compromise the quality of the clustering against the number of clusters, we can utilize normalized mutual information (i.e., NMI) (Danon et al. 2005). The confusion matrix is comprised of ground communities and generated partitions, thereby NMI is defined as

$$
N M I ( A , B ) = \frac { - 2 \sum _ { i = 1 } ^ { C _ { A } } \sum _ { j = 1 } ^ { C _ { B } } N _ { i j } \log \frac { N _ { i j } N } { N _ { i } N _ { j } } } { \sum _ { i = 1 } ^ { C _ { A } } N _ { i } \log \frac { C _ { i } } { N } + \sum _ { j = 1 } ^ { C _ { B } } N _ { j } \log \frac { C _ { j } } { N } } ,
$$

where $A$ and $B$ denote the ground-truth communities and the detected partitions. $C _ { A }$ and $C _ { B }$ are the number of groups in partition $A$ and $B$ , respectively. $N _ { i j }$ depicts the elements of the confusion matrix. $N _ { i }$ is the sum of the elements in row $i$ , $N _ { j }$ is the sum of elements in column $j . N$ is the number of nodes. The range of NMI is 0, 1 . If $A = B$ , $N M I ( A , B ) = 1$ . If $A$ and $B$ are completely different, $N M I ( A , B ) = 0$ . Suppose an approximate size $z$ as the number of community sets, the computation of NMI requires $O ( z ^ { 2 } )$ comparisons, which is incapable of evaluating partitions for large-scale networks. In order to cope with the high computational complexity of such method in recent years, several approaches (Cazabet et al. 2015; Rossetti et al. 2016a, b), e.g., the precision, recall, and $F _ { \mathrm { 1 - s c o r e } }$ are employed, defined as

$$
\begin{array} { c } { { P r e c i s i o n = \displaystyle \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F P } } , } } \\ { { R e c a l l = \displaystyle \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F N } } , } } \\ { { F _ { \mathrm { 1 - s c o r e } } = \displaystyle \frac { 2 \times ( \mathrm { P r e c i s i o n } \times \mathrm { \ R e c a l l } ) } { \mathrm { P r e c i s i o n } + \mathrm { R e c a l l } } , } } \end{array}
$$

with $\mathrm { T P } =$ true positive, $\mathrm { F P = }$ false positive, $\mathrm { F N = }$ false negative and $\mathrm { T N } =$ true negative. Besides, Rand Index is also a popular measure, which represents the percentage of TP and TN decisions assigns that are correct (i.e. accuracy), defined as

$$
R I ( \Omega , C ) = \frac { \mathrm { T P } + \mathrm { T N } } { \mathrm { T P } + \mathrm { F P } + \mathrm { F N } + \mathrm { T N } } .
$$

ARI (Schütze et al. 2008) is RI defined to be scaled in the range 0, 1 . All of the metrics in this subsection are in the range of [0, 1], and the higher the metric, the better the clustering quality is.

# 3.3 Algorithms classification

Early approaches either collapse multilayer networks into a weighted single-layer network (Berlingerio et al. 2011a; Tang et al. 2012b; Taylor et al. 2016b, a), or extend the existing algorithms for each layer and then merge the partitions via consensus clustering (Tang et al. 2009; Papalexakis et al. 2013). However, these approaches have been criticized for ignoring the connections across layers, thereby resulting in low accuracy. Research to date has exhibited some novel algorithms for discovering communities in multilayer networks directly (Ma et al. 2018; Pamfil et al. 2019). Generally speaking, the strategies are mainly classified into three categories (Tagarelli et al. 2017):

– Flattening methods – Aggregation methods – Direct methods

Flattening methods collapse the layers’ information into a single layer and then conduct the traditional monolayer algorithms for detecting communities. This strategy is very common in multiplex networks, where the multiplex network is converted into a multi-relationship network (Rocklin and Pinar 2013) or a monolayer network (Kuncheva and Montana 2015).

Aggregation methods discover the communities in each layer and then merge them by a certain aggregation mechanism, which could be useful for removing redundant information. The aggregation process requires $2 ^ { L }$ comparisons and it’s very timeconsuming for a temporal network with numerous layers. Thus, “layer communities grouping” is proposed to reduce the redundant layers (Kao and Porter 2018). Dalibard proposed a parameter $P _ { C _ { k } } ^ { l }$ for each layer $l \in L$ to describe the probability of communities, and then aggregate the communities in each layer in terms of a correlation coefficient $\rho _ { \alpha \beta }$ between layers $\alpha$ and $\beta$ (Dalibard 2012). Numerical experiments on synthetic multilayer networks show that the analysis fails in aggregated networks, whereas the multilayer method can accurately identify modules across layers that originate from the same interaction process (De Domenico et al. 2015a). Thus, aggregation is not recommended.

Direct methods aim to detect the community structures directly on the multilayer network by optimizing some quality-assessment criteria without flattening (Oselio et al. 2015). For example, Pramanik et al. defined a multilayer modularity index, i.e., $Q _ { M }$ , and combined with the improved GN and Louvain algorithms, namely GN- $Q _ { M }$ and Louvain- $Q _ { M }$ , respectively (Pramanik et al. 2017).

There has been plenty of endeavors made in the last decades, however, research for multilayer networks is still in infancy (Tagarelli et al. 2017), and it is promising to extract communities without collapsing multilayer networks. Several representative methods are introduced in the following subsections.

Table 3 Similarity measures for MNLPA algorithm   

<html><body><table><tr><td>Metric in monolayer networks</td><td>Modification for multilayer networks</td></tr><tr><td></td><td>+区 1 [ 2</td></tr><tr><td>JC(i,j) = 1F80FOl</td><td>£=1α</td></tr><tr><td>CN(i,j)= |r(i) nr(j)l</td><td>£-1 1 (N|+IND))</td></tr><tr><td>AA(i,j)=∑z∈|r(i)nr(j)l Iogkz</td><td>k 1 1 a=1 ogr £1@ £zEN 2@</td></tr></table></body></html>

$T ( i )$ and $T ( i )$ denote the neighbors of node $i$ and node $j$ , respectively. $\omega _ { \alpha }$ denotes the weight of layer $\alpha$ , $N =  { { \cal { r } } } _ { \mathrm { o u t \_ j } } ^ { \alpha } \cap  { { \cal { r } } } _ { \mathrm { i n \_ i } } ^ { \alpha } , \dot { N } =  { { \cal { r } } } _ { \mathrm { i n \_ j } } ^ { \bar { \alpha } } \cap  { { \cal { r } } } _ { \mathrm { o u t \_ i } } ^ { \alpha } , U =  { { \cal { r } } } _ { \mathrm { o u t \_ j } } ^ { \alpha } \cup  { { \cal { r } } } _ { \mathrm { i n \_ i } } ^ { \alpha }$ and $\dot { U } = \Gamma _ { \mathrm { o u t } \_ j } ^ { \alpha } \cup \Gamma _ { \mathrm { i n } \_ i } ^ { \alpha } . \Gamma _ { \mathrm { o u t } \_ j } ^ { \alpha }$ and Γ α denote out-neighbors and in-neighbors of node $j$ and node $i$ in layer $\alpha$ , respectively. $\bar { Z }$ is the intersection of $j$ ’s out-neighbors and $i$ ’s in-neighbors. $\acute { Z }$ is the intersection of $j$ ’s in-neighbors and $i$ ’s out-neighbors

# 3.3.1 Improved label propagation algorithm

Label propagation algorithms utilize the propagation features of networks and have linear complexity and reasonable results. These methods allow the nodes to adopt new characteristics depending on the behavior of their neighbors, e.g. adopts labels of the biggest amount of its neighbors. The process of LPA is shown as follows:

Step 1: Traverse the network and assign a unique label to each node.   
Step 2: Establish a random order of the node’s revision.   
Step 3: Each node is revised in the assigned order and adopts the most frequent label of its neighbors.   
Step 4: The process is performed iteratively until the algorithm converges and no label changes occur anymore.

Inspired by the traditional LPA process, Alimadadi et al. (2019) redefined the neighborhood in multilayer networks and then proposed MNLPA to detect communities in a weighted and directed Facebook activity network. The algorithms are summarized as followings:

Step 1: Each node $u$ is initiated with a unique label, then the neighbors of $u$ in all layers are obtained, marked as $N _ { u }$ .   
Step 2: Calculate the similarity (measures are listed in Table 3) of $u$ between the node $v$ in $N _ { u }$ , and mark $v$ when the similarity score is more than a given threshold $\sigma$ .   
Step 3: Repeat the following steps until the stop criterion is satisfied: – Nodes are ordered randomly; – For each node $u$ , each marked similar neighbor sends out its label to $u$ , and mark the node $u$ with maximum labels.

Step 4: Divide communities by the nodes with the same labels.

The MNLPA is praiseworthy with efficiency, and capable of dealing with weighted and directed networks, but also criticized by instability. The partition result is sensitive to the threshold parameter in MNLPA and the density of the network dataset. As they declared, the MNLPA algorithm is verified by experiments on real-world datasets and the results are reprinted in Fig. 13.

![](images/9fb01acc4a8f478c0e739c35123e16d01d6cecfe0f14851abfca1dcdf6bddf6e.jpg)  
Fig. 13 Comparison of LPA and MNLPA algorithms conducting on Facebook datasets. The homophily obtained by MNLPA algorithm is marked by gray bars, thus the resultant communities are similar and fit the definition of the community to some extent

![](images/1b08eee40a5a7e61b3d49772704daf921b5985824715567445f45b89095774e5.jpg)  
Fig. 14 Three synthetic multilayer networks for evaluating the proposed MNLPA. The top three panels show the multilayer networks, in which each has three layers with community labels generated by LFR benchmark (Lancichinetti et al. 2008). The bottom three panels show the relevant supra-adjacency matrices

As the Facebook datasets are not provided in their works, we construct several synthetic three-layered networks, as plotted in Fig. 14.

Experiments on the constructed synthetic networks suggest that MNLPA algorithm is fastidious about the parameters. The changing of modularity with the varying threshold $\delta$ is plotted, as shown in Fig. 15.

As shown in Fig. 15, the performance of the proposed MNLPA is not satisfied. With an increasing threshold in [0.2, 0.4], the modularity increased, thus we guess the threshold should be greater than 0.4 approximately. The Facebook datasets utilized in the experiments are weighted and directed, which may make prominent differences in the experimental results. In brief, the MNLPA is suitable for large-scale networks under certain conditions (e.g., weighted and directed), while for general multilayer networks, it’s necessary to make modifications to improve the performance.

![](images/3eb586cbb1d178b9ac8e53373f4cd1c20c536f0c0da3ba173842297dfdb77485.jpg)  
Fig. 15 The modularities tendency obtained by the MNLPA algorithm conducting on three different synthetic networks changes with the varying threshold δ

# 3.3.2 Nonnegative matrix factorization methods

Nonnegative matrix factorization (NMF) was proposed by Lee and Seung (2001). It aims to factorize the original nonnegative matrix into the product of two other nonnegative matrices. For applications in community detection methods, the original nonnegative matrix can be an adjacency matrix, thereby the objective (loss) function can be presented as

$$
\operatorname* { m i n } _ { U \geq 0 , V \geq 0 } L ( A , U V ^ { T } ) = \left\| A - U V ^ { T } \right\| _ { F } ^ { 2 } ,
$$

where $A$ is a $n \times n$ adjacency matrix, and both $U$ and $V$ are $n \times k$ matrices. The rank $k$ corresponds to the number of divided communities. It has been widely utilized in detecting communities in complex networks (Jiao et al. 2017; Liu et al. 2017; Wu et al. 2018).

Recently, Ma et al. applied this method (S2j-NMF) to community detection for multilayer networks (Ma et al. 2018). They propose a quantitative function (i.e. multilayer network modularity density) and prove the trace optimization of multilayer modularity density is equative to the objective functions of the community detection algorithms (e.g. $k$ -means (MacQueen 1967), NMF, spectral clustering $\mathrm { N g }$ et al. 2002), multiview clustering for multilayer networks, etc.). The modularity density $Q _ { D }$ for $\{ V _ { c } \} _ { c = 1 } ^ { k }$ is defined as

$$
\mathcal { Q } _ { D } \left( \left\{ V _ { c } \right\} _ { c = 1 } ^ { k } \right) = \sum _ { c = 1 } ^ { k } \frac { L \left( V _ { c } , V _ { c } \right) - L \left( V _ { c } , \bar { V } _ { c } \right) } { \left| V _ { c } \right| } ,
$$

where $Q _ { D } ( \{ V _ { c } \} _ { c = 1 } ^ { k } )$ is the modularity density of community partitions, $k$ is the number of partitions, $\hat { V _ { c } }$ depicts the partitions after removing $V _ { c } . ~ L ( V _ { i } , V _ { j } )$ calculates the connections between $V _ { i }$ and $V _ { j }$ , defined as

$$
L ( V _ { i } , V _ { j } ) = \sum _ { p \in V _ { i } , q \in V _ { j } } w _ { p q } ,
$$

where $p$ and $q$ are the nodes of the partition $V _ { i }$ and $V _ { j }$ , respectively. $w _ { p q }$ is the weight of the edge $( p , q )$ and equals 1 in unweighted networks. The objective function is transformed into a multi-objective optimization problem as

$$
Q _ { D } ^ { \mathcal { G } } \left( \{ V _ { c } \} _ { c = 1 } ^ { k } \right) = \frac { 1 } { m } \sum _ { l = 1 } ^ { m } \sum _ { c = 1 } ^ { k } \frac { L ^ { l } \left( V _ { c } , V _ { c } \right) - L ^ { l } \left( V _ { c } , \bar { V } _ { c } \right) } { \left| V _ { c } \right| } ,
$$

where $L ^ { l } ( V _ { i } , V _ { j } )$ is the same with equation (31) applied in $l$ layer. $\mathcal { Q } _ { D } ^ { \mathcal { G } } ( \{ V _ { c } \} _ { c = 1 } ^ { k } )$ is the objective function of the partitions in multilayer network $\mathcal { G }$ . Thus, the optimal partitioning $\{ V _ { c } \} _ { c = 1 } ^ { k }$ for the multilayer network by maximizing the modularity density in each layer can be represented as

$$
\left\{ \begin{array} { l l } { \operatorname* { m a x } \left( Q _ { D } ^ { 1 } ( \{ V _ { c } \} _ { c = 1 } ^ { k } ) \right) } \\ { \operatorname* { m a x } \left( Q _ { D } ^ { 2 } ( \{ V _ { c } \} _ { c = 1 } ^ { k } ) \right) } \\ { \cdot \cdot \cdot } \\ { \operatorname* { m a x } \left( Q _ { D } ^ { m } ( \{ V _ { c } \} _ { c = 1 } ^ { k } ) \right) } \end{array} \right. .
$$

Afterward, dense subgraphs are discovered by employing a greedy search strategy in multilayer networks. The conventional NMF algorithm combined with a factorized basis matrix and various coefficient matrices are applied to each layer. Finally, the experiments are conducted on several datasets, which verifies the proposed method.

The complexity of this method is $O ( m n ^ { 2 } k )$ , where $m$ is the number of layers and $k$ is the number of partitions. Thus, it is probably not acceptable for large-scale networks. Besides, as the authors mentioned, the algorithm is based on multiplex networks, which is not capable of handling the general form of multilayer networks. The algorithm relies on prior information and the number of target communities, and the decomposition process might be time-consuming.

# 3.3.3 Random walk methods

Kuncheva et al. propose a community detection algorithm, namely LART (Locally Adaptive Random Transitions) for the detection of communities that are shared by either some or all the layers in multiplex networks (Kuncheva and Montana 2015). They employ the supra-adjacency matrix $\check { M }$ and define the transition probabilities of four possible moves among the nodes, described as

$$
\begin{array} { r } { \left\{ { \begin{array} { l } { P _ { ( i , j ) ( i , k ) } = \displaystyle \frac { \check { M } ( i , k ) ( i , k ) } { k _ { i , k } } } \\ { P _ { ( i , j ) ( j , k ) } = \displaystyle \frac { \check { M } ( i , k ) ( j , k ) } { k _ { i , k } } \ : , } \\ { P _ { ( i , k ) ( i , l ) } = \displaystyle \frac { \check { M } ( i , k ) ( i , l ) } { k _ { i , k } } } \\ { P _ { ( i , j ) ( j , l ) } = 0 } \end{array} } \right. } \end{array}
$$

where $k _ { i , k }$ is the multiplex degree of node $v _ { i } ^ { k }$ in $\check { M }$ defined as $\begin{array} { r } { k _ { i , k } = \sum _ { j , l } \check { M } _ { ( i , k ) ( j , l ) } } \end{array}$ , $P _ { ( i , j ) ( j , k ) }$ depicts the transition probability from node $i$ of layer $k$ (i.e., $v _ { i } ^ { k }$ ) to node $j$ of the layer $l$ (i.e., $v _ { j } ^ { l } )$ . The probability to move from node $v _ { i } ^ { k }$ to node $v _ { j } ^ { l }$ is zero when $i \neq j$ and $k \neq l$ since there cannot exist a direct move where there is no connection. The transition probabilities are represented as a matrix $\mathcal { P }$ of the random walk process and written as

$$
\boldsymbol { \mathcal { P } } = \boldsymbol { \mathcal { D } } ^ { - 1 } \check { \boldsymbol { M } } ,
$$

where $\mathcal { D }$ is the diagonal matrix defined by the multiple node degrees. A dissimilarity matrix $S ( t )$ which depends on the multiplex random walk of steps $t$ is defined. The dissimilarity matrix is defined according to the nodes $i$ and $j$ are in the same layer or different layers, denoted by

$$
\begin{array} { l l } { S ( t ) _ { ( i , k ) ( j , k ) } = \sqrt { \displaystyle \sum _ { h = 1 } ^ { N } \sum _ { m = 1 } ^ { L } \frac { \left( \mathcal { P } _ { ( i , k ) ( h , m ) } ^ { t } - \mathcal { P } _ { ( j , k ) ( h , m ) } ^ { t } \right) ^ { 2 } } { k ( h , m ) } } , } \\ { S ( t ) _ { ( i , k ) ( j , l ) } = \sqrt { s _ { 1 } + s _ { 2 } + s _ { 3 } } , } \end{array}
$$

where $s _ { 1 } , s _ { 2 } , s _ { 3 }$ are defined as

$$
\left\{ \begin{array} { l l } { s _ { 1 } = \sum _ { h = 1 } ^ { N } \left( \frac { \mathcal { P } _ { ( i , k ) ( h , k ) } ^ { t } } { \sqrt { k ( h , k ) } } - \frac { \mathcal { P } _ { ( j , l ) ( h , l ) } ^ { t } } { \sqrt { k ( h , l ) } } \right) ^ { 2 } } \\ { s _ { 2 } = \sum _ { h = 1 } ^ { N } \left( \frac { \mathcal { P } _ { ( i , k ) ( h , l ) } ^ { t } } { \sqrt { k ( h , l ) } } - \frac { \mathcal { P } _ { ( j , l ) ( h , k ) } ^ { t } } { \sqrt { k ( h , k ) } } \right) ^ { 2 } } \\ { s _ { 3 } = \sum _ { h = 1 } ^ { N } \sum _ { m = 1 ; m \neq k , l } ^ { L } \frac { \left( \mathcal { P } _ { ( i , k ) ( h , m ) } ^ { t } - \mathcal { P } _ { ( j , k ) ( h , m ) } ^ { t } \right) ^ { 2 } } { k ( h , m ) } } \end{array} \right. .
$$

Afterward, the agglomerative clustering is utilized to merge nodes in communities. The multiplex modularity $Q _ { M }$ is employed to evaluate the quality of partitions. The process of LART is shown as follows:

Step 1: Assign each node in each layer to its own community.   
Step 2: Merge nodes based on the average linkage criterion using the distance matrix S and obey the principle of the merged community has at least one withinlayer or interlayer connection. Step 3: Merge the nodes only if the maximum $Q _ { M }$ is reached.   
Step 4: Obtain the shared and non-shared communities.

![](images/10263d94d6710d0d6b579000cbb840f1f12d2e866292a03c40f91925605ae3fe.jpg)  
Fig. 16 The comparison of the proposed LART algorithm with MM and PMM algorithms (Kuncheva and Montana 2015) on the five simulated scenarios of the synthetic network

The experiments are conducted on synthetic multiplex networks, and the experimental results are shown in Fig. 16.

The proposed LART algorithm is conducting on five different scenarios and the experimental result demonstrates the performance of the proposed algorithm. However, the algorithm is limited to multiplex networks, and the real-world networks are much more complicated. Hence, the performance of the LART algorithm for realworld datasets is uncertain.

# 3.3.4 Multi-objective optimization methods

Pizzuti and Socievole (2017) proposed the Multi-layer many-objective Optimization algorithm (MLMaOP), in which they formulated the community detection problem in multilayer networks as a many-objective optimization problem and a given objective is contemporarily optimized on all the network layers. In their work, they give the multi-objective optimization problem (MOP) as

$$
\operatorname* { m i n } _ { x } F ( x ) = ( f _ { 1 } ( x ) , f _ { 2 } ( x ) , \ldots , f _ { d } ( x ) ) { \mathrm { ~ s u b j e c t ~ t o ~ } } x \in X ,
$$

where $d$ is the number of objective functions, $x = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) \in X$ is the decision vector with a domain of definition $X \subseteq R ^ { n }$ , $F : X  Z$ is the mapping from the decision space $X$ to the objective space $Z$ . When $d \ge 3$ , an MOP is referred to as Many Objective Optimization Problem (MaOP) (Farina and Amato 2002). Paretodominance relation is used to define a partial ordering in the objective space. Thus, the problem of community detection in multilayer networks using MaOP is defined as

$$
\operatorname* { m i n } F ( P ) = ( F _ { 1 } ( P ) , F _ { 2 } ( P ) , \ldots , F _ { d } ( P ) ) \mathrm { s u b j e c t t o } P \in \Omega ,
$$

where each $F _ { \alpha } : \varOmega \to R$ computes the value of the objective function only on the layer $G _ { \alpha }$ . For the main purpose is to get a maximized $Q$ , so $F _ { \alpha } ( P ) = - Q _ { \alpha } ( P )$ means that the greater $Q$ , the smaller $F _ { \alpha } ( P )$ partitions on each layer. The main process of MLMaOP is shown as follows:

Step 1: Initialize a rand partition by using the adjacency matrix of projected $M$ .

![](images/fcce2a33bb446ec8fffcdf1252a2004270a6bc4b552f81384613d970289af37a.jpg)  
Fig. 17 The comparison of MLMaOP algorithm with competitors on SSRM dataset (Loe and Jensen 2015)

Step 2: Traverse the partition in all the layers, evaluate the objection function on $G _ { \alpha }$ to obtain $F _ { \alpha } ( P )$ . Assign a rank based on Pareto dominance and then combine parents and offspring partition into fronts.

Step 3: Select the best points, and apply the variation operators and create the next partition.   
Step 4: Choose a solution from the Pareto front.

The comparison of MLMaOP algorithm with other approaches (Loe and Jensen 2015) is shown in Fig. 17.

The proposed algorithm with three different strategies is competitive on the partitions $P _ { 1 }$ , while on $P _ { 2 }$ and $P _ { 3 }$ , we can see that the NMI results obtained by the other algorithms are better. Besides, the MLMaOP algorithm suffers from a low convergence rate to Pareto front and is likely to be time-consuming for detecting communities in large-scale networks.

# 3.4 Discussion

In the last decade, a plethora of approaches have been proposed to address the community detection problem with enormous network data. We list several representative methods (from 2009 to 2019), as shown in Table 4.

Table 4 shows that most of the presented methods are holding relatively high complexity, where GN- $Q _ { M }$ , Louvain- $Q _ { M }$ and LART methods are based on multiplex modularity maximization and unfavorable on general multilayer networks. Moreover, the majority are designed for multiplex networks, which require the nodes in each layer should be aligned. As we have introduced in the previous subsection, some improved version of classic monolayer algorithms, e.g., GenLouvain has been regarded as a benchmark and is really worth expecting for general multilayer networks. We can anticipate four prospective directions, i.e., random walk-based method, tensor decomposition, nonnegative matrix factorization, and modularity optimization will receive increasing attention over time.

In addition to the above-mentioned directions, quite a part of algorithms focus on overlapping community detection (Liu et al. 2018) and local community detection (Interdonato et al. 2017; Jeub et al. 2015; Li et al. 2019). On the one hand, with the increasing of network scale, global computation becomes time-consuming, which promoting local community detection into our view. Liu et al. (2017) proposed an improved multi-objective evolutionary approach for community detection in multilayer networks. Aiming at solving the local community detection problem, they employ a string-based representative scheme and genetic operation and local search. However, the algorithm adapts the strategy of conducting the Louvain algorithm (Blondel et al. 2008) on each layer and then merges the partitions, which seems to deviate from the multilayer community concept. More than that, comparisons with other competitors are not provided. On the other hand, overlapping communities are also ubiquitous in multilayer networks (De Domenico et al. 2016), i.e., some nodes are attached to multiple partitions simultaneously (Chen et al. 2016). Kao and Porter (2018) proposed a method based on computing pairwise similarities between layers and then executing community detection for grouping structurally similar layers in multiplex networks. The algorithm is verified in both synthetic and empirical multiplex networks. As most of the compared algorithms are designed for multiplex networks, there’s still a great deal of works to do in community detection in the general multilayer networks.

<html><body><table><tr><td>Name</td><td>Classification</td><td>Strategy</td><td>Complexity a</td><td>Network</td></tr><tr><td>PMM (Tang et al. 2009)</td><td>Aggregation</td><td>Multilayer modularity maximization</td><td>0(n3L)</td><td>Multi-dimensional</td></tr><tr><td>MULTICLUS (Papalexakis et al.2013)</td><td>Aggregation</td><td>Minimum description length</td><td>0(mnIC²)</td><td>Multiplex, bipartite</td></tr><tr><td>GRAPHFUSE (Papalexakis et al. 2013)</td><td>Aggregation</td><td>Tensor analy sis</td><td>0(n3L）</td><td> Multiplex</td></tr><tr><td>ABACUS (Berlingerio et al. 2013) b</td><td>Aggregation</td><td>Multilayer modularity maximization</td><td>1</td><td>Multi-dimensional</td></tr><tr><td>DNMF (Jiao et al. 2017)</td><td>Aggregation</td><td>Nonnegative matrix factorization</td><td>0(n2L）</td><td>Multiplex, temporal</td></tr><tr><td>EMCD (Tagarelli et al. 2017) c</td><td>Aggregation</td><td>Modularity maximization</td><td>0(I(m + LC))</td><td>Multiplex</td></tr><tr><td>Multilink (Mondragon et al. 2018)</td><td>Aggregation</td><td>Multilink similarity</td><td>0（m²）</td><td>Multplex</td></tr><tr><td>M-EMCD* (Mandaglio et al. 2018)</td><td>Aggregation</td><td>Modularity maximization</td><td>0(1(m + LC))</td><td>Multplex</td></tr><tr><td>M-Motif (Huang et al. 2019)</td><td>Aggregation</td><td>Merge partitions across layers</td><td>O(n log(n)L2)</td><td>Multilayer</td></tr><tr><td>MEMM (Zhang et al. 2019)</td><td>Aggregation</td><td>Multilayer edge mixture model</td><td>0（n2）</td><td>Multiplex</td></tr><tr><td>HSBM (Paez et al. 2019)</td><td>Aggregation</td><td>Hierarchical SBM and Bayes</td><td>0(n2Lc²)</td><td>Multplex</td></tr><tr><td>Variational-Bayes (Ali et al. 2019)</td><td>Aggregation</td><td>SBM and variational Bayes</td><td>O(n2L²c）</td><td>Multiplex, weighted</td></tr><tr><td>GenLouvain (Jutla et al. 2011)</td><td>Direct</td><td> Multiplex map equation</td><td>O(n2 logn)</td><td>Multiplex, temporal</td></tr><tr><td>MultiGA (Amelio and Pizzuti 2014b)</td><td>Direct</td><td>Genetic representation</td><td>0(n2L)</td><td>Multiplex</td></tr><tr><td>MultiMOGA (Amelio and Pizzuti 2014a)</td><td>Direct</td><td>Multi-objective optimization</td><td>O(LCn²)</td><td> Multiplex</td></tr><tr><td>CLAN (Dabideen et al. 2014)</td><td>Direct</td><td>Variational label propagation</td><td>O(LInK)</td><td> Multiplex, temporal</td></tr><tr><td>LART (Kuncheva and Montana 2015)</td><td>Direct</td><td>Random walk</td><td>0（m3）</td><td> Multiplex</td></tr><tr><td>Multiplex-Infomap (De Domenico et al. 2015a)</td><td>Direct</td><td> Multiplex map equation</td><td>0（n2）</td><td>Multiplex</td></tr><tr><td>LocalNCPs (Jeub et al. 2015) d</td><td>Direct</td><td>Local random walk</td><td>≥ O(nI KL)</td><td>Multiplex</td></tr><tr><td>BAZZI (Bazzi et al. 2016)</td><td>Direct</td><td>Multilayer modularity maximization</td><td>0(n12L)</td><td> Multiplex, temporal</td></tr><tr><td>ML-LCD (Interdonato et al. 2017)</td><td>Direct</td><td>Local objective function maximization</td><td>≥ 0(C³ K²L)</td><td>Multiplex</td></tr></table></body></html>

<html><body><table><tr><td>Name</td><td>Classification</td><td>Strategy</td><td>Complexity a</td><td>Network</td></tr><tr><td>GN-QM (Pramanik et al.2017)</td><td>Direct</td><td>Maximum betweenness edges removal</td><td>0(nm2)</td><td> Multiplex</td></tr><tr><td>Louvain-Qm (Pramanik et al.2017)</td><td>Direct</td><td>Modularity optimization</td><td>0（m3）</td><td>Multiplex, weighted</td></tr><tr><td>MLMaOP (Pizzuti and Socievole 2017) e</td><td>Direct</td><td>Multi-objective Optimization</td><td>一</td><td>Multiplex</td></tr><tr><td>NFC (Aslak et al.2018)</td><td>Direct</td><td> Random walk and Infomap</td><td>O(m(n + m))</td><td>Multiplex, temporal</td></tr><tr><td>S2-jNMF (Ma et al.2018)</td><td>Direct</td><td>Nonnegative matrix factorization</td><td>0(rn2km)</td><td>Multiplex</td></tr><tr><td>MNLPA (Alimadadi et al. 2019)</td><td>Direct</td><td>Label Propagation</td><td>0(nk)</td><td>Multiplex,directed, weighted</td></tr><tr><td>terModMax (Pamfil et al.2019)</td><td>Direct</td><td> SBM and Modularity maxminization</td><td>0(n2L)</td><td> Multiplex, temporal</td></tr><tr><td>TMSCD (Kuncheva and Montana 2017,2019)</td><td>Direct</td><td>Spectral graph wavelet</td><td>0（n2L）</td><td>Multiplex, temporal</td></tr><tr><td>CMNC (Chen et al.2019)</td><td>Direct</td><td>Tensor Decomposition</td><td>0（n³L)</td><td>Multiplex</td></tr><tr><td>MCD-Berlingerio (Berlingerio et al.2011a) f</td><td>Flattening</td><td>Employing monolayer algorithms</td><td></td><td>Multi-dimensional</td></tr><tr><td>CDHIA (Tang et al.2012b)</td><td>Flattening</td><td>network integration and k-means</td><td>≥ O(nICK)</td><td>Multi-dimensional</td></tr><tr><td>AggregationPan (Pan et al. 2018)</td><td>Flattening</td><td>Cutting edges with weight &lt; threshold</td><td>O((m +n)L)</td><td>Multiplex, weighted</td></tr><tr><td>ParticleGao (Gao et al. 2019)</td><td>Flattening</td><td>Particle Competition</td><td>0(nICL2)</td><td>Multiplex,directed, weighted</td></tr></table></body></html>

(LInK g    p;      . mmunity detection algorithm. For a given node, the complexity is approximately O(LInK/C). For C partition umber of iterationstoconverenceatalocalotimumCisthenumber f nodes and edges, respectively. L is the number of layers, K is the average degree of nodes, I denotes the iteration t US depends on the complexity of the employed monolayer algorithms, e.g., O(n) from LPA (Raghavan et al. 2007) r o A   
p    g p, y   . ramework via flattening a multi-dimensional network into a weighted network, and then employs the existing monol ititi y of MLMaOPdeendsonanuncertainconverencerocessthereb   
n, thereby the complexy s unc

In brief, the research on community detection for multilayer networks is just in its infancy. At the time of this writing, there is still no standard algorithms for general multilayer networks and quite a few problems remain to be solved, such as the optimization of algorithm process to avoid time-consuming procedures, the extending of algorithms for applying in general form of multilayer networks, the simplification of mathematical model, and so on.

# 4 Applications

The study of detecting community structures in multilayer networks is experiencing a blossom in the last decade. Relevant researches cover various aspects among our daily life such as analyzing influential users in multiple social platforms (Al-Garadi et al. 2018), finding organization of proteins in a biological system (Gosak et al. 2018) and managing urban transportation system with various traffic manners (Liu et al. 2019), etc. The following subsections summarized applications of community detection via a multilayer network framework.

# 4.1 Temporal networks partition

Community detection in temporal networks, i.e., temporal community detection, is required to find how communities emerge, grow, combine, and decay in an evolving process (Kawadia and Sreenivasan 2012). A common approach to detect temporal communities is to obtain communities independently in each snapshot by utilizing static methods and then map the partitions between two snapshots together as many as possible. Obviously, it fails to achieve the goal of revealing the evolving process because such methods do not adequately use partitions found in past snapshots to inform the identification for the optimal partition on the current snapshot (Jiao et al.

2017). Thus, as the foremost step of modeling, the traditional graph model is incapable of presenting inter-connections in a temporal network.

Multilayer network model is commonly employed in the study of time-varying networks (or temporal networks, multi-slice networks), in which the time snapshots are modeled as layers and the layers are ordered by a certain sequence. However, there’s a foundational question: Across how many layers must a community persist in order for layer aggregation to benefit detection? To solve this problem, a layer aggregation approach (De Domenico et al. 2014) is proposed to reduce data size or as a data filter to benefit network-analysis outcomes. Since Mucha et al. (2010) introduced the multiplex modularity optimization method, numerous attempts were made in this field (Drugan et al. 2011; Nguyen et al. 2011; Li and Garcia-Luna-Aceves 2013), which opened up a upsurge in unveiling the communities in time-varying networks. Taylor et al. (2017) proposed the random matrix theory and found layer aggregation to significantly influence detectability. The detectability limitation is described as the ability of network structure to form a community, i.e., if the community structure is too weak, it cannot be found upon inspection of the network (Lancichinetti and Fortunato 2011). When the aggregative network corresponds to the summation of the adjacency matrices encoding the network layers, aggregation always improves detectability. The research is beneficial to understand the contraction of network layers and analyze pairwise-interaction data to obtain sparse network representations. The application of layer aggregation can be used for anomaly detection in network data, e.g., in cybersecurity, detecting harmful events such as attacks, intrusions, and fraud.

# 4.2 Transportation networks optimization

On account of the critical role of transportation system in modern society, the study on traffic dynamics has become one of the most successful applications of complex network theroy. However, the vast majority of researches treat transportation networks as an isolated system, which is inconsistent with the fact that many complex networks are interrelated in a nontrivial way (Du et al. 2016). Analogously, the transportation system has a variety of traffic manners, such as bus, subway, tram, high-speed train, airline, ship, etc, hence a comprehensive study should cover many of such manners. Early researches of traffic networks mainly focus on a single traffic way and ignore the interactions between their counterparts (Calimente 2012; Chen et al. 2014). Du et al. (2016) utilized a two-layered traffic network to study the distribution-based strategy and improved the generating rate of passengers using a particle swarm optimization algorithm. The multilayer network model utilized in this work is an idealized transportation system, in which each layer has a different topology and supports different traveling speeds. The passengers are allowed to travel along the path of minimal traveling time and with the additional cost they can transfer from one layer to another to avoid congestion. The research indicates that a degree centrality-based strategy is not overly beneficial in enhancing the performance of the system. However, starting from such a strategy and reassigning transfer costs using a particle swarm optimization algorithm improve the capacity and several other properties of the system at a reasonable computational cost. The research is rewarding to the selection of traffic manners and exemplifies how multilayer network models are applied in the urban transportation system.

Inspired by the complex network theory and the multilayer network representation, Hong and Liang (2016) analyze the Chinese airline transportation system with the multilayer network framework, in which each layer is defined by a commercial airline (company) and the weights of links are set by the number of flights, the number of seats and the geographical distance between pairs of airports, respectively. By calculating the clustering coefficient, average shortest path length, and assortativity coefficient of the airports, the research has shown that the Chinese airline is of considerably higher value of a maximal degree and betweenness than the other top airlines. Ding et al. (2018) proposed a method for measurements in areas of Kuala Lumpur (i.e., the national capital of Malaysia) to detect communities. The multilayer network model employed in their research contains the railway layer and urban street layer, which mainly focuses on detecting the changing structures of a rail network and mining in urban network communities. The experimental results suggest that rail network growth triggers structural and community changes, i.e., when an upper-layer rail network grows from a simple tree-like network to a more intricate form, the network diameter and average shortest path length decrease dramatically. The growth of the network allows the remainder of the network to be easily visited, which provides suggestive patterns for city development. Yildirimoglu and Kim (2018) analyzed the urban traffic network by combing bus lines, passenger trajectories, and vehicle trajectories together and formed a three-layered network. By applying the Louvain algorithm (Blondel et al. 2008) independently on the three layers, they found that aggerated patterns can shape geographically well-connected communities in the urban traffic network. The spatial structure is quite alike for the bus and passenger layers, which benefits transit authority in making location decisions. The research is beneficial from a planning perspective that sub-regional borders designate the influential areas around local centers, shopping districts, school zones, etc., and cities can develop policies in order to improve the accessibility to them and enhance network performance.

# 4.3 Social network analysis

Another hot-point of community detection research in multilayer networks is social network analysis (Alhajj and Rokne 2014). Social networks have been studied fairly extensively over the last couple of decades, mainly in the general context of analyzing interactions between people in order to determine important structural patterns in such interactions. With the utilization of plentiful data resources from online social media such as Facebook, Twitter, and Flickr, there’s an increasing tendency in discovering community structures in such time-varying social networks (Alimadadi et al. 2019; Rozario et al. 2019; Zhou et al. 2007, 2016). The emergence of online social networks has altered millions of web users’ behavior so that their interactions with each other produce huge amounts of data on various activities. Facebook and Twitter, as the top-two popular social media in our daily life, have been widely employed for social network analysis in recent years (Alimadadi et al. 2019; Türker and Sulak 2018).

The analysis of social networks is usually accompanied by various applications such as information propagation, internal trades analysis, influential spreaders identification, and so on. Diffusion processes, like the propagation of information or the spreading of diseases, are fundamental phenomena occurring in social networks. While the study of diffusion processes in single networks has received a great deal of interest from various disciplines for over a decade, diffusion on multilayer networks is still a young and promising research area, presenting many challenging research issues (Salehi et al. 2015). Numerous attempts have been made to uncover the community structures in international trades, typically represented as bipartite networks in which connections can be established between countries and industries (Alves et al. 2019). Biondo et al. (2017) present a multilayer network model with contagion dynamics, which is able to simulate the spreading of information and the transactions phase of a typical financial market. In their two-layered network framework, the first layer comprises the trading decisions of investors, and the second layer is constructed of the information dynamics, which is fruitfully beneficial to explain the aggregate behavior of markets. Basaras et al. (2017) proposed an effective method to detect influential spreaders in multilayer networks based on the underlying community structures. The experimental evaluation shows that the proposed method outperforms the major competitors proposed so far for either single-layer or multilayer networks.

The above-mentioned applications mainly focus on a local structure or some certain context-based community detection for the case of large volume and various dynamic changes of networks. Thus, it is of great significance in designing some smart algorithms to mine the valuable information among plentiful social network resources.

# 4.4 Research on biological systems

Biological systems, from a cell to the human brain, are intrinsically complex (Ma’ayan 2017). Multilayer networks, described by an intricate network of relationships across multiple scales, are most widely employed in representing such systems. The majority of the biological processes are constituted by a group of proteins that are connected densely (Cui et al. 2012). The protein-protein interaction (PPI) network contains the communications among the protein groups that communicate with each other closely, which can be used to predict the complexity of the function of normal proteins (Srihari et al. 2017). In general, there are two typical protein communities: protein complexes and protein functional modules. Protein complexes are sets of proteins that interact with each other to execute a single multimolecular mechanism. Protein functional modules are sets of proteins that participate in a particular biological process, and interact with each other at different time and places (Spirin and Mirny 2003). Recently, several studies are highlighting how simple networks, i.e., obtained by aggregating or neglecting temporal or categorical descriptions of biological data, are not able to account for the richness of information characterizing biological systems (De Domenico 2018). Chen et al. (2018a) proposed an MLPCD algorithm by integrating Gene Expression Data (GED) and a parallel solution of MLPCD using cloud computing technology. They reconstructed the weighted protein-protein interaction (WPPI) network by combining PPI network and related GED, and then defined simplified modularity as the ratio of in-degrees and out-degrees of proteins in a community. By utilizing an improved Louvain algorithm (Blondel et al. 2008), they have achieved the goal of detecting protein complexes and protein function modules.

Although non-overlapping communities are more commonly studied in network neuroscience, a model of community structure that allows for overlapping networks offers a more realistic presentation of brain network organization (Wu et al. 2011). Taking overlapping communities into consideration, Zhang et al. (2018a) propose a central edge selection (CES) based community detection algorithms for PPI networks. Experimental results on three benchmark networks and two PPI networks indicate the excellent performance of the proposed CES algorithm. Kurmukov et al. (2017) propose a framework to compare both overlapping and non-overlapping community structures of brain networks within the machine learning settings. The performance of the proposed framework is verified in the task of classifying Alzheimer’s disease, mild cognitive impairment, and healthy participants. Pan et al. (2018) present an aggregation approach to detect communities in multilayer biological networks, which first constructs a consensus graph form multiple networks and then applies traditional algorithms to detect communities. Inspired by the fact of few shared edges existed among different networks, they merge the weights of edges from different layers and cut off the nodes with low weights. The approach is simple but limited by the application scenarios.

Another notable direction of biological research is about human brain networks. Cantini et al. (2015) propose a multi-network-based strategy to integrate different layers of genomic information and use them in a coordinated way to identify diving cancer genes. The multi-networks they focus, combine transcription factor co-targeting, microRNA, cotargeting, protein-protein interaction, and gene co-expression networks. The combination of different layers benefits extracting from the multi-networks indications on the regulatory pattern and functional role of both the already known and the new candidate diver genes. Sanchez-Rodriguez et al. (2019) introduce an approach for the detection of a modular organization by considering the temporal scales of the information flow over large-scale brain graphs, and several organizational patterns existing in the brain anatomical and functional networks are found. The structures may coexist together, in a dynamical way that is given by the temporal scales of the activity they produce, guaranteeing functional independence and coordination.

In brief, discovering the underlying patterns in biological networks is experiencing a blossom. With the development of network science, multi-biological networks provide plentiful data resources than ever before, which requires us to dedicate more to this promising field.

# 5 Outlook

As interdisciplinary research with a variety of prospective applications, complex network has been receiving increasing attention from the scientific community. Inspired by prosperous real-world scenarios such as social networks, biological networks, and transportation networks, extensive researches have been dedicated to the extraction of non-trivial knowledge from such networks. Along with the further study, scholars come to realize many systems are inherently represented by a multilayer network, in which edges exist in multiple layers that encode differently but potentially related, types of interactions, and it is important to uncover the interlayer community structures in a complex system.

This paper first presents the various formats of multilayer networks and then introduces the two basic mathematical models. Subsequently, the quality evaluation measures and several typical community detection algorithms are introduced, including label propagation-based algorithm, nonnegative matrix factorization, random walk methods, and multi-objective optimization methods, and so on. After a comprehensive analysis of the above-mentioned methods, we conclude that most of the existing methods are designed for multiplex networks, i.e., the nodes in each layer are aligned, which limits the research on universal multilayer network format. Besides, the algorithms are with high computational complexity and can hardly obtain reasonable partitions among large-scale multilayer networks. A great deal of works remain to be done in the future, such as designing more efficient algorithms for temporal networks with numerous layers and exploring the community structures in special formats of multilayer networks.

# References

Ahmed I, Witbooi P, Christoffels A (2018) Prediction of human-bacillus anthracis protein-protein interactions using multi-layer neural network. Bioinformatics 34(24):4159–4164   
Al-Garadi MA, Varathan KD, Ravana SD, Ahmed E, Mujtaba G, Khan MUS, Khan SU (2018) Analysis of online social network connections for identification of influential users: survey and open research issues. ACM Comput Surv 51(1):1–37   
Aldecoa R, Marín I (2011) Deciphering network community structure by surprise. PLoS ONE 6(9):e24195   
Aldecoa R, Marín I (2013) Surprise maximization reveals the community structure of complex networks. Sci Rep 3(1):1–9   
Alhajj R, Rokne J (2014) Encyclopedia of social network analysis and mining. Springer, Berlin detection. In: ICASSP 2019-2019 IEEE international conference on acoustics, speech and signal processing (ICASSP). IEEE, pp 8142–8146   
Alimadadi F, Khadangi E, Bagheri A (2019) Community detection in facebook activity networks and presenting a new multilayer label propagation algorithm for community detection. Int J Mod Phys B 33(10):1950089   
Alves LG, Mangioni G, Cingolani I, Rodrigues FA, Panzarasa P, Moreno Y (2019) The nested structural organization of the worldwide trade multi-layer network. Sci Rep 9(1):1–14   
Amelio A, Pizzuti C (2014a) Community detection in multidimensional networks. In: 2014 IEEE 26th international conference on tools with artificial intelligence. IEEE, pp 352–359   
Amelio A, Pizzuti C (2014b) A cooperative evolutionary approach to learn communities in multilayer networks. In: International conference on parallel problem solving from nature. Springer, pp 222–232   
Ansari A, Koenigsberg O, Stahl F (2011) Modeling multiple relationships in social networks. J Mark Res 48(4):713–728   
Aslak U, Rosvall M, Lehmann S (2018) Constrained information flows in temporal networks reveal intermittent communities. Phys Rev E 97(6):062312   
Baltakiene M, Baltakys K, Cardamone D, Parisi F, Radicioni T, Torricelli M, de Jeude J, Saracco F (2018) Maximum entropy approach to link prediction in bipartite networks. arXiv preprint arXiv:1805.04307   
Barabási AL, Albert R (1999) Emergence of scaling in random networks. Science 286(5439):509–512   
Basaras P, Iosifidis G, Katsaros D, Tassiulas L (2017) Identifying influential spreaders in complex multilayer networks: a centrality perspective. IEEE Trans Netw Sci Eng 6(1):31–45   
Battiston F, Nicosia V, Latora V (2014) Structural measures for multiplex networks. Phys Rev E 89(3):032804   
Bayati M, Gleich DF, Saberi A, Wang Y (2013) Message-passing algorithms for sparse network alignment. ACM Trans Knowl Discov Data 7(1):1–31   
Bazzi M, Porter MA, Williams S, McDonald M, Fenn DJ, Howison SD (2016) Community detection in temporal multilayer networks, with an application to correlation networks. Multiscale Model Simul 14(1):1–41   
Berlingerio M, Coscia M, Giannotti F (2011a) Finding and characterizing communities in multidimensional networks. In: 2011 international conference on advances in social networks analysis and mining. IEEE, pp 490–494   
Berlingerio M, Coscia M, Giannotti F (2011b) Finding redundant and complementary communities in multidimensional networks. In: Proceedings of the 20th ACM international conference on Information and knowledge management, pp 2181–2184   
Berlingerio M, Coscia M, Giannotti F, Monreale A, Pedreschi D (2011c) The pursuit of hubbiness: analysis of hubs in large multidimensional networks. J Comput Sci 2(3):223–237   
Berlingerio M, Pinelli F, Calabrese F (2013) Abacus: frequent pattern mining-based community discovery in multidimensional networks. Data Min Knowl Disc 27(3):294–320   
Biondo AE, Pluchino A, Rapisarda A (2017) Informative contagion dynamics in a multilayer network model of financial markets. Ital Econ J 3(3):343–366   
Black J (2018) Urban transport planning: theory and practice, vol 4. Routledge, Abingdon   
Blondel VD, Guillaume JL, Lambiotte R, Lefebvre E (2008) Fast unfolding of communities in large networks. J Stat Mech Theory Exp 2008(10):P10008   
Boccaletti S, Bianconi G, Criado R, Del Genio CI, Gómez-Gardenes J, Romance M, Sendina-Nadal I, Wang Z, Zanin M (2014) The structure and dynamics of multilayer networks. Phys Rep 544(1):1–122   
Bollobás B (2013) Modern graph theory, vol 184. Springer, Berlin   
Bonacich P (1972) Factoring and weighting approaches to status scores and clique identification. J Mathematical Sociology 2(1):113–120   
Bonacich P (1987) Power and centrality: a family of measures. Am J Sociol 92(5):1170–1182   
Brin S, Page L (1998) The anatomy of a large-scale hypertextual web search engine. Comput Netw ISDN Syst 30(1–7):107–117   
Brouwer AE, Haemers WH (2012) Distance-regular graphs. In: Axler S, Capasso V, Casacuberta C, MacIntyre AJ, Ribet K, Sabbah C, Süli E, Woyczynski WA (eds) Spectra of graphs. Springer, pp 177–185   
Brummitt CD (2014) Models of systemic events: interdependence, contagion, and innovation. University of California, Davis   
Buldyrev SV, Parshani R, Paul G, Stanley HE, Havlin S (2010) Catastrophic cascade of failures in interdependent networks. Nature 464(7291):1025–1028 conference on principles of data mining and knowledge discovery. Springer, pp 445–452   
Calimente J (2012) Rail integrated communities in Tokyo. J Trans Land Use 5(1):19–32   
Cantini L, Medico E, Fortunato S, Caselle M (2015) Detection of gene communities in multi-networks reveals cancer drivers. Sci Rep 5:17386   
Caramia M, Dell’Olmo P (2008) Multi-objective management in freight logistics: increasing capacity, service level and safety with optimization algorithms. Springer, Berlin   
Carmagnola F, Cena F (2009) User identification for cross-system personalisation. Inf Sci 179(1–2):16–32   
Carmi S, Havlin S, Kirkpatrick S, Shavitt Y, Shir E (2007) A model of internet topology using k-shell decomposition. Proc Nat Acad Sci 104(27):11150–11154   
Cazabet R, Chawuthai R, Takeda H (2015) Using multiple-criteria methods to evaluate community partitions. arXiv preprint arXiv:1502.05149   
Cellai D, Dorogovtsev SN, Bianconi G (2016) Message passing theory for percolation models on multiplex networks with link overlap. Phys Rev E 94(3):032301   
Chen D, Lü L, Shang MS, Zhang YC, Zhou T (2012) Identifying influential nodes in complex networks. Phys A 391(4):1777–1787   
Chen D, Huang X, Wang D, Jia L (2014) Public transit hubs identification based on complex networks theory. IETE Techn Rev 31(6):440–451   
Chen D, Jia L, Sima D, Huang X, Wang D (2016) Community detection algorithm with membership function. In: Yuan H, Bian F, Geng J (eds) International conference on geo-informatics in resource management and sustainable ecosystem. Springer, pp 185–195   
Chen J, Li K, Bilal K, Metwally AA, Li K, Yu P (2018a) Parallel protein community detection in large-scale PPI networks based on multi-source learning. IEEE/ACM Trans Comput Biol Bioinform. https://doi. org/10.1109/TCBB.2018.2868088   
Chen S, Wang ZZ, Tang L, Tang YN, Gao YY, Li HJ, Xiang J, Zhang Y (2018b) Global vs local modularity for network community detection. PLoS ONE 13(10):e0205284   
Chen Z, Chen C, Zheng Z, Zhu Y (2019) Tensor decomposition for multilayer networks clustering. Proc AAAI Conf Artif Intell 33:3371–3378   
Colladon AF, Remondi E (2017) Using social network analysis to prevent money laundering. Expert Syst Appl 67:49–58   
Cozzo E, Kivelä M, De Domenico M, Solé-Ribalta A, Arenas A, Gómez S, Porter MA, Moreno Y (2015) Structure of triadic relations in multiplex networks. New J Phys 17(7):073029   
Cui G, Shrestha R, Han K (2012) Modulesearch: finding functional modules in a protein-protein interaction network. Comput Methods Biomech Biomed Eng 15(7):691–699   
Dabideen S, Kawadia V, Nelson SC (2014) Clan: An efficient distributed temporal community detection protocol for manets. In: 2014 IEEE 11th international conference on mobile ad hoc and sensor systems. IEEE, pp 91–99   
Dalibard V (2012) Community detection in multi-layer networks. Master’s thesis, University of Cambridge   
Danon L, Diaz-Guilera A, Duch J, Arenas A (2005) Comparing community structure identification. J Stat Mech Theory Exp 20055(09):P09008   
Davis A, Gardner BB, Gardner MR (2009) Deep south: a social anthropological study of caste and class. University of South Carolina Press, Columbia   
De Bacco C, Power EA, Larremore DB, Moore C (2017) Community detection, link prediction, and layer interdependence in multilayer networks. Phys Rev E 95(4):042317   
De Domenico M (2018) Multilayer network modeling of integrated biological systems. arXiv preprint arXiv:1802.01523   
De Domenico M, Solé-Ribalta A, Cozzo E, Kivelä M, Moreno Y, Porter MA, Gómez S, Arenas A (2013) Mathematical formulation of multilayer networks. Phys Rev X 3(4):041022   
De Domenico M, Nicosia V, Arenas A, Latora V (2014) Layer aggregation and reducibility of multilayer interconnected networks. arXiv preprint arXiv:1405.0425   
De Domenico M, Lancichinetti A, Arenas A, Rosvall M (2015a) Identifying modular flows on multilayer networks reveals highly overlapping organization in interconnected systems. Phys Rev X 5(1):011027   
De Domenico M, Porter MA, Arenas A (2015b) Muxviz: a tool for multilayer analysis and visualization of networks. J Compl Netw 3(2):159–176   
De Domenico M, Solé-Ribalta A, Omodei E, Gómez S, Arenas A (2015c) Ranking in interconnected multilayer networks reveals versatile nodes. Nat Commun 6(1):1–6   
De Domenico M, Granell C, Porter MA, Arenas A (2016) The physics of spreading processes in multilayer networks. Nat Phys 12(10):901–906   
Ding R, Ujang N, bin Hamid H, Abd Manan MS, He Y, Li R, Wu J (2018) Detecting the urban traffic network structure dynamics through the growth and analysis of multi-layer networks. Phys A 503:800–817   
Drugan OV, Plagemann T, Munthe-Kaas E (2011) Detecting communities in sparse manets. IEEE/ACM Trans Netw 19(5):1434–1447   
Du WB, Zhou XL, Jusup M, Wang Z (2016) Physics of transportation: towards optimal capacity using the multilayer network framework. Sci Rep 6:19059   
Farina M, Amato P (2002) On the optimal solution definition for many-criteria optimization problems. In: 2002 annual meeting of the North American fuzzy information processing society proceedings. NAFIPS-FLINT 2002 (Cat. No. 02TH8622). IEEE, pp 233–238   
Farooq MJ, Zhu Q (2018) On the secure and reconfigurable multi-layer network design for critical information dissemination in the internet of battlefield things (iobt). IEEE Trans Wireless Commun 17(4):2618–2632   
Feng S, Wang Q, Shen D, Kou Y, Nie T, Yu G (2017) User identification across social networks based on global view features. In: 2017 14th web information systems and applications conference (WISA). IEEE, pp 93–98   
Fortunato S (2010) Community detection in graphs. Phys Rep 486(3–5):75–174   
Fortunato S, Barthelemy M (2007) Resolution limit in community detection. Proc Nat Acad Sci 104(1):36– 41   
Fortunato S, Hric D (2016) Community detection in networks: a user guide. Phys Rep 659:1–44   
Fox PT, Lancaster JL (2002) Mapping context and content: the BrainMap model. Nat Rev Neurosci 3(4):319–321   
Freeman LC (1977) A set of measures of centrality based on betweenness. Sociometry 40:35–41   
Freeman LC (1978) Centrality in social networks conceptual clarification. Soc Netw 1(3):215–239   
Gao J, Buldyrev SV, Havlin S, Stanley HE (2011) Robustness of a network of networks. Phys Rev Lett 107(19):195701   
Gao X, Zheng Q, Verri FA, Rodrigues RD, Zhao L (2019) Particle competition for multilayer network community detection. In: Proceedings of the 2019 11th international conference on machine learning and computing, pp 75–80   
Girvan M, Newman ME (2002) Community structure in social and biological networks. Proc Nat Acad Sci 99(12):7821–7826   
Gosak M, Markoviˇc R, Dolenšek J, Rupnik MS, Marhl M, Stožer A, Perc M (2018) Network science of biological systems at different scales: a review. Phys Life Rev 24:118–135   
Grunwald P (2004) A tutorial introduction to the minimum description length principle. arXiv preprint arXiv:math/0406077   
Halu A, Mondragón RJ, Panzarasa P, Bianconi G (2013) Multiplex pagerank. PLoS ONE 8(10):e78293   
Herlocker JL, Konstan JA, Terveen LG, Riedl JT (2004) Evaluating collaborative filtering recommender systems. ACM Trans Inf Syst 22(1):5–53   
Hong C, Liang B (2016) Analysis of the weighted chinese air transportation multilayer network. In: 2016 12th world congress on intelligent control and automation (WCICA). IEEE, pp 2318–2321   
Huang L, Wang CD, Chao HY (2019) Higher-order multi-layer community detection. Proc AAAI Conf Artif Intell 33:9945–9946   
Interdonato R, Tagarelli A, Ienco D, Sallaberry A, Poncelet P (2017) Local community detection in multilayer networks. Data Min Knowl Disc 31(5):1444–1479   
Jeub LG, Mahoney MW, Mucha PJ, Porter MA (2015) A local perspective on community structure in multilayer networks. arXiv preprint arXiv:1510.05185   
Jiao P, Lyu H, Li X, Yu W, Wang W (2017) Temporal community detection based on symmetric nonnegative matrix factorization. Int J Mod Phys B 31(13):1750102   
Jutla IS, Jeub LG, Mucha PJ (2011) A generalized louvain method for community detection implemented in matlab. http://netwikiamathuncedu/GenLouvain   
Kanawati R (2015) Multiplex network mining: A brief survey. IEEE Intell Informatics Bull 16(1):24–27   
Kao TC, Porter MA (2018) Layer communities in multiplex networks. J Stat Phys 173(3–4):1286–1302   
Kawadia V, Sreenivasan S (2012) Sequential detection of temporal communities by estrangement confinement. Sci Rep 2:794 Kazienko P, Brodka P, Musial K (2010) Individual neighbourhood exploration in complex multi-layered social network. In: 2010 IEEE/WIC/ACM international conference on web intelligence and intelligent agent technology. IEEE, vol 3, pp 5–8 Kempe D, Kleinberg J, Kumar A (2002) Connectivity and inference problems for temporal networks. J Comput Syst Sci 64(4):820–842 Kivelä M, Arenas A, Barthelemy M, Gleeson JP, Moreno Y, Porter MA (2014) Multilayer networks. J Complex Netw 2(3):203–271 Kostakos V (2009) Temporal graphs. Phys A 388(6):1007–1023 Kuncheva Z, Montana G (2015) Community detection in multiplex networks using locally adaptive random walks. In: Proceedings of the 2015 IEEE/ACM international conference on advances in social networks analysis and mining 2015, pp 1308–1315 Kuncheva Z, Montana G (2017) Multi-scale community detection in temporal networks using spectral graph wavelets. In: International workshop on personal analytics and privacy, Springer, pp 139–154 Kuncheva Z, Montana G (2019) Spectral multi-scale community detection in temporal networks with an application. arXiv preprint arXiv:1901.10521 Kurmukov A, Ananyeva M, Dodonova Y, Gutman B, Faskowitz J, Jahanshad N, Thompson P, Zhukov L (2017) Classifying phenotypes based on the community structure of human brain networks. Graphs in biomedical image analysis, computational anatomy and imaging genetics. Springer, Berlin, pp 3–11 Laird AR, Lancaster JL, Fox PT (2005) The social evolution of a human brain mapping database. Neuroinformatics 3(1):65–78 Lancichinetti A, Fortunato S (2011) Limits of modularity maximization in community detection. Phys Rev E 84(6):066122 Lancichinetti A, Fortunato S, Radicchi F (2008) Benchmark graphs for testing community detection algorithms. Phys Rev E 78(4):046110 Lancichinetti A, Fortunato S, Kertész J (2009) Detecting the overlapping and hierarchical community structure in complex networks. New J Phys 11(3):033015 Lee DD, Seung HS (2001) Algorithms for non-negative matrix factorization. In: Leen TK, Dietterich TG, Tresp V (eds) Advances in neural information processing systems. MIT Press, pp 556–562. http:// papers.nips.cc/paper/1861-algorithms-for-non-negative-matrix-factorization.pdf Li C, Zhang Y (2020) A personalized recommendation algorithm based on large-scale real micro-blog data. Neural Comput Appl 32:1–8 Li Q, Garcia-Luna-Aceves J (2013) Opportunistic routing using prefix ordering and self-reported social groups. In: 2013 international conference on computing, networking and communications (ICNC), IEEE, pp 28–34 Li X, Tian Q, Tang M, Chen X, Yang X (2019) Local community detection for multi-layer mobile network based on the trust relation. Wirel Netw 26(8):5503–5515 Li Z, Zhang S, Wang RS, Zhang XS, Chen L (2008) Quantitative function for community detection. Phys Rev E 77(3):036109 Liang W, Meng B, He X, Zhang X (2015) Gcm: A greedy-based cross-matching algorithm for identifying users across multiple online social networks. In: Pacific-Asia workshop on intelligence and security informatics. Springer, pp 51–70 Liu RR, Jia CX, Lai YC (2019) Remote control of cascading dynamics on complex multilayer networks. New J Phys 21(4):045002 Liu W, Suzumura T, Ji H, Hu G (2018) Finding overlapping communities in multilayer networks. PLoS ONE 13(4):e0188747 Liu X, Wang W, He D, Jiao P, Jin D, Cannistraci CV (2017) Semi-supervised community detection based on non-negative matrix factorization with node popularity. Inf Sci 381:304–321 Loe CW, Jensen HJ (2015) Comparison of communities detection algorithms for multiplex. Phys A 431:29–   
45 Lü L, Zhang YC, Yeung CH, Zhou T (2011) Leaders in social networks, the delicious case. PLoS ONE   
6(6):e21202 Lü L, Chen D, Ren XL, Zhang QM, Zhang YC, Zhou T (2016) Vital nodes identification in complex networks. Phys Rep 650:1–63 Ma X, Dong D, Wang Q (2018) Community detection in multi-layer networks using joint nonnegative matrix factorization. IEEE Trans Knowl Data Eng 31(2):273–286 Ma’ayan A (2017) Complex systems biology. J R Soc Interface 14(134):20170391   
MacQueen J et al (1967) Some methods for classification and analysis of multivariate observations. Proceedings of the fifth Berkeley symposium on mathematical statistics and probability, Oakland, CA, USA 1:281–297   
Mandaglio D, Amelio A, Tagarelli A (2018) Consensus community detection in multilayer networks using parameter-free graph pruning. In: Pacific-Asia conference on knowledge discovery and data mining. Springer, pp 193–205   
Mondragon RJ, Iacovacci J, Bianconi G (2018) Multilink communities of multiplex networks. PLoS ONE 13(3):e0193821   
Mucha PJ, Richardson T, Macon K, Porter MA, Onnela JP (2010) Community structure in time-dependent, multiscale, and multiplex networks. Science 328(5980):876–878   
Newman M (2018) Networks. Oxford University Press,   
Newman ME, Girvan M (2004) Finding and evaluating community structure in networks. Phys Rev E 69(2):026113   
Newman ME, Leicht EA (2007) Mixture models and exploratory analysis in networks. Proc Nat Acad Sci 104(23):9564–9569   
Ng AY, Jordan MI, Weiss Y (2002) On spectral clustering: analysis and an algorithm. In: Advances in neural information processing systems, pp 849–856   
Nguyen NP, Dinh TN, Tokala S, Thai MT (2011) Overlapping communities in dynamic networks: their detection and mobile applications. In: Proceedings of the 17th annual international conference on Mobile computing and networking, pp 85–96   
Nicolini C, Bifone A (2016) Modular structure of brain functional networks: breaking the resolution limit by surprise. Sci Rep 6(1):1–13   
Nicosia V, Latora V (2015) Measuring and modeling correlations in multiplex networks. Phys Rev E 92(3):032805   
Oselio B, Kulesza A, Hero A (2015) Information extraction from large multi-layer social networks. In: 2015 IEEE international conference on acoustics, speech and signal processing (icassp). IEEE, pp 5451–5455   
Paez MS, Amini AA, Lin L (2019) Hierarchical stochastic block model for community detection in multiplex networks. arXiv preprint arXiv:1904.05330   
Pamfil AR, Howison SD, Lambiotte R, Porter MA (2019) Relating modularity maximization and stochastic block models in multilayer networks. SIAM J Math Data Sci 1(4):667–698   
Pan Z, Hu G, Li D (2018) Detecting communities from multilayer networks: an aggregation approach. In: proceedings of the international conference on intelligent science and technology, pp 6–11   
Paolucci F (2018) Network service chaining using segment routing in multi-layer networks. IEEE/OSA J Opt Commun Netw 10(6):582–592   
Papalexakis EE, Akoglu L, Ience D (2013) Do more views of a graph help? community detection and clustering in multi-graphs. In: Proceedings of the 16th international conference on information fusion. IEEE, pp 899–905   
Perry JW, Allen K, Berry MM (1955) Machine literature searching x. Machine language; factors underlying its design and development. Am Doc (pre-1986) 6(4):242   
Pizzuti C, Socievole A (2017) Many-objective optimization for community detection in multi-layer networks. In: 2017 IEEE congress on evolutionary computation (CEC). IEEE, pp 411–418   
Pramanik S, Tackx R, Navelkar A, Guillaume JL, Mitra B (2017) Discovering community structure in multilayer networks. In: 2017 IEEE international conference on data science and advanced analytics (DSAA). IEEE, pp 611–620   
Raghavan UN, Albert R, Kumara S (2007) Near linear time algorithm to detect community structures in large-scale networks. Phys Rev E 76(3):036106   
Rocklin M, Pinar A (2013) On clustering on graphs with multiple edge types. Internet Math 9(1):82–112   
Roethlisberger FJ, Dickson WJ (2003) Management and the worker, vol 5. Psychology Press, New York   
Rossetti G, Guidotti R, Miliou I, Pedreschi D, Giannotti F (2016a) A supervised approach for intra-/intercommunity interaction prediction in dynamic social networks. Soc Netw Anal Mining 6(1):86   
Rossetti G, Pappalardo L, Rinzivillo S (2016b) A novel approach to evaluate community detection algorithms on ground truth. In: Complex networks VII. Springer, pp 133–144   
Rosvall M, Bergstrom CT (2008) Maps of random walks on complex networks reveal community structure. Proc Nat Acad Sci 105(4):1118–1123   
Rozario VS, Chowdhury A, Morshed MSJ (2019) Community detection in social network using temporal data. arXiv preprint arXiv:1904.05291   
Salavati C, Abdollahpouri A, Manbari Z (2018) Bridgerank: a novel fast centrality measure based on local structure of the network. Phys A 496:635–653   
Salehi M, Sharma R, Marzolla M, Magnani M, Siyari P, Montesi D (2015) Spreading processes in multilayer networks. IEEE Trans Netw Sci Eng 2(2):65–83   
Sanchez-Rodriguez LM, Iturria-Medina Y, Mouches P, Sotero RC (2019) A method for multiscale community detection in brain networks. bioRxiv p 743732   
Schütze H, Manning CD, Raghavan P (2008) Introduction to information retrieval, vol 39. Cambridge University Press, Cambridge   
Silber MD (2011) The Al Qaeda factor: plots against the West. University of Pennsylvania Press, Philadelphia   
Solá L, Romance M, Criado R, Flores J, García del Amo A, Boccaletti S (2013) Eigenvector centrality of nodes in multiplex networks. Chaos Interdiscip J Nonlinear Sci 23(3):033131   
Spirin V, Mirny LA (2003) Protein complexes and functional modules in molecular networks. Proc Nat Acad Sci 100(21):12123–12128   
Srihari S, Yong CH, Wong L (2017) Computational prediction of protein complexes from protein interaction networks. Morgan & Claypool, Williston   
Sultana S, Salon D, Kuby M (2019) Transportation sustainability in the urban context: a comprehensive review. Urban Geogr 40(3):279–308   
Tagarelli A, Amelio A, Gullo F (2017) Ensemble-based community detection in multilayer networks. Data Min Knowl Disc 31(5):1506–1543   
Tang JK, Leontiadis L, Scellato S, et al. (2012a) Temporal network metrics and their application to real world networks. PhD thesis, Citeseer   
Tang L, Wang X, Liu H (2009) Uncoverning groups via heterogeneous interaction analysis. In: 2009 Ninth IEEE international conference on data mining. IEEE, pp 503–512   
Tang L, Wang X, Liu H (2012b) Community detection via heterogeneous interaction analysis. Data Min Knowl Disc 25(1):1–33   
Taylor D, Caceres RS, Mucha PJ (2016a) Detectability of small communities in multilayer and temporal networks: eigenvector localization, layer aggregation, and time series discretization. Tech. rep   
Taylor D, Shai S, Stanley N, Mucha PJ (2016b) Enhanced detectability of community structure in multilayer networks through layer aggregation. Phys Rev Lett 116(22):228301   
Taylor D, Caceres RS, Mucha PJ (2017) Super-resolution community detection for layer-aggregated multilayer networks. Phys Rev X 7(3):031056   
Türker I, Sulak EE (2018) A multilayer network analysis of hashtags in twitter via co-occurrence and semantic links. Int J Mod Phys B 32(04):1850029   
Vaiana M, Muldoon S (2018) Resolution limits for detecting community changes in multilayer networks. arXiv preprint arXiv:1803.03597   
Verbrugge LM (1979) Multiplexity in adult friendships. Soc Forces 57(4):1286–1309   
Wang D, Li J, Xu K, Wu Y (2017) Sentiment community detection: exploring sentiments and relationships in social networks. Electron Commer Res 17(1):103–132   
Wang P, Robins G, Pattison P, Lazega E (2013) Exponential random graph models for multilevel networks. Soc Netw 35(1):96–115   
Watts DJ, Strogatz SH (1998) Collective dynamics of ‘small-world’ networks. Nature 393(6684):440–442   
Wu K, Taki Y, Sato K, Sassa Y, Inoue K, Goto R, Okada K, Kawashima R, He Y, Evans AC et al (2011) The overlapping community structure of structural brain network in young healthy individuals. PLoS ONE 6(5):e19608   
Wu W, Kwong S, Zhou Y, Jia Y, Gao W (2018) Nonnegative matrix factorization with mixed hypergraph regularization for community detection. Inf Sci 435:263–281   
Xu X, Yuruk N, Feng Z, Schweiger TA (2007) Scan: a structural clustering algorithm for networks. In: Proceedings of the 13th ACM SIGKDD international conference on Knowledge discovery and data mining, pp 824–833   
Yang Y, Yu H, Huang R, Ming T (2018) A fusion information embedding method for user identity matching across social networks. In: 2018 IEEE SmartWorld, ubiquitous intelligence & computing, advanced & trusted computing, scalable computing & communications, cloud & big data computing, internet of people and smart city innovation (SmartWorld/SCALCOM/UIC/ATC/CBDCom/IOP/SCI), IEEE, pp 2030–2035   
Yiapanis P, Rosas-Ham D, Brown G, Luján M (2013) Optimizing software runtime systems for speculative parallelization. ACM Trans Archit Code Optim 9(4):1–27   
Yildirimoglu M, Kim J (2018) Identification of communities in urban mobility networks using multi-layer graphs of network traffic. Transp Res Part C Emerg Technol 89:254–267   
Zhan J, Sun M, Wu H, Sun H (2018) Using triangles and latent factor cosine similarity prior to improve community detection in multi-relational social networks. Concurr Comput Practi Exp 30(16):e4453   
Zhang F, Ma A, Wang Z, Ma Q, Liu B, Huang L, Wang Y (2018a) A central edge selection based overlapping community detection algorithm for the detection of overlapping structures in protein-protein interaction networks. Molecules 23(10):2633   
Zhang H, Zhuge C, Yu X (2018b) Identifying hub stations and important lines of bus networks: a case study in xiamen, china. Phys A 502:394–402   
Zhang H, Wang CD, Lai JH, Philip SY (2019) Community detection using multilayer edge mixture model. Knowl Inf Syst 60(2):757–779   
Zhang S, Wang RS, Zhang XS (2007) Uncovering fuzzy community structure in complex networks. Phys Rev E 76(4):046103   
Zhao Y, Karypis G (2004) Empirical and theoretical comparisons of selected criterion functions for document clustering. Mach Learn 55(3):311–331   
Zhou D, Councill I, Zha H, Giles CL (2007) Discovering temporal communities from social network documents. In: Seventh IEEE international conference on data mining (ICDM 2007). IEEE, pp 745– 750   
Zhou X, Liang W, Wu B, Lu Z, Nishimura S, Shinomiya T, Jin Q (2016) Dynamic community mining and tracking based on temporal social network analysis. In: 2016 IEEE international conference on computer and information technology (CIT), IEEE, pp 177–182   
Zhu J, Wang B, Wu B, Zhang W (2017) Emotional community detection in social network. IEICE Trans Inf Syst 100(10):2515–2525