from django.db import models
# import programs from APP1
from APP1.models import Programs as Programs_from_App1
from django.utils.html import mark_safe

STATUS={
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),
}
class Registration(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    resident=models.CharField(max_length=200)
    phone=models.CharField(max_length=200,unique=True)
    email=models.CharField(max_length=200,primary_key=True)
    tutorial_session=models.TextField(max_length=250)
    accomodation=models.TextField(max_length=250)
    disability=models.TextField(max_length=250)
    certificate=models.TextField(max_length=250)
    marital=models.CharField(max_length=200)
    passport_size=models.ImageField(upload_to='application_passports/')
    certificates=models.FileField(upload_to='application_certificates/')
    date_of_birth=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    message=models.TextField()
    program=models.ForeignKey(Programs_from_App1,on_delete=models.CASCADE)
    
    #add two columns
    Status=models.CharField(max_length=50,null=True,choices=STATUS,default='Pending')
    school_index=models.CharField(max_length=200,unique=True)
    
    def __str__(self):
             return self.email
    def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.passport_size.url))

    
class MessageToForm(models.Model):
    message=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    closed_date=models.DateField()
