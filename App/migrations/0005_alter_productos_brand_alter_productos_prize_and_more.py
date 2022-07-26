# Generated by Django 4.0.5 on 2022-07-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_rename_num_local_locales_mall_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='brand',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Select'), (1, 'Apple'), (2, 'Samsung'), (3, 'Huawei'), (4, 'Sony')], verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='prize',
            field=models.FloatField(verbose_name='Prize $'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
    ]
