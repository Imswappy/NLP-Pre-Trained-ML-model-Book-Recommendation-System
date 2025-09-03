from django.urls   import path
from . import views

#register path APP2

urlpatterns = [
    path('',views.index,name='index'),
]
