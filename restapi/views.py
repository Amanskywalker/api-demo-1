from django.db.models import Q

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import filters

from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    ordering = ['name']

class BranchView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    ordering = ['ifsc']

    def filter_queryset(self, queryset):
        if self.request.query_params.get('q'):
            queryset = queryset.filter(
                Q(branch__icontains=self.request.query_params.get('q')) |
                Q(address__icontains=self.request.query_params.get('q')) |
                Q(city__icontains=self.request.query_params.get('q')) |
                Q(district__icontains=self.request.query_params.get('q')) |
                Q(state__icontains=self.request.query_params.get('q'))
            )

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)

        return queryset

class BranchAutocompleteView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    ordering = ['ifsc']

    def filter_queryset(self, queryset):
        if self.request.query_params.get('q'):
            queryset = queryset.filter(
                Q(branch__icontains=self.request.query_params.get('q'))
            )

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)

        return queryset
