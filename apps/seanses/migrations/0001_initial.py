# Generated by Django 4.1 on 2023-05-16 14:54

import apps.movies.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemas', '0002_alter_cinema_city_alter_cinema_location'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(verbose_name='Уникальный UUID')),
                ('barcode', models.ImageField(upload_to=apps.movies.utils.upload_instance, verbose_name='Баркод')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.CreateModel(
            name='Seanse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('start_time', models.TimeField(verbose_name='Время начало')),
                ('end_time', models.TimeField(verbose_name='Время конца')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinemas.hall', verbose_name='Зал')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.movie', verbose_name='Фильм')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seanses.schedule', verbose_name='Расписание')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеансы',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seanse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seanses.seanse', verbose_name='Сеанс')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinemas.seat', verbose_name='Место')),
                ('ticket', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='seanses.ticket', verbose_name='Билет')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
    ]
