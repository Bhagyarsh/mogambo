
from django.conf.urls import url
from .views import SearchSoftwareListView

urlpatterns = [
    url(r'^$', SearchSoftwareListView.as_view(), name="query"),

]
