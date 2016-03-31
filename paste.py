#import os,sys
import time
import win32api, win32con, clipboard
import left
x_pad = 0
y_pad = 0

#VK_CODE = 'ctrl':0x11 +'v':0x56


def mousePos(cord):
    win32api.SetCursorPos((x_pad+cord[0],y_pad+cord[1]))
   
    

def press():
    win32api.keybd_event(0x11,0,0,0)  #ctrl press
    
    win32api.keybd_event(0x56,0,0,0)  # v press
    
    win32api.keybd_event(0x56,0,win32con.KEYEVENTF_KEYUP,0)  #v release
    win32api.keybd_event(0x11,0,win32con.KEYEVENTF_KEYUP,0)  #ctrl release

    win32api.keybd_event(0x0D,0,0,0)  # v press              #enter
    win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)  #enter
    



def labReport():

    mousePos((20,741)) #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    print "1. labReport module run successfully"

def opLabs():

    mousePos((53,73))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    print "2. opLabs module run successfully"


def opLaboratory():

    mousePos((549,405))   #setting mouse cursor position
    left.leftClick()      #left click on cursor position
    time.sleep(3)         # time between next cursor position
    print "3. opLaboratory module run successfully"

def pmrnNo():

    mousePos((23,412))
    left.leftClick()
    press()
    print "4. pmrnNo module run successfully"

def showAll():

    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    print "5. showAll module run successfully"

def patientName():

    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    print "6. patientName module run successfully"

def tests():

    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position

    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    press()
    print "7. tests module run successfully"


def notListed():
    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    print "8. notListed module run successfully"

def printDirect():
    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    
    
    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    
    press()
    print "9. printDirect module run successfully"

def save():
    
    mousePos((-114,78))  #setting mouse cursor position
    left.leftClick()     #left click on cursor position
    time.sleep(.2)       # time between next cursor position
    print "10. save module run successfully"
    


labReport()
opLabs()
opLaboratory()
pmrnNo()
showAll()
patientName()
tests()
notListed()
printDirect()
save()





