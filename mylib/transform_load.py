"""
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv


# Load the CSV file and insert into a new SQLite3 database
def load(dataset="data/Spotify_Most_Streamed_Songs.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    # Open with explicit encoding
    with open(dataset, newline="", encoding="utf-8") as csvfile:
        payload = csv.reader(csvfile, delimiter=",")

        # Skip the header of CSV
        next(payload)

        # Connect to the SQLite database
        conn = sqlite3.connect("SpotifyDB.db")
        c = conn.cursor()

        # Drop table if exists
        c.execute("DROP TABLE IF EXISTS SpotifyDB")

        # Create the table with the exact 20 columns needed
        c.execute(
            """
            CREATE TABLE SpotifyDB (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                track_name TEXT,
                artist_name TEXT,
                artist_count INTEGER,
                released_year INTEGER,
                released_month INTEGER,
                released_day INTEGER,
                in_spotify_playlists INTEGER,
                in_spotify_charts INTEGER,
                streams INTEGER,
                in_apple_playlists INTEGER,
                key TEXT,
                mode TEXT,
                danceability_percent INTEGER,
                valence_percent INTEGER,
                energy_percent INTEGER,
                acousticness_percent INTEGER,
                instrumentalness_percent INTEGER,
                liveness_percent INTEGER,
                speechiness_percent INTEGER,
                cover_url TEXT
            )
            """
        )

        # Insert data into the database
        c.executemany(
            """
            INSERT INTO SpotifyDB (
                track_name, artist_name, artist_count, released_year, released_month, 
                released_day, in_spotify_playlists, in_spotify_charts, streams, 
                in_apple_playlists, key, mode, danceability_percent, valence_percent, 
                energy_percent, acousticness_percent, instrumentalness_percent, 
                liveness_percent, speechiness_percent, cover_url
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            payload,
        )

        conn.commit()
        conn.close()

    return "SpotifyDB.db"


if __name__ == "__main__":
    load()


# # load the csv file and insert into a new sqlite3 database
# def load(dataset="data/kickstarter_2018.csv"):
#     """Transforms and Loads data into the local SQLite3 database"""

#     # Open with explicit encoding
#     with open(dataset, newline="", encoding="UTF-8") as csvfile:
#         payload = csv.reader(csvfile, delimiter=",")

#         conn = sqlite3.connect("KickstarterDB.db")
#         c = conn.cursor()

#         c.execute("DROP TABLE IF EXISTS kickstarterDB")

#         c.execute(
#             """
#             CREATE TABLE kickstarterDB (
#                 ID INTEGER,
#                 name TEXT,
#                 category TEXT,
#                 main_category TEXT,
#                 currency TEXT,
#                 deadline TEXT,
#                 goal FLOAT,
#                 launched TEXT,
#                 pledged FLOAT,
#                 state TEXT,
#                 backers INTEGER,
#                 country TEXT,
#                 usd_pledged FLOAT,
#                 usd_pledged_real FLOAT,
#                 usd_goal_real FLOAT
#             )
#             """
#         )

#         # insert
#         c.executemany(
#             """
#             INSERT INTO kickstarterDB (
#             ID, name, category, main_category, currency, deadline, goal, launched, pledged,
#             state, backers, country, usd_pledged, usd_pledged_real, usd_goal_real
#             )
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             """,
#             payload,
#         )

#         conn.commit()
#         conn.close()

#     return "KickstarterDB.db"


# if __name__ == "__main__":
#     load()
