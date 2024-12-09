from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),
]
