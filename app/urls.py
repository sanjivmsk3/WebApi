from django.urls import path
from app.views import *

urlpatterns = [
    path('',Home.as_view()),
    path('booking',BookSlot.as_view()),
    path('plot',Plot.as_view())
]