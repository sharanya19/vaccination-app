from rest_framework import viewsets
from .models import Location, Centre, Patient, VaccinationSlot,AddedRecord
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LocationSerializer, CentreSerializer, PatientSerializer, VaccinationSlotSerializer, AddedRecordSerializer
from rest_framework.permissions import IsAuthenticated

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class CentreViewSet(viewsets.ModelViewSet):
    queryset = Centre.objects.all() 
    serializer_class = CentreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']

    def get_queryset(self):
        queryset = Centre.objects.all()
        location_id = self.request.query_params.get('location', None)
        
        if location_id:
            try:
                location_id = int(location_id)
                queryset = queryset.filter(location_id=location_id)
            except ValueError:
                # Handle invalid location_id
                queryset = Centre.objects.none()  # Returns an empty queryset

        return queryset
    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class VaccinationSlotViewSet(viewsets.ModelViewSet):
    queryset = VaccinationSlot.objects.all()
    serializer_class = VaccinationSlotSerializer
    permission_classes = [IsAuthenticated]


class AddedRecordViewSet(viewsets.ModelViewSet):
    queryset = AddedRecord.objects.all()
    serializer_class = AddedRecordSerializer
    permission_classes = [IsAuthenticated]
  
