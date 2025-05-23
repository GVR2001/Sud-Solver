import customtkinter
from frame import WindowFrame

class TopLevelWindow(customtkinter.CTkToplevel):
    def __init__(self, master, parent_app):
        super().__init__(master)
        self.title("Load Grid")
        self.geometry("280x130")
        self.resizable(False,False)
        self.grab_set()     # Prevent interaction with other windows
        self.focus_force()  # Bring window to front and focus

        self.frame = WindowFrame(self, parent_app)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
    
class ErrorWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Error')
        self.geometry("300x100")
        self.grab_set()
        self.focus_force()

        

        