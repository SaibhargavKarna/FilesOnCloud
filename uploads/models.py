from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadItem(models.Model):
    uploaded_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    file_name=models.CharField(max_length=50)
    file_item=models.FileField(upload_to='files/')

    def __str__(self):
        return self.file_name