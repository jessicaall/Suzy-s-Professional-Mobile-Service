# calculator V1
from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re        

class Calculations:
    def __init__(self, partner):

        travel_charge = []
        virus_charge = []
        wof_and_tune_charge = []

        #constant as the fixed rate could change
        SET_CHARGE = 10
        FIXED_DISTANCE = 5
        WOF_COST = 100
        VIRUS_PROTECTION_COST = 0.8
        CENTS_PER_EXTRA_KM = 0.5
        

        # Travel charge
        for i in dist_travelled:
            round(i)
            if i <= FIXED_DISTANCE and i > 0:
                travel_charge.append(SET_CHARGE)

            elif i > FIXED_DISTANCE:
                travel_cost = SET_CHARGE + (i-FIXED_DISTANCE) * CENTS_PER_EXTRA_KM
                travel_charge.append(travel_cost)

            elif i == 0:
                travel_cost = 0
                travel_charge.append(travel_cost)

        # Virus protection charge
        for v in virus_protection_mins:
            round(v)
            virus_cost = v * VIRUS_PROTECTION_COST
            virus_charge.append(virus_cost)

        # wof and tune charge
        for w in wof_tune:
            if w == 'yes':
                wof_and_tune_charge.append(WOF_COST)
                
            else:
                wof_and_tune_charge.append(0)

        number = 0
        for item in travel_charge:
            total_cost = item + virus_charge[number] + wof_and_tune_charge[number]
            job_charge.append(total_cost)
            number += 1

        print(job_charge)




# main routine
if __name__ == "__main__":

    #Global lists
    job_number = [2]
    customer_name = ['Lana']
    dist_travelled = [30]
    virus_protection_mins = [0]
    wof_tune = ['yes']
    job_charge = []
    
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = Calculations(root)
    root.mainloop()

