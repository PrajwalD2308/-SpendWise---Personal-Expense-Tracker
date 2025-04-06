from tkinter import messagebox     #Imports messagebox, a pop-up window tool from tkinter
import matplotlib.pyplot as plt    #Imports matplotlib, which is used to show pie charts of expenses.
from datetime import date          #Lets you use date.today() to auto-fill the current date.

# defines a function which adds a new expense to the database
# cursor is used to run sql queries
# conn is used to commit changes
def add_expense(cursor, conn, amount_entry, category_var, desc_entry, date_entry, clear_fields, load_expenses):
    try:
        amount = float(amount_entry.get())
        category = category_var.get()
        desc = desc_entry.get()
        expense_date = date_entry.get()
# .execute is used to insert all the data into expenses table
# %s is used to insert data and is used with mysql
        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (%s, %s, %s, %s)",
                       (amount, category, desc, expense_date))
        conn.commit() #commit or saves changes perm
        messagebox.showinfo("Success", "Expense added successfully")
        clear_fields()
        load_expenses()
 #if the amount is non numerical then this block is executed and error mssge is shown
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")
# this defines a function clear use for reseting the form
def clear_fields(amount_entry, desc_entry, date_entry, category_var):
    amount_entry.delete(0, 'end')
    desc_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    date_entry.insert(0, str(date.today()))  # Puts today’s date automatically into the date field.
    category_var.set("Food")                  # Resets category dropdown to "Food" (default).

# this funct load expenses and Used to show all expenses in the GUI table.
def load_expenses(cursor, tree):
    for row in tree.get_children():
        tree.delete(row)                     # Clear all the old rows
    cursor.execute("SELECT * FROM expenses")   # fetch all the data 
    for row in cursor.fetchall():
        tree.insert("", 'end', values=row)      #insert each row into the table

# Creates a pie chart of total spending by category.
def show_pie_chart(cursor):
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category") 
    data = cursor.fetchall()                                            
    if data:
        categories = [row[0] for row in data]     #Separates categories and amounts into separate lists.
        amounts = [row[1] for row in data]
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title('Expense Distribution')
        plt.show()
    else:
        messagebox.showinfo("No Data", "No expenses to show")
