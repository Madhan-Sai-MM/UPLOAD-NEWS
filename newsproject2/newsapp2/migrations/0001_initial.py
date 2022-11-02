# Generated by Django 4.0.1 on 2022-03-19 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='madhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(max_length=1000)),
                ('add_image', models.ImageField(null=True, upload_to='images/')),
                ('video', models.FileField(null=True, upload_to='videos/')),
                ('status', models.CharField(choices=[('SRIKAKULAM', 'Srikakulam'), ('VISHAKAPATNAM', 'Vishakapatnam'), ('VIZIANAGARAM', 'Vizianagaram'), ('EAST-GODAVARI', 'East Godavari'), ('WEST-GODAVARI', 'West Godavari'), ('KRISHNA', 'Krishna'), ('GUNTUR', 'Guntur'), ('PRAKASAM', 'Prakasam'), ('NELLORE', 'Nellore'), ('KURNOOL', 'Kurnool'), ('ANANTAPUR', 'Anantapur'), ('KADAPA', 'Kadapa'), ('CHITTOOR', 'Chittoor')], max_length=20, verbose_name='Course')),
            ],
        ),
    ]