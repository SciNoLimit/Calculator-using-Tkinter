from tkinter import *

#COLOR
sunflower = "#f1c40f"
carrot = "#e67e22"
belizehole = "#2980b9"
grey = "#455a64"
green = "#27ae60"

root = Tk()
root.title("CALCULATOR")
root.configure(background = grey)

Display = Entry(
    root, 
    font = ('Arial Black', 30),
    width = 15,
    borderwidth = 3,
    bg = "#78909c",
    fg = "white"
)

Display.grid(
    row = 0,
    column = 0,
    columnspan = 4,
    padx = 5,
    pady = 5
)

def Print(number):
    recent = Display.get()
    Display.delete(0, END)
    Display.insert(0, str(recent) + str(number))

def clear():
    Display.delete(0, END)

def calculate():
    dis = str(Display.get())
    cal = eval(dis)
    Display.delete(0, END)
    Display.insert(0, cal)

button_7 = Button(
    root, 
    text = "7", 
    font = ('Arial Black', 18), 
    padx = 20, 
    pady = 10, 
    bg = "#2d3436", 
    fg = "#ffffff",
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(7)

)

button_7.grid(
    row = 1,
    column = 0, 
    padx = 5, 
    pady = 5
)



button_8 = Button(
    root, 
    text = "8", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(8)

)

button_8.grid(
    row = 1, 
    column = 1, 
    padx = 5, 
    pady = 5
)



button_9 = Button(
    root, 
    text = "9", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(9)

)

button_9.grid(
    row = 1, 
    column = 2, 
    padx = 5, 
    pady = 5
)



button_4 = Button(
    root, 
    text = "4", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(4)

)

button_4.grid(
    row = 2, 
    column = 0, 
    padx = 5, 
    pady = 5
)



button_5 = Button(
    root, 
    text = "5", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(5)

)

button_5.grid(
    row = 2, 
    column = 1, 
    padx = 5, 
    pady = 5
)



button_6 = Button(
    root, 
    text = "6", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(6)

)

button_6.grid(
    row = 2, 
    column = 2, 
    padx = 5, 
    pady = 5
)



button_1 = Button(
    root, 
    text = "1", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(1)

)

button_1.grid(
    row = 3, 
    column = 0, 
    padx = 5, 
    pady = 5
)



button_2 = Button(
    root, 
    text = "2", 
    font = ('Arial Black', 18), 
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(2)

)

button_2.grid(
    row = 3, 
    column = 1, 
    padx = 5, 
    pady = 5
)



button_3 = Button(
    root, 
    text = "3", 
    font = ('Arial Black', 18),
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(3)

)

button_3.grid(
    row = 3, 
    column = 2, 
    padx = 5, 
    pady = 5
)



button_0 = Button(
    root,
    text = "0", 
    font = ('Arial Black', 18),
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(0)

)
button_0.grid(
    row = 4, 
    column = 0, 
    padx = 5, 
    pady = 5
)

#####################-------CLEAR-------#######################

button_AC = Button(
    root,
    text = "AC", 
    font = ('Arial Black', 18),
    bg = "#e74c3c", 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = clear

)

button_AC.grid(
    row = 4, 
    column = 1, 
    padx = 5, 
    pady = 5
)

#####################-------EQUAL TO-------#######################

button_equal = Button(
    root,
    text = "=", 
    font = ('Arial Black', 18),
    bg = green, 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: calculate()

)

button_equal.grid(
    row = 4, 
    column = 2, 
    padx = 5, 
    pady = 5
)

#####################-------ADDITION-------#######################

button_add = Button(
    root,
    text = "+", 
    font = ('Arial Black', 18),
    bg = sunflower, 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print("+")

)

button_add.grid(
    row = 1, 
    column = 3, 
    padx = 5, 
    pady = 5
)

#####################-------SUBTRACTION------#######################

button_sub = Button(
    root,
    text = "- ", 
    font = ('Arial Black', 18),
    bg = sunflower, 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print("-")

)

button_sub.grid(
    row = 2, 
    column = 3, 
    padx = 5, 
    pady = 5
)

#####################-------MULTIPLICATION-------#######################

button_mul = Button(
    root,
    text = "*", 
    font = ('Arial Black', 18),
    bg = sunflower, 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print("*")

)

button_mul.grid(
    row = 3, 
    column = 3, 
    padx = 5, 
    pady = 5
)

#####################-------DIVIDION-------#######################

button_div = Button(
    root,
    text = "/ ", 
    font = ('Arial Black', 18),
    bg = sunflower, 
    fg = "#ffffff", 
    padx = 20, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print("/")

)

button_div.grid(
    row = 4, 
    column = 3, 
    padx = 5, 
    pady = 5
)


#####################-------DOT-------#######################


button_dot = Button(
    root,
    text = ".", 
    font = ('Arial Black', 18),
    bg = "#2d3436", 
    fg = "#ffffff", 
    padx = 22, 
    pady = 10,
    relief = RAISED,
    borderwidth = 5,
    command = lambda: Print(".")

)

button_dot.grid(
    row = 5, 
    column = 1,
    columnspan = 2,
    padx = 5, 
    pady = 5
)

root.mainloop()