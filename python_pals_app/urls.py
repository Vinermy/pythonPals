from django.urls import path

from .views import signup, profile_page

urlpatterns = [
    path('auth/signup', signup, name='signup'),
    path('profile/<int:pk>', profile_page, name='profile-page')
]