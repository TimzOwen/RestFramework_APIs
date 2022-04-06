from . import views
from django.urls import path

urlpatterns = [
    path('', views.CustomerList.as_view()),
    path('<int:pk>', views.customer_details)
]
