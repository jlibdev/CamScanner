# Generated by Django 5.1.6 on 2025-02-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScannedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='scanned/')),
                ('processed_image', models.ImageField(upload_to='proccessed/')),
            ],
        ),
    ]
