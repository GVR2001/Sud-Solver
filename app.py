import customtkinter 
from frame import SudokuFrame, MenuFrame
from window import TopLevelWindow, ErrorWindow
from utils import parse, search, constrain, string_picture, is_valid

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
        self.resizable(False,False)
        self.grid_columnconfigure(0, weight=1)

        # Windows
        self.toplevel_window = None
        self.error_window = None

        # Menu Frame
        self.menu_frame = MenuFrame(self, self)
        self.menu_frame.grid(row=0, column=0, pady=10, padx=30)

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
            self.selected_button.configure(text=event.char, text_color='black')

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

    # Refresh Button
    def clear_grid(self):
        """ Clears grid squares."""
        for i in range(9):
            for j in range(9):
                self.sud_frame.cells[i][j].configure(text="")

    # Solve Button
    def solve(self):
        """ Solves sudoku puzzle."""
        grid = parse(self.get_grid())
        invalid_squares = is_valid(grid)
        if not invalid_squares:
            answer = string_picture(search(constrain(grid)))
            for i in range(9):
                for j in range(9):
                    btn = self.sud_frame.cells[i][j]
                    if  btn.cget("text") == "":
                        btn.configure(text=answer[i * 9 + j], text_color='blue')
        else:
            self.invalidate(invalid_squares)
    
    def invalidate(self, coords: list):
        """ Colors invalid squares red."""
        for coord in coords:
            x,y = coord
            self.sud_frame.cells[x][y].configure(text_color='red')
        

    # Load Sudoku Grid
    def text_grid(self):
        """ Creates window for user to enter textual grid representation."""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow(self, self)  # create window if its None or destroyed
    
    def load_sudoku(self, puzzle: str):
        for i in range(9):
            for j in range(9):
                btn = self.sud_frame.cells[i][j]
                c = puzzle[i * 9 + j] 
                if c != '.':
                    btn.configure(text=c)
    
    def load_error(self, err_msg):
        if self.error_window is None or not self.error_window.winfo_exists():
            self.error_window = ErrorWindow(self, err_msg)  # create error window if its None or destroyed

app = App()
app.mainloop()