
from django.urls import path
from . import views
urlpatterns = [
    path('movie',views.movie_Name),
    path('movie/<int:id>',views.movie_details),
]
