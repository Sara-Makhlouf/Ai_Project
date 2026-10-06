"""[الشخص 1] تنظيف النصوص والتعامل مع القيم الناقصة."""
import pandas as pd


def clean_text(text: str) -> str:
    """TODO: lowercase، إزالة الروابط والرموز، توحيد المسافات."""
    raise NotImplementedError


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """TODO: احذف القيم الناقصة والمكررة، نظّف النصوص، ارجع DataFrame جديد."""
    raise NotImplementedError
