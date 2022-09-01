# Luna 0.2 Prototype l 2022

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from deep_translator import GoogleTranslator
from deep_translator import LingueeTranslator
import psutil
import speedtest
import pyjokes
import pyautogui
from datetime import date
import subprocess


print('Hi, Im Luna. Is anyone here?')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate", 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            Luna_Recorder=r.recognize_google(audio,language='en')
            print(f"Your Record:{Luna_Recorder}\n")

        except Exception as e:
            speak("Sir?")
            return "None"
        return Luna_Recorder

speak("Process is online")
time.sleep(1)



if __name__=='__main__':


    while True:
        speak("What's your order?")
        Luna_Recorder = takeCommand().lower()
        if Luna_Recorder==0:
            continue

        if 'stop' in Luna_Recorder:
            speak('Process is offline')
            print('Cya...')
            break


        elif 'open spotify' in Luna_Recorder:
            speak("Spotify is opening...")
            subprocess.Popen("C:/Users/doguy/AppData/Roaming/Spotify/Spotify.exe")
            
        elif 'open opera' in Luna_Recorder:
            speak("Opera is opening...")
            subprocess.Popen("C:/Users/doguy/AppData/Local/Programs/Opera GX/launcher.exe")
            
        elif 'wikipedia' in Luna_Recorder:
            speak('Searching Wikipedia...')
            Luna_Recorder =Luna_Recorder.replace("wikipedia", "")
            results = wikipedia.summary(Luna_Recorder, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
           
        elif "open instagram" in Luna_Recorder:
            speak("Instagram is opening")
            time.sleep(1)
            webbrowser.open_new_tab("https://www.instagram.com")
            
        elif "hey" in Luna_Recorder:
            speak("yes sir?")
            continue
            
        elif 'open youtube' in Luna_Recorder:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is opening")
            time.sleep(2)
            
        elif 'screenshot' in Luna_Recorder:
            speak("I'm taking a screenshot")
            img=pyautogui.screenshot()
            img.save("C:/Assistant/ss.png")
            speak("You can find your screenshot in Assistant file")
        
        elif 'remember that' in Luna_Recorder:
            remember=open("data.txt","r")
            speak("you said me to remember that" + remember.read())
        
        elif 'tell me a joke' in Luna_Recorder:
            speak(pyjokes.get_joke())

        elif 'open google' in Luna_Recorder:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(2)
            
        elif 'open twitter' in Luna_Recorder:
            speak("Twitter is open now")
            webbrowser.open_new_tab("https://twitter.com/home")
            time.sleep(2)            
            
        elif 'off' in Luna_Recorder:
            os.system("shutdown /r /t 1")
        
        elif 'open gmail' in Luna_Recorder:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(2)
            
        elif 'open my gmail'in Luna_Recorder:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            speak("Your Email is opening")
            time.sleep(2)
            
        elif 'open my github' in Luna_Recorder:
            webbrowser.open_new_tab("https://github.com/Doguhannilt")
            speak("Your GitHub is opening")
            time.sleep(2)
        
        elif 'translate' in Luna_Recorder:
            speak('Ill translate your words till you say stop')
            time.sleep(3)
            words = Luna_Recorder
            time.sleep(5)
            translated_word = LingueeTranslator(source='english', target='german').translate(words)
            speak(translated_word)
            print(translated_word)

        elif "what time is it" in Luna_Recorder:
            today = date.today()
            speak(today)
            
        elif 'time' in Luna_Recorder:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in Luna_Recorder or 'what can you do' in Luna_Recorder:
            speak('I am LUNA and i am here to help you with my knowledge')

        elif "open stackoverflow"in Luna_Recorder or "stackoverflow" in Luna_Recorder:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in Luna_Recorder:
            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=tr&gl=TR&ceid=TR:tr")
            speak('Here we are')
            time.sleep(2)

        elif 'search'  in Luna_Recorder:
            Luna_Recorder = Luna_Recorder.replace("search", "")
            webbrowser.open_new_tab(Luna_Recorder)
            time.sleep(2)

        elif 'ask' in Luna_Recorder:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
        elif 'favorite music' in Luna_Recorder:
            speak("My favorite music? Hmmm, I think my favorite music is")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=dVVZaZ8yO6o")
        
        elif 'how much battery' in Luna_Recorder:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"Mam our system have {percentage} percent battery.")
            if percentage>=75:
                speak("We have enough battery")
            elif percentage>40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery.")
            elif percentage<=15 and percentage<=30:
                speak("We don't have enough battery, please connect charging system ")
            elif percentage<=15:
                speak("we have very low battery, please connect charging system will shutdown soon.")

        elif 'internet speed' in Luna_Recorder:
            st=speedtest.Speedtest()
            d1=st.download()
            up=st.upload()
            speak(f"we have {d1} bit per second downloading speed and {up} bit per second uploading speed.")
            
        elif 'find location' in Luna_Recorder:
            speak('Write the location that you want to find')
            location = input("Location:")
            time.sleep(5)
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            speak("I think i find it, the location of")
            webbrowser.open_new_tab(url)
            
            
        elif 'google' in Luna_Recorder:
            speak("What do you want to search?")
            time.sleep(1)
            Here = input("Write Here: ")
            search = Here
            time.sleep(10)
            url = 'https://google.com/search?q=' + search
            speak('Let me see')
            time.sleep(2)
            webbrowser.get().open(url)
        
        elif 'reference' in Luna_Recorder:
            speak('Thanks to all genius guys that helped me to make that assistant')

        elif "log off" in Luna_Recorder or "sign out" in Luna_Recorder:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)