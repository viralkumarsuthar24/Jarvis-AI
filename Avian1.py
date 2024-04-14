import os

import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time
from googlesearch import search
import webbrowser
import openai
#from playsound import playsound

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random2.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Evening")
    else:
        speak("Good Night")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return speak("I cannot recognize what you have said")

engine.runAndWait() #Without this command, speech will not be audible to us.
if __name__ == "__main__":
    print('Welcome ..!! I am Avian')
    speak('Welcome to Avian artificial intelligence System')
    speak("I am Avian")
    speak("What can I do for you?")
    while True:
        print("Listening...")
        query = str(takeCommand())
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        if query == "what time it is":
            wishme()
            speak ("It is ")
            speak(datetime.now().hour)
            speak("hours")
            speak("It is ")
            speak(datetime.now().minute)
            speak("Minutes")
            speak("Sir time is" + str(datetime.now().hour) + "and" + str(datetime.now().minute) + "minutes")
        #elif "open music" in query:
            #laysound('C:\\Users\\Viral Suthar\\Valentine.mp3')
        elif "Open Youtube".lower() in query.lower():
            speak("Opening Youtube sir...")
            print("Opening Youtube sir...")
            webbrowser.open("https://www.youtube.com")
            time.sleep(10)
            exit()
        elif "Open Google".lower() in query.lower():
            speak("Opening Google sir...")
            print("Opening Google sir...")
            webbrowser.open("https://www.google.com")
            time.sleep(10)
            def takeCommand1():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    # r.pause_threshold =  0.6
                    audio = r.listen(source)
                    try:
                        print("Recognizing...")
                        query1 = r.recognize_google(audio, language="en-in")
                        print(f"User said: {query1}")
                        return query1
                    except Exception as e:
                        return speak("I cannot recognize what you have said")
            if __name__ == "__main__":
                print('Google is Open Now.. What can I search for you. Speak Search with word')
                speak('Google is Open Now.. What can I search for you. Speak Search with word')
                while True:
                    print("Listening...")
                    query1 = str(takeCommand1())
                    if "Stop Google".lower() in query1.lower():
                        speak("I am exiting")
                        exit()
                    elif "Search".lower() in query1.lower():
                        a = "https://www.google.com/search?q="
                        b = query1
                        c = "&sca_esv=560508726&ei=-3brZMzoBZyb4-EP2r-7-A8&ved=0ahUKEwiM0oPCnv2AAxWczTgGHdrfDv8Q4dUDCA8&oq=camera&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmNhbWVyYTILEAAYigUYsQMYkQIyCxAAGIoFGLEDGJECMg4QABiABBixAxiDARjJAzIOEAAYigUYsQMYgwEYkgMyChAAGIoFGLEDGEMyChAAGIoFGLEDGEMyCBAAGIAEGLEDMgsQABiKBRixAxiDATILEAAYgAQYsQMYgwEyCBAAGIoFGLEDSMA_UABYmhtwAXgAkAEAmAHaAaAB5AiqAQUwLjQuMrgBDMgBAPgBAcICBxAAGIoFGEPCAg0QABiKBRixAxiDARhDwgIREC4YgAQYsQMYgwEYxwEY0QPCAhMQLhiKBRixAxiDARjHARjRAxhDwgINEC4YigUYxwEY0QMYQ8ICCBAAGIoFGJECwgIIEC4YgAQYsQPCAhEQLhiKBRixAxiDARjHARivAcICCBAAGIoFGJIDwgIFEAAYgATCAgoQLhiKBRixAxhDwgINEC4YigUYsQMYgwEYQ-IDBBgAIEGIBgE&sclient=gws-wiz-serp"
                        d = b.translate({ord(i): None for i in ' '})
                        e = d.replace('search','')
                        f=a+e+c
                        print(e)
                        webbrowser.open_new_tab(f)
                        time.sleep(5)
                        speak('Opening')
                        exit()
                    else:
                        speak("Some Error Occurred. Sorry from Avian")


        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Stop".lower() in query.lower():
            speak ("I am exiting")
            exit()
        elif "who are you".lower() in query.lower():
            speak("I am Artificial System Develop by Viral")
            print("I am Artificial System Develop by Viral")
        else:
            speak("Some Error Occurred. Sorry from Avian")
