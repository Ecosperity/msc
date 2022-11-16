from django.shortcuts import render
import time, os
from gtts import gTTS
from io import BytesIO
import pygame
import webbrowser
from django.http import JsonResponse
from dashboard.models import SkillSet
import urllib.request

location = 'india'

def jobssearch(request):  
    return render(request, 'chatbot/jobsearch.html')


#text-Speech converzation
def speak(text):
    try:            
        mp3_fp = BytesIO()
        tts = gTTS(text=text, lang='en', tld='com.au')
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_fp, 'mp3')
        pygame.mixer.music.play()
        # time.sleep(4)
    except Exception as e:
        pass

def BotConversation(request):
    # if request.is_ajax:  
        q = request.GET.get('text')
        if q=='':
            speak("Hi, my name is Mia. How may I help you?")
            return JsonResponse("Hi, my name is Mia. How may I help you?", safe=False)
        else:
            all_skills = SkillSet.objects.all().order_by('name')[:10]
            speak("You said " + q)
            if "msc technology india" in q.lower():                
                speak("please wait...")
                # os.system("xdg-open \"\" https://www.msc.com/en/local-information")
                urllib.request.urlopen('https://www.msc.com/en/local-information')  
                # webbrowser.open("https://www.msc.com/en/local-information")
                webbrowser.open('https://www.msc.com/en/local-information', new=0, autoraise=True)
                webbrowser.open_new_tab('https://www.msc.com/en/local-information', new=1, autoraise=True)
                webbrowser.open_new('https://www.msc.com/en/local-information', new=3, autoraise=True)   
                q =  "Opened MSC Technology India Page <br> Anything else?"
                speak('Opened MSC Technology India Page')
                return JsonResponse(q, safe=False)
            if "msc technology" in q.lower():                
                speak("please wait...")  
                webbrowser.open("https://www.msc.com/en/local-information")   
                q =  "Opened MSC Technology Page.<br> Anything else?"
                speak('Opened MSC Technology Page.')
                return JsonResponse(q, safe=False)
            if "management" in q.lower():  
                speak("please wait...")  
                webbrowser.open("https://www.msc.com/en/local-information")   
                q =  "Opened MSC Technology Management Page <br> Anything else?"
                speak('Opened MSC Technology Management Page')
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
            skillData = [item.name.lower() for item in all_skills]                            
            if any(sdata in q.lower() for sdata in skillData): 
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
            