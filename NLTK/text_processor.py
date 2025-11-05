# text_processor.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download resources (only first time)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

ps = PorterStemmer()

def preprocess_text(text):
    """Tokenize, remove stopwords, and stem words."""
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word.lower() not in stopwords.words('english')]
    stemmed = [ps.stem(word) for word in filtered]
    return stemmed
