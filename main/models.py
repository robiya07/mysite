from django.db import models


# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    from_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


class CvModel(models.Model):
    pdf = models.FileField(upload_to='cv/')
