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

urlpatterns = [
    url(r'^', include(router.urls)),
]
