from rest_framework import serializers
from .models import (
    GlobalGroup
)


class GlobalGroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalGroup
        fields = ["name","subject"]
    
    
class GlobalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalGroup
        fields = "__all__"