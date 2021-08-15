from django.db.models import query
from django.shortcuts import render
from .models import Measurement, Symptom
from django.http import HttpResponse
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MeasurementSerializer, SymptomSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

def temp(request):
    
    return HttpResponse(f'Temperature : {Measurement.objects.last().temperature}')

@api_view(['GET',])
def allMea(request):

    queryset = Measurement.objects.all()
    serializer = MeasurementSerializer(queryset, many=True)
    return Response(data=serializer.data)

class AllMeasurementView(APIView):

    # def get_object(self, request):
    #     query_set = Measurement.objects.all()
    #     return query_set

    def get(self, request):
        query_set = Measurement.objects.all()
        serializer = MeasurementSerializer(query_set, many=True)
        return Response(data=serializer.data)

class MeasurementAPIView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SymptomAPIView(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


#viewsets
class MeasurementViewsets(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filterset_fields = ('user__id', 'user__username')

class SymptomViewsets(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

