# Generated by Django 4.0.3 on 2022-03-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
