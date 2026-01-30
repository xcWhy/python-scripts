from tkinter import * # tkinter = Tk interface to Tcl/Tk GUI toolkit
from tkinter import ttk

root = Tk() #this is just the instance, main widget

frm = ttk.Frame(root, padding=100, borderwidth=10, cursor="wait") # the frame for the app what contains

frm.grid() # parent widget, geometry widget, when created widget, they are not automatically added to the ui

ttk.Label(frm, text="hii").grid(row=0, column=0) # these are widgets - python objects

ttk.Entry(frm).grid(row=1, column=0) #single-line text entry


ttk.Button(frm, text="bye", command=root.destroy, cursor="arrow", width=20).grid(row=2, column=0) # hierarchy, the root acts as a parent and must be passed to its children widgtes


# print(dir(frm))

root.title("Meow title")
root.maxsize(1000, 400)

root.mainloop() # an event loop, which is listening for input and refreshesh constantly only while its running


#class tkinter.Tk(...) - main window, we create it always as the main window for out application
# pyinstaller --noconsole <file> - for no background console opening 
# pyinstaller --windowed <file> - for lower risks of problems with windows defender when opening 
# zip the file?
# add an icon to the application -> pyinstaller --onefile --windowed --icon=icon.ico <file>
#for sharing --onedir is better? need to try it