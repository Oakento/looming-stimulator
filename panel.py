from tkinter.ttk import Frame, LabelFrame, Label, Entry, Button
from stimulator import Stimulator
from data import get_config_by_config_id, update_config_by_config_id
from threading import Thread


class Panel(Frame):
    def __init__(self, master, stimulator):
        super().__init__(master)
        self.master = master
        self.master.title('LS')
        self.stimulator = stimulator
        self.thread = None
        self.master.wm_attributes('-topmost',1)
        # self.master.geometry(get_panel_geometry())
        self.data_lock = True


        # <right_frame>
        self.right_frame = Frame(self.master)
            # <config_frame>
        self.config_frame = LabelFrame(self.right_frame, text="Settings")
                # <label_frame>
        self.label_frame = Frame(self.config_frame)
                    # </label-1>
        self.degree_min_label = Label(self.label_frame, text="minimal degree(°):").pack(expand='yes', fill='x')
                    # </label-2>
        self.degree_max_label = Label(self.label_frame, text="maximal degree(°):").pack(expand='yes', fill='x')
        self.chamber_height_label = Label(self.label_frame, text="chamber height(cm):").pack(expand='yes', fill='x')
        self.time_expand_label = Label(self.label_frame, text="time expand(s):").pack(expand='yes', fill='x')
        self.time_hold_label = Label(self.label_frame, text="time hold(s):").pack(expand='yes', fill='x')
        self.time_pause_label = Label(self.label_frame, text="time pause(s):").pack(expand='yes', fill='x')
        self.repeat_label = Label(self.label_frame, text="repeat times:").pack(expand='yes', fill='x')
                    # ...
                    # </label-7>
        self.label_frame.pack(side='left', expand='yes', fill='y')
                # </label_frame>

                # <entry_frame>
        self.entry_frame = Frame(self.config_frame)
                    # <entry-1>
        self.degree_min_entry = Entry(self.entry_frame, width=15)
        self.degree_min_entry.pack(expand='yes', fill='x')
                    # </entry-1>
                    # <entry-2>
        self.degree_max_entry = Entry(self.entry_frame, width=15)
        self.degree_max_entry.pack(expand='yes', fill='x')
                    # </entry-2>
                    # <entry-3>
        self.chamber_height_entry = Entry(self.entry_frame, width=15)
        self.chamber_height_entry.pack(expand='yes', fill='x')
        self.time_expand_entry = Entry(self.entry_frame, width=15)
        self.time_expand_entry.pack(expand='yes', fill='x')
        self.time_hold_entry = Entry(self.entry_frame, width=15)
        self.time_hold_entry.pack(expand='yes', fill='x')
        self.time_pause_entry = Entry(self.entry_frame, width=15)
        self.time_pause_entry.pack(expand='yes', fill='x')
                    # ...
                    # <entry-7>
        self.repeat_entry = Entry(self.entry_frame, width=15)
        self.repeat_entry.pack(expand='yes', fill='x')
                    # </entry-7>
        self.entry_frame.pack(side='right', expand='yes', fill='y')
                # </entry_frame>
        self.config_frame.pack(side='top', expand='yes', fill='x')
            # </config_frame>
            # <button_frame>
        self.button_frame = Frame(self.right_frame, height=100)
        self.button_frame.pack_propagate(0)
                # <edit_button>
        self.edit_button = Button(self.button_frame, text="EDIT", command=self.edit_params)
        self.edit_button.pack(side='top', fill='both', expand='yes')
                # </edit_button>
                # <stimulate_button>
        self.stimulate_button = Button(self.button_frame, text="STIMULATE",  command=self.stimulate_thread)
        self.stimulate_button.pack(side='bottom', fill='both', expand='yes')
                # </stimulate_button>
        self.button_frame.pack(side='bottom', expand='yes', fill='x')
            # </button_frame>
        self.right_frame.pack(side='right', expand='yes', fill='y')
        # </right_frame>

        self.init_data()
        
        self.master.protocol("WM_DELETE_WINDOW", self.close)

    def init_data(self):
        config = get_config_by_config_id()
        self.degree_min_entry.insert(0, str(config.get("min_degree")))
        self.degree_min_entry.config(state='disabled')
        self.degree_max_entry.insert(0, str(config.get("max_degree")))  
        self.degree_max_entry.config(state='disabled')
        self.chamber_height_entry.insert(0, str(config.get("chamber_height")))
        self.chamber_height_entry.config(state='disabled')
        self.time_expand_entry.insert(0, str(config.get("time_expand")))
        self.time_expand_entry.config(state='disabled')
        self.time_hold_entry.insert(0, str(config.get("time_hold")))
        self.time_hold_entry.config(state='disabled')
        self.time_pause_entry.insert(0, str(config.get("time_pause")))
        self.time_pause_entry.config(state='disabled')
        self.repeat_entry.insert(0, str(config.get("repeat")))
        self.repeat_entry.config(state='disabled')




    def get_degree_min(self):
        self.degree_min = int(self.degree_min_entry.get())
        return self.degree_min
    
    def get_degree_max(self):
        self.degree_max = int(self.degree_max_entry.get())
        return self.degree_max   

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



    def edit_params(self):
        if self.data_lock:
            self.data_lock = False
            for child in self.entry_frame.winfo_children():
                    child.config(state='normal')
            self.edit_button.config(text='SAVE')
        else:
            for child in self.entry_frame.winfo_children():
                    child.config(state='disabled')
                    update_config_by_config_id(
                        self.get_degree_min(), self.get_degree_max(), self.get_chamber_height(), 
                        self.get_time_expand(), self.get_time_hold(), self.get_time_pause(), self.get_repeat()
                    )
            self.edit_button.config(text='EDIT')
            self.data_lock = True


    def stimulate_thread(self):
        if self.thread and self.thread.isAlive():
            return
        stimulate = Thread(
            target=self.stimulator.stimulate,
            args=(
                self.get_degree_min(), self.get_degree_max(), self.get_chamber_height(),
                self.get_time_expand(), self.get_time_hold(), self.get_time_pause(), self.get_repeat()
            )
        )
        self.thread = stimulate
        stimulate.start()


    def close(self):
        self.stimulator.close()
        self.master.destroy()
