from django.urls import path

from apps.transactions.views import (TransactionCreateView,
                                     TransactionListView,
                                     TransactionUpdateView)

app_name = "transactions"
urlpatterns = [
    path("create/", TransactionCreateView.as_view(), name="create"),
    path("list/", TransactionListView.as_view(), name="list"),
    path("update/<int:pk>", TransactionUpdateView.as_view(), name="update"),
]
