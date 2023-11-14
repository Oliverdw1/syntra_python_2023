class Leapyear():
    def __init__(self,year):
        self.year = year


    def set_year(self,year):
        self.year = year
    def is_leap_year(self):
        if self.year >= 1582:
            if self.year%400==0:
                return True
            elif self.year%4==0 and not self.year%100==0:
                return True
            else:
                return False
        else:
            return self.year%4==0
