from pickle import TRUE
from time import time
from django.shortcuts import render
import pyttsx3
import speech_recognition as sr
import webbrowser
from django.http import JsonResponse

recognizer = sr.Recognizer()
microphone = sr.Microphone()
def recognize_speech(start_response):
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("i am listening you...")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return response
# time.sleep(3)

#text-Speech converzation
def speak(text):
    # text-to-speach
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)   
    voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[0].id)  #o for male
    engine.setProperty('voice', voices[1].id)   #1 for female
    engine.say(text)
    engine.runAndWait()
    # engine.stop()
    

def BotConversation(request, start_response): 
    q = request.POST.get('text')    
    # voice = recognize_speech().lower()
    if q=='':        
        speak("Hi, my name is Mia. How may I help you?") 
        return JsonResponse("Hi, my name is Mia. How may I help you?", safe=False)
    else:        
        if "jobs" in q: 
            context = {                
                'title':"jobs",                
                'q':"Which Location"
                }
            speak("Which Location")
            return JsonResponse(context, safe=False)
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)      
    return JsonResponse(q, safe=False)


def jobssearch(request, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return render(request, 'chatbot/jobsearch.html')

def msc_technology(request, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)  
    return render(request, 'chatbot/msc_technology.html')
