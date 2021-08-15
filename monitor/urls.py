from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



router = DefaultRouter()
router.register('measurement-viewsets', views.MeasurementViewsets)
router.register('sympton-viewsets', views.SymptomViewsets)

schema_view = get_schema_view(
    openapi.Info(
        title="Covid Self Monitoring API",
        default_version='v1',
        description="bla bla..",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include(router.urls)),
    path('current_temperature/', views.temp, name='temp'),
    path('all_measurement/', views.AllMeasurementView.as_view(), name='all_measurement'),
    path('measurement/', views.MeasurementAPIView.as_view(), name='measurement'),
    path('sympton/', views.SymptomAPIView.as_view(), name='sympton'),
]