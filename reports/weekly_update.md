# Weekly Update — Week 1 (29 Jun – 5 Jul 2026)

**Project:** Amazon Product Reviews Sentiment Dashboard
**Author:** Shravani Kurlapkar
**Manager:** Samiksha Negi

---

## ✅ What I completed

- Set up the project repository with a clean, reproducible folder structure (`data/`, `notebooks/`, `src/`, `reports/`, `powerbi/`)
- Downloaded the Amazon Fine Food Reviews dataset from Kaggle (~568K reviews)
- Built a text-cleaning pipeline in Python that:
  - Removes HTML tags using BeautifulSoup
  - Strips punctuation using `string.punctuation`
  - Removes English stopwords using NLTK
- Verified cleaning quality by comparing raw vs cleaned samples side-by-side
- Saved the cleaned dataset to `data/processed/Reviews_cleaned.csv`
- Extracted reusable cleaning functions into `src/cleaning_utils.py`

## 🔍 What I discovered

- The dataset has ~568K reviews after removing nulls and duplicates
- Many reviews contained embedded HTML tags (mainly `<br />`)
- Average review length dropped noticeably after cleaning (~40–50% reduction in character count due to stopword removal)
- No major data quality issues found — the dataset is well-structured

## 🚀 What I will do next

- Apply sentiment scoring using **TextBlob** and **VADER** on the cleaned text
- Analyze how sentiment correlates with star ratings (1–5)
- Explore patterns in "helpful" reviews (using `HelpfulnessNumerator` / `HelpfulnessDenominator`)
- Begin importing the processed data into Power BI for initial visualizations

## ⚠️ Risks / Blockers

- **None currently**
- (Minor note: dataset is ~300MB — may need to sample rows for smoother Power BI performance in later weeks)

## 📁 Artifacts

- **Repository:** https://github.com/YOUR-USERNAME/amazon-reviews-sentiment
- **Notebook:** `notebooks/01_text_cleaning.ipynb`
- **Reusable code:** `src/cleaning_utils.py`
- **Output:** `data/processed/Reviews_cleaned.csv` (generated locally after running the notebook)
- **Screenshots:** `reports/screenshots/`

## 🔁 How to reproduce

```bash
git clone https://github.com/YOUR-USERNAME/amazon-reviews-sentiment.git
cd amazon-reviews-sentiment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
# Download Reviews.csv from Kaggle into data/raw/
jupyter notebook notebooks/01_text_cleaning.ipynb
# Run all cells
```
