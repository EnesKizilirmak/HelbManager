# Generated by Django 3.2.16 on 2022-12-30 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_date_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_limit',
            new_name='deadline',
        ),
    ]