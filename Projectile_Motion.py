from pyray import *
import math
import time
from raylib import KEY_DOWN, KEY_ENTER, KEY_SPACE, KEY_UP


gravity = 500
coefficient_rest = 2

class Gun:
    def __init__(self, x, y, color, radius, mass, speed, angle, floor):
        self.x0 = x
        self.y0 = y - radius
        self.angle = angle
        self.pos_x = self.x0
        self.pos_y = self.y0
        self.speed_0 = speed
        self.speed_x0 = self.speed_0 * math.cos(math.radians(self.angle))
        self.speed_y0 = self.speed_0 * math.sin(math.radians(self.angle))
        self.speed_x = self.speed_x0
        self.speed_y = self.speed_y0
        self.acceleration_x = 0 #-1 * floor.cof * mass * gravity
        self.acceleration_y = gravity
        self.time_up = [0, self.speed_y0/self.acceleration_y]
        self.time_down = [self.speed_y0/self.acceleration_y, 2*self.speed_y0/self.acceleration_y]
        self.time_fly_middle = self.time_down[1] - self.time_up[0]
        self.y_max = self.y0 - (self.speed_y0**2)/2*self.acceleration_y
        self.color = color
        self.radius = radius
        self.mass = mass
        self.coefficient_rest = coefficient_rest

    def updatePos(self, delta_time):
        self.pos_x = self.x0 + self.speed_x0 * delta_time - 0.5 * self.acceleration_x * (delta_time ** 2)
    
        if 0 <= delta_time <= 2 * self.time_fly_middle:
            self.pos_y = self.y0 - (self.speed_y0 * delta_time - 0.5 * self.acceleration_y * (delta_time ** 2))
        
    def updateSpeed(self, delta_time):
        self.speed_x = self.speed_x0 + self.acceleration_x * delta_time
        self.speed_y = self.speed_y0 - self.acceleration_y * delta_time
        if self.speed_x <= 0:
            self.speed_x = 0

    def updateAngle(self, angle):
        self.angle += angle
        self.pos_x = self.x0
        self.pos_y = self.y0
        self.speed_x0 = self.speed_0 * math.cos(math.radians(self.angle))
        self.speed_y0 = self.speed_0 * math.sin(math.radians(self.angle))
        self.speed_x = self.speed_x0
        self.speed_y = self.speed_y0
        self.time_up = [0, self.speed_y0/self.acceleration_y]
        self.time_down = [self.speed_y0/self.acceleration_y, 2*self.speed_y0/self.acceleration_y]
        self.time_fly_middle = self.time_down[1] - self.time_up[0]
        self.y_max = self.y0 - (self.speed_y0**2)/2*self.acceleration_y

    def detectCollision(self, floor, delta_time):
        return delta_time > 0 and (floor.posY - (self.pos_y + self.radius)) < 0

    def drawGun(self):
        draw_circle(int(self.pos_x + self.radius), int(self.pos_y), int(self.radius), self.color)

class Floor:
    def __init__(self, x, y, width, height, cof, color):
        self.posX = x
        self.posY = y
        self.width = width
        self.height = height
        self.cof = cof
        self.color = color
    def drawFloor(self):
        draw_rectangle(self.posX, self.posY,  self.width, self.height - self.posY, GRAY)

class Window:
    def __init__(self, width, height, title, color):
        self.width = width
        self.height = height
        self.title = title
        self.posX_text = 5
        self.posY_text = 5
        self.font_size = 20
        self.color = color
        self.space = self.font_size * 1.5
        self.fps = 60

    def drawInfo(self, delta_time, gun, floor):

        draw_text("pos_x : " + str(gun.pos_x), self.posX_text, int(self.posY_text + 0 * self.space), self.font_size, WHITE)
        draw_text("pos_y : " + str(int(floor.posY - (gun.pos_y + gun.radius))), self.posX_text, int(self.posY_text + 1 * self.space), self.font_size, WHITE)
        draw_text("speed_x : " + str(gun.speed_x), self.posX_text, int(self.posY_text + 2 * self.space), self.font_size, WHITE)
        draw_text("speed_y : " + str(gun.speed_y), self.posX_text, int(self.posY_text + 3 * self.space), self.font_size, WHITE)
        draw_text("mass : " + str(gun.mass), self.posX_text, int(self.posY_text + 4 * self.space), self.font_size, WHITE)
        draw_text("acceleration_x : " + str(gun.acceleration_x), self.posX_text, int(self.posY_text + 5 * self.space), self.font_size, WHITE)
        draw_text("acceleration_y : " + str(gun.acceleration_y), self.posX_text, int(self.posY_text + 6 * self.space), self.font_size, WHITE)
        draw_text("time of fly : " + str(2 * gun.time_fly_middle), self.posX_text, int(self.posY_text + 7 * self.space), self.font_size, WHITE)
        draw_text("time : "+str(delta_time)+" sec", self.posX_text, int(self.posY_text + 8 * self.space), self.font_size, WHITE)
        draw_text("angle: "+str(gun.angle)+" °", self.posX_text, int(self.posY_text + 9 * self.space), self.font_size, WHITE)
        draw_fps(self.width - 100, 20)


def main():
    window_width = 1920
    window_height = 700
    window = Window(window_width, window_height, "Motion", BLACK)
    floor = Floor(0, 600,  window_width, window_height, 0.05, GRAY)
    gun = Gun(0, floor.posY, WHITE, 20, 10, 700 , 45, floor)
    init_window(window.width, window.height, window.title)
    t0 = 0
    tf = 0
    delta_time = 0
    condition = False
    condition_2 = True
    
    while not window_should_close():
        begin_drawing()
        clear_background(window.color)
        floor.drawFloor()
        
        if is_key_pressed(KEY_SPACE):
            if not condition:
                t0 = time.time()
            condition = True
            condition_2 = False
        elif condition_2:
            if is_key_pressed(KEY_UP) or is_key_down(KEY_UP):
                if gun.angle < 90:
                    gun.updateAngle(0.5)
            if is_key_pressed(KEY_DOWN) or is_key_down(KEY_DOWN):
                if gun.angle > 0:
                    gun.updateAngle(-0.5)
        
        if condition:
            tf = time.time()
            delta_time = tf - t0
            gun.updateSpeed(delta_time)
            gun.updatePos(delta_time)
        window.drawInfo(delta_time, gun, floor)

        if gun.detectCollision(floor, delta_time):
            gun.pos_y = floor.posY - gun.radius
            condition = False
            condition_2 = True
        

        gun.drawGun()
        end_drawing()
        time.sleep(1 / window.fps)

    close_window()

main()
