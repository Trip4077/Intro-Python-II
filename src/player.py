# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.items = []
        self.current_room = None

    def __str__(self):
        return f"Player:\n  name: {self.name}\n  category: {self.category}\n  items: {self.items}\n current_roomm: {self.current_room}"