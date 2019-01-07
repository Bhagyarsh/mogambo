from django.conf.urls import re_path, include

from .views import SoftwareRetrieveView, SoftwarelistAPIView
app_name = 'SoftwareData'
urlpatterns = [
    re_path(r'^(?P<slug>[-\w]+)$', SoftwareRetrieveView.as_view(), name='Software-retrieve'),
    re_path(r'^$', SoftwarelistAPIView.as_view(), name='Software-list'),
]
