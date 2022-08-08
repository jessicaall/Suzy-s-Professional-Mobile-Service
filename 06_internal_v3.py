# Show all jobs V3
from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re

class View:
    def __init__(self, partner):
        print('hello')
        print(job_number[0])

        # Sets up child window (ie. help box)
        self.view_box = Toplevel()

        print('hello2')
        
        # GUI to get starting balalnce and stakes
        self.info_frame = Frame(self.view_box, padx=10, pady=10)
        self.info_frame.grid()

        print('hello3')

        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.info_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        print('hello4')

        # Input Message (row 1)
        self.view_message = Label(self.info_frame, text="All Jobs",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275)
        self.view_message.grid(row=1)

        heading = "Arial 19 bold"
        content = "Arial 19"

        stop = "n"
        num = 0
        
        print('hello5')

        for item in job_charge:
            
            # Starting blance (row 2)
            self.details_frame = Frame(self.info_frame)
            self.details_frame.grid(row=2)

            # Job Number (row 2.0)
            self.job_number_label = Label(self.details_frame,
                                             text="Job Number: ", font=heading,
                                             anchor="e")
            self.job_number_label.grid(row=0, column=0,padx=0)

            self.job_number_value_label = Label(self.details_frame, font=content,
                                                   text="{}".format(job_number[num]),
                                                   anchor="w")
            self.job_number_value_label.grid(row=0, column=1, padx=0)


            # Customer Name (row 2.2)
            self.customer_label = Label(self.details_frame,
                                               text="Customer Name: ", font=heading,
                                               anchor="e")
            self.customer_label.grid(row=1, column=0, padx=0)

            self.customer_value_label = Label(self.details_frame, font=content,
                                                     text="{}".format(customer_name[num]), anchor="w")
            self.customer_value_label.grid(row=1, column=1, padx=0)

            # Job Charge (row 2.2)
            self.charge_label = Label(self.details_frame,
                                               text="Job Charge: ", font=heading,
                                               anchor="e")
            self.charge_label.grid(row=2, column=0, padx=0)

            self.charge_value_label = Label(self.details_frame, font=content,
                                                     text="${}".format(job_charge[num]), anchor="w")
            self.charge_value_label.grid(row=2, column=1, padx=0)

            print('hello6')

            
##            # job number
##            self.job_label = Label(text="Job Number: ")
##            self.job_label.grid(row=0, column=0)
##
##            self.job_no_label = Label(self.info_frame, text=job_number[num])
##            self.job_no_label.grid(row=0, column=1)
##
##            # customer name
##            self.cust_label = Label(text="Customer Name: ")
##            self.cust_label.grid(row=1, column=0)
##
##            self.cust_name_label = Label(self.info_frame, text=customer_name[num])
##            self.cust_name_label.grid(row=1, column=1)
##
##            # Job Charge
##            self.charge_label = Label(text="Job Charge: ")
##            self.charge_label.grid(row=2, column=0)
##
##            self.charge_name_label = Label(self.info_frame, text=job_charge[num])
##            self.charge_name_label.grid(row=2, column=1)

            # Previous and Next buttons
            self.next_button = Button(self.info_frame, text="Next", command = self.next_item(num))
            self.next_button.grid(row=3, column=1)

 
            self.back_button = Button(self.info_frame, text="Previous", command = self.back_item(num))
            self.back_button.grid(row=3, column=0)

            # Dismiss button
            self.dismiss_button = Button(self.info_frame, text="Dismiss", command=self.stopper(stop))
            self.dismiss_button.grid(row=4, column=0)

            # Export Button
            self.export_button = Button(self.info_frame, text="Export", command=self.stopper(stop))
            self.export_button.grid(row=4, column=1)

            if stop == "y":
                break
                

            

            
        

    def next_item(self, num):
        num+=1
        print(num)


    def back_item(self, num):
        num-=1
        print(num)


    def stopper(self, stop):
        stop = "y"
        print(stop)

    
    
        
# main routine
if __name__ == "__main__":

    #Global lists
    job_number = [1, 2, 3]
    customer_name = ['jess', 'lana', 'bob']
    dist_travelled = [2.5, 5, 3]
    virus_protection_mins = [20, 10, 0]
    wof_tune = ['no', 'yes', 'yes']
    job_charge = [26.0, 118.0, 110.0]
    print(job_number[0])
    
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = View(root)
    root.mainloop()



