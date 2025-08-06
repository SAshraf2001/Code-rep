from django.urls import path
from openAI import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.loggedIn, name='loggedIn'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.loggedOut, name='loggedOut'),
    path('ans/', views.chatI, name='chatI'),
    path('save/', views.show_safe_location, name='show_safe_location'),
    path('save-location/', views.save_location, name='save_location')
]
