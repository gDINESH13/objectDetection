# Generated by Django 3.2 on 2021-09-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0002_alter_detectionhistory_rawimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectionhistory',
            name='resImage',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
