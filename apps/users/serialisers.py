from rest_framework import serializers
from  .models import Users

class UsersSerializer(serializers.ModelSerializer):
    user_level = serializers.CharField(source='user_level.level', read_only=True)
    class Meta:
        model = Users
        fields = "__all__"