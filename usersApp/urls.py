from django.urls import path

from usersApp.apps import UsersappConfig
from usersApp.views.user import Registration, LoginView, LogoutView, main, Profile, UserUpdateView, UserDeleteView

app_name = UsersappConfig.name

urlpatterns = [
    # main url
    path('', main, name='main'),
    # all users url
    path('user/registration', Registration.as_view(), name='registration'),
    path('user/login', LoginView.as_view(), name='login'),
    path('user/logout', LogoutView.as_view(), name='logout'),
    path('user/profile', Profile.as_view(), name='profile'),
    path('user/update', UserUpdateView.as_view(), name='update'),
    path('user/delete', UserDeleteView.as_view(), name='delete'),


]
