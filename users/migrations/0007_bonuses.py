# Generated by Django 2.2.10 on 2020-04-13 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20200213_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.IntegerField(verbose_name='Колличество')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Бонусы',
                'ordering': ['date'],
            },
        ),
    ]
