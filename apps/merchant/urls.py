from django.urls import path
from apps.merchant.views import MerchantGenericView

urlpatterns = [
    path("", MerchantGenericView.as_view()),
    path("<int:id>", MerchantGenericView.as_view()),
]