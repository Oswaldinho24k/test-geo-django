from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Restaurant
from .serializers import RestaurantSerializer
import math
import decimal
#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import Distance  

# Create your views here.

class RestaurantViewSet(viewsets.ModelViewSet):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer

# class ListRestaurantView(generics.ListAPIView):
# 	queryset = Restaurant.objects.all()
# 	serializer_class = RestaurantSerializer


# 	def get_queryset(self, *args, **kwargs):
# 		lat = self.request.GET.get('latitude')
# 		lng = self.request.GET.get('longitude')
# 		rad = self.request.GET.get('radius')
		
# 		queryset_list = super(ListRestaurantView, self).get_queryset()
# 		if lat and lng and rad:
# 			lat = decimal.Decimal(lat)
# 			lng = decimal.Decimal(lng)
# 			rad = decimal.Decimal(rad)
# 			print(lat, lng, rad)
# 			point = Point(lng, lat)    
# 			queryset_list.filter(location__distance_lt=(point, Distance(m=rad)))
		
# 		print(len(queryset_list))
# 		return queryset_list

