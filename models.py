from django.db import models

# Create your models here.
class service_Pariticipant(models.Model):
    par_name = models.CharField(max_length=50)
    par_email = models.CharField(max_length=250)
    par_status = models.BooleanField(default=False)
    text_file = models.FileField(upload_to="text_files/",unique=True,null=True,default=None)
    template = models.FileField(upload_to="templates/",unique=True,null=True,default=None)
    
    
    