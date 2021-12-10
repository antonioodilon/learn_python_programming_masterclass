try:
    import tkinter
except ImportError:  # For people running Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
# If you run the above line of code, its pop-up will appear before the following
# one

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+10+300")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side="top")
# .pack is a geometry manager

left_frame = tkinter.Frame(mainWindow)
left_frame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")  # Across the Y axis
# canvas.pack(side="right", fill=tkinter.X, expand=True)  # Across the X axis

right_frame = tkinter.Frame(mainWindow)
right_frame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(right_frame, text="button 1")
button2 = tkinter.Button(right_frame, text="button 2")
button3 = tkinter.Button(right_frame, text="button 3")

button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

# button1 = tkinter.Button(mainWindow, text="button 1")
# button2 = tkinter.Button(mainWindow, text="button 2")
# button3 = tkinter.Button(mainWindow, text="button 3")
#
# button1.pack(side="top", anchor="n")
# button2.pack(side="top", anchor="s")
# button3.pack(side="top", anchor="e")

mainWindow.mainloop()