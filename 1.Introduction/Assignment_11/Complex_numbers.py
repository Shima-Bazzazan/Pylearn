
class Complex_numbers:
    
    def __init__(self, real, image):
        
        #properties
        self.real= real
        self.image= image

    #methods
    def show_complex (self):
        
        print(self.real,"+","i", self.image)

    def sum_complex (self,complex):
        
        result_real=self.real + complex.real
        result_image=self.image + complex.image
        result = Complex_numbers(result_real, result_image)
        return result

    def sub_complex (self,complex):
        
        result_real = self.real- complex.real
        result_image = self.image - complex.image
        result = Complex_numbers(result_real, result_image)
        return result

    def mul_complex (self, complex):
        result_real=self.real * complex.real - self.image * complex.image
        result_image=self.real * complex.image + self.image * complex.real
        result = Complex_numbers(result_real, result_image)
        return result    