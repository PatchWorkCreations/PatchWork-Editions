# Generated by Django 4.2.11 on 2024-09-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='benefits',
            field=models.TextField(blank=True, help_text='Separate each benefit with a new line.', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='how_it_works',
            field=models.TextField(blank=True, help_text='Explain how this service works.', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='the_patchwork/images/services/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]