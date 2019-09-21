from django.urls import path

from bank.debtor.views import DebtorCreate, DebtorList, DebtorUpdateView

urlpatterns = [
    path('', DebtorList.as_view(), name='debtor-list'),
    path('create', DebtorCreate.as_view(), name='debtor-create'),
    path('<int:pk>/change', DebtorUpdateView.as_view(), name='debtor-update'),

]
