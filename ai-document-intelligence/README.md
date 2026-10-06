# AI Document Intelligence

نظام ذكي للتعامل مع الوثائق: تصنيف، بحث دلالي، أسئلة وأجوبة (RAG)، تلخيص، مقارنة، وتوليد أسئلة.
المشروع مبني على 6 مراحل، من Machine Learning التقليدي حتى Transformers و RAG.

## المراحل

| # | المرحلة | المجلد | الحالة |
|---|---------|--------|--------|
| 1 | Machine Learning (تصنيف + K-Means + PCA) | `phase1_ml/` | قيد العمل |
| 2 | Deep Learning (Neural Network من الصفر) | `phase2_deep_learning/` | - |
| 3 | NLP Pipeline (+ Similar Documents) | `phase3_nlp/` | - |
| 4 | RNN / LSTM / GRU | `phase4_rnn_lstm_gru/` | - |
| 5 | Transformers / BERT | `phase5_transformers/` | - |
| 6 | Semantic Search + RAG | `phase6_rag_system/` | - |

## التشغيل

```bash
python -m venv .venv
source .venv/bin/activate          # ويندوز: .venv\Scripts\activate
pip install -r requirements.txt
```

المرحلة الأولى: شوفوا [OWNERSHIP.md](OWNERSHIP.md) لتوزيع الشغل.

## هيكل المشروع

- `src/`: كود قابل لإعادة الاستخدام (تنظيف، تقسيم، features، نماذج، تقييم)
- `phaseN_*/`: notebooks وتجارب كل مرحلة
- `data/`: البيانات (ما بتنرفع، شوفوا `data/README.md`)
- `reports/`: النتائج والرسوم
- `tests/`: اختبارات

طريقة العمل على Git بملف [CONTRIBUTING.md](CONTRIBUTING.md).
