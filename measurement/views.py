from rest_framework.generics import RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorChangeSerializer


class SensorsListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
