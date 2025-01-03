from django.urls import path, include
from expense import views

urlpatterns = [
    path('get-transaction/', views.get_transaction, name='get_transactions'),
    path('create-transaction/', views.create_transaction, name='create_transaction'),
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),

    path('auth/', include('authapp.urls')),
]
