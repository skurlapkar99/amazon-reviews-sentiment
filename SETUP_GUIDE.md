# SETUP GUIDE — Do this in order

## 1. Create the GitHub repo

1. Go to https://github.com → click **+** → **New repository**
2. Name: `amazon-reviews-sentiment`
3. Description: "Amazon product reviews sentiment analysis dashboard using Python NLP and Power BI"
4. Public
5. **Do NOT** check "Initialize with README" (we already have one)
6. Click **Create repository**

## 2. Push this project to GitHub

Open a terminal / Command Prompt inside this folder and run:

```bash
git init
git add .
git commit -m "Week 1: text cleaning pipeline complete"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/amazon-reviews-sentiment.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

If Git asks you to log in, follow the browser prompt.

## 3. Set up Python locally

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

## 4. Download the dataset

1. Go to https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
2. Log in / sign up (free)
3. Click **Download** → extract the zip
4. Move `Reviews.csv` into the `data/raw/` folder of this project

## 5. Run the notebook

```bash
jupyter notebook
```

Open `notebooks/01_text_cleaning.ipynb` → run all cells (Cell → Run All).

Verify:
- The "Before vs After" cell shows HTML/punctuation/stopwords removed
- `data/processed/Reviews_cleaned.csv` now exists

## 6. Take screenshots

Save these into `reports/screenshots/`:

- `01_dataset_shape.png` — dataset shape output
- `02_before_after.png` — before/after comparison output
- `03_length_stats.png` — character length reduction
- `04_output_file.png` — file explorer showing Reviews_cleaned.csv

## 7. Update repo URLs

Before pushing, edit these files and replace `YOUR-USERNAME` with your actual GitHub username:

- `README.md`
- `reports/weekly_update.md`

## 8. Push everything

```bash
git add .
git commit -m "Add screenshots and update repo URLs"
git push
```

## 9. Reply to Samiksha

Use this email template:

---

Hi Samiksha,

Sharing my Week 1 update for the Amazon Product Reviews project.

**Repository:** https://github.com/YOUR-USERNAME/amazon-reviews-sentiment
**Weekly update:** https://github.com/YOUR-USERNAME/amazon-reviews-sentiment/blob/main/reports/weekly_update.md
**Notebook:** https://github.com/YOUR-USERNAME/amazon-reviews-sentiment/blob/main/notebooks/01_text_cleaning.ipynb

Summary: Completed the text cleaning pipeline (HTML removal, punctuation, stopwords) on the Amazon Fine Food Reviews dataset (~568K rows). Cleaned output is saved to `data/processed/`. Next week I'll move on to sentiment analysis with TextBlob and VADER.

No blockers. Happy to walk through the notebook if useful.

Best,
Shravani

---
