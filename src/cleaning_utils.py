"""
cleaning_utils.py
-----------------
Reusable text cleaning functions for the Amazon Reviews project.
"""

import string
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are available
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords', quiet=True)

STOP_WORDS = set(stopwords.words('english'))


def remove_html(text: str) -> str:
    """Strip HTML tags from text using BeautifulSoup."""
    if not isinstance(text, str):
        text = str(text)
    return BeautifulSoup(text, 'html.parser').get_text()


def remove_punctuation(text: str) -> str:
    """Remove all punctuation characters from text."""
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_stopwords(text: str) -> str:
    """Lowercase text and remove English stopwords."""
    words = text.lower().split()
    return ' '.join(w for w in words if w not in STOP_WORDS)


def clean_text(text: str) -> str:
    """Full cleaning pipeline: HTML → punctuation → stopwords."""
    text = remove_html(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    return text
