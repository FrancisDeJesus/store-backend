from rest_framework import viewsets 
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

# Viewset a class that can be inherited in which it will provide you necessary methods for CRUD and other stuff.
 # create a viewset 
class ProductViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = Product.objects.all() 
      
    # specify serializer to be used 
    serializer_class = ProductSerializer 

