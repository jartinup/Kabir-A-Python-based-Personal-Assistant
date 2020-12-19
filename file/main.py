import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import pyjokes
import pyautogui
import os
import time
import subprocess
import wolframalpha
import json
import requests
from database import find
from pygame import mixer


print('Loading your AI personal assistant - Kabir')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def screenshot(index : int = 0):  
    img = pyautogui.screenshot()
    img.save("screenshots\\img.png")      

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant Kabir")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you?")
        mixer.init()
        mixer.music.load('imp\\init.mp3')
        mixer.music.play()
        

        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Okay, Take Care!')
            print('Okay, Take Care!')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(5)

        elif 'search' in statement:
            result = statement.replace('search', '')
            speak('Searching' + result)
            pywhatkit.search(result)
            speak('results are displayed on your computer screen')
            time.sleep(5)  

        elif 'can i tell you my name' in statement or 'i want to tell you my name' in statement :
            speak("Please Tell me your name")
            rememberMessage = takeCommand()
            speak("you told me that your name is"+rememberMessage)
            remember = open('imp\\username.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'what is my name' in statement or 'who am I' in statement:
            remember = open('imp\\username.txt', 'r')
            speak("Your name is" + remember.read())    

        elif 'what is' in statement:
            answer = statement
            speak('searching about' + answer)
            pywhatkit.info(answer)  
            speak("Here is the result!")
            time.sleep(15)  
            
        elif 'take a screenshot' in statement or 'screenshot' in statement:
            speak("Taking a screenshot")
            screenshot()
            speak("Successfully took a screenshot, You can find it in the screenshots folder")

        elif 'database' in statement:
            speak('What you want to search in database?')
            find(takeCommand())

        elif 'who is' in statement:
             person = statement.replace('who is', '')
             info = wikipedia.summary(person, 3)
             speak("According to Wikipedia Summary")
             print(info)
             speak(info)

        elif 'tell me a story' in statement:
            speak("Preeti will now tell you a story")
            exec(open("file\\storydbase.py").read())

        elif 'tell me a hindi story' in statement or 'tell me a story in hindi' in statement:
            speak("Okay, Playing a Hindi story")
            exec(open("file\\hindistories.py").read())
            
 
        elif 'joke' in statement:
            speak('Here is a joke')
            speak(pyjokes.get_joke())  

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="0e1b082a67108a7eecbec710a4803436"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Kabir, a personal assistant designed by Puneet Gautam. I am programmed to minor tasks like'
                  'doing some calculations, opening youtube ,google chrome ,gmail and stackoverflow, social medias, predict time, search'
                  ' on wikipedia, predict weather in different cities , get top headline news from times of india, tell jokes and you can'
                  ' ask me some questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Puneet Gautam")
            print("I was built by Puneet Gautam")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif "open facebook" in statement:
            webbrowser.open_new_tab("https://facebook.com")
            speak("Here is facebook")
        
        elif "open instagram" in statement:
            webbrowser.open_new_tab("https://instagram.com")
            speak("Here is Instagram")

        elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com")
            speak("Here is GitHub")

        elif "open twitter" in statement:
            webbrowser.open_new_tab("https://twitter.com")
            speak("Here is Twitter")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'take a note for me' in statement or 'make a reminder' in statement:
            speak("Please Proceed")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('imp\\notes.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'speak my notes' in statement or 'remind me' in statement:
            remember = open('imp\\notes.txt', 'r')
            speak("you said me to remember that" + remember.read())
        
       

        elif 'date' in statement:
             speak('sorry, I have a girlfriend')
             print('sorry, I have a girlfriend')

        elif 'are you single' in statement:
             speak('I am in a relationship with Preeti')
             print('I am in a relationship with Preeti')

        elif 'ask' in statement or 'question' in statement:
            speak('Sure, I can answer to some questions and I am still learning, so pardon me if I do not have answer to your questions.')
            question=takeCommand()
            app_id="5WQAW9-RPQP5WW66Q"
            client = wolframalpha.Client('5WQAW9-RPQP5WW66Q')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "calculate" in statement.lower(): 
              
        
            app_id = "5WQAW9-RPQP5WW66Q" 
            client = wolframalpha.Client('5WQAW9-RPQP5WW66Q') 
  
            indx = statement.split().index('calculate') 
            query = statement.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer) 
            print("The answer is " + answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)