from django.urls import path
from eventsM.views import HomeView
from .views import index

urlpatterns = [
    path('', index),
    path('', HomeView.as_view(), name='eventsM'),
]