from tkinter import *
import re


class calculator:
    def __init__(self, master):
        self.master = master
        master.title('astrix calculator')
        master.iconbitmap('calculator.ico')
        dark_grey = '#141414'
        med_grey = '#212121'
        cus_red = '#c41212'
        self.screen = Text(master, background=dark_grey, font=('Helvetica', 32), height=1, state='disabled',
                           foreground='white', bd=0, pady=50, padx=5, selectbackground=dark_grey,
                           inactiveselectbackground=dark_grey)

        for x in range(1, 5):
            self.master.columnconfigure(x, weight=1)
            self.master.rowconfigure(x, weight=1)

        self.screen.grid(row=0, column=0, columnspan=5, sticky=W+E+N+S)
        self.screen.configure(state='normal')
        self.equation = ''
        self.master.geometry('500x600')
        b1 = self.createbutton(7)
        b2 = self.createbutton(8)
        b3 = self.createbutton(9)
        b4 = self.createbutton(u"\u00F7", bg=med_grey)
        b5 = self.createbutton(4)
        b6 = self.createbutton(5)
        b7 = self.createbutton(6)
        b8 = self.createbutton(u"\u00D7", bg=med_grey)
        b9 = self.createbutton(1)
        b10 = self.createbutton(2)
        b11 = self.createbutton(3)
        b12 = self.createbutton('-', bg=med_grey)
        b13 = self.createbutton(',')
        b14 = self.createbutton(0)
        b15 = self.createbutton(None)
        b16 = self.createbutton('+', bg=med_grey)
        b17 = self.createbutton('DEL', None, bg=med_grey)
        b18 = self.createbutton('CE', None, bg=med_grey)
        b19 = self.createbutton('=', None, bg=cus_red)
        b15.config(state='disabled')
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19]

        count = 0

        for row in range(1, 5):
            for col in range(4):
                buttons[count].grid(row=row, column=col, sticky=W+E+N+S)
                count += 1
        buttons[16].grid(row=1, column=4, rowspan=1, sticky=W+E+N+S)
        buttons[17].grid(row=2, column=4, rowspan=2, sticky=W+E+N+S)
        buttons[18].grid(row=4, column=4, rowspan=1, sticky=W+E+N+S)

    def createbutton(self, val, write=True, width=5, bg='black'):
        return Button(self.master, text=val, command=lambda: self.click(val, write), width=width, bg=bg, bd=0,
                      fg='white', font=('Helvetica', 24))

    def click(self, text, write):
        if write is None:
            if text == '=' and self.equation:
                self.equation = re.sub(u'\u00F7', '/', self.equation)
                self.equation = re.sub(u'\u00D7', '*', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == "CE":
                self.clear_screen()
            elif text == 'DEL':
                self.del_screen()
        else:
            # add text to screen
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete(1.0, END)
        self.screen.configure(state='disabled')

    def del_screen(self):
        self.equation = self.equation[:-1]
        self.screen.configure(state='normal')
        text = self.screen.get("1.0", END)[:-2]
        self.screen.tag_config('val', justify=RIGHT)
        self.screen.delete(1.0, END)
        self.screen.insert(END, text, 'val')
        self.screen.configure(state='disabled')

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.tag_config('val', justify=RIGHT)
        self.screen.insert(END, str(value), 'val')
        self.equation += str(value)
        self.screen.configure(state='disabled')

root = Tk()
my_gui = calculator(root)
root.mainloop()
