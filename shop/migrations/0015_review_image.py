# Generated by Django 4.2.3 on 2023-08-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to='media_rev/images'),
        ),
    ]
