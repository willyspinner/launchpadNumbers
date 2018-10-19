import launchpad_py
import time
import random
import numberBinaryColor as nbc
import letters8By8 as letters
import signal
import sys
lp=launchpad_py.Launchpad()
lp.ListAll()
lp.Open()
def arrayToDisplay(arr):
    for x in range(8):
        for y in range(8):
            if arr[y][x]==1:
                lp.LedCtrlXY(x,y+1,random.randint(1,3),random.randint(1,3))

def showNum(number):
    if number==0:
        arrayToDisplay(nbc.zero)
    elif number==1:
        arrayToDisplay(nbc.one)
    elif number==2:
        arrayToDisplay(nbc.two)
    elif number==3:
        arrayToDisplay(nbc.three)
    elif number==4:
        arrayToDisplay(nbc.four)
    elif number==5:
        arrayToDisplay(nbc.five)
    elif number==6:
        arrayToDisplay(nbc.six)
    elif number==7:
        arrayToDisplay(nbc.seven)
    elif number==8:
        arrayToDisplay(nbc.eight)
    elif number==9:
        arrayToDisplay(nbc.nine)


def showLetter(letter):
    matrix=[]
    try:
        matrix=letters.letters8x8[letter.upper()]
    except KeyError:
        matrix=[
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        ]
    arrayToDisplay(matrix)

#-----------------MAIN CODE ---------------
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    lp.Reset()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to stop.')

while True:
    for i in "AMZN1252.10:GOOGL1200.2":
    #for i in "2:04am":
        print("doing:",i)
        if(str.isnumeric(i)):
            showNum(int(i))
        else:
            showLetter(i)
        time.sleep(0.20)
        #time.sleep(0.30)
        lp.Reset()
        time.sleep(0.10)
    lp.Reset()
