from pyray import *
import time

from raylib import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_KP_ADD, KEY_KP_SUBTRACT, KEY_PAUSE, KEY_SPACE

init_window(500, 500, "FlappyZoom")

x = 200
y = 120

# definimos las dimensiones de los pixeles
ancho = 20
espacio = 5

def bird(x, y, ancho):
    # fila 1
    draw_rectangle(x, y, 6*ancho, ancho, BLACK)
    # fila 2
    draw_rectangle(x-2*ancho, y+ancho, 2*ancho, ancho, BLACK)
    draw_rectangle(x, y+ancho, 3*ancho, ancho, PINK)
    draw_rectangle(x+3*ancho, y+ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+4*ancho, y+ancho, 2*ancho, ancho, WHITE)
    draw_rectangle(x+6*ancho, y+ancho, 1*ancho, ancho, BLACK)
    # fila 3
    draw_rectangle(x-3*ancho, y+2*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x-2*ancho, y+2*ancho, 2*ancho, ancho, PINK)
    draw_rectangle(x, y+2*ancho, 2*ancho, ancho, YELLOW)
    draw_rectangle(x+2*ancho, y+2*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+3*ancho, y+2*ancho, 4*ancho, ancho, WHITE)
    draw_rectangle(x+7*ancho, y+2*ancho, 1*ancho, ancho, BLACK)
    # fila 4
    draw_rectangle(x-4*ancho, y+3*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x-3*ancho, y+3*ancho, 1*ancho, ancho, PINK)
    draw_rectangle(x-2*ancho, y+3*ancho, 4*ancho, ancho, YELLOW)
    draw_rectangle(x+2*ancho, y+3*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+3*ancho, y+3*ancho, 1*ancho, ancho, SKYBLUE)
    draw_rectangle(x+4*ancho, y+3*ancho, 2*ancho, ancho, WHITE)
    draw_rectangle(x+6*ancho, y+3*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+7*ancho, y+3*ancho, 1*ancho, ancho, WHITE)
    draw_rectangle(x+8*ancho, y+3*ancho, 1*ancho, ancho, BLACK)
    # fila 5
    draw_rectangle(x-5*ancho, y+4*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x-4*ancho, y+4*ancho, 6*ancho, ancho, YELLOW)
    draw_rectangle(x+2*ancho, y+4*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+3*ancho, y+4*ancho, 1*ancho, ancho, SKYBLUE)
    draw_rectangle(x+4*ancho, y+4*ancho, 2*ancho, ancho, WHITE)
    draw_rectangle(x+6*ancho, y+4*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+7*ancho, y+4*ancho, 1*ancho, ancho, WHITE)
    draw_rectangle(x+8*ancho, y+4*ancho, 1*ancho, ancho, BLACK)
    # fila 6
    draw_rectangle(x-5*ancho, y+5*ancho, 5*ancho, ancho, BLACK)
    draw_rectangle(x+0*ancho, y+5*ancho, 3*ancho, ancho, YELLOW)
    draw_rectangle(x+3*ancho, y+5*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+4*ancho, y+5*ancho, 1*ancho, ancho, SKYBLUE)
    draw_rectangle(x+5*ancho, y+5*ancho, 3*ancho, ancho, WHITE)
    draw_rectangle(x+8*ancho, y+5*ancho, 1*ancho, ancho, BLACK)
    # fila 7
    draw_rectangle(x-6*ancho, y+6*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x-5*ancho, y+6*ancho, 5*ancho, ancho, WHITE)
    draw_rectangle(x+0*ancho, y+6*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+1*ancho, y+6*ancho, 3*ancho, ancho, YELLOW)
    draw_rectangle(x+4*ancho, y+6*ancho, 6*ancho, ancho, BLACK)
    # fila 8
    draw_rectangle(x-6*ancho, y+7*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x-5*ancho, y+7*ancho, 1*ancho, ancho, PINK)
    draw_rectangle(x-4*ancho, y+7*ancho, 3*ancho, ancho, WHITE)
    draw_rectangle(x-1*ancho, y+7*ancho, 1*ancho, ancho, PINK)
    draw_rectangle(x+0*ancho, y+7*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+1*ancho, y+7*ancho, 2*ancho, ancho, YELLOW)
    draw_rectangle(x+3*ancho, y+7*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+4*ancho, y+7*ancho, 6*ancho, ancho, RED)
    draw_rectangle(x+10*ancho, y+7*ancho, 1*ancho, ancho, BLACK)
    # fila 9
    draw_rectangle(x-5*ancho, y+8*ancho, 5*ancho, ancho, BLACK)
    draw_rectangle(x+0*ancho, y+8*ancho, 2*ancho, ancho, ORANGE)
    draw_rectangle(x+2*ancho, y+8*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+3*ancho, y+8*ancho, 1*ancho, ancho, RED)
    draw_rectangle(x+4*ancho, y+8*ancho, 6*ancho, ancho, BLACK)
    # fila 10
    draw_rectangle(x-4*ancho, y+9*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x-3*ancho, y+9*ancho, 6*ancho, ancho, ORANGE)
    draw_rectangle(x+3*ancho, y+9*ancho, 1*ancho, ancho, BLACK)
    draw_rectangle(x+4*ancho, y+9*ancho, 5*ancho, ancho, RED)
    draw_rectangle(x+9*ancho, y+9*ancho, 1*ancho, ancho, BLACK)
    # fila 11
    draw_rectangle(x-3*ancho, y+10*ancho, 2*ancho, ancho, BLACK)
    draw_rectangle(x-1*ancho, y+10*ancho, 5*ancho, ancho, ORANGE)
    draw_rectangle(x+4*ancho, y+10*ancho, 5*ancho, ancho, BLACK)
    # fila 12
    draw_rectangle(x-1*ancho, y+11*ancho, 5*ancho, ancho, BLACK)

while not window_should_close():
    clear_background(SKYBLUE)
    draw_text("Pixel = "+str(ancho), 10, 10, 20, BLACK)
    draw_text("Press + or - to zoom", 270, 10, 20, BLACK)
    draw_text("Press left, right, up or down to move the bird", 15, 450, 20, BLACK)
    bird(x, y, ancho)
    if ancho > 1:
        if is_key_pressed(KEY_KP_SUBTRACT):
            ancho -= espacio
    if is_key_pressed(KEY_KP_ADD):
        ancho += espacio
    if is_key_pressed(KEY_UP):
        y -= espacio
    if is_key_pressed(KEY_DOWN):
        y += espacio
    if is_key_pressed(KEY_LEFT):
        x -= espacio
    if is_key_pressed(KEY_RIGHT):
        x += espacio
    end_drawing()
close_window()
