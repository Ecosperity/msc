from django.urls import path
from . import views
app_name='chatbot'

urlpatterns = [    
    path('BotConversation',views.BotConversation, name='BotConversation'),
    path('speaking',views.speaking, name='speaking'),
    path('jobssearch/',views.jobssearch, name='jobssearch'),
    path('msc-technology/',views.msc_technology, name='msc_technology'),
]