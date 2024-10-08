# Generated by Django 4.2.11 on 2024-09-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_service_benefits_service_how_it_works_service_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
