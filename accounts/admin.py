from django.contrib import admin
from .models import UserProfile, Services, Plans, UserPlans

# UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'user_type', 'user_role', 'is_active', 'active_plan')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('user_type', 'user_role', 'is_active', 'active_plan')
    ordering = ['date_added']

# Services Admin
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ['date_added']

# Plans Admin
class PlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    ordering = ['date_added']

# UserPlans Admin
class UserPlansAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'expire', 'is_active')
    search_fields = ('user__full_name', 'plan__name')
    list_filter = ('is_active', 'start_date', 'expire')
    ordering = ['date_added']

# Register the models with admin site
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Plans, PlansAdmin)
admin.site.register(UserPlans, UserPlansAdmin)
