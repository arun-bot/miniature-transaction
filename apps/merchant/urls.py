from django.urls import path
from apps.merchant.views import MerchantListCreate, MerchantRetrieveUpdateDestro, MerchantAPIView, MerchantDetailAPIView, MerchantGenericView

urlpatterns = [
    # TODO: remove this
    # path("", MerchantListCreate.as_view()),
    # path("<int:pk>", MerchantRetrieveUpdateDestro.as_view()),
    # path("", MerchantAPIView.as_view()),
    # path("<int:id>", MerchantDetailAPIView.as_view()),
    path("", MerchantGenericView.as_view()),
    path("<int:id>", MerchantGenericView.as_view()),
]