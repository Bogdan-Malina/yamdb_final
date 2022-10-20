import secrets
import logging

from django.core.mail import send_mail
from django.conf import settings

from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User
from .permissions import AdminOnly
from .serializers import (
    SelfUserSerializer, UserConfirmSerializer,
    UserSerializerPrivelege, UserSerializerUnprivelege
)

logger = logging.getLogger(__name__)


class SignUpView(ModelViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """
        Gets a username and email,
        creates a user and a confirmation token.
        Sends a token to an email.
        :param: request: username and email.
        :return: Response
        """
        serializer = SelfUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, _ = User.objects.get_or_create(
            email=request.data['email'],
            username=request.data['username'],
        )
        user.confirmation_code = secrets.token_hex(32)
        user.save()

        send_mail(
            subject='YAmdb email confirmation',
            message=user.confirmation_code,
            from_email=settings.SERVICE_MAIL,
            recipient_list={user.email}
        )
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def token(self, request):
        """
        Generates and returns a  jwt token
        :param request:
        :return:
        """
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            username=request.data[
                'username']
        )
        token = RefreshToken.for_user(user)
        return Response(str(token.access_token))


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    serializer_class = UserSerializerPrivelege
    permission_classes = (AdminOnly,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        detail=False, methods=['get', 'patch'],
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        """
        Current user information.
        :param request:
        :return: request with user info
        """
        serializer_class = UserSerializerUnprivelege
        if request.method == 'GET':
            serializer = serializer_class(request.user)
            return Response(serializer.data)

        serializer = serializer_class(request.user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
