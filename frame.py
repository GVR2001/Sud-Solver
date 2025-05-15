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