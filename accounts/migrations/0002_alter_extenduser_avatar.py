# Generated by Django 4.1.2 on 2022-11-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
