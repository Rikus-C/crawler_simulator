import tkinter as tk
from crawlers import lead_crawler
from crawlers import follower_crawler

class crawler_simuloator_app:
    def __init__(self, master):
        self.master = master
        master.title("Crawler Control Simulator")

        self.canvas = tk.Canvas(master, width = 1000, height=1000)
        self.canvas.pack()

        # Bind arrow key events to the user_inputs method
        self.canvas.bind("<Up>", self.user_inputs)
        self.canvas.bind("<Down>", self.user_inputs)
        self.canvas.bind("<Left>", self.user_inputs)
        self.canvas.bind("<Right>", self.user_inputs)
        self.canvas.bind("<space>", self.user_inputs)

        # list off all crawlers present in simulation
        self.lead_crawler = None
        self.follower_crawlers = []
        self.delta_t = 20 # milliseconds

        # Set the focus to the canvas so that it can receive keyboard events
        self.canvas.focus_set()

    def run_simulation(self):
        self.lead_crawler.update_position(self, self.delta_t)
        
        for crawler in self.follower_crawlers:
            crawler.update_position(self, self.delta_t)

    def start_simulation(self):
        # Call the update_simulation method after the specified simulation_rate
        self.run_simulation()
        self.master.after(self.delta_t, self.start_simulation)

    def user_inputs(self, event):
        key = event.keysym
        if key == "Up":
            self.lead_crawler.apply_control_input("forward")
        elif key == "Down":
            self.lead_crawler.apply_control_input("back")
        elif key == "Left":
            self.lead_crawler.apply_control_input("left")
        elif key == "Right":
            self.lead_crawler.apply_control_input("right")
        elif key == "space":
            self.lead_crawler.apply_control_input("none")

    def add_follower_crawler(self, crawler):
        self.follower_crawlers.append(crawler)

    def add_lead_crawler(self, crawler):
        self.lead_crawler = crawler

def main():
    root = tk.Tk()
    scene = crawler_simuloator_app(root)

    # define crawlers to simulation
    lead = lead_crawler(scene, 500, 500, 0, 100, 200, 10, 5)
    # follow_1 = follower_crawler(scene, 500, 600, 0, 200, 200, 10, 10)

    # add crawlers to simulation
    scene.add_lead_crawler(lead)
    # scene.add_follower_crawler(follow_1)

    # if (len(scene.follower_crawlers) < 1):
    #     print("No crawlers in scene to simulate")
    #     return

    scene.start_simulation()
    root.mainloop()

if __name__ == "__main__":
    main()
