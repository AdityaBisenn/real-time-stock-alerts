from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ValidateView, ProfileView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('validate/', ValidateView.as_view(), name='validate'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
