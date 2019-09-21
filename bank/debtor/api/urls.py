from django.urls import path

from bank.debtor.api.views import DebtorListApi

urlpatterns = [
    path('', DebtorListApi.as_view(), name='api-debtor-list'),

]
