# Generated by Django 2.1.5 on 2019-03-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_profile_is_profile_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='study_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
