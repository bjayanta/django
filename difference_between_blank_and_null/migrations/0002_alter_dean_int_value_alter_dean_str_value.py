# Generated by Django 4.0.3 on 2022-03-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('difference_between_blank_and_null', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dean',
            name='int_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dean',
            name='str_value',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
