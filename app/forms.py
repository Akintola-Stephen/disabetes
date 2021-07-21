from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name',  'email', 'dob', 'gender', 'pregnancy',
                  'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'pedigree', 'age')
