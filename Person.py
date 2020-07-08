class Person:
    def __init__(self, fname, lname, age, gender, race=None, height=69, weight=70) :
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.race = race
        self.height = height
        self.job = None
        self.weight = weight
        self.max_health = 100
        self.current_health = self.max_health
        self.max_strength = 10
        self.strength = self.max_strength
        self.is_alive = True
        self.is_sick = False
        self.money = 0
        self.emotional_capacity = {
            "anger": 0,
            "happiness": 0,
            "sadness": 0,
            "disgust": 0,
            "stress": 0
        }
        self.fresh_factor = 100
        self.update_person()

    def update_person (self, change_in_health=0, change_in_strength=0,cash_flow=0) :
        self.fresh_factor = self.update_fresh_factor()
        self.update_health(change_in_health)
        self.update_strength(change_in_strength)
        self.update_money(cash_flow)

    def update_fresh_factor (self) : #temporary! update with quadratic formula
        age = self.age
        if 20 < age < 40 : return float(100)
        elif 14 < age < 55 : return float(80)
        elif 10 < age < 70 : return float(50)
        elif 4 < age < 90 : return float(20)
        elif age < 100 : return float(1)
        else : self.die()

    def update_health (self, change_in_health=0) :
        self.max_health = 100 * (self.fresh_factor / 100)
        self.current_health += change_in_health
        if self.current_health > self.max_health : self.current_health = self.max_health
        elif self.current_health <= 0 : self.die()

    def update_strength(self, change_in_strength=0) :
        self.max_strength = 15 * (self.fresh_factor / 100)
        self.strength += change_in_strength
        if self.strength > self.max_strength : self.strength = self.max_strength
        if self.is_sick : self.strength *= .5
    
    def update_money(self, cash_flow) :
        self.money += cash_flow
    
    def die (self) :
        self.is_alive = False
        self.current_health = 0
        print("\n{} has died.\n".format(self.name))
        self.funeral = Funeral()

    def add_job (self, job) :
        if job == None : 
            self.job = job
            return True
        else : return False

    def remove_job (self) :
        if self.job != None :
            self.job == None
            return True
        return False

    def return_stats (self) :
        return """{fname} is a {age} year old {race} {gender} at {height} inches.""".format(fname=self.fname, age=self.age, gender=self.gender, race=self.race, height=self.height)

    # return person attributes

    def get_job (self) :
        if self.job != None :
            return self.job
        else : pass
        # - - replace pass with thrown error

    
# - - implement way of keeping track of working experience