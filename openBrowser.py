from keyboard import press_and_release, write
from time import sleep
from pyautogui import displayMousePosition, click

url = 123
def openBrowser1(url):
    click(273,75)
    sleep(0.2)
    write(url)
    sleep(0.2)
    press_and_release("enter")
    
   



if __name__ == "__main__":
    
    openBrowser1(url)
    