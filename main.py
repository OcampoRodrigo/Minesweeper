from tkinter import *
from cell import Cell
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
top_frame.place(x="0", y="0")

#Creating frame variable to display the score
left_frame = Frame(
    root,
    bg="white",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x="0", y= utils.height_prct(25))

center_frame = Frame(
    root,
    bg="green",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        button = Cell(x, y)
        button.create_btn_object(center_frame)
        button.cell_btn_object.grid(
            column=x, row=y
        )
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=5, y=5
)
Cell.randomize_mines()




#Iterate until we close it.
root.mainloop()
