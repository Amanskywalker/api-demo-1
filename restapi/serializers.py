# Serializer for the models
from .models import Banks, Branches
from rest_framework import serializers


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name']


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']
