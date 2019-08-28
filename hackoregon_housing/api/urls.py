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

urlpatterns = [
    url(r'^', include(router.urls)),
]
