import tkinter as tk
import ttkbootstrap as ttk


#window
window = ttk.Window(themename='superhero')
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



#Run
window.mainloop()