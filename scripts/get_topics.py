import argparse
import json
import os
import time
import requests
from tqdm import tqdm
from utils import download_arxiv_pdf, getClient, generateResponse, robust_json_parse
from prompts import CATEGORIZE_SURVEY_TITLES, EXPAND_CATEGORY_TO_TOPICS
import arxiv

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

category_map = {
        "cs": [
            "cs.AI", "cs.CL", "cs.CC", "cs.CE", "cs.CG", "cs.GT", "cs.CV", "cs.CY",
            "cs.CR", "cs.DS", "cs.DB", "cs.DL", "cs.DM", "cs.DC", "cs.ET", "cs.FL",
            "cs.GL", "cs.GR", "cs.HC", "cs.IR", "cs.IT", "cs.LO", "cs.LG", "cs.MA",
            "cs.MM", "cs.NI", "cs.NE", "cs.NA", "cs.OS", "cs.OH", "cs.PF", "cs.PL",
            "cs.RO", "cs.SI", "cs.SE", "cs.SD", "cs.SC"
        ],
        "stat": [
            "stat.AP", "stat.CO", "stat.ML", "stat.ME", "stat.OT", "stat.TH"
        ],
        "physics": [
            "astro-ph.GA", "astro-ph.CO", "astro-ph.EP", "astro-ph.HE", "astro-ph.IM", "astro-ph.SR",
            "cond-mat.dis-nn", "cond-mat.mtrl-sci", "cond-mat.mes-hall", "cond-mat.other",
            "cond-mat.quant-gas", "cond-mat.soft", "cond-mat.stat-mech", "cond-mat.str-el",
            "cond-mat.supr-con", "gr-qc", "hep-ex", "hep-lat", "hep-ph", "hep-th", "math-ph",
            "nlin.AO", "nlin.CG", "nlin.CD", "nlin.SI", "nlin.PS", "nucl-ex", "nucl-th",
            "physics.acc-ph", "physics.app-ph", "physics.ao-ph", "physics.atom-ph", "physics.bio-ph",
            "physics.chem-ph", "physics.class-ph", "physics.comp-ph", "physics.data-an",
            "physics.flu-dyn", "physics.gen-ph", "physics.geo-ph", "physics.hist-ph",
            "physics.ins-det", "physics.med-ph", "physics.optics", "physics.ed-ph",
            "physics.soc-ph", "physics.plasm-ph", "physics.pop-ph", "physics.space-ph",
            "quant-ph"
        ],
        "math": [
            "math.AG", "math.AT", "math.AP", "math.CT", "math.CA", "math.CO", "math.AC",
            "math.CV", "math.DG", "math.DS", "math.FA", "math.GM", "math.GN", "math.GT",
            "math.GR", "math.HO", "math.IT", "math.KT", "math.LO", "math.MP", "math.MG",
            "math.NT", "math.NA", "math.OA", "math.OC", "math.PR", "math.QA", "math.RT",
            "math.RA", "math.SP", "math.ST", "math.SG"
        ],
        "q-bio": [
            "q-bio.BM", "q-bio.CB", "q-bio.GN", "q-bio.MN", "q-bio.NC", "q-bio.OT",
            "q-bio.PE", "q-bio.QM", "q-bio.SC", "q-bio.TO"
        ],
        "q-fin": [
            "q-fin.CP", "q-fin.EC", "q-fin.GN", "q-fin.MF", "q-fin.PM", "q-fin.PR",
            "q-fin.RM", "q-fin.ST", "q-fin.TR"
        ],
        "eess": [
            "eess.AS", "eess.IV", "eess.SP", "eess.SY"
        ],
        "econ": [
            "econ.EM", "econ.GN", "econ.TH"
        ]
    }

def get_top_survey_papers(cats, num=10):
    """
    支持传入单个cat字符串，或cat列表(List[str])
    """
    import arxiv
    if isinstance(cats, str):
        cats = [cats]
    # 构建联合查询
    cat_query = " OR ".join([f"cat:{c}" for c in cats])
    query = f"({cat_query}) AND (ti:survey OR ti:review)"
    search = arxiv.Search(
        query=query,
        max_results=num,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    papers = []
    for result in search.results():
        arxiv_id = result.entry_id.split('/')[-1].split('v')[0]
        papers.append({
            "title": result.title.strip(),
            "arxiv_id": arxiv_id
        })
    return papers

def get_s2_metadata(arxiv_id):
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=citationCount,venue"
    for _ in range(3):
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 404:
                return None
            else:
                time.sleep(1)
        except Exception as e:
            time.sleep(1)
    return None

def get_top_survey_papers_s2(cats, num=10, min_citations=30, must_have_venue=False):
    """
    支持传入单个cat字符串，或cat列表(List[str])
    只返回title和arxiv_id，内部用S2做引用量和venue筛选
    """
    import arxiv
    if isinstance(cats, str):
        cats = [cats]
    cat_query = " OR ".join([f"cat:{c}" for c in cats])
    query = f"({cat_query}) AND (ti:survey OR ti:review)"
    search = arxiv.Search(
        query=query,
        max_results=num*4,  # 多抓一点以便筛选
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    papers = []
    for result in search.results():
        arxiv_id = result.entry_id.split('/')[-1].split('v')[0]
        s2 = get_s2_metadata(arxiv_id)
        if not s2:
            continue
        if s2.get("citationCount", 0) < min_citations:
            continue
        if must_have_venue and not s2.get("venue"):
            continue
        papers.append({
            "title": result.title.strip(),
            "arxiv_id": arxiv_id
        })
        if len(papers) >= num:
            break
        time.sleep(0.4)  # 避免 API 被限流
    return papers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--granularity', choices=['coarse', 'fine'], default='coarse')
    parser.add_argument('--num-per-cat', type=int, default=5)
    parser.add_argument('--numofsurvey', type=int, default=50)
    parser.add_argument('--output', type=str, default='topics.json')
    parser.add_argument('--with-survey', action='store_true', help='Whether to fetch and cluster related survey papers.')
    args = parser.parse_args()

    categories = COARSE_CATEGORIES if args.granularity == 'coarse' else FINE_CATEGORIES

    client = getClient()
    all_topics = {}

    if not args.with_survey:
        # 原有逻辑
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
        return

    # =========== 新增 with-survey 逻辑 ==============
    if args.granularity == 'coarse':
        # 遍历 category_map 的 key，每个 key 下所有 cat 一起检索
        coarse_surveys_map = {}
        for key in tqdm(category_map, desc="Processing coarse categories"):
            cats = category_map[key]
            print(f"Fetching surveys for categories: {cats}")
            all_surveys = get_top_survey_papers(cats, args.numofsurvey)
            # 去重
            seen_ids = set()
            unique_surveys = []
            for paper in all_surveys:
                if paper['arxiv_id'] not in seen_ids:
                    unique_surveys.append(paper)
                    seen_ids.add(paper['arxiv_id'])

            coarse_surveys_map[key] = unique_surveys

            # 聚类
            survey_str = json.dumps(unique_surveys, ensure_ascii=False, indent=2)
            prompt = CATEGORIZE_SURVEY_TITLES.format(
                survey_titles=survey_str,
                num_clusters=args.num_per_cat
            )
            for attempt in range(3):
                try:
                    raw_response = generateResponse(client, prompt, max_tokens=2048, temerature=0.3)
                    clusters = robust_json_parse(raw_response)
                    break
                except Exception as e:
                    print(f"\nError for clustering '{key}' (attempt {attempt+1}): {e}")
                    if attempt == 2:
                        print(f"Failed to cluster category: {key}, skipping.")
                        clusters = {}
                    else:
                        time.sleep(1)
            # 保存聚类结果
            out_dir = os.path.join("outputs", "dataset", key)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "clusters.json"), 'w', encoding='utf-8') as f:
                json.dump(clusters, f, indent=2, ensure_ascii=False)
            # 下载PDF
            for topic, papers in clusters.items():
                topic_dir = os.path.join(out_dir, topic.replace('/', '_'))
                pdf_dir = os.path.join(topic_dir, "pdfs")
                os.makedirs(pdf_dir, exist_ok=True)
                for paper in papers:
                    try:
                        download_arxiv_pdf(paper['arxiv_id'], pdf_dir)
                    except Exception as e:
                        print(f"Failed to download {paper['arxiv_id']}: {e}")
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/coarse_topics_with_surveys.json", "w", encoding="utf-8") as f:
            json.dump(coarse_surveys_map, f, indent=2, ensure_ascii=False)
        print("Saved outputs/coarse_topics_with_surveys.json")

    elif args.granularity == 'fine':
        fine_surveys_map = {}
        # 遍历 category_map 的 key，每个 key 下每个 cat 单独处理
        for key in tqdm(category_map, desc="Processing fine categories"):
            for cat in category_map[key]:
                all_surveys = get_top_survey_papers(cat, args.numofsurvey)
                # 聚类
                survey_str = json.dumps(all_surveys, ensure_ascii=False, indent=2)
                prompt = CATEGORIZE_SURVEY_TITLES.format(
                    survey_titles=survey_str,
                    num_clusters=args.num_per_cat
                )
                for attempt in range(3):
                    try:
                        raw_response = generateResponse(client, prompt, max_tokens=2048, temerature=0.3)
                        clusters = robust_json_parse(raw_response)
                        break
                    except Exception as e:
                        print(f"\nError for clustering '{cat}' (attempt {attempt+1}): {e}")
                        if attempt == 2:
                            print(f"Failed to cluster category: {cat}, skipping.")
                            clusters = {}
                        else:
                            time.sleep(1)
                # 保存聚类结果
                out_dir = os.path.join("outputs", "dataset", key, cat)
                os.makedirs(out_dir, exist_ok=True)
                with open(os.path.join(out_dir, "clusters.json"), 'w', encoding='utf-8') as f:
                    json.dump(clusters, f, indent=2, ensure_ascii=False)
                # 下载PDF
                for topic, papers in clusters.items():
                    topic_dir = os.path.join(out_dir, topic.replace('/', '_'))
                    pdf_dir = os.path.join(topic_dir, "pdfs")
                    os.makedirs(pdf_dir, exist_ok=True)
                    for paper in papers:
                        try:
                            download_arxiv_pdf(paper['arxiv_id'], pdf_dir)
                        except Exception as e:
                            print(f"Failed to download {paper['arxiv_id']}: {e}")
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/fine_topics_with_surveys.json", "w", encoding="utf-8") as f:
            json.dump(fine_surveys_map, f, indent=2, ensure_ascii=False)
        print("Saved outputs/fine_topics_with_surveys.json")

    print("All survey clustering and downloads completed.")

if __name__ == "__main__":
    main()