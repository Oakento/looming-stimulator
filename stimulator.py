from tkinter import *
from utils import degree_to_radius as radius
from utils import get_screen_height, get_geometry
from decimal import Decimal
import time


class Stimulator(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.overrideredirect(1)
        self.master.geometry(get_geometry())
        self.canvas = Canvas(self.master, bg='white')
        self.canvas.pack(fill = BOTH, expand = True)
        self.canvas.update()
        self.origin_x = int(self.canvas.winfo_width() / 2)
        self.origin_y = int(self.canvas.winfo_height() / 2)


    def stimulate(self, degree_min, degree_max, chamber_height, time_expand, time_hold, time_pause, repeat):
        FLAME_PER_SECOND = 60
        degree_step = ((degree_max - degree_min) / time_expand) / FLAME_PER_SECOND
        screen_height = get_screen_height()
        related = (chamber_height * 2 / screen_height) * self.origin_y
        self.circle = self.canvas.create_oval(
                self.origin_x - radius(degree_min, related),
                self.origin_y - radius(degree_min, related),
                self.origin_x + radius(degree_min, related),
                self.origin_y + radius(degree_min, related),
                fill='black'
            )
        self.canvas.update()

        for i in range(repeat):
            expand_begin = time.time()
            degree = degree_min
            while abs(degree - degree_max) >= 10**(-8) and degree < degree_max:
                begin = time.time()
                self.canvas.coords(
                    self.circle, 
                    self.origin_x - radius(degree, related),
                    self.origin_y - radius(degree, related),
                    self.origin_x + radius(degree, related),
                    self.origin_y + radius(degree, related)
                )
                self.canvas.update()
                degree += degree_step
                time.sleep(
                    (1 / FLAME_PER_SECOND - time.time() + begin) 
                    if time.time() - begin <= 1 / FLAME_PER_SECOND 
                    else 0.0
                )
            
            time.sleep(
                (time_hold + time_expand - time.time() + expand_begin) 
                if time.time() - expand_begin <= time_hold + time_expand
                else 0.0
            )

            pause_begin = time.time()
            self.canvas.coords(
                self.circle, 
                self.origin_x - radius(degree_min, related),
                self.origin_y - radius(degree_min, related),
                self.origin_x + radius(degree_min, related),
                self.origin_y + radius(degree_min, related)
            )
            self.canvas.update()
            time.sleep(
                (time_pause - time.time() + pause_begin) 
                if time.time() - pause_begin <= time_pause
                else 0.0
            )



    def close(self):
        self.master.destroy()
