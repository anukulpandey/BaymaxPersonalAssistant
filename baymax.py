# Importing all the modules
import pyttsx3 as ps
import speech_recognition as sr
import os
import time
from datetime import datetime
import wolframalpha
import webbrowser
import wikipedia
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
# Defining all functions here
engine = ps.init()
engine.setProperty('rate', 175)
def greet(greeting):
    engine.say(f"{greeting}")
    engine.runAndWait()

def listen():
    hear=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        hear.pause_threshold = 1
        audio = hear.listen(source)
        query = hear.recognize_google(audio, language='en-in')
    return query

def error():
    try:
            listenedAudio =listen()
            print("Recognizing...")
            print(listenedAudio)
    except Exception as e:
            greet("Please say it again")
            listenedAudio =listen()
            print("Recognizing...")
            print(listenedAudio)
# Program Starts here
if __name__=="__main__":
        i=1
        if(i==1):
            greet("Hello\n I am Beymax! To order me tell me your identity")
            greet('Please enter your username')
        print('Enter your username here:',end="")
        cred={'username':'anukul','password':1234}
        username=input()
        if cred['username']==username:
            greet("Welcome Back Sir!\nPlease enter password to continue")
            print("Enter your password here:",end="")
            passinput=int(input())
            if passinput==cred['password']:
                while True:
                    greet("Yes Sir! What do you want me to do?")
                    try:
                        listenedAudio=listen()
                        print(listenedAudio)
                    except Exception as e:
                        greet("Can you please repeat?")
                        listenedAudio=listen()
                        print(listenedAudio)

                    if "open chrome" in listenedAudio.lower():
                        path="C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
                        os.startfile(path)
                    elif "who are you" in listenedAudio:
                        greet("I am beymax! You programmed me to help you whenever you feel lazy, I always remind you about important stuff. And I am your first creation.\n I hope I will have a special place in your heart")
                    elif "time" in listenedAudio.lower():
                        greet(f"time now is {current_time}")
                    elif "question" in listenedAudio.lower():
                        while True:
                            try:
                                listenedAudio=listen()
                                break
                            except Exception as e:
                                greet("Sir ! I did not get you, can you please repeat?")
                        print(f'Question>{listenedAudio}')
                        greet("Searching your answer on the web")
                        print("Searching your answer on the web")
                        question=listenedAudio
                        app_id="3YP882-2HX3JK532R"
                        client=wolframalpha.Client(app_id)
                        res = client.query(question)
                        answer = next(res.results).text
                        greet(f"You asked {listenedAudio}")
                        print(answer)
                        greet(f"The answer of the question is{answer}")
                    elif "search web" in  listenedAudio.lower():
                        greet("What do you want me to search on web?")
                        while True:
                            try:
                                listenedAudio=listen()
                                break
                            except Exception as e:
                                greet("Sir ! I did not get you, can you please repeat?")
                        splittedListenedAudio=listenedAudio.split(' ')
                        finalWord=""
                        i=0
                        for elem in splittedListenedAudio:
                            if i!=0:
                                finalWord=f"{finalWord}+{elem}"
                            else:
                                finalWord=f"{elem}"
                                i+=1
                        webbrowser.open(f"google.com/search?q={finalWord}")
                    elif "wiki" in listenedAudio.lower():
                        greet('Selected Operation is wikipedia...What do you want to search on wiki?')
                        while True:
                            try:
                                listenedAudio=listen()
                                results = wikipedia.summary(listenedAudio, sentences=2)
                                break
                            except Exception as e:
                                greet("No such pages found please try another query!")
                        
                        print(results)
                        greet(results)
                    elif "leave" in listenedAudio.lower():
                        greet("Okay Sir!See you soon,Make sure to take rest!")
                        break
                    else:
                        greet('Sir I am not able to perform this task,Please choose another')
            else:
                greet("Sorry This is incorrect password")
        else:
            greet("You are not in my records\n")
        