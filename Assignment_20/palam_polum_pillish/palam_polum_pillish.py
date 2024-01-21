
import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow 
from ui_palam_polum_pillish import Ui_MainWindow 
from functools import partial
  
class Palam_Polum_Pillish(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   
        
        self.front_hand = self.ui.front_hand_btn
        self.back_hand = self.ui.back_hand_btn
        self.win = self.ui.win_btn
        self.computer1_score = self.ui.computer1_score
        self.computer2_score = self.ui.computer2_score
        self.player_score = self.ui.player_score_btn
        self.player_choice = self.ui.player_choice
        self.computer1_choice = self.ui.computer1_choice
        self.computer2_choice = self.ui.computer2_choice
        self.choice = ["🤚🏻" , "🖐🏻"]
        self.computer1_counter = 0 
        self.computer2_counter = 0
        self.player_counter = 0

        self.front_hand.clicked.connect(partial(self.play , "front"))
        self.back_hand.clicked.connect(partial(self.play , "back"))


    def play(self , input):
        global state
        state = input

        if state == "back" :
            self.player_choice.setText("🤚🏻")
        elif state == "front" :
            self.player_choice.setText("🖐🏻")

        computer1_result = self.choice[random.randint(0,1)]
        self.computer1_choice.setText(computer1_result)
        computer2_result = self.choice[random.randint(0,1)]
        self.computer2_choice.setText(computer2_result)

        if (state == "front" and computer1_result == self.choice[0] and computer2_result == self.choice[1]) or (state == "back" and computer1_result == self.choice[1] and computer2_result == self.choice[0]):
                self.player_counter += 1 
                self.computer2_counter +=1
                self.player_score.setText("Player Score:" + str(self.player_counter))     
                self.computer2_score.setText("Computer2 Score:" + str(self.computer2_counter))    
        elif   (state == "front" and computer1_result == self.choice[1] and computer2_result == self.choice[0]) or(state == "back" and computer1_result == self.choice[0] and computer2_result == self.choice[1]) :
                self.player_counter += 1 
                self.computer1_counter +=1
                self.player_score.setText("Player Score :" + str(self.player_counter))     
                self.computer1_score.setText("Computer1 Score :" + str(self.computer1_counter)) 
        elif   (state == "back" and computer1_result == self.choice[1] and computer2_result == self.choice[1] ) or (state == "front" and computer1_result == self.choice[0] and computer2_result == self.choice[0]):
                self.computer2_counter += 1 
                self.computer1_counter +=1
                self.computer2_score.setText("Computer2 Score :" + str(self.computer2_counter))     
                self.computer1_score.setText("Computer1 Score :" + str(self.computer1_counter)) 



        if self.player_counter== 5  :
            self.win.setText("You Won")
        elif self.computer1_counter == 5 :
            self.win.setText("Computer1 Won")
        elif self.computer2_counter == 5 :
            self.win.setText("Computer2 Won")
           

app = QApplication(sys.argv)
main_window = Palam_Polum_Pillish()  
main_window.show()

app.exec()