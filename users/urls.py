from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile')
]