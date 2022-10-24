from tkinter import NW, Tk, Frame, BOTH, Entry
from tkinter.ttk import Combobox
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Окружность")
        self.pack(fill=BOTH, expand=1)

        ent = Entry(self,  bd=3)
        ent.place(
            x=10, 
            y=10, 
            width=200, 
            height = 30
            )

        combo = Combobox(self)
        combo['values']=(
            '1-Решето Эратосфена',
            '2-Размеры коробки',
            '3-Наименьшее общее кратное',
            '4-Числа Фибоначчи',
            '5-Числа Фибоначчи',
            '6-Калькулятор',
            '7-Лотерея',
            '8-Массив',
            '9-Студенты',
            '10-Шахматы',
            '11-Время падения',
            '12-Геометрия(треугольник)',
            
        )
        combo.current(0)
        combo.place(
            x=10,
            y=40,
            width=200,
            height=30
        )
        
        

def main():
    root = Tk()
    root.geometry("800x800+100+100")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()