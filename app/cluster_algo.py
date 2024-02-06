from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_articles(news_articles):
    if len(news_articles) < 5:
        raise ValueError("Number of news articles should be at least 5 for clustering.")

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(news_articles)

    num_clusters = min(len(news_articles), 5)  # Adjusted number of clusters
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)
    clusters = kmeans.labels_

    clustered_data = {}
    for cluster_id in range(num_clusters):
        clustered_data[cluster_id] = [news_articles[i] for i, label in enumerate(clusters) if label == cluster_id]

    return clustered_data

