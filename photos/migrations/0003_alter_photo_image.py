# Generated by Django 3.2.7 on 2021-09-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, height_field='picture_height', max_length=255, null=True, upload_to='images/', width_field='picture_width'),
        ),
    ]
