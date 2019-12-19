from django.urls import path, include

from .v1.router import urlpatterns as v1_patterns


urlpatterns = [
   path("", include((v1_patterns, "v1"), namespace="default")),
   path("v1/", include((v1_patterns, "v1"), namespace="v1")),
]
