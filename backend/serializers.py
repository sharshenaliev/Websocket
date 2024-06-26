from rest_framework import serializers
from rest_framework.authtoken.models import Token
from backend.models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(validated_data['password'])
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def get_key(self, instance):
        token, created = Token.objects.get_or_create(user=instance)
        return token.key

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'
