from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans
from api.serializers import NcdbSampleChangesSerializer, NcdbSampleYearlySerializer, FIPSRecordsSerializer, HmdaOrwaSerializer, TotalLoansSerializer
from django.contrib.postgres.fields import ArrayField
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.views import APIView
from api.filters import NcdbSampleChangesFilter, NcdbSampleYearlyFilter, FIPSRecordsFilter, HmdaOrwaFilter, TotalLoansFilter
from django_filters import rest_framework as filters

class CardOneViewSet(APIView):

    def get(self, request):
        portland_rows = NcdbSampleYearly.objects.filter(metroname="Portland-Vancouver-Hillsboro, OR-WA")
        years = set(row.year for row in portland_rows)
        response = {row.year : {"white" : 0, "black": 0, "hisp": 0, "asoth": 0} for year in years} :

        for row in portland_rows:
            response[row.year["white"]] += (row.population * row.whiteshare / 100)
            response[row.year["black"]] += (row.population * row.blackshare / 100)
            response[row.year["hisp"]] += (row.population * row.hispshare / 100)
            response[row.year["asoth"]] += (row.population * row.asothshare / 100)

        return Response(response)

class CardTwoViewSet(viewsets.ViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'

class CardThreeViewSet(viewsets.ViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'

class CardFourViewSet(viewsets.ViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'

class CardFiveViewSet(viewsets.ViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'

class CardSixViewSet(viewsets.ViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'


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
