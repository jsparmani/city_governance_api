# Generated by Django 2.1.7 on 2019-10-17 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='department.Department'),
            preserve_default=False,
        ),
    ]