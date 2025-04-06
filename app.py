import tkinter as tk
from tkinter import ttk
from database import connect_db
from functions import add_expense, clear_fields, load_expenses, show_pie_chart
from datetime import date

# Connect to DB
conn, cursor = connect_db()

# GUI Window
root = tk.Tk()
root.title("SpendWise - Expense Tracker")
root.geometry("700x500")

# Add Expense Frame
add_frame = tk.LabelFrame(root, text="Add New Expense")
add_frame.pack(fill="x", padx=10, pady=10)

# Add Amount
tk.Label(add_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(add_frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# Add Category
tk.Label(add_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
category_var = tk.StringVar(value="Food")
category_menu = ttk.Combobox(add_frame, textvariable=category_var, values=["Food", "Travel", "Rent", "Utilities", "Other"])
category_menu.grid(row=1, column=1, padx=5, pady=5)

# Add Description
tk.Label(add_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5)
desc_entry = tk.Entry(add_frame)
desc_entry.grid(row=2, column=1, padx=5, pady=5)

# Automatically loads Todays date
tk.Label(add_frame, text="Date:").grid(row=3, column=0, padx=5, pady=5)
date_entry = tk.Entry(add_frame)
date_entry.grid(row=3, column=1, padx=5, pady=5)
date_entry.insert(0, str(date.today()))

tk.Button(add_frame, text="Add Expense", command=lambda: add_expense(
    cursor, conn,
    amount_entry, category_var, desc_entry, date_entry,
    lambda: clear_fields(amount_entry, desc_entry, date_entry, category_var),
    lambda: load_expenses(cursor, tree)
)).grid(row=4, column=0, columnspan=2, pady=10)

# Expense Table
list_frame = tk.LabelFrame(root, text="Expense History")
list_frame.pack(fill="both", expand=True, padx=10, pady=10)

tree = ttk.Treeview(list_frame, columns=("ID", "Amount", "Category", "Description", "Date"), show='headings')
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill="both", expand=True)

# Pie Chart Button
tk.Button(root, text="Show Pie Chart", command=lambda: show_pie_chart(cursor)).pack(pady=10)

# Load data
load_expenses(cursor, tree)

# Start the app
root.mainloop()
conn.close()
