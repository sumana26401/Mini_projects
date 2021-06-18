import speech_recognition as s_r
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = s_r.Recognizer()
x = pyttsx3.init()
x.say('I am your alpha. How can I help you')
x.runAndWait()

def talk(txt):
    x.say(txt)
    x.runAndWait()
def comm():
    try:
        with s_r.Microphone() as s:
            print("Listeningggg.....")
            voi = listener.listen(s, None, 6)
            command = listener.recognize_google(voi)
            command = command.lower()
            if 'alpha' in command:
                command = command.replace('Alpha', "")
                x.say(command)
                x.runAndWait()
                print(command)
    except:
        pass
    return(command)

def alpha_run():
    command = comm()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print("Playing")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk("The current time is " + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I cant understand what you are saying')




while True:
    alpha_run()