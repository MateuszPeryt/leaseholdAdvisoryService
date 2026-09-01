from django.urls import path

from .views import triage

urlpatterns = [path("triage/", triage, name="triage")]

