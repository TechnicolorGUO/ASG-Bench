import argparse
import json
import time
from tqdm import tqdm
from utils import getClient, generateResponse, robust_json_parse
from prompts import EXPAND_CATEGORY_TO_TOPICS

COARSE_CATEGORIES = [
    "Computer Science",
    "Economics",
    "Electrical Engineering and Systems Science",
    "Mathematics",
    "Physics",
    "Quantitative Biology",
    "Quantitative Finance",
    "Statistics"
]

FINE_CATEGORIES = [
    # Computer Science
    "Artificial Intelligence (cs.AI)",
    "Hardware Architecture (cs.AR)",
    "Computational Complexity (cs.CC)",
    "Computational Engineering, Finance, and Science (cs.CE)",
    "Computational Geometry (cs.CG)",
    "Computation and Language (cs.CL)",
    "Cryptography and Security (cs.CR)",
    "Computer Vision and Pattern Recognition (cs.CV)",
    "Computers and Society (cs.CY)",
    "Databases (cs.DB)",
    "Distributed, Parallel, and Cluster Computing (cs.DC)",
    "Digital Libraries (cs.DL)",
    "Discrete Mathematics (cs.DM)",
    "Data Structures and Algorithms (cs.DS)",
    "Emerging Technologies (cs.ET)",
    "Formal Languages and Automata Theory (cs.FL)",
    "General Literature (cs.GL)",
    "Graphics (cs.GR)",
    "Computer Science and Game Theory (cs.GT)",
    "Human-Computer Interaction (cs.HC)",
    "Information Retrieval (cs.IR)",
    "Information Theory (cs.IT)",
    "Machine Learning (cs.LG)",
    "Logic in Computer Science (cs.LO)",
    "Multiagent Systems (cs.MA)",
    "Multimedia (cs.MM)",
    "Mathematical Software (cs.MS)",
    "Numerical Analysis (cs.NA)",
    "Neural and Evolutionary Computing (cs.NE)",
    "Networking and Internet Architecture (cs.NI)",
    "Other Computer Science (cs.OH)",
    "Operating Systems (cs.OS)",
    "Performance (cs.PF)",
    "Programming Languages (cs.PL)",
    "Robotics (cs.RO)",
    "Symbolic Computation (cs.SC)",
    "Sound (cs.SD)",
    "Software Engineering (cs.SE)",
    "Social and Information Networks (cs.SI)",
    "Systems and Control (cs.SY)",

    # Economics
    "Econometrics (econ.EM)",
    "General Economics (econ.GN)",
    "Theoretical Economics (econ.TH)",

    # Electrical Engineering and Systems Science
    "Audio and Speech Processing (eess.AS)",
    "Image and Video Processing (eess.IV)",
    "Signal Processing (eess.SP)",
    "Systems and Control (eess.SY)",

    # Mathematics
    "Commutative Algebra (math.AC)",
    "Algebraic Geometry (math.AG)",
    "Analysis of PDEs (math.AP)",
    "Algebraic Topology (math.AT)",
    "Classical Analysis and ODEs (math.CA)",
    "Combinatorics (math.CO)",
    "Category Theory (math.CT)",
    "Complex Variables (math.CV)",
    "Differential Geometry (math.DG)",
    "Dynamical Systems (math.DS)",
    "Functional Analysis (math.FA)",
    "General Mathematics (math.GM)",
    "General Topology (math.GN)",
    "Group Theory (math.GR)",
    "Geometric Topology (math.GT)",
    "History and Overview (math.HO)",
    "Information Theory (math.IT)",
    "K-Theory and Homology (math.KT)",
    "Logic (math.LO)",
    "Metric Geometry (math.MG)",
    "Mathematical Physics (math.MP)",
    "Numerical Analysis (math.NA)",
    "Number Theory (math.NT)",
    "Operator Algebras (math.OA)",
    "Optimization and Control (math.OC)",
    "Probability (math.PR)",
    "Quantum Algebra (math.QA)",
    "Rings and Algebras (math.RA)",
    "Representation Theory (math.RT)",
    "Symplectic Geometry (math.SG)",
    "Spectral Theory (math.SP)",
    "Statistics Theory (math.ST)",

    # Physics
    "Cosmology and Nongalactic Astrophysics (astro-ph.CO)",
    "Earth and Planetary Astrophysics (astro-ph.EP)",
    "Astrophysics of Galaxies (astro-ph.GA)",
    "High Energy Astrophysical Phenomena (astro-ph.HE)",
    "Instrumentation and Methods for Astrophysics (astro-ph.IM)",
    "Solar and Stellar Astrophysics (astro-ph.SR)",

    "Disordered Systems and Neural Networks (cond-mat.dis-nn)",
    "Mesoscale and Nanoscale Physics (cond-mat.mes-hall)",
    "Materials Science (cond-mat.mtrl-sci)",
    "Other Condensed Matter (cond-mat.other)",
    "Quantum Gases (cond-mat.quant-gas)",
    "Soft Condensed Matter (cond-mat.soft)",
    "Statistical Mechanics (cond-mat.stat-mech)",
    "Strongly Correlated Electrons (cond-mat.str-el)",
    "Superconductivity (cond-mat.supr-con)",

    "General Relativity and Quantum Cosmology (gr-qc)",

    "High Energy Physics - Experiment (hep-ex)",
    "High Energy Physics - Lattice (hep-lat)",
    "High Energy Physics - Phenomenology (hep-ph)",
    "High Energy Physics - Theory (hep-th)",

    "Mathematical Physics (math-ph)",

    "Adaptation and Self-Organizing Systems (nlin.AO)",
    "Chaotic Dynamics (nlin.CD)",
    "Cellular Automata and Lattice Gases (nlin.CG)",
    "Pattern Formation and Solitons (nlin.PS)",
    "Exactly Solvable and Integrable Systems (nlin.SI)",

    "Nuclear Experiment (nucl-ex)",
    "Nuclear Theory (nucl-th)",

    "Accelerator Physics (physics.acc-ph)",
    "Atmospheric and Oceanic Physics (physics.ao-ph)",
    "Applied Physics (physics.app-ph)",
    "Atomic and Molecular Clusters (physics.atm-clus)",
    "Atomic Physics (physics.atom-ph)",
    "Biological Physics (physics.bio-ph)",
    "Chemical Physics (physics.chem-ph)",
    "Classical Physics (physics.class-ph)",
    "Computational Physics (physics.comp-ph)",
    "Data Analysis, Statistics and Probability (physics.data-an)",
    "Physics Education (physics.ed-ph)",
    "Fluid Dynamics (physics.flu-dyn)",
    "General Physics (physics.gen-ph)",
    "Geophysics (physics.geo-ph)",
    "History and Philosophy of Physics (physics.hist-ph)",
    "Instrumentation and Detectors (physics.ins-det)",
    "Medical Physics (physics.med-ph)",
    "Optics (physics.optics)",
    "Plasma Physics (physics.plasm-ph)",
    "Popular Physics (physics.pop-ph)",
    "Physics and Society (physics.soc-ph)",
    "Space Physics (physics.space-ph)",

    "Quantum Physics (quant-ph)",

    # Quantitative Biology
    "Biomolecules (q-bio.BM)",
    "Cell Behavior (q-bio.CB)",
    "Genomics (q-bio.GN)",
    "Molecular Networks (q-bio.MN)",
    "Neurons and Cognition (q-bio.NC)",
    "Other Quantitative Biology (q-bio.OT)",
    "Populations and Evolution (q-bio.PE)",
    "Quantitative Methods (q-bio.QM)",
    "Subcellular Processes (q-bio.SC)",
    "Tissues and Organs (q-bio.TO)",

    # Quantitative Finance
    "Computational Finance (q-fin.CP)",
    "Economics (q-fin.EC)",
    "General Finance (q-fin.GN)",
    "Mathematical Finance (q-fin.MF)",
    "Portfolio Management (q-fin.PM)",
    "Pricing of Securities (q-fin.PR)",
    "Risk Management (q-fin.RM)",
    "Statistical Finance (q-fin.ST)",
    "Trading and Market Microstructure (q-fin.TR)",

    # Statistics
    "Applications (stat.AP)",
    "Computation (stat.CO)",
    "Methodology (stat.ME)",
    "Machine Learning (stat.ML)",
    "Other Statistics (stat.OT)",
    "Statistics Theory (stat.TH)",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--granularity', choices=['coarse', 'fine'], default='coarse',
                        help='Choose category granularity: "coarse" for broad fields, "fine" for arXiv subfields.')
    parser.add_argument('--num-per-cat', type=int, default=5, help='Number of topics for each category.')
    parser.add_argument('--output', type=str, default='topics.json', help='Output JSON file.')
    args = parser.parse_args()

    categories = COARSE_CATEGORIES if args.granularity == 'coarse' else FINE_CATEGORIES

    client = getClient()
    all_topics = {}

    for cat in tqdm(categories, desc="Generating topics"):
        prompt = EXPAND_CATEGORY_TO_TOPICS.format(category=cat, num_topics=args.num_per_cat)
        for attempt in range(3):
            try:
                raw_response = generateResponse(client, prompt, max_tokens=1024, temerature=0.3)
                topics = robust_json_parse(raw_response)
                break
            except Exception as e:
                print(f"\nError for '{cat}' (attempt {attempt+1}): {e}")
                if attempt == 2:
                    print(f"Failed to process category: {cat}, skipping.")
                    topics = {}
                else:
                    time.sleep(1)
        all_topics[cat] = topics

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(all_topics, f, indent=2, ensure_ascii=False)

    print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()