# Generated by Django 2.2.6 on 2020-01-27 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200127_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['-name'], 'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
    ]