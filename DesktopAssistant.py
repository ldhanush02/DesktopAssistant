import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import webbrowser
import pyfiglet
import pywhatkit
import cv2

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Isabella: Listening...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
                break
            except:
                print("Try Again")

print(pyfiglet.figlet_format("I S A B E L L A \nC R E A T E D   B Y\n"))
print(pyfiglet.figlet_format("T E A M \nC A R D I N A L S"))

while True:
    query = command().lower() ## takes user command 
    
    if 'name' in query:
        speak("Hello! My  Name is Isabella and I am Created by my team Cardinals")
    elif 'created you' in query:
        speak("I am Created by team Cardinals")
    elif "what's up" in query:
        speak("Doing good.Thanks for asking") 
    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            cv2.imshow('Input', frame)
            c = cv2.waitKey(1)
            if c == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
    elif "send a message" in query:
        speak("Enter Phone number or Group name")
        phno=input("Enter Phone Number or Group name: ")
        speak("please say your message")
        q1=command()
        speak("at which time message should be delivered")
        h1=int(input("Enter hour(24 hours format): "))
        m1=int(input("Enter minutes(24 hours format): "))
        pywhatkit.sendwhatmsg(phno,q1, h1, m1)
        speak("Message send")
    elif "send a image" in query:
        url="https://th.bing.com/th/id/R.4d467149132aea6da9aacf5421ddf82c?rik=SKlOkssKa92Y6A&riu=http%3a%2f%2fwww.wallpapers13.com%2fwp-content%2fuploads%2f2015%2f12%2fNature-Lake-Bled.-Desktop-background-image-1680x1050.jpg&ehk=iqDwR9dQl7ICwHnf43mg5gcBP%2boZTFX8gnEkw5fBdRI%3d&risl=&pid=ImgRaw&r=0"
        speak("Enter Phone number or Group name")
        phno=input("Enter Phone Number or Group name: ")
        speak("please say your caption to the image")
        q1=command()
        pywhatkit.sendwhats_image(phno, url, q1)
        speak("Image send")
    elif "what's up" in query:
        speak("Doing good.Thanks for asking") 
    elif 'what can you do' in query:
        speak("I can open Facebook,Google,Youtube,Instagram and also I can say jokes,Trending news,play music and can give to accurate time")
    elif 'open youtube' in query:
        url="youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 
    elif 'open google' in query:
        url="google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'search' in query:
        query = query.replace('search',"")
        pywhatkit.search(query)
    elif 'info' in query:
        query = query.replace('info of',"")
        pywhatkit.info(query,lines=4)
    elif 'location' in query:
        url="google.co.in"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 
    elif 'where am i' in query:
        url="https://www.google.co.in/maps/search/maps+location+live"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url) 
    elif 'where is' in query:
        url="https://www.google.co.in/maps/search/maps+location+live/"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        query = query.replace('where is',"")
        speak(wikipedia.summary(query,1))
    elif 'open facebook' in query:
        url="facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'open instagram' in query:
        url="instagram.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with Persons like you")
    ### time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("It's {time} master")
    elif 'play news' in query:
        n=int(input("Select language:\n1) Telugu\n2) Hindi\n3) English\n4) Enter News channel name\n"))
        if(n==1):
            c="TV9 Telugu Live"
        elif(n==2):
            c="NDTV"
        elif(n==3):
            c="IndiaTV"
        elif(n==4):
            speak("say News channel name")
            c=command()    
        pywhatkit.playonyt(c)
    elif 'video song' in query:
        n=int(input("Select language:\n1) Telugu\n2) English\n3) Hindi\n4)say Song name:\n"))
        if(n==1):
            c="https://www.youtube.com/watch?v=OpMJbeC7VV0"
        elif(n==2):
            c="https://www.youtube.com/watch?v=YKLX3QbKBg0"
        elif(n==3):
            c="https://www.youtube.com/watch?v=tionpZAVPd4"
        elif(n==4):
            speak("Say song name")
            c= command()
        pywhatkit.playonyt(c)
    ### celebrity
    elif 'who is' in query:
        query = query.replace('who is',"")
        print(wikipedia.summary(query,4))
        speak(wikipedia.summary(query,4))
    
    ### Joke
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    
    ### news
    elif 'trending news' in query:
            def trndnews(): 
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                page = requests.get(url).json() 
                article = page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                speak("here are the top trending news....!!")
                speak("Do yo want me to read!!!")
                reply = command().lower()
                reply = str(reply)
                if reply == "yes":
                    speak(results)
                else:
                    speak('ok!!!!')
                    pass
            trndnews() 


    ### music
    elif 'music' in query:
        music_dir = 'E:\\music'
        songs = os.listdir(music_dir)
        song = random.randint(0,len(songs)-1)
        print(songs[song])  
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    else:
        speak("I don't understand what you are saying")