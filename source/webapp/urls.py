from django.urls import path

from .views import  play, history

urlpatterns = [
    path('', play),
    path('history', history),
]