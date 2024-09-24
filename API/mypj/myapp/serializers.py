from rest_framework import serializers

class MypjSerializer(serializers.Serializer):
    name=serializers.CharField(label="Enter Your Name")
    age=serializers.CharField(label="Enter Your Age")