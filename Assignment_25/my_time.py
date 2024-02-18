
class MyTime :
    def __init__(self , hour , minute , second) :
        self.hour = int(hour)
        self.minute = int(minute ) 
        self.second = int(second)

    def plus(self):
        self.second += 1
        if self.second >= 60 :
            self.minute += 1
            self.second -= 60

        if self.minute >= 60 :
            self.hour += 1
            self.minute -= 60

        if self.hour >= 24 :
            self.hour = 0
            self.minute = 0 
            self.second = 0
            
    def minus(self):
            if self.second > 0 :
                self.second -= 1
            if self.second == 0 and self.minute > 0 :
                self.minute -= 1
                self.second += 59
            if self.second == 0 and self.minute == 0 and self.hour >0:
                self.hour -= 1
                self.second += 59
                self.minute +=59

