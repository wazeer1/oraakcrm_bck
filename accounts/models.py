from django.db import models
from main.models import *
from django.utils import timezone
import uuid

USER_TYPES = (
    ('admin', 'Admin'),
    ('user', 'User'),
)

USER_ROLES = (
    ('employee', 'Employee'),
    ('admin', 'Admin'),
    ('hr', 'HR'),
    ('accounts', 'Accounts')
)

class UserProfile(BaseModel):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=125, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    user_role = models.CharField(max_length=155,choices=USER_ROLES, blank=True, null=True)
    password = models.TextField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    active_plan = models.BooleanField(default=False)

    class Meta:
        db_table = "user_profile"  
        verbose_name = "User profile"
        verbose_name_plural = "User Profiles"
        ordering = ['date_added']


class Services(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='services/', blank=True, null=True)  

    class Meta:
        db_table = "services"  
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['date_added']


class Plans(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)  # changed to IntegerField
    description = models.TextField(max_length=255, blank=True, null=True)
    services = models.ManyToManyField(Services, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "plans" 
        verbose_name = "Plan"
        verbose_name_plural = "Plans"
        ordering = ['date_added']


class UserPlans(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    expire = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "user_plans"  
        verbose_name = "User Plan"
        verbose_name_plural = "User Plans"
        ordering = ['date_added']

    def save(self, *args, **kwargs):
        if not self.expire and self.start_date and self.plan and self.plan.duration:
            self.expire = self.start_date + timezone.timedelta(days=self.plan.duration)
        super().save(*args, **kwargs)
