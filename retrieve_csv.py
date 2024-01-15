# Importing necessary libraries and module
import pandas as pd
import numpy as np
import json


def main():
    CSV_PATH = '/usr/local/airflow/data/movie_short.csv'

    def retrieve_movie_df(path):

        """Fetches user data from the provided .csv movie_short file"""
        """Fetches user data from the provided .csv movielens file"""
        df = pd.read_csv(path)
        # df_json = pd.read_json("df_movies.json")
        df_movie = df.to_json(orient="records")
        movie_list = json.loads(df_movie)
        
        return movie_list




if __name__ == "__main__":
    main()
