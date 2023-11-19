from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import math

NUMERIC_LIMIT = 999999999999999

str_value      = "0"
str_prep_value = ""
prep_operator  = ' '

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.option_add("*font", "Verdana 14")
root.geometry(f"{260}x{340}")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.title("Calculator")

frame = ctk.CTkFrame(root)
frame.grid(sticky="nsew")
frame.grid_columnconfigure(tuple(range(4)), weight=1)
frame.grid_rowconfigure(tuple(range(7)), weight=1)

prep_lab   = ttk.Label(frame, text="", anchor="e", background="#1c1c1c", foreground="#8f8f8f")
prep_lab.grid(row=0, columnspan=4, sticky="nsew")

output_lab = ttk.Label(frame, text=str_value, anchor="e", background="#1c1c1c", foreground="white", font=("Verdana", 20))
output_lab.grid(row=1, columnspan=4, sticky="nsew")

def get_value_string(s):
    """
    get_value_string returns a properly formatted string with commas in
                     the whole value of the string.

    :param s: a non-formatted numeric string to be formatted.
    :return:  the properly formatted string.
    """
    textval = "{:,}".format(int(float(s)))
    if '.' in s:
        textval += "." + s.split(".")[1]
    return textval

def update_str_value(new_str_value):
    global str_value
    value = float(new_str_value)
    if value > NUMERIC_LIMIT:
        str_value = "0"
        output_lab.config(text="Numeric Overflow")
    elif value < -NUMERIC_LIMIT:
        str_value = "0"
        output_lab.config(text="Numeric Underflow")
    else:
        str_value = new_str_value
        output_lab.config(text=get_value_string(str_value))

def append_digit(digit):
    global str_value
    update_str_value(str_value + str(digit))
        
def prep_calculation(op):
    """
    prep_calculation prepares the calculation of the current
                     user inputted value along with an operator op.

    :param op: the operator to be prepared for calculation.
    """
    global str_value
    global prep_operator
    global str_prep_value
    prep_lab.config(text=get_value_string(str_value) + op)
    str_prep_value = str_value
    str_value = "0"
    prep_operator = op
    output_lab.config(text=get_value_string(str_value))

def value_to_string(value):
    """
    value_to_string converts the numeric value back to the string
                    represented to be presented to the user.
    """
    if value % 1 > 0:
        return str(value)
    else:
        return str(int(value))

def perform_calculation():
    """
    perform_calculation performs the calculation when the user pressed the '=' button.
                        If no operation has been prepared then the function simply
                        returns.
    """

    global str_value
    global str_prep_value
    global prep_operator
    result = 0
    match prep_operator:
        case ' ':
            return
        case '+':
            result = float(str_prep_value) + float(str_value)
        case '-':
            result = float(str_prep_value) - float(str_value)
        case '*':
            result = float(str_prep_value) * float(str_value)
        case '/':
            if float(str_value) == 0:
                str_value = "0"
                str_prep_value = "0"
                output_lab.config(text="Division By Zero")
                return
            result = float(str_prep_value) / float(str_value)
    
    prep_lab.config(text=get_value_string(str_prep_value) + prep_operator + get_value_string(str_value) + "=")
    
    update_str_value(value_to_string(result))
    prep_operator = ' '

def negate_value():
    global str_value
    if str_value == "0":
        return
    elif str_value[0] == "-":
        str_value = str_value[1:]
    else:
        str_value = "-" + str_value
    output_lab.config(text=get_value_string(str_value))

def clear_value():
    global str_value
    str_value = "0"
    output_lab.config(text=get_value_string(str_value))

def make_value_floating():
    global str_value
    if not '.' in str_value:
        str_value += "."
        output_lab.config(text=get_value_string(str_value))

def square_value():
    global str_value
    value = float(str_value) ** 2
    update_str_value(value_to_string(value))

def sqrt_value():
    global str_value
    value = math.sqrt(float(str_value))
    update_str_value(value_to_string(value))

ctk.CTkButton(frame, text="/", command=lambda: prep_calculation('/')).grid(column=3, row=2, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text=".", command=make_value_floating          ).grid(column=0, row=2, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="x^2", command=square_value               ).grid(column=1, row=2, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="sqrt", command=sqrt_value                ).grid(column=2, row=2, padx=(1, 1), pady=(1, 1), sticky="nsew")

ctk.CTkButton(frame, text="1", command=lambda: append_digit(1)      ).grid(column=0, row=3, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="2", command=lambda: append_digit(2)      ).grid(column=1, row=3, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="3", command=lambda: append_digit(3)      ).grid(column=2, row=3, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="+", command=lambda: prep_calculation('+')).grid(column=3, row=3, padx=(1, 1), pady=(1, 1), sticky="nsew")

ctk.CTkButton(frame, text="4", command=lambda: append_digit(4)      ).grid(column=0, row=4, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="5", command=lambda: append_digit(5)      ).grid(column=1, row=4, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="6", command=lambda: append_digit(6)      ).grid(column=2, row=4, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="-", command=lambda: prep_calculation('-')).grid(column=3, row=4, padx=(1, 1), pady=(1, 1), sticky="nsew")

ctk.CTkButton(frame, text="7", command=lambda: append_digit(7)      ).grid(column=0, row=5, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="8", command=lambda: append_digit(8)      ).grid(column=1, row=5, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="9", command=lambda: append_digit(9)      ).grid(column=2, row=5, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="*", command=lambda: prep_calculation('*')).grid(column=3, row=5, padx=(1, 1), pady=(1, 1), sticky="nsew")

ctk.CTkButton(frame, text="0", command=lambda: append_digit(0)      ).grid(column=1, row=6, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="-/+", command=negate_value               ).grid(column=0, row=6, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="=", command=lambda: perform_calculation()).grid(column=3, row=6, padx=(1, 1), pady=(1, 1), sticky="nsew")
ctk.CTkButton(frame, text="C", command=clear_value                  ).grid(column=2, row=6, padx=(1, 1), pady=(1, 1), sticky="nsew")

root.mainloop()