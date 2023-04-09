from django.urls import path

from . import views # import views from current directory

urlpatterns = [
    path("", views.index) # Run index function inside view
    # when user goes to an empty route
]