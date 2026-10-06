# طريقة العمل على Git

1. ما حدا يرفع مباشرة على `main`.
2. كل مهمة بفرع مستقل: `feature/<اسم-المهمة>` (مثلاً `feature/phase1-models`).
3. كوميتات صغيرة ورسائل واضحة: `add SVM baseline`.
4. قبل ما تبلش كل يوم: `git pull origin main`.
5. Pull Request، والشخص التاني يراجعه قبل الدمج.
6. لا تشتغلوا على نفس الـ notebook بنفس الوقت (conflicts).
7. الكود المتكرر بيروح على `src/` مو منسوخ بين الـ notebooks.
8. ما ترفعوا داتا كبيرة أو نماذج مدربة.

## العقد بين الشخصين (المرحلة 1)

الشخص المسؤول عن الداتا بيحفظ:

- `data/processed/train.csv`
- `data/processed/val.csv`
- `data/processed/test.csv`

بعمودين بالضبط: `text` و `label`.
الشخص المسؤول عن النماذج بيقرأهم عن طريق `src.data.loader.load_processed()`.

## تقسيم الشغل

شوفوا [OWNERSHIP.md](OWNERSHIP.md).
