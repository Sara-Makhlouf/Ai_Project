"""[الشخص 2] مقاييس التقييم."""
import pandas as pd


def evaluate(model, X, y) -> dict:
    """TODO: ارجع {"accuracy", "precision", "recall", "f1"}."""
    raise NotImplementedError


def comparison_table(results: dict) -> pd.DataFrame:
    """TODO: results = {اسم_الموديل: metrics} -> جدول مقارنة مرتب."""
    raise NotImplementedError
