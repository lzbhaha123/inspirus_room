# Generated by Django 3.2.12 on 2022-04-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='create_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.CharField(max_length=50),
        ),
    ]