from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Centre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = models.ForeignKey(Location, related_name='centres', on_delete=models.CASCADE, null=True, blank=True)

class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    centre = models.ForeignKey(Centre, related_name='patient_details', on_delete=models.CASCADE, null=True, blank=True)

class VaccinationSlot(models.Model):
    type = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    available_slots = models.IntegerField()
    patient = models.ForeignKey(Patient, related_name='vaccination_slots', on_delete=models.CASCADE, null=True, blank=True)


class AddedRecord(models.Model):
    location = models.CharField(max_length=255)
    locationState = models.CharField(max_length=255)
    locationCountry = models.CharField(max_length=255)
    centre = models.CharField(max_length=255)
    centreAddress = models.CharField(max_length=255)
    patient = models.CharField(max_length=255)
    patientAge = models.CharField(max_length=10)
    patientContact = models.CharField(max_length=255)
    slot = models.CharField(max_length=255)
    slotDate = models.DateField()
    slotTime = models.TimeField()
    availableSlots = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location} - {self.centre} - {self.patient}"