# Generated by Django 3.1.7 on 2021-03-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_rule_function_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='function_name',
            field=models.CharField(max_length=50),
        ),
    ]