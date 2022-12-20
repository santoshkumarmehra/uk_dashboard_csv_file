# Generated by Django 4.1.4 on 2022-12-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segment',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ukcompany',
            name='Total_Funding',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
