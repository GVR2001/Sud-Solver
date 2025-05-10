import customtkinter 
import sudoku_frame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.resizable(False, False)
        self.selected_button = None # Track which button is pressed
        self.btns = []

        for i in range(2):
            self.button = customtkinter.CTkButton(self, width=30, height=30, corner_radius = 0, text="", 
                fg_color='white', border_color='black', border_width= 2,hover=True, hover_color='grey',text_color ='black',
                command=lambda b=i: self.select_button(b))  # Pass index
            self.button.pack(padx=20, pady=20)
            self.btns.append(self.button)

        # Bind number key events to the window
        self.bind("<Key>", self.key_pressed)

    def select_button(self, index):
        if (self.selected_button): self.selected_button.configure(border_color='black') # Resets border
        self.selected_button = self.btns[index]
        self.selected_button.configure(border_color='blue') # Changes border for selected button
        print(f"Selected Button {index+1}")

    def key_pressed(self, event):
        if self.selected_button and event.char.isdigit():
            self.selected_button.configure(text=event.char)
            print(f"Updated selected button text to {event.char}")
app = App()
app.mainloop()
