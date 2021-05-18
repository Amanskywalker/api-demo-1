"""server URL Configuration"""

from django.urls import include, path
from rest_framework import routers
from restapi import views

urlpatterns = [
    path('api/branches', views.BranchView.as_view()),
    path('api/branches/autocomplete', views.BranchAutocompleteView.as_view()),
]
