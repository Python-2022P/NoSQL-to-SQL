# Generated by Django 4.2.1 on 2023-05-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=255)),
                ('img_url', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('memory', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
    ]
