class Journal_Entry():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # sets up these properties on our Animal class
    def __init__(self, id, date, topic, journal_entry, mood_id):
        self.id = id
        self.date = date
        self.topic = topic
        self.journal_entry = journal_entry
        self.mood_id = mood_id