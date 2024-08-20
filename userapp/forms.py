from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields =  ('full_name', 'email', 'phone_number', 'current_status', 'university', 'country', 'publicity_awareness', 'career_goals', 'previous_attendance', 'topic_of_interest', 'availiability', 'whatsapp_no', 'teligram_no', 'comments_or_question')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields