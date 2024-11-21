from django.urls import include, path
from .views import ProductViewSet

from rest_framework import routers

# define the router 
router = routers.DefaultRouter() 
  
# define the router path and viewset to be used 
router.register(r'products', ProductViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]