import tkinter

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5" , "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
    ]

right_symbol = ["/", "x", "-", "+", "="]
top_symbol = ["AC", "+/-", "%", "/"]

column_count = len(button_values[0])
row_count = len(button_values)

neo_blue = "#205b7a"
light_neo_blue = "#a2bbcf"
dark_neo_blue = "#142f44"
dark_blue = "#1d3849"
black = "#000000"
white = "white"
window = tkinter.Tk() #creates a window
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=black, foreground=white)

label.pack()
frame.pack()

window.mainloop()
