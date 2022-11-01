from operator import ge
from tkinter import DISABLED, END, NW, S, SE, SW, W, Button, Label, Tk, Frame, BOTH, Entry, messagebox, Toplevel
from tkinter.ttk import Combobox
from math import gcd, pi, sin, cos, sqrt, factorial
import sys
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Виджеты")
        # self.pack(fill=BOTH, expand=1)
        self.grid()
        
        ent = Entry(self,  bd=3, width=30)
        btn = Button(self, text='Вычислить')
        combo = Combobox(self, width=28)
        label = Label()

        combo['values']=(
            '1-Решето Эратосфена',
            '2-Размеры коробки',
            '3-Наименьшее общее кратное',
            '4-Числа Фибоначчи',
            '5-Факториал',
            '6-Калькулятор',
            '7-Лотерея',
            '8-Массив',
            '9-Студенты',
            '10-Шахматы',
            '11-Время падения',
            '12-Геометрия(треугольник)',
            
        )
        
        combo.current(0)
        combo.grid(
            row=0, column=0,
            padx=14, pady=14,
            ipady=6
        )

        def sieve():
            N = int(ent.get())

            arr_ = [ i+1 for i in range(N+1) ]

            for i in range(3, N + 1, 2):
                k = 0
                q = int(N ** 0.5) + 2
                for j in arr_:
                    if j > q:
                        break
                    if i % j == 0:
                        k = 1
                        break
                if k == 0:
                    arr_.append(i)

            print(*arr_)
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            label.config(text=f'результат - {arr_}')
        def box():
            arr_ = ent.get().split()
            a = int(arr_[0])
            b = int(arr_[1])
            c = int(arr_[2])

            m = int(arr_[3])
            k = int(arr_[4])

            mk = m * k

            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )

            if a * b == mk:
                label.config(text='ab')
                print("ab")
            elif a * c == mk:
                label.config(text='aс')
                print("ac")
            elif b * c == mk:
                label.config(text='bc')
                print("bc")   
        def nok():
            a = int(ent.get().split()[0])
            b = int(ent.get().split()[1])

            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            label.config(text=f'Наименьшее общее кратное - {(a * b) / gcd(a, b)}')
            print( (a * b) / gcd(a, b) )
        def fibonacci():
            n = int(ent.get().split()[0])

            f1 = f2 = 1

            while n-2 > 0:
                f1, f2 = f2, f2+f1
                n -= 1
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            label.config(text=f'{f2}')
            print(f2)
        def factorial():
            def fact(n):
                if n == 0:
                    return 1
                return fact( n - 1 ) * n
            
            ent.grid_remove()
            
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            label.config(text=f'{fact(int(ent.get()))}')
            print(fact(int(ent.get())))
            ent.delete(0, END)
        def lottery():
            a = 100
            b = 3
            p1 = p2 = 1
            for i in range(1,a+1):
                p1 = p1 * i
            for j in range(1,a+1-b):
                p2 = p2 * j
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            label.config(text=f'Количество перестановок: {p1/p2}\nШанс угадать выигрышный лотерейный билет: {1 / (p1 / p2)}')
            print ('Количество перестановок: ', p1/p2)
            print ('Шанс угадать выигрышный лотерейный билет: ', 1 / (p1 / p2))
        def array_():
            arr_1 = ent.get().split()
            # print('Ваш массив: ',arr_1)
            arr_2 = []
            m = 0
            for j in range(len(arr_1)):
                if int(arr_1[j]) > 0:
                    arr_2.append(arr_1[j])
                    if int(arr_1[j]) > m:
                        m = int(arr_1[j])
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            label.config(text=f'Новый массив, состоящий из положительных элементов: {arr_2}\nНаибольший элемент массива: {m}')
            print('Новый массив, состоящий из положительных элементов:', arr_2)
            print ('Наибольший элемент массива:', m)
        def student(): 
            from random import randint
            dct = {}
            fio = ent.get().split(' ')
            for el in fio:
                group = randint(1, 100)
                dct[group] = el
            
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            print(dct)
            dct_s = sorted(dct.items(), key=lambda x: x[0])
            label.config(text=f'{dct_s}')
            print(dct_s)
        def chess():
            k = int(ent.get().split()[0])
            l = int(ent.get().split()[1])
            m = int(ent.get().split()[2])
            n = int(ent.get().split()[3])
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
            if k == m or l == n or (k + l + m + n) % 2 == 0:
                label.config(text='да')
                print("yes")
            else: 
                print("no") 
                label.config(text='нет')
        def timeDown():      
            from math import sqrt
            h = int(ent.get())
            g = 9.8
            t = sqrt(2*h/g)
            label.config(text=t)
            print(t)
            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
        def geometry():
            from math import sqrt
            a = int(ent.get().split()[0])
            b = int(ent.get().split()[1])
            c = int(ent.get().split()[2])

            p = (a + b + c) / 2
            s = sqrt(p * (p-a) * (p-b) * (p-c))

            h1 = 2 * s / a
            h2 = 2 * s / b
            h3 = 2 * s / c
            label.config(text=f'Длины высот - {h1, h2, h3}')

            m1 = sqrt(2 * a**2 + 2 * c**2 - b**2) / 2
            m2 = sqrt(2 * b**2 + 2 * c**2 - a**2) / 2
            m3 = sqrt(2 * a**2 + 2 * b**2 - c**2) / 2
            label.config(text=f'Длины медиан - {m1, m2, m3}')

            la = sqrt(b * c * (a+b+c) * (b+c-a)) / (b+c)
            lb = sqrt(a * c * (a+b+c) * (a+c-b)) / (a+c)
            lc = sqrt(a * b * (a+b+c) * (a+b-c)) / (a+b)
            label.config(text=f'Длины биссектрис - {la, lb, lc}')

            r = (((p-a)*(p-b)*(p-c))/p)**0.5
            R = (a*b*c)/(4*((p*(p-a)*(p-b)*(p-c))**0.5))
            label.config(text=f'Радиус вписанной и описанной окружности {r, R}')

            ent.grid_remove()
            ent.delete(0, END)
            btn.grid_remove()
            label.grid(
                sticky=SW,
                row=0, column=1,
                padx=16, pady=9,
                ipady=6
            )
        def calc():
            newWindow = Toplevel(self)
            bttn_list = [
            "7", "8", "9", "+", "*", 
            "4", "5", "6", "-", "/",
            "1", "2", "3",  "=", "xⁿ",
            "0", ".", "±",  "C",
            "Exit", "π", "sin", "cos",
            "(", ")","n!","√2", ]
            r = 1
            c = 0
            for i in bttn_list:
                rel = ""
                cmd=lambda x=i: calc(x)
                Button(newWindow, text=i, command = cmd, width = 10).grid(row=r, column = c)
                c += 1
                if c > 4:
                    c = 0
                    r += 1
            calc_entry = Entry(newWindow, width = 33)
            calc_entry.grid(row=0, column=0, columnspan=5)
            def calc(key):
                global memory
                if key == "=":
            #исключение написания слов
                    str1 = "-+0123456789.*/)(" 
                    if calc_entry.get()[0] not in str1:
                        calc_entry.insert(END, "First symbol is not number!")
                        messagebox.showerror("Error!", "You did not enter the number!")
            #исчисления
                    try:
                        result = eval(calc_entry.get())
                        calc_entry.insert(END, "=" + str(result))
                    except:
                        calc_entry.insert(END, "Error!")
                        messagebox.showerror("Error!", "Check the correctness of data")
                elif key == "C":
                    calc_entry.delete(0, END)
                elif key == "±":
                    if "=" in calc_entry.get():
                        calc_entry.delete(0, END)
                    try:
                        if calc_entry.get()[0] == "-":
                            calc_entry.delete(0)
                        else:
                            calc_entry.insert(0, "-")
                    except IndexError:
                        pass
                elif key == "π":
                    calc_entry.insert(END, pi)
                elif key == "Exit":
                    newWindow.after(1,newWindow.destroy)
                    sys.exit
                elif key == "xⁿ":
                    calc_entry.insert(END, "**")
                elif key == "sin":
                    calc_entry.insert(END, "=" + str(sin(int(calc_entry.get()))))
                elif key == "cos":
                    calc_entry.insert(END, "=" + str(cos(int(calc_entry.get()))))
                elif key == "(":
                    calc_entry.insert(END, "(")
                elif key == ")":
                    calc_entry.insert(END, ")")
                elif key == "n!":
                    calc_entry.insert(END, "=" + str(factorial(int(calc_entry.get()))))
                elif key == "√2":
                    calc_entry.insert(END, "=" + str(sqrt(int(calc_entry.get()))))
                else:
                    if "=" in calc_entry.get():
                        calc_entry.delete(0, END)
                    calc_entry.insert(END, key)
        def select(event):
            selecotion = combo.get()
            if selecotion == '1-Решето Эратосфена':
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=sieve)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите любое число")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '2-Размеры коробки' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=box)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите 5 чисел через пробел")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '3-Наименьшее общее кратное' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=nok)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите 2 числа через пробел")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '4-Числа Фибоначчи' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=fibonacci)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите 1 число")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '5-Факториал' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=factorial)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите число")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '6-Калькулятор' :
                calc()
            elif selecotion == '7-Лотерея' :
                lottery()
            elif selecotion == '8-Массив' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=array_)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Вводите числа через пробел")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '9-Студенты' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=student)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Вводите фамилии студентов через пробел ")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '10-Шахматы' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=chess)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите числа k,l,m,n через пробел")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '11-Время падения' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=timeDown)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите число")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
            elif selecotion == '12-Геометрия(треугольник)' :
                ent.grid(
                    row=0, column=1,
                    padx=2, pady=1,
                    ipady=6
                )

                btn.config(command=geometry)
                btn.grid(
                    row=1, column=1,
                    padx=[50,5], 
                    ipady=6
                )

                label.config(text="Введите 3 числа через пробел")
                label.grid(
                    sticky=SW,
                    row=0, column=0,
                    padx=16, pady=9,
                    ipady=6
                )
        combo.bind("<<ComboboxSelected>>", select)
        

def main():
    root = Tk()
    # root.geometry("800x800+100+100")

    app = Example(root)
    root.mainloop()  
    
 
if __name__ == '__main__':
    main()