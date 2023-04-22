from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request, ):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to home
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'There was an error logging in. Try again...')
            return redirect('login') 
    else:

        return render(request, 'authenticate/login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('index')