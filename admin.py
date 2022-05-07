from django.contrib import admin
from certigen.models import service_Pariticipant

class service_PariticipantAdmin(admin.ModelAdmin):
    list_display=('par_name','par_email','par_status','text_file','template')
    
# Register your models here.
admin.site.register(service_Pariticipant, service_PariticipantAdmin)