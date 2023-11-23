import math
import tkinter as tk

class lead_crawler:
    def __init__(self, scene, x, y, a, w, l, mf, mt):
        self.x_position = x
        self.y_position = y
        self.angle = a
        self.width = w
        self.length = l
        self.max_forward_speed = mf/1000
        self.max_turn_speed = mt/1000
        self.forward_speed = 0
        self.turn_speed = 0
        self.outline_color = "black"
        self.fill_color = "green"
        self.control_input = "none"

        # add the object in the scene
        self.coordinates = [
        self.x_position - w/2,      #x1 
        self.y_position - l/2,      #y1 
        self.x_position + w/2,      #x2 
        self.y_position - l/2,      #y2 
        self.x_position + w/2,      #x3 
        self.y_position + l/2,      #y3 
        self.x_position - w/2,      #x4 
        self.y_position + l/2]      #y5 

        print(self.coordinates)

        self.crawler = scene.canvas.create_polygon(
            self.coordinates, outline = "black", fill = "green", width=2)        

    def move_forward(self, scene, dt):
        print()

    def move_backwards(self, scene, dt):
        print()

    def rotate_left(self, scene, dt):
        new_coordinates = []
        delta_angle = dt*self.max_turn_speed
        for z in range(int(len(self.coordinates)/2)):
            x = self.coordinates[z*2]
            y = self.coordinates[z*2+1]
            r = math.sqrt((x - self.x_position)**2 + (y - self.y_position)**2)
            # mistake is below
            q = math.asin((x - self.x_position)/r)
            qn = (q + math.radians(delta_angle)) # the mistake is here
            new_coordinates.append(r*math.cos(qn) + self.x_position)
            new_coordinates.append(r*math.sin(qn) + self.y_position)

        print(new_coordinates)
        self.coordinates = new_coordinates
        scene.canvas.coords(self.crawler, *new_coordinates)

    def rotate_right(self, scene, dt):
        print()

    def update_position(self, scene, dt):
        if self.control_input == "forward":
            self.move_forward(scene, dt)
        elif self.control_input == "back":
            self.move_backwards(scene, dt)
        elif self.control_input == "left":
            self.rotate_left(scene, dt)
        elif self.control_input == "right":
            self.rotate_right(scene, dt)

    def apply_control_input(self, user_input):
        self.control_input = user_input


class follower_crawler:
    def __init__(self, scene, x, y, a, w, l, mf, mt):
        self.x_position = x
        self.y_position = y
        self.angle = a
        self.width = w
        self.length = l
        self.max_forward_speed = mf
        self.max_turn_speed = mt
        self.forward_speed = 0
        self.turn_speed = 0
        self.outline_color = "black"
        self.fill_color = "yellow"

        # add the object in the scene
        x1 = self.x_position - l / 2
        y1 = self.y_position - w / 2
        x2 = self.x_position + l / 2
        y2 = self.y_position + w / 2
        scene.canvas.create_rectangle(x1, y1, x2, y2, outline = "black", fill = "blue", width=2)   

    def update_position(self, dt):
        print()

    def pid_control(self, dt):
        print()
