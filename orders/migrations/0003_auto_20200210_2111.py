# Generated by Django 2.2.6 on 2020-02-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200210_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='Почтовый индекс'),
        ),
    ]
