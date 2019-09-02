from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans, MedianHouseholdIncomeByRace2017, RaceByTenure1990T2017, Tl201041Tabblock10, ResidentialBuildingPermitData, HomeInflationKriging, MultnomahHomeOwnershipByRace, PortlandHomeAppreciationAnnuallySince1990Ish, Sc2HmdaApprovalByRace2013T2017, MedianHouseholdIncomeByRace1990T2017Msa
from rest_framework_gis import serializers

class Sc2HmdaApprovalByRace2013T2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sc2HmdaApprovalByRace2013T2017
        fields = "__all__" # TODO: replace with individual fields

class MedianHouseholdIncomeByRace1990T2017MsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedianHouseholdIncomeByRace1990T2017Msa
        fields = "__all__" # TODO: replace with individual fields

class MultnomahHomeOwnershipByRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultnomahHomeOwnershipByRace
        fields = "__all__" # TODO: replace with individual fields

class PortlandHomeAppreciationAnnuallySince1990IshSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortlandHomeAppreciationAnnuallySince1990Ish
        fields = "__all__" # TODO: replace with individual fields

class HomeInflationKrigingSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = HomeInflationKriging
        geo_field = 'geometry'
        fields = "__all__" # TODO: replace with individual fields

class ResidentialBuildingPermitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialBuildingPermitData
        fields = "__all__" # TODO: replace with individual fields

class NcdbSampleYearlySerializer(serializers.ModelSerializer):
    class Meta:
        model = NcdbSampleYearly
        fields = "__all__" # TODO: replace with individual fields

class NcdbSampleChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcdbSampleChanges
        fields = "__all__" # TODO: replace with individual fields

class FIPSRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIPSRecords
        fields = "__all__" # TODO: replace with individual fields

class HmdaOrwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmdaOrwa
        fields = "__all__" # TODO: replace with individual fields

class TotalLoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalLoans
        fields = "__all__" # TODO: replace with individual fields

class MedianHouseholdIncomeByRace2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = MedianHouseholdIncomeByRace2017
        fields = "__all__" # TODO: replace with individual fields

class RaceByTenure1990T2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = RaceByTenure1990T2017
        fields = "__all__" # TODO: replace with individual fields

class Tl201041Tabblock10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tl201041Tabblock10
        fields = "__all__" # TODO: replace with individual fields
