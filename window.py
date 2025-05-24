import customtkinter
from frame import WindowFrame, ErrorFrame

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
    def __init__(self, master, err_msg):
        super().__init__(master)
        self.title('Error!')
        self.geometry("400x125")
        self.resizable(False,False)
        self.grab_set()
        self.focus_force()

        self.frame = ErrorFrame(self, err_msg)
        self.frame.configure(fg_color='transparent')
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        

        