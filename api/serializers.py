from rest_framework.serializers import ModelSerializer

from .models import Vgames

class VgameSerializer(ModelSerializer):
    class Meta:
        model = Vgames
        fields = '__all__'
