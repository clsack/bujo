# Generated by Django 2.0 on 2018-01-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailylog', '0005_auto_20171228_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
