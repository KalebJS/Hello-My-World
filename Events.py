
import random

class Event :
    def __init__ (self, participants, time_required=0) :
        self.participants = participants
        self.time_required = time_required

    def add_participant (self, person) :
        self.participants.append(person)
    
    def increment_time (self, time_increment=1) :
        self.time_required += time_increment

class Brawl (Event) : #check syntax for subclass
    def __init__ (self, participants) :
        super().__init__(participants)
    
    def tc_fight (self) :
        for fighter in self.participants : #everyone gets a punch
            victim = self.determine_victim(fighter, [other for other in self.participants if other != fighter])
            if victim is not None and fighter.is_alive == True:
                damage = self.calculate_damage(fighter, victim)
                print("{} attacked {} causing {} damage.".format(fighter.name, victim.name, round(damage, 2)))
                if victim.is_alive == False : print("(Talk about flogging a dead horse.)")
                else : victim.update_health(-damage)
            else :
                print("{} never got to hit anything.".format(fighter.name))

    def begin_brawl (self) :
        while len(self.participants) >= 2 :
            self.round_of_attack()

            #ensures at least two people remain for the brawl
            self.participants = [participant for participant in self.participants if participant.is_alive == True]
        else : 
            if len(self.participants) > 0 : print("{} wins!".format(self.participants[0].name))
            else : print("Literally everybody died... What a blood bath.")
    
    def calculate_damage (self, attacker, victim) :
        #multiplier accounts for victim's health
        multiplier = float(victim.current_health) / 100 
        return attacker.strength / multiplier if multiplier > 0 else 0
        #should eventually account for if a person is already dead.
         
    def determine_victim (self, attacker, others) :
        path = random.randint(0, 100)
        if path <= 70 : return others[random.randint(0, len(others) - 1)] #attack an other person
        elif path <= 95 : return attacker #attack self... idiot.
        else : return None #misses altogether

    def forfeit (self) :
        pass

class Accident (Event) :
    def __init__(self) :
        pass

class Marriage (Event) :
    def __init__ (self, participants) :
        super(participants)


class GroceryShopping (Event) :
    def __init__ (self, participants) :
        super(participants)


class Funeral (Event) :
    def __init__(self) :
        pass

class Birth (Event) :
    def __init__ (self, participants) :
        super(participants)

class Conversation (Event) :
    def __init__(self, participants) :
        pass

class Cooking (Event) :
    def __init__(self) :
        pass