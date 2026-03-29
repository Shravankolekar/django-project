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

def Showwallcategory(request):
    Categoryes = Category.objects.all()
    return render(request, "Category/showallcategory.html" , {"Categoryes" : Categoryes})

def Deletecategory(request):
    error = " "
    
    if request.method == "POST":
        cid = request.POST.get('cid')
        
        if Category.objects.filter(cid = cid).exists():
            deletecategory = Category.objects.get(cid = cid)
            deletecategory.delete()
            error = "data is deleted sucessfully"
        
        else:
            error= f"{cid} number user not found"
            
        return render(request , "Category/deletecategory.html" , {error : "error"})    
    
def Searchcategory(request):
    error = ""
    c = None

    if request.method == "POST":
        cid = request.POST.get('cid')

        c = Category.objects.filter(cid=cid).first()

        if c is None:
            error = f"{cid} category not present, please enter another number"

    return render(request, "Category/viewcategory.html", {"error": error, "c": c})

def updatecategory(request):
    error = ""
    c = None

    if request.method == "POST":
        try:
            cid = int(request.POST.get("cid"))
            cname = request.POST.get('cname')

            # validation
            if cname.isdigit():
                error = "Enter only characters, not numbers"
                return render(request, "Category/updatecategory.html", {"error": error})

            # get object
            c = Category.objects.get(cid=cid)

            # update
            c.cname = cname
            c.save()

            error = "Record updated successfully"

        except Category.DoesNotExist:
            error = "Category not found"

        except Exception as e:
            error = "Something went wrong"

    return render(request, "Category/updatecategory.html", {"error": error, "c": c})

