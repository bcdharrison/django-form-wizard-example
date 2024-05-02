from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    created_at_nz = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class PerformanceOne(models.Model):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    q1 = models.TextField(default="")
    q2 = models.TextField(default="")
    q3 = models.TextField(default="")
    q4 = models.TextField(default="")
    q5 = models.TextField(default="")
    q6 = models.TextField(default="")
    q7 = models.TextField(default="")
    q8 = models.TextField(default="")
    q9 = models.TextField(default="")


    
class PerformanceTwo(models.Model):
    class CHOICES(models.TextChoices):
        Unsatifactory = "Unsatifactory"
        Below_Expectations = "Below Expectations"
        Meets_Expectations = "Meets Expectations"
        Exceeds_Expectations = "Exceeds Expectations"
        Outstanding = "Outstanding"

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    reliability_and_time_management = models.CharField(max_length=100, choices=CHOICES, blank=True)
    attitude_and_effort = models.CharField(max_length=100, choices=CHOICES, blank=True)
    knowledge_and_skill_improvement = models.CharField(max_length=100, choices=CHOICES, blank=True)
    health_and_safety = models.CharField(max_length=100, choices=CHOICES, blank=True)
    teamwork = models.CharField(max_length=100, choices=CHOICES, blank=True)
    customer_service = models.CharField(max_length=100, choices=CHOICES, blank=True)
    working_under_pressure = models.CharField(max_length=100, choices=CHOICES, blank=True)

    reliability_and_time_management_comment = models.CharField(max_length=10000, blank=True)
    attitude_and_effort_comment = models.CharField(max_length=10000, blank=True)
    knowledge_and_skill_improvement_comment = models.CharField(max_length=10000, blank=True)
    health_and_safety_comment = models.CharField(max_length=10000, blank=True)
    teamwork_comment = models.CharField(max_length=10000, blank=True)
    customer_service_comment = models.CharField(max_length=10000, blank=True)
    working_under_pressure_comment = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return f"{self.staff.full_name}: Completed"