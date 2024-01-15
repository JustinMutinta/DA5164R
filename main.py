import tkinter
from tkinter import ttk

import click

window = tkinter.Tk()
window.title("DA Form 5164-R")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

mos_options = ["15F", "15N"]
task_list_15F = ["15F--1", "15F--2"]
task_list_15N = ["15N--1", "15N--2"]

clicked = tkinter.StringVar()
clicked.set("15F")

clicked_task = tkinter.StringVar()
clicked_task.set("Yes")


rank_label = tkinter.Label(frame, text="Rank")
rank_label.grid(row=0, column=0)
last_name_label = tkinter.Label(frame, text="Last Name")
last_name_label.grid(row=1, column=0)
first_name_label = tkinter.Label(frame, text="First Name")
first_name_label.grid(row=2, column=0)

rank_entry = tkinter.Entry(frame)
rank_entry.grid(row=0, column=1)
last_name_entry = tkinter.Entry(frame)
last_name_entry.grid(row=1, column=1)
first_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=2, column=1)

combo_label = tkinter.Label(frame, text="Select MOS")
combo_label.grid(row=3, column=0)
combo = tkinter.OptionMenu(frame, clicked, *mos_options)
combo.grid(row=3, column=1)

task_list_label = tkinter.Label(frame, text="Select Task")
task_list_label.grid(row=4, column=0)
task_list_combo = tkinter.OptionMenu(frame, clicked_task, "One", "Two", "Three")
task_list_combo.grid(row=4, column=1)

window.mainloop()