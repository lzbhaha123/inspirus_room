# Generated by Django 3.2.12 on 2022-05-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_featurelisttofeature_feature_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='picture',
            field=models.CharField(default='', max_length=50),
        ),
    ]
