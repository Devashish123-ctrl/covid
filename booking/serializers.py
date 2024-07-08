from rest_framework import serializers
from .models import User, VaccinationCenter, VaccinationSlot

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VaccinationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationCenter
        fields = '__all__'

class VaccinationSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationSlot
        fields = '__all__'
