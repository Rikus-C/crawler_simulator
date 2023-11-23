class lead_crawler:
    def __init__(self, x, y, a, w, l, mf, mt):
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
        self.fill_color = "green"
        self.control_input = "none"

    def move_forward(self, dt):
        print()

    def move_backwards(self, dt):
        print()

    def rotate_left(self, dt):
        print()

    def rotate_right(self, dt):
        print()

    def update_position(self, dt):
        if self.control_input == "forward":
            self.move_forward()
        elif self.control_input == "back":
            self.move_backwards()
        elif self.control_input == "left":
            self.rotate_left()
        elif self.control_input == "right":
            self.rotate_right()

    def apply_control_input(self, user_input):
        self.control_input = user_input


class follower_crawler:
    def __init__(self, x, y, a, w, l, mf, mt):
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

    def update_position(self, dt):
        print()

    def pid_control(self, dt):
        print()
