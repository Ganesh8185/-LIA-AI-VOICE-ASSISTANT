import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date, datetime


bot=pyttsx3.init()
bot.setProperty("rate", 180)
voices = bot.getProperty("voices")
bot.setProperty('voice', voices [1].id)
reg=sr.Recognizer()

def engine_talk(text):
    bot.say(text)
    bot.runAndWait()

def Run_LIA():
    with sr.Microphone() as source:
        reg.adjust_for_ambient_noise(source, duration=1)
        print('\n')
        print("Start Speaking!!")
        engine_talk('try saying.. ')
        _audio = reg.listen(source, 10, 3)
    try:
        command=reg.recognize_google(_audio, language='en-in')
        command = command.lower()
        if 'lia' in command :
            command = command.replace('lia', '')
            print('you said'+command)
        else :
            print('you said : '+command)
        if 'heeey' in command :
            print('heeey how can i helpp you ??')
            engine_talk('heeey, how can i help you ??')
        elif 'who are you' in command :
            print("I am lia Python's Daughter but I am Working for you as an AI virtual assistant sir")
            engine_talk("I am lia Python's Daughter but I am Working for you as an AI virtual assistant sir")
            print("\n")
            print("What can i do for you??")
            engine_talk("What can i do for you")
        elif 'can you do' in command :
            print( "I can make Searches on Google. . . I can play Videos and Songs for you ... I can also tell you current date and time... if you wnat open some website like instagram,Wikipedia,stackflow,Github,datascine bootcamp,.. etc I can open it for you...With What you want me to Assist you ??")
            engine_talk("I can make Searches on Google. . . I can play Videos and Songs for you ... I can also tell you current date and time... if you wnat open some website like instagram,Wikipedia,stackflow,Github,datascine bootcamp,.. etc I can open it for you...With What you want me to Assist you ??")
        elif 'play' in command:
            song = command.replace('play', '')
            print('Playing' +song)
            engine_talk('Playing' +song)
            pywhatkit.playonyt(song)
        elif 'date and time' in command :
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            engine_talk('Today is : '+ d2)
            engine_talk('and current time is '+ time)
        elif 'time and date' in command :
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')

            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            engine_talk( 'Current time is '+ time)
            engine_talk('and Today is : '+ d2)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('The current time is' +time)
            engine_talk('The current time is')
            engine_talk(time)
        elif 'date' in command:
            today = date.today()
            print("Today's date:", today)

            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2)
            engine_talk('The todays date is')
            engine_talk(d2)
        elif 'tell me about' in command:
            name = command.replace('tell me about' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'wikipedia' in command:
            name = command.replace('wikipedia' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'what is' in command:
            name = command.replace('what is ' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'who is ' in command:
            name = command.replace('who is' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'what is ' in command :
            search = 'https://www.google.com/search?q='+command
            print(' Here is what i found on the internet..')
            engine_talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)
        elif 'joke' in command:
            _joke = pyjokes.get_joke()
            print(_joke)
            engine_talk(_joke)
        elif 'search' in command :
            search = 'https://www.google.com/search?q='+command
            engine_talk('searching... ')
            webbrowser.open(search)
        elif "my location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            engine_talk("You must be somewhere near here, as per Google maps")
        elif 'locate ' in command :
            engine_talk('locating ...')
            loc = command.replace('locate', '')
            if 'on map' in loc :
                loc= loc.replace('on map',' ')
                url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engine_talk('Here is the location of '+loc)
        elif 'on map' in command :
            engine_talk('locating ...')
            loc = command.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc[1])
            engine_talk('Here is the location of '+loc[1])

        elif 'location of' in command :
            engine_talk('locating ...')
            loc = command.replace('find location of', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engine_talk('Here is the location of '+loc)
        elif 'where is ' in command :
            engine_talk('locating ...')
            loc = command.replace('where is', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engine_talk('Here is the location of '+loc)
        elif 'bootcamps' in command :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            engine_talk('opening boot camps')
            webbrowser.open(search)
        elif 'boot camps' in command :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            engine_talk('opening boot camps')
            webbrowser.open(search)
        elif 'python bootcamp' in command :
            search = 'http://tathastu.twowaits.in/kickstart_python.html'
            engine_talk('showing pythonboot camp')
            webbrowser.open(search)
        elif 'data science bootcamp' in command :
            search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
            engine_talk('showing data science and ml bootcamp')
            webbrowser.open(search)
        elif 'open google' in command :
            print('opening google ...')
            engine_talk('opening google..')
            webbrowser.open_new('https://www.google.co.in/')
        elif 'gmail' in command :
            print('opening gmail ...')
            engine_talk('opening gmail..')
            webbrowser.open_new('https://mail.google.com/')
        elif 'open youtube' in command :
            print('opening you tube ...')
            engine_talk('opening you tube..')
            webbrowser.open_new('https://www.youtube.com/')
        elif 'open instagram' in command :
            print('opening instagram ...')
            engine_talk('opening insta gram...')
            webbrowser.open_new('https://www.instagram.com/')
        elif 'open stack overflow' in command :
            print('opening stackoverflow ...')
            engine_talk('opening stack overflow...')
            webbrowser.open_new('https://stackoverflow.com/')
        elif 'open github' in command :
            print('opening git hub ...')
            engine_talk('opening git hub...')
            webbrowser.open_new('https://github.com/')
        elif 'bye' in command:
            print('ohhh Hoooo!! you going....well good bye')
            engine_talk('ohhh Hoooo!! you going....well good bye')
            sys.exit()
        elif 'thank you' in command :
            print("most welcome")
            engine_talk('most welcome')
        elif 'stop' in command:
            print('good bye, see you again !!')
            engine_talk('good bye, see you again !!')
            sys.exit()
        elif 'tata' in command:
            print('good bye, have a great day !!')
            engine_talk('good bye, have a great day !!')
            sys.exit()
        else:
            print(' Here is what i found on the internet..')
            engine_talk('Here is what i found on the internet..')
            search = 'https://www.google.com/search?q='+command
            webbrowser.open(search)
    except Exception as ex:
        print(ex)

print('Hold on!!..I am Starting')
engine_talk('Hold on ........I am Starting')
print('\n')
h = datetime.now().hour
if (h >= 6) and (h < 12):
    print("Good Morning sir")
    engine_talk(f"Good Morning sir")
elif (h >= 12) and (h < 16):
    print("Good afternoon sir")
    engine_talk(f"Good afternoon sir")
elif (h >= 16) and (h < 19):
    print("Good Evening sir")
    engine_talk(f"Good Evening sir")
print("heeey i am lia  how can i help you")
engine_talk("heeey  i am lia  how can i help you")


while True:
    Run_LIA()