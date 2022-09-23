from django.urls import path
from eventsM.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='eventsM')
]