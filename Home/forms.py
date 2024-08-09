from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'bookingdate':DateInput(),
        }
        labels={
            'pname':"patient name",
            'pphone':"patient phone",
            'pemail':"patient email",
            'docname':"docter name",
            'bookingdate':"booking date"

        }