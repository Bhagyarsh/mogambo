from django.conf.urls import url, include

from .views import SoftwareRetrieveView, SoftwarelistAPIView

urlpatterns = [

    url(r'^(?P<slug>[-\w]+)$', SoftwareRetrieveView.as_view(), name='Software-retrieve'),
    url(r'^$', SoftwarelistAPIView.as_view(), name='Software-list'),
]
