"""housingapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'card_one', views.CardOneViewSet.as_view())
router.register(r'card_two', views.CardTwoViewSet)
router.register(r'card_three', views.CardThreeViewSet)
router.register(r'card_four', views.CardFourViewSet)
router.register(r'card_five', views.CardFiveViewSet)
router.register(r'card_six', views.CardSixViewSet)
router.register(r'ncdbsampleyearly', views.NcdbSampleYearlyViewSet)
router.register(r'ncdbsamplechanges', views.NcdbSampleChangesViewSet)
router.register(r'fipsrecords', views.FIPSRecordsViewSet)
router.register(r'hmdaorwa', views.HmdaOrwaViewSet)
router.register(r'totalloans', views.TotalLoansViewSet)

schema_view = get_swagger_view(title='Housing API')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', schema_view)
]

# router = routers.DefaultRouter()
# router.register(r'ncdbsampleyearly', views.NcdbSampleYearlyViewSet)
# router.register(r'ncdbsamplechanges', views.NcdbSampleChangesViewSet)
