# Movie Recommendation System

> [!NOTE]
> This project is still a work in progress.

MovieLens 25M Dataset: https://grouplens.org/datasets/movielens/25m/

## Overview

For this project I wanted to implement some kind of recommendation system using aspects of ML. I chose to work on creating a movie recommender, utilizing the movie lens dataset. After doing some research I decided to integrate a combination of collaborative filtering and content based filtering. And part of the reason I chose to use this specific data set was because of the presence of different users and ratings, allowing for the implementation of collaborative filtering.

### Vision

Program prompts user for a movie, then returns a list of recommended movies. Users can also specify a specific genre that they enjoy and recommendations should be correspondingly tailored.

## Notes


## Personal Learning Objectives

These were my goals going into this project:

- Get familiar with using AWS services and storing files in the cloud
- Practice implementation of both collaborative and content based filtering
- Create search functionality to enable users to input movies
- Utilize command prompt and create a program loop to make program interactive
- Hone data processing skills

## Project Structure

- `recommend_moves-runner`: The main script to run the project.
- `src/search.py`: Search engine to find movie based on user input
- `src/movie_recommender.py`: Generates movie recommendations based on input

## Next Steps

Institute some kind of content-based filtering system, possibly integrate some kind of GUI. Tweak search and recommendation functionality to be more accurate and intuitive. Improve s3 data access speed by initially downloading csv files from bucket to project directory then referencing local files for regular program runs.