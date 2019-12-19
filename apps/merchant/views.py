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
        