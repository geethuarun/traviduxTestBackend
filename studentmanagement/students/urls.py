# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet, StateViewSet, CityViewSet, SubjectViewSet, PreviousSchoolViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'previous-schools', PreviousSchoolViewSet)

urlpatterns = [

]+router.urls
