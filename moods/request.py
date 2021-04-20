import sqlite3
import json
from models import Mood

def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.mood
        FROM Mood m
        """)

        # Initialize an empty list to hold all mood representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an mood instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # mood class above.
            mood = Mood(row['id'], row['mood'])

            moods.append(mood.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(moods)

def get_single_mood(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.mood
        FROM Mood m
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        # we define data and that is why we pass data in our mood = Mood section below
        data = db_cursor.fetchone()

        # Create a mood instance from the current row
        # sets up init and passes in all the paramaters
        mood = Mood(data['id'], data['mood'])

        return json.dumps(mood.__dict__)