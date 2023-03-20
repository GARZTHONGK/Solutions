# This is a list of useful links about the GUI library tkinter
# Turn back to this page later, when needed.

# grid(): https://tkdocs.com/shipman/grid.html   https://www.tutorialspoint.com/python/tk_grid.htm
#         https://www.youtube.com/watch?v=BSfbjrqIw20&t=108s (from 1:48 till 7:03)

# tk.Button(): https://tkdocs.com/shipman/button.html   https://www.tutorialspoint.com/python/tk_button.htm#
# tk.Label(): https://tkdocs.com/shipman/label.html   https://www.tutorialspoint.com/python/tk_label.htm
# tk.Entry(): https://tkdocs.com/shipman/entry.html   https://www.tutorialspoint.com/python/tk_entry.htm
# tk.Frame(): https://tkdocs.com/shipman/frame.html   https://www.tutorialspoint.com/python/tk_frame.htm
# tk.LabelFrame(): https://tkdocs.com/shipman/labelframe.html   https://www.tutorialspoint.com/python/tk_labelframe.htm


# ttk.Treeview(): https://docs.python.org/3/library/tkinter.ttk.html#treeview
# tk.Scrollbar(): https://tkdocs.com/shipman/scrollbar.html   https://www.tutorialspoint.com/python/tk_scrollbar.htm


from tkinter import *
import tkinter as tk

root = Tk()

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="flat", highlightthickness=0)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

def test():
    print("Hej uli")

canvas = Canvas(root, height=300, width=500)
canvas.pack()

button = RoundedButton(root, 200, 100, 50, 2, 'red', '#ffffff', command=test)
button.place(relx=.1, rely=.1)
button_2 = RoundedButton(button, 400, 100, 50, 2, "#000000", "#ffffff", command=test)
button.place(relx=.1, rely=.1)
root.mainloop()