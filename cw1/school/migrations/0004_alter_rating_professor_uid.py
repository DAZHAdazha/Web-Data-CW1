# Generated by Django 4.0.3 on 2022-03-15 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rating_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='professor_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.professor'),
        ),
    ]
