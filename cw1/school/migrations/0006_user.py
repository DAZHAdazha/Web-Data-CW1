# Generated by Django 4.0.3 on 2022-03-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_rating_professor_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]