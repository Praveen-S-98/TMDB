# Generated by Django 3.0.3 on 2020-08-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
