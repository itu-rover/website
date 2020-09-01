# Generated by Django 2.0.1 on 2020-06-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('form_link', models.TextField(verbose_name='Link of the join form:')),
            ],
        ),
        migrations.CreateModel(
            name='SupportForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('form_link', models.TextField(verbose_name='Link of the support form:')),
            ],
        ),
        migrations.AlterField(
            model_name='contactform_model',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-Mail adresiniz:'),
        ),
        migrations.AlterField(
            model_name='contactform_model',
            name='name',
            field=models.CharField(max_length=120, verbose_name='İsminiz, Soyisminiz:'),
        ),
        migrations.AlterField(
            model_name='contactform_model',
            name='text',
            field=models.TextField(verbose_name='Mesajınız:'),
        ),
    ]
