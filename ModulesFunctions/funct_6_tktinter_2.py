import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480-8-200")

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)
# .grid is another geometry manager

left_frame = tkinter.Frame(mainWindow)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(mainWindow)
right_frame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(right_frame, text="button 1")
button2 = tkinter.Button(right_frame, text="button 2")
button3 = tkinter.Button(right_frame, text="button 3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configuring the columns:
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

left_frame.config(relief="sunken", borderwidth=1)
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky="ns")
right_frame.grid(sticky="new")

right_frame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")

mainWindow.mainloop()