from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    upload = models.FileField(upload_to='documents/')
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.name
