from django.db import models

# Create your models here.


class Valores(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    class Meta:
        db_table = "valores"

