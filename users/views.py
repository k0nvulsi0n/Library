from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic

class ProfileDetailView(generic.DetailView):
    model = User
    template_name = 'users/profile.html'
# Create your views here.
