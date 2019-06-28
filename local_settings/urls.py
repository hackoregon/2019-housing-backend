from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

api_title = 'Hack Oregon Housing 2019 API'

schema_view = get_swagger_view(title=api_title)


urlpatterns = [
    url(r'^housing/schema/', schema_view),
    url(r'^housing/civic/', include('hackoregon_housing.civic.urls')),
    url(r'^housing/docs/', include_docs_urls(title=api_title)),
]
