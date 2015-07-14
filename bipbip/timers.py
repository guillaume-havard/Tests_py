from tkinter import *
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
        
    def pause(self):
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
