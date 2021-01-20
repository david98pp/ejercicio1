from rest_framework import viewsets

from ejercicio1.models.models import Valores
from ejercicio1.serializers.serializer import ValoresSerializer


class ValoresViewSet(viewsets.ModelViewSet):
    queryset = Valores.objects.all()
    serializer_class = ValoresSerializer