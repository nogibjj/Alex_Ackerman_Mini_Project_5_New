"""
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv


# Load the CSV file and insert into a new SQLite3 database
def load(dataset="data/Spotify_Most_Streamed_Songs.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    # Open with explicit encoding
    with open(dataset, newline="", encoding="UTF-8") as csvfile:
        payload = csv.reader(csvfile, delimiter=",")

        # Skip the header of CSV
        next(payload)

        # Connect to the SQLite database
        conn = sqlite3.connect("SpotifyDB.db")
        c = conn.cursor()

        # Drop table if exists
        c.execute("DROP TABLE IF EXISTS SpotifyDB")

        # Create the table with the exact columns needed
        c.execute(
            """
            CREATE TABLE SpotifyDB (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                music_id INTEGER,
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
                in_apple_charts INTEGER,
                in_deezer_playlists INTEGER,
                in_deezer_charts INTEGER,
                in_shazam_charts INTEGER,
                bpm INTEGER,
                key TEXT,
                mode TEXT,
                danceability_percent FLOAT,  
                valence_percent FLOAT,       
                energy_percent FLOAT,        
                acousticness_percent FLOAT, 
                instrumentalness_percent FLOAT, 
                liveness_percent FLOAT,      
                speechiness_percent FLOAT   
            )
            """
        )

        # Insert data into the database
        c.executemany(
            """
            INSERT INTO SpotifyDB (
                music_id, track_name, artist_name, artist_count, released_year, released_month,
                released_day, in_spotify_playlists, in_spotify_charts, streams,
                in_apple_playlists, in_apple_charts, in_deezer_playlists, in_deezer_charts, 
                in_shazam_charts, bpm, key, mode, danceability_percent, valence_percent,
                energy_percent, acousticness_percent, instrumentalness_percent,
                liveness_percent, speechiness_percent
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            payload,
        )

        conn.commit()
        conn.close()

    return "SpotifyDB.db"


if __name__ == "__main__":
    load()

"""Code Attempt for using Kickstarter Data Below"""

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
#                 identifier INTEGER PRIMARY KEY AUTOINCREMENT,
#                 ID INTEGER ,
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
