# Generated by Django 2.0.1 on 2020-05-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_sliderimage_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='place',
            field=models.SmallIntegerField(default=0),
        ),
    ]
