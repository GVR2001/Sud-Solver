import customtkinter

class single_grid(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = customtkinter.CTkButton(self, width=40, height=40, corner_radius = 0, text="1", 
                fg_color='white',hover=True, hover_color='grey',text_color ='black')
                button.grid(row=i,column=j)
                self.buttons.append(button)
        

class sudokuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grids = []
        for i in range(3):
            for j in range(3):
                grid = single_grid(self)
                grid.grid(row=i, column = j, padx = 5, pady= 5)
                self.grids.append(grid)


        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("grid test")
        self.geometry("380x380")
        #self.single_grid = single_grid(self)
        #self.single_grid.grid(row=0, column = 0, padx = 10, pady = 10, sticky='nsew')
        #self.single_grid2 = single_grid(self)
        #self.single_grid2.grid(row=0, column = 1, padx = 10, pady = 10, sticky='nsew')
        self.sud_frame = sudokuFrame(self)
        self.sud_frame.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")

app = App()
app.mainloop()