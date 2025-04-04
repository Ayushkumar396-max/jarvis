import pywhatkit as kit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep, strftime
import os 
from datetime import timedelta
from datetime import datetime



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
engine.setProperty("rate",200)


# text to speech 

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
    
    
    
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("listening.....")
         r.adjust_for_ambient_noise(source)
         r.pause_threshold = 1
         r.energy_threshold = 300
         audio = r.listen(source,0,4)
         
        
         
     
    try: 
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
        
        
        
        
    except Exception as e:
        speak("say that explain again please....")
        return "none"
    
    return query 


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))


def sendMessage():
    speak("who do you want to send to message")
    a = int(input('''person 1 - 1
    person 2 - 2'''))
    if a ==1:
        speak("whats the message")
        message = str(input("Entet the message-"))
        kit.sendwhatmsg("+917858882440",message,time_hour=strTime,time_min=update)
        
    elif a==2:
         pass
    
    