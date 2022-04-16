import pyautogui as pag
import time
import sys

testing = True and False

X_REACTION = 361
Y_REACTION = 945
IDLE_POS = [800, 600]
ROLLS = 0 if testing else int(sys.argv[1])
KAKERA_REACT = False if testing else sys.argv[2].upper() == 'Y'

badColors = {
    'normal': (47, 49, 54),
    'yellow': (210, 199, 103),
    'yellow2': (224, 213, 111),
    'green': (108, 213, 97),
    'blue': (76, 200, 209),
}
goodColors = {
    'free': (163, 109, 228),
}
badColorsArr = list(badColors.values())
goodColorsArr = list(goodColors.values())
claimColor = (92, 76, 76)

def moveToIdlePos():
    pag.moveTo(x=IDLE_POS[0], y=IDLE_POS[1])
def roll():
    pag.write('/wa')
    time.sleep(0.2)
    pag.keyDown('enter')
    pag.keyDown('enter')
def isWish():
    color = pag.pixel(x=800, y=600)
    return (color != (50, 53, 59) and color != (54, 57, 63))
def claim():
    pag.rightClick(x=800, y=600)
    pag.click(x=820, y=630)
def clickReact():
    pag.leftClick(x=X_REACTION, y=Y_REACTION)
def searchKakera():
    px = pag.pixel(x=X_REACTION, y=Y_REACTION)
    return px not in badColorsArr
def rt():
    pag.write('$rt')
    pag.keyDown('enter')

def main():
    app = pag.getWindowsWithTitle('Discord')[0]
    
    app.maximize()
    app.activate()
    pag.keyDown('tab')
    for i in range(ROLLS):
        roll()
        time.sleep(3)
        if isWish():
            clickReact()
            print('Wish claimed')
            if ROLLS - i > 40:
                rt()
                print('Used $rt')
            continue
        if searchKakera() and KAKERA_REACT:
            clickReact()
            print('Kakera reacted')
        moveToIdlePos()
        time.sleep(0.3)
    
def test():
    while(True):
        print(pag.pixel(x=X_REACTION, y=Y_REACTION))
        print(searchKakera())
        time.sleep(1)

if __name__ == '__main__':
    test() if testing else main()
