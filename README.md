# LIA AI VOICE ASSISTANT
In this project, I have created AI Virtual Assistant ,voice recognition machine. and  machine will respond to us and will also perform the task.
## MOUDULES AND LIBRARIES :
### SpeechRecognition:
It’s one of the most straightforward Python libraries for recognizing and processing human speech. It would be responsible for recognizing the speech/verbal commands of the assistant’s user and identifying the input words/input phrases, i.e., the words that will trigger a response from the assistant.
### pyttsx3:
This library offers the reverse of SpeechRecognition. This text-to-speech library will convert the text commands you add to the code (the assistant would say to the user). It’s cross-platform (making it ideal for more than just a test virtual assistant) and also works offline.
### Webbrowser:
One of the most common commands a virtual assistant receives is opening a website like Google, YouTube, or Amazon. The Webbrowser module in Python takes care of that. Once called, it can open a website on your default browser.
### Wikipedia:
Wikipedia module fetches information directly from one of the most extensive knowledge repositories online
### PyWhatKit:
It is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it has about 300k+ downloads and counting. New updates are released frequently with new features and bug fixes.
### pyjokes:
One line jokes for programmers (jokes as a service)
### Requests:
Requests is a simple, yet elegant, HTTP library.
#### To add these, you will have to execute the following commands in the terminal:
pip install pyttsx3

pip install SpeechRecognition

pip install Wikipedia

pip install webbrowser

pip install pywhatkit

pip install pyjokes

pip install requests

When running this code on PyCharm, you might encounter an error regarding PyAudio and will have to download that library. And if the usual “pip install PyAudio” command doesn’t work, you will have to go with a workaround. First, install Pipwin and then use the command “Pipwin install PyAudio.”
# imports:
import speech_recognition as sr

import pyttsx3

import pywhatkit

import datetime

import wikipedia

import pyjokes

import sys

import webbrowser

from datetime import date, datetime
