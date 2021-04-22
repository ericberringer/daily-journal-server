import sqlite3
import json
from models import Journal_Entry
from models import Mood

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
            e.mood_id,
            m.mood
        FROM Journal_Entry e
        JOIN Mood m
            ON m.id = e.mood_id
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

            mood = Mood(row['mood_id'], row['mood'])
            entry.mood = mood.__dict__

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
            e.mood_id,
            m.mood
        FROM Journal_Entry e
        JOIN Mood m
            ON m.id = e.mood_id
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        # we define data and that is why we pass data in our entry = Entry section below
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        # sets up init and passes in all the paramaters
        entry = Journal_Entry(data['id'], data['date'], data['topic'],
                            data['journal_entry'], data['mood_id'])

        mood = Mood(data['id'], data['mood'] )
        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        # SQL query
        # Insert the new entry into the database, this will match my python db
        # new_entry[] section needs to match the object in React i.e. python server has mood_id
        # and react has mood_id written as moodId, although I have changed react to mood_id.
        db_cursor.execute("""
        INSERT INTO Journal_Entry
            ( date, topic, journal_entry, mood_id )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['date'], new_entry['topic'],
              new_entry['entry'], new_entry['mood_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)

def get_entry_by_search(search):
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
        WHERE e.journal_entry LIKE ?
        """, ( search, ))


        entries = []
        # Load the single result into memory
        # we define data and that is why we pass data in our entry = Entry section below
        dataset = db_cursor.fetchall()

        # Create an entry instance from the current row
        # sets up init and passes in all the paramaters
        for data in dataset:

            entry = Journal_Entry(data['id'], data['date'], data['topic'],
                            data['journal_entry'], data['mood_id'])

            entries.append(entry.__dict__)

        return json.dumps(entries)

def update_entry(id, updated_entry):
    # communicate with proper database
    with sqlite3.connect("./dailyjournal.db") as conn:
        # .cursor() allows us to execute SQLite statements
        db_cursor = conn.cursor()
        # executing a python query
        # implementing multiple sql parameters to update the database via data sent by the client
        # here we are changing the current state of the database (edit form)
        db_cursor.execute("""
        UPDATE Journal_Entry
            SET 
                date = ?,
                topic = ?,
                journal_entry = ?,
                mood_id = ?
        WHERE id = ?
        """, (updated_entry['date'],
            updated_entry['topic'],
            updated_entry['entry'],
            updated_entry['mood_id'], id, ))

        rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:  
        return False
    else:
        return True

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal_Entry
        WHERE id = ?
        """, (id, ))