#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Manager for the watches
"""
import tkinter as tk
from watch import *
from timers import *

class WatchManager(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.running = False
        
        self.watch_1 = Watch(self, 0)
        self.watch_2 = Watch(self, 1, bg="red")
        self.watch_tot = Watch(self, 2, bg="blue")
        
        self.timer_1 = Timer()
        self.timer_2 = Timer()
        self.timer_tot = Timer()
        
        
        self.update()
        
    def start(self):
        self.timer_1.play()
        self.timer_2.play()
        self.timer_tot.play()
        self.running = True
        
    def stop(self):
        """Pause the timers"""
        self.timer_1.stop()
        self.timer_2.stop()
        self.timer_tot.stop()
        self.running = False
        
    def reset(self):
        """Reset the timers"""
        if not self.running:
            self.timer_1.reset()
            self.timer_2.reset()
            self.timer_tot.reset()
        
        
    def update(self):
        self.timer_1.update()
        self.timer_2.update()
        self.timer_tot.update()
        
        self.watch_1.config(text=self.timer_1.timedelta_total)
        self.watch_2.config(text=self.timer_2.timedelta_total)
        self.watch_tot.config(text=self.timer_tot.timedelta_total)
        
        self.after(50, self.update)
