# Generated by Django 4.0.2 on 2022-02-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyFeedback', '0008_alter_weeklysliders_form_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='namesample',
            name='slider_value',
        ),
        migrations.AddField(
            model_name='namesample',
            name='q1',
            field=models.IntegerField(blank=True, null=True, verbose_name='slider value'),
        ),
        migrations.AddField(
            model_name='namesample',
            name='q2',
            field=models.IntegerField(blank=True, null=True, verbose_name='slider value'),
        ),
        migrations.AddField(
            model_name='namesample',
            name='q3',
            field=models.IntegerField(blank=True, null=True, verbose_name='slider value'),
        ),
    ]
