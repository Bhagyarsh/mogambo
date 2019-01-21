from django.conf.urls import re_path, include

from .views import (SoftwareRetrieveView, SoftwarelistAPIView,
                    SoftwareRUDAPIView,SoftwarecreateAPIView)
                    # ,CategoryRUD,
                    # CategoryRUDCreateView)
app_name = 'SoftwarData'
urlpatterns = [
    re_path(r'list/(?P<slug>[-\w]+)$', SoftwareRetrieveView.as_view(), name='Software-retrieve'),
    re_path(r'^$', SoftwarelistAPIView.as_view(), name='Software-list'),
    re_path(r'post/(?P<slug>[-\w]+)$',SoftwareRUDAPIView.as_view(),name='Software-rud'),
    re_path(r'create$',SoftwarecreateAPIView.as_view(),name='Software-create'),
    # re_path(r'cat/data$',CategoryRUDCreateView.as_view(),name='Software-cat'),
    # re_path(r'cat/create/$',CategoryRUD.as_view(),name='Software-catc'),
]
