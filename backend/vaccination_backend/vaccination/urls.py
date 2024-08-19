from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, CentreViewSet, PatientViewSet, VaccinationSlotViewSet, AddedRecordViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'centres', CentreViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'vaccination-slots', VaccinationSlotViewSet)
router.register(r'added-records', AddedRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
