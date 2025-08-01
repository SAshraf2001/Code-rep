from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import google.generativeai as genai


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



# Chat with OpenAI (new SDK structure)
def chatI(request):
    question = request.POST.get('message')

    if not question:  # None or empty
        return render(request, 'openAI/answers.html', {'answer': 'No question provided.'})

    # Gemini equivalent of completion
    model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-1.5-pro
    response = model.generate_content(question)

    # Gemini response text
    text = response.text

    responses = {
        'answer': text,
    }

    return render(request, 'openAI/answers.html', responses)