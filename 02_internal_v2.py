# Suzy's mobile service V1
# Component 2, entry boxes v2, trial 2

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

        # Entry boxes... (row 2)
        self.entry_error_frame = Frame(self.input_frame, width=200)
        self.entry_error_frame.grid(row=2)

        box_label = ["Job Number", "Customer Name", "Distance Travelled to Customer (metres)", "Minutes Spent on Virus Protection",
                     "Was WOF and Tune Required? Yes/No"]
        lists = ["job_number", "customer_name", "dist_travelled", "virus_protection_mins", "wof_tune"]
        job_number = []
        customer_name = []
        dist_travelled = []
        virus_protection_mins = []
        wof_tune = []
        

        for items in len(box_label):
            row_no = 0
            
            self.input_label = Label(self.entry_error_frame, text=items,
                                     font="Arial 18 ",
                                     padx=10, pady=10,
                                     wrap=275)
            self.input_label.grid(row=row_no, column=0)
            self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 18 ", width=10)
            self.start_amount_entry.grid(row=row_no, column=1)
            item = self.start_amount_entry.get()
            if row_no == 0:
                job_number.append(item)

            elif row_no == 1:
                customer_name.append(item)

            elif row_no == 2:
                dist_travelled.append(item)

            
            row_no + 1
            

        
        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Start(root)
    root.mainloop()
