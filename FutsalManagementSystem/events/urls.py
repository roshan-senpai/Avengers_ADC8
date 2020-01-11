from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('viewevent/',view_event_data),
]