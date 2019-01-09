"""mogambo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/command/',include(('Platforms.api.urls') ,namespace="command-retrieve")),
    path('api/v1/Softwares/',include(('SoftwareData.api.urls') ,namespace="software-retrieve")),
    path('api/v1/softwareslist/',include(('SoftwareData.api.urls') ,namespace="software-list")),
    path('api/v1/',include('accounts.api.jwt.urls'))
]
    # url(r'api/command/',include(('Platforms.api.urls') ,namespace="command-retrieve")),
    # url(r'api/Softwares/',include(('SoftwareData.api.urls') ,namespace="software-retrieve")),
    # url(r'api/softwareslist/',include(('SoftwareData.api.urls') ,namespace="software-list")),
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)