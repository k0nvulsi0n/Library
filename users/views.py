from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from users.models import User
from django.db.models import Q
# Create your views here.

class UserDetailView(generic.DetailView):
    model = User
    contecontext_object_name = 'user_detail'
    template_name = 'users/profile.html'

class UserListView(generic.ListView):
    model = User
    contecontext_object_name = 'user_list'
    def get_queryset(self):
        query = self.request.GET.get("q") if self.request.GET.get("q") != None else ""
        object_list = User.objects.filter(
            Q(username__icontains=query)
        )
        return object_list
    template_name = 'users/users.html'    
