from django.shortcuts import render
import pyttsx3
# import speech_recognition as sr
import webbrowser
import threading
from django.http import JsonResponse


def jobssearch(request):  
    return render(request, 'chatbot/jobsearch.html')

def msc_technology(request):  
    return render(request, 'chatbot/msc_technology.html')

#text-Speech converzation
def speak(text):
    # text-to-speach
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)    
    # engine.setProperty('voice', 'english_rp+f4')
    engine.setProperty('voice', 'english+f1')
    # engine.setProperty('voice', 'english+f2')
    # engine.setProperty('voice', 'english+f3')
    # engine.setProperty('voice', 'english+f4')
    # engine.setProperty('voice', 'english_rp+f3') 
    engine.say(text)
    engine.runAndWait()
    # engine.stop()

def speaking(request):
    text = request.POST.get('text') 
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    # engine.setProperty('voice', 'english_rp+f4')
    engine.setProperty('voice', 'english+f1')
    engine.say(text)
    engine.runAndWait()
    return JsonResponse(text, safe=False)
    # engine.stop()


def BotConversation(request):   
    q = request.POST.get('text')
    if q=='':
        speak("Hi, My name is Mia")
        speak("How can I help you ?")
        return JsonResponse("Hi, My name is Mia, How can I help you ?", safe=False)
    else:
        speak("You said " + q)
        if "jobs" in q.lower():     
                context = {                
                'title':"jobs",                
                'q':"Which Location"
                }
                speak("Which Location")
                return JsonResponse(context, safe=False)
        if "location india" in q.lower():     
                context = {                
                'title':"location",                
                'q':"India okay, Please tell me Your Skills"
                }
                speak("Please tell me Your Skills")
                return JsonResponse(context, safe=False)        
        if "msc" in q.lower():                
                speak("please wait...")  
                context = {                
                'title':"msc",                
                'q':"Opened MSC Technology Page"
                }
                speak('Opened MSC Technology page')
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
            
        return JsonResponse(q, safe=False)


##Speech to text converzation
# def takeQuerySpeechRec():
#     speech_r = sr.Recognizer()
#     with sr.Microphone() as micro:
#         print("i am listening you............")
#         speak("i am listening you.")
#         audio = speech_r.listen(micro)
#         # listen for 5 seconds and create the ambient noise energy level
#         speech_r.adjust_for_ambient_noise(micro, duration=5)
#         speech_r.pause_threshold=1
#         try:
#             query = speech_r.recognize_google(audio, language='en-IN')
#             speak("you said" + query)
#             print(query)
#             if "youtube" in query.lower():
#                 print("Opening Youtube.com....")
#                 speak("Opening Youtube.com please wait")
#                 webbrowser.open("https://youtube.com/")
#             else:
#                 speak("you said" + query)
#         except sr.UnknownValueError:
#             print("unrecognized your Voice. Say that again please")
#             speak("unrecognized your Voice. Say again please")
    
