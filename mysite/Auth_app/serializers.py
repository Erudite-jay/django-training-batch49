from rest_framework import serializers
from .models import Contact

# class ContactSerializer(serializers.Serializer):
#     fullname=serializers.CharField(max_length=256)
#     email=serializers.EmailField()
#     phone=serializers.CharField(max_length=10)
#     message=serializers.CharField(max_length=2000)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'