# Generated by Django 5.1.5 on 2025-02-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourvalue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/our-value'),
        ),
    ]
