from django.shortcuts import render

# views.py
from rest_framework import viewsets
from students.models import Student, State, City, Subject, PreviousSchool
from students.serializers import StudentSerializer, StateSerializer, CitySerializer, SubjectSerializer, PreviousSchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
    def get_queryset(self):
        queryset = City.objects.all()
        state_id = self.request.query_params.get('state', None)
        if state_id is not None:
            queryset = queryset.filter(state_id=state_id)
        return queryset

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PreviousSchoolViewSet(viewsets.ModelViewSet):
    queryset = PreviousSchool.objects.all()
    serializer_class = PreviousSchoolSerializer

# class StateViewSet(viewsets.ModelViewSet):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer

# class CityViewSet(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


    