# Generated by Django 5.0.4 on 2024-04-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='details',
            field=models.TextField(null=True),
        ),
    ]
