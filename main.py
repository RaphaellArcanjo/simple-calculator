from tkinter import *
from tkinter import ttk


#colors
primary_color = '#1C1C1C'
secondary_color = '#808080'
tertiary_color = '#000000'
quaternary_color = '#FFFFFF'
operators_color = '#FF8C00'

root = Tk()
root.title('Minha calculadora')
root.geometry('235x318')
root.minsize(235, 318)
root.maxsize(235, 318)
root.configure(bg=tertiary_color)


ttk.Separator(root, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

#Functions
all_value = ''
text_value = StringVar()

def enter_value(event):
    global all_value

    all_value = all_value + str(event)
    text_value.set(all_value)


def calculate():
    global all_value
    result = eval(all_value)
    text_value.set(result)
    all_value = str(result)


def clear_screen():
    global all_value
    all_value = ''
    text_value.set('')




frame_screen = Frame(root, width=300, height=56, bg=tertiary_color, padx=0, pady=0, relief=FLAT)
frame_screen.grid(row=1, column=0, sticky=NW)

frame_pictues = Frame(root, width=300, height=340, bg=tertiary_color, padx=0, pady=0, relief=FLAT)
frame_pictues.grid(row=2, column=0, sticky=NW)

app_screen = Label(frame_screen, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor='e', bd=0, justify=RIGHT, bg=tertiary_color, fg=quaternary_color, font=('futura', 13, 'bold'))
app_screen.place(x=60, y=15)

#First row
clear_btn = Button(
    frame_pictues,
    command=lambda:clear_screen(),
    text='C',
    width=11,
    height=2,
    bg=secondary_color,
    activebackground=secondary_color,
    fg=tertiary_color,
    activeforeground=tertiary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
clear_btn.place(x=0, y=0)

porcentage_btn = Button(
    frame_pictues,
    command=lambda:enter_value('%'),
    text='%',
    width=5, 
    height=2,
    bg=secondary_color,
    activebackground=secondary_color,
    fg=tertiary_color,
    activeforeground=tertiary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
porcentage_btn.place(x=118, y =0)

split_btn = Button(
    frame_pictues,
    command=lambda:enter_value('/'),
    text='÷',
    width=5,
    height=2,
    bg=operators_color,
    activebackground=operators_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 13, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
split_btn.place(x=177, y=0)

#Second row
seven_btn = Button(
    frame_pictues,
    command=lambda:enter_value('7'),
    text='7',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
seven_btn.place(x=0, y=52)

eight_btn = Button(
    frame_pictues,
    command=lambda:enter_value('8'),
    text='8',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
eight_btn.place(x=59, y=52)

nine_btn = Button(
    frame_pictues,
    command=lambda:enter_value('9'),
    text='9',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
nine_btn.place(x=118, y=52)

multiplication_btn = Button(
    frame_pictues,
    command=lambda:enter_value('*'),
    text='X',
    width=5,
    height=2,
    bg=operators_color,
    activebackground=operators_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
multiplication_btn.place(x=177, y=52)

#Third row
four_btn = Button(
    frame_pictues,
    command=lambda:enter_value('4'),
    text='4',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
four_btn.place(x=0, y=104)

five_btn = Button(
    frame_pictues,
    command=lambda:enter_value('5'),
    text='5',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
five_btn.place(x=59, y=104)

six_btn = Button(
    frame_pictues,
    command=lambda:enter_value('6'),
    text='6',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
six_btn.place(x=118, y=104)

subtraction_btn = Button(
    frame_pictues,
    command=lambda:enter_value('-'),
    text='-',
    width=5,
    height=2,
    bg=operators_color,
    activebackground=operators_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 13, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
subtraction_btn.place(x=177, y=104)

#Fourth row
one_btn = Button(
    frame_pictues,
    command=lambda:enter_value('1'),
    text='1',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
one_btn.place(x=0, y=156)

two_btn = Button(
    frame_pictues,
    command=lambda:enter_value('2'),
    text='2',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
two_btn.place(x=59, y=156)

three_btn = Button(
    frame_pictues,
    command=lambda:enter_value('3'),
    text='3',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
three_btn.place(x=118, y=156)

addition_btn = Button(
    frame_pictues,
    command=lambda:enter_value('+'),
    text='+',
    width=5,
    height=2,
    bg=operators_color,
    activebackground=operators_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
addition_btn.place(x=177, y=156)

#Fifth row
zero_btn = Button(
    frame_pictues,
    command=lambda:enter_value('0'),
    text='0',
    width=11,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
zero_btn.place(x=0, y=208)

point_btn = Button(
    frame_pictues,
    command=lambda:enter_value('.'),
    text='.',
    width=5,
    height=2,
    bg=primary_color,
    activebackground=primary_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
point_btn.place(x=118, y=208)

equal_btn = Button(
    frame_pictues,
    command=lambda:calculate(),
    text='=',
    width=5,
    height=2,
    bg=operators_color,
    activebackground=operators_color,
    fg=quaternary_color,
    activeforeground=quaternary_color,
    font=('futura', 12, 'bold'),
    relief=FLAT,
    overrelief=RIDGE
)
equal_btn.place(x=177, y=208)

root.mainloop()
