from search import search, clean_title
import pandas as pd
from manage_s3_bucket import get_data
from sklearn.feature_extraction.text import TfidfVectorizer

def findSimilarMovies(movie_id, ratings, movies):   
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]

    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .1]

    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())

    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis = 1)
    rec_percentages.columns = ["similar", "all"]

    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending = False)

    res = rec_percentages.head(10).merge(movies, left_index = True, right_on = "movieId")[["score", "title", "genres"]]
    return res

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
            print(movie_id)
            movie_recommendations = findSimilarMovies(movie_id, ratings_data, movie_data)
            print("-" * 40)
            print(movie_recommendations)
            print("-" * 40)