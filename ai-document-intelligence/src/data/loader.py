"""[الشخص 1] تحميل البيانات.

العقد: data/processed/{train,val,test}.csv بعمودين: text, label
"""
import pandas as pd

from src.utils.config import DATA_PROCESSED, DATA_RAW, LABEL_COL, TEXT_COL


def load_raw(filename: str = "articles.csv") -> pd.DataFrame:
    """TODO: اقرأ الملف من data/raw وارجع DataFrame فيه عمودي text و label."""
    raise NotImplementedError


def load_processed() -> dict:
    """TODO: ارجع {"train": df, "val": df, "test": df} من data/processed.
    الشخص 2 بيستعمل هاي الدالة لقراءة الداتا."""
    raise NotImplementedError
