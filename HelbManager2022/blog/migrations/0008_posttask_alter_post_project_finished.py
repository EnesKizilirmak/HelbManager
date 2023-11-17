# Generated by Django 4.1.4 on 2023-01-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_project_finished'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='project_finished',
            field=models.BooleanField(default=False),
        ),
    ]