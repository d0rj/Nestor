import pyautogui as pag
import time
from typing import List
from tkinter import *
import tkinter.filedialog as fd


FILE_NAME = 'text.txt'


def choose_file():
    global FILE_NAME
    FILE_NAME = fd.askopenfilename()


def on_choose_click(button: Button):
    choose_file()
    button['text'] = FILE_NAME


def write_lines(lines: List[str], interval: float = 0):
    for line in lines:
        pag.write(line, interval)
        pag.write('\n')
        pag.press('home')


def write_from_file(file_path: str = 'text.txt', interval: float = 0):
    time.sleep(5)

    text = str()
    with open(file_path) as file:
        text = file.read()

    write_lines(text.split('\n'), interval)


def main():
    global FILE_NAME

    root = Tk()
    root.title("Тупа пажилой паук")
    root.geometry("400x300")
    root.attributes("-topmost", True)

    interval_label = Label(root,
                            text='Интервал печати:',
                            font='Arial 18')
    interval_label.pack(side=TOP)

    input_interval = StringVar()

    interval_entry = Entry(root,
                            justify=RIGHT,
                            width=100,
                            textvariable=input_interval,
                            )
    interval_entry.insert(0, '0')
    interval_entry.pack(side=TOP)

    select_button = Button(root,
                            text='Файл: ' + FILE_NAME,
                            background='#C0C0C0',
                            command=lambda: on_choose_click(select_button))
    select_button.pack(side=TOP)

    work_button = Button(root, 
                        text='Начать', 
                        background='#696969',
                        command=lambda: write_from_file(FILE_NAME, float(input_interval.get())))
    work_button.pack(side=BOTTOM, fill=X)
    
    root.mainloop()


if __name__ == '__main__':
    main()