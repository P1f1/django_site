# Generated by Django 4.2.3 on 2023-08-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
