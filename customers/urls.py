from . import views
from django.urls import path

urlpatterns = [
    path('', views.customer_list),
    path('<int:pk>', views.customer_details)
]
