"""
Extract a dataset from a URL

Kickstarter Projects From 2018 Dataset
"""

import requests
import os


# def extract(
#     url="https://raw.githubusercontent.com/nogibjj/chris_moreira_week5_python_sql_db_project/main/data/Spotify_Most_Streamed_Songs.csv",
#     file_path="data/Spotify_Most_Streamed_Songs.csv",
#     timeout=10,  # Adding a timeout to avoid indefinite hanging
# ):
#     """Extract a url to a file path"""

#     # Ensure the 'data' directory exists
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)

#     # Extract the file from the URL with a timeout
#     with requests.get(url, timeout=timeout) as r:
#         with open(file_path, "wb") as f:
#             f.write(r.content)

#     return file_path


# if __name__ == "__main__":
#     extract()


def extract(
    url="https://raw.githubusercontent.com/bharatk101/kickstarter_eda/refs/heads/master/ks-projects-201801.csv",
    file_path="data/kickstarter_2018.csv",
):
    """Extract a url to a file path"""

    # Make data directory
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Extract file from URL
    with requests.get(url, timeout=100) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    return file_path


if __name__ == "__main__":
    extract()
