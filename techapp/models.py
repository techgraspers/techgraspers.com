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

class CourseDetailsSection(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    page_link = models.CharField(max_length=1000)
    button_link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="img/%y")

class ServiceDetailsSection(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    popup_link = models.CharField(max_length=1000)
    button_link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="img/%y")
    heading = models.CharField(max_length=1000)
    description_popup = models.TextField(null=True, default="Default description")
    second_heading = models.CharField(max_length=1000, blank=True, null=True)
    list_01 = models.CharField(max_length=1000, blank=True, null=True)
    list_01_desc = models.CharField(max_length=2500, blank=True, null=True)
    list_02 = models.CharField(max_length=1000, blank=True, null=True)
    list_02_desc = models.CharField(max_length=2500, blank=True, null=True)
    list_03 = models.CharField(max_length=1000, blank=True, null=True)
    list_03_desc = models.CharField(max_length=2500, blank=True, null=True)