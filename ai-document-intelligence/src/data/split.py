"""[الشخص 1] تقسيم Train / Validation / Test."""
import pandas as pd


def split_dataframe(df: pd.DataFrame, val_size: float = 0.15, test_size: float = 0.15, seed: int = 42) -> dict:
    """TODO: تقسيم طبقي (stratified). ارجع {"train", "val", "test"}."""
    raise NotImplementedError


def split_and_save(df: pd.DataFrame, **kwargs) -> dict:
    """TODO: قسّم واحفظ train.csv / val.csv / test.csv بـ data/processed."""
    raise NotImplementedError
