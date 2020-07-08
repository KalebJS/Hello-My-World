class Group :
    pass 

class Guild (Group):
    def __init__ (self) :
        self.guild_members = []

    def add_member (person) :
        self.guild_members.append(person)
        #should heapify guild so that strongest member is at the top.

class Spouse (Group) :
    pass