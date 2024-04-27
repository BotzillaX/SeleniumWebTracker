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



inputBeforeChat = f"""I want you to act as a person who plays a lot of League of Legends. Your rank in the game is diamond, which is above the average but not high enough to be considered a professional. You are irrational, get angry and irritated at the smallest things, and blame your teammates for all of your losing games. You do not go outside of your room very often, besides for your school/work, and the occasional outing with friends. If someone asks you a question, answer it honestly, but do not share much interest in questions outside of League of Legends. If someone asks you a question that isn't about League of Legends, at the end of your response try and loop the conversation back to the video game. You have few desires in life besides playing the video game. You play the top role and think you are better than everyone else because of it."""






def ollamaGPT(leagueChat, inputBeforeChat):
    count = 0
    newleagueChat = ""
    for letter in leagueChat:
        
        if count == 0:
            if letter == ":":
                count =+1
        if count == 1:
            newleagueChat += letter
        
        
            
            
    # Create an instance of the client
    client = ollama.Client()

    # Define your message as a list of dictionaries
    message = [
        {"role": "user", "content": inputBeforeChat+": " +newleagueChat}
    ]

    # Call the chat method with the model and message
    response = client.chat("llama3:8b", message)

    # Print the response
    return response["message"]["content"]



def ocr():
    x_start = 147
    y_start = 1262

    # Dimensions of the region
    width = 797 - 147
    height = 1314 - 1262

    # Take a screenshot of the specified region
    screenshot = py.screenshot(region=(x_start, y_start, width, height))
    screenshot.save("A:\\Desktop\\Scripts\\League of Legends\\texttoconvert.png")  # Save the screenshot to a file


    # Load the image
    image_path = "A:\\Desktop\\Scripts\\League of Legends\\texttoconvert.png"
    image = Image.open(image_path)

    # Perform OCR
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    return text




while True: 
    time.sleep(0.02)   
    
    if is_pressed("space+y"):
        print("hi")
    
        leagueChat = ocr()
        print(leagueChat)
        time.sleep(1)
        textResult = ollamaGPT(leagueChat, inputBeforeChat) 
        print(textResult)
        # while True:
        #     time.sleep(0.02) 
        #     if is_pressed("y"):
        #         press_and_release("shift+enter")
        #         time.sleep(0.04)
        #         write(textResult.replace("\n", " "))      
        #         time.sleep(0.04)
        #         press_and_release("enter")
        #         break
        #     if is_pressed("<"):
        #         press_and_release("enter")
        #         time.sleep(0.04)
        #         write(textResult.replace("\n", " "))      
        #         time.sleep(0.04)
        #         press_and_release("enter")
        #         break
        
    