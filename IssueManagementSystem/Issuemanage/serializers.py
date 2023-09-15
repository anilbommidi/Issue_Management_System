from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user = Client.objects.create(Client_Name=validated_data['Client_Name'],
                                     Client_Email=validated_data['Client_Email'],
                                     Client_Phone_Number=validated_data['Client_Phone_Number'],
                                     Client_Password=make_password(validated_data['Client_Password']),
                                     Client_Address=validated_data['Client_Address'],
                                     Client_Description=validated_data['Client_Description'])
        return user


class ClientLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['Client_Email', 'Client_Password']


class PasswordChangeSerializer(serializers.Serializer):
    Client_Id = serializers.IntegerField()
    CurrentPassword = serializers.CharField()
    NewPassword = serializers.CharField()
    ConfirmPassword = serializers.CharField()


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'
