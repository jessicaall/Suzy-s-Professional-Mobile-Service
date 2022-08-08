# Internal entry boxes and checking input v1
from tkinter import *
from functools import partial # To prevent unwanted windows
import math
import tkinter.font as font
from tkinter import ttk

class Start:
    def __init__(self, parent):
        background = "#E00014"

        # GUI setup
        self.welcome_frame = Frame(padx=10, pady=10, bg=background)
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
                                           font="Arial 19 bold", highlightbackground="#FFFFFF",
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
        Enter_Jobs(self)
        self.welcome_frame.destroy()

#parent class for program
class Enter_Jobs:

    def __init__(self, parent):
        # Background colour is white
        background = "white"

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

        #entry frame

        #list containing objects for the customers details
        self.jobs = []

        background = "white"

        # GUI 
        self.start_frame = Frame(root, padx=10, pady=10, bg="white")
        self.start_frame.grid()

        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.start_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER, bg=background)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Input Message (row 1)
        self.input_message = Label(self.start_frame, text="Please Input...",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275, bg="white")
        self.input_message.grid(row=1)

        #frames used for different info
        self.entry_frame = Frame(self.start_frame, bg=background)

        #gridding entry frame as it is shown first
        self.entry_frame.grid()

        # Entry Frame
        

        #labels of details for each customer
        self.job_label = Label(self.entry_frame, text = "Job Number:", bg = background, fg = 'black', padx = 10, font=entry_font)
        self.job_label.grid(row = 2, column = 0, sticky = W)
        
        self.name_label = Label(self.entry_frame, text = "Customer Name:", bg = background, fg = 'black', padx = 10, font=entry_font)
        self.name_label.grid(row = 3, column = 0, sticky = W)
        
        self.distance_label = Label(self.entry_frame, text = "Distance Travelled (km):", bg = background, fg = 'black', padx = 10, font=entry_font)
        self.distance_label.grid(row = 4, column = 0, sticky = W)
        
        self.time_label = Label(self.entry_frame, text = "Virus Protection Time (min):", bg = background, fg = 'black', padx = 10, font=entry_font)
        self.time_label.grid(row = 5, column = 0, sticky = W)
        
        self.wof_label = Label(self.entry_frame, text = "WOF and Tune:", bg = background, fg = 'black', padx = 10, font=entry_font)
        self.wof_label.grid(row = 6, column = 0, sticky = W)


    
        #entry boxes for details
        self.job_num_label = Label(self.entry_frame, text = self.job_number, bg = background, fg = 'black', font=entry_font)
        self.job_num_label.grid(row = 2, column = 1, sticky = W)
        
        self.name_entry = Entry(self.entry_frame, bg = background, highlightbackground = background, fg = 'black', font=entry_font)
        self.name_entry.grid(row = 3, column = 1, sticky = W)
        
        self.distance_entry = Entry(self.entry_frame, bg = background, highlightbackground = background, fg = 'black', font=entry_font)
        self.distance_entry.grid(row = 4, column = 1, sticky = W)
        
        self.time_entry = Entry(self.entry_frame, bg = background, highlightbackground = background, fg = 'black', font=entry_font)
        self.time_entry.grid(row = 5, column = 1, sticky = W)        
        

        #error messages for entry by users
        self.name_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', padx = 10, font=error_font)
        self.name_entry_error.grid(row = 3, column = 2, sticky = W)
        
        self.distance_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', padx = 10, font=error_font)
        self.distance_entry_error.grid(row = 4, column = 2, sticky = W)
        
        self.time_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', padx = 10, font=error_font)
        self.time_entry_error.grid(row = 5, column = 2, sticky = W)
        
        self.wof_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', padx = 10, font=error_font)
        self.wof_entry_error.grid(row = 6, column = 2, sticky = W)
        
        self.one_service_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', padx = 10, font=error_font)
        self.one_service_error.grid(row = 7, columnspan = 2)

 
        
        #radio buttons for whether user wants wof and tune
        self.yes_wof_radiobutton = Radiobutton(self.entry_frame, variable = self.wof_var, value = 'YES',
                                               anchor = W, text = "YES", bg = background, fg="black", font=entry_font)
        self.no_wof_radiobutton = Radiobutton(self.entry_frame, variable = self.wof_var, value = 'NO',
                                              anchor = E, text = "NO", bg = background, fg="black", font=entry_font)

        #columnspan set to 1 so the radiobuttons are shown next to one another
        self.yes_wof_radiobutton.grid(row = 6, column = 1, sticky = W, columnspan = 1, pady = 10, padx = 10)
        self.no_wof_radiobutton.grid(row = 6, column = 1, sticky = E, padx = 10)
       

        

        #error messages for entry by users
        self.name_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', font=error_font, padx = 10)
        self.name_entry_error.grid(row = 3, column = 2, sticky = W)
        
        self.distance_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', font=error_font, padx = 10)
        self.distance_entry_error.grid(row = 4, column = 2, sticky = W)
        
        self.time_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', font=error_font, padx = 10)
        self.time_entry_error.grid(row = 5, column = 2, sticky = W)
        
        self.wof_entry_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', font=error_font, padx = 10)
        self.wof_entry_error.grid(row = 6, column = 2, sticky = W)
        
        self.one_service_error = Label(self.entry_frame, text = "", bg = background, fg = 'red', font=error_font, padx = 10)
        self.one_service_error.grid(row = 7, columnspan = 2)

        # enter job button

        self.enter_job_button = Button(self.entry_frame, text = "Enter Job",
                                    command = self.enter_job, highlightbackground = "grey", fg = 'Black', font=button_font)
        self.enter_job_button.grid(row = 8, column = 1, pady = 10, padx = 10)


        # button frame
        #frames used for different info
        self.button_frame = Frame(self.entry_frame, bg=background)

        #gridding entry frame as it is shown first
        self.button_frame.grid()


        #buttons to show all jobs
        
        self.show_jobs_button = Button(self.button_frame, text = "Show all Jobs",
                                       command = lambda: self.to_view(self.job_number, self.counter, self.jobs), highlightbackground = '#002564', fg = 'Black', borderwidth = 4,
                                       font=button_font)
        self.show_jobs_button.grid(row = 9, column=1, pady = 10, padx=1)

        # Dismiss Button
        self.quit_button = Button(self.button_frame, text="Quit", fg="Black",
                                  highlightbackground="maroon", borderwidth=4,
                                  command=self.to_quit, font=button_font)
        self.quit_button.grid(row=9, column=0, pady=10, padx=1)

        # Help button
        self.help_button = Button(self.button_frame, text = "Help",
                               command = self.help, highlightbackground = '#002564', fg = '#002564', font=button_font, borderwidth = 4)
        self.help_button.grid(row=9, column = 2, pady = 10, padx = 1)


        #set the show all jobs button initially to disabled as there are no jobs to show
        self.show_jobs_button.configure(state = DISABLED)
        

    def to_quit(self):
        root.destroy()

    def to_view(self, job_number, count, job):
        View_jobs(self, job_number, count, job)

        

    def enter_job(self):
        
        #show all jobs can be clicked as there is at least one job entered
        self.show_jobs_button.configure(state = NORMAL)
            
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
        self.name_entry_box = self.name_entry.get().strip().lower().capitalize()
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
            self.charge = self.job_charge(self.distance, self.time, self.wof)
                
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
            


    def help(self):
        get_help = Help()
        get_help.help_text.configure(text = "Suzy's Mobile Computer Service Help\n"
                                     "\n"
                                     "Please enter the details of the you would like to enter.\n"
                                     "Then press the 'Add Job' button to save the job.\n"
                                     "You can then show all entered jobs by pressing the 'Show All Jobs' button.\n"
                                     "The job must include at least one service, either a WOF and Tune or Virus Protection,\n"
                                     "so please make sure that one of these has been entered or selected.")

    def job_charge(self, distance, time, wof):

        #constant as the fixed rate could change
        SET_CHARGE = 10
        FIXED_DISTANCE = 5
        WOF_COST = 100
        VIRUS_PROTECTION_COST = 0.8

        #rounding up
        if distance % 1 >= 0.5:
            distance_rounded = round(distance)
            
        #rounding down
        elif distance % 1 < 0.5:
            distance_rounded = round(distance)
        
        #if distance is greater than 5km
        if distance_rounded > FIXED_DISTANCE:
            add_on = distance_rounded - 5
            add_on *= 0.5
            SET_CHARGE += add_on

        #time for virus protection
        if time != 0:
            SET_CHARGE += time * VIRUS_PROTECTION_COST

        #using wof
        if wof != "NO":
            SET_CHARGE += WOF_COST

        #formatted job charge to 2 deciaml places for currency
        job_charge_formatted = format(SET_CHARGE, ".2f")
        
        return job_charge_formatted


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

class Help:
    def __init__(self):

        #help button
        help_button_font = font.Font(family = 'Verdana', size = 12)
        background = "#002564"
        self.help_box = Toplevel()
        self.help_box.title("Instructions")
        self.help_frame = Frame(self.help_box, width = 300, height = 200, bg = background)
        self.help_frame.grid()
        heading = Label(self.help_frame, text = " ", justify=LEFT, width = 40, bg = background, wrap = 250)
        heading.grid(column = 0, row = 1)
        self.help_text = Label(self.help_frame, text = " ", justify = LEFT, width = 40, bg = background, wrap = 250, fg = 'white')
        self.help_text.grid(column = 0, row = 1)
        dismiss_btn = Button(self.help_frame, text = "Dismiss", width = 10, highlightbackground = "#002564", command = self.close_help, fg = '#002564')
        dismiss_button['font'] = help_button_font
        dismiss_button.grid(row = 2, pady = 10)

    def close_help(self):
        self.help_box.destroy()
        

class View_jobs:
    def __init__(self, partner, job_num, count, job):

        self.job_number = job_num
        self.counter = count
        self.jobs = job

        #box
        self.view_box = Toplevel()

        
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

        # Input Message (row 1)
        self.message = Label(self.view_frame, text="All Jobs...",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275)
        self.message.grid(row=1)
        

        # GUI to get starting balalnce and stakes
        self.summary_frame = Frame(self.view_frame, padx=10, pady=10)
        self.summary_frame.grid()

        ##### Add fonts
        summary_font = "Verdana 17"
        button_font = "verdana 18"

        #titles of details for each customer
        self.job_label_summary = Label(self.view_frame, text = "Job Number:", bg = '#002564', fg = 'white', padx = 10, pady = 10, font=summary_font)
        self.job_label_summary.grid(row = 1, column = 0, sticky = W)
        
        self.name_label = Label(self.view_frame, text = "Customer Name:", bg = '#002564', fg = 'white', padx = 10, pady = 10, font=summary_font)
        self.name_label.grid(row = 2, column = 0, sticky = W)
        
        self.job_charge_label = Label(self.view_frame, text = "Job Charge ($):", bg = '#002564', fg = 'white', padx = 10, pady = 10, font=summary_font)
        self.job_charge_label.grid(row = 3, column = 0, sticky = W)


        #details of each customer
        self.job_num_output = Label(self.summary_frame, text = (self.job_number),
                                    bg = '#002564', fg = 'white', padx = 10, pady = 10, font=summary_font)
        self.job_num_output.grid(row = 1, column = 1, sticky = W)
        
        self.name_output = Label(self.summary_frame, text = " ", bg = '#002564',
                                 fg = 'white', padx = 10, pady = 10, font=summary_font)
        self.name_output.grid(row = 2, column = 1, sticky = W)
        
        self.job_charge_output = Label(self.summary_frame, text = "Not Calculated",
                                       bg = '#002564', fg = 'white', padx = 10, pady = 10, font=summary_font)
        self.job_charge_output.grid(row = 3, column = 1, sticky = W)
       

        #previous and next buttons
        self.previous_button = Button(self.view_frame, text = "Previous", command = self.previous_btn, bg = '#002564', fg = '#002564', padx = 10)
        self.next_button = Button(self.view_frame, text = "Next", command = self.next_btn, state = DISABLED, bg = '#002564', fg = '#002564', padx = 10)

        self.previous_button['font'] = button_font
        self.next_button['font'] = button_font

        self.previous_button.grid(row = 5, column = 0, sticky = W, pady = 10, padx = 10)
        self.next_button.grid(row = 5, column = 1, sticky = E, pady = 10, padx = 10)
            
        #back button
        self.back_button = Button(self.view_frame, text = "Back", command = self.back_btn, bg = '#002564', fg = '#002564', padx = 10)
        self.back_button['font'] = button_font
        self.back_button.grid(row = 6, column = 0, sticky = W, pady = 10, padx = 10)

        self.show_all()        

        #next and previous buttons set to normal if there are more than one customer 
        if self.counter == len(self.jobs)-1:
            self.next_button.configure(state = DISABLED)
            self.previous_button.configure(state = DISABLED)

        elif len(self.jobs) > 0:
            self.next_button.configure(state = NORMAL)
            self.previous_button.configure(state = NORMAL)
            
        else:
            self.next_button.configure(state = NORMAL)
            self.previous_button.configure(state = NORMAL)

    def show_all(self):

        #use self.counter to display in summary frame as it is access from the self.jobs list
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

        #setting the next button to be disabled when the show all button is clicked if there's only one job
        if self.counter == len(self.jobs)-1:
            self.next_button.configure(state = DISABLED)

        ###### next and previous buttons set to normal if there are more than one customer
        
        #if :
            #self.next_button.configure(state = NORMAL)
            #self.previous_button.configure(state = NORMAL)

        if len(self.jobs) >= 0:
            self.next_button.configure(state = NORMAL)
            self.previous_button.configure(state = NORMAL)
            
    def previous_btn(self):

        #going to previous customer in object list
        self.counter -=1
        print(self.counter)
        if self.counter == 0:
            self.previous_button.configure(state = DISABLED)
        self.next_button.configure(state = NORMAL)

        #easier to change the job number in function rather than when it is initialized
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

    def next_btn(self):

        #going to next customer in object list
        self.counter +=1
        print(self.counter)
        
        #parameters on the buttons
        if self.counter == len(self.jobs)-1:
            self.next_button.configure(state = DISABLED)
        self.previous_button.configure(state = NORMAL)

        #easier to change the job number in function rather than when it is initialized
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)


    def back_btn(self):

        # Go back a window
        self.view_frame.destroy()
        



# main routine
if __name__ == "__main__":
    root = Tk()
    #if the frame is extended the background stays blue
    #root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0, weight=1)
    root.title("Suzy's Professional Mobile Service")
    radiobuttons = Start(root)
    root.mainloop()

##if __name__ == "__main__":
##
##    #Global lists
##    job_number = []
##    customer_name = []
##    dist_travelled = []
##    virus_protection_mins = []
##    wof_tune = []
##    
##    root = Tk()
##    root.title("Suzy's Mobile Service")
##    something = Start(root)
##    root.mainloop()

