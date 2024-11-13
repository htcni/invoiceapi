from django.urls import path

from .views import InvoiceDetail, InvoiceList

urlpatterns = [
    path("", InvoiceList.as_view()),
    path("<int:pk>", InvoiceDetail.as_view()),
]
