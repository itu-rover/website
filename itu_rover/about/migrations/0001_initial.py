# Generated by Django 2.0.1 on 2020-05-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('detail', models.TextField(verbose_name='detail')),
                ('image', models.ImageField(blank=True, upload_to='images/about')),
                ('eng_title', models.CharField(default='eng', max_length=50, verbose_name='eng_title')),
                ('eng_detail', models.TextField(default='eng', verbose_name='eng_detail')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
