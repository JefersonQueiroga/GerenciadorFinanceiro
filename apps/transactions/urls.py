from django.urls import path

from apps.transactions.views import ClienteCreateView, ClienteListView

app_name = "transactions"
urlpatterns = [
    path("create/", ClienteCreateView.as_view(), name="create"),
    path("list/", ClienteListView.as_view(), name="listaclientesview"),
]
