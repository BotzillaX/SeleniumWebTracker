from pyautogui import moveTo, screenshot
from time import sleep
from os import getcwd, path
import cv2


def MouseMover():
    moveTo(2, 2)

cwd = getcwd()

filePath = path.dirname(__file__)+"\\"+ path.basename(__file__)
filePath_pictures = path.dirname(__file__)+"\\"
filePath_pictures = path.dirname(path.realpath(__file__))+"\\"+"pictures"+"\\"


def lookingForPixel(name):
    print("looking for " +name )
    MouseMover()
   
    sleep(0.2)
    picture1 = screenshot() #region=(1446, 597, 220, 230) minimap location  #start while in game


    picture1.save(filePath_pictures+"whatsapp.jpg")


    TestJungle = cv2.imread(filePath_pictures+name+".PNG", cv2.IMREAD_UNCHANGED)

    DesktopTest = cv2.imread(filePath_pictures+"whatsapp.jpg", cv2.IMREAD_UNCHANGED)

    nesne = cv2.cvtColor(DesktopTest, cv2.COLOR_BGR2GRAY)

    nesne1 = cv2.cvtColor(TestJungle, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(nesne1, nesne, cv2.TM_CCOEFF_NORMED)
    
    min_val , max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    print("done looking for "+ name)
    
    return max_loc, max_val


if __name__ == "__main__":
    print(lookingForPixel("message"))