from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from usersApp.forms import UserForm, UserUpdate
from usersApp.models import User


def main(request):
    return render(request, 'usersApp/main.html')


class LoginView(BaseLoginView):
    template_name = 'usersApp/login.html'


class LogoutView(BaseLogout):
    pass


class Registration(generic.CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usersApp:login')
    template_name = 'usersApp/registration.html'


class Profile(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdate

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('usersApp:profile')


class UserDeleteView(generic.DeleteView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('usersApp:login')
