# Generated by Django 5.1 on 2024-09-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0003_faqsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetailsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('page_link', models.CharField(max_length=1000)),
                ('button_link', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
