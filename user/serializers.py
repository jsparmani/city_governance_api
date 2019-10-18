from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""

        username = attrs.get('username'),
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=username[0],
            password=password
        )

        if not user:
            msg = 'Unable to authenticate with provided credentials'

            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
        read_only_fields = ('id', )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class EditUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('id', 'username', )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }


class UserListSerializer(serializers.ModelSerializer):
    """List users"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
