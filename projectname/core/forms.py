from django import forms
from django.utils import timezone
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('service', 'stylist', 'start_time', 'notes')

    def __init__(self, member, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = self.fields['service'].queryset.filter(active=True)
        self.fields['stylist'].queryset = self.fields['stylist'].queryset.filter(user__is_active=True)
        self.fields['start_time'].widget.attrs.update({'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['stylist'].widget.attrs.update({'class': 'form-control'})
        self.member = member

    def clean_start_time(self):
        start_time = self.cleaned_data['start_time']
        if start_time < timezone.now():
            raise forms.ValidationError('The start time cannot be in the past.')
        if self.member.appointment_set.filter(start_time=start_time).exists():
            raise forms.ValidationError('You already have an appointment scheduled at that time.')
        return start_time

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.member = self.member
        if commit:
            instance.save()
        return instance
