import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    return " ".join(tokens)

def preprocess_data(df):
    df = df.copy()
    df['clean_text'] = df['complaint_text'].apply(clean_text)
    return df
