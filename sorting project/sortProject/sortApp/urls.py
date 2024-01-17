from django.urls import path
from .views import *

urlpatterns = [
    path('products/',productDetails.as_view(),name='product'),
    path('feedback/',feedbackDetails.as_view(),name='feedback')
    
]
