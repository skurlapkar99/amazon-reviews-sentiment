# Amazon Product Reviews — Sentiment Dashboard

Analyze Amazon product review data to extract sentiment trends, rating distributions, and helpful review patterns using Python NLP (TextBlob/VADER) and Power BI.

## Project Structure

```
amazon-reviews-sentiment/
│
├── README.md                       # This file
├── requirements.txt                # Python dependencies
├── .gitignore                      # Files/folders Git ignores
│
├── data/
│   ├── raw/                        # Original Kaggle dataset (not committed)
│   └── processed/                  # Cleaned outputs (not committed)
│
├── notebooks/
│   └── 01_text_cleaning.ipynb      # Week 1 — text cleaning pipeline
│
├── src/
│   └── cleaning_utils.py           # Reusable cleaning functions
│
├── reports/
│   ├── weekly_update.md            # Weekly status report
│   └── screenshots/                # Output screenshots
│
└── powerbi/                        # Power BI dashboard files (later weeks)
```

## Week 1 — Text Cleaning

Cleaned Amazon product review text by:
- Removing HTML tags (BeautifulSoup)
- Stripping punctuation (`string.punctuation`)
- Removing English stopwords (NLTK)

**Notebook:** [`notebooks/01_text_cleaning.ipynb`](notebooks/01_text_cleaning.ipynb)
**Weekly update:** [`reports/weekly_update.md`](reports/weekly_update.md)

## Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/amazon-reviews-sentiment.git
   cd amazon-reviews-sentiment
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset:**
   Download [Amazon Fine Food Reviews from Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) and place `Reviews.csv` in `data/raw/`.

5. **Run the notebook:**
   ```bash
   jupyter notebook
   ```
   Open `notebooks/01_text_cleaning.ipynb` and run all cells.

## Dataset

[Amazon Fine Food Reviews (Kaggle)](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) — ~568K reviews of fine foods on Amazon.

## Tools

- Python 3.10+ (pandas, BeautifulSoup, NLTK, TextBlob, VADER, matplotlib)
- Jupyter Notebook
- Power BI Desktop (upcoming weeks)

## Author

Shravani Kurlapkar
