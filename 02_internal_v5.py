# Internal entry boxes and checking input v5
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

        # View all jobs
        self.view_jobs = Button(self.entry_error_frame,
                                font="Arial 18 bold",
                                command=lambda: Calculations(self))
        self.view_jobs.grid(row=8, column=2, pady=10)

        # Quit button
        self.quit_button = Button(self.entry_error_frame, text="Quit", fg="black",
                                  highlightbackground="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=8, column=0, pady=10)

    def to_quit(self):
        root.destroy()

        

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


class Calculations:
    def __init__(self, partner):

        travel_charge = []
        virus_charge = []
        wof_and_tune_charge = []

        # Travel charge
        for i in dist_travelled:
            round(i)
            if i <= 5 and i > 0:
                travel_cost = 10
                travel_charge.append(travel_cost)

            elif i > 5:
                travel_cost = 10 + (i-5)*.5
                travel_charge.append(travel_cost)

            elif i == 0:
                travel_cost = 0
                travel_charge.append(travel_cost)

        # Virus protection charge
        for v in virus_protection_mins:
            round(v)
            virus_cost = v * 0.8
            virus_charge.append(virus_cost)

        # wof and tune charge
        for w in wof_tune:
            if w == 'yes':
                cost = 100
                wof_and_tune_charge.append(cost)
                
            else:
                cost = 0
                wof_and_tune_charge.append(cost)

        number = 0
        for item in travel_charge:
            total_cost = item + virus_charge[number] + wof_and_tune_charge[number]
            job_charge.append(total_cost)
            number += 1

        print(job_charge)
        View(self)


class View:
    def __init__(self, partner):

        # Sets up child window (ie. help box)
        self.view_box = Toplevel()

        
        # GUI to get starting balalnce and stakes
        self.info_frame = Frame(self.view_box, padx=10, pady=10)
        self.info_frame.grid()

        # Image logo (row 0)
        photo = PhotoImage(file="logo3.png")
        self.logo_label = Label(self.info_frame,
                                image=photo, padx=10, pady=10,
                                justify=CENTER)
        self.logo_label.photo = photo
        self.logo_label.grid(row=0)

        # Input Message (row 1)
        self.view_message = Label(self.info_frame, text="All Jobs",
                                     font="Arial 25 bold ",
                                     justify=CENTER,
                                     padx=40, pady=40,
                                     wrap=275)
        self.view_message.grid(row=1)

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



# main routine
if __name__ == "__main__":

    #Global lists
    job_number = []
    customer_name = []
    dist_travelled = []
    virus_protection_mins = []
    wof_tune = []
    job_charge = []
    
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = Start(root)
    root.mainloop()


