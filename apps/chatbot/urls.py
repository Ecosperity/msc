from django.urls import path
from . import views
app_name='chatbot'

urlpatterns = [    
    path('BotConversation',views.BotConversation, name='BotConversation'),  
    path('jobssearch/',views.jobssearch, name='jobssearch'),
    
]