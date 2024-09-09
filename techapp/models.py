from django.db import models

# Create your models here.
class TestimonialSection(models.Model):
    name = models.CharField(max_length=1000)
    profession = models.CharField(max_length=1000)
    comment = models.CharField(max_length=2500)
    avatar = models.ImageField(upload_to="img/%y")
    youtube = models.CharField(max_length=2500)

class LogoScrollSection(models.Model):
    company = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to="img/%y")

class FaqSection(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=3000)