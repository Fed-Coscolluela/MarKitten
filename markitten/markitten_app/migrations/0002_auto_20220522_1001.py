# Generated by Django 3.2.2 on 2022-05-22 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markitten_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(default='Male/Female', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]