from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('update_user', views.update_user, name='update_user'),
    path('user_profile/<user_id>', views.user_profile, name='user_profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'authenticate/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'authenticate/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'authenticate/password_reset_confirm.html'), name='password_reset_confirm')
]