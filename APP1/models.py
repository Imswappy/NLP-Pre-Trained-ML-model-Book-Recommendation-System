from django.db import models
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils.html import mark_safe


#department model

class Department(models.Model):
    department_name=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.department_name

class Programs(models.Model):
    program_name=models.CharField(max_length=200,primary_key=True)
    program_duration=models.IntegerField()
    program_fee=MoneyField(max_digits=14,decimal_places=2,default_currency='TZS')
    date_registered=models.DateField(auto_now_add=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.program_name

class Course(models.Model):
    course_name=models.CharField(max_length=200)
    program=models.ForeignKey(Programs,on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name

class Student(models.Model):

       #enumerated list

       class Region_List(models.TextChoices):
         Default="Tanzania"
         Dodoma="Dodoma"
         Tanga="Tanga"
         Arusha="Arusha"
         Tabora="Tabora"

       regno=models.CharField(max_length=200,primary_key=True)     
       full_name=models.CharField(max_length=200)
       passport_size=models.ImageField(upload_to='passports/')
       application_form=models.FileField(upload_to='applications/')
       program=models.ForeignKey(Programs,on_delete=models.CASCADE)
       date_registered=models.DateField(auto_now_add=True)
       resident=models.CharField(choices=Region_List.choices,max_length=100)

       def __str__(self):
             return self.regno
       def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.passport_size.url))

#herroes

class Herroes(models.Model):

     class Category(models.TextChoices):
       Best_Student="Best_Student"
       Best_Staff="Best_Staff"
       Best_Footbal_Winner="Best_Footbal_Winner"
       Best_Leader="Best_Leader"


     full_name=models.CharField(max_length=200)
     heading=models.CharField(max_length=200)
     title=models.CharField(choices=Category.choices,max_length=100)
     image=models.ImageField(upload_to='herroes/')
     date_registered=models.DateField(auto_now_add=True)
     program=models.ForeignKey(Programs,on_delete=models.CASCADE)
     department=models.ForeignKey(Department,on_delete=models.CASCADE)
     def __str__(self):
             return self.full_name
     def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.image.url))

class Announcements(models.Model):
     heading=models.CharField(max_length=200)
     title=models.CharField(max_length=200)
     date_registered=models.DateField(auto_now_add=True)
     file=models.FileField(upload_to='announcements/')
     def __str__(self):
             return self.title