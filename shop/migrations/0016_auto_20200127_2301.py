# Generated by Django 2.2.6 on 2020-01-27 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20200127_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['id'], 'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
    ]
