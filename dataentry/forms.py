from django import forms
from django.forms import fields

from .models import marks

# creating a model form


def checkStringLength(arr):
    for i in arr:
        # print(i)
        if len(i) != 1:
            return False
    return True


class markform(forms.ModelForm):
    '''Model form, we dont need to declare our fields' types'''

    grades = forms.CharField()
    credits = forms.CharField()

    class Meta:
        model = marks
        fields = ['name',
                  'registrationNumber',
                  'grades',
                  'credits'
                  ]

    def clean_grades(self, *args, **kwargs):
        grades = self.cleaned_data.get('grades')

        print(grades)
        if not checkStringLength(grades.split(',')):
            raise forms.ValidationError('Please give comma separated input')
        return grades

    def clean_credits(self, *args, **kwargs):
        credits = self.cleaned_data.get('credits')
        print(credits)
        if not checkStringLength(credits.split(',')):
            raise forms.ValidationError('Please give comma separated input')
        return credits


class rawForm(forms.Form):
    '''The long way of creating a form and saving data through it'''
    name = forms.CharField()
    registrationNumber = forms.CharField()
    grades = forms.CharField()
    credits = forms.CharField()
