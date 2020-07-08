class Company :
    def __init__(self, location, payday_frequency=1,budget=0) :
        self.employees = [] # - - consider converting to dictionary with person class pointing to job class
        self.location = location
        self.payday_frequency = payday_frequency
        self.budget = budget
        self.annual_earnings = 0
        self.annual_spending = 0
        self.divisions = {}

    def open_division (self, division_title) :
        self.divisions[division_title] = []

    def open_job (self, job, division_title) :
        self.divisions[division_title].append(job)

    def close_division (self, division_title) :
        for job in self.divisions[division_title] :
            for employee in job.positions_filled :
                self.fire_employee(employee, job)
        # - - figure out how to delete a key

    def close_job (self, division_title, job) :
        for job_idx in range(len(self.divisions[division_title])) :
            if job == self.divisions[division_title][job_idx] :
                for employee in job.positions_filled :
                    self.fire_employee(employee, job)
                return True

    def update_location (self, new_location) :
        self.location = new_location
        return True
    
    def hire_employee (self, person, job) :
        if person not in self.employees :
            self.employees.append(person)
            job.fill_position(person)
            return True
        else : return False
    
    def fire_employee (self, person) :
        if person in self.employees :
            #one month of severance
            self.give_bonus(float(0.083), person)
            job = person.get_job()
            job.vacate_position(person)
            self.employees.pop([idx for idx in range(len(self.employees)) if self.employees[idx] == person][0])
            return True
        else : return False

    def hiring_process (self, applicants) :
        pass

    def pay_employees (self, bonus=False) : 
        for employee in self.employees :
            paycheck = 0
            job = employee.get_job()
            if job.is_wages :
                # - -fix wages algorithm... 
                paycheck = job.hours_per_week * paygrade * self.payday_frequency
            else :
                paycheck = paygrade / (52 / self.payday_frequency)
            self.spend_money(bonus)
            employee.update_money(paycheck)

    def give_bonus (self, bonus_ratio, person=None) :
        #bonus ratio should be the percentage of normal paycheck the company is willing to deal out (ie. .52 .13 .33)
        if person is not None :
            job = person.get_job()
            if not job.is_wages :
                bonus = job.calculate_bonus(bonus_ratio)
                self.spend_money(bonus)
                person.update_money(bonus)
            return True

        for employee in self.employees :
            job = employee.get_job()
            if not job.is_wages :
                bonus = job.calculate_bonus(bonus_ratio)
                self.spend_money(bonus)
                employee.update_money(bonus)
            else : continue

    def spend_money (self, money) :
        self.annual_spending += money
        self.budget -= money

    def file_taxes (self, tax_ratio, recipient) :
        #tax ratio should be the percentage of annual earnings (ie. .52 .13 .33)
        tax = self.annual_earnings * tax_ratio
        self.spend_money(tax)
        # - - Input Recipient government organization here...

    def shutdown (self) :
        #this is the equivelant of the company shutting down. 
        # - - could implement another company acquiring this one
        for employee in self.employees :
            self.fire_employee(employee)
        self.update_location(None)
        self.budget = 0
        self.divisions = 0

    def promote_employee (self, division_title, employee) :
        # - - employee should choose whether he wants to accept the position
        job = employee.get_job()
        current_rank = job.get_rank()
        if current_rank > 1 :
            for position in self.divisions[division_title] :
                if position.get_rank == (current_rank + 1) :
                    if position.get_remaining_positions() > 0 :
                        job.vacate_position(employee)
                        position.fill_position(employee)
                        return True
                    else : 
                        pass
                        # - - throw error because it tried to promote him without an available position
        else :
            pass
            # - - if is already the highest level in the division, should be promoted to the next division of management

    def demote_employee (self, division_title, employee) :
        job = employee.get_job()
        current_rank = job.get_rank()
        if current_rank < self.get_division_count() :
            for position in self.divisions[division_title] :
                if position.get_rank == (current_rank - 1) :
                    if position.get_remaining_positions() > 0 :
                        job.vacate_position(employee)
                        position.fill_position(employee)
                        return True
                    else : 
                        pass
                        # - - figure out what to do with a demotion for someone whose lower rank job is full up (keep moving down the ladder until there is an open position?)
        else : 
            pass 
            # - - decide on whether to fire them or send them to lower available position.
                    
    
    # retrieve data regarding company

    def get_division_count (self) :
        return len(self.divisions)


# - - need to figure out consulting businesses collaborating with others.










    def tc_work (self, time_used=1) :
        pass