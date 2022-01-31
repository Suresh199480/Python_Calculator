from tkinter import *

root = Tk()
root.title("Suresh's Calculator")
root.geometry('320x435')
root.minsize(320, 435)
root.maxsize(320, 435)
root.config(bg='black')


def clear():
    db.delete(0, END)


def btn_clk(num):
    cur_num = db.get()
    clear()
    f_num = cur_num + num
    db.insert(0, f_num)
    db.config(fg='green')


first_num = 0
math = ''
math_sign = ''
math_list = ['+', '-', '*', '/', '%']


def calc(math_type, ms):
    global first_num, math, math_sign
    math_sign = ms
    math = math_type
    first_num = db.get()
    for x in math_list:
        if x in first_num:
            first_num = first_num.replace(x, '')
    clear()
    db.insert(0, first_num + math_sign)


def equal():
    result = ''
    global first_num, math, math_sign
    second_num = db.get().replace(str(first_num) + math_sign, '')
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)

    elif math == 'sub':
        result = int(first_num) - int(second_num)

    elif math == 'mul':
        result = int(first_num) * int(second_num)

    elif math == 'div':
        result = int(first_num) / int(second_num)
        result = round(result, 3)

    elif math == 'module':
        result = int(first_num) % int(second_num)

    db.insert(0, str(result))


db = Entry(root, width=14, font=('Arial', 28), justify=RIGHT)

btn_1 = Button(root, text='1', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('1'), bg='black',
               fg='cyan')
btn_2 = Button(root, text='2', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('2'), bg='black',
               fg='cyan')
btn_3 = Button(root, text='3', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('3'), bg='black',
               fg='cyan')
btn_4 = Button(root, text='4', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('4'), bg='black',
               fg='cyan')
btn_5 = Button(root, text='5', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('5'), bg='black',
               fg='cyan')
btn_6 = Button(root, text='6', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('6'), bg='black',
               fg='cyan')
btn_7 = Button(root, text='7', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('7'), bg='black',
               fg='cyan')
btn_8 = Button(root, text='8', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('8'), bg='black',
               fg='cyan')
btn_9 = Button(root, text='9', font=('Arial', 14), padx=37, pady=10, command=lambda: btn_clk('9'), bg='black',
               fg='cyan')

btn_clr = Button(root, text='Clear', font=('Arial', 14), padx=20, pady=10, command=clear, bg='black', fg='cyan')
btn_0 = Button(root, text='0', font=('Arial', 14), padx=36, pady=10, command=lambda: btn_clk('0'), bg='black',
               fg='cyan')
btn_module = Button(root, text='%', font=('Arial', 14), padx=34, pady=10, command=lambda: calc('module', '%'),
                    bg='black', fg='cyan')

btn_add = Button(root, text='+', font=('Arial', 14), padx=37, pady=10, command=lambda: calc('add', '+'), bg='black',
                 fg='cyan')
btn_sub = Button(root, text='-', font=('Arial', 14), padx=38, pady=10, command=lambda: calc('sub', '-'), bg='black',
                 fg='cyan')
btn_mul = Button(root, text='*', font=('Arial', 14), padx=39, pady=10, command=lambda: calc('mul', '*'), bg='black',
                 fg='cyan')
btn_div = Button(root, text='/', font=('Arial', 14), padx=39, pady=10, command=lambda: calc('div', '/'), bg='black',
                 fg='cyan')
btn_eql = Button(root, text='=', font=('Arial', 14), padx=36, pady=40, command=equal, bg='black', fg='cyan')

db.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_0.grid(row=4, column=0, padx=2, pady=2)
btn_clr.grid(row=4, column=1, padx=2, pady=2)
btn_module.grid(row=4, column=2, padx=2, pady=2)

btn_div.grid(row=5, column=0, padx=2, pady=2)
btn_mul.grid(row=5, column=1, padx=2, pady=2)
btn_sub.grid(row=6, column=0, padx=2, pady=2)
btn_add.grid(row=6, column=1, padx=2, pady=2)
btn_eql.grid(row=5, column=2, padx=2, pady=2, rowspan=2)

root.mainloop()
