# Generated by Django 5.1.6 on 2025-02-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='event',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='event',
            name='meta_title',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
