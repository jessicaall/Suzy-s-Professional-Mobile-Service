# Show all jobs V2
from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re

class View:
    def __init__(self, partner):
        
##        # disable button
##        partner.enter.config(state=DISABLED)

        # Sets up child window (ie. help box)
        self.view_box = Toplevel()

        # If users press cross at top, closes help and 'releases help button
        # self.view_box.protocol('WM_DELETE_WINDOW', partial(self.close_view, partner))


        
        # GUI 
        self.view_frame = Frame(self.view_box, padx=10, pady=10)
        self.view_frame.grid()

        

        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.view_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Message (row 1)
        self.message = Label(self.view_frame, text="All Jobs",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275)
        self.message.grid(row=1)


        # Info
        self.info_frame = Frame(self.view_frame, width=200)
        self.info_frame.grid()

        stop = "n"
        num = 0

        while stop != "y":

            # job number
            self.job_label = Label(text="Job Number: ")
            self.job_label.grid(row=0, column=0)

            self.job_no_label = Label(self.info_frame, text=job_number[num])
            self.job_no_label.grid(row=0, column=1)

            # customer name
            self.cust_label = Label(text="Customer Name: ")
            self.cust_label.grid(row=1, column=0)

            self.cust_name_label = Label(self.info_frame, text=customer_name[num])
            self.cust_name_label.grid(row=1, column=1)

            # Job Charge
            self.charge_label = Label(text="Job Charge: ")
            self.charge_label.grid(row=2, column=0)

            self.charge_name_label = Label(self.info_frame, text=job_charge[num])
            self.charge_name_label.grid(row=2, column=1)

            # Previous and Next buttons
            self.back_button = Button(self.info_frame, text="Previous", command=self.to_change(-1, num))
            self.back_button.grid(row=3, column=0)

            self.next_button = Button(self.info_frame, text="Next", command= self.to_change(1, num))
            self.next_button.grid(row=3, column=1)


            # Dismiss button
            self.dismiss_button = Button(self.info_frame, text="Dismiss", command=self.stopper(stop))
            self.dismiss_button.grid(row=4, column=0)

            # Export Button
            self.export_button = Button(self.info_frame, text="Export", command=self.stopper(stop))
            self.export_button.grid(row=4, column=1)

            
        

    def to_change(self, number, num):
        num = num + number

        return num

    def stopper(self, stop):
        stop = "y"

        return stop

##    def close_view(self, partner):
##        # Put button back to normal...
##        partner.view_jobs.config(state=NORMAL)
##        self.view_box.destroy()


# main routine
if __name__ == "__main__":

    #Global lists
    job_number = [1, 2, 3]
    customer_name = ['jess', 'lana', 'bob']
    dist_travelled = [2.5, 5, 3]
    virus_protection_mins = [20, 10, 0]
    wof_tune = ['no', 'yes', 'yes']
    job_charge = [26.0, 118.0, 110.0]
    
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = View(root)
    root.mainloop()


