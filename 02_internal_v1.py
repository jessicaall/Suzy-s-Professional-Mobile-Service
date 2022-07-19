# Suzy's mobile service V2
# Component 2, entry boxes v1, trial 1

from tkinter import *
from functools import partial # To prevent unwanted windows

class Start:
    def __init__(self, parent):

        background = "#FFFFFF"

        # GUI setup
        self.welcome_frame = Frame(padx=10, pady=10, bg=background, width=300)
        self.welcome_frame.grid()

        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.welcome_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER, bg=background)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Welcome Message (row 1)
        self.welcome_message = Label(self.welcome_frame, text="Welcome!",
                                     font="Arial 30 bold italic",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275,
                                     bg=background)
        self.welcome_message.grid(row=1)

        # Enter New Job Button (row 3)
        self.enter_new_job_button = Button(self.welcome_frame, text="Enter A New Job",
                                           width=30, height=2,
                                           padx=13, pady=13,
                                           font="Arial 19 bold", highlightbackground="#000000",
                                           command=lambda: self.to_input())
        self.enter_new_job_button.grid(row=3)

        # Close button
        self.close_button = Button(self.welcome_frame, text="Close", fg="black",
                                  highlightbackground="#000000", font="Arial 15 bold", width=20,
                                  command=self.to_close, padx=20, pady=10)
        self.close_button.grid(row=6, pady=10)

    def to_close(self):
        root.destroy()

    def to_input(self):
        Input(self)
        self.welcome_frame.destroy()


class Input:
    def __init__(self, partner):

        # GUI setup
        self.input_frame = Frame(padx=10, pady=10)
        self.input_frame.grid()
        
        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.input_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Input Message (row 1)
        self.input_message = Label(self.input_frame, text="Please Input...",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275)
        self.input_message.grid(row=1)

        # Input Lists
        job_number = []
        customer_name = []
        dist_travelled = []
        virus_protection_mins = []
        wof_tune = []

        # Entry boxes... (row 2)
        self.entry_error_frame = Frame(self.input_frame, width=200)
        self.entry_error_frame.grid(row=2)

        
        self.job_no_label = Label(self.entry_error_frame, text="Job Number:",
                                     font="Arial 18 ",
                                     padx=10, pady=10,
                                     wrap=275)
        self.job_no_label.grid(row=1, column=0)
        self.job_number_entry = Entry(self.entry_error_frame, font="Arial 18 ", width=10)
        self.job_number_entry.grid(row=1, column=1)

        self.customer_name_label = Label(self.entry_error_frame, text="Customer Name: ",
                                     font="Arial 18 ",
                                     padx=10, pady=10,
                                     wrap=275)
        self.customer_name_label.grid(row=2, column=0)
        self.customer_name_entry = Entry(self.entry_error_frame, font="Arial 18 ", width=10)
        self.customer_name_entry.grid(row=2, column=1)


        self.dist_label = Label(self.entry_error_frame, text="Distance Travelled to the Customer: ",
                                     font="Arial 18 ",
                                     padx=10, pady=10,
                                     wrap=275)
        self.dist_label.grid(row=3, column=0)
        self.dist_entry = Entry(self.entry_error_frame, font="Arial 18 ", width=10)
        self.dist_entry.grid(row=3, column=1)
        


        self.mins_virus_label = Label(self.entry_error_frame, text="Minutes Spent on Virus Protection: ",
                                     font="Arial 18 ",
                                     padx=10, pady=10,
                                     wrap=275)
        self.mins_virus_label.grid(row=4, column=0)
        self.mins_virus_entry = Entry(self.entry_error_frame, font="Arial 18 ", width=10)
        self.mins_virus_entry.grid(row=4, column=1)
        

        self.wof_tune_label = Label(self.entry_error_frame,
                                 text="Was WOF and Tune Required?"
                                 "Yes/No",
                                     font="Arial 18 ",
                                     padx=10, pady=10,
                                     wrap=275)
        self.wof_tune_label.grid(row=5, column=0)
        self.wof_tune_entry = Entry(self.entry_error_frame, font="Arial 18 ", width=10)
        self.wof_tune_entry.grid(row=5, column=1)

        self.add_job_button = Button(self.entry_error_frame,
                                       font="Arial 14 bold",
                                       text="Add Job",
                                       command=self.add_info_to_lists(job_number, customer_name, dist_travelled, virus_protection_mins, wof_tune))
        self.add_job_button.grid(row=6)

    def add_info_to_lists(self, job_number, customer_name, dist_travelled, virus_protection_mins, wof_tune):
        job=self.job_number_entry.get()
        dist_travelled.append(self.dist_entry.get())
        virus_protection_mins.append(self.mins_virus_entry.get())
        customer_name.append(self.customer_name_entry.get())
        wof_tune.append(self.wof_tune_entry.get())

        print(job)

    def to_quit(self):
        root.destroy()

        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Start(root)
    root.mainloop()
