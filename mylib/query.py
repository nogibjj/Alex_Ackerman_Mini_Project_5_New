"""Query the database"""

import sqlite3


def query_create():
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    # Inserting a random row into the SpotifyDB table
    random_record = (
        "Random Song",
        "Random Artist",
        1,
        2024,
        10,
        3,
        400,
        100,
        150000000,
        200,
        "C#",
        "Major",
        60,
        70,
        80,
        10,
        0,
        20,
        5,
        "https://coverurl.com",
    )

    # Insert the record
    cursor.execute(
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
        random_record,
    )

    conn.commit()
    conn.close()
    return "Create Success"


def query_read():
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    # read execution
    cursor.execute("SELECT * FROM SpotifyDB LIMIT 10")

    conn.close()
    return "Read Success"


def query_update():
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    # Update the artist_name to 'Chris' for the record where id is 3
    cursor.execute(
        """
        UPDATE SpotifyDB 
        SET artist_name = 'Chris' 
        WHERE id = 3
        """
    )

    conn.commit()
    conn.close()
    return "Update Success"


def query_delete():
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    # Delete the record where id is 5
    cursor.execute("DELETE FROM SpotifyDB WHERE id = 5")

    conn.commit()
    conn.close()
    return "Delete Success"


if __name__ == "__main__":
    query_create()
    query_read()
    query_update()
    query_delete()

# # Function to insert a new project into the kickstarter table
# def queryCreate():
#     conn = sqlite3.connect("KickstarterDB.db")
#     cursor = conn.cursor()
#     # Insert execution (example project details provided)
#     cursor.execute(
#         """
#         INSERT INTO kickstarterDB (ID, name, category, main_category, currency, deadline, goal, launched, pledged, state, backers, country, usd_pledged, usd_pledged_real, usd_goal_real)
#         VALUES (1, 'Sample Project', 'Technology', 'Tech', 'USD', '2024-12-31', 10000, '2024-01-01', 5000, 'live', 100, 'US', 5000, 5000, 10000)
#         """
#     )
#     conn.commit()
#     conn.close()
#     return "Create Success"


# # Function to read data from the kickstarter table
# def queryRead():
#     conn = sqlite3.connect("KickstarterDB.db")
#     cursor = conn.cursor()
#     # Read execution
#     cursor.execute("SELECT * FROM kickstarterDB LIMIT 10")
#     # rows = cursor.fetchall()
#     conn.close()
#     # return rows
#     return "Read Success"


# # Function to update an entry in the kickstarter table
# def queryUpdate():
#     conn = sqlite3.connect("kickstarterDB.db")
#     cursor = conn.cursor()
#     # Update execution (updating an example project)
#     cursor.execute("UPDATE kickstarterDB SET pledged = 6000 WHERE ID = 1")
#     conn.commit()
#     conn.close()
#     return "Update Success"


# # Function to delete an entry from the kickstarter table
# def queryDelete():
#     conn = sqlite3.connect("KickstarterDB.db")
#     cursor = conn.cursor()
#     # Delete execution
#     cursor.execute("DELETE FROM kickstarterDB WHERE ID = 1")
#     conn.commit()
#     conn.close()
#     return "Delete Success"


# # Main program execution
# if __name__ == "__main__":
#     print(queryCreate())
#     print(queryRead())
#     print(queryUpdate())
#     print(queryDelete())
