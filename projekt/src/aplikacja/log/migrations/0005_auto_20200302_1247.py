# Generated by Django 3.0.3 on 2020-03-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20200225_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='when_in',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Kiedy'),
        ),
    ]
