# Generated by Django 4.0.1 on 2022-03-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp2', '0002_madhan_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='madhan',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]