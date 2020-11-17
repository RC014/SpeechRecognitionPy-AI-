import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id') #Cifra indica tipuk vocii(0-Barbat;1-Femeie)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Salut, buna dimineata")
        print("Salut, buna dimineata!")
    elif hour>=12 and hour<18:
        speak("Salut, buna ziua")
        print("Salut, buna ziua")
    else:
        speak("Salut, buna seara")
        print("Salut, buna seara")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ascult...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='ro')
            print(f"Utilizatorul a spus:{statement}\n")

        except Exception as e:
            speak("Scuze, nu am inteles, mai repeta o data")
            return "None"
        return statement

print("Lansarea asistentului tau personal")
speak("Lansarea asistentului tau personal")
wishMe()

if __name__=='__main__':


    while True:
        speak("Cu ce te pot ajuta?")
        statement = takeCommand().lower()
        if statement==0:
            continue

if "pa" in statement or "la revedere" in statement or "stop" in statement:
            speak('Asistentul tau personal opreste, pa')
            print('Asistentul tau personal opreste, pa')
            break

if 'wikipedia' in statement:
            speak('Caut in Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("Conform informatiei din Wikipedia:")
            print(results)
            speak(results)
elif 'deschide youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube s-a deschis")
            time.sleep(5)
elif 'deschide google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome s-a deschis")
            time.sleep(5)
elif 'deschide gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail s-a deschis")
            time.sleep(5)
elif 'ora' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
elif "camera" in statement or "fa o fotografie" in statement:
            ec.capture(0,"robo camera","img.jpg")
elif 'cauta'  in statement:
            statement = statement.replace("cauta", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)	
elif 'intrebare' in statement:
            speak('Pot raspunde la intrebari de calcul si geografice, ce vreai sa stii?')
            question=takeCommand()
            app_id="Introdu ID-ul tau unic aici"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
elif "deconecteaza tot" in statement or "stinge tot" in statement:
            speak("Ok , calculatorul tau va deconecta in 10 secunde, verifica daca ai iesit din toate aplicatiile")
            subprocess.call(["shutdown", "/l"])
			
time.sleep(3)
