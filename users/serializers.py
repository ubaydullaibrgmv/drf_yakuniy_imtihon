from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "phone", "password", "full_name"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        # user = User.objects.create(**validated_data) ****************************
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):

    phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        user = authenticate(
            phone=data["phone"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid phone or password")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
