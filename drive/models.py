from django.db import models
import os
from datetime import datetime
# Create your models here.


class Folder(models.Model):
    foldername = models.CharField(max_length=200, unique=True)
    folderdesc = models.CharField(max_length=300)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Folder {} | Parent {} '.format(self.foldername, self.parent_folder)

class File(models.Model):
    filename = models.CharField(max_length=200)
    uploadDate = models.DateTimeField(auto_created=True, default=datetime.now, blank=True)
    filedesc = models.CharField(max_length=100, default="")
    filedir = models.ImageField(upload_to='pics/',  default="pics/default.jpeg")
    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'File Name: {}'.format(self.filename)
    def get_fileExt(self):
        name, extension = os.path.splitext(self.filedir.url)
        return extension[1:]
    def get_fileName(self):
        name, extension = os.path.splitext(self.filedir.url)
        return name
