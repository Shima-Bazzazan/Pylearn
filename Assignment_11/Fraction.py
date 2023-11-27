
class Fraction:
    
    def __init__(self,num1,num2):
        self.numerator = num1
        self.denominator = num2

    def sum_fraction (self,fraction):
        
        update_numerator = self.numerator * fraction.denominator + self.denominator * fraction.numerator
        update_denominator = self.denominator * fraction.denominator
        sum = Fraction (update_numerator , update_denominator)
        return sum
    
    def mul_fraction (self,fraction):
        
        update_numerator = fraction.numerator * self.numerator
        update_denominator = fraction.denominator * self.denominator
        mul = Fraction(update_numerator,update_denominator)
        return mul
    
    def sub_fraction (self,fraction):
        
        update_numerator = self.numerator * fraction.denominator - self.denominator * fraction.numerator
        update_denominator = fraction.denominator * self.denominator
        sub = Fraction( update_numerator,update_denominator)
        return sub

    def div_fraction (self, fraction):
        
        update_numerator = fraction.denominator * self.numerator
        update_denominator = fraction.numerator * self.denominator
        div = Fraction(update_numerator, update_denominator)
        result = div.Simplification()
        return result

    def fraction_to_number (self):
        
        result =  self.numerator /self.denominator 
        return result

    def sim_fraction (self):
        
        if (self.denominator < self.numerator):
            j = self.denominator
            i = self.numerator
        else:
            j = self.numerator
            i = self.denominator

        while (j != 0):
            outcome = i % j
            i = j
            j = outcome

        temp= i
        update_numerator =(self.numerator // temp)
        update_denominator =(self.denominator // temp)
        result = Fraction(update_numerator, update_denominator)
        return result
    
    def show_fraction (self):
       
        print(self.numerator, "/" , self.denominator)