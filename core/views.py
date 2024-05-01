from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from core.forms import StaffDetailForm, PerformanceOneForm, PerformanceTwoForm
from django.http import HttpResponse
from django.urls import reverse_lazy
import logging


logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'core/index.html')

def success(request):
    return render(request, 'core/success.html')

class StaffDetailFormView(FormView):
    form_class = StaffDetailForm
    template_name = 'core/staff_detail_form.html'
    success_url = '/performance_one'

    def form_valid(self, form):
        self.request.session['staff_detail_form_data'] = form.cleaned_data
        return super().form_valid(form)

class PerformanceOneFormView(FormView):
    form_class = PerformanceOneForm
    template_name = 'core/performance_one_form.html'
    success_url = '/performance_two'

    def form_valid(self, form):
        self.request.session['performance_one_form_data'] = form.cleaned_data
        return super().form_valid(form)

class PerformanceTwoFormView(FormView):
    form_class = PerformanceTwoForm
    template_name = 'core/performance_two_form.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        staff_detail_form = StaffDetailForm(self.request.session.get('staff_detail_form_data', {}))
        performance_one_form = PerformanceOneForm(self.request.session.get('performance_one_form_data', {}))

        if staff_detail_form.is_valid() and performance_one_form.is_valid():
            staff = staff_detail_form.save()
            performance_one = performance_one_form.save(commit=False)
            performance_one.staff = staff
            performance_one.save()
            performance_two = form.save(commit=False)
            performance_two.staff = staff
            performance_two.save()

            # Clear the session data
            self.request.session.pop('staff_detail_form_data', None)
            self.request.session.pop('performance_one_form_data', None)

            return super().form_valid(form)
        else:
            # Handle the case where the forms are not valid
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Log the form errors instead of printing them
        logger.error(form.errors)
        return super().form_invalid(form)
    