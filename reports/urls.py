from django.urls import path
from .views import get_reports
urlpatterns = [
    path('reports/', get_reports, name='reports')
]
