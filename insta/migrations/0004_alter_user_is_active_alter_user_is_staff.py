# Generated by Django 4.2 on 2023-04-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_alter_user_is_active_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
