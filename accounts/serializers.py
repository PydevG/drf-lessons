from .models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError("Email is already taken")
        
        return super().validate(attrs)