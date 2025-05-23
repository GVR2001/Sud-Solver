import customtkinter

class WindowFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Label
        self.label = customtkinter.CTkLabel(self, text="Enter 81-digit Sudoku string:")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        # Input box
        self.input_box = customtkinter.CTkEntry(self, width=250)
        self.input_box.grid(row=1, column=0, padx=5, pady=5)
        # Enter Button
        self.enterBtn = customtkinter.CTkButton(self,text="Enter", width=250)
        self.enterBtn.grid(row=2, column=0, padx=5, pady=5)

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, parent_app):
        super().__init__(master)
        self.parent_app = parent_app

        # Enter Button 
        self.loadBtn = customtkinter.CTkButton(self, width=60, text='Load Grid', command=parent_app.text_grid)
        self.loadBtn.grid(row=0, column=0, padx=5, pady=5)
        # Solve Button
        self.solveBtn = customtkinter.CTkButton(self, width=60, text="Solve", command=parent_app.solve)
        self.solveBtn.grid(row=0, column=1, padx=5, pady=5)
        # Refresh Button
        self.refreshBtn = customtkinter.CTkButton(self, width=60, text="Refresh", command=parent_app.clear_grid)
        self.refreshBtn.grid(row=0, column=2, padx=5, pady=5)
    


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
                button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=0, text="", 
                    fg_color='white', border_color='grey', border_width=.5,hover=True, hover_color='grey', text_color='black',
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