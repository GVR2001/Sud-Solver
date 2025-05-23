import customtkinter
from frame import WindowFrame

class TopLevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Load Grid")
        self.geometry("280x130")
        self.resizable(False,False)
        self.grab_set()     # Prevent interaction with other windows
        self.focus_force()  # Bring window to front and focus

        self.frame = WindowFrame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        

        