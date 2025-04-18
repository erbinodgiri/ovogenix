# Generated by Django 4.2.11 on 2025-04-10 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HatcheryMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the hatchery machine (e.g., Incubator A)', max_length=100)),
                ('machine_id', models.CharField(help_text='Unique identifier for the machine', max_length=50, unique=True)),
                ('location', models.CharField(help_text='Location within the hatchery', max_length=100)),
                ('assigned_staff', models.ManyToManyField(help_text='Staff assigned to monitor this machine', related_name='assigned_machines', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='Hatchery client who owns this machine', on_delete=django.db.models.deletion.CASCADE, related_name='hatchery_machines', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hatchery Machine',
                'verbose_name_plural': 'Hatchery Machines',
            },
        ),
        migrations.CreateModel(
            name='MachineObservationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField(help_text='Temperature in Celsius')),
                ('humidity', models.FloatField(help_text='Humidity in percentage')),
                ('turning', models.BooleanField(default=False, help_text='Whether the eggs were turned')),
                ('entered_by', models.ForeignKey(help_text='Staff who entered this data', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='machine_observations', to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observation_data', to='machine_observation_data.hatcherymachine')),
            ],
            options={
                'verbose_name': 'Machine Observation Data',
                'verbose_name_plural': 'Machine Observation Data',
            },
        ),
    ]
