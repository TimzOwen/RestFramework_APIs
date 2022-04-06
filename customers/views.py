from django.http import Http404
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics


class CustomerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CustomerDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)

    # def get_customer(self, pk):
    #     try:
    #         return Customer.objects.get(pk=pk)
    #     except Customer.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     customer = self.get_customer(pk)
    #     serializer = CustomerSerializer(customer)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     customer = self.get_customer(pk)
    #     serializer = CustomerSerializer(customer, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     customer = self.get_customer()
    #     customer.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def customer_list(request):
#     if request.method == "GET":
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = CustomerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET', 'PUT', 'DELETE'])
# def customer_details(request, pk):
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
