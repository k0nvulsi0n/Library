from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from users.models import User

class ProfileDetailView(generic.DetailView):
    model = User
    contecontext_object_name = 'user_detail'
    template_name = 'users/profile.html'
# Create your views here.
