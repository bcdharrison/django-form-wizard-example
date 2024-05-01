from django import forms
from core.models import Staff, PerformanceOne, PerformanceTwo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML, Fieldset, Div, Column, Row



class StaffDetailForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'email', 'position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()


class PerformanceOneForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
            
    class Meta:
        model = PerformanceOne
        exclude = ('staff',)
        fields = (
            'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'
                )
        labels = {
            'q1': 'How well do you think you are doing on the job?',
            'q2': 'Which parts of your job are doing well and where do you think you could improve?',
            'q3': 'Is there any equipment or training to help you in your role?',
            'q4': 'How do you feel about your job and the company?',
            'q5': 'What would you change if you could?',
            'q6': 'What are your achievable goals for the next 12 months?',
            'q7': 'Are you aware of what you need to do to achieve these goals?',
            'q8': 'Do you feel you have achieved the goals you set last year?',
            'q9': 'Explain how you have or why you have managed to achieve these goals',
        }

class PerformanceTwoForm(forms.ModelForm):

    class Meta:
        model = PerformanceTwo
        exclude = ('staff',)
        fields = '__all__'
        widgets = {
            'reliability_and_time_management': forms.RadioSelect(),
            'attitude_and_effort': forms.RadioSelect(),
            'knowledge_and_skill_improvement': forms.RadioSelect(),
            'health_and_safety': forms.RadioSelect(),
            'teamwork': forms.RadioSelect(),
            'customer_service': forms.RadioSelect(),
            'working_under_pressure': forms.RadioSelect(),
            'reliability_and_time_management_comment': forms.Textarea(),
            'attitude_and_effort_comment': forms.Textarea(),
            'knowledge_and_skill_improvement_comment': forms.Textarea(),
            'health_and_safety_comment': forms.Textarea(),
            'teamwork_comment': forms.Textarea(),
            'customer_service_comment': forms.Textarea(),
            'working_under_pressure_comment': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                Row(
                    Field(''),
                    Field('')
                ),
                Row(
                    Field('reliability_and_time_management', wrapper_class='form-group col-md-6 mb-20'),
                    Field('reliability_and_time_management_comment', wrapper_class='form-group col-md-6 mb-20')
                ),
                Row(
                    Field('attitude_and_effort', wrapper_class='form-group col-md-6 mb-20'),
                    Field('attitude_and_effort_comment', wrapper_class='form-group col-md-6 mb-20'),
                ),
                Row(
                    Field('knowledge_and_skill_improvement', wrapper_class='form-group col-md-6 mb-20'),
                    Field('knowledge_and_skill_improvement_comment', wrapper_class='form-group col-md-6 mb-20'),
                ),
                Row(
                    Field('health_and_safety', wrapper_class='form-group col-md-6 mb-20'),
                    Field('health_and_safety_comment', wrapper_class='form-group col-md-6 mb-20'),
                ),
                Row(
                    Field('teamwork', wrapper_class='form-group col-md-6 mb-20'),
                    Field('teamwork_comment', wrapper_class='form-group col-md-6 mb-20'),
                ),
                Row(
                    Field('customer_service', wrapper_class='form-group col-md-6 mb-20'),
                    Field('customer_service_comment', wrapper_class='form-group col-md-6 mb-20'),
                ),
                Row(
                    Field('working_under_pressure', wrapper_class='form-group col-md-6 mb-20'),
                    Field('working_under_pressure_comment', wrapper_class='form-group col-md-6 mb-20'),
                ),
            ),
            Div(
                Submit('submit', u'Submit', css_class='btn btn-lg'),
                css_class="row justify-content-center",
            )
        )
        self.helper.form_method = 'POST'


        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field, forms.ChoiceField):
                field.choices = list(field.choices)[1:]
        for field in self.fields.values():
            field.required = True