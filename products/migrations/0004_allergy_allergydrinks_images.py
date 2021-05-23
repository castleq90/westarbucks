# Generated by Django 3.2.3 on 2021-05-23 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_drinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'products_allergy',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=500)),
                ('Drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
            options={
                'db_table': 'products_image',
            },
        ),
        migrations.CreateModel(
            name='AllergyDrinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('Drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
            options={
                'db_table': 'products_allergydrinks',
            },
        ),
    ]