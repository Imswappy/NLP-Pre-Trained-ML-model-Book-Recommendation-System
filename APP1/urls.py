from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.home,name='home'),
    path('about_us',views.about,name='about'),
    path('herroes',views.herroes,name='herroes'),
    path('anouncements',views.anouncements,name='anouncements'),
    path('online_application',views.application,name='application'),
    path('courses',views.courses,name='courses'),
    path('appstatus',views.appstatus,name='appstatus')
 
 
]