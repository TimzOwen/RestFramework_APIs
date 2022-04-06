from .serializers import CustomerSerializer
from .models import Customer
from django.http import JsonResponse


def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)