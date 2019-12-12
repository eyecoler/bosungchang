from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_world1, name='hello_world1')
]