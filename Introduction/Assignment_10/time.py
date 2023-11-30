
class Time:
    def __init__(self, hour, minute , second ):
    
        self.hour = hour
        self.minute = minute
        self.second = second

    def convert_day_to_sec(self , hour , minute , second) :
        ...

    def convert_sec_to_hour(self, hour , minute , second) :
        ...
    
    def stopwatch(self ,hour,minute,second) :
        ... 
    
    def show(self):
         print(self.hour,":", self.minute,":" ,self.second)
    
current_time = Time( 22 , 22 , 22)
current_time.show()