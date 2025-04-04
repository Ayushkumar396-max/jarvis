import pyttsx3
import pywhatkit as kit
import wikipedia
import webbrowser

import speech_recognition as sr

from main import speak


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


query = takecommand().lower()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
engine.setProperty("rate",170)


# text to speech 

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def searchGoogle(query):
   if "google" in query:
       import wikipedia as googleScrap
       query = query.replace("jarvis","")
       
       query = query.replace("google search","")
       
       query = query.replace("google","")
       speak("this is what i found on google")
       
       
       try:
           kit.search(query)
           results = googleScrap.summary(query,1)
           speak(results)
           
           
           
       except:
           speak("No speakable output is available")
           
           
def searchYoutube(query):
    if "youtube" in query:
        speak("this is what i found for your search!")
        
        query = query.replace("youtube search","")
       
        query = query.replace("youtube","")
           
        query = query.replace("jarvis","")
       
       
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        kit.playonyt(query)
        speak("Done sir")
        
        
 
 
def searchwikipedia(query):
    if "wikipedia" in query:
       speak("Searching from wikipedia....")
             
       query = query.replace("wikipedia","")      
       
       query = query.replace("search wikipedia","")
       
       query = query.replace("jarvis","")
       
       results =wikipedia.summary(query,sentences = 2)
       speak("According to wikipedia....")
       print(results)
       speak(results)
        