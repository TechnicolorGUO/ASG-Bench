# Literature Review: Computational thinking in programming with Scratch in primary schools- A systematic review.

*Generated on: 2025-12-26 21:34:58*
*Progress: [32/50]*
*Saved to: /Users/joanna/Desktop/Literature_Reviews/Computational_thinking_in_programming_with_Scratch_in_primar_20251226_213458.md*
---

# Computational thinking in programming with Scratch in primary schools- A systematic review

### Key Points
*   **Ubiquity of Scratch:** Scratch is the dominant platform for introducing Computational Thinking (CT) in primary education due to its low barrier to entry and block-based visual interface.
*   **Theoretical Framework:** The field heavily relies on Brennan and Resnick’s (2012) framework, which divides CT into Concepts, Practices, and Perspectives.
*   **Assessment Challenges:** While automated tools like Dr. Scratch provide scalable assessment of code, they often fail to capture the iterative "process" of thinking, leading to a reliance on mixed-method approaches including artifact-based interviews.
*   **Curricular Integration:** Recent trends show a shift from teaching Scratch as an isolated subject to integrating it into Mathematics and Science to foster domain-specific problem-solving skills.
*   **Emerging Frontiers:** The integration of Artificial Intelligence (AI) extensions into Scratch represents the newest wave of research, aiming to democratize AI literacy for young children.

## Abstract
**Background:** As digital literacy becomes a prerequisite for the 21st-century workforce, educational systems worldwide are integrating Computational Thinking (CT) into primary school curricula. Scratch, a visual block-based programming environment, has emerged as the primary pedagogical tool for this demographic.
**Objective:** This systematic literature review examines the state of research regarding the development and assessment of CT skills using Scratch in primary education (K-9).
**Method:** A comprehensive analysis of empirical studies, theoretical frameworks, and case studies was conducted to identify key themes, methodologies, and findings.
**Results:** The review identifies that while Scratch effectively lowers the barrier to programming, the definition and assessment of CT remain fragmented. The Brennan and Resnick (2012) framework is the most widely adopted theoretical lens. Assessment methods have evolved from manual code inspection to automated static analysis (e.g., Dr. Scratch) and data-driven process mining.
**Conclusion:** Scratch is effective for fostering algorithmic thinking and creativity. However, significant gaps remain regarding the transferability of skills to non-computing domains, the long-term retention of CT concepts, and the effective professional development of teachers.

## 1. Introduction

The digitization of modern society has necessitated the inclusion of computer science concepts in compulsory education. At the forefront of this educational shift is the concept of Computational Thinking (CT), a term popularized by Wing (2006) to describe the problem-solving processes involved in formulating problems so their solutions can be represented as computational steps and algorithms [cite: 1]. In primary education, the challenge has been to introduce these abstract concepts in a developmentally appropriate manner.

Scratch, developed by the Lifelong Kindergarten group at the MIT Media Lab, has become the de facto standard for introducing programming to young children [cite: 2, 3]. Its "low floor" (easy to get started) and "high ceiling" (ability to create complex projects) make it an ideal environment for fostering CT [cite: 4]. Unlike text-based languages, Scratch eliminates syntax errors through a block-based interface, allowing students to focus on logic and design [cite: 5].

Despite its popularity, the educational objectives of CT in primary schools remain somewhat unclear, with curricula often conflating digital literacy with computational thinking [cite: 6]. Furthermore, there is a lack of consensus on how to assess CT effectively. While some educators focus on the final code artifact, others emphasize the iterative design process [cite: 7]. This review aims to synthesize existing literature to provide a comprehensive overview of how Scratch is used to teach and assess CT, highlighting historical milestones, current methodologies, and future research directions.

## 2. Key Concepts and Definitions

### 2.1 Defining Computational Thinking
While Wing's definition serves as a high-level guide, operationalizing CT for primary education has required more granular frameworks. CT is generally understood not just as programming, but as a set of thinking skills including abstraction, decomposition, pattern recognition, and algorithmic design [cite: 1]. In the context of Scratch, these skills are manifested through the manipulation of media and logic blocks to create interactive stories, games, and animations [cite: 8].

### 2.2 The Brennan and Resnick Framework
The most influential framework in this domain is that proposed by Brennan and Resnick (2012), which was developed specifically through observations of young creators in the Scratch community. This framework categorizes CT into three dimensions:
1.  **Computational Concepts:** The concepts designers use as they program, such as sequences, loops, parallelism, events, conditionals, operators, and data [cite: 2, 9].
2.  **Computational Practices:** The problem-solving practices that occur during programming, including experimenting and iterating, testing and debugging, reusing and remixing, and abstracting and modularizing [cite: 2, 7].
3.  **Computational Perspectives:** The shifts in perspective that learners experience, such as expressing oneself through technology, connecting with others, and questioning the technological world [cite: 2, 9].

### 2.3 Core Educational Principles (CEPs)
Building on previous frameworks, Fagerlund et al. (2020) proposed "Core Educational Principles" to concretize CT for primary education. This approach maps abstract CT concepts to tangible Scratch activities. For example, "Abstraction" is operationalized as understanding that programming languages and algorithms are representations of real-world phenomena, while "Algorithmic Thinking" involves defining clear steps to solve a problem [cite: 6].

## 3. Historical Development and Milestones

### 3.1 From Logo to Scratch
The pedagogical roots of Scratch lie in Constructionism, a theory developed by Seymour Papert, who argued that learning happens best when students are actively engaged in making tangible objects [cite: 3]. Papert's Logo language (1980s) was the first to introduce children to programming via a "turtle" that drew geometric shapes. Scratch represents an evolution of this tradition, moving from text-based commands to a media-rich, block-based environment that supports "tinkering" [cite: 3, 10].

### 3.2 The Rise of Block-Based Coding
The launch of Scratch in 2007 marked a significant milestone. It shifted the focus from syntax to semantics, allowing children to assemble code like LEGO bricks. This visual metaphor made programming accessible to primary school students (ages 7-11) who might struggle with the typing and syntax requirements of languages like Python or Java [cite: 5, 11].

### 3.3 Curricular Integration (2010s-Present)
Following the release of the "Computing at School" curriculum in the UK (2014) and similar initiatives in Finland (2016) and the US, Scratch was widely adopted as the primary tool for implementing these new standards [cite: 5, 12]. Research during this period shifted from usability studies to efficacy studies, examining whether Scratch actually improved problem-solving skills [cite: 1, 13].

## 4. Current State-of-the-Art Methods and Techniques

### 4.1 Automated Assessment: Dr. Scratch
A major challenge in CT education is assessment. Manual evaluation of student projects is time-consuming and subjective. To address this, researchers developed **Dr. Scratch**, a web-based static analysis tool [cite: 14, 15]. Dr. Scratch analyzes Scratch project files and assigns a "CT Score" based on the presence and sophistication of seven computational concepts: abstraction, parallelism, logic, synchronization, flow control, user interactivity, and data representation [cite: 16, 17].
*   **Validity:** Studies comparing Dr. Scratch scores with human expert evaluations have shown strong correlations, suggesting it is a valid proxy for coding proficiency [cite: 16].
*   **Feedback:** Beyond scoring, the tool provides feedback to students, encouraging them to improve their code (e.g., suggesting the use of loops instead of repeated blocks) [cite: 14].

### 4.2 Process Mining and Transaction-Level Data
Critics of static analysis argue that it only evaluates the final product, missing the learning process (e.g., debugging struggles). Recent state-of-the-art methods involve **process mining** or analyzing transaction-level data [cite: 18]. By logging every click and block movement a student makes, researchers can visualize the development of a script over time. This allows for the detection of "productive failure" and specific misconceptions that vanish in the final code [cite: 18, 19].

### 4.3 Qualitative and Mixed Methods
To capture the "Perspectives" dimension of the Brennan and Resnick framework, researchers continue to rely on qualitative methods. **Artifact-based interviews** involve asking students to explain their code, revealing whether they truly understand the blocks they used or if they merely copied them [cite: 2, 20]. **Design scenarios** present students with existing projects to debug or remix, testing their ability to read and interpret code rather than just write it [cite: 20].

## 5. Applications and Case Studies

### 5.1 Integration with Mathematics
A significant body of research focuses on using Scratch to teach primary mathematics. Studies have shown that Scratch can help students visualize abstract mathematical concepts such as geometry, fractions, and variables [cite: 21, 22].
*   **Case Study (Hong Kong):** A study involving 4th-grade students used Scratch to build a "fraction magic calculator." The results showed that programming variables and conditionals helped students internalize the mathematical rules of fractions, effectively blending mathematical thinking with CT [cite: 21].
*   **Case Study (Geometry):** Research indicates that using Scratch to draw shapes (similar to Logo) helps students understand angles and coordinate systems better than traditional methods [cite: 10, 23].

### 5.2 Game-Based Learning
Game design is the most common application of Scratch in primary schools. Creating games requires students to utilize complex CT concepts like synchronization (e.g., collision detection) and variables (e.g., scorekeeping) [cite: 24, 25].
*   **Motivation:** Studies consistently find that the desire to create playable games drives high engagement and persistence in debugging, which are key CT practices [cite: 4, 24].
*   **Pedagogy:** "Games-based construction" is distinct from playing games; it positions the student as the designer, fostering "constructionist" learning [cite: 24].

### 5.3 Gender Differences in CT
Research into gender differences in Scratch yields mixed results.
*   **Performance:** Several studies using Dr. Scratch or standardized tests found no significant difference in CT skills between boys and girls in primary school [cite: 26, 27].
*   **Project Preferences:** Differences often emerge in the *types* of projects created. Boys are more likely to create games and use motion/sensing blocks, while girls often prefer storytelling and art projects, utilizing looks and sound blocks [cite: 28, 29].
*   **Implications:** This suggests that gender gaps in STEM may not stem from aptitude differences at this age, but rather from how coding activities are framed (e.g., gaming vs. storytelling) [cite: 30, 31].

### 5.4 Artificial Intelligence Extensions
The most recent frontier in Scratch research is the integration of AI. Extensions like "Cognimates" or "Machine Learning for Kids" allow Scratch projects to utilize image recognition, text-to-speech, and predictive models [cite: 32, 33].
*   **Application:** Students can train simple models (e.g., distinguishing between happy and sad faces) and use them to control Scratch sprites. This demystifies AI, moving it from a "black box" to a tool students can manipulate [cite: 34, 35].
*   **Findings:** Early research suggests these extensions effectively introduce concepts of supervised learning and data bias to primary students [cite: 36, 37].

## 6. Challenges and Open Problems

### 6.1 Assessment Validity and Reliability
While tools like Dr. Scratch are useful, they have limitations. A high score on Dr. Scratch does not necessarily prove a student understands the code; they might have remixed a complex project without comprehending it [cite: 1, 17]. Furthermore, static analysis cannot measure "Computational Practices" like debugging or "Perspectives" like collaboration [cite: 14, 38]. There is a risk of "gaming the system," where students add unnecessary complex blocks just to increase their score [cite: 39].

### 6.2 Teacher Professional Development (PD)
A critical bottleneck is the lack of prepared teachers. Many primary teachers lack a background in computer science and struggle to assess student work or debug complex projects [cite: 40, 41].
*   **The Gap:** Research shows that while teachers recognize the benefits of CT, they struggle to balance it with existing curriculum demands. PD programs often focus on tool mechanics (how to use Scratch) rather than pedagogical strategies (how to teach CT) [cite: 41, 42].
*   **TPACK:** Effective PD requires developing Technological Pedagogical Content Knowledge (TPACK), specifically understanding how coding intersects with subject matter like math or language arts [cite: 42, 43].

### 6.3 Transfer of Skills
The "transfer" hypothesis—that learning to code in Scratch improves general problem-solving skills in other domains—remains debated. While some studies show positive transfer to mathematics [cite: 44, 45], others find no significant improvement in general problem-solving or algorithmic thinking outside the programming context [cite: 13, 46]. There is a concern that students may learn to use the tool (Scratch) without internalizing the underlying logic in a way that is transferable to text-based languages or real-world logic problems [cite: 46].

## 7. Future Research Directions

### 7.1 Longitudinal Studies
Most existing studies are short-term interventions (e.g., 8-week workshops). There is a critical need for longitudinal studies that track students over several years to see if early exposure to Scratch leads to sustained interest in STEM or long-term retention of CT concepts [cite: 13, 47].

### 7.2 AI-Scaffolded Learning
With the rise of Generative AI, future research should explore how AI "copilots" within Scratch can support learning. Tools like the "Cognimates Scratch Copilot" are being developed to offer real-time debugging assistance and ideation prompts [cite: 32]. Research is needed to determine if these tools scaffold learning or create dependency.

### 7.3 Beyond Code Analysis
Assessment research must move beyond static code analysis. Future work should focus on **multimodal learning analytics**, combining log data with eye-tracking, screen recording, and classroom audio to understand the collaborative and cognitive processes of coding [cite: 15, 18].

### 7.4 Inclusive Pedagogy
More research is required on how to design Scratch interventions that are inclusive of students with disabilities and those from low socioeconomic backgrounds. Initial studies suggest that while Scratch is accessible, students with disabilities may not achieve the same gains as their peers without targeted curriculum adaptations [cite: 46].

## 8. Conclusion

The integration of Scratch in primary schools represents a paradigm shift in education, moving students from consumers of technology to creators. This systematic review highlights that Scratch is a powerful vehicle for fostering Computational Thinking, particularly when framed through the Brennan and Resnick (2012) framework of Concepts, Practices, and Perspectives.

The field has matured from simple feasibility studies to rigorous assessments using automated tools like Dr. Scratch and complex process mining techniques. Evidence suggests that Scratch is particularly effective when integrated into existing subjects like mathematics and when used to create games or stories that resonate with students' personal interests.

However, challenges remain. The assessment of "thinking" rather than just "coding" is an ongoing struggle, and the professional development of teachers lags behind the adoption of the tools. Furthermore, the promise of CT as a universal problem-solving skill requires more robust evidence regarding transferability. As the field evolves, the integration of AI extensions and the use of data-driven learning analytics will likely define the next generation of research in primary school computing education.

## References

[cite: 8] Zhang, L., & Nouri, J. (2019). A systematic review of learning computational thinking through Scratch in K-9. *Computers & Education*. [cite: 8]
[cite: 6] Fagerlund, J., Häkkinen, P., Vesisenaho, M., & Viiri, J. (2020). Computational thinking in programming with Scratch in primary schools: A systematic review. *Computer Applications in Engineering Education*. [cite: 6]
[cite: 1] Stewart, W. H., & Baek, K. (2023). Analyzing Computational Thinking Studies in Scratch Programming: A Review of Elementary Education Literature. *International Journal of Computer Science Education in Schools*. [cite: 1]
[cite: 38] Stewart, W. H., & Baek, K. (2023). Analyzing Computational Thinking Studies in Scratch Programming: A Review of Elementary Education Literature. *International Journal of Computer Science Education in Schools*. [cite: 38, 48]
[cite: 24] Connolly, T. (2013). Using Scratch with Primary School Children: An Evaluation of Games Constructed to Gauge Understanding of Programming Concepts. *International Journal of Game-Based Learning*. [cite: 24]
[cite: 4] Sáez-López, J. M., Román-González, M., & Vázquez-Cano, E. (2016). Visual programming languages integrated across the curriculum in elementary school. *Computers & Education*. [cite: 4, 47]
[cite: 7] Yang, Y., & Bers, M. U. (2019). Studying Computational Thinking in Collaborative Design Activities with Scratch. *Creativity Labs*. [cite: 7]
[cite: 2] Brennan, K., & Resnick, M. (2012). New frameworks for studying and assessing the development of computational thinking. *AERA*. [cite: 2]
[cite: 43] Piedade, J. (2021). A TPACK Guided Scratch Visual Executing Environment for Assessing Computational Thinking. *International Journal of Computer Science Education in Schools*. [cite: 43]
[cite: 14] Moreno-León, J., Robles, G., & Román-González, M. (2015). Dr. Scratch: Automatic Analysis of Scratch Projects to Assess and Foster Computational Thinking. *Revista de Educación a Distancia*. [cite: 14]
[cite: 15] Moreno-León, J., Robles, G., & Román-González, M. (2015). Dr. Scratch: a Web Tool to Automatically Evaluate Scratch Projects. *Revista de Educación a Distancia*. [cite: 15]
[cite: 25] Troiano, G. M., Snodgrass, S., Argüello, J., & Harteveld, C. (2019). Is My Game OK Dr. Scratch? Exploring Programming and Computational Thinking Development via Metrics in Student-Designed Serious Games for STEM. *ResearchGate*. [cite: 25]
[cite: 49] Rich, P. J. (2017). Using Dr. Scratch as a Formative Feedback Tool to Assess Computational Thinking. *BYU ScholarsArchive*. [cite: 49]
[cite: 44] Kong, S. C., & Kwok, W. Y. (2021). From Mathematical Thinking to Computational Thinking: Use Scratch Programming to Teach Concepts of Prime and Composite Numbers. *ICCE*. [cite: 44]
[cite: 50] Rodríguez-Martínez, M., et al. (2022). Computational Thinking in Initial Teacher Training for Primary Education Mathematics. *Mathematics*. [cite: 50, 51]
[cite: 52] Getenet, S. (2023). Computational Thinking in Mathematics Education: A Systematic Review. *Education Sciences*. [cite: 52]
[cite: 21] Fang, X. (2023). Integrating Computational Thinking into Primary Mathematics: A Case Study of Fraction Lessons with Scratch Programming Activities. *ResearchGate*. [cite: 21]
[cite: 53] Nordby, S. K., Mifsud, L., & Bjerke, A. H. (2024). Computational thinking in primary mathematics classroom activities. *Frontiers in Education*. [cite: 53]
[cite: 40] Fagerlund, J., et al. (2020). Computational thinking in programming with Scratch in primary schools: A systematic review. *Computer Applications in Engineering Education*. [cite: 40]
[cite: 42] Espinal, A., et al. (2024). Professional Development in Computational Thinking: A Systematic Literature Review. *ResearchGate*. [cite: 42]
[cite: 26] Paucar-Curasma, R. (2025). Gender Characteristics and Computational Thinking in Scratch. *ResearchGate*. [cite: 26]
[cite: 28] Kim, H. S., & Lee, S. (2023). Investigating the Effect of Binary Gender Preferences on Computational Thinking Skills. *Education Sciences*. [cite: 28, 54]
[cite: 55] Montuori, C., et al. (2022). Gender Differences in Computational Thinking and Executive Functions in Primary School Children. *Frontiers in Psychology*. [cite: 55]
[cite: 30] Ibrohim, M. M. (2025). Gender Differences in Computational Thinking Skills Among Elementary School Students. *ResearchGate*. [cite: 30]
[cite: 1] Stewart, W. H., & Baek, K. (2023). Analyzing Computational Thinking Studies in Scratch Programming. *International Journal of Computer Science Education in Schools*. [cite: 1]
[cite: 45] Ibrohim, M. M., Siregar, E., & Chaeruman, U. A. (2023). Scratch and Computational Thinking in Elementary School: A Meta-analysis. *Al-Ishlah: Jurnal Pendidikan*. [cite: 45]
[cite: 13] Jiang, B., & Li, Z. (2021). Effect of Scratch on computational thinking skills of Chinese primary school students. *Journal of Computers in Education*. [cite: 13]
[cite: 34] Code Week. (n.d.). Craft Magic with AI Hand Gestures. *EU Code Week*. [cite: 34]
[cite: 56] UNESCO. (2022). Artificial Intelligence in Education. *UNESCO*. [cite: 56]
[cite: 32] Druga, S. (2025). Cognimates Scratch Copilot: AI-Powered Support for Creative Coding. *arXiv*. [cite: 32]
[cite: 21] Fang, X. (2023). Integrating Computational Thinking into Primary Mathematics: A Case Study. *ResearchGate*. [cite: 21]
[cite: 1] Stewart, W. H. (2023). Analyzing Computational Thinking Studies in Scratch Programming. *ERIC*. [cite: 1]
[cite: 57] Noda, S. (2025). Impact of computer science education with robotics and math apps on computational thinking: A randomized controlled trial in primary schools in Iraq. *PLOS ONE*. [cite: 57]
[cite: 12] Noda, S. (2025). Impact of computer science education with robotics and math apps on computational thinking. *PMC*. [cite: 12]
[cite: 46] Yang, Y., & Bers, M. U. (2023). Coding as Another Language: A Randomized Controlled Trial. *Computer Science Education*. [cite: 46, 58]
[cite: 47] Kjällander, S., et al. (2021). Learning and Assessing Programming in Primary Education. *Education Sciences*. [cite: 47]
[cite: 3] Resnick, M., et al. (2003). Scratch: A Sneak Preview. *MIT Media Lab*. [cite: 3]
[cite: 24] Connolly, T. (2013). Using Scratch with Primary School Children. *International Journal of Game-Based Learning*. [cite: 24]
[cite: 5] Berry, M. (2020). Some Scratch Research. *MilesBerry.net*. [cite: 5]
[cite: 11] Aivaloglou, E., & Hermans, F. (2016). How kids code and how we know: An exploratory study on the Scratch repository. *ACM*. [cite: 11]
[cite: 27] Asad, M. M., et al. (2021). Gender Differences in Computational Thinking Skills among Malaysian's Primary School Students. *IEEE*. [cite: 27]
[cite: 29] Simon, A., & Geldreich, K. (2017). Gender Differences in Scratch Programs of Primary School Children. *WiPSCE*. [cite: 29]
[cite: 31] Zhang, Y. (2024). Gender Differences in Computational Thinking Skills: A Systematic Review. *Education Sciences*. [cite: 31]
[cite: 6] Fagerlund, J., et al. (2020). Computational thinking in programming with Scratch in primary schools. *JYX*. [cite: 6]
[cite: 2] Brennan, K., & Resnick, M. (2012). New frameworks for studying and assessing the development of computational thinking. *AERA*. [cite: 2]
[cite: 9] Brennan, K., & Resnick, M. (2012). New frameworks for studying and assessing the development of computational thinking. *MIT Media Lab*. [cite: 9]
[cite: 36] Quiroz, P., & Gutierrez, F. J. (2024). Scratch-NB: A Scratch Extension for Introducing K-12 Learners to Supervised Machine Learning. *Semantic Scholar*. [cite: 36]
[cite: 33] Kim, J., et al. (2021). Extending Scratch with Text-Based Visual Blocks for Big Data and AI Education. *IEEE Access*. [cite: 33]
[cite: 35] Create & Learn. (2025). Best Resources for Learning AI with Scratch. *Create & Learn*. [cite: 35]
[cite: 32] Druga, S. (2025). Cognimates Scratch Copilot. *arXiv*. [cite: 32]
[cite: 37] Al-Zoubi, A. (2025). DeepScratch: Scratch Programming Language Extension for Deep Learning Education. *ResearchGate*. [cite: 37]
[cite: 16] Moreno-León, J., et al. (2017). On the Automatic Assessment of Computational Thinking Skills: A Comparison with Human Experts. *ResearchGate*. [cite: 16]
[cite: 39] Park, Y., & Shin, Y. (2019). A Comparative Study of Scratch and App Inventor for Learning Computational Thinking. *Electronics*. [cite: 39]
[cite: 17] Moreno-León, J., & Robles, G. (2015). Inferring Computational Thinking from Scratch Code. *Jemole.me*. [cite: 17]
[cite: 14] Moreno-León, J., et al. (2015). Dr. Scratch: Automatic Analysis of Scratch Projects. *ResearchGate*. [cite: 14]
[cite: 17] Moreno-León, J. (2015). Inferring Computational Thinking from Scratch Code. *Jemole.me*. [cite: 17]
[cite: 18] Srinivas, M. J., et al. (2018). Assessing Scratch Programmers' Development of Computational Thinking with Transaction-Level Data. *ResearchGate*. [cite: 18]
[cite: 20] Brennan, K. (n.d.). Assessing the development of CT. *ScratchEd*. [cite: 20]
[cite: 41] Cohen, A. (2023). Scratch Teachers' Perceptions of Teaching Computational Thinking. *CRIS*. [cite: 41]
[cite: 59] Oide Technology in Education. (n.d.). Coding and Computational Thinking Using Scratch. *Oide*. [cite: 59]
[cite: 51] Rodríguez-Martínez, M., et al. (2022). Introduction to Computational Thinking with Scratch for Teacher Training. *ResearchGate*. [cite: 51]
[cite: 22] Fang, X. (2023). Integrating computational thinking into primary mathematics. *EdUHK*. [cite: 22]
[cite: 60] Sjöberg, C., et al. (2018). Teaching and learning mathematics in primary school through Scratch. *ResearchGate*. [cite: 60]
[cite: 23] ScratchEd. (n.d.). Scratch Dissertation. *ScratchEd*. [cite: 23]
[cite: 10] Calder, N. (2010). Problem solving in Scratch. *ERIC*. [cite: 10]
[cite: 44] Kong, S. C., & Kwok, W. Y. (2021). From Mathematical Thinking to Computational Thinking. *ICCE*. [cite: 44]
[cite: 61] Çakıroğlu, Ü., & Muştu, E. (2024). Mathematical Thinking behind Coding: Promoting Generalization Skills via Scratch. *ResearchGate*. [cite: 61]
[cite: 18] Srinivas, M. J., et al. (2018). Assessing Scratch Programmers' Development of Computational Thinking. *ResearchGate*. [cite: 18]
[cite: 19] Wang, Y., et al. (2023). ScratchLog: Live Learning Analytics for Scratch. *ResearchGate*. [cite: 19]

**Sources:**
1. [ed.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuwmyZgEVPKlQXHuQ8YNNMY7fQz9fdtAMC3oI9xFSUT7zUJy_1ah0fSrwk64sChFHe8MYBgz5knNlL1g4sghmJGMTnbmdBginDp9xaq7oUbKGy208sk8yv1tfcKHkxtGiGlz3DBMk=)
2. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtbu01Nl4ofeZscOfYoxi2yxd0n8Nyrg7Rkhv1P5llUon68kPMnmreuImOGXEKoIE_tSMyMWlOfI1lkRtIPYvmsbxBiCH8C8RfYXe-D1182tKglH-fsBVdDy5xKi3d6XXJgSwXVoHgIYovgBTq)
3. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfYYyJ5UQ8Xaf2JE8yPmrcfCmoi4X6QkepwpRyC0na8rqAIoLlSuiu_hhJ5EfuSus_vxQkCCsbz2Blr6zy_4HT7OYBr5A4NJXsU8htVUWayFya4SwM2KGb-XEeOi01DQtJgXxlD3jW0lS400S3VF2QygNkx4XdG1yg)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAY2H6frHI-XCduUW1VRR5Xh5k5U-0FitmveBXMsek6q4tUav-kGRfWihvUj_uwOydwCZ_Uq98sMYSMvwZFnBI_YaYqortOUQjz-UqoD_0YPKMEeeEO66LRFQaRw==)
5. [milesberry.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY3hQpJR8CBSvGxwbIjcdWqlLrn4dxyzkGspc9J3irVK3CR6Js44GmsUBqlIHF47xsl2rvwrPvt2OwJfOwfW9Zddi_6jGOIeQY_yp31bpmS_gLv15cAnrR9kavo8nfkdo20__IcXIglQBwSQ==)
6. [jyu.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEebIstPDYsj_5azAk9quiVn3u5RWfkqAvYNg9V9HpeTQYjeHjtfy-3sBvLf8EEt2fiU3D_W2EHEss0kbRapOO8tizSbofWe5sXByaaqtI_I_Bsp1f7OBdTLU3_po15SaYzXkJ48Epy3EjwErAwphiumPWmuYocOqbfT2hx-xFJfr0=)
7. [creativitylabs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXu4QlldiBAI-XlB1zWKKtzXlLq25CdIwk1OsePYLZTc9VY0pNVCbNM5u5Ynvnda4NniEHUkRH7UIK0Lwh0YjYSl1PFKHYr3vx2lDokjF7keGckngFq_68a_fl7LjNJEY8V_gl1fWDABP6FqHA8bydbDChJGG0FeLg-guSLoI=)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP7yjfjuU4IS4W4ADARASCEdhTF7YuQKUuRmCLJcguo1PK2Pv3n_k_dwHmJCCuRYYqdT6eOhnttoIWhVv1gJBZx6U-L55sMBcpkpozdqkG563NYwLkr10OLHhx9hPGg01DkyyvbFATQk0c3KHBmsGX3ETggCkwHcxcV1mFdwfofPr-A8ZdPoYWjg9mp0aiuUP0Hyr_qPd4riIiR3l4_NG0FR9kjcFNPecfGDdX_4tOIhBUW_aS7O4=)
9. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMI_BW5T-cGool92ixlEDhAbP_bRfw3-S2o0gwb418dPSmU8ZPDw2natKLMGmgvR9XMFkqJD6ZAh_ubdL1xv3g8LYLo-anlkwO1v0EieeUFfFwPBeOBDjUQhJn8FKPLRG02NYyJOjC_DsZkFnaoJwleDPv74C6gMNkzclqy-ppLOACVI0r8kHDAHR_hE_mhWMGojaKBuDFBxIYcbUimN-ZUqi5G90AWiLhW3OsF9-q8Bk=)
10. [ed.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB12xoEopJ32qKr8sVLDF3moBb1qHRT9W3wf_ba2BoYcVP7fTCZqNrDGvA9JsogrD_69Sjim8LuFzoD-kLMZ5f_OS80tTljvDWq5nGvZUvBs7_b3ir9NCnN3NPGLB0aI28h9KyJA==)
11. [aivaloglou.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkK3GukG8m7u3VePBT8Bbq-_RRAKMMmJ4BWtTSvqQColiC_ojpqAhKrRLUiGs8JK52_AFwgmqxqyyk526vANLkXP4QBpnoZywEuDFG4DBvbkGxLzALXCftQfAJzB-9It0in191KFIi3yZqc4lSTlRdcFTcdCjOh5TWhw==)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP4TX3mB443ugr80ClcpiZK58uUd0JgEzUIZj7GFGxP8ibTn4P6-dxgMkigHqMzVJyhrYwok8TRmGBNspVkt6XA5LSIlfGjpu5CV96aflkAAnqcUyew9SD3p_1kY4GiSfMyH4I13v91g==)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvD1GXDPkAgWCaPOzqjckddLovRfmn4ZCWY7Ibulo7HOc6QqoyU7CAFGVZprm5qNMXiBRKoy2CSskD_D9hKHvxUz-I-RfoaEQzFIFwW6yuibqM-oPrkAbdoZjGoWs6fKf4DWH-FLmdf40HFoZY4Ze58oul-rS0wRXdbuR0vob6N1FIOIBmY0iz_h8N7Eb6VF0vx69EbAEdwuDhDAf0JDMw_nttztykODosM88KgBSSAGbHwRGVDyUasVCADaIZAg==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ5BIadVTVJ5m6ybIFHV4Cl6qb-p1oYIWgUtKvFOKfvHKJdaSGuiAg4dY0l5D44mFc3PyfRv4ZTvDPkOE1hsg2pyhn8WD3H666dnuAiYP9ik1E-FQxhuc5988q5VBvTOYY9kwLYC47LRLqTuO3Vjx8ud6NbcoUsuMzESP9sP9XhKUmad7jHjWD6feJeoo-FLr3qnBl9IgcpJ6COy2Akf2uwBmaUrTTRPZ-E2grt88AKWhpysBpNbIIyxQPpKI27PFjbsQNOPKQ)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM2MzfvS6WF8MIWUKFhXb_iAC9SIAicJuGvdV8aZ7SPKvnLDu2dPRLYvrK9DI8PPfSzxoW7b6Cl17Ampv7bsUpix2Kviyw19lwKnSqNnIbIMkf9yQTvDE1MRQ4JBbvToYDAntHjGGOo2irDvHfzvGVVp3u1fg5AEZfKo-ybwJ1WfqxbnRvYF30RwwlF1SRJRl16W1Ov-G3LCJxHAQz6hu2_R9La4zd7lxI)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFza7Cmx6yai_-8-coQqzcceETCyWuD0CgstEifmwi5wz2hcwgEtl1H76oBVojO7QGVa3ReYMriyaXGpjGYBFrg5uIRUbkdlxpC89Rcs-SXQsSti5zxXtmHJlqNLy8EV04q_0-ElzcIwtKsiuIKcvWdOvfUXzlqpTG4Y0aRv8hu9IE-czEdIHPU0XPDWzcRFrd6qjgtmVX1Zv9vhQvCkU2N8_khNT2lfokhjY-tz0Bp8l4psjFCbT0LLFai4Cv-vXLqz1Z00Ow=)
17. [jemole.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTPdNH4qy8fGvJKC5B3J4j8UcHKvotXzN8ILLT3FtuM9ijtD7ao-VGCyie7PKlUVtOpTjncfp_KCFF6L6y-z0_jf7bBudPz4Nmbu1IpEByN_oWhTk36gaa41EzkiYEW1DdpBc4BZWrE7zhPg==)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJr6ZttXYMntx_iviD97V4AFXkRoCGuMjMMcgkYl0kMz8bcCsvIaJYheNa48FzJWSAZC8eOBk-IiXYspW3nQqxYlv61eYyPLYhYVdyDCreXDubnkQfXAcBFgLJ-fBVPsVl9Bfk9eEbo7J5Ff6PMLCm5fv_dB8qIPlsMd7xVoJcQBLB4nukBVSEUs6REis08vl_TLfv2WKxeoTM_1cX5YcoXVTOFbHuiM7pQANg6dZOV9_r9MdxWdPNnR1Y3gXuWsQrh18M6bS8T8bo)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyvCmK6RLDjA11F1XeN_7uuctKGtdm3GPyI6D2S3fGjfwYmasos8xeHQZD1E_85sWo5w-H04iviG4bWlNcvQwm0Pi3VtDUWrfKcKyE5K-ffNAhryN-8SdkGeVtiYupjO2pYEBRb16H_iIH_zBzRLQJ5m4YDX1VfVKoUwsGKE62Udr-yL9_N5wROXd8tZNpliEF1KBZMxCm)
20. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBBG50ItI6NCTGdtxldMPJhV4m4hvXhT6wbxyiiyVhhNyWy_acoEBZ3mEpDTMWtKvvayJO0M16xMdMtL8UVeJOCzW9euCceRM_TgbGQh__GascYOyyph6CVEfcm2VaaoucFdiNPmOm8o=)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4epkjEq_syUaV3r5ZMIHd3cbJUA0yJWjiBPx6D8wUyEtr4EFa1MTFYYL-04Hh4tprKd2WXJf7j2DVF-nIVg14eST2pwY51erI9jyNt4fEgmAuB3c-DY_dp1uMt3kdAOmoKEVw0eLSf9sMg09RTfyFOfjedlQWmfIBLVSo_MtHspuOp0YOaNpf47bo09xfOMpMKzARBzM6ybtb8uQB63tQ1EjBF0vSqW4Jm6-TMtbu5NLrY2HMvOduayMzzM5plqag_sy4T9gF_Yz5o2jei5y81pwruk4ptS0zUgLOcfWST8hHYyyN-htmF4=)
22. [eduhk.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfrGTlgV1r2FrKsY3rCioKZVYj7HucxL8qQtR8pq2PBf_VEwiJ7nVNXIp7nkKmpsdk_E6GUEx9FlWklBw0Y0G2olhx9tXzCmtWTeSly5BWMjk9wufiXuSDbaTRqv3xcKyq0Z6i4WEDNBJzSUXSwVoJtZR2pDwWgOCkR5wC5P7NDQiI-kVVqpL6vCDosMhCQ5HsWeAFAgynAp1NufdgcrvB2leb)
23. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHINw3Iq7g1RZZA7-w-RNNhBXg9DDVgv7TpNJ7thcq7k_TRILXpXinULng9e9oykWADy8yg_h6r5cR-rYEe8AG0036qKqo22AvPZA9cq0fG3ycOS4RET6Y6dSGwiqpA48IcYA7D81SzJ8Pl2LAa4E1gI6nm1_r23SzEuwY-DLw41AejCDNJ5g8mUvQSiak=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH86NYcSBjCKC5HRvnBou0lDzlHsEfdLHQiqo-Pt5NlzN1emmDD86j9s3CzBLZOUC5D4Kp0raAVaSBKAoxjRjax7u4zfumn5DWFoUY7EXNRVYhb8C1HtrIFhoewQ2Qipi9ZAZsgw7MYzasy7G5xXuWhVsLkJ6QyA09aA35beG126xlr1DnVESxCPX-a6TTPnkRCp-4=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOKiEoepaIURsoEG7COPBQothtgEQzsCNKTgHyAEO4RVeo2DvUBrHPRbaYMLh1CVro9ZuMnbWXN3qtxpheOKvmtzrtq10mxQasXgBhyadrF7jH9Eu_oUJRRfq_zdP7aaeX_IkHzl9XE2f5KZzCvBVaCitG_I5iiJ87mO50GE-sN-9V6Utr9aWruVc4uBr7wMGF2VNdaI40VoSSOHSu-ZqaJXQ8PQ3r1OwKbhXfWffPJ7LjfMeLNwJ6zVnnRQee7YcvoVGWXbIYAwtgLcr69gfVp28dJr0LaA_cCh_eQvucwPenRB3qstx5X68pEhgDjCv2WxoKArY=)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl10cD8O958gsg2Z-OgQFI9tY8k-UgpB9tEeSyM1NHfMoAKmSyKnDG6eWMdIOwR22hMxTXlaPUKp2t6wHDwpHbTwi5b0ZgLTxRaufq_nUipnemUH0xNyoO5iMy9vr9gMNNAcDEMO7Rnmg1YpMjjWL3Q9CK1moGRmmYbCNiivBYhl-9zg0I-QuRoUz4R9D-fxSW3Is-7PzKFwQ-hX_mA_HV6QtPObI=)
27. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj1nEz_HV7ffulhlZSEzG1OQ0l0kKndUgxSAmtrBulbu2G9dgGAoCUKMxgPlIH84DLrD3iDlGgWt2MIRVgvxwrjmn1zTEhFsRTVwIeT43MAVmroiJ7zTDxInFNbWYHRbxLxHk=)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGobyBEGxSFYT1dJofdmUY1nBrLKEiUaMIUXv9lJUrRejqhr6nngEGo6gbkQFUTdF6yeEDi-dnGztCnr9xmgWRG3SkHZta2eBTVVk2iOs08Ff9_gOgf3SWhBmiz5aQ=)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFH2J47RCJGwWYjsuOYCwD6WmKG2FKFefS7GZEUzv_w8TmRSEq-KWALpyeszFF1PhX6UQRVedxw2lY0ZKpjXUTG_Lxuht_3t1bbiUojyzn-Go1gkZL7tSookI1sYci_Pfc2kzAWy5b8n1Lf1ne4CMavVrGQewexgdX1q5WvDG38AzIIJBBbjqlVGwt4r0mvrt7l4nPFZ5LzjXhmR-q-KrcQwV16lnINLiYC-A==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyXEQM-gWzzSfy-53eeJKdP1EUh5RDJpxUPcrjdLPWyXlnA_N1jlw_tu_FJGx7aCoFeWrJOm8u9Aqc44aJrbDPTDfpiyrH52g5cGUVk9A2ytcfkLC380gtHXGS1HXwnfrXpO6ABZGXgfnp9THXF7qbFYMtdWPL1n2ZVqOu1LpRWSU0ZgQd_hnS1K9uVv54AVPVdNmGlcrmiOHnZHrtjkXoC9YRrRILUzWkp2JbdZ6Xgt6CEAJ-wWEsB__If4Zb)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6K_gY_cIuQY1M2IZmrLiT_iVYDVp2ojkH_B_gSEa9OGHlIEtL450mX3qPrdjn7f8A6Pm4DhnG9biSpgDice9icRAxGW_Olq7NlB0_XLJmy-zXhl5xThQt-ydPSyA=)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPI0xt6p0HVE_aOxdSOVuOdpslbr6UrQJaSVOIuM5_x5sIWd8ze0vou5Tujx5_a5SGSEXrY3pLv2ZD9I9eqttxHq--rIdiaVjHPxWlkSi8nuoKsayhwCeQ2g==)
33. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwR6UodC2A5ZGu-uxb0vG_GZv4BLIf4PdGsrqulgGRjN38nOhUHC2Mrz-fVEBo5vDtoEWMRVm64P6SDuj3adlf0P-uKnWXP8drHa0nE9IjWZPnXtnZ7XVIseU2AWX5zQhOXHTZWmWYbPKeqRBAzte_FeNy)
34. [codeweek.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4kKJ8wcbDnBVZ2Xt8EsnDym_2p4DIG8MFDr1hsRGZ1S2DlU10Y1NAMhUMJcjDJ-b8N-qWTqVO3dSxbmQQRzgFYZmX5qJwYFYJlHqufvujxCB3OxHfjsLUp048o0a19Q0=)
35. [create-learn.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzPo9l1zOc6PbZKslVWhCzMbzuLLF5e3UEiqvyOmSFzrlmJ-WxCur69aJXGaZWJiKx0yid7kGMnpjwtE_9ToAlVXlY_jXObgfe5LLXyzFg5JAI2v5_RdMhIRRhkkp7hWeEJ3g2CP4lCYLCDfO5mLFqCj0GUsDpMqACeQhioPc9TA5dBceDbm8XoEeNPoASVmf6IQlxy0x3_9xvcUDPoO_33w==)
36. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUKg98Fso_p3yK3WrZkIiGupM2XeZcVQl5OlPyUS8yhbTBfnF_cH4oEZe_GpZBiczUGUQCfj49Uvg6hG1aUBdqzlbWyC8N85QYl8u0xsVw4EgeferzEncdZMtEyD59I7szVXRJiUUfb3J24iq2fre3th4mLynIYZxXgRrvOJBOHg61NZE=)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH80sl1JM4l7UfMCrYIan4iiKLsZeCZIr1k_snsYq-yv7hVb7tY4uVSaErhcwMfiDpfuLvvHYhtnk1rWPvLyhd0Bkmvitd1y7xrDOVAgN0a-h3S0ukxnGvFWMmYkpL3-2-PIC8bpUd-RakpO4TM5CxedeoBjAxRnRzcRZPvnw2A05FNF72Y-TRlSGoykZn5h4fUOCoemmOgCvSmgCaTYDhU7XGwrEl6INaty7kJhDY1dXl2NWckVqzI)
38. [ijcses.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6zabGZssL-T7C51FJvEnd2D9dA1miRcmWgBj-QIfeeqio010ma_xSGSXQM9ADyKMqabrEbz48-kiGFT5JllOBHue84atMqFongxlUCL8cpRZX9U4e8X9WEAEExqilFesNEEgbTWri9KJBKBIA4A==)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjudcog8oLjE_hMpIuhw-ozbT5jbPsQXsf23FjsW6kRbgACWdFNdkkGivKsTeLk-ei8chVGLacS3HzLuLjsuVwEsfWq5oxHNuL2lEwaqzIe4_7OW-X9hYLLwKtF5D-)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNROkmX2Y_mZukVT2dQqD3kbCyquXRNz46L-fg-0tce3tA1kRh6YNSkcyeRP89UwjPT4LKMAK-Jso_I8p1cEZWdXhU0XKCUF1dIo5iumtQf-fFHmD6F_LFXe9pulAlp3TMSDh0a1clReuThaeQzO4UPSdP0IVOPvBA1u4E30y3TaNznxVjdTsReSK4D7p64E2kivqn1bE47mXYjq8fnFHolAWt8T8hXFGNklD09dLLzaur-ReGCpwcY_de3UFmFFBlOVg=)
41. [iucc.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBHq96qFa4yQk4bj322wb2QOUg2vgc1L_ol9Hrs63Qi0bXXDqhH9NtI9TzIOvEbmMgLWQXTms5fY3If6X430eYnTYyQufJu3wISYyLH78gO5oVB7vyGEw2HdVKQNdMIenLFxTR41NuT7yanebDQQaDGx8CVrvsk5s0ESYL-wX_pUTCWXDE-7vPAOUkPVGEkYtZawP6IOEpUdAax-e3igI=)
42. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYCZlSyteBSHOUA64joY8r1H7zU6lpju-b5Rmm5Z762LjAgxVe6ieSlqHNC6A8qveHc0F13bxon0MrFyzedqypBcYOrTHshhcz80F-DHwC-apQR-G6bjltsIW8f2gCw293ikQxAwiQxYbB3-lc7htnsoiHrqKxslBejkkKsUxFRIgHg6MI3JlUB_WnG4Ol1rioJh7GCEBRDr1ReA9wxreOiZRDJcG7ZhYOktpEKzUU3RjE4gqU51lWqKYp)
43. [ed.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyevuu5mWjFotbgos_M2pViWDYb7I3mctmHJz9aEM6eVowG1TwQYaECAwBbBrTy9BcHhWjJPOjoaahpPQUjLIUDphKR3WZP7i_7Y13S6geIQQa51urk0B1b_YkAkA2nNtziq1pQv4=)
44. [apsce.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFObvWAEG5mQ3Z1SvOAznjQE6m_ivHeX-nXRb0aEqbepEhiR4wUVpyye4KSZOYLoOp9aWRK-EiCVe0_3oZ2PVwnOUcKuvHncbVxE3NyhwNwEuIsPgFEVcc1FZC6YFXSC-b1e3FFGoYTXo-cBjyWw9pS)
45. [staihubbulwathan.id](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwsF7bOkzyXr1Iji0l--cQAsSWiCECGfxlCoitmGzRlohpC6nIYNbYbF14v29wVG2i2p2YXArM9WkN1VvVUaTxrxH3g-zxcxgLm41KETUUbQSZqbcoUwsAt1z6Vdd4esZqy_12-XtQlakwkJTGzI08FjTyTtLa4ArzMy-gps=)
46. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC3n9UbcwXy3JafZ1Ysskw1nnktHLopfY5bg_uptbJQkxzBOipEA4I0RKfVoyJV4WrJgo9ST_kKWXKQfHOT2GwQIsn4jwVcwPJg1_d86QvnC5W_7ZVd3DP0EVUwigoQX6ki_F73iTgqKsB50pMRhmE2u0NF4vMIg==)
47. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNKvhDM0ithH3FxyVYoJ6FEi7FX00LF2BTFriSOEgy6AublnHUY7Iap0Er_XN5D2w0uA3DGyZayJJuvrNbjprixvRgtNZNW3V930saR2SyzA5RqpOLiC7072ZRog==)
48. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR1H235Qsz8Yrur7kHtFu_Qsd9HOdZeZLAPVMtkPOcucgPTHtNpx7UjJK7PUR5MS3XVSygM9Tx_LX_HldslpuGAAJdCJ6t7Re5ni1jNMr6uVfHQ72Q0YksZDIp63iNeTIlrM1spT4MQtWZqRguhMjBIv51jjMm_6kP4AmM5xYQuDUXbBN-jmG5Ucwy4V7DJ1c2bQrw0zEZ5SCy_69duiNqTCojfK2iFckno22e9AzmmIIhOWYpvqoSwQ4bmsWoJypG4xrrGWAuV--Hp9OAYJNISf9ComM=)
49. [byu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHopOKdqIsShyEjjcOuuRSNhuLh0bvpme1ezx91KbA97yxqxoxt3DDmaF45FVbWzOkUR9VNAcPj5K73CBnrlxnGV-L-AZ1aYhOo8AJkO9RTxMV5itEUnmyuGdd6FfHearWlBtdvgvdr6JtqbqyPULxJU-gAGmBlbELqq5G3QcKbW1q6)
50. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJv4HnzwDnF4eW0HE1xan8AGo7hmns5hm8_h5rc-B3G9Goj6za_-vGR-Ge_FVDV6h0noYMw_NxecLb7xbowpx2Ocbc8v7LRD5Kv3UIE7fLITBd5nrLcwD2u4dyMLUJ)
51. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHD6zdiLdwedQaNSgRhE9G66pIyRuADzffb19SRqVT1usg54JQ5c5mt-HeQXRioviHoppG2nA5eV2D0wtDAW7PTRHW0y-Q9ncJMZhfbJpRk_n3xtRs4spyadSiBr1IIWyIAxQOjAgFZSL55ztNOMTi8fpUydZAtEYppfBqZlI1CTU3VdGOmecLZH_8Ey2RqAvz4aiL22sc6Bbzu5SgMjmDwjTT0zOq7yMI80P5Dc6J2pnlfmZioEjbr8tONJau_goTcQwEjGE6AcLwUt6GJAz3kmC10AkU52syFtz1Bb8aFdEvSuat)
52. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3vinyEwEuWicSYhTdTeNbbwDPqg-mKf9Ow2c3TMLp_pcKaAiuDqq-W0eB3ATbXugp_FTuQ0-AQgIIoi9vm6GaxDrRAywIgfWmx951H3bNTTxhmYnMjbCpvajIKHw=)
53. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyAsMLVgpOi-T3ng7PXjotpChPJxyxKzN9YfQvWab93kBTwf8tP6s5RmeARRE9xhrsCYfxaEifl5iPkLKYzdF6KtexvdX9betUYegFT7Hwzk9fitLw9G_Y1jnJule-dXRFbstQMZJIJat3h6KI1uz6GoX8yjQLPsfw5UCz1ZffAS5ypFRan-9Zm8M1m1w=)
54. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEps90gDFdhAnIYQ9LX4TQl4-AYEbWC3AAsHY-KtRWdpwZvCqar_waUan7NUGv_Y_tYBgulqkDRyXGDYEk_9HfoIfKRWv7zEjfXw1vOlh70UBA9HRc-Zlf-nx6HNj95pqaa0U6E-OkEwB7UmhK2woYi1urAA6rINOwF-Fw6Mt2EFfzr-nJMVSLvDZaEbJFNyxR8_0_ffLd3gqvY80DM9pdQN17ULtlV6EWpQt9T07JKRTrRt2kq8NFBwG-YneV2sso=)
55. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF1srsZFxXWPm6hTFZRi1vDZGySEDhKvT3IyHD0Une_tjp2gLuJoCNNh9MMlRJOCWARDsTBqzt1z05ZVdVTytF4xSsg_c4lT0uRJry_H-G5CWnHJzRkxA5aonm5nB0QurYDw20ukE8-aiNjutxKG-Bw1-z1s5PxMyIIQPFEY9duhc9QY_g4Fz6_ErY8Yc=)
56. [unesco.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBsAGU9KNE9sVUmPmFXvOd_RjKnj-qGp_WkkkxfmGqbIeyQtZew0fx-BhXA_3iJQx3cveYvv8pxVRuAaUth_cH8-sx4AYkrf42_FSSkK1rS2sZ2RQPW4Drpy8swknQK9rMevwWNkYD9Q==)
57. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEb7i-fEe_dF_ZGvkej4WIIyicNn6DYPEp-Cqf8uI7awk3iO2Oz09iosUgCDElT_1HXkhmFfHyzsIc3cOXLTwx9lDiQpXx5pFBbKdqzY3U47r9_79KcyjQ873BSAtMXo1WWdoRlx0Teu6allv5NU3IhvqX-ALBsMl0yypHgz2Y)
58. [bc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLRlmzaLq3elNbcNBnoMpp3H7bfqNcuaF7pH7hciHtkzhW_khJYE0_Z8FIq5eLQN0Wc1n6FCz96OrYgmyX8fAvenui4HdQlIBR9YBh0ElS8kHwd4oo_SUnNPw1lDxEjUvWGHtjr-V8Z523KIBkQ3CSA89u0ACbG4sfJwbzjAN7YWFu9w-_tv_tQlDBng==)
59. [oidetechnologyineducation.ie](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqnlp19Vhb3o4mr_p7-eFVzLbXVDp0JaWq3xRdEpOqpCWwCQ86JzkBPL93glFIwD54zlxUpjXlNIYAOugr8wDgk9PmdB4dJs8fYwPtFuvKoIEgPTn003BiSRYApRP37YJiLX8fN06_YSeFdYMv-2tVziLThxTmLA5WFGRSlwjnonlVsMkpDCyctUQlIkr8yHAJRj0PkltQ1UnbjkSy)
60. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8CjlLl2pDIZ-ZaaEdNQNKOYy2BfAEG3zBPf3MBdhrWRsL9J0zpfG4Y-ll6uBZuxz81fBw_2cFwRL51Udq_ACW7iKAtbrl0fYXqsi8Pa692uBxwFXrBrr9weaMffOpfrzShweVLD3jmyiHPoPsXeMbah48lSm8_ehrVW-9ZSkR5rIzVAR72aaDV72etkLnS8R8FlPQSKZBh8yQeKj5FO_mgwXOQZuyQ3u2EXlC)
61. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOxH7bAS4AnDZXtE919hqTi0cohRU18M2jG7YaFPU48VhjyZ2ZaxZjVvbVwuBGZ23-xuXs8EoXjAiClUYytkPHev_ghPPZXla74cNlGDmlgR_EqtBOWpizAiXE7lPEpC_qpaCBm8idveXR9mgPI4-7Z0CZjmriLmDVJUIyzMJz9rneSZcTALe0kUacXBc7XHpIGnbRW1EfLcTWpP5ZZ_JImJ5e2sv5bhIEBIPOLW4fiI-ut6GHXlV6oQ==)
