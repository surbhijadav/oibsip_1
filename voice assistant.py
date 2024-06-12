import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice',voice[1].id)


def bolo(audio):
    engine.say(audio)
    engine.runAndWait()

def web_whatsapp():
    whatsapp_url = "https://web.whatsapp.com//"
    webbrowser.open(whatsapp_url)

def greet():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
         bolo("Good morning!")

        elif hour>=12 and hour<18:
            bolo("good afternoon!") 

        else:
            bolo("good evening!")

        bolo("hello i'm subhu.how may i help you!")


def takecommand():
   
    #it takes microphone input from the use and returns string output 
                  
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
         print("say that again please...")
         return"None"    
    return query

if __name__ == '__main__':
     greet()
     while True:
        query = takecommand().lower()

       #logic for executing  tasks based on query
        if 'wikipedia' in query:
            bolo('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            bolo("According to Wikipedia")
            print(results)
            bolo(results)

        elif 'open youtube' in query:
           webbrowser.open("youtube.com")

        elif 'open google' in query:    
           webbrowser.open("google.com")

        elif'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            bolo(f"mam,the time is {strTime}")
        
        elif 'open whatsapp' in query:
            web_whatsapp()