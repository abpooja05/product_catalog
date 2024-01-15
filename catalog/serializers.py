from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                return data
            else:
                raise serializers.ValidationError('Incorrect username or password.')
        else:
            raise serializers.ValidationError('Both username and password are required.')


class UserLogoutSerializer(serializers.Serializer):
    pass
