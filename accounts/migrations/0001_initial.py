# Generated by Django 5.1.2 on 2024-10-17 13:33

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, editable=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='services/')),
                ('creator', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'db_table': 'services',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, editable=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('services', models.ManyToManyField(blank=True, to='accounts.services')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
                'db_table': 'plans',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, editable=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=125, null=True)),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10)),
                ('user_role', models.CharField(blank=True, choices=[('employee', 'Employee'), ('admin', 'Admin'), ('hr', 'HR'), ('accounts', 'Accounts')], max_length=155, null=True)),
                ('password', models.TextField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('active_plan', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': 'User Profiles',
                'db_table': 'user_profile',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='UserPlans',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, editable=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('start_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('expire', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.plans')),
                ('updater', models.ForeignKey(blank=True, editable=False, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_%(app_label)s_%(class)s_objects', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
            options={
                'verbose_name': 'User Plan',
                'verbose_name_plural': 'User Plans',
                'db_table': 'user_plans',
                'ordering': ['date_added'],
            },
        ),
    ]