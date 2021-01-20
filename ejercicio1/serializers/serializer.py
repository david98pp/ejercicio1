
from rest_framework import serializers

from ejercicio1.models.models import Valores


class ValoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Valores
        db_table = "valores"
        fields = ['fecha', 'valor']
