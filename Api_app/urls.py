from django.urls import path
from .views import *


urlpatterns = [
    path("", api_homepage, name="api-homepage"),
    path("<int:id>/detail/", api_detailedpage, name="detail"),
    path("<int:id>/update/", api_updatepage, name="update"),
    path("<int:id>/delete/", api_deletepage, name="delete"),
    path("create/", api_createpage, name="delete"),   
]