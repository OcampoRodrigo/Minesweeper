from tkinter import *
import settings
import utils
#Creating basic window class. We use name "root" because it is a convention on tkinter so we can search for problems in
# stackoverflow for example.
root = Tk()
root.configure(bg="lightblue")

#Setting some properties for the windows
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False , False)

#Creating frame variable
top_frame = Frame(
    root,
    bg="black",
    width="1440",
    height= utils.height_prct(25)
)
#Placing the variable
top_frame.place(x="0" , y="0")

#Creating frame variable to display the score
left_frame = Frame(
    root,
    bg="blue",
    width= utils.width_prct(25),
    height= utils.height_prct(75)
)
left_frame.place(x="0", y= utils.height_prct(25))

#Iterate until we close it.
root.mainloop()
