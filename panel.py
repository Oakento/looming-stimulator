from tkinter import *
from stimulator import Stimulator

class Panel(Frame):
    def __init__(self, master, stimulator):
        super().__init__(master)
        self.master = master
        self.stimulator = stimulator
        self.master.wm_attributes('-topmost',1)
        self.master.geometry('350x205')
        self.degree_min_label = Label(self.master, text="minimal degree(°):")
        self.degree_min_label.grid(row=0)
        self.degree_min_entry = Entry(self.master)
        self.degree_min_entry.grid(row=0, column=1)
        self.degree_min_entry.insert(0, '2')
        self.degree_max_label = Label(self.master, text="maximal degree(°):")
        self.degree_max_label.grid(row=1)
        self.degree_max_entry = Entry(self.master)
        self.degree_max_entry.grid(row=1, column=1)
        self.degree_max_entry.insert(0, '20')
        self.screen_height_label = Label(self.master, text="screen height(cm):")
        self.screen_height_label.grid(row=2)
        self.screen_height_entry = Entry(self.master)
        self.screen_height_entry.grid(row=2, column=1)
        self.screen_height_entry.insert(0, '19.5')        
        self.chamber_height_label = Label(self.master, text="chamber height(cm):")
        self.chamber_height_label.grid(row=3)
        self.chamber_height_entry = Entry(self.master)
        self.chamber_height_entry.grid(row=3, column=1)
        self.chamber_height_entry.insert(0, '30')
        self.time_expand_label = Label(self.master, text="time expand(s):")
        self.time_expand_label.grid(row=4)
        self.time_expand_entry = Entry(self.master)
        self.time_expand_entry.grid(row=4, column=1)
        self.time_expand_entry.insert(0, '0.25')
        self.time_hold_label = Label(self.master, text="time hold(s):")
        self.time_hold_label.grid(row=5)
        self.time_hold_entry = Entry(self.master)
        self.time_hold_entry.grid(row=5, column=1)
        self.time_hold_entry.insert(0, '0.25')
        self.time_pause_label = Label(self.master, text="time pause(s):")
        self.time_pause_label.grid(row=6)
        self.time_pause_entry = Entry(self.master)
        self.time_pause_entry.grid(row=6, column=1)
        self.time_pause_entry.insert(0, '0.5')
        self.repeat_label = Label(self.master, text="repeat times:")
        self.repeat_label.grid(row=7)
        self.repeat_entry = Entry(self.master)
        self.repeat_entry.grid(row=7, column=1)
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
        self.fullscreen = Button(self.master, text="FULLSCREEN", pady=5, command=self.stimulator.fullscreen)
        self.stimulate = Button(
            self.master, 
            text="STIMULATE",
            pady=30,
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
        self.quit = Button(self.master, text="STOP", padx=20, pady=5,
                              command=self.stimulator.close)
        self.fullscreen.grid(row=9, column=0)
        self.quit.grid(row=9, column=1)
        self.stimulate.grid(row=2, column=3, rowspan=4)
            