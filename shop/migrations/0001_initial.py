# Generated by Django 4.0.2 on 2022-02-15 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('sale', models.BooleanField(default=False)),
                ('brand', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('availability', models.BooleanField(default=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.image')),
            ],
        ),
    ]
