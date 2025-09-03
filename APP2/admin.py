from django.contrib import admin
from . import models
from django.utils.html import format_html

class RegistrationAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_max_show_all = 6
    exclude=['status']
    #list_editable = ['program']
    #search_fields = ('marital','resident','program','firstname',)
    readonly_fields=['firstname','lastname','resident','phone','email','tutorial_session','accomodation','disability','certificate','marital','passport_size','certificates','date_of_birth','program','school_index']
    list_display=('school_index','marital','resident','program','firstname','lastname','image_tag','status','_')

#change icons to status
    def _(self,obj):
        if obj.Status=='Approved':
            return True
        elif obj.Status=='Pending':
             return None
        else:
            return False
    _.boolean=True

    def status(self,obj):
      if obj.Status=="Approved":
            color='#00F142'
      elif obj.Status=="Pending":
             color='#CEBB00'
      else:
           color='#FF0000'
      return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.Status))
    status.allow_tags=True   
    
admin.site.register(models.Registration,RegistrationAdmin)




class MessageAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_max_show_all = 6
    list_display=('message','created_at','closed_date')
admin.site.register(models.MessageToForm,MessageAdmin)