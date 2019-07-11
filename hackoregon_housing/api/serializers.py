from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans
from rest_framework import serializers

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
