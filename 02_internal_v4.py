# Internal entry boxes v4
from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re


class Start:
    def __init__(self, parent):

        # GUI 
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()
        
        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.start_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Input Message (row 1)
        self.input_message = Label(self.start_frame, text="Please Input...",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275)
        self.input_message.grid(row=1)

        # entry boxes

        self.job_number_text = Label(self.start_frame, text = "Job Number:",)
        self.job_number_text.grid(row=2, column=0)
        self.customer_name_text = Label(self.start_frame, text = "Customer Name:",)
        self.customer_name_text.grid(row=3, column=0)
        self.dist_text = Label(self.start_frame, text="Distance Travelled to Customer (Km):")
        self.dist_text.grid(row=4, column=0)
        self.virus_text = Label(self.start_frame, text="Minutes spent on Virus Protection:")
        self.virus_text.grid(row=5, column=0)
        self.wof_tune_text = Label(self.start_frame, text="General WOF and TUNE? Yes/No:")
        self.wof_tune_text.grid(row=6, column=0)
       

        job_number = IntVar()
        customer_name = StringVar()
        dist_travelled = IntVar()
        virus_mins = IntVar()
        wof_tune = StringVar()

        self.job_number_entry = Entry(self.start_frame, textvariable = job_number)
        self.job_number_entry.grid(row=2, column=1)
        self.customer_name_entry = Entry(self.start_frame, textvariable=customer_name)
        self.customer_name_entry.grid(row=3, column=1)
        self.dist_entry = Entry(self.start_frame, textvariable=dist_travelled)
        self.dist_entry.grid(row=4, column=1)
        self.virus_entry = Entry(self.start_frame, textvariable=virus_mins)
        self.virus_entry.grid(row=5, column=1)
        self.wof_tune_entry = Entry(self.start_frame, textvariable=wof_tune)
        self.wof_tune_text.grid(row=6, column=1)

        add_job = Button(self.start_frame, text = "Add Job", width="30", height="2", command=save_info)
        add_job.grid(row=7)
        

    def save_info(self):
        job_info = job_number_entry.get()
        cust_info = customer_name_entry.get()
        dist_info = dist_entry.get()
        virus_info = virus_entry.get()
        wof_info = wof_tune_entry.get()

        job_number.append(job_info)
        customer_name.append(cust_info)
        dist_travelled.append(dist_info)
        virus_protection_mins.append(virus_info)
        wof_tune.append(wof_info)
        
        
        


# main routine
if __name__ == "__main__":

    #Global lists
    job_number = []
    customer_name = []
    dist_travelled = []
    virus_protection_mins = []
    wof_tune = []


    root = Tk()
    root.geometry('500x500')
    root.title("Suzy's Mobile Service")
    something = Start(root)
    root.mainloop()


    
