
import arcade
import time
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart


class Game (arcade.Window):
    def __init__(self):
        super().__init__(width= 600, height= 600, title= "Interstaller Game")
        self.background= arcade.load_texture(".\\game.png")
        self.spaceship =Spaceship(self)
        self.enemy_list= []
        self.heart_list= []
        self.collosion= 0
        self.score= 0
        self.game_over= arcade.load_sound(".\\game_over.mp3")
        self.laser = arcade.load_sound(":resources:sounds/laser2.wav",False)
        self.explosion = arcade.load_sound(":resources:sounds/explosion1.wav",False)
        self.second=time.time()
        self.rise_speed= time.time()
        for i in range(3):
            heart= Heart(i)
            self.heart_list.append(heart)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        arcade.draw_text("Score: "+ str(self.score), self.width-103, 15, arcade.color.LIGHT_SALMON_PINK, 15, 12)
        self.spaceship.draw()
        
        for enemy in self.enemy_list:
            enemy.draw()
            
        for bullet in self.spaceship.bullet_list:
            bullet.draw()
        
        for heart in self.heart_list:
            heart.draw()
        
        if len(self.heart_list)== 0 or self.collosion==1:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over",self.width/3.5, self.height/2, arcade.color.TEA_GREEN, 36, 20)
            self.background= arcade.load_texture(":resources:images/backgrounds/stars.png")
            
        
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol== arcade.key.RIGHT or symbol== arcade.key.D:
            self.spaceship.change_x=1
            
        elif symbol== arcade.key.LEFT or symbol== arcade.key.A:
            self.spaceship.change_x=-1
        
        elif symbol== arcade.key.DOWN or symbol== arcade.key.S:
            self.spaceship.change_x= 0

        elif symbol== arcade.key.SPACE or symbol == arcade.key.F :
            self.spaceship.fire()
            arcade.play_sound(self.laser,True)
    
    def on_key_release(self, symbol: int, modifiers: int):
        self.spaceship.change_x= 0
    
    
    def on_update(self, delta_time: float):
        if len(self.heart_list)!=0 and self.collosion==0:    
            for enemy in self.enemy_list:
                if arcade.check_for_collision(self. spaceship, enemy):
                    self.collosion=1
                    self.heart_list.clear()
                    arcade.play_sound(self.game_over,1)
                    
            for enemy in self.enemy_list:    
                for bullet in self.spaceship.bullet_list:
                    if arcade.check_for_collision (enemy, bullet):
                        self.enemy_list.remove(enemy)
                        self.spaceship.bullet_list.remove(bullet)
                        arcade.play_sound(self.explosion,1)
                        self.score +=1
            
            for enemy in self.enemy_list:
                if enemy.center_y < 0:
                    self.enemy_list.remove(enemy)
                    self.heart_list.pop()
                    if len(self.heart_list)==0:
                        arcade.play_sound(self.game_over,1)
         
            self.spaceship.move()
            
            for enemy in self.enemy_list:
                enemy.move()  

            for bullet in self.spaceship.bullet_list:
                bullet.move()  
            
            if time.time()-self.second >= 3:
                self.second=time.time()
                self.newe_nemy=Enemy(self)
                self.enemy_list.append(self.newe_nemy)

            if time.time() - self.rise_speed >= 10:
                self.rise_speed = time.time()
                Enemy(self).rise_speed()
        else:
            self.enemy_list.clear()
            self.spaceship.bullet_list.clear()
            self.spaceship.kill()
    

window= Game()
arcade.run() 
