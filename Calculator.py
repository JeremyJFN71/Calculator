import tkinter as tk


def label(button, number=False):
    # Number
    if number is True:
        if num_label1['text'] == '0':
            num_label1['text'] = button
        else:
            num_label1['text'] += button

    # Non number
    else:
        if button == 'del':
            if num_label2['text'] != '':
                num_label2['text'] = ''
            else:
                num_label1['text'] = num_label1['text'][:-1]
                if len(num_label1['text']) == 0:
                    num_label1['text'] = '0'
            
        elif button == '+/-':
            if num_label1['text'] != '0':
                if num_label1['text'][0] != '-':
                    num_label1['text'] = '-' + num_label1['text']
                else:
                    num_label1['text'] = num_label1['text'][1:]

        elif button == '.':
            if '.' not in num_label1['text']:
                num_label1['text'] += button

        elif button == 'esc':
            num_label2['text'] = ''
            num_label1['text'] = '0'
        
        # Operator
        else:
            if button == '%':
                num_label1['text'] = str(float(num_label1['text']) / 100)
            else:
                num_label1['text'] += button

def calc():
    num_label2['text'] = num_label1['text']+' ='

    num_label1['text'] = num_label1['text'].replace('×','*')
    num_label1['text'] = num_label1['text'].replace('÷','/')
    num_label1['text'] = str(eval(num_label1['text']))


window = tk.Tk()
window.configure(bg='black', padx=10, pady=10)
window.title('Calculator')
window.iconbitmap('calculator.ico')
window.resizable(0, 0)

num_label2 = tk.Label(window, text='', font=('Arial', 15), bg='black', fg='#aaa')
num_label2.pack(side='top', anchor='se', pady=5)

num_label1 = tk.Label(window, text='0', font=('Arial', 25), bg='black', fg='white')
num_label1.pack(anchor='se', pady=5)

button_frame = tk.Frame(window)
button_frame.configure(bg='black')
button_frame.pack()

# Calculator button
tk.Button(button_frame, text='1', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='1', num=True: label(button, num)).grid(row=3, column=0)
tk.Button(button_frame, text='2', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='2', num=True: label(button, num)).grid(row=3, column=1)
tk.Button(button_frame, text='3', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='3', num=True: label(button, num)).grid(row=3, column=2)
tk.Button(button_frame, text='4', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='4', num=True: label(button, num)).grid(row=2, column=0)
tk.Button(button_frame, text='5', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='5', num=True: label(button, num)).grid(row=2, column=1)
tk.Button(button_frame, text='6', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='6', num=True: label(button, num)).grid(row=2, column=2)
tk.Button(button_frame, text='7', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='7', num=True: label(button, num)).grid(row=1, column=0)
tk.Button(button_frame, text='8', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='8', num=True: label(button, num)).grid(row=1, column=1)
tk.Button(button_frame, text='9', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='9', num=True: label(button, num)).grid(row=1, column=2)
tk.Button(button_frame, text='0', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='0', num=True: label(button, num)).grid(row=4, column=1)
tk.Button(button_frame, text='+/-', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='+/-': label(button)).grid(row=4, column=0)
tk.Button(button_frame, text='.', font=('Arial', 20), bg='black', fg='white', width=4, bd=0, activebackground='#333', activeforeground='white', command=lambda button='.': label(button)).grid(row=4, column=2)
tk.Button(button_frame, text='=', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda: calc()).grid(row=4, column=3)
tk.Button(button_frame, text='+', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='+': label(button)).grid(row=3, column=3)
tk.Button(button_frame, text='-', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='-': label(button)).grid(row=2, column=3)
tk.Button(button_frame, text='×', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='×': label(button)).grid(row=1, column=3)
tk.Button(button_frame, text='÷', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='÷': label(button)).grid(row=0, column=3)
tk.Button(button_frame, text='%', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='%': label(button)).grid(row=0, column=2)
tk.Button(button_frame, text='⌦', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='del': label(button)).grid(row=0, column=1)
tk.Button(button_frame, text='AC', font=('Arial', 20), bg='black', fg='orange', width=4, bd=0, activebackground='#333', activeforeground='orange', command=lambda button='esc': label(button)).grid(row=0, column=0)

# Keybind
window.bind('1', lambda event, button='1', num = True: label(button, num))
window.bind('2', lambda event, button='2', num = True: label(button, num))
window.bind('3', lambda event, button='3', num = True: label(button, num))
window.bind('4', lambda event, button='4', num = True: label(button, num))
window.bind('5', lambda event, button='5', num = True: label(button, num))
window.bind('6', lambda event, button='6', num = True: label(button, num))
window.bind('7', lambda event, button='7', num = True: label(button, num))
window.bind('8', lambda event, button='8', num = True: label(button, num))
window.bind('9', lambda event, button='9', num = True: label(button, num))
window.bind('0', lambda event, button='0', num = True: label(button, num))
window.bind('.', lambda event, button='.': label(button))
window.bind('<Return>', lambda event: calc())
window.bind('+', lambda event, button='+': label(button))
window.bind('-', lambda event, button='-': label(button))
window.bind('*', lambda event, button='×': label(button))
window.bind('/', lambda event, button='÷': label(button))
window.bind('%', lambda event, button='%': label(button))
window.bind('<BackSpace>', lambda event, button='del': label(button))
window.bind('<Escape>', lambda event, button='esc': label(button))

window.mainloop()