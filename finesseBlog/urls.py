from django.urls import path, include
from . import views
from .views import AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('summernote/', include('django_summernote.urls')),
    path("", views.PostList.as_view(), name="blogs"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_detail/edit/<int:pk>', UpdatePostView.as_view(),
         name='update_post'),
    path('post_detail/<int:pk>/remove', DeletePostView.as_view(),
         name='delete_post'),
]
