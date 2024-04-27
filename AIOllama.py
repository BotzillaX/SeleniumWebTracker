import pytesseract
from PIL import Image
import ollama
import pyautogui as py
import time
from keyboard import is_pressed, press_and_release, write
gameMode = "normal 5 vs 5"

toplane = "[myself]Gwen vs [enemyTeam]Garen"
jungle  = "[myTeam]Nocturne vs [enemyTeam]Yorick"
midlane = "[myTeam]Vladimir vs [enemyTeam]Yasuo"
adc = "[myTeam]VAyne vs [enemyTeam]Samira"
support = "[myTeam]Poppy vs [enemyTeam]Ashe"



inputBeforeChat = f"""Schauspielere den Käufer des Artikels, der einen Artikel auf Kleinanzeigen kaufen möchte. Die bist freundlich, nciht aufdringlich, hälst dich kurz, schreibst, auf deutscher sprache aber professionell"""






def ollamaGPT(inputBeforeChat):
            
            
    # Create an instance of the client
    client = ollama.Client()

    # Define your message as a list of dictionaries
    
    message = [
        {"role": "user", "content": inputBeforeChat}
    ]
    print(message)
    # Call the chat method with the model and message
    response = client.chat("llama3:8b", message)

    # Print the response
    return response["message"]["content"]







if __name__ == "__main__":
    ollamaGPT(inputBeforeChat)