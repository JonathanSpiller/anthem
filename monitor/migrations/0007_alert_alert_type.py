# Generated by Django 3.1.7 on 2021-03-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_rule_alert_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='alert_type',
            field=models.CharField(default='x', max_length=10),
            preserve_default=False,
        ),
    ]
