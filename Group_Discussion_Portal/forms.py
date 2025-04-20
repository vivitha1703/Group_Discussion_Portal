from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['event_name', 'student_name', 'email_id', 'attended_date', 'overall_marks', 'remarks']
