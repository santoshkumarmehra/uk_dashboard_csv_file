# Generated by Django 4.1.4 on 2022-12-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfile', '0007_alter_ukcompany_total_funding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ukcompany',
            name='Total_Funding',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]