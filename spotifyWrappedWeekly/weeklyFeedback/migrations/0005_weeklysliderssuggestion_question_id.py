# Generated by Django 4.0.2 on 2022-02-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyFeedback', '0004_weeklysliders_weeklysliderssuggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklysliderssuggestion',
            name='question_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='unique_id_for_a_question'),
        ),
    ]
