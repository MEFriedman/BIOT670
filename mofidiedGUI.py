#Use tkinter to create GUI in Python

import tkinter as tk
window= tk.Tk()

import ttips

border_effects = { #creates dictioary whose keys are name of relief effects
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

"""
for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack() (add different effects to text)
"""


from tkinter import *
from tkinter import messagebox


C = Canvas(window, bg="blue", height=400, width=200)
filename = PhotoImage(file =r"C:\Users\Mary Friedman\Documents\GitHub\BioProj\Homework4\src\biojava\BIOT670\gene.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



frame_welc=tk.Frame()   #adding labels to frames fits them perfectly to screen
frame_imp= tk.Frame()
frame_imp_btn=tk.Frame()

lab_welcome= tk.Label( #WElcome label here
    master=frame_welc,
    text= "Welcome to the fusion gene visualizer!", font=("Courier", 34),
    foreground= "black", # set the text color to blue, shortcut fg
    background = "plum1", #set background color, shortcut bg

)
lab_welcome.pack() 
lab_import= tk.Label( #directions here
    master=frame_imp,
    text= "Directions: Import your sequence location file", font=("Courier", 34),
    fg= "black",
    bg ="tan1"
)

#to create import button to navigate to file
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog

from tkinter.filedialog import askopenfile 
  
  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
    file = askopenfile(mode ='r',
        filetypes =[('Python Files', '*.py')]) #can change file types
    if file is not None: 
        content = file.read() 
        print(content) 
#can adjust code here on what we want the program to do with the opened file
#Right now it is set just to read it in
btn_import = tk.Button(
    master=frame_imp_btn,
    text ='Import',
    font=("Courier", 34),
    bg= "bisque3",
    command = lambda:open_file())

ttips.CreateToolTip(frame_imp_btn, "Please import your .bam file")

C.pack()
lab_import.pack()
frame_welc.pack()
frame_imp.pack()
frame_imp_btn.pack()
btn_import.pack(side = TOP, pady = 10) 



window.mainloop()
