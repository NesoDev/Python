from glfw import KEY_SPACE, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_ESCAPE
from pyray import *
import time
init_window(900, 900, "Ejemplo de movimiento")
x = 400
y = 225

condition = -1

while not window_should_close():
    begin_drawing()
    draw_rectangle(x, y, 50, 50, GREEN)
    if is_key_pressed(KEY_UP) or condition == 0:
        condition = 0
        while condition == 0:
            clear_background(BLACK)
            y -= 4
            draw_rectangle(x, y, 50, 50, GREEN)
            end_drawing()
            time.sleep(0.045)
            if is_key_pressed(KEY_UP):
                condition = 0
            if is_key_pressed(KEY_DOWN):
                condition = 1
            if is_key_pressed(KEY_LEFT):
                condition = 2
            if is_key_pressed(KEY_RIGHT):
                condition = 3
            if is_key_pressed(KEY_SPACE):
                condition = 4
            if is_key_pressed(KEY_ESCAPE):
                close_window()
    if is_key_pressed(KEY_DOWN) or condition == 1:
        condition = 1
        while condition == 1:
            clear_background(BLACK)
            y += 4
            draw_rectangle(x, y, 50, 50, GREEN)
            end_drawing()
            time.sleep(0.045)
            if is_key_pressed(KEY_UP):
                condition = 0
            if is_key_pressed(KEY_DOWN):
                condition = 1
            if is_key_pressed(KEY_LEFT):
                condition = 2
            if is_key_pressed(KEY_RIGHT):
                condition = 3
            if is_key_pressed(KEY_SPACE):
                condition = 4
            if is_key_pressed(KEY_ESCAPE):
                close_window()
    if is_key_pressed(KEY_LEFT) or condition == 2:
        condition = 2
        while condition == 2:
            clear_background(BLACK)
            x -= 4
            draw_rectangle(x, y, 50, 50, GREEN)
            end_drawing()
            time.sleep(0.045)
            if is_key_pressed(KEY_UP):
                condition = 0
            if is_key_pressed(KEY_DOWN):
                condition = 1
            if is_key_pressed(KEY_LEFT):
                condition = 2
            if is_key_pressed(KEY_RIGHT):
                condition = 3
            if is_key_pressed(KEY_SPACE):
                condition = 4
            if is_key_pressed(KEY_ESCAPE):
                close_window()
    if is_key_pressed(KEY_RIGHT) or condition == 3:
        condition = 3
        while condition == 3:
            clear_background(BLACK)
            x += 4
            draw_rectangle(x, y, 50, 50, GREEN)
            end_drawing()
            time.sleep(0.045)
            if is_key_pressed(KEY_UP):
                condition = 0
            if is_key_pressed(KEY_DOWN):
                condition = 1
            if is_key_pressed(KEY_LEFT):
                condition = 2
            if is_key_pressed(KEY_RIGHT):
                condition = 3
            if is_key_pressed(KEY_SPACE):
                condition = 4
            if is_key_pressed(KEY_ESCAPE):
                close_window()
    if is_key_pressed(KEY_SPACE) or condition == 4:
        condition = 4
        while condition == 4:
            clear_background(BLACK)
            draw_rectangle(x, y, 50, 50, GREEN)
            end_drawing()
            time.sleep(0.045)
            if is_key_pressed(KEY_UP):
                condition = 0
            if is_key_pressed(KEY_DOWN):
                condition = 1
            if is_key_pressed(KEY_LEFT):
                condition = 2
            if is_key_pressed(KEY_RIGHT):
                condition = 3
            if is_key_pressed(KEY_SPACE):
                condition = 4
            if is_key_pressed(KEY_ESCAPE):
                close_window()
    end_drawing()
close_window()