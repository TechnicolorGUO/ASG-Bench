import arxiv

# 所有CS子类（2024年官方）
cs_subcats = [
    "cs.AI", "cs.AR", "cs.CC", "cs.CE", "cs.CG", "cs.CL", "cs.CR", "cs.CV", "cs.CY",
    "cs.DB", "cs.DC", "cs.DL", "cs.DM", "cs.DS", "cs.ET", "cs.FL", "cs.GL", "cs.GR",
    "cs.GT", "cs.HC", "cs.IR", "cs.IT", "cs.LG", "cs.LO", "cs.MA", "cs.MM", "cs.MS",
    "cs.NA", "cs.NE", "cs.NI", "cs.OH", "cs.OS", "cs.PF", "cs.PL", "cs.RO", "cs.SC",
    "cs.SE", "cs.SI", "cs.SD", "cs.SY"
]

client = arxiv.Client(num_retries=1, page_size=10)

for cat in cs_subcats:
    query = f'cat:{cat} AND (ti:survey OR ti:review)'
    search = arxiv.Search(
        query=query,
        max_results=1,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    print(f"\n--- {cat} ---")
    found = False
    for result in client.results(search):
        print(f"title: {result.title.strip()}\narxiv_id: {result.entry_id.split('/')[-1].split('v')[0]}\ndate: {result.published.date()}")
        found = True
    if not found:
        print("No survey/review paper found.")