# Generated by Django 2.0.1 on 2020-06-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
