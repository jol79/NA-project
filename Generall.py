# ------------------------------------------
#   Program by Chernov.M.
#
#
#
#   Version
#     0.1
#
# ------------------------------------------
import tkinter as tk
from tkinter import Entry

import mysql.connector

# -----Creating connection to our DB-----
DB = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="Nikita16012001",
                             database="BazyDanych")

# here cursor is a storage for requests that we send by functions below
my_cursor = DB.cursor(buffered=True)

# ----- Part of working with mysql DB: -----
# Here I can just write a simple code that I can write in mysql to make action in DB, nothing hard:
my_cursor.execute("SELECT * From users")

for tb in my_cursor:
    print(tb)


# ----- End of the working with mysql DB -----

# ----- Script for Search button ------
def printing_DB_inf():
    my_cursor.execute("SELECT * FROM users")

    # Printing ID_user:
    my_cursor.execute("SELECT ID_user FROM users;")

    entry_1.delete(0, tk.END)
    entry_1.config(fg="#272b30")
    for id_user in my_cursor.fetchall():
            if not None:
                # placing in correct queue just in 1 entry:
                entry_1.insert(tk.END, id_user)
                # the default placing needed for normal placement into the different entries:
                # entry_1.insert(0, id_user)

    # Printing Names:
    my_cursor.execute("SELECT Name FROM users;")

    entry_n_1.delete(0, tk.END)
    entry_n_1.config(fg="#272b30")
    for Name in my_cursor.fetchall():
        if not None:
            entry_n_1.insert(0, Name)

    # Printing Date of birth:
    my_cursor.execute("SELECT Date_of_birth FROM users;")

    entry_b_1.delete(0, tk.END)
    entry_b_1.config(fg="#272b30")
    for date in my_cursor.fetchall():
        if not None:
            entry_b_1.insert(0, date)


# ----- Script for Search button -----
def search_DB_inf():
    my_cursor.execute("SELECT * FROM users")

    # creating the case for data from the entry:
    name = entry.get()
    # ----- Printing results for Name -----
    my_cursor.execute("SELECT Name FROM users where Name = name;")

    entry_n_1.delete(0, tk.END)
    for names in my_cursor.fetchall():
        if not None:
            entry_n_1.config(fg="#272b30")
            entry_n_1.insert(0, names)

    # ----- Printing results for Index -----
    my_cursor.execute("SELECT ID_user FROM users where Name = name;")

    entry_1.delete(0, tk.END)
    for ind in my_cursor.fetchall():
        if not None:
            entry_1.config(fg="#272b30")
            entry_1.insert(0, ind)

    # ----- Printing results for DB -----
    my_cursor.execute("SELECT Date_of_birth FROM users where Name = name;")

    entry_b_1.delete(0, tk.END)
    for date_birth in my_cursor.fetchall():
        if not None:
            entry_b_1.config(fg="#272b30")
            entry_b_1.insert(0, date_birth)


# ----- Script for ADD button -----
def add_DB_inf():
    my_cursor.execute("SELECT * FROM users;")

    # ----- Taking Index -----
    ind_add = entry_1.get()
    # ----- Taking names -----
    name_add = entry_n_1.get()
    # ----- Taking date of birth -----
    datebirth_add = entry_b_1.get()

    my_cursor.execute("INSERT INTO users (ID_user, Name, Date_of_birth) VALUES (%s, %s, %s)", (ind_add, name_add, datebirth_add));
    # commit -> function needed to save all changes after insert/update commands
    DB.commit()

# ----- Script for DEL button -----
def deleting_DB_inf():
    my_cursor.execute("SELECT * FROM users;")

    # ----- Taking names -----
    name_add = entry_n_1.get()
    entry_n_1.delete(0, tk.END)

    # DELETE FROM users Where Name = 1;
    # ----- Using Parametrized query -----
    delete_query = """Delete from users where Name = %s"""
    records_to_del = str(name_add)

    my_cursor.execute(delete_query, records_to_del)

    # commit -> function needed to save all changes after insert/update commands
    DB.commit()


# ----- Configure settings for [buttons]- menus -----
def change_1():
    button['text'] = "Search"
    button['bg'] = '#EDEADA'
    button['activebackground'] = '#555555'
    button['fg'] = '#000000'
    button['activeforeground'] = '#ffffff'


def change_2():
    button_2['text'] = "ADDed!"
    button_2['bg'] = '#EDEADA'
    button_2['activebackground'] = '#555555'
    button_2['fg'] = '#000000'
    button_2['activeforeground'] = '#ffffff'


def change_3():
    button_3['text'] = "Deleted!"
    button_3['bg'] = '#EDEADA'
    button_3['activebackground'] = '#555555'
    button_3['fg'] = '#000000'
    button_3['activeforeground'] = '#ffffff'


def change_4():
    button_4['text'] = "Printed!"
    button_4['bg'] = '#EDEADA'
    button_4['activebackground'] = '#555555'
    button_4['fg'] = '#000000'
    button_4['activeforeground'] = '#ffffff'


# ----- size of the window -----
HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("DB reminder")
root.resizable(False, False)

# -----CANVAS FIELDS-----
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="Green")
canvas.pack()

background_image = tk.PhotoImage(file='Mountains and birds.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#732800", bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

# -----ENTRY FIELDS-----
entry = tk.Entry(frame, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.7)

entry.insert(0, "Write name:")
entry.config(fg='#272b30')

# -----FRAME FIELD-----
frame_2 = tk.Frame(root, bg="#732800")
frame_2.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

# A lot of the Indexes for printing from the DB all of ones the 5 values maximum

# ----- entry_fields to print the results from the DB -----
# ----- ID-entries for ID_user in DB -----
entry_1 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_1.place(relx=0.02, rely=0.04, relwidth=0.15, relheight=0.12)

entry_1.insert(0, "Index_1")
entry_1.config(fg='gray')

entry_2 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_2.place(relx=0.02, rely=0.20, relwidth=0.15, relheight=0.12)

entry_2.insert(0, "Index_2")
entry_2.config(fg='gray')

entry_3 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_3.place(relx=0.02, rely=0.36, relwidth=0.15, relheight=0.12)

entry_3.insert(0, "Index_3")
entry_3.config(fg='gray')

entry_4 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_4.place(relx=0.02, rely=0.52, relwidth=0.15, relheight=0.12)

entry_4.insert(0, "Index_4")
entry_4.config(fg='gray')

entry_5 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_5.place(relx=0.02, rely=0.68, relwidth=0.15, relheight=0.12)

entry_5.insert(0, "Index_5")
entry_5.config(fg='gray')

# ----- Entries for the Name-column in DB -----
entry_n_5 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_n_5.place(relx=0.25, rely=0.68, relwidth=0.50, relheight=0.12)

entry_n_5.insert(0, "f_name/s_name")
entry_n_5.config(fg='gray')

entry_n_4 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_n_4.place(relx=0.25, rely=0.52, relwidth=0.50, relheight=0.12)

entry_n_4.insert(0, "f_name/s_name")
entry_n_4.config(fg='gray')

entry_n_3 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_n_3.place(relx=0.25, rely=0.36, relwidth=0.50, relheight=0.12)

entry_n_3.insert(0, "f_name/s_name")
entry_n_3.config(fg='gray')

entry_n_2 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_n_2.place(relx=0.25, rely=0.20, relwidth=0.50, relheight=0.12)

entry_n_2.insert(0, "f_name/s_name")
entry_n_2.config(fg='gray')

entry_n_1 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_n_1.place(relx=0.25, rely=0.04, relwidth=0.50, relheight=0.12)

entry_n_1.insert(0, "f_name/s_name")
entry_n_1.config(fg='gray')

# ----- Date_of_birth-entries for Date_of_birth-column in DB -----
entry_b_1 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_b_1.place(relx=0.78, rely=0.04, relwidth=0.20, relheight=0.12)

entry_b_1.insert(0, "date of birth")
entry_b_1.config(fg='gray')

entry_b_2 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_b_2.place(relx=0.78, rely=0.20, relwidth=0.20, relheight=0.12)

entry_b_2.insert(0, "date of birth")
entry_b_2.config(fg='gray')

entry_b_3 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_b_3.place(relx=0.78, rely=0.36, relwidth=0.20, relheight=0.12)

entry_b_3.insert(0, "date of birth")
entry_b_3.config(fg='gray')

entry_b_4 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_b_4.place(relx=0.78, rely=0.52, relwidth=0.20, relheight=0.12)

entry_b_4.insert(0, "date of birth")
entry_b_4.config(fg='gray')

entry_b_5 = tk.Entry(frame_2, bg="#EDEADA", font="Arial", borderwidth=2.5)
entry_b_5.place(relx=0.78, rely=0.68, relwidth=0.20, relheight=0.12)

entry_b_5.insert(0, "date of birth")
entry_b_5.config(fg='gray')

# -----BUTTONS-----
button = tk.Button(frame, text="Search", font="Arial", bg="#EDEADA", command=lambda: [search_DB_inf(), change_1()])
button.place(relx=0.025, rely=0.1, relwidth=0.15, relheight=0.7)


button_2 = tk.Button(frame, text="ADD", font="Arial", bg="#EDEADA", command=lambda: [add_DB_inf(), change_2()])
button_2.place(relx=0.18, rely=0.1, relwidth=0.15, relheight=0.7)


button_3 = tk.Button(frame, text="Delete", font="Arial", bg="#EDEADA", command=lambda: [deleting_DB_inf(), change_3()])
button_3.place(relx=0.333, rely=0.1, relwidth=0.15, relheight=0.7)


button_4 = tk.Button(frame, text="ALL", font="Arial", bg="#EDEADA", command=lambda: [printing_DB_inf(), change_4()])
button_4.place(relx=0.92, rely=0.1, relwidth=0.08, relheight=0.7)


root.mainloop() 
