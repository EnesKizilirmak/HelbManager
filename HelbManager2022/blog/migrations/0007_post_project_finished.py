# Generated by Django 4.1.4 on 2023-01-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_collaborators_alter_post_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project_finished',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
