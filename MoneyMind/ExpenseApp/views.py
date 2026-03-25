from django.shortcuts import render
from .models import User

# Create your views here.



def SignUp(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            error = "Email already exists"

        elif len(password) < 8:
            error = "Password must be at least 8 characters"

        elif username.isdigit():
            error = "Username should not be only numbers"

        else:
            try:
                User.objects.create(
                    username=username,
                    email=email,
                    password=password
                )
                error = "Signup Successful"
            except:
                error = "Signup Failed"

    return render(request, "User/signup.html", {"error": error})

def LogIn(request):
    return render(request, 'User/login.html')