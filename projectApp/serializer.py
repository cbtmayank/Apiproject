from rest_framework import serializers
from .models import projectModel

# SERIALIZER MODEL

class projectDataSerializers(serializers.ModelSerializer):

    class Meta:
        model = projectModel
        fields = ('__all__')