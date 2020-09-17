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
from random import uniform


FILE_NAME = 'text.txt'
DEFAULT_INTERVAL = 0
DEFAULT_TIMEOUT = 5


def createParser ():
	parser = argparse.ArgumentParser()
	parser.add_argument('--source', '-s', type=Path, help='Путь к файлу с текстом, из которого нужно переписать.')
	parser.add_argument('--clipboard', '-clip', type=bool, help='Переписать ли из буффера обмена.')
	parser.add_argument('--interval_start', '-int_s', type=float, help='Начало интервала печати между каждым символом.', default=DEFAULT_INTERVAL)
	parser.add_argument('--interval_end', '-int_e', type=float, help='Конец интервала печати между каждым символом.', default=DEFAULT_INTERVAL)
	parser.add_argument('--timeout', '-t', type=float, help='Задержка перед началом печати.', default=DEFAULT_TIMEOUT)
 
	return parser


def choose_file():
	global FILE_NAME
	FILE_NAME = fd.askopenfilename()


def on_choose_click(button: Button):
	choose_file()
	button['text'] = FILE_NAME


def write_line(line: str, interval_start: float, interval_end: float):
	for symbol in line:
		interval = uniform(interval_start, interval_end) if interval_start < interval_end else interval_start
		pag.write(symbol, interval)


def write_lines(lines: List[str], interval_start: float = DEFAULT_INTERVAL, interval_end: float = DEFAULT_INTERVAL):
	for line in lines:
		write_line(line, interval_start, interval_end)
		pag.write('\n')
		pag.press('home')
		interval = 0


def write_from_file(file_path: str = 'text.txt', interval_start: float = DEFAULT_INTERVAL, interval_end: float = DEFAULT_INTERVAL, timeout: float = DEFAULT_TIMEOUT):
	if not os.path.exists(file_path):
		messagebox.showerror('Ошибка', 'Файл: \"{}\" не найден'.format(file_path))
		return

	time.sleep(timeout)

	text = str()
	with open(file_path) as file:
		text = file.read()

	write_lines(text.split('\n'), interval_start, interval_end)


def write_from_clipboard(root: Tk, interval_start: float = DEFAULT_INTERVAL, interval_end: float = DEFAULT_INTERVAL, timeout: float = DEFAULT_TIMEOUT):
	time.sleep(timeout)

	write_lines(root.clipboard_get().split('\n'), interval_start, interval_end)


def work(file_path: str, interval_start: float, interval_end: float, timeout: float, root: Tk, use_clipboard: bool = False):
	if bool(use_clipboard):
		write_from_clipboard(root, interval_start, interval_end, timeout)
	else:
		write_from_file(file_path, interval_start, interval_end, timeout)


def on_startClick(file_path: str, interval_start: float, interval_end: float, timeout: float, root: Tk, use_clipboard: BooleanVar = None):
	work(file_path, interval_start, interval_end, timeout, root, bool(use_clipboard.get()))


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

	interval_frame = Frame(root)

	input_interval_start = StringVar()
	input_interval_end   = StringVar()

	interval_start_entry = Entry(interval_frame,
							justify=CENTER,
							textvariable=input_interval_start,
							)
	interval_start_entry.insert(0, str(DEFAULT_INTERVAL))
	interval_start_entry.pack(side=LEFT)

	interval_start_label = Label(interval_frame,
							text='с    - ',)
	interval_start_label.pack(side=LEFT)

	interval_end_entry = Entry(interval_frame,
							justify=CENTER,
							textvariable=input_interval_end,
							)
	interval_end_entry.insert(0, str(DEFAULT_INTERVAL))
	interval_end_entry.pack(side=LEFT)

	interval_end_label = Label(interval_frame,
							text='с',)
	interval_end_label.pack(side=LEFT)

	interval_frame.pack(fill=X, side=TOP)

	timeout_label = Label(root,
							text='Задержка перед печатью:',
							font='Arial 18'
							)
	timeout_label.pack(side=TOP)

	input_timeout = StringVar()

	timeout_entry = Entry(root,
							justify=CENTER,
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
											abs(float(input_interval_start.get())),
											abs(float(input_interval_end.get())),
											abs(float(input_timeout.get())),
											root,
											use_clipboard
											)
						)
	work_button.pack(side=BOTTOM, fill=X)
	
	root.resizable(False, False)
	
	root.mainloop()


def main():
	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])

	if namespace.source != None or namespace.clipboard != None:
		work(namespace.source, namespace.interval_start, namespace.interval_end, namespace.timeout, Tk(), namespace.clipboard)
	else:
		window_app_loop()


if __name__ == '__main__':
	main()
