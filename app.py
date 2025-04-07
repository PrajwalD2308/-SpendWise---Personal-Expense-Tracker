from login import show_login
from style import setup_styles
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SpendWise")
    root.geometry("400x400")
    setup_styles()  # Apply custom CSS-like styles
    show_login(root)
    root.mainloop()
