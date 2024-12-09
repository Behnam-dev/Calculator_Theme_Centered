import tkinter as tk
import ttkbootstrap as ttk

# Window
window = ttk.Window(themename='darkly')
window.title('Calculator')
window.geometry('400x650')

# Output
output_frame = ttk.Frame(window)
output_frame.place(x=0, y=0, relwidth=1, relheight=0.3)

out1 = ttk.Frame(output_frame)
out1.place(x=0, y=0, relwidth=1, relheight=0.4)
out2 = ttk.Frame(output_frame)
out2.place(x=0, y=78, relwidth=1, relheight=0.6)

val_label_1 = tk.StringVar()
label_1 = ttk.Label(out1, textvariable=val_label_1, font='Calibri 24 bold')
label_1.pack(side='left', padx=20)

val_label_2 = tk.StringVar()
val_label_2.set('0')
label_2 = ttk.Label(out2, textvariable=val_label_2, font='Calibri 40 bold')
label_2.pack(side='right', padx=20)

# Input
math_cup = ''
clear_result = False

def f_but_numbers(x):
    global clear_result
    if clear_result:
        val_label_2.set('0')
        clear_result = False
    if val_label_2.get() == '0':
        val_label_2.set(x)
    else:
        val_label_2.set(val_label_2.get() + x)

def delete_one():
    global clear_result
    if clear_result:
        val_label_2.set('0')
        clear_result = False
    x = val_label_2.get()
    if x == '0':
        pass
    elif len(x) == 1:
        val_label_2.set('0')
    else:
        cup = ''
        for i in range(len(x)-1):
            cup += x[i]
        val_label_2.set(cup)

def f_dot():
    global clear_result
    if clear_result:
        val_label_2.set('0')
        clear_result = False
    if '.' in val_label_2.get():
        pass
    else:
        val_label_2.set(val_label_2.get() + '.')

def f_operation(op):
    global math_cup
    val_1 = val_label_1.get()
    val_2 = val_label_2.get()
    if val_1 == '':
        if val_2[-1] == '.':
            cup = ''
            for i in range(len(val_2)-1):
                cup += val_2[i]
            val_label_1.set(cup + op)
            ln_val_1 = len(val_label_1.get())
            if ln_val_1 > 18:
                val_label_1.set(val_label_1.get()[ln_val_1-18::1])
            math_cup += cup + op
        else:
            val_label_1.set(val_2 + op)
            ln_val_1 = len(val_label_1.get())
            if ln_val_1 > 18:
                val_label_1.set(val_label_1.get()[ln_val_1-18::1])
            math_cup += val_2 + op

    else:
        if val_2[-1] == '.':
            cup = ''
            for i in range(len(val_2)-1):
                cup += val_2[i]
            val_label_1.set(val_1 + cup + op)
            ln_val_1 = len(val_label_1.get())
            if ln_val_1 > 18:
                val_label_1.set(val_label_1.get()[ln_val_1-18::1])
            math_cup += cup + op

        else:
            val_label_1.set(val_1 + val_2 + op)
            ln_val_1 = len(val_label_1.get())
            if ln_val_1 > 18:
                val_label_1.set(val_label_1.get()[ln_val_1-18::1])
            math_cup += val_2 + op
    val_label_2.set('0')

def evaluate_math_equation(equation):
    equation = equation.replace('x', '*').replace('÷', '/')
    equation = equation.replace('%', '/100')
    try:
        result = eval(equation)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def f_c():
    global math_cup
    math_cup = ''
    val_label_1.set('')
    val_label_2.set('0')

def f_equals():
    global math_cup, clear_result
    val_1 = val_label_1.get()
    val_2 = val_label_2.get()
    if val_2 == '0' and math_cup[-1] in '+-x÷':
        result = evaluate_math_equation(val_1 + '0')
    elif val_2 == '0' and math_cup[-1] =='%':
        result = evaluate_math_equation(val_1)
    else:
        result = evaluate_math_equation(val_1 + val_2)
    val_label_2.set(str(result))
    math_cup = ''
    val_label_1.set('')
    clear_result = True

# Input frame and buttons
input_frame = ttk.Frame(window)
input_frame.place(x=0, y=195, relwidth=1, relheight=0.7)

# Define grids
input_frame.columnconfigure((0, 1, 2, 3), weight=1)
input_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7 ,8), weight=1)

s = ttk.Style()
s.configure('.', font=('Calibri', 24))

# Button definitions
but_percent = ttk.Button(input_frame, text='%', bootstyle='secondary', command=lambda: f_operation('%'))
but_percent.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)

but_divide = ttk.Button(input_frame, text='÷', bootstyle='secondary', command=lambda: f_operation('÷'))
but_divide.grid(row=0, column=1, sticky='nesw', padx=5, pady=5)

but_c = ttk.Button(input_frame, text='C', bootstyle='secondary', command=f_c)
but_c.grid(row=0, column=2, sticky='nesw', padx=5, pady=5)

but_delete = ttk.Button(input_frame, text='<-', bootstyle='secondary', command=delete_one)
but_delete.grid(row=0, column=3, sticky='nesw', padx=5, pady=5)

# Row 1
but_7 = ttk.Button(input_frame, text='7', bootstyle='secondary', command=lambda: f_but_numbers('7'))
but_7.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)

but_8 = ttk.Button(input_frame, text='8', bootstyle='secondary', command=lambda: f_but_numbers('8'))
but_8.grid(row=1, column=1, sticky='nesw', padx=5, pady=5)

but_9 = ttk.Button(input_frame, text='9', bootstyle='secondary', command=lambda: f_but_numbers('9'))
but_9.grid(row=1, column=2, sticky='nesw', padx=5, pady=5)

but_product = ttk.Button(input_frame, text='x', bootstyle='secondary', command=lambda: f_operation('x'))
but_product.grid(row=1, column=3, sticky='nesw', padx=5, pady=5)

# Row 2
but_4 = ttk.Button(input_frame, text='4', bootstyle='secondary', command=lambda: f_but_numbers('4'))
but_4.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)

but_5 = ttk.Button(input_frame, text='5', bootstyle='secondary', command=lambda: f_but_numbers('5'))
but_5.grid(row=2, column=1, sticky='nesw', padx=5, pady=5)

but_6 = ttk.Button(input_frame, text='6', bootstyle='secondary', command=lambda: f_but_numbers('6'))
but_6.grid(row=2, column=2, sticky='nesw', padx=5, pady=5)

but_minus = ttk.Button(input_frame, text='-', bootstyle='secondary', command=lambda: f_operation('-'))
but_minus.grid(row=2, column=3, sticky='nesw', padx=5, pady=5)

# Row 3
but_1 = ttk.Button(input_frame, text='1', bootstyle='secondary', command=lambda: f_but_numbers('1'))
but_1.grid(row=3, column=0, sticky='nesw', padx=5, pady=5)

but_2 = ttk.Button(input_frame, text='2', bootstyle='secondary', command=lambda: f_but_numbers('2'))
but_2.grid(row=3, column=1, sticky='nesw', padx=5, pady=5)

but_3 = ttk.Button(input_frame, text='3', bootstyle='secondary', command=lambda: f_but_numbers('3'))
but_3.grid(row=3, column=2, sticky='nesw', padx=5, pady=5)

but_plus = ttk.Button(input_frame, text='+', bootstyle='secondary', command=lambda: f_operation('+'))
but_plus.grid(row=3, column=3, sticky='nesw', padx=5, pady=5)

# Row 4
but_000 = ttk.Button(input_frame, text='000', bootstyle='secondary', command=lambda: f_but_numbers('000'))
but_000.grid(row=4, column=0, sticky='nesw', padx=5, pady=5)

but_0 = ttk.Button(input_frame, text='0', bootstyle='secondary', command=lambda: f_but_numbers('0'))
but_0.grid(row=4, column=1, sticky='nesw', padx=5, pady=5)

but_dot = ttk.Button(input_frame, text='.', bootstyle='secondary', command=f_dot)
but_dot.grid(row=4, column=2, sticky='nesw', padx=5, pady=5)

but_equals = ttk.Button(input_frame, text='=', bootstyle='success', command=f_equals)
but_equals.grid(row=4, column=3, sticky='nesw', padx=5, pady=5)

# Adding Keyboard Bindings
def key_press(event):
    key = event.keysym

    # Numbers
    if key in '0123456789':
        f_but_numbers(key)
    # Operations
    elif key == 'asterisk':  # multiplication
        f_operation('x')
    elif key == 'plus':  # addition
        f_operation('+')
    elif key == 'minus':  # subtraction
        f_operation('-')
    elif key == 'slash':  # division
        f_operation('÷')
    elif key == 'percent':  # percentage
        f_operation('%')
    # Equals
    elif key == 'Return':  # equals
        f_equals()
    # Delete
    elif key == 'BackSpace':  # delete one character
        delete_one()
    # Dot
    elif key == 'period':  # decimal point
        f_dot()

# Binding keys to the window
window.bind('<KeyPress>', key_press)

# Run the window
window.mainloop()
