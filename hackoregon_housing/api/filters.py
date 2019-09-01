from django_filters import rest_framework as filters
from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans, MedianHouseholdIncomeByRace2017, RaceByTenure1990T2017, Tl201041Tabblock10, ResidentialBuildingPermitData, HomeInflationKriging, MultnomahHomeOwnershipByRace, PortlandHomeAppreciationAnnuallySince1990Ish
import coreapi
from django_filters import Filter, NumberFilter
from django_filters.fields import Lookup
from django_filters.rest_framework import DjangoFilterBackend

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class MultnomahHomeOwnershipByRaceFilter(filters.FilterSet):

    class Meta:
        model = MultnomahHomeOwnershipByRace
        fields = '__all__'

class PortlandHomeAppreciationAnnuallySince1990IshFilter(filters.FilterSet):

    class Meta:
        model = PortlandHomeAppreciationAnnuallySince1990Ish
        fields = '__all__'

class HomeInflationKrigingFilter(filters.FilterSet):

    class Meta:
        model = HomeInflationKriging
        fields = '__all__'

class ResidentialBuildingPermitDataFilter(filters.FilterSet):

    class Meta:
        model = ResidentialBuildingPermitData
        fields = '__all__'

class NcdbSampleChangesFilter(filters.FilterSet):

    class Meta:
        model = NcdbSampleChanges
        fields = '__all__'

class NcdbSampleYearlyFilter(filters.FilterSet):

    year = NumberInFilter(field_name='year', lookup_expr='in')

    class Meta:
        model = NcdbSampleYearly
        fields = '__all__'

class FIPSRecordsFilter(filters.FilterSet):

    class Meta:
        model = FIPSRecords
        fields = '__all__'

class HmdaOrwaFilter(filters.FilterSet):

    class Meta:
        model = HmdaOrwa
        fields = '__all__'

class TotalLoansFilter(filters.FilterSet):

    class Meta:
        model = TotalLoans
        fields = '__all__'

class MedianHouseholdIncomeByRace2017Filter(filters.FilterSet):

    class Meta:
        model = MedianHouseholdIncomeByRace2017
        fields = "__all__" # TODO: replace with individual fields

class RaceByTenure1990T2017Filter(filters.FilterSet):

    class Meta:
        model = RaceByTenure1990T2017
        fields = "__all__" # TODO: replace with individual fields

class Tl201041Tabblock10Filter(filters.FilterSet):

    class Meta:
        model = Tl201041Tabblock10
        fields = "__all__" # TODO: replace with individual fields
