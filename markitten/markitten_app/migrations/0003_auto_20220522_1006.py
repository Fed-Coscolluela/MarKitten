# Generated by Django 3.2.2 on 2022-05-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markitten_app', '0002_auto_20220522_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='billing_address',
            field=models.CharField(default='House No., Street Address, City, State', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='citizenship',
            field=models.CharField(default='Filipino', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='landline_number',
            field=models.CharField(default='09xx xxx xxxx', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(default='09xx xxx xxxx', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(default='Filipino', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='office_address',
            field=models.CharField(default='House No., Street Address, City, State', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='office_number',
            field=models.CharField(default='09xx xxx xxxx', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='permanent_address',
            field=models.CharField(default='House No., Street Address, City, State', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='present_address',
            field=models.CharField(default='House No., Street Address, City, State', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='shopping_address',
            field=models.CharField(default='House No., Street Address, City, State', max_length=100),
        ),
    ]