from django import forms
from .models import FormModel
from django_countries.widgets import CountrySelectWidget

class MasterClassRegistrationForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'
        widgets = {
            'country': CountrySelectWidget(),
        }
#from django import forms
#from phone_field import PhoneField
#from django_countries.fields import CountryField

#class SeminarRegistrationForm(forms.Form):
#    name = forms.CharField(label='Full Name', max_length=100)
 #   email = forms.EmailField(label='Email Address')
#phone = forms.CharField(label='Phone Number', max_length=15)
   # currentStatus = forms.ChoiceField(
#        label='Current Status',
#choices=[
  #          ('', 'Select a status'),
#('fresh', 'Fresh graduate'),
   #         ('final', 'Final year student'),
#            ('working', 'Working class'),
#('student', 'Student'),
  #          ('others', 'others'  ),
  #          ]
#)
    #university = forms.CharField(label='university/college name', max_length=300)
 #  country = CountryField(blank_label="United State")
  #  publicityawareness = forms.ChoiceField(
 #       label='How did you hear about this master class?',
  #     choices=[
  #          ('', 'Select one'),
  #          ('social', 'Social media'),
   #         ('family', 'Friend/ Family'),
  #         ('university', 'University/College'),
  #          ('others', 'others'),
#
 #       ]
  #  )
#    careerGoals = forms.CharField(label="what are your career goals for the next 5 years?", max_length=400)
 #   PreviousAttendance = forms.ChoiceField(label=' Have you attended  any career development workshops before?', choices=[
 #       ('y', 'Yes'),
#        ('n', 'No'),
 #   ] )
 #   topicOfInterest= forms.CharField(label='What specific topic would you like to learn about in this masterclass?', max_length=300)
  #  availiability = forms.ChoiceField(label='Are you available to attend both days of the masterclass on August 24th and 25th, 2024?', choices=[
   #     ('y', 'Yes'),
 #       ('n', 'No'),
  #  ] )
 #   whatsappNo = forms.CharField(label='Phone Number', max_length=15)
 #   telegramNo  = forms.CharField(label='Phone Number', max_length=15)