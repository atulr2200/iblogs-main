# Generated by Django 3.0.5 on 2023-10-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231009_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=1, verbose_name=''),
            preserve_default=False,
        ),
    ]
