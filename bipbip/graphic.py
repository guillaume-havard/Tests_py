#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Graphical interface


3 times (with names)
Timers (periods, total time)
Buttons (play/pause, reset)

"""
import tkinter as tk
from watchinit import *
from watchmanager import *

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.timer_init_1 = None 
        self.timer_init_2 = None 
        self.timer_init_tot = None 
        self.timer_1 = None 
        self.timer_2 = None 
        self.timer_tot = None 
        self.launched = False # It is launched or still at 00:00
        self.running = False # It is running or in suspend 
        
        self.grid()
        
        self.frame_watches_init = tk.Frame(self)
        self.frame_watches_init.grid(row=0, columnspan=3)
        
        self.add_watches_init()   
        
        
        # Real timers
        self.watches_manager = WatchManager(self)
        self.watches_manager.grid(row=1, columnspan=3)
        
        # Buttons
        self.ss_button = tk.Button(self, text="Start",
                                   command=self.start_stop)
        self.ss_button.grid(row=2, column=0)                                   
        self.reset_button = tk.Button(self, text="Reset",
                                      command=self.reset_timers)
        self.reset_button.grid(row=2, column=1)                                  
        # Keyboard shortcut
        
                 
    def add_watches_init(self):
        """Put the three timer on display"""
        
        self.timer_init_1 = WatchInit(self.frame_watches_init,
                                  "time 1", 0)
        self.timer_init_2 = WatchInit(self.frame_watches_init,
                                  "time 2", 1)
        self.timer_init_tot = WatchInit(self.frame_watches_init,
                                  "time Total", 2)

    def start_stop(self):
        """Start or stop the differents timers.
        
        First start : launch the timers with the time on the watches.
        Stop : pause the timers
        start : unpause the timers
        """
        if self.watches_manager.running:
            self.watches_manager.stop()
            self.ss_button["text"] = "Start"
        else:
            self.watches_manager.start()
            self.ss_button["text"] = "Stop"
        
    def reset_timers(self):
        """Reset the timers."""
        self.watches_manager.reset()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    
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
