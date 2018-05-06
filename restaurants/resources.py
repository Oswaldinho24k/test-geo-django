from import_export import resources
from .models import Restaurant

class RestaurantResource(resources.ModelResource):

    class Meta:
        model = Restaurant