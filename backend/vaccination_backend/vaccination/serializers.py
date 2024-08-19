from rest_framework import serializers
from .models import Location, Centre, Patient, VaccinationSlot,AddedRecord

class VaccinationSlotSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = VaccinationSlot
        fields = ['id', 'type', 'date', 'time', 'available_slots', 'patient']

    def create(self, validated_data):
        return VaccinationSlot.objects.create(**validated_data)

class PatientSerializer(serializers.ModelSerializer):
    vaccination_slots = VaccinationSlotSerializer(many=True, read_only=True)
    centre = serializers.PrimaryKeyRelatedField(queryset=Centre.objects.all())

    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'age', 'gender', 'centre', 'vaccination_slots']

    def create(self, validated_data):
        return Patient.objects.create(**validated_data)

class CentreSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(many=True, read_only=True)
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

    class Meta:
        model = Centre
        fields = ['id', 'name', 'address', 'location', 'patient_details']

    def create(self, validated_data):
        return Centre.objects.create(**validated_data)

class LocationSerializer(serializers.ModelSerializer):
    centres = CentreSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'country', 'state', 'city', 'centres']

class AddedRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddedRecord
        fields = '__all__'        
