from django.contrib import admin
from .models import Restaurant
from import_export.admin import ImportExportModelAdmin
from .resources import RestaurantResource

# Register your models here.
class RestaurantAdmin(ImportExportModelAdmin):
	resource_class = RestaurantResource
	list_display = ['id', 'name','email','phone']
	search_fields = ['name', 'email', 'id']

admin.site.register(Restaurant, RestaurantAdmin)
