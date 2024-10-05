"""
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/kickstarter_2018.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Open with explicit encoding
    with open(dataset, newline="", encoding="UTF-8") as csvfile:
        payload = csv.reader(csvfile, delimiter=",")

        conn = sqlite3.connect("KickstarterDB.db")
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS kickstarter")

        c.execute(
            """
            CREATE TABLE kickstarter (
                ID INTEGER,
                name TEXT,
                category TEXT,
                main_category TEXT,
                currency TEXT,
                deadline TEXT,
                goal FLOAT,
                launched TEXT,
                pledged FLOAT,
                state TEXT,
                backers INTEGER,
                country TEXT,
                usd_pledged FLOAT,
                usd_pledged_real FLOAT,
                usd_goal_real FLOAT
            )
            """
        )

        # insert
        c.executemany(
            """
            INSERT INTO kickstarter
            (ID, name, category, main_category, currency, deadline, goal, launched, pledged,
            state, backers, country, usd_pledged, usd_pledged_real, usd_goal_real)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            payload,
        )

        conn.commit()
        conn.close()

    return "KickstarterDB.db"


if __name__ == "__main__":
    load()
