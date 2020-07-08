class Job :
    def __init__(self, rank, is_wages, paygrade, required_skills, company, hours_per_week, vacation_day_count, max_position_count, works_weekends=False) :
        self.rank = rank
        self.title = ""
        self.is_wages = is_wages
        self.hours_per_week = hours_per_week
        self.paygrade = paygrade
        self.required_skills = required_skills
        self.company = company
        self.vacation_day_count = vacation_day_count
        self.max_position_count = max_position_count
        self.positions_filled = []
        self.hours_per_day = self.calculate_hours_per_day(works_weekends)
    
    def calculate_hours_per_day (self, works_weekends) :
        if works_weekends : return self.hours_per_week / 5
        else : return self.hours_per_week / 7

    def estimate_annual_earnings (self) :
        if self.is_wages : return paygrade * ((self.hours_per_week * 52) - (self.hours_per_day * self.vacation_day_count))
        else : return self.paygrade

    def give_raise (self, increase) :
        self.paygrade += increase
        return True
    
    def give_cut (self, decrease) :
        self.paygrade -= decrease
        return True

    def calculate_bonus (self, bonus_ratio) :
        return self.paygrade * bonus_ratio

    def stress_levels (self, person) :
        pass

    def add_skill (self, new_skill) :
        self.required_skills.append(new_skill)
        return True
    
    def fill_position (self, person) :
        if len(self.positions_filled) < self.max_position_count : 
            self.positions_filled.append(person)
            person.add_job(self)
            return True
        else : return False

    def set_max_position_count(self, new_position_count) :
        if len(self.positions_filled) <= new_position_count :
            self.max_position_count = new_position_count
            return True
        else : 
            print("Too many people currently working in this division: {} too many.".format(len(self.positions_filled) - new_position_count))
            return False
    
    def vacate_position (self, person) :
        for position_idx in range(len(self.positions_filled)) :
            if self.positions_filled(position_idx) == person :
                self.positions_filled.pop(position_idx)
                person.remove_job(self)
                return True
        return False

    # retrieve data regarding job

    def get_rank (self) :
        return self.rank

    def get_remaining_positions (self) :
        return self.max_position_count - len(self.positions_filled)
