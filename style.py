from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TFrame", background="#f4f4f4")
    style.configure("TLabel", background="#f4f4f4", font=("Segoe UI", 10))
    style.configure("TButton", background="#4CAF50", foreground="white", padding=5, font=("Segoe UI", 10))
    style.configure("TEntry", padding=5)
    style.configure("TCombobox", padding=5)
    style.configure("TLabelframe", font=("Segoe UI", 11, "bold"), background="#e0e0e0")
    style.configure("Treeview", font=("Segoe UI", 9))
