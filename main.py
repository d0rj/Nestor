import pyautogui as pag
import time
from typing import List
from tkinter import *
import tkinter.filedialog as fd
from tkinter import messagebox
import os
import sys
import argparse
from pathlib import Path


FILE_NAME = 'text.txt'
DEFAULT_INTERVAL = 0
DEFAULT_TIMEOUT = 5


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', type=Path, help='Путь к файлу с текстом, из которого нужно переписать.')
    parser.add_argument('--clipboard', '-clip', type=bool, help='Переписать ли из буффера обмена.')
    parser.add_argument('--interval', '-int', type=float, help='Интервал печать между каждым символом.', default=DEFAULT_INTERVAL)
    parser.add_argument('--timeout', '-t', type=float, help='Задержка перед началом печати.', default=DEFAULT_TIMEOUT)
 
    return parser


def choose_file():
    global FILE_NAME
    FILE_NAME = fd.askopenfilename()


def on_choose_click(button: Button):
    choose_file()
    button['text'] = FILE_NAME


def write_lines(lines: List[str], interval: float = DEFAULT_INTERVAL):
    for line in lines:
        pag.write(line, interval)
        pag.write('\n')
        pag.press('home')


def write_from_file(file_path: str = 'text.txt', interval: float = DEFAULT_INTERVAL, timeout: float = DEFAULT_TIMEOUT):
    if not os.path.exists(file_path):
        messagebox.showerror('Ошибка', 'Файл: \"{}\" не найден'.format(file_path))
        return

    time.sleep(timeout)

    text = str()
    with open(file_path) as file:
        text = file.read()

    write_lines(text.split('\n'), interval)


def write_from_clipboard(root: Tk, interval: float = DEFAULT_INTERVAL, timeout: float = DEFAULT_TIMEOUT):
    time.sleep(timeout)

    write_lines(root.clipboard_get().split('\n'), interval)


def work(file_path: str, interval: float, timeout: float, root: Tk, use_clipboard: bool = False):
    if bool(use_clipboard):
        write_from_clipboard(root, interval, timeout)
    else:
        write_from_file(file_path, interval, timeout)


def on_startClick(file_path: str, interval: float, timeout: float, root: Tk, use_clipboard: BooleanVar = None):
    work(file_path, interval, timeout, root, bool(use_clipboard.get()))


def window_app_loop():
    global FILE_NAME

    root = Tk()
    root.title("Nestor")
    root.geometry("400x300")
    root.attributes("-topmost", True)

    interval_label = Label(root,
                            text='Интервал печати:',
                            font='Arial 18'
                            )
    interval_label.pack(side=TOP)

    input_interval = StringVar()

    interval_entry = Entry(root,
                            justify=RIGHT,
                            width=100,
                            textvariable=input_interval,
                            )
    interval_entry.insert(0, str(DEFAULT_INTERVAL))
    interval_entry.pack(side=TOP)

    timeout_label = Label(root,
                            text='Задержка перед печатью:',
                            font='Arial 18'
                            )
    timeout_label.pack(side=TOP)

    input_timeout = StringVar()

    timeout_entry = Entry(root,
                            justify=RIGHT,
                            width=100,
                            textvariable=input_timeout,
                            )
    timeout_entry.insert(0, str(DEFAULT_TIMEOUT))
    timeout_entry.pack(side=TOP)

    select_button = Button(root,
                            text='Файл: ' + FILE_NAME,
                            background='#C0C0C0',
                            command=lambda: on_choose_click(select_button),
                            width=200
                            )
    select_button.pack(side=TOP)

    use_clipboard = BooleanVar()
    use_clipboard.set(0)
    clipboard_box = Checkbutton(
        text='Из буффера обмена',
        variable=use_clipboard,
        onvalue=1,
        offvalue=0
    )
    clipboard_box.pack(side=TOP)

    work_button = Button(root, 
                        text='Начать', 
                        background='#696969',
                        command=lambda: 
                            on_startClick(FILE_NAME,
                                            abs(float(input_interval.get())),
                                            abs(float(input_timeout.get())),
                                            root,
                                            use_clipboard
                                            )
                        )
    work_button.pack(side=BOTTOM, fill=X)
    
    root.mainloop()


def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.source != None or namespace.clipboard != None:
        work(namespace.source, namespace.interval, namespace.timeout, Tk(), namespace.clipboard)
    else:
        window_app_loop()


if __name__ == '__main__':
    main()
