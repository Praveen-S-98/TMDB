# Generated by Django 3.0.3 on 2020-08-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200828_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
