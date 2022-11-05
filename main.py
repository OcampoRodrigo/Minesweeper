from tkinter import *

#Creating basic window class. We use name "root" because it is a convention on tkinter so we can search for problems in
# stackoverflow for example.
root = Tk()
root.configure(bg="lightblue")
#Setting some properties for the windows
root.geometry("1440x720")
root.title("Minesweeper Game")
root.resizable(False , False)

#Iterate until we close it.
root.mainloop()
