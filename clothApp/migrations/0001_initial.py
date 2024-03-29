# Generated by Django 4.2.7 on 2023-11-28 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_image', models.ImageField(default=None, upload_to='product_images')),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Both')], max_length=30)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothApp.category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
