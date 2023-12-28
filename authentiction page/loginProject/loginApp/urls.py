from django.urls import path
from .views import home,register,login
urlpatterns = [
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('register/',register,name="register"),

]
