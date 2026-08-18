#!/usr/bin/env python3
import csv

path = "data.csv"

def find_nans(path):
    nan_tokens = {"", "nan", "NaN", "NAN", "NA", "N/A", "null", "NULL"}
    found = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        for row_idx, row in enumerate(reader, start=2):  # 2 = first data row after header
            for col_idx, value in enumerate(row):
                if value.strip() in nan_tokens:
                    col_name = header[col_idx] if col_idx < len(header) else f"col{col_idx}"
                    found.append((row_idx, col_idx + 1, col_name, value))

    return found

def main():
    results = find_nans(path)

    if not results:
        print("No NaN/missing values found.")
        return

    print(f"Found {len(results)} NaN/missing value(s):\n")
    for row, col, col_name, raw in results:
        print(f"Row {row}, Column {col} ({col_name}): {raw!r}")

if __name__ == "__main__":
    main()
