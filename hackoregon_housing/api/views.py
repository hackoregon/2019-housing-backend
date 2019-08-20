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
        black_proportion_filter = float(request.GET.get('1990-black-pop-proportion-floor', '0'))

        portland_rows = NcdbSampleYearly.objects.filter(metroname="Portland-Vancouver-Hillsboro, OR-WA").select_related('fips_code').order_by('year')

        years = set(row.year for row in portland_rows)
        response = {year : {"white" : 0, "black": 0, "hisp": 0, "asoth": 0} for year in years}
        skips = []

        for row in portland_rows:
            print(row.year)
            if row.fips_code.geo_fips in skips:
                continue

            blackshare = row.blackshare
            if blackshare is None:
                blackshare = 0

            if( row.year == 1990 and (blackshare * 0.01) < black_proportion_filter):
                skips.append(row.fips_code.geo_fips)
                continue
            else:
                print('Black share: ' + str(blackshare * 0.01))
                print('Filter: ' + str(black_proportion_filter))

            pop = row.tractpopulation
            if pop is None:
                pop = 0
            whiteshare = row.whiteshare
            if whiteshare is None:
                whiteshare = 0
            hispshare = row.hispshare
            if hispshare is None:
                hispshare = 0
            asothshare = row.asothshare
            if asothshare is None:
                asothshare = 0
            response[row.year]["white"] += (pop * whiteshare * 0.01)
            response[row.year]["black"] += (pop * blackshare * 0.01)
            response[row.year]["hisp"] += (pop * hispshare * 0.01)
            response[row.year]["asoth"] += (pop * asothshare * 0.01)

        for year in years:
            response[year]["white"] = round(response[year]["white"])
            response[year]["black"] = round(response[year]["black"])
            response[year]["hisp"] = round(response[year]["hisp"])
            response[year]["asoth"] = round(response[year]["asoth"])

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