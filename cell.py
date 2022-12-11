from tkinter import Button, Label
import random
import settings

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_opened = False
        self.x = x
        self.y = y
        #Append the object to the Cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        # Bind = Print something when we left-click on a button

        btn.bind("<Button-1>", self.left_click_actions)  # "<Button-1>" is convention for left-click
        btn.bind("<Button-3>", self.right_click_actions)  # "<Button-3>" is convention for right-click
        self.cell_btn_object = btn
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells left: {Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl
        return lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mines_length == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
            self.show_cell()
    def get_cell_by_axis(self, x, y):
        #Return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    @property
    def surrounding_cells_mines_length(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounding_cells_mines_length)
            #Replace the text of count cell label with the remaining cells
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells left: {Cell.cell_count}"
                )
        # Mark the cell as opened(use this as the last line of the method)
        self.is_opened = True
    def show_mine(self):
        #A logic to interrupt the game and display a message that the player lost
        #For now, we only change the background color to red
        self.cell_btn_object.configure(bg="red")
    def right_click_actions(self, event):
        print("i am right click")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"

