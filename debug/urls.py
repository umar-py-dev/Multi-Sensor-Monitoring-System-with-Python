from django.urls import path
from .views import debug_log

urlpatterns = [
    path('debug/', debug_log)
]
