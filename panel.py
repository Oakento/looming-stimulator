from tkinter import *
from stimulator import Stimulator

class Panel(Frame):
    def __init__(self, master, stimulator):
        super().__init__(master)
        self.master = master
        self.stimulator = stimulator
        self.degree_min_label = Label(self.master, text="minimal degree")
        self.degree_min_label.pack()
        self.degree_min_entry = Entry(self.master)
        self.degree_min_entry.pack()
        self.degree_min_entry.insert(0, '2')
        self.degree_max_label = Label(self.master, text="maximal degree")
        self.degree_max_label.pack()
        self.degree_max_entry = Entry(self.master)
        self.degree_max_entry.pack()
        self.degree_max_entry.insert(0, '20')
        self.screen_height_label = Label(self.master, text="chamber height")
        self.screen_height_label.pack()
        self.screen_height_entry = Entry(self.master)
        self.screen_height_entry.pack()
        self.screen_height_entry.insert(0, '19.5')        
        self.chamber_height_label = Label(self.master, text="chamber height")
        self.chamber_height_label.pack()
        self.chamber_height_entry = Entry(self.master)
        self.chamber_height_entry.pack()
        self.chamber_height_entry.insert(0, '30')
        self.time_expand_label = Label(self.master, text="time expand")
        self.time_expand_label.pack()
        self.time_expand_entry = Entry(self.master)
        self.time_expand_entry.pack()
        self.time_expand_entry.insert(0, '0.25')
        self.time_hold_label = Label(self.master, text="time hold")
        self.time_hold_label.pack()
        self.time_hold_entry = Entry(self.master)
        self.time_hold_entry.pack()
        self.time_hold_entry.insert(0, '0.25')
        self.time_pause_label = Label(self.master, text="time pause")
        self.time_pause_label.pack()
        self.time_pause_entry = Entry(self.master)
        self.time_pause_entry.pack()
        self.time_pause_entry.insert(0, '0.5')
        self.repeat_label = Label(self.master, text="repeat")
        self.repeat_label.pack()
        self.repeat_entry = Entry(self.master)
        self.repeat_entry.pack()
        self.repeat_entry.insert(0, '5')
        self.control()
        

    def get_degree_min(self):
        self.degree_min = int(self.degree_min_entry.get())
        return self.degree_min
    
    def get_degree_max(self):
        self.degree_max = int(self.degree_max_entry.get())
        return self.degree_max   

    def get_screen_height(self):
        self.screen_height = float(self.screen_height_entry.get())
        return self.screen_height

    def get_chamber_height(self):
        self.chamber_height = float(self.chamber_height_entry.get())
        return self.chamber_height

    def get_time_expand(self):
        self.time_expand = float(self.time_expand_entry.get())
        return self.time_expand

    def get_time_hold(self):
        self.time_hold = float(self.time_hold_entry.get())
        return self.time_hold

    def get_time_pause(self):
        self.time_pause = float(self.time_pause_entry.get())
        return self.time_pause

    def get_repeat(self):
        self.repeat = int(self.repeat_entry.get())
        return self.repeat


    def control(self):
        self.stimulate = Button(
            self.master, 
            text="STIMULATE",
            command=lambda: self.stimulator.stimulate(
                self.get_degree_min(),
                self.get_degree_max(),
                self.get_screen_height(),
                self.get_chamber_height(),
                self.get_time_expand(),
                self.get_time_hold(),
                self.get_time_pause(),
                self.get_repeat()
            )
        )
        self.quit = Button(self.master, text="QUIT",
                              command=self.stimulator.close)

        self.stimulate.pack(side=BOTTOM)
        self.quit.pack(side=BOTTOM)
            