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
                  'how_well_do_you_think_you_are_doing_on_the_job',
                  'which_parts_of_your_job_are_doing_well_and_where_do_you_think_you_could_improve',
                  'is_there_any_equipment_or_training_to_help_you_in_your_role',
                  'how_do_you_feel_about_your_job_and_the_company',
                  'what_would_you_change_if_you_could',
                  'what_are_your_achievable_goals_for_the_next_12_months',
                  'are_you_aware_of_what_you_need_to_do_to_achieve_these_goals',
                  'do_you_feel_you_have_achieved_the_goals_you_set_last_year',
                  'explain_how_you_have_or_why_you_have_managed_to_achieve_these_goals',
                )

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