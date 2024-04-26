from search import search, clean_title
from manage_s3_bucket import get_data
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == '__main__':
    movie_data = get_data("movie")
    movie_data["clean_title"] = movie_data["title"].apply(clean_title)

    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = vectorizer.fit_transform(movie_data["clean_title"])

    while True:
        title = input("Enter a movie title or [q] to quit: ")
        if title == "q":
            break
        else:
            results = search(title, movie_data, vectorizer, tfidf)
            print(results)