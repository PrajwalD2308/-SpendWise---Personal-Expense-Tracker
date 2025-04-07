import tkinter as tk
from tkinter import messagebox
from database import connect_db

def show_signup():
    signup_win = tk.Toplevel()
    signup_win.title("Sign Up")
    signup_win.geometry("300x250")

    tk.Label(signup_win, text="Username").pack(pady=5)
    username_entry = tk.Entry(signup_win)
    username_entry.pack()

    tk.Label(signup_win, text="Password").pack(pady=5)
    password_entry = tk.Entry(signup_win, show="*")
    password_entry.pack()

    def register_user():
        username = username_entry.get()
        password = password_entry.get()

        conn, cursor = connect_db()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "User already exists")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "User registered successfully")
            signup_win.destroy()
            # 👇 Import placed here to avoid circular import
            from login import show_login
            show_login()

        conn.close()

    tk.Button(signup_win, text="Sign Up", command=register_user).pack(pady=10)
