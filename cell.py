from tkinter import Button


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text="Text",
            width=12,
            height=4

        )
        # Bind = Print something when we left-click on a button

        btn.bind("<Button-1>", self.left_click_actions)  # "<Button-1>" is convention for left-click
        btn.bind("<Button-3>", self.right_click_actions)  # "<Button-3>" is convention for right-click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print("i am left clicked")

    def right_click_actions(self, event):
        print("i am right click")
