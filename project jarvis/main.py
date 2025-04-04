# from calendar import c
import instaloader
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
from bs4 import BeautifulSoup
import requests
import webbrowser
import pywhatkit as kit
import pyautogui
import pyperclip  
import time

import smtplib  
import sys






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
    
    
    
# text to speech 
    
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


#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('20ayushjha@gmail.com','22222789')
    server.close()
    
 #for opening google
   
   
   
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
           
   
  #for opening wikipedia 
            
    
        
        
def searchwikipedia(query):
    if "wikipedia" in query:
       speak("Searching from wikipedia....")
             
       query = query.replace("wikipedia","")      
       
       query = query.replace("search wikipedia","")
       
       query = query.replace("jarvis","")
       
       #construct the wikipedia url and the featch content
       
       search_url = (f"https://en.wikipedia.org/wiki/(query)")
       response = requests.get(search_url)
       
       # Parse the html response
       soup = BeautifulSoup(response.text, features="html.parser")
       
       # Extract the first paragraph as a summary
       
       summary = soup.find('div',{'class': 'reflist'}).text if soup.find('div', {'class':'reflist'}) else "No speak available."
       
       
       results =wikipedia.summary(query,sentences = 2)
       speak("According to wikipedia....")
       print(results)
       speak(results)
               
        
        
       
                   
 
            
            
            

 
 
 
 
 
 
 
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0  and hour<=12:
        speak("Good morning  ,sir")
        
    elif hour>=12  and hour<=18:
        speak("Good afternoon ,sir")
        
    else:
        speak("Good evening ,sir")
        
    speak("i am jarvis please tell me how can i help you")
        
    
       
    
    
    
   
    
if __name__=="__main__":
    wish()
    while True:   #to run this code infinite 
        
        query = takecommand().lower()
        
        
        
        
        #logic building for tasks
        
        
        if "open notepad" in query:
            npath = "c:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif "close notepad " in query:
             speak("okay sir clossing notepad")
             os.system("taskkill /f /im notepad.exe")
             
            
        elif "shutdown" in query:
             os.system("shutdown /s /t 5")
            
            
        elif "hello" in query:
            speak("Hello sir, how are you")
        elif "  fine" in query:
            speak("great, sir")
        elif " who made " in query:
            speak("my boss Ayush")
        elif "thank you "in query:
            speak("you are welcome, sir")
            
            
            
        
            
            
            
        # elif "wikipedia" in query:
        #     speak("searching wikipedia.....")
        #     query = query.replace("wikipedia","")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("according to wikipedia")
        #     speak(results)
        #     print(results)
        

        
            


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
            
            
        # elif c.lower().startswith("play"):
        #  song = c.lower().split(" ")[1]
        # link = musiclibrary.music[song]
        # webbrowser.open(link)
      
            
            
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com") 
            
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            
        elif "open google" in query:
            
            webbrowser.open(f"www.google.com")
            
        
        elif "google" in query:
            from Searchnow import searchGoogle
            searchGoogle(query)
            
            
        elif "wikipedia" in query:
            from Searchnow import wikipedia
            searchwikipedia(query)
            
            
        # elif "Youtube" in query:
        #     from Searchnow import youtube
        #     searchYoutube(query)
            
      
        
            
            
        elif "send message" in query:
            kit.sendwhatmsg("+919835611822", "Hello how are you",00,00)
          
          
          
        elif "play skyfall on youtube" in query:
            
            
            
            webbrowser.open("https://youtu.be/sZrTJesvJeo?si=MBk15_2nhQbZ7r1b ")
          
              
        elif "play Race theme on youtube" in query:
            webbrowser.open("https://youtu.be/aPZep2m43JM?si=y7ARytm25lCGmyGA ")
            
              
        elif "play  Diet mountain Dew on youtube" in query:
            webbrowser.open("https://youtu.be/StZXT82TtX4?si=wCqIiKD0p5CyrDly ")
              
        elif "play video on youtube" in query:
            webbrowser.open("https://youtu.be/sc5MQSgum84?si=4mu3i9wBX016h3bL ")
            
            
            
        elif "email" in query:
           try:
               speak("what should i send to ayush")
               content = takecommand().lower()
               to = "20ayushjha@gmail.com"
               sendEmail(to, content)
               speak("Email has been sent to ayush")
               
               
           except Exception as e:
               print(e)
               speak ("sorry sir, i  am not able to sent this email to ayush")
               
               
         
         
         
         
         
        elif "temperature" in query:
            search = "temperature   in bhilai"
            
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")
            
            
        
         
        elif "weather" in query:
            search = "weather  in Bhilai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")
            
            
         
         
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir , the time is {strTime}")
                                                      
         
        elif "instagram profile" in query :
            speak("sir please enter the user name correctly.")
            name = input("Enter the username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is thr profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download the profile pic of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only= True)
                speak("i am done sir, profile pic is saved in our main foulder .")
                
            else:
                pass
            
            
            
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file ")
            name = takecommand().lower
            speak("please sir hold the screen for few second, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder")
                
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            
            sys.exit()
            
            
        speak("sir,do you have any other work") 
        
    