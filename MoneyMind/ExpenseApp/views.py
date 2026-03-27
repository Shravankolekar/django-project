from django.shortcuts import render
from .models import User , Category

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
    error = ""
    msg = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        
            
        if len(password) < 8:
            error = "Password must be at least 8 characters"
        
        else:
            try:
                loginuser = User.objects.get(email=email, password=password)
                error = "Login Successful"
            except:
                error = "Invalid email or password"
    
    return render(request, 'User/login.html', {'error': error , msg : "msg"})

def AllUserDetails(request):
    usersdata = User.objects.all()
    return render(request, "User/AllUserDetails.html",{'usersdata ': usersdata})

def Addcategory(request):
    error = ""
    
    if request.method == "POST":
        cname = request.POST.get("cname")
        
        try:
            
            Category.objects.create(
                cname = cname
            )
            error = "category is added sucessfuly"
        except :
            error = "category is not added sucessfuly"
    return render(request,"Category/addcategory.html" , {"error" : error})