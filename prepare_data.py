from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_iris, load_wine

DATA_DIR = Path("data")
IRIS_PATH = DATA_DIR / "iris.csv"
WINE_PATH = DATA_DIR / "wine.csv"


def save_deterministic_csv(df: pd.DataFrame, path: Path, sort_cols: list[str]) -> None:
    """Детерминированная сортировка и сохранение в CSV без индекса."""
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = df.sort_values(by=sort_cols, kind="mergesort").reset_index(drop=True)
    ordered.to_csv(path, index=False, lineterminator="\n", float_format="%.10g")


def get_base_iris() -> tuple[pd.DataFrame, list[str]]:
    iris = load_iris(as_frame=True).frame.copy()
    base_cols = list(iris.columns)
    return iris, base_cols


def get_base_wine() -> tuple[pd.DataFrame, list[str]]:
    wine = load_wine(as_frame=True).frame.copy()
    base_cols = list(wine.columns)
    return wine, base_cols


def main() -> None:
    parser = argparse.ArgumentParser(description="Детерминированный генератор данных.")
    parser.add_argument(
        "mode",
        choices=["base", "wine", "iris_features"],
        help="Режим генерации: base | wine | iris_features",
    )
    args = parser.parse_args()

    if args.mode == "base":
        iris_df, sort_cols = get_base_iris()
        save_deterministic_csv(iris_df, IRIS_PATH, sort_cols)
        print(f"[base] Сохранен {IRIS_PATH.as_posix()}")

    elif args.mode == "wine":
        wine_df, sort_cols = get_base_wine()
        save_deterministic_csv(wine_df, WINE_PATH, sort_cols)
        print(f"[wine] Сохранен {WINE_PATH.as_posix()}")

    elif args.mode == "iris_features":
        iris_df, sort_cols = get_base_iris()
        iris_df = iris_df.sort_values(by=sort_cols, kind="mergesort").reset_index(drop=True)
        iris_df["sepal_area"] = iris_df["sepal length (cm)"] * iris_df["sepal width (cm)"]
        iris_df["petal_area"] = iris_df["petal length (cm)"] * iris_df["petal width (cm)"]
        save_deterministic_csv(iris_df, IRIS_PATH, sort_cols)
        print(f"[iris_features] Обновлен {IRIS_PATH.as_posix()} с новыми признаками")


if __name__ == "__main__":
    main()