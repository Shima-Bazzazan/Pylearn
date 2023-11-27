
class Time:
    felag = 0
    def __init__(self, h, m, s):
       
        self.hour = h
        self.minute = m 
        self.second = s
        self.fix()
 

    def show_time (self):
       
        print(self.hour,":",self.minute,":",self.second)

    def sum_time (self, time):
        
        update_second = self.second + time.second
        update_minute = self.minute + time.minute
        update_hour = self.hour + time.hour
        Time.felag = 1
        result = Time(update_hour,  update_minute, update_second)
        return result
    
    def sub_time (self, time):
        
        update_second = self.second - time.second
        update_minute = self.minute - time.minute
        update_hour = self.hour - time.hour
        Time.felag = 1
        result = Time(update_hour, update_minute, update_second)
        return result
    
    def second_to_time (self, second):
        
        update_hour = second // 3600
        temp = second - 3600 * update_hour
        update_minute = temp // 60
        update_second = temp - 60 * update_minute
        result = Time(update_hour, update_minute ,update_second)
        return result
    
    def time_to_second(self, time):
        
        update_second = time.hour * 3600 + time.minute * 60 + time.second
        result = update_second
        return result

    def GMT_to_tehran_time(self, GMT):
        
        tehan_second = 0 + GMT.second
        tehran_minute = 30 + GMT.minute
        tehran_hour = 3 + GMT.hour
        result = Time(tehran_hour, tehran_minute, tehan_second)
        return result

    def fix (self):
        
        if self.second >= 60:
            
            if self.felag == 1:
            
                self.minute+=1
            self.second %=60
            
        if self.minute >=60:
            
            if self.felag == 1:
            
               self.hour +=1
            self.minute %=60

        if self.hour >=24:
            
            self.hour %=24

        if self.second <0:
            
            self.second *=-1
            self.second %=60
            self.second =60 - self.second
            
            if self.felag ==1:
            
                self.minute -=1

        if self.minute <0:
            
            self.minute *=-1
            self.minute %=60
            self.minute = 60 - self.minute
            
            if self.felag == 1:
            
                self.hour -=1

        if self.hour <0:
            
            self.hour*=-1
            self.hour%=24
            self.hour=24-self.hour
            
            if self.hour == 24:
            
                self.hour=0
        
        Time.felag = 0