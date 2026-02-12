from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer
from wallets.permissions import IsOwner

class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(wallet__user=self.request.user)