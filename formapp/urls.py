from django.urls import path, include
from .views import HomepageView, SignUpView, SuccessView


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('reistered/', SuccessView.as_view(), name='success'),
    path('', HomepageView.as_view(), name="home"),
    path('register/', SignUpView.as_view(), name='register'),
]
