# مين بيشتغل على شو (المرحلة 1)

كل شخص بفرع، وبيعدّل بس على ملفاته. هيك ما بيصير conflicts.

## الشخص 1 — فرع `feature/phase1-data`
- `src/data/loader.py`
- `src/data/cleaning.py`
- `src/data/split.py`
- `src/features/tfidf.py`
- `phase1_ml/notebooks/01_eda.ipynb`
- `phase1_ml/notebooks/02_preprocessing.ipynb`
- `scripts/download_arxiv.py` (جاهز: بيحمّل الداتا من arXiv إلى `data/raw/articles.csv`)
- `data/README.md` (مصدر الداتا)

**التسليم:** `data/processed/train.csv, val.csv, test.csv` بعمودين `text,label` + دالة `load_processed()` شغالة.

## الشخص 2 — فرع `feature/phase1-models`
- `src/models/classical.py`
- `src/models/clustering.py`
- `src/evaluation/metrics.py`
- `src/evaluation/plots.py`
- `phase1_ml/notebooks/03_models.ipynb`
- `phase1_ml/notebooks/04_kmeans_pca.ipynb`

**التسليم:** جدول مقارنة النماذج الأربعة + K-Means/PCA.
**ملاحظة:** لحد ما الداتا تجهز، جرّب على `fetch_20newsgroups` بملف notebook عندك.

## مشترك (بعد ما الاتنين يخلصوا)
- `phase1_ml/run_phase1.py` — دمج كل شي بسكربت واحد (فرع `feature/phase1-integration`).
- `src/utils/config.py` — ما تعدلوه إلا باتفاق.

## ترتيب الدمج
1. Pull Request للـ `main` من كل فرع.
2. الشخص التاني بيراجع.
3. بعد دمج الاتنين: `git pull origin main` ثم تشغيل `run_phase1.py`.
