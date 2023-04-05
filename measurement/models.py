from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название датчика')
    description = models.CharField(max_length=255, verbose_name='Расположение датчика')


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='Темпетатура')
    created_at = models.DateTimeField(auto_now_add=True)
