import random 
import sys
from PySide6.QtWidgets import QApplication , QMainWindow ,  QMessageBox
from ui_main import Ui_MainWindow

class Guess_Number(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.btn_guess = self.ui.btn_guess
        self.btn_number = self.ui.btn_number
        self.btn_result = self.ui.btn_result
        self.user_number = 0
        self.counter = 0 
        self.computer_number = random.randint(1 , 50)
        self.btn_guess.clicked.connect(self.play)
        
    def play(self):

        self.user_number = int(self.btn_number.toPlainText())
        while (self.computer_number != self.user_number):
            self.counter +=  1
            if self.computer_number > self.user_number :
                self.btn_result.setText(" GO UP!"+"\n"+"("+str(self.counter)+" guess)")
                break
            elif self.computer_number < self.user_number :
                self.btn_result.setText(" GO Down!"+"\n"+"("+str(self.counter)+" guess)")    
                break
        else :
            if self.computer_number == self.user_number :
                message = QMessageBox()
                message.setText("You Win After " + str(self.counter) + " Times")
                message.exec()

app = QApplication(sys.argv)
main_window = Guess_Number()
main_window.show()


app.exec()
