import customtkinter

class single_grid(customtkinter.CTkFrame):
    def __init__(self, master):
        pass

class sudokuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.buttons = []
        for i in range(9):
            for j in range(9):
                button = customtkinter.CTkButton(self, width=40, height=40, corner_radius = 0, text="1", 
                fg_color='white',hover=True, hover_color='grey',text_color ='black')
                button.grid(row=i,column=j)
                self.buttons.append(button)

        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("grid test")
        self.geometry("380x380")
        self.sud_frame = sudokuFrame(self)
        self.sud_frame.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")

app = App()
app.mainloop()