import pandas as pd
import boto3
import os
import io
from dotenv import load_dotenv
load_dotenv()

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

def get_data(type):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    bucket_name = "mm01-movie-data"

    if (type == 'movie'):
        s3Obj = s3.get_object(Bucket=bucket_name, Key="movies.csv")
        movie_data = s3Obj["Body"].read().decode("utf-8")
        movies = pd.read_csv(io.StringIO(movie_data), index_col=0)

        print("Movies Loaded")
        return movies
    
    elif (type == 'ratings'):
        s3Obj = s3.get_object(Bucket=bucket_name, Key="ratings.csv")
        ratings_data = s3Obj["Body"].read().decode("utf-8")
        ratings = pd.read_csv(io.StringIO(ratings_data), index_col=0)

        print("Ratings Loaded")
        return ratings