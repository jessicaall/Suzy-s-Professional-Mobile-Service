# view gui, show all jobs V5
#previous and next buttons
from tkinter import *
from functools import partial # To prevent unwanted windows
import math
import tkinter.font as font
from tkinter import ttk

class Show_all:
    def __init__(self, partner):
        #declaring the counter used to iterate through object list
        self.counter = -1

        #used to keep track of the job number in entry frame
        self.job_number = 1
        
        #variable set up
        self.wof_var = StringVar()
        self.wof_var.set(" ")

        #frames used for different info
        self.entry_frame = Frame(root, bg = '#002564')
        self.summary_frame = Frame(root, bg = '#002564')

        #gridding entry frame as it is shown first
        self.entry_frame.grid()

        #font size and colour used throughout program
        entry_font = font.Font(family = 'Verdana', size = 15)
        summary_font = font.Font(family = 'Verdana', size = 17)
        button_font = font.Font(family = 'Verdana', size = 18)
        error_font = font.Font(family = 'Verdana', size = 12)
        help_button_font = font.Font(family = 'Verdana', size = 12)

        #entry frame

        #list containing objects for the customers details
        self.jobs = []

        
        #titles of details for each customer
        self.job_label_summary = Label(self.summary_frame, text = "Job Number:", bg = '#002564', fg = 'white', padx = 10, pady = 10, font = summary_font)
        self.name_label = Label(self.summary_frame, text = "Customer Name:", bg = '#002564', fg = 'white', padx = 10, pady = 10, font = summary_font)
        self.job_charge_label = Label(self.summary_frame, text = "Job Charge ($):", bg = '#002564', fg = 'white', padx = 10, pady = 10, font = summary_font)
        
        self.job_label_summary.grid(row = 1, column = 0, sticky = W)
        self.name_label.grid(row = 2, column = 0, sticky = W)
        self.job_charge_label.grid(row = 3, column = 0, sticky = W)
        
        #details of each customer
        self.job_num_output = Label(self.summary_frame, text = (self.job_number), bg = '#002564', fg = 'white', padx = 10, pady = 10, font = summary_font)
        self.name_output = Label(self.summary_frame, text = " ", bg = '#002564', fg = 'white', padx = 10, pady = 10, font = summary_font)
        self.job_charge_output = Label(self.summary_frame, text = "Not Calculated", bg = '#002564', fg = 'white', padx = 10, pady = 10, font = summary_font)
        
        self.job_num_output.grid(row = 1, column = 1, sticky = W)
        self.name_output.grid(row = 2, column = 1, sticky = W)
        self.job_charge_output.grid(row = 3, column = 1, sticky = W)

        # Previous and next buttons
        self.previous_btn = Button(self.summary_frame, text = "Previous",
                                   command = self.previous_btn, bg = '#002564', fg = '#002564', padx = 10, font = button_font)
        self.next_btn = Button(self.summary_frame, text = "Next",
                               command = self.next_btn, state = DISABLED, bg = '#002564', fg = '#002564', padx = 10, font = button_font)

        self.previous_btn.grid(row = 5, column = 0, sticky = W, pady = 10, padx = 10)
        self.next_btn.grid(row = 5, column = 1, sticky = E, pady = 10, padx = 10)

        #back button
        self.back_btn = Button(self.summary_frame, text = "Back",
                               command = self.back_btn, bg = '#002564', fg = '#002564', padx = 10, font = button_font)
        self.back_btn.grid(row = 6, column = 0, sticky = W, pady = 10, padx = 10)

        #if the user enters only one job both buttons are disabled
        if self.counter <= 0:
            self.next_btn.configure(state = DISABLED)
            self.previous_btn.configure(state = DISABLED)
            

    def show_all(self):
            
        #using summary frame
        self.entry_frame.grid_remove()
        self.summary_frame.grid()

        #use self.counter to display in summary frame as it is access from the self.jobs list
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

        #setting the next button to be disabled when the show all button is clicked
        if self.counter == len(self.jobs)-1:
            self.next_btn.configure(state = DISABLED)


    def previous_btn(self):

        #going to previous customer in object list
        self.counter -=1
        if self.counter == 0:
            self.previous_btn.configure(state = DISABLED)
        self.next_btn.configure(state = NORMAL)

        #easier to change the job number in function rather than when it is initialized
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

    def next_btn(self):

        #going to next customer in object list
        self.counter +=1
        
        #parameters on the buttons
        if self.counter == len(self.jobs)-1:
            self.next_btn.configure(state = DISABLED)
        self.previous_btn.configure(state = NORMAL)

        #easier to change the job number in function rather than when it is initialized
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

    def back_btn(self):

        #frames changed
        self.summary_frame.grid_remove()
        self.entry_frame.grid()



if __name__ == "__main__":
    root = Tk()
    #if the frame is extended the background stays white
    root.config(bg='#002564')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.title("Suzy's Mobile Computer Repairs")
    radiobuttons = Show_all(root)
    root.mainloop()


