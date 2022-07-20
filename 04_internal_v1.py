from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re

class Calculations:
    def __init__(self, partner):

        travel_charge = []
        virus_charge = []
        wof_and_tune_charge = []

        # Travel charge
        for i in dist_travelled:
            round(i)
            if i <= 5 and i > 0:
                travel_cost = 10
                travel_charge.append(travel_cost)

            elif i > 5:
                travel_cost = 10 + (i-5)*.5
                travel_charge.append(travel_cost)

            elif i == 0:
                travel_cost = 0
                travel_charge.append(travel_cost)

        # Virus protection charge
        for v in virus_protection_mins:
            round(v)
            virus_cost = v * 0.8
            virus_charge.append(virus_cost)

        # wof and tune charge
        for w in wof_tune:
            if w == 'yes':
                cost = 100
                wof_and_tune_charge.append(cost)
                
            else:
                cost = 0
                wof_and_tune_charge.append(cost)

        number = 0
        for item in travel_charge:
            total_cost = item + virus_charge[number] + wof_and_tune_charge[number]
            job_charge.append(total_cost)
            number += 1

        print(job_charge)
        
        
        







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

