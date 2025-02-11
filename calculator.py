import json
import tkinter as tk
import ttkbootstrap as ttk

# Window
style = ttk.Style()
window = style.master
window.title('Calculator')
window.geometry('400x600')
icon = tk.PhotoImage(file='icon.png')
window.iconphoto(True, icon)

#Themes
def themesetter(theme, equaltheme, buttonstheme):
    style = ttk.Style(theme=theme)
    style.configure('.', font=('Calibri', 24))
    but_list = (but_plus, but_0, but_000, but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_divide, but_percent, but_minus, but_product, but_c, but_delete, but_dot)
    for button in but_list:
        button.configure(bootstyle=buttonstheme)
    but_equals.configure(bootstyle=equaltheme)
    theme_data = {
        'general_theme' : theme,
        'equal_theme' : equaltheme,
        'buttons_theme' : buttonstheme
    }
    with open('settings.json', 'w') as js:
        json.dump(theme_data, js)

menu = ttk.Menu(window)
submen1 = ttk.Menu(menu, tearoff=False)
dark_themes = ttk.Menu(submen1, tearoff=False)
dark_themes.add_command(label='Dark Blue', command=lambda : themesetter('superhero', 'primary', 'secondary'))
dark_themes.add_command(label='Black', command=lambda : themesetter('darkly', 'success', 'secondary'))
dark_themes.add_command(label='Purple', command=lambda : themesetter('vapor', 'primary', 'dark'))
dark_themes.add_command(label='Solar', command=lambda : themesetter('solar', 'primary', 'success'))
light_themes = ttk.Menu(submen1, tearoff=False)
light_themes.add_command(label='Lumen', command=lambda : themesetter('lumen', 'primary', 'light'))
light_themes.add_command(label='Morph', command=lambda : themesetter('morph', 'primary', 'light'))
light_themes.add_command(label='Mint', command=lambda : themesetter('minty', 'dark', 'primary'))
submen1.add_cascade(label='Dark', menu=dark_themes)
submen1.add_cascade(label='Light', menu=light_themes)
menu.add_cascade(label='Themes', menu=submen1)


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
    global math_cup, clear_result, style
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

# Button definitions
but_percent = ttk.Button(input_frame, text='%', command=lambda: f_operation('%'))
but_percent.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)

but_divide = ttk.Button(input_frame, text='÷', command=lambda: f_operation('÷'))
but_divide.grid(row=0, column=1, sticky='nesw', padx=5, pady=5)

but_c = ttk.Button(input_frame, text='C', command=f_c)
but_c.grid(row=0, column=2, sticky='nesw', padx=5, pady=5)

but_delete = ttk.Button(input_frame, text='<-', command=delete_one)
but_delete.grid(row=0, column=3, sticky='nesw', padx=5, pady=5)

# Row 1
but_7 = ttk.Button(input_frame, text='7', command=lambda: f_but_numbers('7'))
but_7.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)

but_8 = ttk.Button(input_frame, text='8', command=lambda: f_but_numbers('8'))
but_8.grid(row=1, column=1, sticky='nesw', padx=5, pady=5)

but_9 = ttk.Button(input_frame, text='9', command=lambda: f_but_numbers('9'))
but_9.grid(row=1, column=2, sticky='nesw', padx=5, pady=5)

but_product = ttk.Button(input_frame, text='x', command=lambda: f_operation('x'))
but_product.grid(row=1, column=3, sticky='nesw', padx=5, pady=5)

# Row 2
but_4 = ttk.Button(input_frame, text='4', command=lambda: f_but_numbers('4'))
but_4.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)

but_5 = ttk.Button(input_frame, text='5', command=lambda: f_but_numbers('5'))
but_5.grid(row=2, column=1, sticky='nesw', padx=5, pady=5)

but_6 = ttk.Button(input_frame, text='6', command=lambda: f_but_numbers('6'))
but_6.grid(row=2, column=2, sticky='nesw', padx=5, pady=5)

but_minus = ttk.Button(input_frame, text='-', command=lambda: f_operation('-'))
but_minus.grid(row=2, column=3, sticky='nesw', padx=5, pady=5)

# Row 3
but_1 = ttk.Button(input_frame, text='1', command=lambda: f_but_numbers('1'))
but_1.grid(row=3, column=0, sticky='nesw', padx=5, pady=5)

but_2 = ttk.Button(input_frame, text='2', command=lambda: f_but_numbers('2'))
but_2.grid(row=3, column=1, sticky='nesw', padx=5, pady=5)

but_3 = ttk.Button(input_frame, text='3', command=lambda: f_but_numbers('3'))
but_3.grid(row=3, column=2, sticky='nesw', padx=5, pady=5)

but_plus = ttk.Button(input_frame, text='+', command=lambda: f_operation('+'))
but_plus.grid(row=3, column=3, sticky='nesw', padx=5, pady=5)

# Row 4
but_000 = ttk.Button(input_frame, text='000', command=lambda: f_but_numbers('000'))
but_000.grid(row=4, column=0, sticky='nesw', padx=5, pady=5)

but_0 = ttk.Button(input_frame, text='0', command=lambda: f_but_numbers('0'))
but_0.grid(row=4, column=1, sticky='nesw', padx=5, pady=5)

but_dot = ttk.Button(input_frame, text='.', command=f_dot)
but_dot.grid(row=4, column=2, sticky='nesw', padx=5, pady=5)

but_equals = ttk.Button(input_frame, text='=', command=f_equals)
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

#set current theme
with open('settings.json', 'r') as js:
    current_theme = json.load(js)
themesetter(current_theme['general_theme'],current_theme['equal_theme'],current_theme['buttons_theme'], )

# Run the window
window.configure(menu=menu)
window.mainloop()
