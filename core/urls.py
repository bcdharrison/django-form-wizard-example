from django.urls import path
from core.views import StaffDetailFormView, PerformanceOneFormView, PerformanceTwoFormView, index, success

urlpatterns = [
    path('', index, name='index'),
    path('staff_detail/', StaffDetailFormView.as_view(), name='staff_detail'),
    path('performance_one/', PerformanceOneFormView.as_view(), name='performance_one'),
    path('performance_two/', PerformanceTwoFormView.as_view(), name='performance_two'),
    path('success/', success, name='success')
]