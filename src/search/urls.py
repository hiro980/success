from django.urls import re_path, path

from .views import (
        SearchProductView
        )
app_name = "serch"
urlpatterns = [
    re_path(r'^$', SearchProductView.as_view(), name='query'),
]

