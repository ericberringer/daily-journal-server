class Mood():

    # Class initializer. It has 2 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # sets up these properties on our Mood class
    def __init__(self, id, mood):
        self.id = id
        self.mood = mood