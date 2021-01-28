from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    is_doctor = models.BooleanField(default=True)
    off_days = models.ManyToManyField('OffDays')
    appointments = models.ManyToManyField(
        'Appointments', related_name='doctor_bookings')

    def __str__(self):
        return self.person


class Patient(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=True)
    appointment = models.ForeignKey(
        'Appointments', on_delete=models.CASCADE, related_name='my_appointments')

    def __str__(self):
        return self.person


class OffDays(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return self.date


class Appointments(models.Model):
    patient = models.ForeignKey(
        'Patient', on_delete=models.CASCADE, related_name='patient')
    subject = models.CharField(max_length=255)
    issue = models.TextField()
    time = models.DateTimeField()
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='booked_doctor')

    def __str__(self):
        return self.subject
