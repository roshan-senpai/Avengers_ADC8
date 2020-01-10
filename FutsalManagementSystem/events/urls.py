from django.contrib import admin
from django.urls import path
from .views import *
# url path fr html page 
urlpatterns = [
    path('update/',view_update_page),
    path('eventdataform/<int:ID>',view_eventdata_updateform),
    path('eventdataupdateform/<int:ID>',view_update_form_data_in_db)
]
