#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

"""
Manager for the watches
"""
import tkinter as tk
from watch import *
from timers import *
import sound
import _thread
from datetime import timedelta

class WatchManager(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.running = False
        self.timer_on = 1
        
        self.watch_1 = Watch(self, 0)
        self.watch_2 = Watch(self, 1, bg="red")
        self.watch_tot = Watch(self, 2, bg="blue")
        
        self.timer_1 = Timer()
        self.timer_2 = Timer()
        self.timer_tot = Timer()
        
        self.sm = sound.SoundManager()
        
        self.update()
        
    def start(self, time1=None, time2=None, timetot=None):
        """Start the timer with the given limits
        
        The time are datetime.timedelta
        """
        
        self.timer_1.limit = time1
        self.timer_2.limit = time2
        self.timer_tot.limit = timetot        
        
        if self.timer_1.limit and self.timer_1.limit > timedelta(seconds=0):
            self.timer_1.play()
        #self.timer_2.play()
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
        ret1 = self.timer_1.update()
        ret2 = self.timer_2.update()
        ret_tot = self.timer_tot.update()
        
        
        # LES SONS
        if ret_tot:
            if self.timer_tot.limit and \
               self.timer_tot.limit >= timedelta(seconds=2):
                _thread.start_new_thread(self.sm.play_end_timer, ())
            self.stop() 
            self.reset()
        if ret1:
            if self.timer_1.limit and \
               self.timer_1.limit >= timedelta(seconds=2):
                _thread.start_new_thread(self.sm.play_end, ())
            self.timer_2.play()
        elif ret2:
            if self.timer_2.limit and \
               self.timer_2.limit >= timedelta(seconds=4):    
                _thread.start_new_thread(self.sm.play_end_pause, ())
            self.timer_1.play()
            
        
        self.watch_1.config(text=self.timer_1.timedelta_total)
        self.watch_2.config(text=self.timer_2.timedelta_total)
        self.watch_tot.config(text=self.timer_tot.timedelta_total)
        
        self.after(50, self.update)
