"""
URL configuration for MoneyMind project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ExpenseApp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('' , views.SignUp , name="SignUp"),

    path('Loginuser/', views.LogIn, name='login'),
    path("AllUserdetails/", views.AllUserDetails , name="AllUserdetails"),
    
    path("addcategory/" , views.Addcategory , name="addcategory"),
    path("showallcategory/" , views.Showwallcategory , name="showallcategory"),
    path("deletecategory/" , views.Deletecategory , name="deletecategory"),
    path("searchcategoryrecord/" , views.Searchcategory , name="searchcategoryrecords"),
    path("updatecategoryrecords/" , views.updatecategory , name="updatecategoryrecords"),
    
    path("addexpense/" , views.addexpense , name="addexpense"),
    path("showallexpencess/" , views.showallexpencesrecord , name="showallexpencess"),
    path("searchdata/" , views.searchrecordinexpencess , name="searchdata"),
    path("deleteexpensedata/" , views.deleteexpencesrecord , name="deleteexpensedata"),
    # path("updateexpensedata/", views.Updateallexpensedata , name="updateexpensedata"),
    
    path("searchbudgetrecords/" , views.searchrecordsofbudget, name="searchbudgetrecords"),
    
]
