from rest_framework import serializers
from .models import (
    GlobalGroup
)
from account.serializer import (
    MyuserUsernameSerializer
)


class GlobalGroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalGroup
        fields = ["name","subject"]
    
    
class GlobalGroupSerializer(serializers.ModelSerializer):
    group_admin = MyuserUsernameSerializer()
    class Meta:
        model = GlobalGroup
        fields = ["id","uuid_field","name","subject","group_admin","members"]