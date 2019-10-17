# Generated by Django 2.1.7 on 2019-10-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.PositiveIntegerField()),
                ('department_name', models.CharField(max_length=255)),
                ('department_description', models.TextField()),
                ('department_head_name', models.CharField(max_length=255)),
                ('department_head_phone', models.PositiveIntegerField()),
                ('department_email', models.EmailField(max_length=254)),
            ],
        ),
    ]