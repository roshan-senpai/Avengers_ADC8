from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('viewevent/',view_event_data),
    path('eventform/',view_event_form),
    path('eventform/save',view_event_save),
    path('viewevent/delete/<int:ID>',view_event_delete),
    path('eventdataform/<int:ID>',view_eventform),
    path('eventdataform/update/<int:ID>',view_update_form_data_in_db),
    path('searchdata/<int:ID>',view_search_data),
    path('upload/',upload)
]
