# Generated by Django 4.1.2 on 2022-12-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_extenduser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
