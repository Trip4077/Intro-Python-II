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

    def grab(self, item_to_grab=None):
        if not item_to_grab:
            item_to_grab = input( "\nWhat item do you want to grab\n------> " )

        for item in self.current_room.items:
 
            if item.name.lower() == item_to_grab.lower():
                self.items.append( item )
                self.current_room.items.remove( item )
                item.on_grab()
                break

    def drop(self, item_to_drop=None):
        if not item_to_drop:
            item_to_drop = input ( "\nWhat item do you want to drop\n------> " )

        for item in self.items:

            if item.name.lower() == item_to_drop.lower():
                self.current_room.items.append( item )
                self.items.remove( item )
                item.on_drop()
                break

    def look(self):
        print( f"\n{self.name} found:" )

        if len( self.current_room.items ) > 0:
            for item in self.current_room.items:
                print( f">> {item}" )

        else:
            print("Nothing...")

    def show_inventory(self):
        print( f"\n{self.name}\'s Invertory:" )

        for item in self.items:
            print( f">> {item}" )

    def move_rooms(self, direction):
        if direction == 'n':
            if self.current_room.n_to == "Solid Wall":
                print( "\nYou find a solid wall, there might be another way..." )
            else:
                self.current_room = self.current_room.n_to

        elif direction == 's':
            if self.current_room.s_to == "Solid Wall":
                print( "\nYou find a solid wall, there might be another way..." )
            else:
                self.current_room = self.current_room.s_to

        elif direction == 'e':
            if self.current_room.e_to == "Solid Wall":
                print( "\nYou find a solid wall, there might be another way..." )
            else:
                self.current_room = self.current_room.e_to
        else:
            if self.current_room.w_to == "Solid Wall":
                print( "\nYou find a solid wall, there might be another way..." )
            else:
                self.current_room = self.current_room.w_to