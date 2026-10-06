"""[الشخص 2] النماذج التقليدية."""

MODEL_NAMES = ["Logistic Regression", "Decision Tree", "Random Forest", "SVM"]


def build_pipeline(name: str):
    """TODO: ارجع sklearn Pipeline = TF-IDF (من src.features.tfidf) + classifier حسب الاسم."""
    raise NotImplementedError


def train_model(name: str, X_train, y_train):
    """TODO: درّب الـ pipeline وارجعه."""
    raise NotImplementedError
