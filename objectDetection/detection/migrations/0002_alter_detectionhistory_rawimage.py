# Generated by Django 3.2 on 2021-09-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectionhistory',
            name='rawImage',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]