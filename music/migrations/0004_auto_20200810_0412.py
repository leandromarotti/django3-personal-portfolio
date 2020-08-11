# Generated by Django 3.0.7 on 2020-08-10 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200803_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='portfolio/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='music',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]