# Generated by Django 3.2.7 on 2021-09-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
