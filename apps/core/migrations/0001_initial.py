# Generated by Django 3.0.1 on 2019-12-19 13:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='number')),
                ('seats', models.PositiveIntegerField(verbose_name='seats number')),
                ('shape', models.CharField(choices=[('rectangle', 'Rectangle'), ('oval', 'Oval')], max_length=20, verbose_name='shape')),
                ('position_x', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='table position in the room X - % related to the room length')),
                ('position_y', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='table position in the room Y - % related to the room width')),
                ('length', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='table length in % related to the room length')),
                ('width', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='table width in % related to the room width')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Table', verbose_name='table')),
            ],
        ),
    ]
