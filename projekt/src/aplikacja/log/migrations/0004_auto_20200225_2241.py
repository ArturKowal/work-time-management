# Generated by Django 3.0.3 on 2020-02-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20200217_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='when_in',
            field=models.DateTimeField(verbose_name='Kiedy'),
        ),
    ]
