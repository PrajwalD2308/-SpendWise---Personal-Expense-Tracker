from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import date

def add_expense(cursor, conn, user_id, amount_entry, category_var, desc_entry, date_entry, clear_fields, load_expenses):
    try:
        amount = float(amount_entry.get())
        category = category_var.get()
        desc = desc_entry.get()
        expense_date = date_entry.get()

        cursor.execute(
            "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (%s, %s, %s, %s, %s)",
            (user_id, amount, category, desc, expense_date)
        )
        conn.commit()
        messagebox.showinfo("Success", "Expense added successfully")
        clear_fields()
        load_expenses()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")

def clear_fields(amount_entry, desc_entry, date_entry, category_var):
    amount_entry.delete(0, 'end')
    desc_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    date_entry.insert(0, str(date.today()))
    category_var.set("Food")

def load_expenses(cursor, tree, user_id):
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM expenses WHERE user_id = %s", (user_id,))
    for row in cursor.fetchall():
        tree.insert("", 'end', values=row)

from tkinter import messagebox
import matplotlib.pyplot as plt

def show_pie_chart(cursor, user_id):
    cursor.execute("SELECT category, SUM(amount) FROM expenses WHERE user_id=%s GROUP BY category", (user_id,))
    data = cursor.fetchall()

    if data:
        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]
        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title('Expense Distribution')
        plt.axis('equal')  # Keeps pie chart as a circle
        plt.show()
    else:
        messagebox.showinfo("No Data", "No expenses to show.")

     