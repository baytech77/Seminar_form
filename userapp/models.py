from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phone_field import PhoneField
from django_countries.fields import CountryField
# Create your models here.

GENDER_CHOICES =(('M', 'Male'),
                 ('F', 'Female')
                 )

CHOICES =(('Y', 'Yes'),
                 ('N', 'No')
                 )

CURRENT_STATUS_CHOICES = (('A', 'Fresh graduate'),
                          ('B', 'Final year student')
                          )

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
    full_name = models.CharField(max_length=255, unique=True, help_text="full name")
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField(blank=False)
    current_status = models.CharField(choices=CURRENT_STATUS_CHOICES, default='A')
    university = models.CharField(max_length=255)
    country = CountryField(blank_label="United State")
    publicity_awareness = models.CharField(choices=GENDER_CHOICES)
    career_goals = models.CharField(max_length=255)
    previous_attendance = models.CharField(choices=CHOICES, default='Y')
    topic_of_interest = models.CharField(max_length=300)
    availiability = models.CharField(choices=CHOICES, default='Y')
    whatsapp_no = PhoneField(blank=False)
    teligram_no = PhoneField(blank=False)
    comments_or_question = models.TextField(max_length=500,)

