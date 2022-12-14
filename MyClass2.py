# I have created a class with an instance

class ship:
    def __init__(self, manufacturer, color):
        self.manufacturer = manufacturer
        self.color = color


# ship class is now created, so we can create an instance os the class. The instance gets the same key characters
# next I have told Python to get the key characters of boat and use them for Big_boat and Small_boat
Big_boat = ship("Big_engine", "crew quarters")
Small_boat = ship("small_engine", "small_sail")
# printing now will give to diffectent outputs as they both point to different instances of the memory
print(Big_boat)
# Big_boat has the same characters as the class ship and has additional characters of its own.
# I have then printed Big_boat