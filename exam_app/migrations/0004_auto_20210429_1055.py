# Generated by Django 2.2.4 on 2021-04-29 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_auto_20210429_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='upload_by',
            new_name='added_by',
        ),
    ]
