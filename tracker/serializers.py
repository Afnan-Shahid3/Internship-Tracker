from rest_framework import serializers

from .models import Company, Application, Interview, Contact

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'location', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'company', 'position', 'date_applied', 'status', 'notes']


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['id', 'application', 'interview_date', 'round_name', 'feedback']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'company', 'name', 'role', 'email', 'linkedin']