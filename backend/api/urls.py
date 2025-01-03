from django.urls import path, include
from expense import views

urlpatterns = [
    # List all transactions
    path('get-transaction/', views.get_transaction, name='get_transactions'),

    # Create a new transaction
    path('create-transaction/', views.create_transaction, name='create_transaction'),

    # Retrieve, update, or delete a specific transaction by ID
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),
]
