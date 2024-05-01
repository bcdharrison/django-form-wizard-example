from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class PerformanceOne(models.Model):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    how_well_do_you_think_you_are_doing_on_the_job = models.TextField(default="")
    which_parts_of_your_job_are_doing_well_and_where_do_you_think_you_could_improve = models.TextField(default="")
    is_there_any_equipment_or_training_to_help_you_in_your_role = models.TextField(default="")
    how_do_you_feel_about_your_job_and_the_company = models.TextField(default="")
    what_would_you_change_if_you_could = models.TextField(default="")
    what_are_your_achievable_goals_for_the_next_12_months = models.TextField(default="")
    are_you_aware_of_what_you_need_to_do_to_achieve_these_goals = models.TextField(default="")
    do_you_feel_you_have_achieved_the_goals_you_set_last_year = models.TextField(default="")
    explain_how_you_have_or_why_you_have_managed_to_achieve_these_goals = models.TextField(default="")


    
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