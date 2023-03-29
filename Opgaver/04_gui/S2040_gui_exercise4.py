"""
Exercise "GUI step 4":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2040.png

Reuse your code from "GUI step 3".

Fill the treeview with test data.
Play with the color values. Find a color combination that you like.

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes.
    clicking on a data row in the treeview copies the data of this row into the entry fields.

When your program is complete, push it to your GitHub repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
import tkinter as tk
from tkinter import ttk


def clear_entry_boxes():
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)


def read_table(tree):  # fill tree with test data
    count = 0
    for record in test_data_list:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1


def edit_record(event, tree):  # Copy data from selected row into entry box. Parameter event is mandatory, but we don't use it. (1)
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    id_entry.delete(0, tk.END)
    id_entry.insert(0, values[0])
    weight_entry.delete(0, tk.END)
    weight_entry.insert(0, values[1])
    destination_entry.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    destination_entry.insert(0, values[2])  # write data into entry box


# add test data
test_data_list = []
test_data_list.append(('1', 1000, 'oslo'))
test_data_list.append(('2', 2000, 'chicago'))
test_data_list.append(('3', 3000, 'milano'))
test_data_list.append(('4', 4000, 'amsterdam'))

oddrow = "#ddeedd"
evenrow = "#cce0cc"

padx = 8
pady = 6

rowheight = 24
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#773333"  # color of selected row in treeview

main_window = tk.Tk()
main_window.title("sejt navn")
main_window.geometry("500x500")

# create labelframe
container = tk.LabelFrame(main_window, text="Container")
container.grid(row=0, column=0)

# container
container1 = tk.LabelFrame(main_window, text="Container")
container1.grid(row=0, column=0)

# frame 1
frame1 = tk.Frame(container1)
frame1.grid(row=0, column=0)

# style
style = ttk.Style()
style.theme_use('default')
style.configure('Treeview', background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)

tree_1_scrollbar = tk.Scrollbar(frame1)
tree_1_scrollbar.grid(row=0, column=1, sticky='ns')
tree_1 = ttk.Treeview(frame1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=0, column=0)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ('Id', 'Weight', 'Destination')
tree_1.column('#0', width=0, stretch=tk.NO)
tree_1.column('Id', width=40, anchor=tk.CENTER)
tree_1.column('Weight', width=80, anchor=tk.CENTER)
tree_1.column('Destination', width=200, anchor=tk.CENTER)

tree_1.heading('#0', text='', anchor=tk.W)
tree_1.heading('Id', text='Id', anchor=tk.CENTER)
tree_1.heading('Weight', text='Weight', anchor=tk.CENTER)
tree_1.heading('Destination', text='Destination', anchor=tk.CENTER)

tree_1.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors (3)
tree_1.tag_configure('evenrow', background=evenrow)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))  # Define function to be called, when an item is selected. (2)
# frame 2
frame2 = tk.Frame(container1)
frame2.grid(row=1, column=0)

# labels
id_label = tk.Label(frame2, text="Id", padx=padx, pady=pady)
id_label.grid(row=0, column=0)

weight = tk.Label(frame2, text="Weight", padx=padx, pady=pady)
weight.grid(row=0, column=1)

destination = tk.Label(frame2, text="Destination", padx=padx, pady=pady)
destination.grid(row=0, column=2)

weather = tk.Label(frame2, text="Weather", padx=padx, pady=pady)
weather.grid(row=0, column=3, padx=padx, pady=pady)

# entries
id_entry = tk.Entry(frame2, width=4)
id_entry.grid(row=1, column=0, padx=padx, pady=pady)

weight_entry = tk.Entry(frame2, width=8)
weight_entry.grid(row=1, column=1, padx=padx, pady=pady)

destination_entry = tk.Entry(frame2, width=20)
destination_entry.grid(row=1, column=2, padx=padx, pady=pady)

weather_entry = tk.Entry(frame2, width=14)
weather_entry.grid(row=1, column=3, padx=padx, pady=pady)

# buttons
frame3 = tk.Frame(container1)
frame3.grid(row=2, column=0)

create_button = tk.Button(frame3, text="Create")
create_button.grid(row=2, column=0, padx=padx, pady=pady)

update_button = tk.Button(frame3, text="Update")
update_button.grid(row=2, column=1, padx=padx, pady=pady)

delete_button = tk.Button(frame3, text="Delete")
delete_button.grid(row=2, column=2, padx=padx, pady=pady)

clear_button = tk.Button(frame3, text="Clear Entry Boxes", command=clear_entry_boxes)
clear_button.grid(row=2, column=3, padx=padx, pady=pady)

read_table(tree_1)

if __name__ == "__main__":
    main_window.mainloop()
