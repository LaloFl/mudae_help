import pyautogui as pag
import time
import sys

ROLLS = int(sys.argv[1])

def roll():
    pag.write('/pokeslot')
    time.sleep(0.2)
    pag.keyDown('enter')
    pag.keyDown('enter')

def main():
    app = pag.getWindowsWithTitle('Discord')[0]
    app.maximize()
    app.activate()
    pag.keyDown('tab')
    for i in range(ROLLS):
        roll()
        time.sleep(3)
    

if __name__ == '__main__':
    main()
