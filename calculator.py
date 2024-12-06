import tkinter as tk
import ttkbootstrap as ttk


#window
window = ttk.Window(themename='darkly')
window.title('Calculator')
window.geometry('400x650')

#Output
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
label_2 = ttk.Label(out2, textvariable=val_label_2, font='Calibri 40 bold')
label_2.pack(side='right', padx=20)

#input





input_frame = ttk.Frame(window)
input_frame.place(x=0, y=195, relwidth=1, relheight=0.7)

# define grids
input_frame.columnconfigure((0, 1, 2, 3), weight=1)
input_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7 ,8), weight=1)

s = ttk.Style()
s.configure('.', font=('Calibri', 24))

but_percent = ttk.Button(input_frame, text='%', bootstyle = 'secondary')
but_percent.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)

but_divide = ttk.Button(input_frame, text='/', bootstyle = 'secondary')
but_divide.grid(row=0, column=1, sticky='nesw', padx=5, pady=5)

but_c = ttk.Button(input_frame, text='C', bootstyle = 'secondary')
but_c.grid(row=0, column=2, sticky='nesw', padx=5, pady=5)

but_delete = ttk.Button(input_frame, text='del', bootstyle = 'secondary')
but_delete.grid(row=0, column=3, sticky='nesw', padx=5, pady=5)
#_______________________________________________________________________
but_7 = ttk.Button(input_frame, text='7', bootstyle = 'secondary')
but_7.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)

but_8 = ttk.Button(input_frame, text='8', bootstyle = 'secondary')
but_8.grid(row=1, column=1, sticky='nesw', padx=5, pady=5)

but_9 = ttk.Button(input_frame, text='9', bootstyle = 'secondary')
but_9.grid(row=1, column=2, sticky='nesw', padx=5, pady=5)

but_product = ttk.Button(input_frame, text='x', bootstyle = 'secondary')
but_product.grid(row=1, column=3, sticky='nesw', padx=5, pady=5)
#_______________________________________________________________________
but_4 = ttk.Button(input_frame, text='4', bootstyle = 'secondary')
but_4.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)

but_5 = ttk.Button(input_frame, text='5', bootstyle = 'secondary')
but_5.grid(row=2, column=1, sticky='nesw', padx=5, pady=5)

but_6 = ttk.Button(input_frame, text='6', bootstyle = 'secondary')
but_6.grid(row=2, column=2, sticky='nesw', padx=5, pady=5)

but_minus = ttk.Button(input_frame, text='-', bootstyle = 'secondary')
but_minus.grid(row=2, column=3, sticky='nesw', padx=5, pady=5)
#_______________________________________________________________________

but_1 = ttk.Button(input_frame, text='1', bootstyle = 'secondary')
but_1.grid(row=3, column=0, sticky='nesw', padx=5, pady=5)

but_2 = ttk.Button(input_frame, text='2', bootstyle = 'secondary')
but_2.grid(row=3, column=1, sticky='nesw', padx=5, pady=5)

but_3 = ttk.Button(input_frame, text='3', bootstyle = 'secondary')
but_3.grid(row=3, column=2, sticky='nesw', padx=5, pady=5)

but_sum = ttk.Button(input_frame, text='+', bootstyle = 'secondary')
but_sum.grid(row=3, column=3, sticky='nesw', padx=5, pady=5)
#_______________________________________________________________________

but_000 = ttk.Button(input_frame, text='000', bootstyle = 'secondary')
but_000.grid(row=4, column=0, sticky='nesw', padx=5, pady=5)

but_0 = ttk.Button(input_frame, text='0', bootstyle = 'secondary')
but_0.grid(row=4, column=1, sticky='nesw', padx=5, pady=5)

but_dot = ttk.Button(input_frame, text='.', bootstyle = 'secondary')
but_dot.grid(row=4, column=2, sticky='nesw', padx=5, pady=5)

but_equals = ttk.Button(input_frame, text='=')
but_equals.grid(row=4, column=3, sticky='nesw', padx=5, pady=5)




#Run
window.mainloop()