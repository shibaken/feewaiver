# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-27 05:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feewaiver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalUserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('what', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(blank=True, max_length=256, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=256, null=True)),
                ('postal_address', models.CharField(blank=True, max_length=256, null=True)),
                ('suburb', models.CharField(blank=True, max_length=256, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('organisation_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetailsDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('_file', models.FileField(null=True, upload_to='')),
                ('can_delete', models.BooleanField(default=True)),
                ('contact_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_details_documents', to='feewaiver.ContactDetails')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetailsLogDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('_file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetailsLogEntry',
            fields=[
                ('communicationslogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feewaiver.CommunicationsLogEntry')),
                ('approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comms_logs', to='feewaiver.ContactDetails')),
            ],
            bases=('feewaiver.communicationslogentry',),
        ),
        migrations.CreateModel(
            name='FeeWaiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_waiver_purpose', models.TextField(blank=True)),
                ('fee_waiver_description', models.TextField(blank=True)),
                ('date_from', models.DateField(null=True, verbose_name='Date from')),
                ('date_to', models.DateField(null=True, verbose_name='Date to')),
                ('number_of_vehicles', models.IntegerField()),
                ('age_of_participants', models.CharField(blank=True, choices=[('15', 'Under 15 yrs'), ('24', '15-24 yrs'), ('25', '25-39 yrs'), ('40', '40-59 yrs'), ('60', '60 yrs and over')], max_length=100, null=True, verbose_name='Age of Participants')),
                ('contact_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fee_waivers', to='feewaiver.ContactDetails')),
            ],
        ),
        migrations.AlterField(
            model_name='usersystemsettings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='system_settings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contactdetailslogdocument',
            name='log_entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='feewaiver.ContactDetailsLogEntry'),
        ),
        migrations.AddField(
            model_name='approvaluseraction',
            name='contact_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_logs', to='feewaiver.ContactDetails'),
        ),
        migrations.AddField(
            model_name='approvaluseraction',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
