from django import forms
from .models import Registration
from django.core.validators import RegexValidator
from.import models
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms import ValidationError   

TIME=(
    ('Evening','Evening'),
     ('Morning','Morning'),
      ('Fulltime','Fulltime'),
)
ACCOMODATION=(
  ('off campus','off campus'),
  ('on campus','on campus'),
  ('both','both'),
)

CERTIFICATE=(
  ('secondary education','secondary education'),
  ('high level','high level'),
  ('basic technician certificate','basic technician certificate'),
  ('diploma','diploma'),
  ('advanced diploma','advanced diploma'),
)
DISABILITY=(
('vision Impairment','vision Impairment'),
('deaf or hard of hearing','deaf or hard of hearing'),
('mental health conditions','mental health conditions'),
('intellectual disability','intellectual disability'),
('acquired brain injury','acquired brain injury'),
('autism spectrum disorder','autism spectrum disorder'),
('physical disability','physical disability'),
('none','none')
)
MARITAL=(
  ('married','married'),
  ('single','single')
)
REGION=(
         ('Default',"Tanzania"),
         ('Dodoma',"Dodoma"),
         ('Tanga',"Tanga"),
         ('Arusha',"Arusha"),
         ('Tabora',"Tabora"),
         ('Mwanza',"Mwanza"),
         ('Kigoma',"Kigoma"),
         ('Kilimanjaro',"Kilimanjaro"),
         ('Pwani',"Pwani"),
         ('Morogoro',"Morogoro"),
         ('Singida',"Singida"),
         ('Shinyanga',"Shinyanga"),
      )
#convert user input
class Lowercase(forms.CharField):
    def to_python(self,value):
        return value.lower()
     
class Uppercase(forms.CharField):
    def to_python(self,value):
        return value.upper()
    

class DataForm(forms.ModelForm): 
 firstname=forms.CharField(label='First Name',
                              min_length=2,max_length=50,
                              validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
                              message="Only letter is allowed")],
                              error_messages={'required':'first name can not be empty'},
                              required=True,
                              widget=forms.TextInput(attrs={'placeholder':'first name','style':'text-transform:capitalize'}))

 lastname=forms.CharField(label='Last Name',
                              min_length=2,max_length=50,
                              validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
                              message="Only letter is allowed")],
                              error_messages={'required':'first name can not be empty'},
                              required=True,
                              widget=forms.TextInput(attrs={'placeholder':'your lastname','style':'text-transform:capitalize'}))

 email=Lowercase(label='Email Address',
                              min_length=2,max_length=50,
                              validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                              message="Invalid Email address")],
                              error_messages={'required':'Email address is required'},
                              required=True,
                              widget=forms.TextInput(attrs={'placeholder':'example: xxx@gmail.com','style':'text-transform:lowercase'}))
 
 massage=forms.CharField(label='Enter Message',
                              min_length=2,max_length=20,
                              error_messages={'required':'enter a message'},
                              required=False,
                              widget=forms.TextInput(attrs={'placeholder':'enter something...','rows':2,'style':'font-size:18px'}))

 school_index=forms.CharField(label='Enter Private/School Index',
                              min_length=5,max_length=20,
                              error_messages={'required':'enter school index number'},
                              required=False,
                              widget=forms.TextInput(attrs={'placeholder':'P or S1000/1000','style':'font-size:18px'}))


 Status=forms.CharField(required=False)
 
 class Meta:
     model=Registration
     fields="__all__"
     
     widgets={
         
         'resident':forms.Select(choices=REGION,attrs={'class':'form-control','style':'font-size:18px;'}),
         'marital':forms.RadioSelect(choices=MARITAL,attrs={'class':'form-control','style':'font-size:18px;'}),
         'tutorial_session':forms.RadioSelect(choices=TIME,attrs={'class':'form-control','style':'font-size:18px;'}),
         'accomodation':forms.CheckboxSelectMultiple(choices=ACCOMODATION,attrs={'class':'form-control','style':'font-size:18px;'}),
         'disability':forms.CheckboxSelectMultiple(choices=DISABILITY,attrs={'class':'form-control','style':'font-size:18px;'}),
         'certificate':forms.CheckboxSelectMultiple(choices=CERTIFICATE,attrs={'class':'form-control','style':'font-size:18px;'}),
         'program':forms.Select(attrs={'class':'form-control','style':'font-size:18px;'}),
         'date_of_birth':DatePickerInput()
          
         
     }
     
 def __init__(self,*args,**kwargs):
        super(DataForm,self).__init__(*args,**kwargs)
         
         #font size
        font_size=['accomodation','marital','certificate','disability','tutorial_session']
        for field in font_size:
             self.fields[field].widget.attrs.update({'style':'font-size:20px;font-color:#B4D7FF'})
       
              
         #error to radio button
        error_message_radio=['marital','tutorial_session','accomodation','marital','resident','program','certificate','disability',]
        for field in error_message_radio:
             self.fields[field].error_messages.update({'required':'select at least one'})
        
        disabled=['marital','tutorial_session','accomodation','marital','resident','program','certificate','disability','firstname','lastname','marital','date_of_birth','passport_size','certificates']
        for field in disabled:
              self.fields[field].widget.attrs['disabled']=False
              
      