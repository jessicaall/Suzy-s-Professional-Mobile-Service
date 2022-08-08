# Internal help gui component 5 v1
# Jessica Allen
from tkinter import *
from functools import partial # To prevent unwanted windows
import tkinter.font as font
from tkinter import ttk

class Start:
    def __init__(self, partner):

        background="white"
        text_colour="black"

        button_font = font.Font(family = 'Verdana', size = 18)

        # bottom buttons frame
        self.button_frame = Frame(root, bg=background)
        self.button_frame.grid()
        
        self.help_btn = Button(self.button_frame, text = "Help", command = self.help, highlightbackground="lightGrey", fg=text_colour, font=button_font,
                               borderwidth=2)
        self.help_btn.grid(row=9, column=2, sticky = E, pady = 10, padx = 10)

    def help(self):
        get_help = Help()

class Help:
    def __init__(self):

        #help button
        help_button_font = font.Font(family = 'Verdana', size = 12)
        background = "#002564"
        self.help_box = Toplevel()
        self.help_box.title("Instructions")
        self.help_frame = Frame(self.help_box, width = 300, height = 200,
                                bg = background)
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
                               "so please make sure that one of these has been entered or selected.",
                               justify = LEFT, width = 40,
                               bg = background, wrap = 250, fg = 'white')
        self.help_text.grid(column = 0, row = 2)
        dismiss_button = Button(self.help_frame, text = "Dismiss", width = 10,
                                highlightbackground = "#002564", command = self.close_help, fg = '#002564')
        dismiss_button['font'] = help_button_font
        dismiss_button.grid(row = 3, pady = 10)

    def close_help(self):
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    #if the frame is extended the background stays blue
    root.config(bg="white")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.title("Suzy's Mobile Computer Repairs")
    radiobuttons = Start(root)
    root.mainloop()
