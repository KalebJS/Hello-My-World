class Location :
    def __init__(self, area) :
        self.area = area

# - - - - - - - - - - - - 

class Building (Location):
    def __init__(self, floors) :
        self.floors = floors
        self.has_electricity = True
        self.electricity_bill = 0
        self.has_water = True
        self.water_bill = 0
        self.inhabitants = []

    def move_locations (self, destination) :
        destination.inhabitants.append(self.inhabitants)
        self.inhabitants = []

class Recreation (Location):
    pass

class Plant (Location):
    pass

class Room :
    def __init__(self, chair_count=0, bed_count=0, table_count=0, appliances=0) :
        self.chair_count = chair_count
        self.bed_count = bed_count
        self.table_count = table_count
        self.appliances = appliances

# - - - - - - - - - - - -

class Home (Building) :
    def __init__(self, neighborhood, bedroom_count=1,bathroom_count=1) :
        self.bathrooms = [Room() for i in range(bathroom_count)]
        self.bedrooms = [Room() for i in range(bedroom_count)]
        self.kitchen = Room()
        self.living_room = Room()
        self.closet = Room()
        self.has_electricity = True
        self.electricity_bill = 0
        self.has_water = True
        self.water_bill = 0
        self.inhabitants = []
        self.neighborhood = neighborhood
    
    def add_inhabitant (self, person) :
        if person not in inhabitants : self.inhabitants.append(person)

    def remove_inhabitant (self, person) :
        for idx in len(range(inhabitants)) :
            if inhabitants[idx] == person :
                inhabitants.pop(idx)


class Office (Building) :
    def __init__(self) :
        pass

class Restaraunt (Building) :
    def __init__(self) :
        pass

class GroceryStore (Building) :
    def __init__(self) :
        pass

class Hospital (Building) :
    def __init__(self) :
        pass

class School (Building) :
    def __init__(self) :
        pass

class Apartments (Building) :
    def __init__(self) :
        pass

class Museum (Building) :
    def __init__(self) :
        pass

class Gym (Building) :
    def __init__(self) :
        pass

class Church (Building) :
    def __init__(self) :
        pass

class Beach (Recreation) :
    def __init__(self) :
        pass

class Park (Recreation) :
    def __init__(self) :
        pass

class Campground (Recreation) :
    def __init__(self) :
        pass

class Factory (Plant) :
    def __init__(self) :
        pass

class Farm (Plant) :
    def __init__(self) :
        pass

class Utilities (Plant) :
    def __init__(self) :
        pass

class Sewage (Plant) :
    def __init__(self) :
        pass