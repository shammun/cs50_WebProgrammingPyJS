from django.contrib import admin

from .models import Airport, Flights, Passenger

# Register your models here.
admin.site.register(Airport) # allow admin panel to manipulate Airport
admin.site.register(Flights) # allow admin panel to manipulate Flights
admin.site.register(Passenger)