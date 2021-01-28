from django.contrib import admin
from .models import Doctor, Patient, OffDays, Appointments


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['person', ]
    list_filter = ('off_days',)


class PatientAdmin(admin.ModelAdmin):
    list_display = ['appointment']
    list_filter = ('appointment',)


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['patient', 'subject', 'time', 'doctor']
    list_filter = ('patient',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(OffDays)
admin.site.register(Appointments, AppointmentsAdmin)
