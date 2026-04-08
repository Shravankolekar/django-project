from django.db import models

# Create your models here.
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    
    def __str__(self):
        return self.username
    
class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField()
    
    def __str__(self):
        return self.cname
    
class Expense(models.Model):
    eid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Users , on_delete=models.CASCADE)
    cid = models.ForeignKey(Category , on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    description = models.CharField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.description
    
class Budget(models.Model):
    bid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    monthly_limit = models.BigIntegerField()
    month = models.CharField()
    
    def __str__(self):
        return self.month
    
class Report(models.Model):
    rid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Users , on_delete=models.CASCADE)
    total_expense = models.BigIntegerField()
    month = models.CharField()
    
    def __str__(self):
        return self.month
    