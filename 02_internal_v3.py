# Internal entry boxes and checking input v1
from tkinter import *
from functools import partial # To prevent unwanted windows
import random
import re

class Start:
    def __init__(self, parent):

        # GUI to get starting balalnce and stakes
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


        # Entry boxes... (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        # job number

        self.job_number_label = Label(self.entry_error_frame, text="Job Number:", justify=LEFT, pady=10, padx=10)
        self.job_number_label.grid(row=1, column=0)
        
        self.job_number_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.job_number_entry.grid(row=1, column=1)


        # customer_name

        self.customer_name_label= Label(self.entry_error_frame, text="Customer Name:", justify=LEFT, pady=10, padx=10)
        self.customer_name_label.grid(row=2, column=0)
        
        self.customer_name_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.customer_name_entry.grid(row=2, column=1)



        # distance

        self.dist_label= Label(self.entry_error_frame, text="Distance Travelled to Customer (Km):", justify=LEFT, pady=10, padx=10)
        self.dist_label.grid(row=3, column=0)
        
        self.dist_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.dist_entry.grid(row=3, column=1)



        # virus

        self.virus_mins_label = Label(self.entry_error_frame, text="Minutes Spent on Virus Protection:", justify=LEFT, pady=10, padx=10)
        self.virus_mins_label.grid(row=4, column=0)
        
        self.virus_mins_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.virus_mins_entry.grid(row=4, column=1)


        # wof and tune

        self.wof_tune_label = Label(self.entry_error_frame, text="WOF and Tune Required? Yes/No:", justify=LEFT, pady=10, padx=10)
        self.wof_tune_label.grid(row=5, column=0)
        
        self.wof_tune_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.wof_tune_entry.grid(row=5, column=1)

        #error label


        self.error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", justify=LEFT,
                                        wrap=275)
        self.error_label.grid(row=6, pady=10, padx=10)


        # add job button

        self.add_job_button = Button(self.entry_error_frame,
                                       font="Arial 14 bold",
                                       text="Add Job",
                                       command=self.check_input)
        self.add_job_button.grid(row=7)

        

    def check_input(self):
        job_no = self.job_number_entry.get()
        name = self.customer_name_entry.get()
        distance = self.dist_entry.get()
        virus = self.virus_mins_entry.get()
        wof = self.wof_tune_entry.get()

        
        
        # Set error background colours (and assume that there are no errors at the start)
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes)
        self.job_number_entry.config(bg="white")
        self.customer_name_entry.config(bg="white")
        self.dist_entry.config(bg="white")
        self.virus_mins_entry.config(bg="white")
        self.wof_tune_entry.config(bg="white")


        try:
            job_no = int(job_no)
            distance = float(distance)
            virus = int(virus)
            wof = wof.lower()

            # Customer name error checking
            # Regular expression to check name is valid
            valid_char = "[A-Za-z]"


            # wof and tune error checking

            if wof != "yes" and wof != "no":
                has_errors == "yes"
                error_feedback_2 = "Only 'Yes' or 'No' for WOF and TUNE"

            # number error checking
            if job_no < 0 or distance < 0 or virus < 0:
                has_errors == "yes"
                error_feedback_3 = "Input cannot be below 0"

            for letter in name:
                if re.match(valid_char, letter):
                    continue

                elif letter == " ":
                    has_errors = "no"

                else:
                    error_feedback_1 = ("There are no {}'s allowed in the customer name".format(letter))
                    has_errors = "yes"
                break

            
          
                
        except ValueError:
            has_errors = "yes"

        if has_errors == "yes":
            self.virus_mins_entry.config(bg="#ffafaf")
            self.dist_entry.config(bg="#ffafaf")
            self.job_number_entry.config(bg="#ffafaf")
            self.wof_tune_entry.config(bg="#ffafaf")
            self.customer_name_entry.config(bg="#ffafaf")

            self.error_label.config(text=error_feedback_1+", "+error_feedback_2+", "+error_feedback_3)

            
            


        else:
            self.error_label.config(text="Job Added", fg="lightGreen", font="Arial 15 italic", justify=CENTER)
            job_number.append(job_no)
            customer_name.append(name)
            dist_travelled.append(distance)
            virus_protection_mins.append(virus)
            wof_tune.append(wof)

            # delete contents so it cannot be entered twice
            self.virus_mins_entry.delete(0, 'end')
            self.dist_entry.delete(0, 'end')
            self.job_number_entry.delete(0, 'end')
            self.wof_tune_entry.delete(0, 'end')
            self.customer_name_entry.delete(0, 'end')




# main routine
if __name__ == "__main__":

    #Global lists
    job_number = []
    customer_name = []
    dist_travelled = []
    virus_protection_mins = []
    wof_tune = []
    
    root = Tk()
    root.title("Mystery Box Game!")
    something = Start(root)
    root.mainloop()

