from django.urls import path

from apps.transactions.views import (
    TransactionCreateView,
    TransactionListView,
    TransactionUpdateView,
)

app_name = "transactions"
urlpatterns = [
    path("create/", TransactionCreateView.as_view(), name="create-transaction"),
    path("list/", TransactionListView.as_view(), name="list-transaction"),
    path("update/<int:pk>", TransactionUpdateView.as_view(), name="update-transaction"),
]
