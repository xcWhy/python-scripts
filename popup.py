from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

#class tkinter.Tk(...) - main window, we create it always as the main window for out application
# pyinstaller --noconsole <file> - for no background console opening 
# pyinstaller --windowed <file> - for lower risks of problems with windows defender when opening 
# zip the file?
# add an icon to the application -> pyinstaller --onefile --windowed --icon=icon.ico <file>
#for sharing --onedir is better? need to try it