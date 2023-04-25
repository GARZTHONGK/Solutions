import tkinter as tk
from tkinter import ttk
import plusbus_data as pbd
import plusbus_func as pbf
import  plusbus_sql as pbsql


padx = 8
pady = 4
rowheight = 24
treeview_background = "#ffffff"
treeview_foreground = "#000000"
treeview_selected = "#68caf7"
oddrow = "#dddddd"
evenrow = "#cccccc"


def read_customer_entries():  # Read content of entry boxes
    return entry_customer_id.get(), entry_customer_email.get(), entry_customer_phone_number.get(),


def create_new_customer(tree, record):
    customer = pbd.Customers.convert_from_tuple(record)
    pbsql.create_record(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customers)


def update_customer(tree, record):
    customer = pbd.Customers.convert_from_tuple(record)
    pbsql.update_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customers)


def delete_customer(tree, record):
    customer = pbd.Customers.convert_from_tuple(record)
    pbsql.delete_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customers)


def clear_customer_entries():  # Clear entry boxes
    entry_customer_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_customer_email.delete(0, tk.END)
    entry_customer_phone_number.delete(0, tk.END)


def write_container_entries(values):  # Fill entry boxes
    entry_customer_id.insert(0, values[0])
    entry_customer_email.insert(0, values[1])
    entry_customer_phone_number.insert(0, values[2])


def edit_container(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_customer_entries()  # Clear entry boxes
    write_container_entries(values)  # Fill entry boxes


def read_table(tree, class_):
    count = 0
    result = pbsql.select_all(class_)
    for record in result:
        if record.valid():
            if count % 2 == 0:
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))
            else:
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))
            count += 1
        else:
            print("record not valid")


def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)


def empty_treeview(tree):
    tree.delete(*tree.get_children())


main_window =tk.Tk()
main_window.title("Plusbus S2 Prøveeksamen")
main_window.geometry("900x500")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackgrond=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])

frame_container = tk.LabelFrame(main_window, text="Customers")
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=1, padx=pady, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=padx, pady=pady, sticky="ns")
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)


tree_container["columns"] = ("Id", "Email", "Phone Number")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("Id", anchor=tk.E, width=40)
tree_container.column("Email", anchor=tk.E, width=200)
tree_container.column("Phone Number", anchor=tk.W, width=120)
tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("Id", text="Id", anchor=tk.CENTER)
tree_container.heading("Email", text="Email address", anchor=tk.CENTER)
tree_container.heading("Phone Number", text="Phone number", anchor=tk.CENTER)
tree_container.tag_configure("oddrow", background=oddrow)
tree_container.tag_configure("evenrow", background=evenrow)

tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))


# Create container for buttons
controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

# create container for labels and entries
edit_frame_container = tk.Frame(controls_frame_container)
edit_frame_container.grid(row=0, column=1, padx=padx, pady=pady)

# create labels and entries
label_customer_id = tk.Label(edit_frame_container, text="Id")
label_customer_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_customer_id = tk.Entry(edit_frame_container, width=4, justify="right")
entry_customer_id.grid(row=1, column=0, padx=padx, pady=pady)

label_customer_email = tk.Label(edit_frame_container, text="Email address")
label_customer_email.grid(row=2, column=0, padx=padx, pady=pady)
entry_customer_email = tk.Entry(edit_frame_container, width=30, justify="right")
entry_customer_email.grid(row=3, column=0, padx=padx, pady=pady)

label_customer_phone_number = tk.Label(edit_frame_container, text="Phone number")
label_customer_phone_number.grid(row=4, column=0, padx=padx, pady=pady)
entry_customer_phone_number = tk.Entry(edit_frame_container, width=8, justify="right")
entry_customer_phone_number.grid(row=5, column=0, padx=padx, pady=pady)

# create buttons
button_create_customer = tk.Button(controls_frame_container, text="Create", command=lambda: create_new_customer(tree_container, read_customer_entries()))
button_create_customer.grid(row=0, column=0, padx=padx, pady=pady)

button_update_customer = tk.Button(controls_frame_container, text="Update", command=lambda: update_customer(tree_container, read_customer_entries()))
button_update_customer.grid(row=1, column=0, padx=padx, pady=pady)

button_delete_customer = tk.Button(controls_frame_container, text="Delete", command=lambda: delete_customer(tree_container, read_customer_entries()))
button_delete_customer.grid(row=2, column=0, padx=padx, pady=pady)

button_clear_entries = tk.Button(controls_frame_container, text="Clear all entries", command=clear_customer_entries)
button_clear_entries.grid(row=3, column=0, padx=padx, pady=pady)





if __name__ == "__main__": #main loop
    refresh_treeview(tree_container, pbd.Customers)
    main_window.mainloop()