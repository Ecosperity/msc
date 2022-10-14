from django.shortcuts import render
import pyttsx3
# import speech_recognition as sr
import webbrowser
import threading
from django.http import JsonResponse, HttpResponse
import time
import nltk
from nltk.chat.util import Chat, reflections


location = 'india'

def jobssearch(request):  
    return render(request, 'chatbot/jobsearch.html')

def msc_technology(request):  
    return render(request, 'chatbot/msc_technology.html')

#text-Speech converzation
def speak(text): 
    engine = pyttsx3.init()    
    engine.setProperty('rate', 160)   
    voices = engine.getProperty('voices')#getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #o for male
    engine.setProperty('voice', voices[1].id)   #1 for female
    engine.say(text)
    engine.runAndWait()
    # time.sleep(1)
    if engine._inLoop:
        engine.endLoop()
    engine.stop()

def BotConversation(request):   
    q = request.POST.get('text')
    # chat = Chat(pairs, reflections)
    # res = chat.converse('hi')
    # print('neeeeeeeeeeeeeeeeeeew', res)

    if q=='':
        speak("Hi, My name is Mia. How can I help you ?")        
        return JsonResponse("Hi, My name is Mia, How can I help you ?", safe=False)
    else:
        speak("You said " + q)
        if "msc" in q.lower():                
                speak("please wait...")  
                context = {                
                'title':"msc",                
                'q':"Opened MSC Technology Page"
                }
                speak('Opened MSC Technology page')
                return JsonResponse(context, safe=False)
        if "jobs" in q.lower():     
                context = {                
                'title':"jobs",                
                'q':"Which Location"
                }
                speak("Which Location")
                return JsonResponse(context, safe=False)
        if "india" in q.lower():     
                context = {                
                'title':"location",                
                'q':"India okay, Please tell me Your Skills"
                }
                speak("Please tell me Your Skills")
                return JsonResponse(context, safe=False)        
        if "india" in q.lower():     
                context = {                
                'title':"location",                
                'q':"India okay, Please tell me Your Skills"
                }
                speak("Please tell me Your Skills")
                return JsonResponse(context, safe=False)        
        
        if "open newton website" in q.lower():                
                speak("Opening Newton Website")
                webbrowser.open("https://www.newton.co.in/")   
                q =  "Opened Newton Website"
        if "newton service" in q.lower():                
                speak("Opening Newton service")
                webbrowser.open("https://www.newton.co.in/#service2")   
                q =  "Opened Newton service"
        if "newton contact" in q.lower():                
                speak("Opening Newton Cantact us page")
                webbrowser.open("https://www.newton.co.in/#contact")   
                q =  "Opened Newton contact page"
        if "newton career" in q.lower():                
                speak("Opening Newton Career page")
                webbrowser.open("https://www.newton.co.in/#career")   
                q =  "Opened Newton Career page"

        if "youtube" in q.lower():                
                speak("Opening Youtube.com")
                webbrowser.open("https://youtube.com/")   
                q =  "Opened Youtube.com"
        if "google search" in q.lower():                
                speak("Opening google.com")
                webbrowser.open("https://google.com/")   
                q =  "Opened google.com"
        if "django developer" in q.lower():             
            speak("Please wait....")            
            context = {
                'page':"job",
                'title':"Django Developer",
                'skill':"django",
                'q':"Opened Check it please"
            }
            return JsonResponse(context, safe=False)
        if "php" in q.lower():             
            speak("Please wait....")            
            context = {
                'page':"job",
                'title':"PHP SENIOR DEVELOPER",
                'skill':"PHP",
                'q':"Opened Check it please"
            }
            return JsonResponse(context, safe=False)
        if "chennai" in q.lower():             
            speak("Please wait....")            
            context = {
                'location':"chennai",
                'title':"python Developer",
                'skill':"Python",
                'q':"Opened Check it please"
            }
            return JsonResponse(context, safe=False)
        q = "Not find it please select below"    
        return JsonResponse(q, safe=False)

def gohil(request):
    reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
    }
    pairs = [
        [
            r"my name is (.*)",
            ["Hello %1, How are you today ?",]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey there",]
        ], 
        [
            r"what is your name ?",
            ["I am a bot created by Analytics Vidhya. you can call me crazy!",]
        ],
        [
            r"how are you ?",
            ["I'm doing goodnHow about You ?",]
        ],
        [
            r"sorry (.*)",
            ["Its alright","Its OK, never mind",]
        ],
        [
            r"I am fine",
            ["Great to hear that, How can I help you?",]
        ],
        [
            r"i'm (.*) doing good",
            ["Nice to hear that","How can I help you?:)",]
        ],
        [
            r"(.*) age?",
            ["I'm a computer program dudenSeriously you are asking me this?",]
        ],
        [
            r"what (.*) want ?",
            ["Make me an offer I can't refuse",]
        ],
        [
            r"(.*) created ?",
            ["Raghav created me using Python's NLTK library ","top secret ;)",]
        ],
        [
            r"(.*) (location|city) ?",
            ['Indore, Madhya Pradesh',]
        ],
        [
            r"how is weather in (.*)?",
            ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
        ],
        [
            r"i work in (.*)?",
            ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
        ],
        [
            r"(.*)raining in (.*)",
            ["No rain since last week here in %2","Damn its raining too much here in %2"]
        ],
        [
            r"how (.*) health(.*)",
            ["I'm a computer program, so I'm always healthy ",]
        ],
        [
            r"(.*) (sports|game) ?",
            ["I'm a very big fan of Football",]
        ],
        [
            r"who (.*) sportsperson ?",
            ["Messy","Ronaldo","Roony"]
        ],
        [
            r"who (.*) (moviestar|actor)?",
            ["Brad Pitt"]
        ],
        [
            r"i am looking for online guides and courses to learn data science, can you suggest?",
            ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
        ],
        [
            r"quit",
            ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
        ],
    ]  
    chat = Chat(pairs, reflections)
    chat.converse()
    print('neeeeeeeeeeeeeeeeeeew', chat)
    return HttpResponse("gohil fun call")
    pass