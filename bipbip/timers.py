#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import time

import datetime as dtime

"""
This module manage the timers

# TODO : error
# TODO : limitation avec 'limit'

"""
# Ne pas garder la date de début et de fin, fair des ajouts de delta.
# Sinon ne fonctionnera pas en cas de pause.

class Timer:
    """
    Manage a timer !
    
    The timer can be set to stop automaticaly when a limit is reach
    Can be launched, paused ...
    
    TODO : Pour le moment il faut l'updater, voir ce que je veux
    """
    
    def __init__(self, limit=None):

        if isinstance(limit, dtime.time ):
            self.limit = limit
        elif not limit:
            self.limit = None
        else:
            self.limit = None
            #raise error
            
        print("limit : ", limit)
        
        self.reset()
        
    def play(self):
        """Launch the timer"""
        if not self.playing:
            self.playing = True            
            self.time_tmp = dtime.datetime.now()
        
    def stop(self):
        """Pause the timer"""
        if self.playing:
            self.update()
            self.playing = False
        
    def update(self):
        """update the timer to have the current elapsed time"""
        
        if self.playing:
            self.timedelta_total += dtime.datetime.now() - self.time_tmp
            self.time_tmp = dtime.datetime.now()
        
        # TODO : limitation avec 'limit'
        
    def reset(self):
        """Reset the timer 
        
        The timer is paused
        """
        self.playing = False
        self.time_tmp = dtime.time(0, 0, 0)
        self.timedelta_total = dtime.timedelta(0)
    




#

if __name__ == "__main__":

    t1 = Timer()
    
    t2 = Timer(dtime.time(0, 1, 0))
    
    t1.play()
    
    time.sleep(1)
    t1.update()
    print(t1.timedelta_total)   
    #import pdb; pdb.set_trace()
    
    time.sleep(1)
    t1.update()
    t1.pause()
    print(t1.timedelta_total)
    #import pdb; pdb.set_trace()
    
    t1.reset()
    t1.play()
    time.sleep(1)
    t1.pause()
    time.sleep(3)
    t1.update()
    print(t1.timedelta_total)
    #import pdb; pdb.set_trace()
    
    
    
    

