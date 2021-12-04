import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    # Multiple say can be used
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing')
        pywhatkit.playonyt(song)
    elif 'search' in command:
        src = command.replace('search','')
        talk('searching')
        pywhatkit.search(src)

    elif 'inform' in command:
        inform = command.replace('inform','')
        talk('just wait a moment')
        pywhatkit.info(inform)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        talk(info)
        print(info)
run_alexa()
