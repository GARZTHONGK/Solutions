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

# customer functions region

def read_customer_entries():  # Read content of entry boxes
    return entry_customer_id.get(), entry_customer_email.get(), entry_customer_phone_number.get(),


def create_new_customer(tree, record):
    customer = pbd.Customers.convert_from_tuple(record)
    pbsql.create_record_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customers)


def update_customer(tree, record):
    customer = pbd.Customers.convert_from_tuple(record)
    pbsql.update_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customers)


def delete_customer(tree, record):
    customer = pbd.Customers.convert_from_tuple(record)
    pbsql.soft_delete_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customers)


def clear_customer_entries():  # Clear entry boxes
    entry_customer_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_customer_email.delete(0, tk.END)
    entry_customer_phone_number.delete(0, tk.END)


def write_customer_entries(values):  # Fill entry boxes
    entry_customer_id.insert(0, values[0])
    entry_customer_email.insert(0, values[1])
    entry_customer_phone_number.insert(0, values[2])


def edit_customer(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_customer_entries()  # Clear entry boxes
    write_customer_entries(values)  # Fill entry boxes

# endregion of customer functions


# journeys function region


def read_journey_entries():
    return entry_journeys_id.get(), entry_journeys_route.get(), entry_journeys_date.get(), entry_journeys_max_capacity.get()


def clear_journey_entries():
    entry_journeys_id.delete(0, tk.END)
    entry_journeys_route.delete(0, tk.END)
    entry_journeys_date.delete(0, tk.END)
    entry_journeys_max_capacity.delete(0, tk.END)


def write_journey_entries(values):
    entry_journeys_id.insert(0, values[0])
    entry_journeys_route.insert(0, values[1])
    entry_journeys_date.insert(0, values[2])
    entry_journeys_max_capacity.insert(0, values[3])


def edit_journey(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, "values")
    clear_journey_entries()
    write_journey_entries(values)


def create_new_journey(tree, record):
    journey = pbd.Journeys.convert_from_tuple(record)
    print("create_record_journey")
    print(journey)
    pbsql.create_record_journey(journey)
    # clear_journey_entries()
    print("refresh_treeview")
    refresh_treeview(tree, pbd.Journeys)


def update_journey(tree, record):
    journey = pbd.Journeys.convert_from_tuple(record)
    pbsql.update_journey(journey)
    clear_journey_entries()
    refresh_treeview()


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
            print(f"record not valid ({record})")


def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)


def empty_treeview(tree):
    tree.delete(*tree.get_children())


main_window = tk.Tk()
main_window.title("Plusbus S2 Prøveeksamen")
main_window.geometry("1200x1200")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackgrond=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])

frame_customers = tk.LabelFrame(main_window, text="Customers")
frame_customers.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_customers = tk.Frame(frame_customers)
tree_frame_customers.grid(row=0, column=1, padx=pady, pady=pady)
tree_scroll_customers = tk.Scrollbar(tree_frame_customers)
tree_scroll_customers.grid(row=0, column=1, padx=padx, pady=pady, sticky="ns")
tree_customers = ttk.Treeview(tree_frame_customers, yscrollcommand=tree_scroll_customers.set, selectmode="browse")
tree_customers.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customers.config(command=tree_customers.yview)


tree_customers["columns"] = ("Id", "Email", "Phone Number")
tree_customers.column("#0", width=0, stretch=tk.NO)
tree_customers.column("Id", anchor=tk.E, width=40)
tree_customers.column("Email", anchor=tk.E, width=200)
tree_customers.column("Phone Number", anchor=tk.W, width=120)
tree_customers.heading("#0", text="", anchor=tk.W)
tree_customers.heading("Id", text="Id", anchor=tk.CENTER)
tree_customers.heading("Email", text="Email address", anchor=tk.CENTER)
tree_customers.heading("Phone Number", text="Phone number", anchor=tk.CENTER)
tree_customers.tag_configure("oddrow", background=oddrow)
tree_customers.tag_configure("evenrow", background=evenrow)

tree_customers.bind("<ButtonRelease-1>", lambda event: edit_customer(event, tree_customers))


# Create container for containers
controls_frame_customers = tk.Frame(frame_customers)
controls_frame_customers.grid(row=0, column=0, padx=padx, pady=pady)

# create container for labels and entries
edit_frame_customers = tk.Frame(controls_frame_customers)
edit_frame_customers.grid(row=0, column=1, padx=padx, pady=pady)

# create container for buttons
button_frame_customers = tk.Frame(controls_frame_customers)
button_frame_customers.grid(row=0, column=0, padx=padx, pady=pady)


# create labels and entries

label_customer_id = tk.Label(edit_frame_customers, text="Id")
label_customer_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_customer_id = tk.Entry(edit_frame_customers, width=4, justify="right")
entry_customer_id.grid(row=1, column=0, padx=padx, pady=pady)

label_customer_email = tk.Label(edit_frame_customers, text="Email address")
label_customer_email.grid(row=2, column=0, padx=padx, pady=pady)
entry_customer_email = tk.Entry(edit_frame_customers, width=30, justify="right")
entry_customer_email.grid(row=3, column=0, padx=padx, pady=pady)

label_customer_phone_number = tk.Label(edit_frame_customers, text="Phone number")
label_customer_phone_number.grid(row=4, column=0, padx=padx, pady=pady)
entry_customer_phone_number = tk.Entry(edit_frame_customers, width=8, justify="right")
entry_customer_phone_number.grid(row=5, column=0, padx=padx, pady=pady)

# create buttons
button_create_customer = tk.Button(button_frame_customers, text="Create", command=lambda: create_new_customer(tree_customers, read_customer_entries()))
button_create_customer.grid(row=0, column=0, padx=padx, pady=10)

button_update_customer = tk.Button(button_frame_customers, text="Update", command=lambda: update_customer(tree_customers, read_customer_entries()))
button_update_customer.grid(row=1, column=0, padx=padx, pady=10)

button_delete_customer = tk.Button(button_frame_customers, text="Delete", command=lambda: delete_customer(tree_customers, read_customer_entries()))
button_delete_customer.grid(row=2, column=0, padx=padx, pady=10)

button_clear_entries_customer = tk.Button(button_frame_customers, text="Clear all entries", command=clear_customer_entries)
button_clear_entries_customer.grid(row=3, column=0, padx=padx, pady=10)

# customer end region
# journey region

frame_journeys = tk.LabelFrame(main_window, text="Journeys")
frame_journeys.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_journeys = tk.Frame(frame_journeys)
tree_frame_journeys.grid(row=0, column=1, padx=pady, pady=pady)
tree_scroll_journeys = tk.Scrollbar(tree_frame_journeys)
tree_scroll_journeys.grid(row=0, column=1, padx=padx, pady=pady, sticky="ns")
tree_journeys = ttk.Treeview(tree_frame_journeys, yscrollcommand=tree_scroll_journeys.set, selectmode="browse")
tree_journeys.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_journeys.config(command=tree_journeys.yview)


tree_journeys["columns"] = ("Id", "Route", "Date", "Max Capacity")
tree_journeys.column("#0", width=0, stretch=tk.NO)
tree_journeys.column("Id", anchor=tk.E, width=40)
tree_journeys.column("Route", anchor=tk.E, width=200)
tree_journeys.column("Date", anchor=tk.W, width=80)
tree_journeys.column("Max Capacity", anchor=tk.W, width=80)

tree_journeys.heading("#0", text="", anchor=tk.W)
tree_journeys.heading("Id", text="Id", anchor=tk.CENTER)
tree_journeys.heading("Route", text="Route", anchor=tk.CENTER)
tree_journeys.heading("Date", text="Date", anchor=tk.CENTER)
tree_journeys.heading("Max Capacity", text="Max Capacity", anchor=tk.CENTER)

tree_journeys.tag_configure("oddrow", background=oddrow)
tree_journeys.tag_configure("evenrow", background=evenrow)

tree_journeys.bind("<ButtonRelease-1>", lambda event: edit_journey(event, tree_journeys))


# Create container for containers
controls_frame_journeys = tk.Frame(frame_journeys)
controls_frame_journeys.grid(row=0, column=0, padx=padx, pady=pady)

# create container for labels and entries
edit_frame_journeys = tk.Frame(controls_frame_journeys)
edit_frame_journeys.grid(row=0, column=1, padx=padx, pady=pady)

# create container for buttons
button_frame_journeys = tk.Frame(controls_frame_journeys)
button_frame_journeys.grid(row=0, column=0, padx=padx, pady=pady)


# create labels and entries

label_journeys_id = tk.Label(edit_frame_journeys, text="Id")
label_journeys_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_journeys_id = tk.Entry(edit_frame_journeys, width=4, justify="right")
entry_journeys_id.grid(row=1, column=0, padx=padx, pady=pady)

label_journeys_route = tk.Label(edit_frame_journeys, text="route")
label_journeys_route.grid(row=2, column=0, padx=padx, pady=pady)
entry_journeys_route = tk.Entry(edit_frame_journeys, width=30, justify="right")
entry_journeys_route.grid(row=3, column=0, padx=padx, pady=pady)

label_journeys_date = tk.Label(edit_frame_journeys, text="date")
label_journeys_date.grid(row=4, column=0, padx=padx, pady=pady)
entry_journeys_date = tk.Entry(edit_frame_journeys, width=12, justify="right")
entry_journeys_date.grid(row=5, column=0, padx=padx, pady=pady)

label_journeys_max_capacity = tk.Label(edit_frame_journeys, text="Max capacity")
label_journeys_max_capacity.grid(row=6, column=0, padx=padx, pady=pady)
entry_journeys_max_capacity = tk.Entry(edit_frame_journeys, width=4, justify="right")
entry_journeys_max_capacity.grid(row=7, column=0, padx=padx, pady=pady)

# create buttons
button_create_journeys = tk.Button(button_frame_journeys, text="Create", command=lambda: create_new_journey(tree_journeys, read_journey_entries()))
button_create_journeys.grid(row=0, column=0, padx=padx, pady=10)

button_update_journeys = tk.Button(button_frame_journeys, text="Update", command=lambda: update_journey(tree_journeys, read_journey_entries()))
button_update_journeys.grid(row=1, column=0, padx=padx, pady=10)

button_delete_journeys = tk.Button(button_frame_journeys, text="Delete", command=lambda: delete_journey(tree_journeys, read_journey_entries()))
button_delete_journeys.grid(row=2, column=0, padx=padx, pady=10)

button_clear_entries_journeys = tk.Button(button_frame_journeys, text="Clear all entries", command=clear_journey_entries)
button_clear_entries_journeys.grid(row=3, column=0, padx=padx, pady=10)





if __name__ == "__main__": # main loop
    refresh_treeview(tree_customers, pbd.Customers)
    refresh_treeview(tree_journeys, pbd.Journeys)
    main_window.mainloop()