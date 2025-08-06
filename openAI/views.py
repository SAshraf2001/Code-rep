from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import google.generativeai as genai
import json
from django.http import JsonResponse
from .models import Location
from django.contrib.auth.decorators import login_required

genai.configure(api_key="AIzaSyCvOuatvoVCOpQF_kWuBD9ALqKjR3FaMEw")

# Home Page
def index(request):
    return render(request, 'openAI/chati.html')

# Sign In
def loggedIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'The account has been logged in successfully.')
            return redirect('/')  # Redirect after login
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'openAI/signin.html')

# Sign Up
def signup(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']

        if len(username) > 10:
            messages.error(request, 'Your username is too long. Please choose a shorter one.')
            return redirect('/signup')

        if password != confirmPassword:
            messages.error(request, 'Passwords do not match. Try again.')
            return redirect('/signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('/signup')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        messages.success(request, 'The account has been created successfully.')
        return redirect('/signin')

    return render(request, 'openAI/signup.html')

# Logout
def loggedOut(request):
    logout(request)
    messages.success(request, 'The account has been logged out.')
    return redirect('/')

# Chat
def chatI(request):
    question = request.POST.get('message')
    if not question:
        return render(request, 'openAI/answers.html', {'answer': 'No question provided.'})

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(question)
    text = response.text
    return render(request, 'openAI/answers.html', {'answer': text})


@login_required
def save_location(request):
    print("Request method:", request.method)

    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return JsonResponse({'status': 'error', 'message': 'Incomplete location data'}, status=400)

        Location.objects.update_or_create(
            getUser=request.user,
            defaults={'getLatitude': latitude, 'getLongitude': longitude}
        )

        return JsonResponse({'status': 'success', 'message': 'Location saved successfully'})

    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON: ' + str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    

def show_safe_location(request):
    return render(request, 'openAI/Save.html')