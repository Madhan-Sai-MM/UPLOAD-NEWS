# Generated by Django 4.0.1 on 2022-03-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp2', '0004_alter_madhan_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madhan',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
