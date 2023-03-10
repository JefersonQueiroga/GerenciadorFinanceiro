from django.urls import path

from rest_framework import routers
from apps.transactions.api.viewsets import CategoryViewSet

from apps.transactions.views import (
    TransactionCreateView,
    TransactionListView,
    TransactionUpdateView,
)


app_name = "transactions"
urlpatterns = [
    path("create/", TransactionCreateView.as_view(), name="create_transaction"),
    path("list/", TransactionListView.as_view(), name="list_transaction"),
    path("update/<int:pk>", TransactionUpdateView.as_view(), name="update_transaction"),
]
