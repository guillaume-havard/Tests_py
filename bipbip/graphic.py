#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Graphical interface


3 times (with names)
Timers (periods, total time)
Buttons (play/pause, reset)

"""
import tkinter as tk
from watch import *

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.grid()
        
        self.frame_watches = tk.Frame(self)
        self.frame_watches.grid(row=0)
        
        self.timer_1 = None 
        self.timer_2 = None 
        self.timer_tot = None 
                
    def add_watches(self):
        """Put the three timer on display"""
        
        self.timer_1 = Watch(self.frame_watches,
                                  "time 1", 0)
        self.timer_2 = Watch(self.frame_watches,
                                  "time 2", 1)
        self.timer_tot = Watch(self.frame_watches,
                                  "time Total", 2)



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.add_watches()
    import pdb; pdb.set_trace()
    app.mainloop()

    """
    # test du timer avec tkinter
    debut = datetime.now()
    print(debut)

    root = Tk()
    clock = Label(root, font=('times', 20, 'bold'), bg='green')
    clock.pack(fill=BOTH, expand=1)
     
    def tick():
        time2 = str(datetime.now() - debut)
        
        clock.config(text=time2)
        
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(50, tick)
     
    tick()
    root.mainloop(  )
    """
