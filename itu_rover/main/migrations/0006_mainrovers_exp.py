# Generated by Django 2.0.1 on 2019-11-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191123_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainrovers',
            name='exp',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
