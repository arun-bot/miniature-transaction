from django.urls import path
from apps.order.views import OrderStatus

urlpatterns = [
    # TODO: remove this
    path('dummy-view/', OrderStatus.as_view(), name='order_status'),
]