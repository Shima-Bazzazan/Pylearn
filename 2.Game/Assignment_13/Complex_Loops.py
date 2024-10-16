
import arcade

center_x = 310
center_y = 100
counter_1 = 0
counter_2 = 0

arcade.Window(400,400,"Complex Loops-Box")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for i in range(10):
    if i % 2 == 0:
        counter_2 = 0
        for j in range(10):
            if j % 2 == 0:
                arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.BLUE, 45)
                counter_2 += 25
            elif j % 2 == 1 :
                arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.RED, 45)
                counter_2 += 25
    elif i % 2 == 1:
        counter_2 = 0
        for j in range(10):
            if j % 2 == 0:
                arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.RED, 45)
                counter_2 += 25
            elif j % 2 == 1 :
                arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.BLUE, 45)
                counter_2 += 25
    counter_1 += 25

arcade.finish_render()
arcade.run()