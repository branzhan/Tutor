class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def toStr(self):
        valStr = str(self.value)
        return "Name: " + self.name + "\n" + "Description: " + self.description + "\n" + "Value: " + valStr

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super().__init__(name, description, value)
        self.damage = damage
    
    def toStr(self):
        valStr = str(self.value)
        damStr = str(self.damage)
        return "Name: " + self.name + "\n" + "Description: " + self.description + "\n" + "Value: " + valStr + "\n" + "Damage: " + damStr

class Sword(Weapon):
    def __init__(self):
        super().__init__(name = "Sword",
                         description = "A Sword",
                         value = 10,
                         damage = 40)                                   