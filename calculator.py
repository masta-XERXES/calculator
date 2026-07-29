import tkinter as tk


root = tk.Tk()

root.title("Calculator")
root.geometry("350x500")

current_expression = ""

def add_to_expression(value):
    global current_expression
    
    current_expression += str(value)
    
    display_label.config(
        text=current_expression
    )

def clear_expression():
    global current_expression
    
    current_expression = ""
    
    display_label.config(
        text="0"
    )
    
def calculate_expression():
    global current_expression
    
    try:
        result = eval(current_expression)
        
        current_expression = str(result)
        
        display_label.config(
            text=current_expression
        )
    except:
        display_label.config(
            text="Error"
        )
        
        current_expression = ""
        
display_label = tk.Label(
    root,
    text="0",
    font=("Arial", 32, "bold"),
    anchor="e",
    width=12,
    relief="sunken",
    bg="white"
)

display_label.pack(pady=20)
button_frame = tk.Frame(root)
button_frame.pack()

button_0 = tk.Button(
    button_frame,
    text="0",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("0")
)

button_0.grid(
    row=3,
    column=1,
    padx=5,
    pady=5
)

button_1 = tk.Button(
    button_frame,
    text="1",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("1")
)

button_1.grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)

button_2 = tk.Button(
    button_frame,
    text="2",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("2")
)

button_2.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

button_3 = tk.Button(
    button_frame,
    text="3",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("3")
)

button_3.grid(
    row=2,
    column=2,
    padx=5,
    pady=5
)

button_4 = tk.Button(
    button_frame,
    text="4",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("4")
)

button_4.grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)

button_5 = tk.Button(
    button_frame,
    text="5",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("5")
)

button_5.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

button_6 = tk.Button(
    button_frame,
    text="6",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("6")
)

button_6.grid(
    row=1,
    column=2,
    padx=5,
    pady=5
)

button_7 = tk.Button(
    button_frame,
    text="7",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("7")
)

button_7.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

button_8 = tk.Button(
    button_frame,
    text="8",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("8")
)

button_8.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

button_9 = tk.Button(
    button_frame,
    text="9",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("9")
)

button_9.grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)

division_button = tk.Button(
    button_frame,
    text="/",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("/")
)

division_button.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)

multiplication_button = tk.Button(
    button_frame,
    text="*",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("*")
)

multiplication_button.grid(
    row=1,
    column=3,
    padx=5,
    pady=5
)

addition_button = tk.Button(
    button_frame,
    text="+",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("+")
)

addition_button.grid(
    row=2,
    column=3,
    padx=5,
    pady=5
)

subtraction_button = tk.Button(
    button_frame,
    text="-",
    font=("Arial", 18),
    width=5,
    height=2,
    command=lambda: add_to_expression("-")
)

subtraction_button.grid(
    row=3,
    column=3,
    padx=5,
    pady=5
)

equals_button = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 18),
    width=5,
    height=2,
    command=calculate_expression
)

equals_button.grid(
    row=3,
    column=2,
    padx=5,
    pady=5
)

clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18),
    width=5,
    height=2,
    command=clear_expression

)

clear_button.grid(
    row=3,
    column=0,
    padx=5,
    pady=5
)

root.mainloop()