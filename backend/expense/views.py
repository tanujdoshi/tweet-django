from django.shortcuts import get_object_or_404
from .models import Transactions
from .serializer import TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def get_transaction(request):
    queryset = Transactions.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response({"data": serializer.data})

@api_view(['POST'])
def create_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transactions, pk=pk)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response({"data": serializer.data})

    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
