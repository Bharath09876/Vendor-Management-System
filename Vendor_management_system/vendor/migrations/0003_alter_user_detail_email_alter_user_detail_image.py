# Generated by Django 4.2.7 on 2023-12-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_user_detail_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='image',
            field=models.ImageField(default='null', upload_to='user_images'),
        ),
    ]
