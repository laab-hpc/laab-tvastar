from pathlib import Path

import pandas as pd


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "benchmark.csv"
)


def get_results():
    df = pd.read_csv(DATA_FILE)

    return df.to_dict(orient="records")


head = "Dashboard"
title = "Performance Report"
version = 1.0

kpis = [
    {
        "name": "Users",
        "value": 128,
    },
    {
        "name": "Revenue",
        "value": "12,457 €",
    },
    {
        "name": "Orders",
        "value": 324,
    },
    {
        "name": "Streams",
        "value": 3,
    },
]
libraries = [
    "OpenBLAS",
    "MKL",
    "AOCL"
]
results = [
    {"library": "OpenBLAS", "gflops": 120},
    {"library": "MKL",      "gflops": 145},
    {"library": "AOCL",     "gflops": 138}
]
