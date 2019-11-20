# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        # Room details
        self.name = name
        self.description = description
        
        # Adjacant rooms
        self.n_to = "Solid Wall"
        self.s_to = "Solid Wall"
        self.e_to = "Solid Wall"
        self.w_to = "Solid Wall"

    def __str__(self):
        return f"Room: \n  name: {self.name}, \n  description: {self.description}"