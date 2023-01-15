# Generated by Django 4.1.4 on 2023-01-15 12:57

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, validators=[users.validators.check_birth_date], verbose_name='Дата рождения'),
        ),
    ]
