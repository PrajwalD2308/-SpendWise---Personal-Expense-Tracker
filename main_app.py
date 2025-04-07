import tkinter as tk
from tkinter import ttk
from datetime import date
from functions import add_expense, clear_fields, load_expenses, show_pie_chart

def open_main_app(root, conn, cursor, user_id, username):
    for widget in root.winfo_children():
        widget.destroy()

    root.title(f"SpendWise - {username}'s Tracker")

    add_frame = ttk.LabelFrame(root, text="Add New Expense")
    add_frame.pack(fill="x", padx=10, pady=10)

    tk.Label(add_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
    amount_entry = tk.Entry(add_frame)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(add_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
    category_var = tk.StringVar(value="Food")
    category_menu = ttk.Combobox(add_frame, textvariable=category_var,
                                  values=["Food", "Travel", "Rent", "Utilities", "Other"])
    category_menu.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(add_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5)
    desc_entry = tk.Entry(add_frame)
    desc_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(add_frame, text="Date:").grid(row=3, column=0, padx=5, pady=5)
    date_entry = tk.Entry(add_frame)
    date_entry.grid(row=3, column=1, padx=5, pady=5)
    date_entry.insert(0, str(date.today()))

    tree = ttk.Treeview(root, columns=("ID", "Amount", "Category", "Description", "Date"), show='headings')
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    ttk.Button(add_frame, text="Add Expense", command=lambda: add_expense(
        cursor, conn, user_id, amount_entry, category_var, desc_entry, date_entry,
        lambda: clear_fields(amount_entry, desc_entry, date_entry, category_var),
        lambda: load_expenses(cursor, tree, user_id)
    )).grid(row=4, columnspan=2, pady=10)

    ttk.Button(root, text="Show Pie Chart", command=lambda: show_pie_chart(cursor, user_id)).pack(pady=10)

    load_expenses(cursor, tree, user_id)
