class Date :
    
    def __init__(self , year , month , day):

        self.day = day
        self.month = month
        self.year = year

    def age_calc(self , year , month , day) :
        ...

    def calendar(self ,year , month , day):
        ...

    def show(self):
        print(self.year,"/", self.month,"/" ,self.day)
    
current_date = Date( 1401 , 1 , 1)
current_date.show()