# Generated by Django 3.0.3 on 2020-08-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200825_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
