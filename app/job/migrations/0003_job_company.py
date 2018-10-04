# Generated by Django 2.0.7 on 2018-10-01 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_company_name'),
        ('job', '0002_job_post_local_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='company.Company'),
        ),
    ]
