# Generated by Django 2.2.6 on 2019-12-31 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='image',
            field=models.ImageField(default='', upload_to='background'),
        ),
        migrations.AddField(
            model_name='tool',
            name='url',
            field=models.URLField(default=''),
        ),
    ]