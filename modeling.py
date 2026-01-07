from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_complaints(text_data, clusters=3):
    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(text_data)

    model = KMeans(n_clusters=clusters, random_state=42)
    labels = model.fit_predict(X)

    return labels
