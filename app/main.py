import tkinter as tk
from tkinter import Menu

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Windows App Template")
        self.geometry("400x300")

        # Create a menu bar
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

        # Add a menu item
        file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", command=self.quit)

        # Add an image
        self.icon_image = tk.PhotoImage(file="app/icons/app-icon.ico")
        self.label = tk.Label(self, image=self.icon_image)
        self.label.pack(pady=20)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
