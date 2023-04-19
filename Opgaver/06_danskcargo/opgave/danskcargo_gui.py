import tkinter as tk
from tkinter import ttk

import danskcargo_data as dcd
import danskcargo_sql as dcsql

def read_container_entries():
    return entry_container_id.get(), entry_container_weight.get(), entry_container_destination.get(), entry_container_weather.get()

def clear_container_entries():
    entry_container_id.delete(0, tk.END)
    entry_container_weight.delete(0, tk.END)
    entry_container_destination.delete(0, tk.END)
    entry_container_weather.delete(0, tk.END)
    print("cleared all entries")

def write_container_entries(values):
    entry_container_id.insert(0, values[0])
    entry_container_weight.insert(0, values[1])
    entry_container_destination.insert(0, values[2])
    print("wrote all entries")

def edit_container(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, "values")
    clear_container_entries()
    write_container_entries(values)

def read_table(tree, class_):  # fill tree from database
   count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
   result = dcsql.select_all(class_)  # Read all containers from database
   for record in result:
       if record.valid():  # this condition excludes soft deleted records from being shown in the data table
           if count % 2 == 0:  # even
              tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
           else:  # odd
              tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
           count += 1

def empty_treeview(tree):  # Clear treeview table
   tree.delete(*tree.get_children())

def refresh_treeview(tree, class_):  # Refresh treeview table
   empty_treeview(tree)  # Clear treeview table
   read_table(tree, class_)  # Fill treeview from database

def create_container(tree, record):
    container = dcd.Container.convert_to_tuple(record)
    dcsql.create_record(container)
    clear_container_entries()
    refresh_treeview(tree, dcd.Container)


def update_container(tree, record):
    container = dcd.Container.convert_to_tuple(record)
    dcsql.update_container(container)
    clear_container_entries()
    refresh_treeview(tree, dcd.Container)


def delete_container(tree, record):
    container = dcd.Container.convert_to_tuple(record)
    dcsql.delete_soft_container(container)
    clear_container_entries()
    refresh_treeview(tree, dcd.Container)


padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "#000000"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"

main_window = tk.Tk()
main_window.title("DanskCargo aspit")
main_window.geometry("500x500")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])



frame_container = tk.LabelFrame(main_window, text="Container")
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=padx, pady=pady, sticky="ns")
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview())

tree_container["columns"] = ("id", "weight", "destination")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("id", anchor=tk.E, width=40)
tree_container.column("weight", anchor=tk.E, width=80)
tree_container.column("destination", anchor=tk.W, width=200)
tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("weight", text="Weight", anchor=tk.CENTER)
tree_container.heading("destination", text="Destination", anchor=tk.CENTER)
tree_container.tag_configure("oddrow", background=oddrow)
tree_container.tag_configure("evenrow", background=evenrow)

controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_container = tk.Frame(controls_frame_container)  # Add tuple entry boxes
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for container id
label_container_id = tk.Label(edit_frame_container, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for container weight
label_container_weight = tk.Label(edit_frame_container, text="Weight")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for container destination
label_container_destination = tk.Label(edit_frame_container, text="Destination")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for container destination
label_container_weather = tk.Label(edit_frame_container, text="Weather")
label_container_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_container_weather = tk.Entry(edit_frame_container, width=14)
entry_container_weather.grid(row=1, column=3, padx=padx, pady=pady)

button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update")
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete")
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes", command=clear_container_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)

tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))



if __name__ == "__main__":
    refresh_treeview(tree_container, dcd.Container)
    main_window.mainloop()