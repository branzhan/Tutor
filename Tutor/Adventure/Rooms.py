import Items, Enemies

class Room():
    text = "Generic Room"
    def __init__(self):
        self.room_text = text
    
    def room_text(self):
        return self.room_text

class LootRoom(Room):
    def __init__(self, item):
        self.item = item
        super().__init__(room_text = "Contains loot")

