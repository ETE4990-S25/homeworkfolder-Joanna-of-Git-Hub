import time

today_str = time.strftime("%Y-%m-%d",time.gmtime()) # figured this out using the Python datasheet

# for keeping track of which months have 30 or 31 days
days_31 = [1,3,5,7,8,10,12]
days_30 = [4,6,9,11]

class Date(object):
    """Keeps track of year, month, day while allowing values to be iterated."""
    
    def __init__(self, year=2011, month=5, day=4):
        """Initializes values, defaulting to our starting day 2011-05-04."""
        self.year = year
        self.month = month
        self.day = day

    def return_date(self):
        """Turning date values into a string. Adds a zero ahead of day/month number if needed."""
        date_str = "0"
        
        if self.day < 10 and self.month >= 10:
            date_str = f"{self.year}-{self.month}-0{self.day}"
        elif self.day < 10 and self.month < 10:
            date_str = f"{self.year}-0{self.month}-0{self.day}"
        elif self.day >= 10 and self.month < 10:
            date_str = f"{self.year}-0{self.month}-{self.day}"
        else:
            date_str = f"{self.year}-{self.month}-{self.day}" 

        return date_str
    
    def increment_date(self):
        """A function to increment the date and returns date in yr-mos-day format as a string."""
        # incrementing dates depending on the month
        if self.month == 12 and self.day == 31:
            self.year += 1
            self.month = 1
            self.day = 1
        
        elif self.day == 31 and self.month in days_31:
            self.month += 1
            self.day = 1
        
        elif self.day == 30 and self.month in days_30:
            self.month += 1
            self.day = 1
        
        elif self.month == 2 and self.day == 28:
            self.month += 1
            self.day = 1
        
        else:
            self.day += 1