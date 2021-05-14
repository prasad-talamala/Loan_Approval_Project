from django.db import models


class UserEnquiry(models.Model):
    JOB_CHOICES = (
        ('SE', 'Self Employed'),
        ('SL', 'Salaried'),
    )

    enquiry_id = models.CharField(blank=False, max_length=10)
    customer_name = models.CharField(max_length=100, blank=False)
    job_type = models.CharField(choices=JOB_CHOICES, max_length=100)
    loan_amount = models.IntegerField(blank=False)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    status = models.CharField(max_length=100, default="Pending")
