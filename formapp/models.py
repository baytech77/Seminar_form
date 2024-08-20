from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField
# Create your models here.
CURRENT_STATUS = (

    ('fresh', 'Fresh graduate'),
    ('final', 'Final year student'),
    ('working', 'Working class'),
    ('student', 'Student'),
    ('others', 'others'),

)


PUBLICITY_AWARENESS = ( ('social', 'Social media'),
            ('family', 'Friend/ Family'),
            ('university', 'University/College'),
            ('others', 'others'),
                        )


GENDER_CHOICES =(('M', 'Male'),
                 ('F', 'Female')
                 )

CHOICES =(('Y', 'Yes'),
                 ('N', 'No')
                 )


class FormModel(models.Model):
        full_name = models.CharField(max_length=100, unique=True, help_text="full name")
        email = models.EmailField()
        phone_number = models.SlugField(max_length=15)
        current_status = models.CharField(choices=CURRENT_STATUS, default='fresh', help_text='Current Status?')
        university = models.CharField(help_text='University/College name?',max_length=105)
        country = CountryField( )
        publicity_awareness = models.CharField(choices=PUBLICITY_AWARENESS, default='social',  help_text='How did you hear about this master class?')
        career_goals = models.TextField(max_length=400, help_text='what are your career goals for the next 5 years?')
        previous_attendance = models.CharField(choices=CHOICES, default='Y', help_text='Have you attended  any career development workshops before?')
        topic_of_interest = models.TextField(max_length=300, help_text='What specific topic would you like to learn about in this masterclass?')
        availiability = models.CharField(choices=CHOICES, default='Y', help_text='Are you available to attend both days of the masterclass on August 24th and 25th, 2024?')
        whatsapp_no = models.SlugField(max_length=15)
        teligram_no = models.SlugField(max_length=15)
        comments_or_question = models.TextField(max_length=500, )

        def __str__(self):
            return self.full_name

