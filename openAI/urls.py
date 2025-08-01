from django.urls import path
from openAI import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.loggedIn, name='loggedIn'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.loggedOut, name='loggedOut'),
    path('ans/', views.chatI, name='chatI'),
    # path('ans/', views.answers, name='answers')
]
