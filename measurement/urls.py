from django.urls import path

from measurement.views import SensorListCreateAPIView, MeasurementListCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='list_create_sens'),
    path('measurements/', MeasurementListCreateAPIView.as_view(), name='create_measurement')
]
