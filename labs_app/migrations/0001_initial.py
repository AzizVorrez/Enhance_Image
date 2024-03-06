# Generated by Django 5.0.3 on 2024-03-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('enhanced_image', models.ImageField(blank=True, null=True, upload_to='enhanced_images/')),
            ],
        ),
    ]
