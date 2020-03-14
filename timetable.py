import tkinter as tk

days = 5
periods = 6
recess_break_aft = 3 # recess after 3rd Period

period_names = list(map(lambda x: 'Period ' + str(x), range(1, 6+1)))
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']

tt = tk.Tk()

title_lab = tk.Label(
    tt,
    text='T  I  M  E  T  A  B  L  E',
    font=('Consolas', 20, 'bold'),
    pady=15
)
title_lab.pack()

table = tk.Frame(tt)
table.pack()

first_half = tk.Frame(table)
first_half.pack(side='left')

recess_frame = tk.Frame(table)
recess_frame.pack(side='left')

second_half = tk.Frame(table)
second_half.pack(side='left')

recess = tk.Label(
    recess_frame,
    text='R\n\nE\n\nC\n\nE\n\nS\n\nS',
    font=('Consolas', 18, 'italic'),
    width=3,
    relief='sunken'
)
recess.pack()

for i in range(days):
    b = tk.Label(
        first_half,
        text=day_names[i],
        font=('Consolas', 12, 'bold'),
        width=9,
        height=2,
        bd=5,
        relief='raised'
    )
    b.grid(row=i+1, column=0)

for i in range(periods):
    if i < 3:
        b = tk.Label(
            first_half,
            text=period_names[i],
            font=('Consolas', 12, 'bold'),
            width=9,
            height=1,
            bd=5,
            relief='raised'
        )
        b.grid(row=0, column=i+1)
    else:
        b = tk.Label(
            second_half,
            text=period_names[i],
            font=('Consolas', 12, 'bold'),
            width=9,
            height=1,
            bd=5,
            relief='raised'
        )
        b.grid(row=0, column=i)

for i in range(days):
    for j in range(periods):
        if j < 3:
            b = tk.Label(
                first_half,
                text='Hello World!',
                font=('Consolas', 10),
                width=13,
                height=3,
                bd=5,
                relief='raised',
                wraplength=80,
                justify='center'
            )
            b.grid(row=i+1, column=j+1)
        else:
            b = tk.Label(
                second_half,
                text='Hello World!',
                font=('Consolas', 10),
                width=13,
                height=3,
                bd=5,
                relief='raised',
                wraplength=80,
                justify='center'
            )
            b.grid(row=i+1, column=j)

tt.mainloop()