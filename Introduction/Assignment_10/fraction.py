
class Fraction :
    
    def __init__(self, numerator , denominator):
        self.num1 = numerator 
        self.num2 = denominator 
        self.operator ="/"


    def divison(self , num1 , num2) : 
        ...

    def makhraj_moshtarak(self , num1 , num2):
        ...

    def simplify(self , num1 , num2):
        ...

    def multiply(self , operand_1 , operand_2):
        ...

    def add(self , operand_1 , operand_2):
        ...

    def show(self):
         print(self.num1, self.operator ,self.num2)


fraction=Fraction(13,66)
fraction.show()