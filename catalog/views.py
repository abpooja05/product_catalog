from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import ProductSerializer, UserRegistrationSerializer, UserLoginSerializer, UserLogoutSerializer
from django.contrib.auth.models import User
from rest_framework.views import status
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from .models import Product



# Querying the MongoDB database
mongo_products = Product.objects.using("mongo").all()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    # serializer_class = UserLogoutSerializer

    def delete(self, request, *args, **kwargs):
        # Check if there is an authenticated user
        if request.auth and request.user.is_authenticated:
            request.auth.delete()
            logout(request)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'No authenticated user found.'}, status=status.HTTP_400_BAD_REQUEST)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


