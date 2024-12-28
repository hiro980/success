from django.urls import re_path
from django.contrib.auth import views as auth_views

app_name = "accounts_passwords"

urlpatterns = [
    re_path(r'^password/change/$', 
            auth_views.PasswordChangeView.as_view(), 
            name='password_change'),
    re_path(r'^password/change/done/$', 
            auth_views.PasswordChangeDoneView.as_view(), 
            name='password_change_done'),
    re_path(r'^password/reset/$', 
            auth_views.PasswordResetView.as_view(), 
            name='password_reset'),
    re_path(r'^password/reset/done/$', 
            auth_views.PasswordResetDoneView.as_view(), 
            name='password_reset_done'),
    re_path(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
            auth_views.PasswordResetConfirmView.as_view(), 
            name='password_reset_confirm'),
    re_path(r'^password/reset/complete/$', 
            auth_views.PasswordResetCompleteView.as_view(), 
            name='password_reset_complete'),
]
