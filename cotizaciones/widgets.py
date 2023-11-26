from django.forms import DateInput
class FenChenDatePickerInput(DateInput):
    template_name = 'widgets/fenchen_datepicker.html'
