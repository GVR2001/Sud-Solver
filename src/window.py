import customtkinter
from frame import WindowFrame, ErrorFrame

class TopLevelWindow(customtkinter.CTkToplevel):
    """Creates an additional window so that the user can load a sudoku puzzle."""
    def __init__(self, master, parent_app):
        """Initializes a window (load_grid functionality)
        
        -Parameters-
        master: the object creating the window
        parent_app: the main application object
        """
        super().__init__(master)
        self.title("Load Grid")
        self.geometry("280x130")
        self.resizable(False,False)
        self.grab_set()     # Prevent interaction with other windows
        self.focus_force()  # Bring window to front and focus

        self.frame = WindowFrame(self, parent_app)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
    
class ErrorWindow(customtkinter.CTkToplevel):
    """Creates an additional window to show an error message."""
    def __init__(self, master, err_msg):
        """ Initializes an error window.
        
        -Parameters-
        master: the object creating the error window
        err_msg (str): the error message we want to convey to the user
        """
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

        

        