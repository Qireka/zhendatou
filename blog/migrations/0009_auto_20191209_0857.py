# Generated by Django 2.2.6 on 2019-12-09 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_readnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogType'),
        ),
    ]
