from django.urls import path
from eventsM.views import HomeView
from .views import index
from . import views

urlpatterns = [
    path('newsletter/', views.newslett, name='newsletter'),
    path('validate/', views.validate_email, name='validate_email'),
    path('', index),
    path('', HomeView.as_view(), name='eventsM'),
]