from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords, HmdaOrwa, TotalLoans, MedianHouseholdIncomeByRace2017, RaceByTenure1990T2017, Tl201041Tabblock10, ResidentialBuildingPermitData, HomeInflationKriging, MultnomahHomeOwnershipByRace, PortlandHomeAppreciationAnnuallySince1990Ish, Sc2HmdaApprovalByRace2013T2017, MedianHouseholdIncomeByRace1990T2017Msa, HolcPortlandRedlining, TractToNeighborhoodPdx, PortlandHomeOwnershipByRace
from rest_framework_gis import serializers

class HolcPortlandRedliningSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = HolcPortlandRedlining
        geo_field = 'geometry'
        fields = "__all__" # TODO: replace with individual fields

class Sc2HmdaApprovalByRace2013T2017Serializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Sc2HmdaApprovalByRace2013T2017
        geo_field = 'geometry'
        fields = "__all__" # TODO: replace with individual fields

class TractToNeighborhoodPdxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractToNeighborhoodPdx
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

class NcdbSampleYearlySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = NcdbSampleYearly
        geo_field = 'tract_geom'
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

class TotalLoansSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TotalLoans
        geo_field = 'tract_geom'
        fields = "__all__" # TODO: replace with individual fields

class MedianHouseholdIncomeByRace2017Serializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = MedianHouseholdIncomeByRace2017
        geo_field = 'tract_geom'
        fields = "__all__" # TODO: replace with individual fields

class RaceByTenure1990T2017Serializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RaceByTenure1990T2017
        geo_field = 'tract_geom'
        fields = "__all__" # TODO: replace with individual fields

class Tl201041Tabblock10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tl201041Tabblock10
        geo_field = 'wkb_geometry'
        fields = "__all__" # TODO: replace with individual fields

class PortlandHomeOwnershipByRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortlandHomeOwnershipByRace
        fields = "__all__" # TODO: replace with individual fields
