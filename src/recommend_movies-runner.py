from search import search, clean_title
import pandas as pd
from manage_s3_bucket import get_data
from sklearn.feature_extraction.text import TfidfVectorizer
from movie_recommender import findSimilarMovies

if __name__ == '__main__':
    # movie_data = get_data("movie")
    movie_data = pd.read_csv("../ml-25m/movies.csv")
    print("Movies loaded")
    # ratings_data = get_data("ratings")
    ratings_data = pd.read_csv("../ml-25m/ratings.csv")
    print("Ratings loaded")
    movie_data["clean_title"] = movie_data["title"].apply(clean_title)

    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = vectorizer.fit_transform(movie_data["clean_title"])

    while True:
        title = input("Enter a movie title or [q] to quit: ")
        if title == "q":
            break
        else:
            search_results = search(title, movie_data, vectorizer, tfidf)
            movie_id = search_results.movieId.iloc[0]
            movie_recommendations = findSimilarMovies(movie_id, ratings_data, movie_data)

            print("-" * 40)
            if movie_recommendations.empty:
                print(f"Not seeing any results for [{title}]")
                print("Make sure to use specific titles and include articles (The, A, An etc.) and production year for better results")
            else:
                print(f"Showing recommendations for {title}:")
                print(movie_recommendations)
            print("-" * 40)