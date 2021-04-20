import sqlite3
import json
from models import Journal_Entry

def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.topic,
            e.journal_entry,
            e.mood_id
        FROM Journal_Entry e
        """)

        # Initialize an empty list to hold all journal_entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Journal_Entry class above.
            entry = Journal_Entry(row['id'], row['date'], row['topic'],
                            row['journal_entry'], row['mood_id'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.topic,
            e.journal_entry,
            e.mood_id
        FROM Journal_Entry e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        # we define data and that is why we pass data in our entry = Entry section below
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        # sets up init and passes in all the paramaters
        entry = Journal_Entry(data['id'], data['date'], data['topic'],
                            data['journal_entry'], data['mood_id'])

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal_Entry
        WHERE id = ?
        """, (id, ))