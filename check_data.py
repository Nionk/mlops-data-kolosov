from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_csv(path: Path, expected_rows: int, base_cols: list[str], is_iris: bool = False) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Отсутствует ожидаемый файл: {path.as_posix()}")

    df = pd.read_csv(path)
    cols = list(df.columns)

    # Проверка на безымянный столбец индекса
    if any(col.startswith("Unnamed:") or col == "" for col in cols):
        raise ValueError(f"ОШИБКА [{path.name}]: Обнаружен безымянный столбец индекса: {cols}")

    # Проверка количества строк
    if len(df) != expected_rows:
        raise ValueError(
            f"ОШИБКА [{path.name}]: Количество строк ({len(df)}) != ожидаемому ({expected_rows})"
        )

    # Проверка сохранения исходных столбцов и их порядка
    if cols[: len(base_cols)] != base_cols:
        raise ValueError(
            f"ОШИБКА [{path.name}]: Нарушен порядок или состав базовых столбцов.\n"
            f"Ожидалось в начале: {base_cols}\nПолучено: {cols}"
        )

    if is_iris and ("sepal_area" in cols or "petal_area" in cols):
        expected_cols = base_cols + ["sepal_area", "petal_area"]
        if cols != expected_cols:
            raise ValueError(f"ОШИБКА [{path.name}]: Неверный состав столбцов с фичами: {cols}")

        expected_sepal = df["sepal length (cm)"] * df["sepal width (cm)"]
        expected_petal = df["petal length (cm)"] * df["petal width (cm)"]

        if not np.allclose(df["sepal_area"], expected_sepal, rtol=1e-7, atol=1e-9):
            raise ValueError(f"ОШИБКА [{path.name}]: Неверные значения в столбце sepal_area")
        if not np.allclose(df["petal_area"], expected_petal, rtol=1e-7, atol=1e-9):
            raise ValueError(f"ОШИБКА [{path.name}]: Неверные значения в столбце petal_area")

    file_hash = sha256_file(path)
    missing_count = int(df.isna().sum().sum())

    print(f"Относительный путь: {path.as_posix()}")
    print(f"SHA-256: {file_hash}")
    print(f"Строк и столбцов: {df.shape[0]} rows x {df.shape[1]} cols")
    print(f"Список столбцов: {cols}")
    print(f"Пропущенных знач.: {missing_count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Проверка CSV таблиц.")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Путь к директории с данными",
    )
    parser.add_argument(
        "--require-wine",
        action="store_true",
        help="Требовать обязательного наличия wine.csv",
    )
    parser.add_argument(
        "--require-iris-features",
        action="store_true",
        help="Требовать наличия sepal_area и petal_area в iris.csv",
    )
    args = parser.parse_args()

    iris_meta = load_iris(as_frame=True).frame
    wine_meta = load_wine(as_frame=True).frame

    iris_path = args.data_dir / "iris.csv"
    wine_path = args.data_dir / "wine.csv"

    try:
        validate_csv(
            iris_path,
            expected_rows=len(iris_meta),
            base_cols=list(iris_meta.columns),
            is_iris=True,
        )
        if args.require_iris_features:
            df_iris = pd.read_csv(iris_path)
            if "sepal_area" not in df_iris.columns or "petal_area" not in df_iris.columns:
                raise ValueError("ОШИБКА: В iris.csv отсутствуют требуемые столбцы sepal_area/petal_area")

        if wine_path.exists() or args.require_wine:
            validate_csv(
                wine_path,
                expected_rows=len(wine_meta),
                base_cols=list(wine_meta.columns),
                is_iris=False,
            )
        print("Успех")
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
