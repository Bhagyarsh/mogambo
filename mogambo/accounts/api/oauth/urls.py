
from django.urls import include, path
import oauth2_provider
from .views import UserList,UserDetails
urlpatterns = [
    path('o/', include('oauth2_provider.urls')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
 
    
]