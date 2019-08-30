from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans, MedianHouseholdIncomeByRace2017, RaceByTenure1990T2017, Tl201041Tabblock10, ResidentialBuildingPermitData
from rest_framework import serializers

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
