from .views import UserRegistrationView,UserEditView,PasswordsChangeView,ShowProfileView,EditProfilePageView,CreateProfilePageView
from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('edit_profile/',UserEditView.as_view(), name='user_edit'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),name="pass_change"),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html'),name="pass_change"),
    path('password_success/',views.password_success,name="pass_success"),
    path('<int:pk>/Profile/',ShowProfileView.as_view(),name="show_profile"),
    path('<int:pk>/edit_profile/',EditProfilePageView.as_view(),name="edit_profile"),
    path('create_profile/',CreateProfilePageView.as_view(),name="create_profile")
]
