from django.urls import re_path

from products.views import UserProductHistoryView
from .views import (
        AccountHomeView, 
        AccountEmailActivateView,
        UserDetailUpdateView
        )
app_name = 'account'
urlpatterns = [
    re_path(r'^$', AccountHomeView.as_view(), name='home'),
    re_path(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    re_path(r'history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    re_path(r'^email/resend-activation/$', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),
]

# account/email/confirm/asdfads/ -> activation view