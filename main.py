import pyautogui as pag
import time


def main():
    time.sleep(5)

    text = str()
    with open('test.txt') as file:
        text = file.read()

    lines = text.split('\n')

    for line in lines:
        pag.write(line)
        pag.write('\n')
        pag.press('home')


if __name__ == '__main__':
    main()