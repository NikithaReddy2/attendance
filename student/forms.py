from django import forms
from student.models import studentModel


class formName(forms.ModelForm):
    class Meta():
        model = studentModel
        fields = '__all__'
