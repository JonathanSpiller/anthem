# Generated by Django 3.1.7 on 2021-03-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_alert_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='function_name',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
