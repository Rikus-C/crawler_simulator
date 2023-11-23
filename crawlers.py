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

    def move_forward():
        print()

    def move_backwards():
        print()

    def rotate_left():
        print()

    def rotate_right():
        print()

    def update_position(self, dt):
        print()

    def apply_control_input(self, user_input):
        print(user_input)


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
