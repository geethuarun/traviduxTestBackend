# serializers.py
from rest_framework import serializers
from .models import Student, State, City, Subject, PreviousSchool

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class PreviousSchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PreviousSchool
        fields = '__all__'

# class StudentSerializer(serializers.ModelSerializer):
    # state=serializers.SlugRelatedField(read_only=True,slug_field="name")
    # city=serializers.SlugRelatedField(read_only=True,slug_field="name")
    # subjects=serializers.SlugRelatedField(read_only=True,slug_field="name")
    # class Meta:
    #     model = Student
    #     fields = ['first_name','last_name','date_of_birth','email','address','state','city','pincode','subjects']



class StudentSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    subjects = serializers.SlugRelatedField(
        many=True,
        queryset=Subject.objects.all(),
        slug_field='name'
    )
    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        slug_field='name'
    )
    state = serializers.SlugRelatedField(
        queryset=State.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Student
        fields = ['id','first_name', 'last_name', 'date_of_birth', 'email', 'address', 'state', 'city', 'pincode', 'subjects']

    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects')
        city_data = validated_data.pop('city')
        state_data = validated_data.pop('state')

        student = Student.objects.create(**validated_data)

        student.city = city_data
        student.state = state_data

        for subject_name in subjects_data:
            subject, _ = Subject.objects.get_or_create(name=subject_name)
            student.subjects.add(subject)

        return student
