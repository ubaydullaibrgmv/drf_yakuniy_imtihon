from rest_framework import serializers
from .models import SupportMessage

class SupportMessageSerializer(serializers.ModelSerializer):
    user_phone = serializers.CharField(source='user.phone', read_only=True)

    class Meta:
        model = SupportMessage
        fields = ['id', 'user', 'user_phone', 'text', 'is_from_admin', 'created_at']
        read_only_fields = ['user', 'is_from_admin', 'created_at']