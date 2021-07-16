import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("My name is Jarvis. Please tell me how may i assist you today")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
    

if __name__=="__main__":
    wishMe()
    
    #Logic for executing tasks based on query
    while True:

        query=takeCommand().lower()

        if 'wikipedia' in query:                    # Adding wikipedia
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif'open youtube' in query:                  # Adding the browser actions 
            webbrowser.open("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")

        elif'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")


        elif 'play music' in query:
            webbrowser.open("music.youtube.com")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")        

        elif 'open brave' in query:
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)

        elif 'sleep more' in query:
            speak("Please wake up sir else I will, call her")

        elif 'who' in query:
            speak("Am I suppose to take her name sir?")

        elif 'cool down' in query:
            speak("as your wish sir")

        elif "today's task" in query:
            speak("you have completed your exercise and now time to Sove some data structure problems")

        elif 'marathi' in query:
            speak(" Sir, Mala yeta Marathi, kadachit tumchya peksha changla")

        elif 'hello' in query:
            speak(" Helllo sir, yes I am awake, it's been so long you are sleeping, now wake up it's time to work")

        elif 'thank you' in query:
            speak('always welcome sir')

    

        