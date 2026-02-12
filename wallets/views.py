from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Wallet
from .serializers import WalletSerializer
from .permissions import IsOwner


class WalletViewSet(ModelViewSet):

    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
