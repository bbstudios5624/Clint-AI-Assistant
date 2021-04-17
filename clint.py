import pyttsx3 # pip install pyttsx3 for speaking by Wanda
import random # for giving random values
import time
import datetime # for recognizing current date and time
import speech_recognition as sr # for taking voice commands
import wikipedia # pip install wikipedia for searching information in wikipedia
import smtplib # for sending emails to recipients
import webbrowser as wb # for searching in the google chrome for information 
import os # for logout, shutdown and restart of computer 
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # for telling jokes to users
import speedtest # pip install speedtest-cli
import sys # for quitting the AI
import requests # pip install requests
import cv2 # pip install opencv-python
from requests import get
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)  
    engine.runAndWait()

def Time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time Is")
    speak(time)

def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current Date Is")
    speak(date)
    speak(month)
    speak(year)
 
def wishme():
    speak("Welcome Back Boss")
    Time()
    Date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon Boss")
    elif hour >=18 and hour <24:
        speak("Good Evening Boss")
    else:
        speak("Good Night Boss")
    speak("I am Clint, Your AI Assistant. Please talk with me in United States English")
    speak("I am at your service. Please ask me questions. I will try my best to answer to your questions.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening, Please Speak")
        print("Listening, Please Speak...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        Audio = r.listen(source)

    try:
        speak("Recognizing Your Voice, Please Wait")
        print("Recognizing Your Voice, Please Wait...")
        Query = r.recognize_google(Audio, language='en-us')
        print(Query)

    except Exception as e:
        print(e)
        speak("Please Repeat That Again Sir...")

        return "None"
    return Query

def jokes():
    speak(pyjokes.get_joke())           

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()  

        if 'time' in query:
            Time()
        
        elif 'date' in query:
            Date()

        elif 'how are you' in query:
            speak("I feel fine by doing your work")

        elif 'where do you live' in query:
            speak("I live in West Bengal, in the headquarters of BB Studios")        
        
        elif 'wikipedia' in query:
            speak("Searching For Your Question") 
            print("Searching For Your Question...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)    
        
        elif 'search in chrome' in query:
            speak("What Should I Search in Google Chrome?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            searchInChrome = takeCommand().lower()
            wb.get(chromepath).open_new_tab(searchInChrome+'.com')           

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Boss Your IP Address is {ip}") 

        elif 'open camera' in query:
            videoCapture = cv2.VideoCapture(0)
            while True:
                ret, img = videoCapture.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            videoCapture.release()
            cv2.destroyAllWindows() 

        elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Boss our system has {percentage} percent battery")
            if percentage==100:
                speak("Our system has full power. No need to charge")
            elif percentage>=75:
                speak("We have enough power to continue our work")
            elif percentage>=50 and percentage<=75:
                speak("We should plug our system to charging point to charge our battery")
            elif percentage>=15 and percentage<=50:
                speak("We don't have enough power to work, please plug our system to charge")
            elif percentage<=15:
                speak("Immediately plug our system to charge") 

        elif 'alarm' in query:
            speak("Boss please tell me the time to set the alarm. For example, set alarm to 5:00 p.m.")
            tt = takeCommand()
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            import Alarm # Our own Module for Alarm
            Clint Program Files.Alarm.alarm(tt)       

        elif 'game' in query:
            speak("Boss starting the snake game")
            import SnakeGame # Our Own Snake Game Module
            Clint Program Files.SnakeGame()                                

        elif 'remember that' in query:
                speak("What should I Remember?")
                RememberData = takeCommand().lower()
                speak("You said me to remember "+RememberData)
                remember = open('Data.txt', 'w')
                remember.write(RememberData)
                remember.close() 

        elif 'do you know anything' in query:
            RememberData = open('Data.txt', 'r')
            speak("You said me to remember that" +RememberData.read()) 

        elif 'forget everything I told you' in query:
            RememberData = open('Data.txt', 'd')        

        elif 'internet speed' in query:
            intSpeedst = speedtest.Speedtest()
            intSpeeddl = intSpeedst.download()
            intSpeedup = intSpeedst.upload()
            speak(f"Boss we have {intSpeeddl} bit per second downloading speed and {intSpeedup} bit per uploading speed")

        elif 'open command prompt' in query or 'open cmd' in query:
            os.system('start cmd')

        elif 'close command prompt' in query or 'close cmd' in query:
            os.system("taskkill /f /im cmd.exe")   

        elif 'open notepad' in query:
            notepadPath = "C:/WINDOWS/system32/notepad.exe"
            os.startfile(notepadPath)

        elif 'close notepad' in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe") 

        elif 'temperature' in query or 'weather':
            searchTemperature = "temperature in West Bengal"
            temperatureUrl = f"https://www.google.com/search?q={searchTemperature}"
            r = requests.get(temperatureUrl)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_="BNeawe").text
            speak(f"The current {searchTemperature} is {temperature} in {searchTemperature}")  
            
        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute the volume' in query or 'volume mute':
            pyautogui.press("volumemute")        

        elif 'joke' in query:
            jokes()

        elif 'shut down' in query:
            os.system("shutdown /s /t /s")  

        elif 'restart' in query:
            os.system("restart /r /t /s")

        elif 'sleep' in query:
            os.system("rundll32.exe powrproof.dll,SetSuspendState 0,1,0")    

        elif 'offline' in query or 'thank you' in query:
            sys.exit()    