# Generated by Django 4.0.1 on 2022-04-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp2', '0009_delete_category_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madhan',
            name='news',
            field=models.TextField(max_length=1000),
        ),
    ]
