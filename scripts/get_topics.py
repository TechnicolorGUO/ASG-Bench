import argparse
from datetime import datetime, timedelta
import json
import os
import shutil
import time
import requests
from tqdm import tqdm
from utils import download_arxiv_pdf, extract_and_save_outline_from_md, getClient, generateResponse, pdf2md, robust_json_parse
from prompts import CATEGORIZE_SURVEY_TITLES, CATEGORIZE_SURVEY_TITLES_SINGLE, EXPAND_CATEGORY_TO_TOPICS, CATEGORIZE_SURVEY_TITLES_HEURISTIC
import arxiv
from reference import extract_refs
import concurrent.futures
from typing import List, Dict, Set, Optional

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
            "cs.AI", "cs.AR", "cs.CC", "cs.CE", "cs.CG", "cs.CL", "cs.CR", "cs.CV", "cs.CY",
            "cs.DB", "cs.DC", "cs.DL", "cs.DM", "cs.DS", "cs.ET", "cs.FL", "cs.GL", "cs.GR",
            "cs.GT", "cs.HC", "cs.IR", "cs.IT", "cs.LG", "cs.LO", "cs.MA", "cs.MM", "cs.MS",
            "cs.NA", "cs.NE", "cs.NI", "cs.OH", "cs.OS", "cs.PF", "cs.PL", "cs.RO", "cs.SC",
            "cs.SE", "cs.SI", "cs.SD", "cs.SY"
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

def get_s2_citation(arxiv_id: str) -> int:
    """
    Fetch citation count for a paper from Semantic Scholar API.
    
    Args:
        arxiv_id: The arXiv ID of the paper
        
    Returns:
        int: Number of citations, 0 if not found or error
    """
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=citationCount"
    for _ in range(3):
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.json().get("citationCount", 0)
            elif resp.status_code == 404:
                return 0
            else:
                time.sleep(1)
        except Exception as e:
            time.sleep(1)
    return 0

def get_top_survey_papers_by_citation(
    cats: List[str], 
    num: int = 10, 
    oversample: int = 3,
    months_ago_start: int = 36, 
    months_ago_end: int = 3,
    seen_ids: Optional[Set[str]] = None,
    allow_duplicates: bool = False,
    allow_cross_category: bool = False,
    max_attempts: int = 10,
    max_oversample: int = 20  # Maximum oversample rate to try
) -> List[Dict]:
    """
    Get top survey papers by citation count within a time range.
    If not enough papers are found, first increases oversample rate, then extends time window.
    
    Args:
        cats: List of arXiv categories to search
        num: Target number of papers to return
        oversample: Initial oversample rate
        months_ago_start: Start of time range in months ago
        months_ago_end: End of time range in months ago
        seen_ids: Set of already seen arXiv IDs
        allow_duplicates: Whether to allow papers that exist in seen_ids
        allow_cross_category: Whether to allow papers that exist in other categories
        max_attempts: Maximum number of time window extensions to try
        max_oversample: Maximum oversample rate to try before extending time window
        
    Returns:
        List of paper dictionaries with title, arxiv_id, citationCount and category
    """
    if seen_ids is None:
        seen_ids = set()

    now = datetime.utcnow()
    start_date = now - timedelta(days=months_ago_start*30)
    end_date = now - timedelta(days=months_ago_end*30)
    
    all_papers = []  # Store all papers found across time windows
    current_start_date = start_date
    current_end_date = end_date
    current_oversample = oversample
    attempt = 0
    last_paper_count = 0

    while len(all_papers) < num and attempt < max_attempts:
        # 1. Fetch papers for current time window
        arxiv_papers = get_arxiv_papers_in_time_range(
            cats, current_start_date, current_end_date, max_results=num*current_oversample
        )

        # 2. Get citations in parallel with progress bar
        papers = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_paper = {}
            for result in arxiv_papers:
                arxiv_id = result.entry_id.split('/')[-1].split('v')[0]
                if not allow_cross_category and not allow_duplicates and arxiv_id in seen_ids:
                    continue
                future = executor.submit(get_s2_citation, arxiv_id)
                future_to_paper[future] = {
                    "title": result.title.strip(),
                    "arxiv_id": arxiv_id,
                    "category": result.primary_category
                }
                time.sleep(0.1)  # Rate limiting

            # Add progress bar for citation fetching
            with tqdm(total=len(future_to_paper), desc="Fetching citations") as pbar:
                for future in concurrent.futures.as_completed(future_to_paper):
                    paper = future_to_paper[future]
                    try:
                        citation = future.result()
                        paper["citationCount"] = citation
                        papers.append(paper)
                    except Exception as e:
                        print(f"Error getting citation for {paper['arxiv_id']}: {e}")
                    pbar.update(1)

        # Sort by citation count
        papers.sort(key=lambda x: x["citationCount"], reverse=True)
        
        # Add new papers to all_papers
        for paper in papers:
            if paper["arxiv_id"] not in {p["arxiv_id"] for p in all_papers}:
                all_papers.append(paper)
                if not allow_cross_category:
                    seen_ids.add(paper["arxiv_id"])

        # If still not enough papers
        if len(all_papers) < num:
            print(f"\nNot enough papers found ({len(all_papers)}/{num})")
            
            # If paper count hasn't increased, try increasing oversample rate first
            if len(all_papers) == last_paper_count:
                if current_oversample < max_oversample:
                    print(f"Increasing oversample rate from {current_oversample} to {current_oversample * 2}")
                    current_oversample *= 2
                    continue
                else:
                    print("Maximum oversample rate reached, extending time window...")
                    # Move the end date to the start date, and extend start date back
                    current_end_date = current_start_date
                    current_start_date = current_start_date - timedelta(days=365)  # Extend by 1 year
                    attempt += 1
                    # Reset oversample rate for the new time window
                    current_oversample = oversample
            else:
                # If we got more papers, try increasing oversample rate
                if current_oversample < max_oversample:
                    print(f"Got more papers, increasing oversample rate from {current_oversample} to {current_oversample * 2}")
                    current_oversample *= 2
                else:
                    print("Maximum oversample rate reached, extending time window...")
                    current_end_date = current_start_date
                    current_start_date = current_start_date - timedelta(days=365)
                    attempt += 1
                    current_oversample = oversample
            
            last_paper_count = len(all_papers)
            continue

    # Sort all papers by citation count and take top num
    all_papers.sort(key=lambda x: x["citationCount"], reverse=True)
    selected_papers = all_papers[:num]
    
    return selected_papers  # Return full paper objects with citation count and category

def is_true_survey_or_review(title: str, summary: str) -> bool:
    """
    Heuristically determine if a paper is a true survey/review paper.
    
    Args:
        title: Paper title
        summary: Paper abstract/summary
        
    Returns:
        bool: True if paper appears to be a survey/review
    """
    title = title.lower()
    summary = summary.lower()
    # Exclude common false positives
    bad_keywords = [
        "code reviewer", "reviewer assignment", "reviewer selection", "peer review", "peer-review",
        "reviewing system", "review process", "reviewer recommendation"
    ]
    if any(bad in title for bad in bad_keywords):
        return False
    # Strong positive phrases
    good_phrases = [
        "a survey of", "an overview of", "a review of", "this survey", "this review",
        "comprehensive review", "comprehensive survey", "this paper surveys", "this paper reviews",
        "literature review", "review and prospect", "survey and taxonomy", "survey and analysis",
        "state of the art", "state-of-the-art review", "systematic review", "meta-analysis",
        "comparative study", "comparative analysis", "critical review", "tutorial survey",
        "empirical review", "empirical survey", "recent advances in", "recent progress in",
        "progress and challenges", "trends and challenges", "past, present and future",
        "perspectives and challenges", "review and future directions", "survey and future directions",
        "review and opportunities", "survey and opportunities", "review and trends",
        "survey and trends", "review and challenges", "survey and challenges",
        "review and perspectives", "survey and perspectives", "review and roadmap",
        "survey and roadmap", "review and outlook", "survey and outlook"
    ]
    if any(phrase in title for phrase in good_phrases):
        return True
    if any(phrase in summary for phrase in good_phrases):
        return True
    return False

def get_arxiv_papers_in_time_range(cats: List[str], start_date: datetime, end_date: datetime, max_results: int = 10) -> List:
    """
    Get survey/review papers from arXiv within a time range.
    
    Args:
        cats: List of arXiv categories
        start_date: Start of time range
        end_date: End of time range
        max_results: Maximum number of results per category
        
    Returns:
        List of arXiv paper results
    """
    client = arxiv.Client()
    seen_ids = set()
    unique_papers = []
    for cat in cats:
        query = f"cat:{cat} AND (ti:survey OR ti:review)"
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        for result in client.results(search):
            arxiv_id = result.entry_id.split('/')[-1].split('v')[0]
            published = result.published.replace(tzinfo=None)
            if (
                arxiv_id not in seen_ids
                and start_date <= published <= end_date
                and is_true_survey_or_review(result.title, result.summary)
            ):
                seen_ids.add(arxiv_id)
                unique_papers.append(result)
    print(f"Found {len(unique_papers)} unique, filtered papers in the date range across all cats.")
    return unique_papers

def copy_dataset_to_surveys(systems: List[str]) -> None:
    """
    Copy dataset to surveys directory and create system subfolders.
    
    Args:
        systems: List of system names to create subfolders for
    """
    src_root = os.path.join("outputs", "dataset")
    dst_root = "surveys"
    if os.path.exists(dst_root):
        shutil.rmtree(dst_root)
    shutil.copytree(src_root, dst_root)
    for dirpath, dirnames, filenames in os.walk(dst_root):
        rel_path = os.path.relpath(dirpath, dst_root)
        parts = rel_path.split(os.sep)
        if len(parts) == 2:
            for sys_name in systems:
                sys_dir = os.path.join(dirpath, sys_name)
                os.makedirs(sys_dir, exist_ok=True)

def generate_tasks_json(systems: List[str], surveys_root: str = "surveys") -> None:
    """
    Generate tasks.json file for the survey dataset.
    
    Args:
        systems: List of system names
        surveys_root: Root directory for surveys
    """
    tasks = {}
    leaf_dirs = []
    for dirpath, dirnames, filenames in os.walk(surveys_root):
        rel_path = os.path.relpath(dirpath, surveys_root)
        parts = rel_path.split(os.sep)
        if len(parts) == 2:
            leaf_dirs.append(dirpath)

    for system in systems:
        system_tasks = []
        for leaf in leaf_dirs:
            folder_name = os.path.basename(leaf)
            system_path = os.path.join(leaf, system)
            abs_system_path = os.path.abspath(system_path).replace(os.sep, '/')
            system_tasks.append({folder_name: abs_system_path})
        tasks[system] = system_tasks

    tasks_json_path = os.path.join(surveys_root, "tasks.json")
    with open(tasks_json_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    print(f"Generated {tasks_json_path}")

def get_existing_papers(cat: str) -> List[Dict]:
    """
    Get existing papers for a category from arxiv_ids.json.
    
    Args:
        cat: Category name
        
    Returns:
        List of paper dictionaries with title and arxiv_id
    """
    cat_dir = os.path.join("outputs", "dataset", cat)
    arxiv_ids_path = os.path.join(cat_dir, "arxiv_ids.json")
    
    if not os.path.exists(arxiv_ids_path):
        return []
    
    papers = []
    try:
        with open(arxiv_ids_path, 'r', encoding='utf-8') as f:
            arxiv_urls = json.load(f)
            for url in arxiv_urls:
                arxiv_id = url.split('/')[-1]
                papers.append({
                    "arxiv_id": arxiv_id,
                    "title": ""  # Title will be filled in during processing
                })
    except Exception as e:
        print(f"Error reading arxiv_ids.json for {cat}: {e}")
        return []
        
    return papers

def save_arxiv_ids(cat: str, papers: List[Dict]) -> None:
    """
    Save arxiv URLs to a JSON file for a category.
    
    Args:
        cat: Category name
        papers: List of paper dictionaries
    """
    cat_dir = os.path.join("outputs", "dataset", cat)
    os.makedirs(cat_dir, exist_ok=True)
    
    arxiv_urls = [f"https://arxiv.org/abs/{paper['arxiv_id']}" for paper in papers]
    with open(os.path.join(cat_dir, "arxiv_ids.json"), 'w', encoding='utf-8') as f:
        json.dump(arxiv_urls, f, indent=2, ensure_ascii=False)

def process_papers_for_category(cat: str, papers: List[Dict], client) -> None:
    """
    Process papers for a category (download PDFs, convert to MD, extract refs).
    Also updates arxiv_ids.json and clusters.json with new papers.
    
    Args:
        cat: Category name
        papers: List of paper dictionaries
        client: OpenAI client instance
    """
    cat_dir = os.path.join("outputs", "dataset", cat)
    
    # Load existing clusters if any
    clusters_path = os.path.join(cat_dir, "clusters.json")
    existing_clusters = {}
    if os.path.exists(clusters_path):
        try:
            with open(clusters_path, 'r', encoding='utf-8') as f:
                existing_clusters = json.load(f)
        except Exception as e:
            print(f"Error reading existing clusters.json for {cat}: {e}")
    
    # Process surveys in batches for clustering
    BATCH_SIZE = 10
    all_clusters = {}
    
    for batch_start in range(0, len(papers), BATCH_SIZE):
        batch = papers[batch_start:batch_start+BATCH_SIZE]
        survey_str = json.dumps(batch, ensure_ascii=False, indent=2)
        prompt = CATEGORIZE_SURVEY_TITLES_SINGLE.format(
            survey_titles=survey_str,
        )

        for attempt in range(3):
            try:
                raw_response = generateResponse(client, prompt, max_tokens=2048, temperature=0.3)
                clusters = robust_json_parse(raw_response)
                break
            except Exception as e:
                print(f"\nError for clustering '{cat}', batch {batch_start//BATCH_SIZE+1} (attempt {attempt+1}): {e}")
                if attempt == 2:
                    print(f"Failed to cluster category: {cat}, batch {batch_start//BATCH_SIZE+1}, skipping.")
                    clusters = {}
                else:
                    time.sleep(1)
        all_clusters.update(clusters)

    # Merge new clusters with existing ones
    merged_clusters = existing_clusters.copy()
    for topic, topic_papers in all_clusters.items():
        if topic in merged_clusters:
            # Add only new papers to existing topic
            existing_ids = {p['arxiv_id'] for p in merged_clusters[topic]}
            new_papers = [p for p in topic_papers if p['arxiv_id'] not in existing_ids]
            merged_clusters[topic].extend(new_papers)
        else:
            # Add new topic
            merged_clusters[topic] = topic_papers

    # Save updated clusters
    with open(clusters_path, 'w', encoding='utf-8') as f:
        json.dump(merged_clusters, f, indent=2, ensure_ascii=False)

    # Update arxiv_ids.json
    all_papers = []
    for topic_papers in merged_clusters.values():
        all_papers.extend(topic_papers)
    arxiv_urls = [f"https://arxiv.org/abs/{paper['arxiv_id']}" for paper in all_papers]
    with open(os.path.join(cat_dir, "arxiv_ids.json"), 'w', encoding='utf-8') as f:
        json.dump(arxiv_urls, f, indent=2, ensure_ascii=False)

    # Download and process PDFs for new papers only
    for topic, topic_papers in all_clusters.items():
        topic_dir = os.path.join(cat_dir, topic.replace('/', '_'))
        pdf_dir = os.path.join(topic_dir, "pdfs")
        os.makedirs(pdf_dir, exist_ok=True)
        
        for paper in topic_papers:
            try:
                download_arxiv_pdf(paper['arxiv_id'], pdf_dir)
            except Exception as e:
                print(f"Failed to download {paper['arxiv_id']}: {e}")
                
            try:
                pdf_path = os.path.join(pdf_dir, f"{paper['arxiv_id']}.pdf")
                md_dir = pdf_dir
                md_path = os.path.join(md_dir, f"{paper['arxiv_id']}.md")
                if os.path.exists(pdf_path) and not os.path.exists(md_path):
                    pdf2md(pdf_path, md_dir)
                extract_and_save_outline_from_md(md_file_path=md_path)
            except Exception as e:
                print(f"Failed to convert {paper['arxiv_id']} PDF to MD: {e}")
                
            try:
                extract_refs(input_file=md_path, output_folder=pdf_dir)
            except Exception as e:
                print(f"Failed to extract references from {paper['arxiv_id']}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numofsurvey', type=int, default=50)
    parser.add_argument('--systems', nargs='+', default=[], help='List of system names to create subfolders for')
    parser.add_argument('--allow_cross_category', action='store_true', help='Allow papers to be used in multiple categories')
    args = parser.parse_args()

    dataset_dir = os.path.join("outputs", "dataset")
    if os.path.exists(dataset_dir):
        print(f"{dataset_dir} exists, checking existing papers...")
    else:
        os.makedirs(dataset_dir, exist_ok=True)

    client = getClient()
    coarse_surveys_map = {}
    seen_ids_global = set()

    # First pass: Collect all arxiv IDs
    for key in tqdm(category_map, desc="Collecting papers"):
        cats = category_map[key]
        print(f"Processing category: {key}")
        
        # Get existing papers
        existing_papers = get_existing_papers(key)
        existing_ids = {paper['arxiv_id'] for paper in existing_papers}
        seen_ids_global.update(existing_ids)
        
        if len(existing_papers) >= args.numofsurvey:
            print(f"Category {key} already has enough papers ({len(existing_papers)}/{args.numofsurvey})")
            coarse_surveys_map[key] = existing_papers
            continue
            
        # Calculate how many more papers we need
        needed = args.numofsurvey - len(existing_papers)
        print(f"Category {key} needs {needed} more papers")
        
        # Get additional papers
        new_papers = get_top_survey_papers_by_citation(
            cats,
            num=needed,
            oversample=2,
            seen_ids=seen_ids_global,
            allow_duplicates=False,
            allow_cross_category=args.allow_cross_category
        )
        
        # Combine existing and new papers
        all_papers = existing_papers + new_papers
        coarse_surveys_map[key] = all_papers
        
        # Save arxiv IDs
        save_arxiv_ids(key, all_papers)

    # Save the complete paper list
    with open("outputs/dataset/topics.json", "w", encoding="utf-8") as f:
        json.dump(coarse_surveys_map, f, indent=2, ensure_ascii=False)
    print("Saved outputs/dataset/topics.json")

    # Second pass: Process all papers
    for key in tqdm(category_map, desc="Processing papers"):
        papers = coarse_surveys_map[key]
        process_papers_for_category(key, papers, client)

    copy_dataset_to_surveys(args.systems)
    generate_tasks_json(args.systems)
    print("Data generation complete. Copied dataset to surveys/ and created system subfolders.")

if __name__ == "__main__":
    # main()
    get_arxiv_papers_in_time_range(category_map["eess"], datetime(2024, 1, 1), datetime(2025, 12, 31))

#python scripts/get_topics.py --granularity coarse --numofsurvey 10 --systems InteractiveSurvey AutoSurvey SurveyX SurveyForge LLMxMapReduce vanilla