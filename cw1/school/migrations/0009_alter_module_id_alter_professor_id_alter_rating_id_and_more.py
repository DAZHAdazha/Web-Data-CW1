# Generated by Django 4.0.3 on 2022-03-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_user_id_alter_module_uid_alter_module_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
