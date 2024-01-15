import tkinter
from mos_15F_task_list import mos_15F
from mos_15N_task_list import mos_15N
from form_creater import Form_creator

window = tkinter.Tk()
window.title("DA Form 5164-R")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

rank_options = ["PVT", "PV2", "PFC", "SPC", "SGT", "SSG", "SFC"]
mos_options = ["15F", "15N"]
task_list_15F = []
task_list_15N = []
task_list_output = ("Click on the Button", ("That says Update Task List"))


def update_15F_and_15N_task_list():
    for task in mos_15F:
        new_task =f"{task[0]} --- {task[1]}"
        task_list_15F.append(new_task)
        # print(task)
    for task in mos_15N:
        new_task = f"{task[0]} --- {task[1]}"
        task_list_15N.append(new_task)
        # print(task)


update_15F_and_15N_task_list()


clicked = tkinter.StringVar()
clicked.set("15F")

clicked_task = tkinter.StringVar()
clicked_task.set("")

clicked_rank = tkinter.StringVar()
clicked_rank.set("PVT")


rank_label = tkinter.Label(frame, text="Rank")
rank_label.grid(row=0, column=0)
last_name_label = tkinter.Label(frame, text="Last Name")
last_name_label.grid(row=1, column=0)
first_name_label = tkinter.Label(frame, text="First Name")
first_name_label.grid(row=2, column=0)

# rank_entry = tkinter.Entry(frame)
rank_entry = tkinter.OptionMenu(frame, clicked_rank, *rank_options)
rank_entry.grid(row=0, column=1, columnspan=2, sticky="news")
last_name_entry = tkinter.Entry(frame)
last_name_entry.grid(row=1, column=1, columnspan=2, sticky="news")
first_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=2, column=1, columnspan=2, sticky="news")

combo_label = tkinter.Label(frame, text="Select MOS")
combo_label.grid(row=3, column=0)
combo = tkinter.OptionMenu(frame, clicked, *mos_options)
combo.grid(row=3, column=1)

task_list_label = tkinter.Label(frame, text="Select Task")
task_list_label.grid(row=4, column=0)
task_list_combo = tkinter.OptionMenu(frame, clicked_task, *task_list_output)
task_list_combo.grid(row=4, column=1, columnspan=2, sticky="news")


def update_tasklist():
    mos = clicked.get()
    if mos == "15F":
        clicked_task.set('')
        task_list_combo['menu'].delete(0, 'end')

        for tasks in task_list_15F:
            task_list_combo['menu'].add_command(label=tasks, command=tkinter._setit(clicked_task, tasks))
        # print(task_list_15F)
    else:
        clicked_task.set('')
        task_list_combo['menu'].delete(0, 'end')

        for tasks in task_list_15N:
            task_list_combo['menu'].add_command(label=tasks, command=tkinter._setit(clicked_task, tasks))
        # print(task_list_15N)


update_tasklist_button = tkinter.Button(frame, text = "Update Task List", command=update_tasklist)
update_tasklist_button.grid(row=3, column=2)


def print_form():
    rank = clicked_rank.get()
    last_name = last_name_entry.get().upper()
    first_name = first_name_entry.get().upper()
    task = clicked_task.get()
    task_number = task[0:12]
    task_name = task[17:]

    new_form = Form_creator(rank, last_name, first_name, task_number)
    new_form.pdf_creator()
    #
    # last_name_entry.delete(0, tkinter.END)
    # first_name_entry.delete(0, tkinter.END)
    #
    #
    # print(rank, last_name, first_name, task)

    print(task_number, task_name)


print_button = tkinter.Button(frame, text="Print form", command=print_form)
print_button.grid(row=5, column=0, columnspan=3, sticky="news", padx=20, pady=5)


window.mainloop()