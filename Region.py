class Region :
    def __init__(self, area) :
        self.area = area

class Country (Region):
    pass

class State (Region):
    pass

class City (Region):
    pass

class Town (Region):
    pass

class Village (Region):
    pass

class Neighborhood (Region):
    def __init__(self) :
        self.homes = []
    
    def add_home (self, home) :
        self.homes.append(home)
