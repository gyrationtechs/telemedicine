from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Doctor, Patient, Appointments, OffDays


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['url', 'person', 'is_doctor', 'off_days', 'appointments']


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['url', 'person', 'is_patient', 'appointment']


class AppointmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointments
        fields = ['url', 'patient', 'subject', 'issue', 'time', 'doctor']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
