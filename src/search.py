import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from manage_s3_bucket import get_data

def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", title)

def search(title, data_set):
    movie_data = get_data("movie")

    movie_data["clean_title"] = movie_data["title"].apply(clean_title)

    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = vectorizer.fit_transform(movie_data["clean_title"])

    title = clean_title(title)
    query_vec = vectorizer.transform([title])

    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movie_data.iloc[indices][::-1]

    return results

# if __name__ == "__main__":
#     print(search("The Martian"))