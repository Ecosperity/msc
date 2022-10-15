from django.shortcuts import render
import pyttsx3
# import speech_recognition as sr
import webbrowser
import threading
from django.http import JsonResponse, HttpResponse
import time
from dashboard.models import SkillSet


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
        # all_skills = SkillSet.objects.all()
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
        if "italy" in q.lower():     
                context = {                
                'title':"location",                
                'q':"Italy okay, Please tell me Your Skills"
                }
                speak("Please tell me Your Skills")
                return JsonResponse(context, safe=False)        
        if "switzerland" in q.lower():     
                context = {                
                'title':"location",                
                'q':"Switzerland okay, Please tell me Your Skills"
                }
                speak("Please tell me Your Skills")
                return JsonResponse(context, safe=False)        
        if "usa" in q.lower():     
                context = {                
                'title':"location",                
                'q':"USA okay, Please tell me Your Skills"
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
    return HttpResponse("gohil fun call")
  