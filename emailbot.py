# this is an automated email bot
# importing libraries
import smtplib
import speech_recognition as s_r
import pyttsx3
from email.message import EmailMessage
# use recognizer to recognize whatever we r saying
listener = s_r.Recognizer()
x = pyttsx3.init()


def talk(text):
    x.say(text)
    x.runAndWait()


def getinformation():
    try:
        # accepting the microphone
        with s_r.Microphone() as s:
            print('Listening')
            # voi task is to listen whatever we are saying
            voi = listener.listen(s, None, 6)
            # covert the audio to text we use google recognizer api
            information = listener.recognize_google(voi)
            print(information)
            # to get all the text in lowercase
            return information.lower()
    except:
        pass


# inorder not to send email again and again
def sendemail(receive, subject, content):
    # email will be sent to server and then server will send it to receiver's email
    # we are using this bot to send emails from gmail to gmail and 587 is the port number
    server_1 = smtplib.SMTP('smtp.gmail.com', 587)
    # tls is transport layer security
    server_1.starttls()
    # we give username and password of the sender's mail
    server_1.login('sumana26401@gmail.com', 'x')
    email = EmailMessage()
    email['From'] = 'sumana26401@gmail.com'
    email['To'] = receive
    email['Subject'] = subject
    email.set_content(content)
    server_1.send_message(email)


list_email = {
    'su': 'sumana26401@gmail.com',
    'sumana': 'sumanabushireddy@gmail.com',
    'kartik': 'karthikbs129@gmail.com',
    'sai kumar': 'saikumar.avu.78@gmail.com'
}


def get_email_information():
    talk("To whom you wanna send email")
    name = getinformation()
    receive = list_email[name]
    talk("What is the subject of your email")
    subject = getinformation()
    talk("Tell me the mail u wanna send")
    content = getinformation()
    sendemail(receive, subject, content)
    talk('Email sent successfully')


get_email_information()



