# final compiled program v4
# Jessica Allen
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
        help_button_font = font.Font(family="Verdana", size=12)
        background = "#002564"
        self.help_box = Toplevel()
        self.help_box.title("Instructions")
        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        # Image logo (row 0)
        photo = PhotoImage(file="logo9.png")
        self.logo_label = Label(self.help_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER, bg=background)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Message (row 1)
        self.heading = Label(self.help_frame, text="Instructions",
                                     font="Verdana 20 bold ",
                                     justify=CENTER,
                                     padx=40, pady=20,
                                     wrap=275, fg="white", bg=background)
        self.heading.grid(row=1)
        
        self.help_text = Label(self.help_frame, text="Suzy's Mobile Computer Service Help\n"
                               "\n"
                               "Please enter the details of the you would like to enter."
                               "Then press the 'Add Job' button to save the job."
                               "You can then show all entered jobs by pressing the 'Show All Jobs' button."
                               "The job must include at least one service, either a WOF and Tune or Virus Protection,"
                               "so please make sure that one of these has been entered or selected."
                               "No entry box can be blank, if you do not want the virus protection service"
                               "please enter 0 in the entry box."
                               "To close the program, press 'Quit'. If you try to enter an invalid job,"
                               "the show all jobs button will be disabled, please fix any mistakes using the"
                               "prompts and enter a valid job to enable the button again if you wish to see"
                               "the jobs you have entered.",
                               justify=LEFT, width=40,
                               bg=background, wrap=250, fg="white")
        self.help_text.grid(column = 0, row = 2)
        dismiss_button = Button(self.help_frame, text = "Dismiss", width=10,
                                highlightbackground="#002564", command=self.close_help, fg="#002564", font=help_button_font)
        dismiss_button.grid(row=3, pady=10)

    def close_help(self):
        self.help_box.destroy()
        

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
        entry_font = font.Font(family = "Verdana", size=15)
        summary_font = font.Font(family = "Verdana", size=17)
        button_font = font.Font(family = "Verdana", size=18)
        error_font = font.Font(family = "Verdana", size=12)
        help_button_font = font.Font(family = "Verdana", size=12)

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
                                     font="Verdana 20 bold",
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
        self.job_label = Label(self.entry_frame, text = "Job Number:", bg=background, fg=text_colour, padx=10, font=entry_font)
        self.job_label.grid(row=2, column=0, sticky=W)
        
        self.name_label = Label(self.entry_frame, text = "Customer Name:", bg=background, fg=text_colour, padx=10, font=entry_font)
        self.name_label.grid(row=3, column=0, sticky=W)
        
        self.distance_label = Label(self.entry_frame, text = "Distance Travelled to Customer (km):", bg=background, fg=text_colour, padx=10, font=entry_font)
        self.distance_label.grid(row=4, column=0, sticky=W)
        
        self.time_label = Label(self.entry_frame, text = "Time Spent on Virus Protection (min):", bg=background, fg=text_colour, padx=10, font=entry_font)
        self.time_label.grid(row=5, column=0, sticky=W)
        
        self.wof_label = Label(self.entry_frame, text = "WOF and Tune:", bg=background, fg=text_colour, padx=10, font=entry_font)
        self.wof_label.grid(row=6, column=0, sticky=W)

        #entry boxes for details
        self.job_num_label = Label(self.entry_frame, text = self.job_number, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.job_num_label.grid(row=2, column=1, sticky=W)
        
        self.name_entry = Entry(self.entry_frame, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.name_entry.grid(row=3, column=1, sticky=W)
        
        self.distance_entry = Entry(self.entry_frame, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.distance_entry.grid(row=4, column=1, sticky=W)
        
        self.time_entry = Entry(self.entry_frame, bg=background, highlightbackground=background, fg=text_colour, font=entry_font)
        self.time_entry.grid(row=5, column=1, sticky=W)

        #error messages for entry by users
        self.name_entry_error = Label(self.entry_frame, text = "", bg=background, fg="red", padx=10, font=error_font)
        self.name_entry_error.grid(row=3, column=2, sticky=W)
        
        self.distance_entry_error = Label(self.entry_frame, text = "", bg=background, fg="red", padx=10, font=error_font)
        self.distance_entry_error.grid(row=4, column=2, sticky=W)
        
        self.time_entry_error = Label(self.entry_frame, text = "", bg=background, fg="red", padx=10, font=error_font)
        self.time_entry_error.grid(row=5, column=2, sticky=W)
        
        self.wof_entry_error = Label(self.entry_frame, text = "", bg=background, fg = 'red', padx=10, font=error_font)
        self.wof_entry_error.grid(row=6, column=2, sticky=W)
        
        self.one_service_error = Label(self.entry_frame, text = "", bg=background, fg="red", padx=10, font=error_font)
        self.one_service_error.grid(row=7, column=0, padx=10)
        
        #radio buttons for whether user wants wof and tune
        self.yes_wof_radiobutton = Radiobutton(self.entry_frame, variable = self.wof_var, value = "YES", anchor=W, text="YES",
                                               bg=background, fg=text_colour, font=entry_font)
        self.yes_wof_radiobutton.grid(row=6, column=1, sticky=W, columnspan=1, pady=10, padx=10)
        
        self.no_wof_radiobutton = Radiobutton(self.entry_frame, variable = self.wof_var, value ="'NO", anchor=E, text="NO",
                                              bg=background, fg=text_colour, font=entry_font)
        self.no_wof_radiobutton.grid(row=6, column=1, sticky=E, padx=10)


        #buttons to enter a job and show all jobs
        self.enter_job_btn = Button(self.entry_frame, text = "Enter Job", command = self.enter_job, highlightbackground=background, fg=text_colour, font=button_font,
                                    borderwidth=2)
        self.enter_job_btn.grid(row=7, column=1, sticky=E, pady=10, padx=10)

        # bottom buttons frame
        self.button_frame = Frame(root, bg=background)
        self.button_frame.grid()
        
        self.show_jobs_btn = Button(self.button_frame, text = "Show all Jobs", command = self.show_all, highlightbackground="#002564", fg=text_colour, borderwidth=2,
                                    font=button_font)
        self.show_jobs_btn.grid(row=9, column=1, pady=10, padx=10, sticky=W)
        
        self.help_btn = Button(self.button_frame, text = "Help", command = self.help, highlightbackground="lightGrey", fg=text_colour, font=button_font,
                               borderwidth=2)
        self.help_btn.grid(row=9, column=2, sticky=E, pady=10, padx=10)

        self.quit_button = Button(self.button_frame, text="Quit", command=self.quit, borderwidth=2, highlightbackground="maroon", fg=text_colour, font=button_font)
        self.quit_button.grid(row=9, column=0, pady=10, padx=10, sticky=W)


        #set the show all jobs button initially to disabled as there are no jobs to show
        self.show_jobs_btn.configure(state = DISABLED)
        

        
        #summary frame

        #Suzys logo image
        self.logo_img_summary = PhotoImage(file = "logo3.png")

        #showing logo image
        self.logo = Label(self.summary_frame, image = self.logo_img_summary, padx = 10, pady = 10, bg=background)
        self.logo.grid(columnspan=2)

        #titles of details for each customer
        self.job_label_summary = Label(self.summary_frame, text = "Job Number:", bg=background, fg=text_colour, padx=10, pady=10, font=summary_font)
        self.job_label_summary.grid(row=1, column=0, sticky=W)
        
        self.name_label = Label(self.summary_frame, text = "Customer Name:", bg=background, fg=text_colour, padx=10, pady=10, font=summary_font)
        self.name_label.grid(row=2, column=0, sticky=W)
        
        self.job_charge_label = Label(self.summary_frame, text = "Job Charge ($):", bg=background, fg=text_colour, padx=10, pady=10, font=summary_font)
        self.job_charge_label.grid(row=3, column=0, sticky=W)
        
        
        #details of each customer
        self.job_num_output = Label(self.summary_frame, text = (self.job_number), bg=background, fg=text_colour, padx=10, pady=10, font=summary_font)
        self.job_num_output.grid(row=1, column=1, sticky=W)
        
        self.name_output = Label(self.summary_frame, text = " ", bg=background, fg=text_colour, padx=10, pady=10, font=summary_font)
        self.name_output.grid(row=2, column=1, sticky=W)
        
        self.job_charge_output = Label(self.summary_frame, text = "Not Calculated", bg=background, fg=text_colour, padx=10, pady=10, font=summary_font)
        self.job_charge_output.grid(row=3, column=1, sticky=W)
         

        #previous and next buttons
        self.previous_btn = Button(self.summary_frame, text = "Previous", command = self.previous_btn, highlightbackground=background, fg=text_colour, padx=10,
                                   font=button_font)
        self.previous_btn.grid(row=5, column=0, sticky=W, pady=10, padx=10)
        
        self.next_btn = Button(self.summary_frame, text = "Next", command = self.next_btn, state = DISABLED, highlightbackground=background, fg=text_colour, padx=10,
                               font=button_font)
        self.next_btn.grid(row=5, column=1, sticky=E, pady=10, padx=10)
            
        #back button
        self.back_btn = Button(self.summary_frame, text = "Back", command = self.back_btn, highlightbackground=background, fg=text_colour, padx=10, font=button_font,
                               width=45)
        self.back_btn.grid(row=6, columnspan=3, sticky=S, pady=10, padx=10)


        #if the user enters only one job both buttons are disabled
        if self.counter <= 0:
            self.next_btn.configure(state = DISABLED)
            self.previous_btn.configure(state = DISABLED)

    def enter_job(self):

        #next and previous buttons set to normal if there are more than one customer
        if self.counter <= -1:
            self.next_btn.configure(state = DISABLED)
            self.previous_btn.configure(state = DISABLED)
        else:
            self.next_btn.configure(state = NORMAL)
            self.previous_btn.configure(state = NORMAL)
            
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

            #show all jobs can be clicked as there is at least one job entered
            self.show_jobs_btn.configure(state = NORMAL)
            
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
            
        if error == False:
            #show all jobs cannot be clicked if the job entry is invalid. 
            self.show_jobs_btn.configure(state = DISABLED)
            

    def show_all(self):
            
        #using summary frame
        self.entry_frame.grid_remove()
        self.heading_frame.grid_remove()
        self.button_frame.grid_remove()
        self.summary_frame.grid()

        #use self.counter to display in summary frame as it is access from the self.jobs list
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

        #setting the next button to be disabled when the show all button is clicked
        if self.counter == len(self.jobs)-1:
            self.next_btn.configure(state = DISABLED)

    def job_charge(self):

        #constant as the fixed rate could change
        SET_CHARGE = 10
        FIXED_DISTANCE = 5
        WOF_COST = 100
        VIRUS_PROTECTION_COST = 0.8

        #rounding up distance
        if self.distance_entry_box % 1 >= 0.5:
            distance_rounded = math.ceil(self.distance)
            
        #rounding down distance
        elif self.distance_entry_box % 1 < 0.5:
            distance_rounded = math.floor(self.distance)
        
        
        #if distance is greater than 5km
        if distance_rounded > FIXED_DISTANCE:
            add_on = distance_rounded - 5
            add_on *= 0.5
            SET_CHARGE += add_on

        #time for virus protection
        if self.time != 0:
            SET_CHARGE += self.time_entry_box * VIRUS_PROTECTION_COST

        #using wof
        if self.wof != "NO":
            SET_CHARGE += WOF_COST

        #formatted job charge to 2 deciaml places for currency
        job_charge_formatted = format(SET_CHARGE, ".2f")
        
        return job_charge_formatted

    def previous_btn(self):

        #going to previous customer in object list
        self.counter -=1
        if self.counter == 0:
            self.previous_btn.configure(state = DISABLED)
        self.next_btn.configure(state = NORMAL)

        #easier to change the job number in function rather than when it is initialised
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

        #easier to change the job number in function rather than when it is initialised
        self.job_num_output.configure(text = self.jobs[self.counter].job)
        self.name_output.configure(text = self.jobs[self.counter].name)
        self.job_charge_output.configure(text = self.jobs[self.counter].charge)

    def back_btn(self):

        #frames changed
        self.summary_frame.grid_remove()
        self.entry_frame.grid()
        self.heading_frame.grid()
        self.button_frame.grid()

    def help(self):
        get_help = Help()
        
    def quit(self):
        root.destroy()
    
        

if __name__ == "__main__":
    root = Tk()
    #if the frame is extended the background stays blue (stack overflow tip - no noted creator)
    root.config(bg="white")
    root.title("Suzy's Mobile Computer Repairs")
    radiobuttons = Start(root)
    root.mainloop()
