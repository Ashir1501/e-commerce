# Generated by Django 4.2.7 on 2024-01-23 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_key',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
