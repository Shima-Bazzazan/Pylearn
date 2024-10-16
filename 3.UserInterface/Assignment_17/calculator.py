
import math 
from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader

def sum():
    global num1 , num2 , noun
    global operator
    operator = "+"
    num1 = window.box.text()
    window.box.setText("")

def sub():
    global num1, num2 , noun 
    global operator
    operator = str("-")
    num1 = window.box.text()
    window.box.setText("")

def mul():
    global num1, num2 , noun 
    global operator
    operator = "x"
    num1 = window.box.text()
    window.box.setText("")
    
def div():
    global num1, num2 , noun
    global operator
    operator = "÷"
    num1 = window.box.text()
    window.box.setText("")

def ce():
    window.box.setText("")

def sin():
    global num1, noun
    global operator
    operator = "sin"
    num1 = window.box.text()
    noun = math.sin(math.radians(float(num1)))
    window.box.setText(str(noun))

def cos():
    global num1, noun
    global operator
    operator = "cos"
    num1 = window.box.text()
    noun = math.cos(math.radians(float(num1)))
    window.box.setText(str(noun))

def tan():
    global num1, noun
    global operator
    operator = "tan"
    num1 = window.box.text()
    noun = math.tan(math.radians(float(num1)))
    window.box.setText(str(noun))

def cot():
    global num1, noun
    global operator
    operator = "cot"
    num1 = window.box.text()
    if math.tan(math.radians(float(num1)))==0:
        window.box.setText("ERROR")
    else:
        noun = 1/math.tan(math.radians(float(num1)))
        window.box.setText(str(noun))

def log():
    global num1, noun
    global operator
    operator = "log"
    num1 = window.box.text()
    if float(num1)>0:
        noun = math.log(int(num1))
        window.box.setText(str(noun))
    else:
        window.box.setText("ERROR")

def reverse():
    global num1, noun
    global operator
    operator = "1/x"
    num1 = window.box.text()
    if float(num1)==0:
        window.box.setText("ERROR")
    else:
        noun = 1/(float(num1))
        window.box.setText(str(noun))
    
def euler():
    global noun
    noun= math.e
    window.box.setText(str(noun))

def pi():
    global noun
    noun= math.pi
    window.box.setText(str(noun))

def absolute_value():
    global num1, noun
    global operator
    operator= "| x |"
    num1 = window.box.text()
    noun = math.fabs(float(num1))
    window.box.setText(str(noun))

def fact():
    global num1, temp, noun
    global operator
    operator= "n!"
    num1 = window.box.text()
    temp= float(num1)
    num1= int(temp)
    if (temp-num1) ==0 and num1>=0:
        noun = math.factorial(int(num1))
        window.box.setText(str(noun))
    else:    
         window.box.setText("ERROR")

def percent():
    global num1, noun
    global operator
    operator= "%"
    num1 = window.box.text()
    noun = (float(num1))/100
    window.box.setText(str(noun))

def root():
    global num1, noun
    global operator
    operator= "√"
    num1 = window.box.text()
    if float(num1)<0:
        window.box.setText("ERROR")
    else:
        noun = math.sqrt(float(num1))
        window.box.setText(str(noun))

def correspondence():
    global num1,voun
    global operator
    operator= "+/-"
    num1= window.box.text()
    if num1=="" or float(num1)==0:
       window.box.setText("ERROR")
    else: 
        noun= -1 * float(num1)
        window.box.setText(str(noun))

def result(noun):
        if operator == "-" :
            num2 = window.box.text()
            noun = float(num1) - float(num2)
            window.box.setText(str(noun))
        
        elif operator == "+" :
            num2 = window.box.text()
            noun = float(num1) + float(num2)
            window.box.setText(str(noun))
        
        elif operator == "x" :
            num2 = window.box.text()
            noun = float(num1) * float(num2)
            window.box.setText(str(noun))

        elif operator == "÷" :
            num2 = window.box.text()
            if num2 == 0 :
                window.box.setText("ERROR")            
            else:
                noun = float(num1) / float(num2)
                window.box.setText(str(noun)) 

def one():
    num = window.box.text()  
    window.box.setText(num +"1")
def two():
    num = window.box.text()  
    window.box.setText(num +"2")
def three():
    num = window.box.text()  
    window.box.setText(num +"3")    
def four():
    num = window.box.text()  
    window.box.setText(num +"4") 
def five():
    num = window.box.text()  
    window.box.setText(num +"5") 
def six():
    num = window.box.text()  
    window.box.setText(num +"6") 
def seven():
    num = window.box.text()  
    window.box.setText(num +"7") 
def eight():
    num = window.box.text()  
    window.box.setText(num +"8") 
def nine():
    num = window.box.text()  
    window.box.setText(num +"9") 
def zero():
    num = window.box.text()  
    window.box.setText(num +"0") 
def dot():
    num = window.box.text()  
    window.box.setText(num +".") 

loader = QUiLoader()
myapp = QApplication([])

window = loader.load("G:\python_project\pylearn7\sessions\session_17\calculator.ui")
window.show()

window.sum.clicked.connect(sum)
window.sub.clicked.connect(sub)
window.mul.clicked.connect(mul)
window.div.clicked.connect(div)
window.ce.clicked.connect(ce)
window.sin.clicked.connect(sin)
window.cos.clicked.connect(cos)
window.tan.clicked.connect(tan)
window.cot.clicked.connect(cot)
window.log.clicked.connect(log)
window.reverse.clicked.connect(reverse)
window.pi.clicked.connect(pi)
window.euler.clicked.connect(euler)
window.absolute_value.clicked.connect(absolute_value)
window.fact.clicked.connect(fact)
window.percent.clicked.connect(percent)
window.root.clicked.connect(root)
window.correspondence.clicked.connect(correspondence)
window.result.clicked.connect(result)
window.one.clicked.connect(one)
window.two.clicked.connect(two)
window.three.clicked.connect(three)
window.four.clicked.connect(four)
window.five.clicked.connect(five)
window.six.clicked.connect(six)
window.seven.clicked.connect(seven)
window.eight.clicked.connect(eight)
window.nine.clicked.connect(nine)
window.zero.clicked.connect(zero)
window.dot.clicked.connect(dot)

myapp.exec()