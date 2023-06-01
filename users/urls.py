from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('users/', views.UserListView.as_view(), name='users'),
]