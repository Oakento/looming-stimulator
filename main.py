from tkinter import Tk
from panel import Panel
from stimulator import Stimulator

root1 = Tk()
root2 = Tk()
stimulator = Stimulator(master=root1)
control_panel = Panel(master=root2, stimulator=stimulator)
root1.mainloop()
root2.mainloop()