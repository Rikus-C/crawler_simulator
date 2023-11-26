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

        # set crawlers initial rotation
        new_coordinates = []
        delta_angle = self.angle

        for z in range(int(len(self.coordinates)/2)):
            x = self.coordinates[z*2]
            y = self.coordinates[z*2+1]
            r = math.sqrt((x - self.x_position)**2 + (y - self.y_position)**2)
            q = math.degrees(abs(math.acos((x - self.x_position)/r))) 

            if x >= self.x_position and y >= self.y_position:       # quadrant 1
                qn = math.radians(q - delta_angle)
            elif x <= self.x_position and y >= self.y_position:     # quadrant 2
                qn = math.pi - math.radians((180 - q + delta_angle))
            elif x <= self.x_position and y <= self.y_position:     # quadrant 3
                qn = math.pi + math.radians((180 - q - delta_angle))
            else: qn = -math.radians((q + delta_angle))             # quadrant 4

            new_coordinates.append(r*math.cos(qn) + self.x_position)
            new_coordinates.append(r*math.sin(qn) + self.y_position)

        self.crawler = scene.canvas.create_polygon(
            self.coordinates, outline = "black", fill = "green", width=2)

        self.coordinates = new_coordinates
        scene.canvas.coords(self.crawler, *new_coordinates)        

    def move_forward(self, scene, dt):
        delta_forward = dt*self.max_forward_speed

        # calculate angle at which crawler is tilted
        x1 = self.coordinates[2]
        x2 = self.coordinates[4]
        y1 = self.coordinates[3]
        y2 = self.coordinates[5]

        if y1 == y2:
            if x1 > x2:
                for cord in range(len(self.coordinates)):
                    if cord % 2 == 0:
                        self.coordinates[cord] -= delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.y_position -= delta_forward
                return
            else:
                for cord in range(len(self.coordinates)):
                    if cord % 2 == 0:
                        self.coordinates[cord] += delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.y_position += delta_forward
                return

        elif x1 == x2:
            if y1 > y2:
                for cord in range(len(self.coordinates)):
                    if cord % 2 != 0:
                        self.coordinates[cord] += delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.x_position += delta_forward
                return
            else:
                for cord in range(len(self.coordinates)):
                    if cord % 2 != 0:
                        self.coordinates[cord] -= delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.x_position -= delta_forward
                return

        # msitake is somehere here

        q = math.atan((y1-y2)/(x1-x2))
        delta_x = abs(delta_forward*math.cos(q))
        delta_y = abs(delta_forward*math.sin(q))

        for cord in range(len(self.coordinates)):
            if cord % 2 == 0:
                self.coordinates[cord] -= delta_x
            else: self.coordinates[cord] -= delta_y

        # update centre position
        self.x_position -= delta_x
        self.y_position -= delta_y

        scene.canvas.coords(self.crawler, *self.coordinates)

    def move_backwards(self, scene, dt):
        delta_forward = dt*self.max_forward_speed

        # calculate angle at which crawler is tilted
        x1 = self.coordinates[2]
        x2 = self.coordinates[4]
        y1 = self.coordinates[3]
        y2 = self.coordinates[5]

        if y1 == y2:
            if x1 < x2:
                for cord in range(len(self.coordinates)):
                    if cord % 2 == 0:
                        self.coordinates[cord] -= delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.y_position -= delta_forward
                return
            else:
                for cord in range(len(self.coordinates)):
                    if cord % 2 == 0:
                        self.coordinates[cord] += delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.y_position += delta_forward
                return

        elif x1 == x2:
            if y1 < y2:
                for cord in range(len(self.coordinates)):
                    if cord % 2 != 0:
                        self.coordinates[cord] += delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.x_position += delta_forward
                return
            else:
                for cord in range(len(self.coordinates)):
                    if cord % 2 != 0:
                        self.coordinates[cord] -= delta_forward
                scene.canvas.coords(self.crawler, *self.coordinates)
                self.x_position -= delta_forward
                return

        # mistake is somewhere here

        q = math.atan((y1-y2)/(x1-x2))
        delta_x = abs(delta_forward*math.cos(q))
        delta_y = abs(delta_forward*math.sin(q))

        for cord in range(len(self.coordinates)):
            if cord % 2 == 0:
                self.coordinates[cord] += delta_x
            else: self.coordinates[cord] += delta_y

        # update center postion
        self.x_position += delta_x
        self.y_position += delta_y

        scene.canvas.coords(self.crawler, *self.coordinates)

    def rotate_left(self, scene, dt):
        new_coordinates = []
        delta_angle = dt*self.max_turn_speed

        for z in range(int(len(self.coordinates)/2)):
            x = self.coordinates[z*2]
            y = self.coordinates[z*2+1]
            r = math.sqrt((x - self.x_position)**2 + (y - self.y_position)**2)
            q = math.degrees(abs(math.acos((x - self.x_position)/r))) 

            if x >= self.x_position and y >= self.y_position:       # quadrant 1
                qn = math.radians(q - delta_angle)
            elif x <= self.x_position and y >= self.y_position:     # quadrant 2
                qn = math.pi - math.radians((180 - q + delta_angle))
            elif x <= self.x_position and y <= self.y_position:     # quadrant 3
                qn = math.pi + math.radians((180 - q - delta_angle))
            else: qn = -math.radians((q + delta_angle))             # quadrant 4

            new_coordinates.append(r*math.cos(qn) + self.x_position)
            new_coordinates.append(r*math.sin(qn) + self.y_position)

        self.coordinates = new_coordinates
        scene.canvas.coords(self.crawler, *new_coordinates)

    def rotate_right(self, scene, dt):
        new_coordinates = []
        delta_angle = dt*self.max_turn_speed

        for z in range(int(len(self.coordinates)/2)):
            x = self.coordinates[z*2]
            y = self.coordinates[z*2+1]
            r = math.sqrt((x - self.x_position)**2 + (y - self.y_position)**2)
            q = math.degrees(abs(math.acos((x - self.x_position)/r))) 

            if x >= self.x_position and y >= self.y_position:       # quadrant 1
                qn = math.radians(q + delta_angle)
            elif x <= self.x_position and y >= self.y_position:     # quadrant 2
                qn = math.pi - math.radians((180 - q - delta_angle))
            elif x <= self.x_position and y <= self.y_position:     # quadrant 3
                qn = math.pi + math.radians((180 - q + delta_angle))
            else: qn = -math.radians((q - delta_angle))             # quadrant 4

            new_coordinates.append(r*math.cos(qn) + self.x_position)
            new_coordinates.append(r*math.sin(qn) + self.y_position)

        self.coordinates = new_coordinates
        scene.canvas.coords(self.crawler, *new_coordinates)

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
