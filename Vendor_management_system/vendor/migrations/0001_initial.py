# Generated by Django 4.2.7 on 2023-12-22 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Address', models.TextField(max_length=500)),
                ('Phone_number', models.TextField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('image', models.ImageField(upload_to='user_images')),
            ],
        ),
    ]
