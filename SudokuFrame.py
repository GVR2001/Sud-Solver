import customtkinter

class GridFrame(customtkinter.CTkFrame):
    """Creates a 3x3 grid component for the Sudoku Grid."""
    def __init__(self, master, parent_app, grid_row_pos, grid_col_pos):
        """ Initializes a 3x3 grid for the sudoku grid.

        -Parameters-
        master: class responsible for creating the GridFrame objects (SudokuFrame)
        parent_app: the main application (App)
        grid_row_pos: the row position within the sudoku grid (9 GridFrame objects are arranged into a 3x3 grid)
        grid_col_pos: the column position within the sudoku grid (9 GridFrame objects are arranged into a 3x3 grid)
        """
        super().__init__(master)
        self.parent_app = parent_app
        # Position of the 3x3 grid in the sudoku grid
        self.grid_row = grid_row_pos
        self.grid_col = grid_col_pos
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = customtkinter.CTkButton(self, width=40, height=40, corner_radius = 0, text="", 
                fg_color='white', border_color='grey', border_width=.5,hover=True, hover_color='grey',text_color ='black',
                command=lambda a=row, b=col: self.find_button(a,b))
                button.grid(row=row,column=col)
                self.buttons[row][col] = button

    def find_button(self, local_row, local_col):
        """ Finds the global postion of the button in the 9x9 sudoku grid.

        -Parameters-
        local_row (int): the row position in the singular 3x3 grid 
        local_col (int): the column position in the singular 3x3 grid
        """
        # Creates coords on sudoku grid (0-8)
        global_row = self.grid_row * 3 + local_row
        global_col = self.grid_col * 3 + local_col
        # Let App() handle button selection
        self.parent_app.select_button(global_row, global_col) 


class SudokuFrame(customtkinter.CTkFrame):
    """A Frame containing the entire sudoku grid."""
    def __init__(self, master, parent_app):
        """ Initializes the 9x9 sudoku grid.

        -Parameters-
        master: class responsible for creating the SudokuFrame (App)
        parent_app: the main application (App) (this is included if master is different to parent)
        """
        super().__init__(master)
        self.parent_app = parent_app
        self.cells = [[None for _ in range (9)] for _ in range(9)]
        for row in range(3):
            for col in range(3):
                grid = GridFrame(self, self.parent_app, row, col)
                grid.grid(row=row, column = col, padx = 2.5, pady= 2.5)
                
                # Copy button references to the main 9x9 cell grid
                for x in range(3):
                    for y in range(3):
                        self.cells[row * 3 + x][col * 3 + y] = grid.buttons[x][y]


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

        self.title("Sudoku Grid")
        self.geometry("420x420")

        self.selected_button = None
        self.selected_coords = None

        self.sud_frame = SudokuFrame(self, self)
        self.sud_frame.configure(fg_color='black', corner_radius = 0)
        self.sud_frame.grid(row=0, column=0, padx=6, pady=6,sticky="nsew")

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
        if event.keysym in App.key_map: 
            self.move_square(App.key_map[event.keysym])
        elif self.selected_button and event.char.isdigit() and event.char != '0':
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