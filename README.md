# 🧹 Python Pandas Data Cleaning Pipeline

A Python data preprocessing script built with Pandas that cleans, normalizes, and validates messy tabular data. This project demonstrates foundational data engineering tasks, including whitespace removal, missing value imputation, deduplication, and outlier filtering.

## 🚀 Key Cleaning Operations

* **String Normalization:** Trims leading and trailing whitespace from string columns using `.str.strip()`.
* **Missing Value Imputation:** Fills missing numerical values (`NaN`) dynamically with the column mean using `.fillna()`.
* **Deduplication:** Identifies and removes duplicate records using `.drop_duplicates()`.
* **Range Validation:** Filters out unrealistic or invalid numerical entries (e.g., test scores outside the range $0 < \text{Marks} \le 100$) using boolean masking.

## 🧠 Data Processing Flow

1. **Raw Input:** Contains extra spaces, missing entries (`None`), duplicate records, and out-of-bound marks ($110$).
2. **Preprocessing Pipeline:**
   * `Name`: `" Aftab "` $\rightarrow$ `"Aftab"`
   * `Age`: `None` $\rightarrow$ Imputed mean value
   * `Duplicates`: Removed exact duplicate rows
   * `Marks`: Outliers ($>100$) filtered out
3. **Clean Output:** Returns a validated DataFrame ready for analysis.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/pandas-data-cleaning.git](https://github.com/your-username/pandas-data-cleaning.git)
