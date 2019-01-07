from django.conf.urls import url, include,re_path

from .views import CommandRetrieveView
app_name = 'Platforms'
urlpatterns = [

    re_path(r'^(?P<pk>\d+)/$',CommandRetrieveView.as_view(), name='command-retrieve')

]
