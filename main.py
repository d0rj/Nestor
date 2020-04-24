import pyautogui as pag
import time
from typing import List


def write_lines(lines: List[str], interval: float = 0):
    for line in lines:
        pag.write(line, interval)
        pag.write('\n')
        pag.press('home')


def write_from_file(file_path: str = 'text.txt', interval: float = 0):
    text = str()
    with open(file_path) as file:
        text = file.read()

    write_lines(text.split('\n'), interval)


def main():
    time.sleep(5)

    write_from_file()


if __name__ == '__main__':
    main()