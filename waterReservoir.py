class WaterReservoir: 
    """
    Class water reservoir. Flow rate is in liters per minute. 
    """
    def __init__(self, max_level, min_level, flow_rate = 50, level = 0): 
        self.level = level
        self.max_level = max_level 
        self.min_level = min_level 
        self.flow_rate = flow_rate 

    def fill(self, amount): 
        """
        Fill the reservoir with the given amount (liters).
        Returns the actual added amount (limited by max_level).
        Raises ValueError if amount <= 0.
        """
        if amount <= 0: 
            raise ValueError(f"Amount must be greater than zero") 
        if self.level + amount > self.max_level:
            added = self.max_level - self.level 
            self.level = self.max_level 
            return added
        else: 
            self.level += amount 
            return amount 
        
    def drain(self, amount): 
        """
        Drain the reservoir with the given amount (liters).
        Returns the actual drained amount (limited by min_level).
        Raises ValueError if amount <= 0.
        """
        if amount <= 0: 
            raise ValueError(f"Amount must be greater than zero")
        if self.level - amount < self.min_level: 
            drained = self.level - self.min_level
            self.level = self.min_level
            return drained
        else: 
            self.level -= amount 
            return amount 
        
    def get_level(self): 
        return self.level 
    
    def time_to_fill(self, amount): 
        added = self.fill(amount)
        time = added / self.flow_rate
        return time 

    def time_to_drain(self, amount): 
        drained = self.drain(amount) 
        time = drained / self.flow_rate 
        return time

        
    
    