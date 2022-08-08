# Internal entry boxes and checking input v1
from tkinter import *
from functools import partial # To prevent unwanted windows
import math
import tkinter.font as font
from tkinter import ttk



#support class
class Job:
    #used to save the customer details in object list
    def __init__(self, job, name, distance, time, wof, charge):
        self.job = job
        self.name = name
        self.distance = distance
        self.time = time
        self.wof = wof
        self.charge = charge


#parent class for program
class Enter_Jobs:

    def __init__(self, parent):

        # background = white
        background = "white"
        text_colour = "black"

        #declaring the counter used to iterate through object list
        self.counter = -1

        #used to keep track of the job number in entry frame
        self.job_number = 1
        
        #variable set up
        self.wof_var = StringVar()
        self.wof_var.set(" ")

        #font size and colour used throughout program
        entry_font = font.Font(family = 'Verdana', size = 15)
        summary_font = font.Font(family = 'Verdana', size = 17)
        button_font = font.Font(family = 'Verdana', size = 18)
        error_font = font.Font(family = 'Verdana', size = 12)
        help_button_font = font.Font(family = 'Verdana', size = 12)

        #heading frame
        # GUI 
        self.heading_frame = Frame(root, padx=10, pady=10, bg="white")
        self.heading_frame.grid()

        #list containing objects for the customers details
        self.jobs = []

        #showing logo image

        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.heading_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER, bg=background)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Input Message (row 1)
        self.input_message = Label(self.heading_frame, text="Please Input...",
                                     font="Verdana 20 bold ",
                                     justify=CENTER,
                                     padx=20, pady=20,
                                     wrap=275, bg=background)
        self.input_message.grid(row=1)

        # entry frame
        
        #frames used for different info
        self.entry_frame = Frame(root, self.heading_frame, bg=background)
        #gridding entry frame as it is shown first
        self.entry_frame.grid()

        # Summary frame set up, will grid when use needed 
        self.summary_frame = Frame(root, bg=background)

        #labels of details for each customer
        self.job_label = Label(self.entry_frame, text = "Job Number:", bg=background, fg=text_colour, padx = 10, font=entry_font)
        self.job_label.grid(row = 2, column = 0, sticky = W)
        
        self.name_label = Label(self.entry_frame, text = "Customer Name:", bg=background, fg=text_colour, padx = 10, font=entry_font)
        self.name_label.grid(row = 3, column = 0, sticky = W)
        
        self.distance_label = Label(self.entry_frame, text = "Distance Travelled (km):", bg=background, fg=text_colour, padx = 10, font=entry_font)
        self.distance_label.grid(row = 4, column = 0, sticky = W)
        
        self.time_label = Label(self.entry_frame, text = "Virus Protection Time (min):", bg=background, fg=text_colour, padx = 10, font=entry_font)
        self.time_label.grid(row = 5, column = 0, sticky = W)
        
        self.wof_label = Label(self.entry_frame, text = "WOF and Tune:", bg=background, fg=text_colour, padx = 10, font=entry_font)
        self.wof_label.grid(row = 6, column = 0, sticky = W)

        #entry boxes for details
        self.job_num_label = Label(self.entry_frame, text = self.job_number, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.job_num_label.grid(row = 2, column = 1, sticky = W)
        
        self.name_entry = Entry(self.entry_frame, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.name_entry.grid(row = 3, column = 1, sticky = W)
        
        self.distance_entry = Entry(self.entry_frame, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.distance_entry.grid(row = 4, column = 1, sticky = W)
        
        self.time_entry = Entry(self.entry_frame, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.time_entry.grid(row = 5, column = 1, sticky = W)

        #error messages for entry by users
        self.name_entry_error = Label(self.entry_frame, text = "", bg=background, fg = 'red', padx = 10, font=error_font)
        self.name_entry_error.grid(row = 3, column = 2, sticky = W)
        
        self.distance_entry_error = Label(self.entry_frame, text = "", bg=background, fg = 'red', padx = 10, font=error_font)
        self.distance_entry_error.grid(row = 4, column = 2, sticky = W)
        
        self.time_entry_error = Label(self.entry_frame, text = "", bg=background, fg = 'red', padx = 10, font=error_font)
        self.time_entry_error.grid(row = 5, column = 2, sticky = W)
        
        self.wof_entry_error = Label(self.entry_frame, text = "", bg=background, fg = 'red', padx = 10, font=error_font)
        self.wof_entry_error.grid(row = 6, column = 2, sticky = W)
        
        self.one_service_error = Label(self.entry_frame, text = "", bg=background, fg = 'red', padx = 10, font=error_font)
        self.one_service_error.grid(row = 7, column=0, padx=10)
        
        #radio buttons for whether user wants wof and tune
        self.yes_wof_radiobutton = Radiobutton(self.entry_frame, variable = self.wof_var, value = 'YES', anchor = W, text = "YES",
                                               bg=background, fg=text_colour, font=entry_font)
        self.yes_wof_radiobutton.grid(row = 6, column = 1, sticky = W, columnspan = 1, pady = 10, padx = 10)
        
        self.no_wof_radiobutton = Radiobutton(self.entry_frame, variable = self.wof_var, value = 'NO', anchor = E, text = "NO",
                                              bg=background, fg=text_colour, font=entry_font)
        self.no_wof_radiobutton.grid(row = 6, column = 1, sticky = E, padx = 10)


        #buttons to enter a job and show all jobs
        self.enter_job_btn = Button(self.entry_frame, text = "Enter Job", command = self.enter_job, highlightbackground=background, fg=text_colour, font=button_font,
                                    borderwidth=2)
        self.enter_job_btn.grid(row = 7, column=1, sticky = E, pady=10, padx=10)

        # bottom buttons frame
        self.button_frame = Frame(root, bg=background)
        self.button_frame.grid()
        
        self.show_jobs_btn = Button(self.button_frame, text = "Show all Jobs", #command = self.show_all,
                                    highlightbackground="#002564", fg=text_colour, borderwidth=2,
                                    font=button_font)
        self.show_jobs_btn.grid(row=9, column=1, pady=10, padx=10, sticky=W)
        
        self.help_btn = Button(self.button_frame, text = "Help", #command = self.help,
                               highlightbackground="lightGrey", fg=text_colour, font=button_font,
                               borderwidth=2)
        self.help_btn.grid(row=9, column=2, sticky = E, pady = 10, padx = 10)

        self.quit_button = Button(self.button_frame, text="Dismiss", command=self.quit, borderwidth=2, highlightbackground="maroon", fg=text_colour, font=button_font)
        self.quit_button.grid(row=9, column=0, pady=10, padx=10, sticky=W)


        #set the show all jobs button initially to disabled as there are no jobs to show
        self.show_jobs_btn.configure(state = DISABLED)
        

        
        

    def enter_job(self):
        
        #show all jobs can be clicked as there is at least one job entered
        self.show_jobs_btn.configure(state = NORMAL)        
            
        #set the error messages to only show once exceptional input occurs
        self.name_entry_error.configure(text = "")
        self.distance_entry_error.configure(text = "")
        self.time_entry_error.configure(text = "")
        self.wof_entry_error.configure(text = "")
        self.one_service_error.configure(text = "")

        #used to check if the user entered an invalid detail
        error = True

        #distance
        try:
            #set the distance as a variable so it is fixed and remembered
            self.distance_entry_box = float(self.distance_entry.get())
            if self.distance_entry_box <= 0:
                self.distance_entry_error.configure(text = "Enter a positive number")
                #change boolean to false as an invalid error arose
                error = False
        #if a number is not entered    
        except ValueError:
            self.distance_entry_error.configure(text = "Enter a positive number")
            error = False

        #time
        try:
            self.time_entry_box = float(self.time_entry.get())
            if self.time_entry_box < 0:
                self.time_entry_error.configure(text = "Enter a positive number")
                error = False
            else:
                #checking whether a service has be chosen, if not reentry
                if self.wof_var.get() == "NO" and self.time_entry_box == 0.0:
                    self.wof_entry_error.configure(text = "")
                    self.time_entry_error.configure(text = "")
                    self.one_service_error.configure(text = "Must provide at least one service")
                    error = False
        except ValueError:
            self.time_entry_error.configure(text = "Enter a positive number")
            error = False

        #customer name
        #error only occurs if no name is entered
        self.name_entry_box = self.name_entry.get().strip().lower().title()
        if self.name_entry_box == "":
            self.name_entry_error.configure(text = "Enter customer name")
            error = False

        #wof
        #error only occurs if no radiobutton is selected
        if self.wof_var.get() == " ":
            self.wof_entry_error.configure(text = "Check YES or NO")
            error = False

        #if there are no errors in entry
        if error == True:
            
            #go to next job when the enter job button is clicked
            self.counter +=1
            
            #setting the instances to what the user enters into the entry boxes
            self.job = self.job_number
            self.name = self.name_entry_box
            self.distance = self.distance_entry_box #set as variable that was set earlier
            self.time = self.time_entry_box
            self.wof = self.wof_var.get()
            self.charge = self.job_charge()
                
            #instance variables are added to the class
            customer = Job(self.job, self.name, self.distance, self.time, self.wof, self.charge)
            self.jobs.append(customer)

            #setting entry boxes to default for next customer entry
            self.name_entry.delete(0, END)
            self.distance_entry.delete(0, END)
            self.time_entry.delete(0, END)
            self.wof_var.set(" ")

            #change the job number
            self.job_number +=1
            self.job_num_label.configure(text = self.job_number)            


    def quit(self):
        root.destroy()
    
        

if __name__ == "__main__":
    root = Tk()
    #if the frame is extended the background stays blue
    root.config(bg="white")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.title("Suzy's Mobile Computer Repairs")
    radiobuttons = Enter_Jobs(root)
    root.mainloop()
