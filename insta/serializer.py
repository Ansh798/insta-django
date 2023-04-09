from rest_framework import serializers
from insta.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()  
    password = serializers.CharField()
    bio = serializers.CharField()

    def create(self,validate_data):
        return User.objects.create(**validate_data)