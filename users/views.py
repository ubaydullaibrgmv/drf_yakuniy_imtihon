from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from drf_spectacular.utils import extend_schema

class RegisterView(APIView):

    permission_classes = []

    @extend_schema(request=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class LoginView(APIView):

    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data)

        return Response(serializer.errors, status=400)
