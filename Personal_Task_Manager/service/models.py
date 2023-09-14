from django.db import models
class Service(models.Model):
     Book_title=models.CharField(max_length=10)
     Book_description=models.TextField()
     date=models.DateField()
     Book_image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
     status=models.TextField()
# Create your models here.
