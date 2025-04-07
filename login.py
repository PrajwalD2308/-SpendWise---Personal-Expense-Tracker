import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
from main_app import open_main_app
from signup import show_signup

def show_login(root):
    for widget in root.winfo_children():
        widget.destroy()

    conn, cursor = connect_db()

    login_frame = ttk.Frame(root, padding=20)
    login_frame.pack(expand=True)

    ttk.Label(login_frame, text="Username").grid(row=0, column=0, pady=5)
    username_entry = ttk.Entry(login_frame)
    username_entry.grid(row=0, column=1, pady=5)

    ttk.Label(login_frame, text="Password").grid(row=1, column=0, pady=5)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            open_main_app(root, conn, cursor, username)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    ttk.Button(login_frame, text="Login", command=login).grid(row=2, columnspan=2, pady=10)
    ttk.Button(login_frame, text="Sign Up", command=lambda: show_signup(root)).grid(row=3, columnspan=2, pady=5)
