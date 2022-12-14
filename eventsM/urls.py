from django.urls import path, include
from eventsM.views import HomeView
from .views import (index,
                    UserEditView,
                    PasswordsChangeView,
                    ShowProfilePageView,
                    EditProfilePageView)
from . import views


urlpatterns = [
    path('newsletter/', views.newslett, name='newsletter'),
    path('validate/', views.validate_email, name='validate_email'),
    path('', index),
    path('', HomeView.as_view(), name='eventsM'),
    path('blog/', include('finesseBlog.urls')),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/',
         PasswordsChangeView.as_view
         (template_name='account/password_change.html')),
    path('<int:pk>/profile',
         ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page',
         EditProfilePageView.as_view(), name='edit_profile_page'),
]
