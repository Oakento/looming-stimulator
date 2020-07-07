from tkinter import *
from utils import degree_to_radius as radius
from utils import get_screen_height, get_stimulator_geometry
from data import get_config_by_config_id
import time


class Stimulator(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.overrideredirect(1)
        self.width, self.height, self.x, self.y = get_stimulator_geometry()
        self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        self.canvas = Canvas(self.master, bg='white')
        
        self.canvas.pack(fill = 'both', expand = True)
        self.canvas.update()
        self.origin_x = int(self.canvas.winfo_width() / 2)
        self.origin_y = int(self.canvas.winfo_height() / 2)
        self.init_canvas()


    def init_canvas(self):
        config = get_config_by_config_id()
        self.min_degree = config.get("min_degree")
        self.max_degree = config.get("max_degree")  
        self.chamber_height = config.get("chamber_height")
        self.time_expand = config.get("time_expand")
        self.time_hold = config.get("time_hold")
        self.time_pause = config.get("time_pause")
        self.repeat = config.get("repeat")
        FLAME_PER_SECOND = 60
        degree_step = ((self.max_degree - self.min_degree) / self.time_expand) / FLAME_PER_SECOND
        screen_height = get_screen_height()
        related = (self.chamber_height * 2 / screen_height) * self.origin_y
        degree = self.min_degree
        self.circle_list = []
        self.canvas.delete('all')
        while abs(degree - self.max_degree) >= 10**(-8) and degree < self.max_degree:
            circle = self.canvas.create_oval(
                self.origin_x - radius(degree, related),
                self.origin_y - radius(degree, related),
                self.origin_x + radius(degree, related),
                self.origin_y + radius(degree, related),
                fill='black'
            )
            self.canvas.itemconfigure(circle, state='hidden')
            self.circle_list.append(circle)
            degree += degree_step
        self.canvas.update()


    def stimulate(self):
        FLAME_PER_SECOND = 60
        self.canvas.itemconfigure(self.circle_list[0], state='normal')
        for i in range(self.repeat):
            expand_begin = time.time()

            for circle in self.circle_list[1:]:
                begin = time.time()
                self.canvas.itemconfigure(circle, state='normal')
                time.sleep(
                    (1 / FLAME_PER_SECOND - time.time() + begin) 
                    if time.time() - begin <= 1 / FLAME_PER_SECOND
                    else 0.0
                )
            
            time.sleep(
                (self.time_hold + self.time_expand - time.time() + expand_begin) 
                if time.time() - expand_begin <= self.time_hold + self.time_expand
                else 0.0
            )

            pause_begin = time.time()
            for circle in self.circle_list[1:]:
                self.canvas.itemconfigure(circle, state='hidden')

            time.sleep(
                (self.time_pause - time.time() + pause_begin) 
                if time.time() - pause_begin <= self.time_pause
                else 0.0
            )


    def close(self):
        self.master.destroy()
