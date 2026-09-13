from rest_framework import serializers

from spells.models import Spells

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spells
        fields = '__all__'