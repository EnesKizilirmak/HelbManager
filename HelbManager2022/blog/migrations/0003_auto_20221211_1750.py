# Generated by Django 3.2.16 on 2022-12-11 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='subtask',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content2',
            new_name='task',
        ),
    ]
