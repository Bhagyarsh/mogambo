"""mogambo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include

from SoftwareData.views import SoftwareListView, SoftwareCreateView,  SoftwareDetailView

urlpatterns = [

    url(r'^$', SoftwareListView.as_view(), name='list'),


    url(r'^(?P<slug>[-\w]+)$', SoftwareDetailView.as_view(), name="detail"),
    url(r'^add/$', SoftwareCreateView.as_view(), name='form'),

]
