"""
from django.urls import path, include
from django.contrib import admin
from .views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include user management URLs
]

"""

from django.urls import path
from users.views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/",    LoginView.as_view(), name='login'),
    path("profile/",  ProfileView.as_view(), name='profile'),
     
 ]