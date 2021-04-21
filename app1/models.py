from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=128)
    phone = models.IntegerField(unique=True)
    profile_pic = models.ImageField(upload_to="images" ,blank=True, null=True)

    def __str__(self):
    	return self.name
