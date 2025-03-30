import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pt
import musicLibrary 


recognizer = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(command):
    print(command)
    if "open google" in command.lower():
        wb.open("https://www.google.com/")
        speak("Opening Google...")
    elif "open stackoverflow" in command.lower():
        wb.open("https://stackoverflow.com/")
        speak("Opening StackOverflow...")
    elif "open youtube" in command.lower():
        wb.open("https://www.youtube.com/")
        speak("Opening YouTube...")
    elif "open facebook" in command.lower():
        wb.open("https://www.facebook.com/")
        speak("Opening Facebook...")
    elif "play" in command.lower():
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        wb.open(link)
    
if __name__ == "__main__":
    speak("Initializing JARVIS.....!")
    #listen for the wake word for the recognition AI
    while True:
        r = sr.Recognizer()
        print("Recognizing....!")
        try:
            with sr.Microphone() as source:
                print("Say Something...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                speak("Yah!")
                with sr.Microphone() as source:
                    print("Jarvis Activate...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
        except Exception as e:
            print("error; {0}".format(e))