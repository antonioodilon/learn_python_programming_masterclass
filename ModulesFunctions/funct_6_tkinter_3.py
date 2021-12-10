import tkinter
import os

main_window = tkinter.Tk()

main_window.title("Grid Demo")
main_window.geometry("640x480-8-200")

label = tkinter.Label(main_window, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=2, sticky="nsew", rowspan=2)
file_list.config(border=2, relief="sunken")

for zone in os.listdir("R:\Antonio\Imagens"):
    file_list.insert(tkinter.END, zone)

list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL,
                                command=file_list.yview)
list_scroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
file_list["yscrollcommand"] = list_scroll.set

option_frame = tkinter.LabelFrame(main_window, text="File details")
option_frame.grid(row=1, column=2, sticky="ne")

rb_value = tkinter.IntVar()
rb_value.set(3)

radio1 = tkinter.Radiobutton(option_frame, text="Filename", value=1, variable=rb_value)
radio2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rb_value)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rb_value)

radio1.grid(row=0, column=0, sticky="w")
radio2.grid(row=1, column=0, sticky="w")
radio3.grid(row=2, column=0, sticky="w")

# Widget to display the result
result_label = tkinter.Label(main_window, text="Result")
result_label.grid(row=2, column= 2, sticky="nw")
result = tkinter.Entry(main_window)
result.grid(row=2, column=2, sticky="sw")

# Frame for the time spinners
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(row=3, column=0, sticky="new")

# Time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)

hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=": ").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=": ").grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
time_frame["padx"] = 36

main_window.mainloop()

print(rb_value.get())  # Printing the value of rb_value every time the button
# is pressed