# Generated by Django 4.0.2 on 2022-02-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyFeedback', '0007_remove_weeklysliders_question_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklysliders',
            name='form_field',
            field=models.CharField(max_length=200, verbose_name='algins_this_to_a_form'),
        ),
    ]
