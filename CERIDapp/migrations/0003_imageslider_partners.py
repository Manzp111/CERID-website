# Generated by Django 5.2 on 2025-04-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CERIDapp', '0002_leaderteam_description_alter_leaderteam_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/imgSlider/')),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/partner/')),
            ],
        ),
    ]
