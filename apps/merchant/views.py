from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins
from apps.merchant.models import Merchant

from apps.merchant.serializers import MerchantSerializer

class MerchantGenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
        
class MerchantAPIView(APIView):
    def get(self, request):
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        data = request.data
        serializer = MerchantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MerchantDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Merchant.objects.get(id=id)
        except MerchantAPIView.DoesNotExist as e:
            return Response({"error": "Given merchant object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = MerchantSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        instance = self.get_object(id)
        data = request.data
        serializer = MerchantSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



class MerchantListCreate(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MerchantRetrieveUpdateDestro(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MerchantSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Merchant.objects.all().filter(user=self.request.user)
