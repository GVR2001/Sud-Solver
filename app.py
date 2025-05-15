import customtkinter 
from frame import SudokuFrame, MenuFrame

class App(customtkinter.CTk):
    """Responsible for running the GUI"""
    # Key mapping to move around grid
    key_map = {
            "Up": "Up", "w": "Up", "W": "Up",
            "Down": "Down", "s": "Down", "S": "Down",
            "Left": "Left", "a": "Left", "A": "Left",
            "Right": "Right", "d": "Right", "D": "Right"
    }

    def __init__(self):
        """Initializes the GUI"""
        super().__init__()

        self.title("Sudoku Solver")
        self.geometry("450x450")
        self.grid_columnconfigure(0, weight=1)
        # Menu Frame
        self.menu_frame = MenuFrame(self)
        self.menu_frame.grid(row=0, column=0, pady=10, padx=30, sticky='nsew')

        # Sudoku Frame
        self.selected_button = None
        self.selected_coords = None

        self.sud_frame = SudokuFrame(self, self)
        self.sud_frame.configure(fg_color='black', corner_radius = 0)
        self.sud_frame.grid(row=1, column=0, padx=37.25, pady=5, sticky='nsew')

        self.bind('<Key>', self.key_pressed)

    def select_button(self, row, col):
        """ Allows the user to select a grid square to modify.

        -Parameters-
        row (int): the row position of the button in the grid
        col (int): the column postion of the button in the grid
        """
        if (self.selected_button): 
            self.selected_button.configure(border_color='grey', border_width = .5) # Resets border
        
        self.selected_coords = (row, col)
        self.selected_button = self.sud_frame.cells[row][col]
        self.selected_button.configure(border_color='blue', border_width = 3) # Changes border for selected button

    def key_pressed(self, event):
        """ Monitors keyboard for relevant key presses (0-9, wasd, directional arrows)
            to update sudoku grid.

        -Parameters-
        event: a keyboard button press
        """
        if event.keysym in App.key_map: # Moves around Grid
            self.move_square(App.key_map[event.keysym])
        elif event.keysym in ("BackSpace", "Delete") and self.selected_button: # Clears selected square
            self.selected_button.configure(text="")
        elif self.selected_button and event.char.isdigit() and event.char != '0': # Updates a square
            self.selected_button.configure(text=event.char)
            print(f"Set cell {self.selected_coords} to {event.char}")

    def get_grid(self):
        """ Creates a textual representation of the sudoku grid.

        -Returns-
        text (str): a textual representation of the grid
        """
        text = ''
        for i in range(9):
            for j in range(9):
                btn_text = self.sud_frame.cells[i][j].cget("text")
                if btn_text: text += btn_text
                else: text += '.'
        return text

    def move_square(self, direction):
        """Changes the selected square with directional keys or 'wasd'.
        
        -Parameters-
        direction (str): the direction we want to move on the grid
        """
        # No button selected yet
        if self.selected_coords is None: 
            self.selected_coords = (0,0)
            self.selected_button = self.sud_frame.cells[0][0]
            self.selected_button.configure(border_color='blue', border_width = 3) # Changes border for selected button
            return  

        row, col = self.selected_coords
        if direction == "Up":
            row = (row - 1) % 9  # wrap around
        elif direction == "Down":
            row = (row + 1) % 9
        elif direction == "Left":
            col = (col - 1) % 9
        elif direction == "Right":
            col = (col + 1) % 9

        self.select_button(row, col)



app = App()
app.mainloop()