# Generated by Django 3.1.7 on 2021-03-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20210326_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='alert_type',
            field=models.CharField(choices=[('danger', 'Critical'), ('success', 'Success'), ('warning', 'Warning'), ('primary', 'Info')], default='danger', max_length=10),
            preserve_default=False,
        ),
    ]
