import launchpad_py
import time
import random
import numberBinaryColor as nbc
lp=launchpad_py.Launchpad()
lp.ListAll()
lp.Open()
def showNum(number):
    def arrayToDisplay(arr):
        for x in xrange(8):
            for y in xrange(8):
                if arr[y][x]==1:
                    lp.LedCtrlXY(x,y+1,random.randint(1,3),random.randint(1,3))

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


#-----------------MAIN CODE ---------------
# for a in xrange(30):
#
#     showNum(a%10)
#     time.sleep(0.4)
#     lp.Reset()

for num in "13235044924":
    showNum(int(num))
    time.sleep(0.35)
    lp.Reset()
    time.sleep(0.2)
#lp.LedAllOn()

lp.Reset()
