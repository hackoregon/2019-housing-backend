from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r'ncdbsampleyearly', views.NcdbSampleYearlyViewSet, basename="ncdb-sample-yearly")
router.register(r'ncdbsamplechanges', views.NcdbSampleChangesViewSet, basename="ncdb-sample-changes")
router.register(r'fipsrecords', views.FIPSRecordsViewSet, basename="fips-records")
router.register(r'hmdaorwa', views.HmdaOrwaViewSet, basename="hmda-orwa")
router.register(r'totalloans', views.TotalLoansViewSet, basename="total-loans")
router.register(r'medianhouseholdinecomebyrace2017', views.MedianHouseholdIncomeByRace2017ViewSet, basename="median-household-income-by-race-2017")
router.register(r'racebytenure1990t2017', views.RaceByTenure1990T2017ViewSet, basename="race-by-tenure-1990-t-2017")
router.register(r'tl201041tabblock10', views.Tl201041Tabblock10ViewSet, basename="tl-2010-41-tab-block-10")
router.register(r'residentialbuildingpermitdata', views.ResidentialBuildingPermitDataViewSet, basename="residential-building-permit-data")
router.register(r'homeinflationkriging', views.HomeInflationKrigingViewSet, basename="home-inflation-kriging")
router.register(r'multnomahhomeownershipbyrace', views.MultnomahHomeOwnershipByRaceViewSet, basename="multnomah-home-ownership-by-race")
router.register(r'portlandhomeappreciationannuallysince1990ish', views.PortlandHomeAppreciationAnnuallySince1990IshViewSet, basename="portland-home-appreciation-annually-since-1990-ish")
router.register(r'sc2hmdaapprovalbyrace2013t2017', views.Sc2HmdaApprovalByRace2013T2017ViewSet, basename="sc2-hmda-approval-by-race-2013t2017")
router.register(r'medianhouseholdincomebyrace1990t2017msa', views.MedianHouseholdIncomeByRace1990T2017MsaViewSet, basename="median-household-income-by-race-2017")

router.register(r'holcportlandredlining', views.HolcPortlandRedliningViewSet, basename="holc-portland-redlining")



urlpatterns = [
    url(r'^', include(router.urls)),
]
