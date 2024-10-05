"""Query the database"""

import sqlite3


# Function to insert a new record into the SpotifyDB table
def query_create():
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    try:
        # Insert a new record with sample values into the SpotifyDB table
        new_record = (
            12345,  # music_id
            "Sample Track",  # track_name
            "Sample Artist",  # artist_name
            3,  # artist_count
            2023,  # released_year
            8,  # released_month
            15,  # released_day
            100,  # in_spotify_playlists
            50,  # in_spotify_charts
            50000000,  # streams
            200,  # in_apple_playlists
            180,  # in_apple_charts
            150,  # in_deezer_playlists
            100,  # in_deezer_charts
            50,  # in_shazam_charts
            120,  # bpm
            "A",  # key
            "Minor",  # mode
            80.5,  # danceability_percent
            70.4,  # valence_percent
            90.2,  # energy_percent
            12.3,  # acousticness_percent
            0.0,  # instrumentalness_percent
            15.6,  # liveness_percent
            5.8,  # speechiness_percent
        )

        # Insert the record into the SpotifyDB table
        cursor.execute(
            """
            INSERT INTO SpotifyDB (
                music_id, track_name, artist_name, artist_count, released_year, released_month,
                released_day, in_spotify_playlists, in_spotify_charts, streams, in_apple_playlists,
                in_apple_charts, in_deezer_playlists, in_deezer_charts, in_shazam_charts, bpm,
                key, mode, danceability_percent, valence_percent, energy_percent, acousticness_percent,
                instrumentalness_percent, liveness_percent, speechiness_percent
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            new_record,
        )

        conn.commit()
        return "Create Success"

    finally:
        conn.close()


# Function to read records from the SpotifyDB table
def query_read(limit=5):
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    try:
        # Execute read query to fetch 'limit' records
        cursor.execute(f"SELECT * FROM SpotifyDB LIMIT {limit}")
        # records = cursor.fetchall()

        # Print fetched records for demonstration
        # for record in records:
        #     print(record)

        return "Read Success"

    finally:
        conn.close()


# Function to update a specific record in the SpotifyDB table
def query_update(record_id=1, new_artist_name="Updated Artist"):
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    try:
        # Update the artist_name to 'Updated Artist' for the record where id = record_id
        cursor.execute(
            """
            UPDATE SpotifyDB
            SET artist_name = ?
            WHERE id = ?
            """,
            (new_artist_name, record_id),
        )

        conn.commit()
        return "Update Success"

    finally:
        conn.close()


# Function to delete a specific record from the SpotifyDB table
def query_delete(record_id=1):
    conn = sqlite3.connect("SpotifyDB.db")
    cursor = conn.cursor()

    try:
        # Delete the record where id = record_id
        cursor.execute("DELETE FROM SpotifyDB WHERE id = ?", (record_id,))

        conn.commit()
        return "Delete Success"

    finally:
        conn.close()


# Test the functions
if __name__ == "__main__":
    print(query_create())
    print(query_read())
    print(query_update())
    print(query_delete())


# """Code Attempt for using Kickstarter Data Below"""

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
