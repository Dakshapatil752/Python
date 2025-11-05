import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "NLTK is a powerful library for natural language processing in Python."

# Tokenize the text
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
print("Filtered Tokens:", filtered_tokens)

# Perform stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_tokens]
print("Stemmed Words:", stemmed_words)
