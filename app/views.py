# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Person
import numpy as np
import joblib



def index(request):
    context = {}
    records_count = Person.objects.count()
    diabetic_count = Person.objects.filter(predicted_result=1).count()
    non_diabetic_count = Person.objects.filter(predicted_result=0).count()
    male_count = Person.objects.filter(gender="Male").count()
    female_count = Person.objects.filter(gender="Female").count()

    female_precent_count = ( female_count / records_count ) * 100
    male_precent_count =  100 - female_precent_count

    context = {'records_count': records_count,
               'diabetic_count': diabetic_count,
               'non_diabetic_count': non_diabetic_count,
               'male_count': male_count,
               'female_count': female_count,
               'female_precent_count': round(female_precent_count,2),
               'male_precent_count': round(male_precent_count,2)
               }

    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def diagnosis(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.email = request.POST.get("mail")
        person.dob = request.POST.get("dob")
        person.gender = request.POST.get("gender")
        person.pregnancy = request.POST.get("Pregnancies")
        person.glucose = request.POST.get("Glucose")
        person.blood_pressure = request.POST.get("BloodPressure")
        person.skin_thickness = request.POST.get("SkinThickness")
        person.insulin = request.POST.get("Insulin")
        person.bmi = request.POST.get("BMI")
        person.pedigree = request.POST.get("DiabetesPedigreeFunction")
        person.age = request.POST.get("Age")

        ml_pickled_model = "../django-datta-able-master/app/ml model.pkl"

        person_data = np.array(
            [
                [
                    person.pregnancy,  person.glucose, person.blood_pressure,
                    person.skin_thickness, person.insulin, person.bmi,
                    person.pedigree, person.age
                ]
            ]
        ).reshape(1, 8)

        test_model = joblib.load(open(ml_pickled_model, 'rb'))
        prediction = test_model.predict(person_data)
        person.predicted_result = prediction[0]

        person.save()
        return redirect("result_list")
    return render(request, 'ui-forms.html', {'form': 'context'})


def result_list(request):
    person = Person()
    all_records = Person.objects.all()
    diabetic = Person.objects.filter(predicted_result=1)
    non_diabetic = Person.objects.filter(predicted_result=0)
    print(diabetic)
    print(all_records)
    context = {'all_records': all_records,
               'diabetic': diabetic, 'non_diabetic': non_diabetic}
    return render(request, 'ui-tables.html', context)
