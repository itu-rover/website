# Generated by Django 2.0.1 on 2020-02-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_auto_20200201_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='did_work',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='eng_description',
            field=models.CharField(blank=True, max_length=75, verbose_name='english description (e.g. department)'),
        ),
        migrations.AlterField(
            model_name='member',
            name='eng_working',
            field=models.TextField(blank=True, null=True, verbose_name='english working experiences'),
        ),
    ]
