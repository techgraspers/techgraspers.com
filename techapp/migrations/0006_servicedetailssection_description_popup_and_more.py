# Generated by Django 5.1 on 2024-09-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0005_servicedetailssection'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetailssection',
            name='description_popup',
            field=models.TextField(default='Default description', null=True),
        ),
        migrations.AlterField(
            model_name='servicedetailssection',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
