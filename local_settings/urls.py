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
# from django.contrib import admin
# from django.urls import include, path, url
# from rest_framework import exceptions
# from api import views
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.routers import DefaultRouter

from django.conf.urls import include, url
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from api import views

router = DefaultRouter()

class JSONOpenAPIRender(renderers.OpenAPIRenderer):
    media_type = "application/json"

def get_swagger_view(title=None, url=None, patterns=None, urlconf=None):
    """
    Returns schema view which renders Swagger/OpenAPI.
    """

    class SwaggerSchemaView(APIView):
        _ignore_model_permissions = True
        exclude_from_schema = True
        permission_classes = [AllowAny]
        renderer_classes = [
            CoreJSONRenderer,
            JSONOpenAPIRender,
            renderers.OpenAPIRenderer,
            renderers.SwaggerUIRenderer,
        ]

        def get(self, request):
            generator = SchemaGenerator(
                title=title, url=url, patterns=patterns, urlconf=urlconf
            )
            schema = generator.get_schema(request=request)

            if not schema:
                raise exceptions.ValidationError(
                    "The schema generator did not return a schema Document"
                )

            return Response(schema)

    return SwaggerSchemaView.as_view()

api_title = 'Hack Oregon Housing 2019 API'

schema_view = get_swagger_view(title=api_title)

urlpatterns = [
    url(r"housing2019/v1/schema/", schema_view),
    url(r'housing2019/v1/api/portland-metro-tract-population-by-race', views.CardOneView.as_view()),
    url(
        r"housing2019/v1/api/",
        include("hackoregon_housing.api.urls"),
    ),
        url(r'^housing2019/v1/docs/', include_docs_urls(title=api_title)),
        url(r'^housing2019/v1/health/', include('health_check.urls'))
]

url(r'^$', schema_view)
