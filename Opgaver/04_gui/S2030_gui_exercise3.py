"""
Exercise "GUI step 3":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2030.png

Reuse your code from "GUI step 2".

The GUI structure should be this:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("sejt navn")
main_window.geometry("500x500")

# create labelframe
container = tk.LabelFrame(main_window, text="Container")
container.grid(row=0, column=0)

# create label
padx = 8
pady = 6

# container
container1 = tk.LabelFrame(main_window, text="Container")
container1.grid(row=0, column=0)

# frame 1
frame1 = tk.Frame(container1)
frame1.grid(row=0, column=0)


# labels
id = tk.Label(frame1, text="Id", padx=padx, pady=pady)
id.grid(row=0, column=0)

weight = tk.Label(frame1, text="Weight", padx=padx, pady=pady)
weight.grid(row=0, column=1)

destination = tk.Label(frame1, text="Destination", padx=padx, pady=pady)
destination.grid(row=0, column=2)

weather = tk.Label(frame1, text="Weather", padx=padx, pady=pady)
weather.grid(row=0, column=3, padx=padx, pady=pady)


# entries
id_entry = tk.Entry(frame1, width=4)
id_entry.grid(row=1, column=0, padx=padx, pady=pady)

weight_entry = tk.Entry(frame1, width=8)
weight_entry.grid(row=1, column=1, padx=padx, pady=pady)

destination_entry = tk.Entry(frame1, width=20)
destination_entry.grid(row=1, column=2, padx=padx, pady=pady)

weather_entry = tk.Entry(frame1, width=14)
weather_entry.grid(row=1, column=3, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()

