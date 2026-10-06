
import argparse
from pathlib import Path

import arxiv
import pandas as pd

CATS = {
    "cs.AI": "Artificial Intelligence",
    "cs.CR": "Cybersecurity",
    "cs.PL": "Programming",
    "cs.NI": "Networks",
    "cs.DB": "Data Science",
}
OUT = Path(__file__).resolve().parents[1] / "data" / "raw" / "articles.csv"


def main(per_class: int):
    client = arxiv.Client(page_size=200, delay_seconds=3, num_retries=3)
    rows = []
    for cat, label in CATS.items():
        search = arxiv.Search(query=f"cat:{cat}", max_results=per_class * 2,
                              sort_by=arxiv.SortCriterion.SubmittedDate)
        count = 0
        for r in client.results(search):
            if r.primary_category == cat:
                rows.append({"text": f"{r.title}. {r.summary}", "label": label})
                count += 1
                if count >= per_class:
                    break
        print(f"{label}: {count}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"Saved {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-class", type=int, default=1000)
    main(ap.parse_args().per_class)
