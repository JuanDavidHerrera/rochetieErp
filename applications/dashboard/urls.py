from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.InitialDashboard.as_view(), name="inicio"),
]