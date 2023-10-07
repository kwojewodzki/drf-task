from django.contrib.auth import login
from rest_framework import permissions, views
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED

from . import serializers


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=HTTP_202_ACCEPTED)
