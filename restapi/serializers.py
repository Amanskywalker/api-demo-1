# Serializer for the models
from .models import Bank, Branch
from rest_framework import serializers

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']
