# Generated by Django 3.1.2 on 2020-12-01 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0002_auto_20201202_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]