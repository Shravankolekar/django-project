from django.shortcuts import render , redirect
from .models import Users , Category , Expense , Budget , Report
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def homepage(request):
    return render(request, "Common/home.html")

def SignUp(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Users.objects.filter(email=email).exists():
            error = "Email already exists"

        elif len(password) < 8:
            error = "Password must be at least 8 characters"

        elif username.isdigit():
            error = "Username should not be only numbers"

        else:
            try:
                Users.objects.create(
                    username=username,
                    email=email,
                    password=password
                )
                
                return redirect('homepage')
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
                loginuser = Users.objects.get(email=email, password=password)
                return redirect('homepage')
            except:
                error = "Invalid email or password"
    
    return render(request, 'User/login.html', {'error': error , msg : "msg"})


def AllUserDetails(request):
    usersdata = Users.objects.all()
    return render(request, "User/AllUserDetails.html",{"usersdata": usersdata})

def Addcategory(request):
    error = ""
    
    if request.method == "POST":
        cname = request.POST.get("cname")
        
        try:
            
            Category.objects.create(
                cname = cname
            )
            return redirect('addexpense')
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

            
            if cname.isdigit():
                error = "Enter only characters, not numbers"
                return render(request, "Category/updatecategory.html", {"error": error})

            
            c = Category.objects.get(cid=cid)

           
            c.cname = cname
            c.save()

            error = "Record updated successfully"

        except Category.DoesNotExist:
            error = "Category not found"

        except Exception as e:
            error = "Something went wrong"

    return render(request, "Category/updatecategory.html", {"error": error, "c": c})

def addexpense(request):
    
    error = ""
    
    if request.method == "POST":
        try:
            uid = request.POST.get("uid")
            cid = request.POST.get("cid")
            amount = request.POST.get('amount')
            description = request.POST.get('description')
            
            user = Users.objects.get(uid = uid)  # Replace with actual user retrieval logic
            
            if Users.objects.filter(uid = uid).exists():
                pass
            else:
                error = "user not found"
            
            categoryid = Category.objects.get(cid=cid)
            
            Expense.objects.create(
                uid = user,
                cid = categoryid,
                amount = amount,
                description = description
            )
            
            error = "Expense added successfully"
            
        except:
            error = "Invalid category"
    return render(request, "Expense/addexpense.html", {"error": error})

def showallexpencesrecord(request):
    Expenses = Expense.objects.all()
    return render(request , "Expense/showallexpense.html" , {"Expenses" : Expenses})

def searchrecordinexpencess(request):
    error = " "
    s = None
    
    if request.method == "POST":
        eid = request.POST.get("eid")
        
        s = Expense.objects.filter(eid = eid).first()
        
        if s is None:
            error = f"{eid} numbers data not found in the database please Enter a currect Expences id"
            
    return render(request , "Expense/viewexpense.html" , {"error" : error , "s" : s})

def deleteexpencesrecord(request):
    error = ""
    
    if request.method == "POST":
        eid = request.POST.get("eid")
        
        if Expense.objects.filter(eid = eid).exists():
            deletedata = Expense.objects.get(eid = eid)
            deletedata.delete()
            error = f"{eid} number data is deleted sucessfullay"
            
        else:
            error = f"{eid} Number Data nout found"
    return render(request, "Expense/deleteexpense.html" , {"error" : error})

# def Updateallexpensedata(request):
#     error = ""
#     u = None
    
#     if request.method == "POST":
#         eid = request.POST.get("eid")
#         uid = request.POST.get("uid")
#         cid = request.POST.get("cid")
#         amount = request.POST.get("amount")
#         description = request.POST.get("descrition")
        
#         try:
#             u = Expense.objects.get(eid=eid)
#         except :
#             error = f"{eid} number bit found"
        
#         if uid is not None:
#             if User.objects.filter(uid = uid).exists():
                
#                     u.uid = User.objects.get(uid=uid)

                    
                
#             else:
#                 error = f"{uid} numbers user not found"
#         else:
#             pass
        
#         if cid:
#             if Category.objects.get(cid = cid):
                
#                     u.cid = Category.objects.get(cid=cid)
#             else : 
#                 error = f"{uid} numbers category not found"
#         else:
#             pass
            
#         if amount:
            
#                 u.amount = amount
                
            
#         else:
#             pass
        
#         if description:
            
#                 u.description = description
            
#         else:
#             pass
                
#         try:
#             u.date = date.today()
            
#         except:
#             error = f"{eid} expense numbser is not found"
#         u.save()
#     return render(request, "Expense/updateexpense.html", {"error" : error , "u" : u})
def setbudget(request):
    
    error = ""

    if request.method == "POST":
        uid = request.POST.get('uid')
        monthly_limit = request.POST.get('monthly_limit')
        month = request.POST.get('month')
        
        try:
            user = Users.objects.filter(uid=uid).first()

            if user is None:
                error = "User not found"
            elif month == "":
                error = "Please select a month"
            else:
                Budget.objects.create(
                    uid=user,
                    monthly_limit=int(monthly_limit),
                    month=month
                )
                error = "Set successfully"
        except Exception as e:
            error = f"Error: {e}"
            
    return render(request, "Budget/setbudge.html", {"error": error})





def searchrecordsofbudget(request):

    error = ""
    a = None

    if request.method == "POST":
        bid = request.POST.get("bid")

        try:
            a = Budget.objects.get(bid=bid)
        except Budget.DoesNotExist:
            error = "Data not found! Please enter correct Budget ID"

    return render(request, "budget/viewbudget.html", {"a": a, "error": error})
        
        
def updatebudget(request):
    error = ""
    u = None
    
    if request.method == "POST":
        bid = request.POST.get('bid')
        uid = request.POST.get('uid')
        monthly_limit = request.POST.get('monthly_limit')
        month = request.POST.get('month')
        
        try:
            userid = Users.objects.filter(uid = uid).first()
            
            if userid is None:
                error = "user not found"
            elif month == "":
                error = "please select month "
            else:
                
                u = Budget.objects.get(bid = bid)
                u.uid = userid
                u.monthly_limit = monthly_limit
                u.month = month
                
                u.save()
                
                error = "update sucessfullay"
        except : 
            error = "update unsucessfullay"
    
    return render ( request , "Budget/updatebudget.html" , {"error" : error , "u" : u})



import matplotlib.pyplot as plt
import io
import base64

from django.shortcuts import render
from .models import Expense

def analyze_expense(request):

    # 👉 Get data from database
    expenses = Expense.objects.all()
    budget = Budget.objects.all()
    report = Report.objects.all()
    
    amounts = []
    month_limit = []
    total_exe = []
    months = []
    cid_exp = []

    for e in expenses:
        amounts.append(e. amount)
        cid_exp.append(e.cid.cname)
    
    for b in budget:
        month_limit.append(b.monthly_limit)
        
    for r in report:
        total_exe.append(r. total_expense)
        months.append(r.month)
        

    # 👉 Create graph
    plt.figure(figsize=(6,4))
    plt.bar(cid_exp, amounts, color='orange')
    plt.title("Expense Analysis")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    
    
    plt.bar(months, total_exe, label='Total Expense')

    # 👉 Save graph to memory
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    graph1 = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'Reports/analyticsdashboard.html', {'graph': graph , 'graph1': graph1})

@login_required
def homepage(request):
    return render(request, "Common/home.html")