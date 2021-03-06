# Generated by Django 3.2.7 on 2021-09-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='picture_height', max_length=255, upload_to='pictures/', width_field='picture_width')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
