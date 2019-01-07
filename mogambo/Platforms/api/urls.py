from django.conf.urls import url, include

from .views import CommandRetrieveView

urlpatterns = [

    url(r'^(?P<pk>\d+)/$',CommandRetrieveView.as_view(), name='command-retrieve')

]
