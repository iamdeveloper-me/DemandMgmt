# Generated by Django 2.0.7 on 2018-09-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180924_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(default='', max_length=2000),
        ),
    ]