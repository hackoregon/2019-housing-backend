from django_filters import rest_framework as filters
from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans

class NcdbSampleChangesFilter(filters.FilterSet):
    # fips_code = filters.ModelChoiceFilter(FIPSRecords.objects.all())
    # start_year = filters.NumberFilter()
    # end_year = filters.NumberFilter()
    # TODO: allow filtering by less than or equal to or more than or equal to for other fields?

    class Meta:
        model = NcdbSampleChanges
        fields = '__all__'

class NcdbSampleYearlyFilter(filters.FilterSet):
    # fips_code = filters.ModelChoiceFilter(FIPSRecords.objects.all())
    # year = filters.NumberFilter(field_name='year', lookup_expr='iexact')
    # TODO: allow filtering by less than or equal to or more than or equal to for other fields?

    class Meta:
        model = NcdbSampleYearly
        fields = '__all__'

class FIPSRecordsFilter(filters.FilterSet):
    # fips_code = filters.ModelChoiceFilter(FIPSRecords.objects.all())
    # year = filters.NumberFilter(field_name='year', lookup_expr='iexact')
    # TODO: allow filtering by less than or equal to or more than or equal to for other fields?

    class Meta:
        model = FIPSRecords
        fields = '__all__'

class HmdaOrwaFilter(filters.FilterSet):
    # fips_code = filters.ModelChoiceFilter(FIPSRecords.objects.all())
    # year = filters.NumberFilter(field_name='year', lookup_expr='iexact')
    # TODO: allow filtering by less than or equal to or more than or equal to for other fields?

    class Meta:
        model = HmdaOrwa
        fields = '__all__'

class TotalLoansFilter(filters.FilterSet):
    # fips_code = filters.ModelChoiceFilter(FIPSRecords.objects.all())
    # year = filters.NumberFilter(field_name='year', lookup_expr='iexact')
    # TODO: allow filtering by less than or equal to or more than or equal to for other fields?

    class Meta:
        model = TotalLoans
        fields = '__all__'
