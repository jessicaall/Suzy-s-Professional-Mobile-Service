# calculator V2
from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re        

    def job_charge(self, self.distance, self.time, self.wof):

        #constant as the fixed rate could change
        SET_CHARGE = 10
        FIXED_DISTANCE = 5
        WOF_COST = 100
        VIRUS_PROTECTION_COST = 0.8

        #rounding up
        if self.distance % 1 >= 0.5:
            distance_rounded = round(self.distance)
            
        #rounding down
        elif self.distance % 1 < 0.5:
            distance_rounded = round(self.distance)
        
        #if distance is greater than 5km
        if distance_rounded > FIXED_DISTANCE:
            add_on = distance_rounded - 5
            add_on *= 0.5
            SET_CHARGE += add_on

        #time for virus protection
        if self.time != 0:
            SET_CHARGE += self.time * VIRUS_PROTECTION_COST

        #using wof
        if self.wof != "NO":
            SET_CHARGE += WOF_COST

        #formatted job charge to 2 deciaml places for currency
        job_charge_formatted = format(SET_CHARGE, ".2f")
        
        return job_charge_formatted







# main routine
if __name__ == "__main__":

    #Global lists
    job_number = [1, 2, 3]
    customer_name = ['jess', 'lana', 'bob']
    dist_travelled = [6, 5, 3.5]
    virus_protection_mins = [20, 10, 0]
    wof_tune = ['no', 'yes', 'yes']
    job_charge = []
    
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = Calculations(root)
    root.mainloop()

