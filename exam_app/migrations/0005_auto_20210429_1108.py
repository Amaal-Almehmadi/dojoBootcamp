# Generated by Django 2.2.4 on 2021-04-29 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0004_auto_20210429_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='created_at',
            new_name='added_at',
        ),
    ]