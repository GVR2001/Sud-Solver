import customtkinter
from frame import WindowFrame

class TopLevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.grab_set()     # Prevent interaction with other windows
        self.focus_force()  # Bring window to front and focus
        
        self.frame = WindowFrame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        