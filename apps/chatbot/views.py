from django.shortcuts import render
import pyttsx3
# import speech_recognition as sr
import webbrowser
import threading
from django.http import JsonResponse, HttpResponse
from django.db.models.functions import Lower
import time
from dashboard.models import SkillSet


location = ''

def jobssearch(request):  
    return render(request, 'chatbot/jobsearch.html')

def msc_technology(request):  
    return render(request, 'chatbot/msc_technology.html')

#text-Speech converzation
def speak(text):
    engine = pyttsx3.init()
    try:            
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
    except:       
        pass

def BotConversation(request):   
    q = request.POST.get('text')
    # chat = Chat(pairs, reflections)
    # res = chat.converse('hi')
    # print('neeeeeeeeeeeeeeeeeeew', res)

    if q=='':
        speak("Hi, My name is Mia. How can I help you ?")        
        return JsonResponse("Hi, My name is Mia, How can I help you ?", safe=False)
    else:
        all_skills = SkillSet.objects.all() 
        speak("You said " + q)
        if "msc technology" in q.lower():                
            speak("please wait...")  
            webbrowser.open("https://www.msc.com/en/local-information")   
            q =  "Opened MSC Technology Page.<br> Anything else?"
            speak('Opened MSC Technology Page.')
            return JsonResponse(q, safe=False)

        if "msc newsroom" in q.lower():                
            speak("please wait...")  
            webbrowser.open("https://www.msc.com/en/newsroom")   
            q =  "Opened MSC Newsroom page <br> Anything else?"
            speak('Opened MSC Newsroom page')
            return JsonResponse(q, safe=False)

        if "msc contact" in q.lower():                
            speak("please wait...")  
            webbrowser.open("https://www.msc.com/contact-us")   
            q =  "Opened MSC contact-us page <br> Anything else?"
            speak('Opened MSC contact-us page')
            return JsonResponse(q, safe=False)

        if "jobs" in q.lower():     
            context = {                
            'title':"jobs",                
            'q':"Which Location"
            }
            speak("Which Location")
            return JsonResponse(context, safe=False)
        
        if "india" in q.lower():              
            data = [item.name for item in all_skills]                         
            context = {                
            'title':"location",                
            'q':"India okay, Please tell me Your Skills",
            'skill_list':data
            }
            speak("Please tell me Your Skills")
            return JsonResponse(context, safe=False)        
        if "italy" in q.lower():   
            data = [item.name for item in all_skills]  
            context = {                
            'title':"location",                
            'q':"Italy okay, Please tell me Your Skills",
            'skill_list':data
            }
            speak("Please tell me Your Skills")
            return JsonResponse(context, safe=False)        
        if "switzerland" in q.lower():  
            data = [item.name for item in all_skills]   
            context = {                
            'title':"location",                
            'q':"Switzerland okay, Please tell me Your Skills",
            'skill_list':data
            }
            speak("Please tell me Your Skills")
            return JsonResponse(context, safe=False)        
        if "usa" in q.lower(): 
            data = [item.name for item in all_skills]    
            context = {                
            'title':"location",                
            'q':"USA okay, Please tell me Your Skills",
            'skill_list':data
            }
            speak("Please tell me Your Skills")
            return JsonResponse(context, safe=False)        
    
       
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
        # if "django" in q.lower():             
        #     speak("Please wait....")            
        #     context = {
        #         'page':"job",
        #         'title':"Django",
        #         'skill':"django",
        #         'q':"Opened Check it please <br> Anything else?"
        #     }
        # if "python" in q.lower():             
        #     speak("Please wait....")            
        #     context = {
        #         'page':"job",
        #         'title':"Python",
        #         'skill':"Python",
        #         'q':"Opened Check it please <br> Anything else?"
        #     }
        #     return JsonResponse(context, safe=False)
        # if "php" in q.lower():             
        #     speak("Please wait....")            
        #     context = {
        #         'page':"job",
        #         'title':"PHP SENIOR DEVELOPER",
        #         'skill':"PHP",
        #         'q':"Opened Check it please <br> Anything else?"
        #     }
        #     return JsonResponse(context, safe=False)
        if "chennai" in q.lower():             
            speak("Please wait....")            
            context = {
                'location':"chennai",
                'title':"python Developer",
                'skill':"Python",
                'q':"Opened Check it please <br> Anything else?"
            }
            return JsonResponse(context, safe=False)

        skillData = [item.name.lower() for item in all_skills]    
        if any(sdata in q.lower() for sdata in skillData): 
            # speak("Skill Available thank you....") 
            skill = []           
            for item in skillData:
                if item in q.lower():
                    skill.append(item)
            speak("Please wait....") 
            context = {
                'page':"job",
                'title': q,
                'skill':skill,
                'q':"Opened Check it please <br> Anything else?"
            }
            return JsonResponse(context, safe=False)
        
        botend = ['not','no','close','stop'] 
        if any(cdata in q for cdata in botend):            
            speak("Ok Thank You") 
            context = {                
            'title':"thankYou",                
            'q':"Thank you!!"            
            }
            return JsonResponse(context, safe=False)
        q = "Not find it please select below"    
        return JsonResponse(q, safe=False)
        
def gohil(request):    
    return HttpResponse("gohil fun call")
  