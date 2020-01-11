from django.contrib import admin
from django.urls import path
from .views import *
# url path fr html page 
urlpatterns = [
    path('eventdataform/<int:ID>',view_eventform),
    path('eventdataform/update/<int:ID>',view_update_form_data_in_db),
    path('searchform/search/',view_search_data),
]
