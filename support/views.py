from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import SupportMessage
from .serializers import SupportMessageSerializer

class SupportViewSet(ModelViewSet):
    serializer_class = SupportMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return SupportMessage.objects.all().order_by('-created_at')
        return SupportMessage.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            is_from_admin=self.request.user.is_staff
        )