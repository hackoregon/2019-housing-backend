from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans
from api.serializers import NcdbSampleChangesSerializer, NcdbSampleYearlySerializer, FIPSRecordsSerializer, HmdaOrwaSerializer, TotalLoansSerializer
from django.contrib.postgres.fields import ArrayField
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route
from api.filters import NcdbSampleChangesFilter, NcdbSampleYearlyFilter, FIPSRecordsFilter, HmdaOrwaFilter, TotalLoansFilter
from django_filters import rest_framework as filters

class NcdbSampleChangesViewSet(viewsets.ModelViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'

class NcdbSampleYearlyViewSet(viewsets.ModelViewSet):
    queryset = NcdbSampleYearly.objects.all()
    serializer_class = NcdbSampleYearlySerializer
    filter_class = NcdbSampleYearlyFilter
    ordering_fields = '__all__'

class FIPSRecordsViewSet(viewsets.ModelViewSet):
    queryset = FIPSRecords.objects.all()
    serializer_class = FIPSRecordsSerializer
    filter_class = FIPSRecordsFilter
    ordering_fields = '__all__'

class HmdaOrwaViewSet(viewsets.ModelViewSet):
    queryset = HmdaOrwa.objects.all()
    serializer_class = HmdaOrwaSerializer
    filter_class = HmdaOrwaFilter
    ordering_fields = '__all__'

class TotalLoansViewSet(viewsets.ModelViewSet):
    queryset = TotalLoans.objects.all()
    serializer_class = TotalLoansSerializer
    filter_class = TotalLoansFilter
    ordering_fields = '__all__'
