from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import date

def add_expense(cursor, conn, amount_entry, category_var, desc_entry, date_entry, clear_fields, load_expenses):
    try:
        amount = float(amount_entry.get())
        category = category_var.get()
        desc = desc_entry.get()
        expense_date = date_entry.get()
        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (%s, %s, %s, %s)",
                       (amount, category, desc, expense_date))
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

def load_expenses(cursor, tree):
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM expenses")
    for row in cursor.fetchall():
        tree.insert("", 'end', values=row)

def show_pie_chart(cursor):
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    if data:
        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title('Expense Distribution')
        plt.show()
    else:
        messagebox.showinfo("No Data", "No expenses to show")
