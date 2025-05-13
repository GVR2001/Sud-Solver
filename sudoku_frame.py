import customtkinter

class GridFrame(customtkinter.CTkFrame):
    def __init__(self, master, parent_app, grid_row_pos, grid_col_pos):
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
                command=lambda a=row, b=col: self.select_button(a,b))
                button.grid(row=row,column=col)
                self.buttons[row][col] = button

    def select_button(self, local_row, local_col):
        # Creates coords on sudoku grid (0-8)
        global_row = self.grid_row * 3 + local_row
        global_col = self.grid_col * 3 + local_col
        # Let App() handle button selection
        self.parent_app.select_button(global_row, global_col) 


class SudokuFrame(customtkinter.CTkFrame):
    def __init__(self, master, parent_app):
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
    def __init__(self):
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
        if (self.selected_button): self.selected_button.configure(border_color='grey', border_width = .5) # Resets border
        
        self.selected_coords = (row, col)
        self.selected_button = self.sud_frame.cells[row][col]
        self.selected_button.configure(border_color='blue', border_width = 3) # Changes border for selected button

    def key_pressed(self, event):
        key_map = {
            "Up": "Up", "w": "Up", "W": "Up",
            "Down": "Down", "s": "Down", "S": "Down",
            "Left": "Left", "a": "Left", "A": "Left",
            "Right": "Right", "d": "Right", "D": "Right"
        }
        if event.keysym in key_map: 
            self.move_selection(key_map[event.keysym])
        elif self.selected_button and event.char.isdigit() and event.char != '0':
            self.selected_button.configure(text=event.char)
            print(f"Set cell {self.selected_coords} to {event.char}")

    def move_selection(self, direction):
        if self.selected_coords is None: return  # No button selected yet

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